#!/usr/bin/env python3
"""Second visual pass over www.creatio.com/page/bpmn: the four business-process figures not yet
looked at, plus the five designer-palette figures, tiled for one look.

The page is the vendor's marketing landing page for BPMN. First pass looked at four of the eight
process figures (purchase request, converting lead to sale, closing a sale, recruitment) and at the
'System Actions' palette figure. This sheet adds the other four process figures (event
participation planning, business trip request, employee onboarding, termination of employment) and
the remaining palette figures (User Actions, Start events, Logical operators).
"""
import json, pathlib, urllib.request
from PIL import Image, ImageDraw

ELI = pathlib.Path(__file__).resolve().parents[1]
OUT = ELI / "ledgers" / "_creatio"
FIGS = OUT / "figs"
BASE = "https://www.creatio.com/page/sites/landings/files/2019-12/"
PROC = ["2stand_preparation", "3businesstriprequest", "5onboarding1", "6termination_0"]
PAL = ["bpmn_pic1", "bpmn_pic2", "bpmn_pic3", "bpmn_pic4", "bpmn_pic5"]
ALT = {"2stand_preparation": "Event participation planning", "3businesstriprequest": "Business trip request",
       "5onboarding1": "Employee onboarding", "6termination_0": "Termination of employment",
       "bpmn_pic1": "User Actions", "bpmn_pic2": "System Actions in Creatio",
       "bpmn_pic3": "Start events", "bpmn_pic4": "Logical operators", "bpmn_pic5": "Subprocesses"}

def get(name):
    p = FIGS / ("crm_" + name + ".png")
    if not p.exists() or p.stat().st_size < 500:
        req = urllib.request.Request(BASE + name + ".png", headers={"User-Agent": "Mozilla/5.0",
                                     "Referer": "https://www.creatio.com/page/bpmn"})
        p.write_bytes(urllib.request.urlopen(req, timeout=60).read())
    return Image.open(p).convert("RGB")

cellw, cellh = 700, 520
sheet = Image.new("RGB", (cellw * 2, cellh * 4 + 60), "white")
d = ImageDraw.Draw(sheet)
for i, name in enumerate(PROC):
    im = get(name)
    im.thumbnail((cellw - 8, cellh - 34))
    x, y = (i % 2) * cellw + 4, (i // 2) * cellh + 30
    d.text((x + 2, y - 24), f"{i+1}. {name}  [{ALT[name]}]  native {im.width}x{im.height} shown",
           fill="black")
    sheet.paste(im, (x, y))
    d.rectangle([x - 2, y - 2, x + im.width + 2, y + im.height + 2], outline="red")
# palette strip: native width, one row
y = cellh * 2 + 40
x = 4
for j, name in enumerate(PAL):
    im = get(name)
    im.thumbnail((420, 520))
    d.text((x, y - 24), f"P{j+1}. {ALT[name]} ({im.width}x{im.height})", fill="black")
    sheet.paste(im, (x, y))
    d.rectangle([x - 2, y - 2, x + im.width + 2, y + im.height + 2], outline="blue")
    x += im.width + 20
sheet.save(OUT / "crm_sheet2.png")
print("saved", OUT / "crm_sheet2.png", sheet.size)
