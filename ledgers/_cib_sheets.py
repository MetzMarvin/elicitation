# -*- coding: utf-8 -*-
"""Build contact sheets over every distinct content image of the CIB seven manual.

Input : ledgers/cib-seven.raw/img.json  (src -> {file, pages, alt})
Output: ledgers/cib-seven.raw/sheets/c00.jpg .. cNN.jpg (48 tiles, 8x6, 340 px wide)
        ledgers/cib-seven.raw/sheets.json  [{"sheet": "c00.jpg", "tiles": [{pos, file, src}]}]

Tiles are labelled with their index on the sheet so a reader can name the tile
("c00 #17") and the index can be mapped back to the asset name and the pages.

usage: python ledgers/_cib_sheets.py [--cols 8 --rows 6 --tile 340]
"""
import io, json, os, sys
from PIL import Image, ImageDraw

RAW = 'ledgers/cib-seven.raw'
IMGDIR = os.path.join(RAW, 'img')
OUT = os.path.join(RAW, 'sheets')


def main():
    cols = rows = None
    args = sys.argv[1:]
    cols = int(args[args.index('--cols') + 1]) if '--cols' in args else 8
    rows = int(args[args.index('--rows') + 1]) if '--rows' in args else 6
    tile = int(args[args.index('--tile') + 1]) if '--tile' in args else 340
    man = json.load(io.open(os.path.join(RAW, 'img.json'), encoding='utf-8'))
    items = [(src, e) for src, e in sorted(man.items()) if e.get('file') and os.path.exists(os.path.join(IMGDIR, e['file']))]
    print('images available:', len(items), 'of', len(man))
    os.makedirs(OUT, exist_ok=True)
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
                im = Image.open(os.path.join(IMGDIR, e['file'])).convert('RGB')
            except Exception as ex:
                d.rectangle([x, y, x + tile - 2, y + tile - 2], outline='red')
                d.text((x + 6, y + 6), 'ERR', fill='red')
                continue
            w, h = im.size
            sc = min((tile - 34) / max(1, w), (tile - 34) / max(1, h), 1.0)
            im2 = im.resize((max(1, int(w * sc)), max(1, int(h * sc))), Image.LANCZOS)
            sheet.paste(im2, (x + (tile - im2.width) // 2, y + 30 + (tile - 30 - im2.height) // 2))
            label = '#%d %dx%d %s' % (k, w, h, os.path.basename(e['file'])[:34])
            d.text((x + 4, y + 4), label, fill='black')
            d.rectangle([x, y, x + tile - 2, y + tile - 2], outline='#bbbbbb')
            tiles.append({'pos': k, 'file': e['file'], 'src': src, 'size': [w, h]})
        name = 'c%02d.jpg' % (s // per)
        sheet.save(os.path.join(OUT, name), quality=88)
        index.append({'sheet': name, 'tiles': tiles})
        print(' ', name, len(tiles), 'tiles', sheet.size)
    json.dump(index, io.open(os.path.join(RAW, 'sheets.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
