# -*- coding: utf-8 -*-
"""Download every distinct content image the CIB seven manual publishes.

Input:  ledgers/cib-seven.raw/pages.json (per-page imgs from the nav census)
Output: ledgers/cib-seven.raw/img/<n>_<name>  +  ledgers/cib-seven.raw/img.json
        {src_as_written: {"file": ..., "page": <first page>, "pages": [..]}}

Paced at ~1 request/second (CLAUDE.md rule 10). Skips files already on disk,
so it can be re-run to resume.
"""
import io, json, os, sys, time, urllib.parse, urllib.request

RAW = 'ledgers/cib-seven.raw'
IMGDIR = os.path.join(RAW, 'img')
BASE = 'https://docs.cibseven.org'
UA = {'User-Agent': 'Mozilla/5.0 (research; master-thesis elicitation, read-only)'}


def main():
    pages = json.load(io.open(os.path.join(RAW, 'pages.json'), encoding='utf-8'))
    seen = {}
    for u, v in pages.items():
        base = BASE + u
        for i in v.get('imgs') or []:
            src = i['src']
            full = urllib.parse.urljoin(base, src)
            e = seen.setdefault(full, {'pages': [], 'alt': i.get('alt', '')})
            if u not in e['pages']:
                e['pages'].append(u)
    print('distinct images:', len(seen))
    os.makedirs(IMGDIR, exist_ok=True)
    manifest = {}
    if os.path.exists(os.path.join(RAW, 'img.json')):
        manifest = json.load(io.open(os.path.join(RAW, 'img.json'), encoding='utf-8'))
    ok = skip = fail = 0
    for n, (full, e) in enumerate(sorted(seen.items()), 1):
        name = urllib.parse.unquote(full.split('/manual/latest/')[-1]).replace('/', '_')
        name = ''.join(c if c.isalnum() or c in '._-' else '_' for c in name)[-90:]
        dest = '%03d_%s' % (n, name)
        path = os.path.join(IMGDIR, dest)
        e['file'] = dest
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
            e['error'] = '%s %s' % (type(ex).__name__, str(ex)[:80])
            manifest[full] = e
            fail += 1
            print('FAIL', full, e['error'])
        if n % 25 == 0:
            print('  ...%d/%d (ok %d skip %d fail %d)' % (n, len(seen), ok, skip, fail))
            json.dump(manifest, io.open(os.path.join(RAW, 'img.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        time.sleep(0.7)
    json.dump(manifest, io.open(os.path.join(RAW, 'img.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('done: ok %d skip %d fail %d' % (ok, skip, fail))


if __name__ == '__main__':
    main()
