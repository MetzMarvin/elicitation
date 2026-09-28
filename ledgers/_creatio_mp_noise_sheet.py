#!/usr/bin/env python3
"""Tile the figures the contact sheets' noise filter dropped, for the phase-2 candidate listings.

The sheets dropped anything whose file name matched NOISE (logo|team|photo|...|highlight|...), which
also caught families that are NOT chrome at all - "Highlighted screenshot 1.png", "sc2_...StaffUnitPage",
"Experceo-QRCodeGenerator....png". This sheet puts them in front of the eye so the phase-2 notes never
claim to have looked at a figure they did not.

  python ledgers/_creatio_mp_noise_sheet.py OUT_STEM
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import _creatio_mp_rows as M  # noqa: E402
import _creatio_mp_sheets as S  # noqa: E402
from PIL import Image, ImageDraw  # noqa: E402

OUT = pathlib.Path(__file__).resolve().parent / "_creatio"
items = json.loads((OUT / "mp_items.json").read_text(encoding="utf-8"))["items"]
pages = json.loads((OUT / "mp_pages.json").read_text(encoding="utf-8"))
blog = json.loads((OUT / "mp_blog_index.json").read_text(encoding="utf-8"))["articles"]
bp = json.loads((OUT / "mp_blog_pages.json").read_text(encoding="utf-8"))
sel = json.loads((OUT / "mp_figsel.json").read_text(encoding="utf-8"))
shown = {(e["link"], e["file"]) for e in sel}

todo = []
for kind, link in [("app", i["link"]) for i in items] + [("blog", b) for b in blog]:
    p = (pages if kind == "app" else bp).get(link) or {}
    if p.get("status") != "ok" or not M.EYES.search(M.hay_of(p)):
        continue
    for i in (p.get("imgs") or []):
        f = i["src"].split("/")[-1]
        if (link, f) not in shown:
            todo.append((link, f, i["src"]))

COLS, TW, TH = 6, 330, 300
rows = (len(todo) + COLS - 1) // COLS
sheet = Image.new("RGB", (COLS * TW, rows * TH), (250, 250, 250))
d = ImageDraw.Draw(sheet)
for k, (link, f, src) in enumerate(todo):
    x, y = (k % COLS) * TW, (k // COLS) * TH
    try:
        im = Image.open(S.cached_image(src)).convert("RGB")
    except Exception as e:
        d.text((x + 6, y + 6), "ERR %s %s" % (f[:30], e), fill=(200, 0, 0))
        continue
    w, h = im.size
    sc = min((TW - 10) / w, (TH - 30) / h, 1.6)
    sheet.paste(im.resize((max(1, int(w * sc)), max(1, int(h * sc))), Image.LANCZOS), (x + 5, y + 26))
    d.rectangle([x, y, x + TW - 1, y + TH - 1], outline=(170, 170, 170))
    d.text((x + 5, y + 7), "%d %s | %s [%dx%d]" % (k + 1, link.replace("/app/", "")[:22],
                                                   f[:34], w, h), fill=(0, 0, 0))
    print("%-4d %-40s %s" % (k + 1, link, f))
sheet.save("%s.png" % sys.argv[1])
print("wrote %s.png (%d figures)" % (sys.argv[1], len(todo)))
