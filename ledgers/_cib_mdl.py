# -*- coding: utf-8 -*-
"""Download the cibseven.org (marketing host) images the census found.

Input : ledgers/cib-seven.raw/mkt_pages.json   (per-page imgs)
Output: ledgers/cib-seven.raw/mimg/<n>_<name> + ledgers/cib-seven.raw/mimg.json

Chrome images (language icon, GDPR badge, social icons, decorative SVG
quote/icon sprites) are still downloaded so the census is complete, but they
are marked chrome=True and kept out of the contact sheets.

Paced ~1 request/second. Re-runnable (skips files already on disk).
"""
import io, json, os, sys, time, urllib.parse, urllib.request

RAW = 'ledgers/cib-seven.raw'
OUTDIR = os.path.join(RAW, 'mimg')
UA = {'User-Agent': 'Mozilla/5.0 (research; master-thesis elicitation, read-only)'}
CHROME = ('icon-lang', 'gdpr_cib', 'linkedin.png', 'youtube-e', 'quotes-', 'icons-', 'favicon')


def main():
    pages = json.load(io.open(os.path.join(RAW, 'mkt_pages.json'), encoding='utf-8'))
    seen = {}
    for u, v in pages.items():
        for s in v.get('imgs') or []:
            full = urllib.parse.urljoin(u, s)
            e = seen.setdefault(full, {'pages': []})
            if u not in e['pages']:
                e['pages'].append(u)
    for full, e in seen.items():
        e['chrome'] = any(c in full for c in CHROME)
    print('distinct images:', len(seen), 'chrome:', sum(1 for e in seen.values() if e['chrome']))
    os.makedirs(OUTDIR, exist_ok=True)
    manifest = {}
    ok = skip = fail = 0
    for n, (full, e) in enumerate(sorted(seen.items()), 1):
        name = urllib.parse.unquote(full.split('/wp-content/')[-1]).replace('/', '_')
        name = ''.join(c if c.isalnum() or c in '._-' else '_' for c in name)[-80:]
        dest = '%03d_%s' % (n, name)
        path = os.path.join(OUTDIR, dest)
        e['file'] = dest
        e['url'] = full
        if os.path.exists(path) and os.path.getsize(path) > 0:
            manifest[full] = e
            skip += 1
            continue
        try:
            r = urllib.request.urlopen(urllib.request.Request(full, headers=UA), timeout=30)
            b = r.read()
            with io.open(path, 'wb') as f:
                f.write(b)
            e['bytes'] = len(b)
            e['ct'] = r.headers.get('content-type')
            manifest[full] = e
            ok += 1
        except Exception as ex:
            e['error'] = '%s %s' % (type(ex).__name__, str(ex)[:70])
            manifest[full] = e
            fail += 1
        time.sleep(0.6)
    json.dump(manifest, io.open(os.path.join(RAW, 'mimg.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('done: ok %d skip %d fail %d' % (ok, skip, fail))


if __name__ == '__main__':
    main()
