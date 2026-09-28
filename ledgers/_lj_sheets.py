# -*- coding: utf-8 -*-
"""Build contact sheets over every downloaded marketing asset, 48 tiles per sheet,
tile labels '#idx filename'.  Writes ledgers/_lj_mkt_sheets.json listing sheets."""
import io, json, os, math
from PIL import Image, ImageDraw

SRC = 'ledgers/loyjoy.raw/mkt_all'
OUT = 'ledgers/loyjoy.raw/sheets'
os.makedirs(OUT, exist_ok=True)
files = sorted(f for f in os.listdir(SRC) if os.path.getsize(os.path.join(SRC, f)) > 200)
print('assets', len(files))
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
        d.text((x + 6, y + 8), '#%d %s' % (idx, f.split('__')[0][:34]), fill='blue')
    p = '%s/s%02d.jpg' % (OUT, s)
    im.save(p, quality=85)
    sheets.append({'sheet': p, 'first': s * per, 'last': s * per + len(chunk) - 1})
json.dump({'files': files, 'sheets': sheets}, io.open('ledgers/_lj_mkt_sheets.json', 'w'), indent=1)
print('sheets', len(sheets))
for s in sheets[:3]:
    print(s)
