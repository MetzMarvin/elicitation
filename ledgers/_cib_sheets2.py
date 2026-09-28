# -*- coding: utf-8 -*-
"""Contact sheets over a downloaded-image manifest.

usage: python ledgers/_cib_sheets2.py <manifest.json> <imgdir> <outdir> <prefix> [--cols N --rows N --tile px --min-px N]

Tiles are labelled "#<pos> <WxH> <file>" so a reader can name a tile and the
position maps back to the asset. Images smaller than --min-px on both sides are
skipped as chrome (icons, badges, spacers) unless --keep-small is given.
Writes <outdir>/sheets_<prefix>.json = [{sheet, tiles:[{pos,file,src,size}]}]
"""
import io, json, os, sys
from PIL import Image, ImageDraw


def main():
    a = [x for x in sys.argv[1:] if not x.startswith('--')]
    manifest, imgdir, outdir, prefix = a[0], a[1], a[2], a[3]
    args = sys.argv[1:]
    cols = int(args[args.index('--cols') + 1]) if '--cols' in args else 8
    rows = int(args[args.index('--rows') + 1]) if '--rows' in args else 6
    tile = int(args[args.index('--tile') + 1]) if '--tile' in args else 340
    minpx = int(args[args.index('--min-px') + 1]) if '--min-px' in args else 0
    keep_small = '--keep-small' in args
    man = json.load(io.open(manifest, encoding='utf-8'))
    items = []
    for src, e in sorted(man.items()):
        if not e.get('file'):
            continue
        p = os.path.join(imgdir, e['file'])
        if not os.path.exists(p):
            continue
        if e.get('chrome') and not keep_small:
            continue
        try:
            w, h = Image.open(p).size
        except Exception:
            continue
        if not keep_small and minpx and max(w, h) < minpx:
            continue
        items.append((src, e))
    print('tiles:', len(items), 'of', len(man))
    os.makedirs(outdir, exist_ok=True)
    per = cols * rows
    index = []
    for s in range(0, len(items), per):
        chunk = items[s:s + per]
        sheet = Image.new('RGB', (cols * tile, rows * tile), 'white')
        d = ImageDraw.Draw(sheet)
        tiles = []
        for k, (src, e) in enumerate(chunk):
            cx, cy = k % cols, k // cols
            x, y = cx * tile, cy * tile
            try:
                im = Image.open(os.path.join(imgdir, e['file'])).convert('RGB')
            except Exception:
                continue
            w, h = im.size
            sc = min((tile - 34) / max(1, w), (tile - 34) / max(1, h), 1.0)
            im2 = im.resize((max(1, int(w * sc)), max(1, int(h * sc))), Image.LANCZOS)
            sheet.paste(im2, (x + (tile - im2.width) // 2, y + 30 + (tile - 30 - im2.height) // 2))
            d.text((x + 4, y + 4), '#%d %dx%d %s' % (k, w, h, os.path.basename(e['file'])[:32]), fill='black')
            d.rectangle([x, y, x + tile - 2, y + tile - 2], outline='#bbbbbb')
            tiles.append({'pos': k, 'file': e['file'], 'src': src, 'size': [w, h], 'pages': e.get('pages')})
        name = '%s%02d.jpg' % (prefix, s // per)
        sheet.save(os.path.join(outdir, name), quality=88)
        index.append({'sheet': name, 'tiles': tiles})
        print(' ', name, len(tiles), sheet.size)
    json.dump(index, io.open(os.path.join(outdir, 'sheets_%s.json' % prefix), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
