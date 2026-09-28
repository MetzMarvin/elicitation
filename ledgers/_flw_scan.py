# -*- coding: utf-8 -*-
"""Page scan for the Flowable census (docs + marketing + training + flowfest).

For every enumerated frontier URL it records one JSON object:
  st       http status (int) or 'ERR:<msg>'
  t        <title>
  len      visible-text length of the main content
  text     visible text of the main content (first 7000 chars, whitespace collapsed)
  ai       [{kw, ctx}] - windows around AI/LLM/agent keywords, for quoting evidence
  pre      [snippet] - <pre>/<code> blocks naming BPMN elements or connectors
  files    [href]    - downloadable .bpmn/.dmn/.cmmn/.zip/.form targets
  imgs     [{u,w,alt}] - <img> sources (absolute; largest srcset candidate)
  bgs      [url]     - CSS url() background images (absolute)
  svg      [class]   - distinct djs-*/bjs-*/bpmn* class names on <svg> roots
  viewer   [marker]  - bpmn-js / djs-element / bpmn.io markers
  src      which sitemap group the url came from

Input : ledgers/flowable.frontier.txt
Output: ledgers/flowable.raw/scan.json   (resumable: skips urls already scanned)
Paced ~1 request/second (CLAUDE.md rule 10).
"""
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'flowable.raw')
FRONTIER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'flowable.frontier.txt')
OUT = os.path.join(RAW, 'scan.json')
UA = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/124.0 Safari/537.36 (research; master-thesis elicitation, read-only)',
      'Accept-Language': 'en-US,en;q=0.9,de;q=0.8'}

STRONG = re.compile(
    r'(?<![A-Za-z])(AI|GPT|LLM|OpenAI|Anthropic|Claude|LangChain|MCP|agent\w*|agentic|'
    r'machine learning|embedding|vector store|prompt|chatbot|copilot|robot\w*|RAG|KI|'
    r'künstliche|Artificial Intelligence|Mistral|Ollama|Bedrock|Gemini|Llama|Hugging Face|'
    r'generative|GenAI|A2A|inference|fine-tun\w+|guardrail\w*|hallucinat\w+)(?![A-Za-z])', re.I)
BPMNISH = re.compile(
    r'(bpmn:|serviceTask|userTask|exclusiveGateway|connectorId|camunda:|zeebe:|\.bpmn|'
    r'element template|aiAgent|ai-agent|AgentTask|bpmn2?)', re.I)
IMGEXT = re.compile(r'\.(png|jpe?g|webp|gif|svg)(\?|$)', re.I)

GROUP = {}


def group_of(u):
    if u.startswith('https://documentation.flowable.com/'):
        return 'docs_ent'
    if u.startswith('https://training.flowable.com/'):
        return 'training'
    if 'flowfest.flowable.com' in u:
        return 'flowfest'
    if u.startswith('https://flowable.com/open-source/') or u.startswith('https://www.flowable.com/open-source/'):
        return 'os_docs'
    return 'marketing'


def strip(s):
    return re.sub(r'(?is)<(script|style|noscript|svg)\b.*?</\1>', ' ', s)


def text_of(h):
    for pat in (r'(?is)<article\b.*?</article>', r'(?is)<main\b.*?</main>',
                r'(?is)<div[^>]*class="[^"]*(?:theme-doc-markdown|markdown)[^"]*"[^>]*>.*?</div>',
                r'(?is)<body\b.*?</body>'):
        m = re.search(pat, h)
        if m and len(m.group(0)) > 400:
            s = m.group(0)
            break
    else:
        s = h
    s = strip(s)
    s = re.sub(r'(?is)<br\s*/?>|</p>|</div>|</li>|</h[1-6]>|</td>|</tr>', '\n', s)
    s = re.sub(r'(?s)<[^>]+>', ' ', s)
    s = html.unescape(s)
    s = re.sub(r'[ \t\x0b\f\r]+', ' ', s)
    s = re.sub(r'\n\s*\n+', '\n', s)
    return s.strip()


def absolutize(u, base):
    u = u.strip()
    if not u or u.startswith('data:'):
        return None
    if u.startswith('//'):
        return 'https:' + u
    if u.startswith('/'):
        m = re.match(r'(https?://[^/]+)', base)
        return (m.group(1) if m else '') + u
    if u.startswith('http'):
        return u
    return base.rsplit('/', 1)[0] + '/' + u


def scan(h, url, status):
    rec = {'st': status, 'src': group_of(url)}
    m = re.search(r'(?is)<title[^>]*>(.*?)</title>', h)
    rec['t'] = html.unescape(re.sub(r'\s+', ' ', m.group(1)).strip()) if m else ''
    body = strip(h)

    pre = []
    for m in re.finditer(r'(?is)<(pre|code)\b[^>]*>(.*?)</\1>', body):
        s = html.unescape(re.sub(r'(?s)<[^>]+>', '', m.group(2)))
        s = re.sub(r'\s+', ' ', s).strip()
        if s and BPMNISH.search(s) and len(s) > 20:
            pre.append(s[:400])
    rec['pre'] = sorted(set(pre))[:6]

    rec['files'] = sorted(set(
        absolutize(x, url) for x in re.findall(r'href="([^"]+\.(?:bpmn|dmn|cmmn|zip|form|xml))"', body, re.I))-{None})[:15]

    imgs = []
    seen = set()
    for m in re.finditer(r'<img\b[^>]*>', body, re.I):
        tag = m.group(0)
        sm = re.search(r'\bsrc="([^"]+)"', tag, re.I)
        if not sm:
            continue
        u = absolutize(sm.group(1), url)
        if not u or not IMGEXT.search(u):
            continue
        sset = re.search(r'\bsrcset="([^"]+)"', tag, re.I)
        if sset:
            cands = []
            for part in sset.group(1).split(','):
                part = part.strip().split()
                if not part:
                    continue
                w = 0
                if len(part) > 1:
                    wm = re.match(r'(\d+)w', part[1])
                    w = int(wm.group(1)) if wm else 0
                cands.append((w, part[0]))
            if cands:
                u2 = absolutize(max(cands)[1], url)
                if u2:
                    u = u2
        alt = re.search(r'\balt="([^"]*)"', tag, re.I)
        key = u
        if key in seen:
            continue
        seen.add(key)
        imgs.append({'u': u, 'alt': html.unescape(alt.group(1))[:120] if alt else ''})
    rec['imgs'] = imgs[:60]

    bgs = set()
    for m in re.finditer(r'url\((["\']?)([^)"\']+)\1\)', body):
        u = absolutize(m.group(2), url)
        if u and IMGEXT.search(u):
            bgs.add(u)
    rec['bgs'] = sorted(bgs)[:40]

    cls = set()
    for m in re.finditer(r'(?is)<svg\b[^>]*class="([^"]*)"', body):
        for c in m.group(1).split():
            if c.startswith(('djs', 'bjs', 'bpmn')):
                cls.add(c)
    rec['svg'] = sorted(cls)[:20]
    v = [mk for mk in ('djs-element', 'djs-shape', 'djs-connection', 'data-element-id',
                       'bpmn-js', 'bpmn.io', 'bpmnjs', 'bpmn-modeler') if mk in body]
    rec['viewer'] = v

    art = re.search(r'(?is)<article\b.*?</article>', body)
    if art and len(art.group(0)) > 400:
        txt = text_of(art.group(0))
    else:
        txt = text_of(h)
    rec['len'] = len(txt)
    rec['text'] = txt[:7000]

    ais = []
    seenk = set()
    for m in STRONG.finditer(txt):
        a, b = max(0, m.start() - 110), min(len(txt), m.end() + 150)
        ctx = re.sub(r'\s+', ' ', txt[a:b]).strip()
        k = ctx[:60]
        if k in seenk:
            continue
        seenk.add(k)
        ais.append({'kw': m.group(0), 'ctx': ctx})
        if len(ais) >= 25:
            break
    rec['ai'] = ais
    rec['ai_n'] = len(STRONG.findall(txt))
    return rec


def main():
    urls = [l.strip() for l in open(FRONTIER, encoding='utf-8') if l.strip()]
    if os.path.exists(OUT):
        data = json.load(open(OUT, encoding='utf-8'))
    else:
        data = {}
    lo = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    hi = int(sys.argv[2]) if len(sys.argv) > 2 else len(urls)
    todo = [u for i, u in enumerate(urls) if lo <= i < hi and u not in data]
    print(f'frontier={len(urls)} scanned={len(data)} todo={len(todo)}', flush=True)
    n = 0
    for u in todo:
        n += 1
        try:
            req = urllib.request.Request(u, headers=UA)
            with urllib.request.urlopen(req, timeout=35) as r:
                raw = r.read()
                ct = r.headers.get('Content-Type', '')
                st = r.status
            if 'html' not in ct:
                data[u] = {'st': st, 'src': group_of(u), 't': '', 'len': 0, 'text': '',
                           'ai': [], 'ai_n': 0, 'pre': [], 'files': [], 'imgs': [],
                           'bgs': [], 'svg': [], 'viewer': [], 'nonhtml': ct}
            else:
                data[u] = scan(raw.decode('utf-8', 'replace'), u, st)
        except urllib.error.HTTPError as e:
            data[u] = {'st': e.code, 'src': group_of(u), 't': '', 'len': 0, 'text': '',
                       'ai': [], 'ai_n': 0, 'pre': [], 'files': [], 'imgs': [], 'bgs': [],
                       'svg': [], 'viewer': []}
        except Exception as e:  # noqa: BLE001
            data[u] = {'st': f'ERR:{type(e).__name__}:{e}', 'src': group_of(u), 't': '', 'len': 0,
                       'text': '', 'ai': [], 'ai_n': 0, 'pre': [], 'files': [], 'imgs': [],
                       'bgs': [], 'svg': [], 'viewer': []}
        if n % 20 == 0:
            json.dump(data, open(OUT, 'w', encoding='utf-8'))
            print(f'  {n}/{len(todo)} last={u[:90]} ai={data[u]["ai_n"]}', flush=True)
        time.sleep(0.55)
    json.dump(data, open(OUT, 'w', encoding='utf-8'))
    print('DONE', len(data), flush=True)


if __name__ == '__main__':
    main()
