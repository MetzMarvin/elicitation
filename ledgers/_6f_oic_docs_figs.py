#!/usr/bin/env python3
"""Download the figures of every docs page that publishes one, and build contact sheets.

Purpose: give the worker a *real* look at the docs figures (the Pass 2 visual pass) so the
per-page verdict can say what the artefact actually is, instead of inferring it.

Read-only GETs, ~1 request/second. Output: ledgers/_6f_docs/figs/ + sheet_N.png + figs_index.json
"""
import json
import pathlib
import re
import time
import urllib.parse
import urllib.request

from PIL import Image

ELI = pathlib.Path(__file__).resolve().parents[1]
OUT = ELI / "ledgers" / "_6f_docs"
FIGS = OUT / "figs"
FIGS.mkdir(parents=True, exist_ok=True)
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128 Safari/537.36")
CH = re.compile(r"(sp_common|/icons?/|[-_/]icon|icon[-_.]|logo|bullet|/nav|_nav|note\.|caution"
                r"|warning|arrow|expand|collapse|checkmark|sprite|spacer|blank|1x1|favicon)", re.I)

survey = (json.loads((OUT / "survey.json").read_text(encoding="utf-8"))
          + json.loads((OUT / "survey_recipes.json").read_text(encoding="utf-8")))

items = []          # (page_url, page_title, img_src_abs)
seen_src = set()
for s in survey:
    figs = [i for i in (s.get("imgs") or [])
            if not CH.search(i.get("src", "")) and (i.get("w") is None or i.get("w") > 32)]
    for i in figs[:2]:                                   # up to two figures per page
        src = urllib.parse.urljoin(s["url"], i["src"])
        items.append((s["url"], s.get("title") or "", src))
        seen_src.add(src)

print("figure downloads:", len(items), "distinct:", len(seen_src), flush=True)

index = []
for k, (page, title, src) in enumerate(items, 1):
    name = re.sub(r"[^A-Za-z0-9._-]", "_", urllib.parse.urlparse(src).path.split("/")[-1])
    name = "%03d_%s" % (k, name)
    dest = FIGS / name
    if not dest.exists():
        try:
            req = urllib.request.Request(src, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=45) as r:
                dest.write_bytes(r.read())
            time.sleep(0.8)
        except Exception as exc:                          # noqa: BLE001
            print("ERR", k, src, exc, flush=True)
            continue
    index.append({"cell": k, "page": page, "title": title, "src": src, "file": name})
    if k % 25 == 0:
        print("...", k, flush=True)

(OUT / "figs_index.json").write_text(json.dumps(index, indent=1, ensure_ascii=False),
                                     encoding="utf-8")

# ---- contact sheets: 6 columns x 5 rows, one image per cell ------------------
COLS, ROWS, TW, TH, PAD, LBL = 6, 5, 250, 190, 8, 26
per = COLS * ROWS
sheets = 0
for start in range(0, len(index), per):
    chunk = index[start:start + per]
    W = COLS * (TW + PAD) + PAD
    H = ROWS * (TH + LBL + PAD) + PAD
    sheet = Image.new("RGB", (W, H), "white")
    for j, it in enumerate(chunk):
        try:
            im = Image.open(FIGS / it["file"]).convert("RGB")
        except Exception:                                 # noqa: BLE001
            continue
        im.thumbnail((TW, TH))
        cx = PAD + (j % COLS) * (TW + PAD) + (TW - im.width) // 2
        cy = PAD + (j // COLS) * (TH + LBL + PAD) + (TH - im.height) // 2
        sheet.paste(im, (cx, cy))
    sheets += 1
    sheet.save(OUT / ("sheet_%d.png" % sheets))
    print("sheet_%d.png cells %d..%d" % (sheets, chunk[0]["cell"], chunk[-1]["cell"]), flush=True)

print("done. figures:", len(index), "sheets:", sheets, flush=True)
