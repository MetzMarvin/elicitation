# -*- coding: utf-8 -*-
"""Contact sheets for the Flowable census visual screen.

Downloads image assets, caches them, and tiles them into numbered sheets so a
human/agent can screen many images at thumbnail size and then open only the
candidates at native resolution.

usage: python ledgers/_flw_sheets.py <itemlist.json> <outprefix> [per_sheet]
itemlist.json: [[page_url, img_url], ...]
Writes <outprefix>_NN.png + <outprefix>_index.json  (thumb no -> [page,img,w,h])
"""
import io
import json
import os
import re
import sys
import time
import urllib.request

from PIL import Image, ImageDraw

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'flowable.raw')
CACHE = os.path.join(RAW, 'imgcache')
UA = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/124.0 Safari/537.36 (research; master-thesis elicitation, read-only)'}
THUMB_W = 300
COLS = 6


def cache_path(u):
    h = re.sub(r'[^A-Za-z0-9]', '_', u)[-140:]
    return os.path.join(CACHE, h)


def fetch(u):
    p = cache_path(u)
    if os.path.exists(p) and os.path.getsize(p) > 0:
        return p
    req = urllib.request.Request(u, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read()
    except Exception as e:  # noqa: BLE001
        open(p + '.fail', 'w').write(f'{u}\n{e}\n')
        return None
    open(p, 'wb').write(data)
    time.sleep(0.35)
    return p


def main():
    items = json.load(open(sys.argv[1], encoding='utf-8'))
    prefix = sys.argv[2]
    per = int(sys.argv[3]) if len(sys.argv) > 3 else 36
    os.makedirs(CACHE, exist_ok=True)
    imgs = []
    for page, u in items:
        p = fetch(u)
        if not p:
            imgs.append((page, u, None, None, None))
            continue
        try:
            im = Image.open(p)
            im.load()
            imgs.append((page, u, im, im.width, im.height))
        except Exception:  # noqa: BLE001
            imgs.append((page, u, None, None, None))
    # drop tiny images (< 220 px wide) unless they are all we have - icons/logos
    keep = [t for t in imgs if t[4] and t[3] >= 220]
    dropped = len(imgs) - len(keep)
    rows = (per + COLS - 1) // COLS
    index = {}
    sheets = 0
    for s in range(0, len(keep), per):
        chunk = keep[s:s + per]
        cell_h = 260
        sheet = Image.new('RGB', (COLS * THUMB_W, rows * cell_h), 'white')
        dr = ImageDraw.Draw(sheet)
        for i, (page, u, im, w, h) in enumerate(chunk):
            n = s + i + 1
            index[str(n)] = [page, u, w, h]
            r, c = divmod(i, COLS)
            t = im.copy()
            t.thumbnail((THUMB_W - 8, cell_h - 26))
            sheet.paste(t, (c * THUMB_W + 4, r * cell_h + 20))
            dr.text((c * THUMB_W + 4, r * cell_h + 3), f'#{n} {w}x{h}', fill='black')
            dr.rectangle([c * THUMB_W, r * cell_h, c * THUMB_W + THUMB_W - 1,
                          r * cell_h + cell_h - 1], outline='#bbbbbb')
        out = f'{prefix}_{s // per + 1:02d}.png'
        sheet.save(out)
        sheets += 1
        print('wrote', out, len(chunk), flush=True)
    json.dump(index, open(prefix + '_index.json', 'w'), indent=0)
    print(f'items={len(items)} kept={len(keep)} dropped_small={dropped} sheets={sheets}')


if __name__ == '__main__':
    main()
