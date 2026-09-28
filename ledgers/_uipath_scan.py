# -*- coding: utf-8 -*-
"""Crawl the UiPath Maestro census population (docs.uipath.com).

Population = the vendor sitemap, pinned to one product line and version:
    https://docs.uipath.com/products/maestro/sitemaps/en/sitemap.xml  (317 urls)
    -> 222 urls under /maestro/automation-cloud/latest   (the population)
    ->  95 urls under /maestro/automation-suite/2.2510   (other version, out of scope)
The English tree is the one enumerated (the German tree is a translation of it and the
docs themselves warn that localisation lags: a recall risk).

Per page this pass keeps server-rendered content only (the site is Docusaurus; the
page's own heading is <h2 class="title"> inside div.theme-doc-markdown):
    t          page heading
    text       cleaned content region
    pre        []code blocks
    imgs       [{src, alt, title, cap}]
    files      .bpmn/.dmn/.cmmn/.zip/.json download targets
    links      in-page links under /maestro/automation-cloud/latest/  (closure check)
    ai         strong AI/LLM/agent keyword hits with context
    svg        count of inline <svg> (a rendered BPMN canvas would show up here)
    err        fetch error, else None

Output: ledgers/uipath-maestro-docs.raw/scan.json
Paced ~1 request/second (CLAUDE.md rule 10).  Re-runnable: keeps what it has.
"""
import io, json, os, re, sys, time, html, gzip, urllib.request

RAW = 'ledgers/uipath-maestro-docs.raw'
OUT = os.path.join(RAW, 'scan.json')
SITEMAP = os.path.join(RAW, 'sitemap_en.xml')
UA = {'User-Agent': 'Mozilla/5.0 (research; master-thesis elicitation, read-only)'}
# Both Maestro product lines the vendor's own sitemap for this product lists.  They are
# two publication lines of the same manual (Automation Cloud SaaS + Automation Suite
# on-premise, pinned release), so both are enumerated and a page whose figure set is
# byte-identical to an already-recorded page is E3-duplicate ("one docs page under two
# URLs"), not a silent omission.
PREFIX = ('/maestro/automation-cloud/latest', '/maestro/automation-suite/2.2510')
# Link-union closure: pages reachable from the crawled pages but absent from the vendor
# sitemap for this product.  Two further out-of-sitemap links (introduction-to-maestro,
# process-monitoring) redirect to /user-guide/overview and are ledger rows of their own
# (E3-duplicate, one page under two URLs) rather than pages to fetch.
EXTRA = ['/maestro/automation-cloud/latest/user-guide/automate-getting-started',
         '/maestro/automation-cloud/latest/user-guide/choosing-maestro-orchestrate-or-maestro-automate',
         '/maestro/automation-cloud/latest/user-guide/maestro-automate-capabilities-comparison',
         '/maestro/automation-cloud/latest/user-guide/node-human']
STRONG = re.compile(
    r'(?<![A-Za-z])(AI|A\.I\.|GPT|LLM|LLMs|OpenAI|Anthropic|Claude|Gemini|Azure OpenAI|'
    r'agent|agents|agentic|multi-agent|chatbot|copilot|prompt|prompts|RAG|embedding|'
    r'knowledge base|vector store|machine learning|Autopilot|generative)(?![A-Za-z])', re.I)


def clean(s):
    s = re.sub(r'(?is)<(script|style|noscript)\b.*?</\1>', ' ', s)
    s = re.sub(r'(?is)<br\s*/?>|</p>|</div>|</li>|</h[1-6]>|</tr>|</pre>', '\n', s)
    s = re.sub(r'(?s)<[^>]+>', ' ', s)
    s = html.unescape(s)
    s = s.replace('​', ' ')
    s = re.sub(r'[ \t\x0b\f\r]+', ' ', s)
    s = re.sub(r'\n\s*\n+', '\n', s)
    return s.strip()


def content_region(h):
    i = h.find('theme-doc-markdown')
    if i < 0:
        return ''
    chunk = h[i:i + 400000]
    for stop in ('Was this article helpful', 'On this page', 'class="footer', 'Previous page'):
        j = chunk.find(stop, 2000)
        if j > 0:
            chunk = chunk[:j]
    return clean(chunk)


def extract(u, h, final=None):
    reg = content_region(h)
    m = re.search(r'(?is)<h2[^>]*class="title"[^>]*>(.*?)</h2>', h)
    title = clean(m.group(1)) if m else ''
    if not title:
        m = re.search(r'(?is)<h1[^>]*>(.*?)</h1>', h)
        title = clean(m.group(1)) if m else ''
    pre = [clean(p)[:1500] for p in re.findall(r'(?is)<pre[^>]*>(.*?)</pre>', h)][:8]
    imgs = []
    for m in re.finditer(r'(?is)<img\b([^>]*)>', h):
        at = m.group(1)
        src = (re.search(r'src="([^"]*)"', at) or [None, ''])[1]
        if not src or 'logo' in src.lower():
            continue
        alt = (re.search(r'alt="([^"]*)"', at) or [None, ''])[1]
        ttl = (re.search(r'title="([^"]*)"', at) or [None, ''])[1]
        cap = re.sub(r'(?s)<[^>]+>', ' ', h[m.end():m.end() + 300])
        cap = re.sub(r'\s+', ' ', html.unescape(cap)).replace('​', ' ').strip()[:200]
        imgs.append({'src': html.unescape(src), 'alt': html.unescape(alt),
                     'title': html.unescape(ttl), 'cap': cap})
    files = sorted(set(re.findall(r'href="([^"]+\.(?:bpmn|dmn|cmmn|zip|json|xml))"', h)))
    links = sorted(set(re.findall(r'/maestro/automation-cloud/latest[a-z0-9\-/]*', h)))
    ai = []
    for m in STRONG.finditer(reg):
        a, b = max(0, m.start() - 100), min(len(reg), m.end() + 100)
        ai.append({'kw': m.group(0), 'ctx': re.sub(r'\s+', ' ', reg[a:b])})
        if len(ai) >= 40:
            break
    m = re.search(r'<link rel="canonical" href="([^"]+)"', h)
    canon = m.group(1) if m else ''
    return {'t': title, 'text': reg[:12000], 'len': len(reg), 'pre': pre, 'imgs': imgs,
            'files': files, 'links': links, 'ai': ai, 'canon': canon,
            'final': (final or u).replace('https://docs.uipath.com', ''),
            'svg': len(re.findall(r'<svg', h)), 'err': None}


def main():
    urls = [x for x in re.findall(r'<loc>(.*?)</loc>',
                                  io.open(SITEMAP, encoding='utf-8').read())
            if any(p in x for p in PREFIX)]
    urls = sorted(set(u.replace('https://docs.uipath.com', '') for u in urls) | set(EXTRA))
    seen = {}
    if os.path.exists(OUT):
        seen = json.load(io.open(OUT, encoding='utf-8'))
    ok = fail = skip = 0
    only = sys.argv[1:] or None
    for i, p in enumerate(urls, 1):
        if only and not any(o in p for o in only):
            continue
        if p in seen and not seen[p].get('err'):
            skip += 1
            continue
        try:
            r = urllib.request.urlopen(urllib.request.Request(
                'https://docs.uipath.com' + p, headers=UA), timeout=45)
            h = r.read().decode('utf-8', 'replace')
            seen[p] = extract(p, h, r.geturl())
            ok += 1
        except Exception as ex:
            seen[p] = {'err': '%s %s' % (type(ex).__name__, str(ex)[:70])}
            fail += 1
            print('FAIL', p, seen[p]['err'])
        if i % 10 == 0:
            json.dump(seen, io.open(OUT, 'w', encoding='utf-8'), ensure_ascii=True)
            print('  %d/%d ok %d skip %d fail %d' % (i, len(urls), ok, skip, fail), flush=True)
        time.sleep(0.9)
    json.dump(seen, io.open(OUT, 'w', encoding='utf-8'), ensure_ascii=True)
    print('done: ok %d skip %d fail %d total %d' % (ok, skip, fail, len(seen)))


if __name__ == '__main__':
    main()
