# make contact sheets (<=1600px wide) of all media for the given listing numbers, for viewing
import sys, os, glob, json
from PIL import Image
RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uipath-marketplace.raw')
os.makedirs(os.path.join(RAW, 'view'), exist_ok=True)
for n in map(int, sys.argv[1:]):
    fs = sorted(glob.glob(os.path.join(RAW, 'media', f'{n:04d}_*')))
    ims = []
    for f in fs:
        try:
            im = Image.open(f); im.seek(0); im = im.convert('RGB'); ims.append((f, im))
        except Exception as e:
            print(n, 'unreadable', os.path.basename(f), e)
    for f, im in ims:
        print(n, os.path.basename(f), im.size)
    if not ims: continue
    W = 780 if len(ims) > 1 else 1400
    parts = [im.resize((W, max(1, int(im.height * W / im.width)))) if im.width > W else im for f, im in ims]
    cols = 2 if len(parts) > 1 else 1
    rows = [parts[i:i + cols] for i in range(0, len(parts), cols)]
    H = sum(max(p.height for p in r) + 10 for r in rows)
    sheet = Image.new('RGB', (cols * (W + 10), H), 'white'); y = 0
    for r in rows:
        for j, p in enumerate(r): sheet.paste(p, (j * (W + 10), y))
        y += max(p.height for p in r) + 10
    if H > 2600:
        sheet = sheet.resize((int(sheet.width * 2600 / H), 2600))
    sheet.save(os.path.join(RAW, 'view', f'{n:04d}.jpg'), quality=80)
