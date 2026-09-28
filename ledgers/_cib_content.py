# -*- coding: utf-8 -*-
"""Content-region re-extraction for the cib-seven census (both hosts).

The first crawl's text for docs.cibseven.org pages began with the global
sidebar, because the manual uses neither <article> nor <main>: the page body is
<div class="col-xs-12 content-text"> under <h1 class="page-title">.  That made
every docs quote nav-noise and made "AI wording inside the page content" hard to
see.  This pass re-fetches every enumerated page and keeps only the content
region, then re-runs the strong-AI keyword scan on that region alone.

Output: ledgers/cib-seven.raw/content.json
        {url: {h1, text, ai:[{kw,ctx}], imgs:N, len, err}}

Paced ~1 request/second (CLAUDE.md rule 10).  Re-runnable: keeps what it has.
"""
import io, json, os, re, sys, time, html, urllib.request

RAW = 'ledgers/cib-seven.raw'
OUT = os.path.join(RAW, 'content.json')
DOCS = 'https://docs.cibseven.org'
UA = {'User-Agent': 'Mozilla/5.0 (research; master-thesis elicitation, read-only)'}
STRONG = re.compile(
    r'(?<![A-Za-z])(AI|A\.I\.|GPT|LLM|LLMs|OpenAI|Anthropic|Claude|LangChain|MCP|agent|agents|'
    r'agentic|KI|künstliche|Artificial Intelligence|Mistral|Ollama|Bedrock|RAG|chatbot|copilot|'
    r'robot\w*|knowledge base|embedding|vector store|prompt)(?![A-Za-z])', re.I)


def clean(s):
    s = re.sub(r'(?is)<(script|style|noscript)\b.*?</\1>', ' ', s)
    s = re.sub(r'(?is)<br\s*/?>|</p>|</div>|</li>|</h[1-6]>|</tr>', '\n', s)
    s = re.sub(r'(?s)<[^>]+>', ' ', s)
    s = html.unescape(s)
    s = re.sub(r'[ \t\x0b\f\r]+', ' ', s)
    s = re.sub(r'\n\s*\n+', '\n', s)
    return s.strip()


def region(h, url):
    if url.startswith(DOCS):
        m = re.search(r'(?is)<h1[^>]*class="[^"]*page-title[^"]*"[^>]*>(.*?)</h1>', h)
        h1 = clean(m.group(1)) if m else ''
        i = h.find('content-text')
        if i < 0:
            return h1, ''
        chunk = h[i:i + 120000]
        j = chunk.find('</div>\n</div>')      # the content wrapper's own close
        if j > 2000:
            chunk = chunk[:j]
        return h1, clean(chunk)
    # marketing (WordPress / Yoast)
    for pat in (r'(?is)<div[^>]*class="[^"]*(?:entry-content|elementor-widget-theme-post-content)[^"]*"[^>]*>(.*?)</div>\s*</div>',
                r'(?is)<main\b.*?</main>',
                r'(?is)<article\b.*?</article>'):
        m = re.search(pat, h)
        if m and len(m.group(0)) > 800:
            return '', clean(m.group(0))
    m = re.search(r'(?is)<body\b.*?</body>', h)
    return '', clean(m.group(0) if m else h)


def main():
    scan = json.load(io.open(os.path.join(RAW, 'scan.json'), encoding='utf-8'))
    urls = [u for u, v in scan.items() if not v.get('error')]
    seen = {}
    if os.path.exists(OUT):
        seen = json.load(io.open(OUT, encoding='utf-8'))
    print('targets', len(urls), 'have', len(seen))
    ok = fail = skip = 0
    for i, u in enumerate(urls, 1):
        if u in seen and not seen[u].get('err'):
            skip += 1
            continue
        try:
            r = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30)
            h = r.read().decode('utf-8', 'replace')
            h1, txt = region(h, u)
            ai = []
            for m in STRONG.finditer(txt):
                a, b = max(0, m.start() - 90), min(len(txt), m.end() + 90)
                ai.append({'kw': m.group(0), 'ctx': re.sub(r'\s+', ' ', txt[a:b])})
                if len(ai) >= 25:
                    break
            seen[u] = {'h1': h1, 'text': txt[:8000], 'len': len(txt), 'ai': ai,
                       'imgs': len(re.findall(r'<img[^>]+src="', h)),
                       'err': None}
            ok += 1
        except Exception as ex:
            seen[u] = {'err': '%s %s' % (type(ex).__name__, str(ex)[:60])}
            fail += 1
            print('FAIL', u, seen[u]['err'])
        if i % 20 == 0:
            json.dump(seen, io.open(OUT, 'w', encoding='utf-8'), ensure_ascii=False)
            print('  %d/%d ok %d skip %d fail %d' % (i, len(urls), ok, skip, fail))
        time.sleep(0.9)
    json.dump(seen, io.open(OUT, 'w', encoding='utf-8'), ensure_ascii=False)
    print('done: ok %d skip %d fail %d total %d' % (ok, skip, fail, len(seen)))


if __name__ == '__main__':
    main()
