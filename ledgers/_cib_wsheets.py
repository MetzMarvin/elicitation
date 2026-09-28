# -*- coding: utf-8 -*-
"""Contact sheets for the docs figures under /webapps/ (Cockpit, Admin, Tasklist, Modeler).

Question the sheets answer, per page: do the page's figures show a *rendered BPMN
diagram* (Cockpit canvas / Modeler canvas) or only application UI (tables, forms,
dialogs, dashboards without a process canvas)?  A BPMN rendering inside the app is a
BPMN artefact -> E2-no-ai-element; pure UI is E1-not-bpmn.

usage: python ledgers/_cib_wsheets.py
"""
import io, json, os, re
from PIL import Image, ImageDraw

RAW = 'ledgers/cib-seven.raw'
OUT = os.path.join(RAW, 'sheets_ws')
DOCS = 'https://docs.cibseven.org'


def main():
    os.makedirs(OUT, exist_ok=True)
    img = json.load(io.open(os.path.join(RAW, 'img.json'), encoding='utf-8'))
    items = []
    for src, e in img.items():
        f = e.get('file') or ''
        if not f or f.lower().endswith('.svg'):
            continue
        p = os.path.join(RAW, 'img', f)
        if not os.path.exists(p):
            continue
        try:
            w, h = Image.open(p).size
        except Exception:
            continue
        if max(w, h) < 120 or 'logo.png' in src or 'creativecommons' in src:
            continue
        for pg in (e.get('pages') or []):
            if '/webapps/' in pg:
                items.append({'page': pg, 'file': f, 'w': w, 'h': h})
    items.sort(key=lambda o: (o['page'], o['file']))
    COLS, ROWS, TILE = 8, 6, 400
    per = COLS * ROWS
    manifest = []
    for s in range(0, len(items), per):
        chunk = items[s:s + per]
        sheet = Image.new('RGB', (COLS * TILE, ROWS * TILE), 'white')
        d = ImageDraw.Draw(sheet)
        meta = []
        for k, o in enumerate(chunk):
            r, c = divmod(k, COLS)
            im = Image.open(os.path.join(RAW, 'img', o['file'])).convert('RGB')
            im.thumbnail((TILE - 8, TILE - 26), Image.LANCZOS)
            x = c * TILE + (TILE - im.size[0]) // 2
            y = r * TILE + 20
            sheet.paste(im, (x, y))
            d.text((c * TILE + 3, r * TILE + 4), '#%d %dx%d %s' % (s + k, o['w'], o['h'],
                                                                   o['file'][:34]), fill='black')
            d.rectangle([c * TILE, r * TILE, c * TILE + TILE - 1, r * TILE + TILE - 1], outline='#bbbbbb')
            meta.append(o)
        fn = os.path.join(OUT, 'ws%02d.jpg' % (s // per))
        sheet.save(fn, quality=88)
        manifest.append({'sheet': fn, 'items': meta})
        print(fn, len(chunk))
    io.open(os.path.join(OUT, 'sheets_ws.json'), 'w', encoding='utf-8').write(
        json.dumps(manifest, ensure_ascii=False, indent=1))
    print('pages', len(set(o['page'] for o in items)), 'figures', len(items))


if __name__ == '__main__':
    main()
