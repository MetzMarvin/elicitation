# -*- coding: utf-8 -*-
"""Composite a list of asset basenames into read-optimised sheets: images are
stacked VERTICALLY at native resolution and the sheet is kept under 1400 x 1560
so the Read tool does not downscale (diagram labels stay legible).

usage: python ledgers/_lj_sheet_of.py <out_prefix> <basename> [<basename> ...]
writes ledgers/loyjoy.raw/zoom/<prefix>_<k>.jpg and prints the paths + sizes."""
import io, json, os, sys
from PIL import Image

RAW = 'ledgers/loyjoy.raw/mkt_all'
OUT = 'ledgers/loyjoy.raw/zoom'
os.makedirs(OUT, exist_ok=True)
sh = json.load(io.open('ledgers/_lj_mkt_sheets.json', encoding='utf-8'))
key_by_base = dict(zip(sh['bases'], sh['files']))


def build(prefix, bases, maxw=1400, maxh=1550):
    ims = []
    for b in bases:
        k = key_by_base.get(b)
        if not k:
            print('MISSING', b)
            continue
        p = os.path.join(RAW, k)
        if not os.path.exists(p):
            print('NOFILE', b, k)
            continue
        ims.append((b, Image.open(p).convert('RGB')))
    out, batch, w, h, names = [], [], 0, 0, []
    def flush():
        nonlocal batch, w, h, names
        if not batch:
            return
        canvas = Image.new('RGB', (max(w, 10), h), 'white')
        y = 0
        for _, im in batch:
            canvas.paste(im, (0, y))
            y += im.height + 8
        p = '%s/%s_%d.jpg' % (OUT, prefix, len(out))
        canvas.save(p, quality=90)
        out.append((p, canvas.size, list(names)))
        batch, w, h, names = [], 0, 0, []
    for b, im in ims:
        if im.width > maxw:
            im = im.resize((maxw, int(im.height * maxw / im.width)), Image.LANCZOS)
        if batch and h + im.height + 8 > maxh:
            flush()
        batch.append((b, im))
        w = max(w, im.width)
        h += im.height + 8
        names.append(b)
    flush()
    for p, size, ns in out:
        print(p, size, len(ns), ','.join(x.split('.')[0] for x in ns))
    return out


if __name__ == '__main__':
    build(sys.argv[1], sys.argv[2:])
