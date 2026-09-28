# -*- coding: utf-8 -*-
"""Crawl the uipath-marketplace census population (elicitation-15, 2026-09-27).

Frontier = ledgers/uipath-marketplace.frontier.txt (2326 /listings/<slug> paths taken
from https://marketplace.uipath.com/sitemap, document order, deduplicated).
Listing pages are server-rendered (htmx), so a plain GET returns the full listing.

Per listing:
  raw/html/<idx>.html.gz   the page as served (archive, judged_from)
  raw/scan.jsonl           parsed: title, type, publisher, breadcrumb, main text
                           (listing name .. "Similar Listings"), tags, media imgs,
                           links, AI / BPMN keyword hits
Paced ~1 request/second.  Re-runnable: skips indices already in scan.jsonl.
"""
import gzip, html, json, os, re, sys, time, urllib.request

ELI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ELI, 'ledgers', 'uipath-marketplace.raw')
FRONTIER = os.path.join(ELI, 'ledgers', 'uipath-marketplace.frontier.txt')
OUT = os.path.join(RAW, 'scan.jsonl')
UA = {'User-Agent': 'Mozilla/5.0 (research; master-thesis elicitation, read-only)',
      'Accept-Language': 'en-US,en;q=0.9'}

AI = re.compile(
    r'(?<![A-Za-z])(AI|A\.I\.|GenAI|Gen AI|GPT[-\w.]*|ChatGPT|LLMs?|OpenAI|Anthropic|Claude|Gemini|'
    r'Llama|Mistral|Bedrock|Vertex|Copilot|agents?|agentic|multi-agent|chatbot|prompts?|RAG|'
    r'embeddings?|vector|machine learning|ML|Autopilot|generative|Agentforce|CrewAI|'
    r'Context Grounding|intelligent|NLP|sentiment|summari[sz]\w*|classif\w*)(?![A-Za-z])', re.I)
BPMN = re.compile(r'(?<![A-Za-z])(BPMN|Maestro|agentic process|process model\w*|swimlane|'
                  r'gateway|lane|pool|orchestrat\w*|\.bpmn)(?![A-Za-z])', re.I)


def text(s):
    s = re.sub(r'(?is)<(script|style|noscript|svg)\b.*?</\1>', ' ', s)
    s = re.sub(r'(?is)<br\s*/?>|</p>|</div>|</li>|</h[1-6]>|</tr>', '\n', s)
    s = re.sub(r'(?s)<[^>]+>', ' ', s)
    s = html.unescape(s).replace('​', ' ')
    s = re.sub(r'[ \t\r\f\v]+', ' ', s)
    return re.sub(r'\n\s*\n+', '\n', s).strip()


def hits(rx, t):
    out = {}
    for m in rx.finditer(t):
        k = m.group(1).lower()
        if k not in out:
            a, b = max(0, m.start() - 70), min(len(t), m.end() + 70)
            out[k] = t[a:b].replace('\n', ' ')
    return out


def parse(idx, url, code, s):
    r = {'n': idx, 'url': url, 'http': code}
    if code != 200 or not s:
        return r
    m = re.search(r'<h1 class="mp-listing-name"[^>]*>(.*?)</h1>', s, re.S)
    r['title'] = html.unescape(re.sub(r'<[^>]+>', '', m.group(1))).strip() if m else None
    m = re.search(r'class="mp-listing-meta-type">(.*?)</span>', s, re.S)
    r['type'] = html.unescape(m.group(1)).strip() if m else None
    r['crumbs'] = [html.unescape(x) for x in re.findall(r'"name":\s*"([^"]*)"', s.split('BreadcrumbList', 1)[-1].split('</script>', 1)[0])]
    a = s.find('class="mp-listing-name"')
    b = s.find('Similar Listings', a if a > 0 else 0)
    main = s[a if a > 0 else 0: b if b > 0 else len(s)]
    t = text('<x ' + main)
    r['text'] = t
    m = re.search(r'by\s*</?[^>]*>?\s*<a[^>]*>(.*?)</a>', main, re.S)
    pub = re.search(r'Publisher\s*\n\s*(.+)', t)
    r['publisher'] = pub.group(1).strip() if pub else None
    r['tags'] = [html.unescape(x).strip() for x in re.findall(r'class="mp-sidebar-tag[^"]*"[^>]*>(.*?)<', main, re.S)]
    r['media'] = re.findall(r'<img src="([^"]+)"[^>]*class="mp-media-img', main)
    r['media'] += [u for u in re.findall(r'(?:src|data-src|href)="([^"]+\.(?:gif|mp4|webm)[^"]*)"', main)]
    r['video'] = re.findall(r'(?:src|href|data-src)="([^"]*(?:youtube|youtu\.be|vimeo|wistia|\.mp4)[^"]*)"', main)
    r['links'] = sorted(set(re.findall(r'href="(https?://[^"]+)"', main)))
    r['ai'] = hits(AI, t)
    r['bpmn'] = hits(BPMN, t)
    return r


def main():
    urls = [l.strip() for l in open(FRONTIER, encoding='utf-8') if l.strip()]
    done = set()
    if os.path.exists(OUT):
        for l in open(OUT, encoding='utf-8'):
            done.add(json.loads(l)['n'])
    os.makedirs(os.path.join(RAW, 'html'), exist_ok=True)
    with open(OUT, 'a', encoding='utf-8') as fo:
        for i, u in enumerate(urls, 1):
            if i in done:
                continue
            t0 = time.time()
            code, s = None, ''
            for attempt in range(3):
                try:
                    with urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=40) as resp:
                        code, s = resp.status, resp.read().decode('utf-8', 'replace')
                        final = resp.geturl()
                    break
                except urllib.error.HTTPError as e:
                    code, final = e.code, u
                    break
                except Exception as e:
                    code, final = 'ERR ' + str(e)[:80], u
                    time.sleep(5)
            if s:
                with gzip.open(os.path.join(RAW, 'html', f'{i:04d}.html.gz'), 'wt', encoding='utf-8') as g:
                    g.write(s)
            r = parse(i, u, code, s)
            r['final_url'] = final
            fo.write(json.dumps(r, ensure_ascii=False) + '\n')
            fo.flush()
            if i % 100 == 0:
                print(i, code, r.get('title'), flush=True)
            time.sleep(max(0, 1.0 - (time.time() - t0)))


if __name__ == '__main__':
    main()
