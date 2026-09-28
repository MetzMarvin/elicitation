# -*- coding: utf-8 -*-
"""Contact sheets over the marketing assets, one tile per *distinct asset name*
(the same name shipped as .webp and .png is one picture), 48 tiles (8x6) at
340px, tile labels '#idx name'. Writes ledgers/_lj_mkt_sheets.json:
files (chosen download key per name), bases (asset name), sheets."""
import io, json, os, math
from PIL import Image, ImageDraw

SRC = 'ledgers/loyjoy.raw/mkt_all'
OUT = 'ledgers/loyjoy.raw/sheets'
os.makedirs(OUT, exist_ok=True)


def name_of(k):
    """download key 'name__hash8.ext' -> asset name 'name'"""
    stem, _, ext = k.rpartition('.')
    if '__' not in stem:
        return stem
    return stem.partition('__')[0]


best = {}
for f in os.listdir(SRC):
    p = os.path.join(SRC, f)
    if os.path.getsize(p) <= 200:
        continue
    nm = name_of(f)
    try:
        w, h = Image.open(p).size
    except Exception:
        continue
    score = w * h
    if nm not in best or score > best[nm][0]:
        best[nm] = (score, f, w, h)
names = sorted(best)
files = [best[n][1] for n in names]
print('distinct asset names', len(names), '(from', len(os.listdir(SRC)), 'files)')
T, C, R = 340, 8, 6
per = C * R
sheets = []
for s in range(math.ceil(len(files) / per)):
    chunk = files[s * per:(s + 1) * per]
    im = Image.new('RGB', (C * T, R * T), 'white')
    d = ImageDraw.Draw(im)
    for i, f in enumerate(chunk):
        idx = s * per + i
        x, y = (i % C) * T, (i // C) * T
        try:
            im2 = Image.open(os.path.join(SRC, f)).convert('RGB')
        except Exception:
            d.text((x + 6, y + 6), 'ERR %s' % f, fill='red')
            continue
        im2.thumbnail((T - 10, T - 30))
        im.paste(im2, (x + 5, y + 26))
        d.rectangle([x + 1, y + 1, x + T - 1, y + T - 1], outline='black')
        d.text((x + 6, y + 8), '#%d %s' % (idx, names[idx][:34]), fill='blue')
    p = '%s/t%02d.jpg' % (OUT, s)
    im.save(p, quality=85)
    sheets.append({'sheet': p, 'first': s * per, 'last': s * per + len(chunk) - 1})
json.dump({'files': files, 'bases': names, 'sizes': {n: [best[n][2], best[n][3]] for n in names},
           'sheets': sheets}, io.open('ledgers/_lj_mkt_sheets.json', 'w'), indent=1)
print('sheets', len(sheets), sheets[0], sheets[-1])
