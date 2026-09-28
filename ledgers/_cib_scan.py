# -*- coding: utf-8 -*-
"""Deep page scan for the CIB seven census (both hosts).

For every enumerated page it records, as one JSON object:
  t        <title>
  url      page url
  len      visible-text length of the main content
  text     visible text of the main content (first 6000 chars, whitespace collapsed)
  ai       [{kw, ctx}]  - windows around AI/LLM/agent keywords, for quoting evidence
  pre      [snippet]    - <pre>/<code> blocks that name BPMN elements or connectors
  files    [href]       - downloadable .bpmn/.dmn/.cmmn/.zip targets
  imgs     [src]        - <img> sources (as written)
  bgs      [url]        - CSS url() background images
  svg      [class]      - distinct class names on <svg> roots (djs-* = rendered bpmn-js)
  viewer   [marker]     - hits for bpmn-js / djs-element / bpmn.io / modeler embed markers

Input : ledgers/cib-seven.raw/nav_latest.txt   (docs)  + ledgers/cib-seven.raw/mkt_pages.json (keys)
Output: ledgers/cib-seven.raw/scan.json
Paced ~1 request/second (CLAUDE.md rule 10).  Re-runnable: skips urls already scanned.
"""
import io, json, os, re, sys, time, html, urllib.request

RAW = 'ledgers/cib-seven.raw'
OUT = os.path.join(RAW, 'scan.json')
UA = {'User-Agent': 'Mozilla/5.0 (research; master-thesis elicitation, read-only)'}
DOCS = 'https://docs.cibseven.org'
KW = ['AI', 'GPT', 'LLM', 'OpenAI', 'Anthropic', 'Claude', 'LangChain', 'MCP', 'agent',
      'Agent', 'agentic', 'machine learning', 'knowledge', 'embedding', 'vector', 'prompt',
      'chatbot', 'copilot', 'robot', 'RAG', 'KI', 'künstliche', 'Artificial Intelligence',
      'model', 'connector', 'Mistral', 'Ollama', 'Azure OpenAI', 'Bedrock', 'Anthropic']
STRONG = re.compile(r'(?<![A-Za-z])(AI|GPT|LLM|OpenAI|Anthropic|Claude|LangChain|MCP|agent\w*|KI|künstliche|Artificial Intelligence|Mistral|Ollama|Bedrock|RAG|chatbot|copilot|robot\w*)(?![A-Za-z])', re.I)
BPMNISH = re.compile(r'(bpmn:|serviceTask|userTask|exclusiveGateway|connectorId|camunda:|zeebe:|\.bpmn|element template|cibseven-ai-agent|cibseven-knowledge-ingestor)', re.I)


def strip(s):
    s = re.sub(r'(?is)<(script|style|noscript)\b.*?</\1>', ' ', s)
    return s


def text_of(h):
    m = re.search(r'(?is)<article\b.*?</article>', h)
    if not m:
        m = re.search(r'(?is)<main\b.*?</main>', h)
    if not m:
        m = re.search(r'(?is)<body\b.*?</body>', h)
    s = strip(m.group(0) if m else h)
    s = re.sub(r'(?is)<br\s*/?>|</p>|</div>|</li>|</h[1-6]>', '\n', s)
    s = re.sub(r'(?s)<[^>]+>', ' ', s)
    s = html.unescape(s)
    s = re.sub(r'[ \t\x0b\f\r]+', ' ', s)
    s = re.sub(r'\n\s*\n+', '\n', s)
    return s.strip()


def scan(html_text, url):
    rec = {}
    m = re.search(r'(?is)<title[^>]*>(.*?)</title>', html_text)
    rec['t'] = html.unescape(re.sub(r'\s+', ' ', m.group(1)).strip()) if m else ''
    body = strip(html_text)
    # code / pre blocks that name BPMN or connectors
    pre = []
    for m in re.finditer(r'(?is)<pre\b[^>]*>(.*?)</pre>', body):
        s = html.unescape(re.sub(r'(?s)<[^>]+>', '', m.group(1)))
        s = re.sub(r'\s+', ' ', s).strip()
        if s and BPMNISH.search(s):
            pre.append(s[:400])
    rec['pre'] = pre[:6]
    rec['files'] = sorted(set(re.findall(r'href="([^"]+\.(?:bpmn|dmn|cmmn|zip))"', body, re.I)))[:10]
    rec['imgs'] = sorted(set(re.findall(r'<img[^>]+src="([^"]+)"', body, re.I)))[:60]
    rec['bgs'] = sorted(set(re.findall(r'url\((["\']?)([^)"\']+)\1\)', body)))[:0]
    rec['bgs'] = sorted(set(u for _, u in re.findall(r'url\((["\']?)([^)"\']+)\1\)', body) if not u.startswith('data:')))[:40]
    cls = set()
    for m in re.finditer(r'(?is)<svg\b[^>]*class="([^"]*)"', body):
        for c in m.group(1).split():
            if c.startswith(('djs', 'bjs', 'bpmn')):
                cls.add(c)
    rec['svg'] = sorted(cls)[:20]
    v = []
    for mk in ('djs-element', 'djs-shape', 'djs-connection', 'data-element-id', 'bpmn-js', 'bpmn.io', 'bpmnjs'):
        if mk in body:
            v.append(mk)
    rec['viewer'] = v
    art = re.search(r'(?is)<article\b.*?</article>', body)
    core = art.group(0) if art else body
    txt = text_of(core) if art else text_of(html_text)
    rec['len'] = len(txt)
    rec['text'] = txt[:6000]
    ais = []
    for m in STRONG.finditer(txt):
        a, b = max(0, m.start() - 90), min(len(txt), m.end() + 90)
        ais.append({'kw': m.group(0), 'ctx': re.sub(r'\s+', ' ', txt[a:b])})
        if len(ais) >= 25:
            break
    rec['ai'] = ais
    return rec


def load():
    if os.path.exists(OUT):
        try:
            return json.load(io.open(OUT, encoding='utf-8'))
        except Exception:
            return {}
    return {}


def main():
    docs = [DOCS + l.strip() for l in io.open('ledgers/cib.raw/nav_latest.txt', encoding='utf-8') if l.strip()]
    mkt = sorted(json.load(io.open(os.path.join(RAW, 'mkt_pages.json'), encoding='utf-8')))
    urls = docs + mkt
    seen = load()
    print('targets', len(urls), 'already', len(seen))
    ok = fail = skip = 0
    for i, u in enumerate(urls, 1):
        if u in seen and not seen[u].get('error'):
            skip += 1
            continue
        try:
            r = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30)
            h = r.read().decode('utf-8', 'replace')
            rec = scan(h, u)
            rec['url'] = u
            rec['status'] = r.status
            seen[u] = rec
            ok += 1
        except Exception as ex:
            seen[u] = {'url': u, 'error': '%s %s' % (type(ex).__name__, str(ex)[:70])}
            fail += 1
            print('FAIL', u, seen[u]['error'])
        if i % 20 == 0:
            json.dump(seen, io.open(OUT, 'w', encoding='utf-8'), ensure_ascii=False)
            print('  %d/%d ok %d skip %d fail %d' % (i, len(urls), ok, skip, fail))
        time.sleep(0.9)
    json.dump(seen, io.open(OUT, 'w', encoding='utf-8'), ensure_ascii=False)
    print('done: ok %d skip %d fail %d total %d' % (ok, skip, fail, len(seen)))


if __name__ == '__main__':
    main()
