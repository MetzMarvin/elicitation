# -*- coding: utf-8 -*-
"""Download Maestro figure assets and lay them out as labelled contact sheets.

The docs publish every figure as a .webp under dev-assets.cms.uipath.com; a page's
diagram is judged from the asset itself (CLAUDE.md: capture the asset at its native
URL, do not screenshot the rendered page).

usage: python ledgers/_uipath_sheets.py <manifest.json> <outdir> [--cols N --rows N --tile px]
  manifest.json : [{"page": "...", "src": "https://...webp", "alt": "..."}, ...]
Each sheet tile is labelled "#pos  WxH  filestem  [page-tail]".
"""
import io, json, os, re, sys, urllib.request
from PIL import Image, ImageDraw

RAW = 'ledgers/uipath-maestro-docs.raw'
IMG = os.path.join(RAW, 'img')
UA = {'User-Agent': 'Mozilla/5.0 (research; master-thesis elicitation, read-only)'}


def local(src):
    return os.path.join(IMG, re.sub(r'[^A-Za-z0-9._-]', '_', src.split('/')[-1]))


def fetch(src):
    p = local(src)
    if os.path.exists(p) and os.path.getsize(p) > 1000:
        return p
    d = urllib.request.urlopen(urllib.request.Request(src, headers=UA), timeout=60).read()
    open(p, 'wb').write(d)
    return p


def main():
    man = json.load(io.open(sys.argv[1], encoding='utf-8'))
    out = sys.argv[2]
    cols = rows = tile = None
    args = sys.argv[3:]
    for i, a in enumerate(args):
        if a == '--cols':
            cols = int(args[i + 1])
        if a == '--rows':
            rows = int(args[i + 1])
        if a == '--tile':
            tile = int(args[i + 1])
    cols = cols or 6
    rows = rows or 5
    tile = tile or 520
    os.makedirs(out, exist_ok=True)
    os.makedirs(IMG, exist_ok=True)
    items = []
    for o in man:
        try:
            p = fetch(o['src'])
            w, h = Image.open(p).size
        except Exception as ex:
            print('SKIP', o['src'], type(ex).__name__)
            continue
        items.append(dict(o, file=p, w=w, h=h))
    per = cols * rows
    manifest = []
    for s in range(0, len(items), per):
        chunk = items[s:s + per]
        sheet = Image.new('RGB', (cols * tile, rows * tile), 'white')
        d = ImageDraw.Draw(sheet)
        for k, o in enumerate(chunk):
            r, c = divmod(k, cols)
            im = Image.open(o['file']).convert('RGB')
            im.thumbnail((tile - 10, tile - 34), Image.LANCZOS)
            sheet.paste(im, (c * tile + (tile - im.size[0]) // 2, r * tile + 26))
            lab = '#%d %dx%d %s' % (s + k, o['w'], o['h'], os.path.basename(o['src'])[:38])
            d.text((c * tile + 3, r * tile + 4), lab, fill='black')
            d.text((c * tile + 3, r * tile + 14), o['page'].split('/user-guide/')[-1][:52], fill='#444444')
            d.rectangle([c * tile, r * tile, c * tile + tile - 1, r * tile + tile - 1], outline='#bbbbbb')
        fn = os.path.join(out, 'sh%02d.jpg' % (s // per))
        sheet.save(fn, quality=88)
        manifest.append({'sheet': fn, 'items': [{k: o[k] for k in ('page', 'src', 'alt', 'w', 'h')} for o in chunk]})
        print(fn, len(chunk))
    io.open(os.path.join(out, 'sheets.json'), 'w', encoding='utf-8').write(
        json.dumps(manifest, ensure_ascii=True, indent=1))
    print('figures', len(items), 'sheets', len(manifest))


if __name__ == '__main__':
    main()
