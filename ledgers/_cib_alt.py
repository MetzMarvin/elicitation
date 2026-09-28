# -*- coding: utf-8 -*-
"""Alt-text / caption harvest for every docs page that carries a figure.

CLAUDE.md prefers textual and DOM evidence over the picture itself.  Docusaurus
figure captions and alt attributes frequently name the notation ("BPMN diagram",
"architecture", "decision table", "screenshot of the Cockpit ..."), which decides
E1 vs E2 for a figure page without reading the image.

Output: ledgers/cib-seven.raw/alt.json  {url: [{src, alt, title, cap}]}
Paced ~1 request/second (CLAUDE.md rule 10).  Re-runnable.
"""
import io, json, os, re, time, html, urllib.request

RAW = 'ledgers/cib-seven.raw'
OUT = os.path.join(RAW, 'alt.json')
DOCS = 'https://docs.cibseven.org'
UA = {'User-Agent': 'Mozilla/5.0 (research; master-thesis elicitation, read-only)'}


def main():
    img = json.load(io.open(os.path.join(RAW, 'img.json'), encoding='utf-8'))
    pages = []
    for src, e in img.items():
        f = e.get('file') or ''
        if not f or 'logo.png' in src or 'creativecommons' in src:
            continue
        for pg in (e.get('pages') or []):
            if pg not in pages:
                pages.append(pg)
    pages.sort()
    seen = {}
    if os.path.exists(OUT):
        seen = json.load(io.open(OUT, encoding='utf-8'))
    ok = fail = skip = 0
    for i, u in enumerate(pages, 1):
        if u in seen:
            skip += 1
            continue
        try:
            h = urllib.request.urlopen(urllib.request.Request(DOCS + u, headers=UA),
                                       timeout=30).read().decode('utf-8', 'replace')
            out = []
            for m in re.finditer(r'(?is)<img\b([^>]*)>', h):
                at = m.group(1)
                src = (re.search(r'src="([^"]*)"', at) or [None, ''])[1]
                if 'logo.png' in src or 'creativecommons' in src or not src:
                    continue
                alt = (re.search(r'alt="([^"]*)"', at) or [None, ''])[1]
                ttl = (re.search(r'title="([^"]*)"', at) or [None, ''])[1]
                tail = h[m.end():m.end() + 400]
                cap = re.sub(r'(?s)<[^>]+>', ' ', tail)
                cap = re.sub(r'\s+', ' ', html.unescape(cap)).strip()[:160]
                out.append({'src': src, 'alt': html.unescape(alt), 'title': html.unescape(ttl),
                            'cap': cap})
            seen[u] = out
            ok += 1
        except Exception as ex:
            seen[u] = {'err': '%s %s' % (type(ex).__name__, str(ex)[:60])}
            fail += 1
            print('FAIL', u)
        if i % 10 == 0:
            json.dump(seen, io.open(OUT, 'w', encoding='utf-8'), ensure_ascii=False)
            print('  %d/%d ok %d skip %d fail %d' % (i, len(pages), ok, skip, fail))
        time.sleep(0.9)
    json.dump(seen, io.open(OUT, 'w', encoding='utf-8'), ensure_ascii=False)
    print('done ok %d skip %d fail %d of %d' % (ok, skip, fail, len(pages)))


if __name__ == '__main__':
    main()
