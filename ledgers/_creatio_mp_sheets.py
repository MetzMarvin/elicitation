#!/usr/bin/env python3
"""Tile the marketplace candidates' figures into numbered contact sheets for the visual pass.

Which figures need eyes: every figure of every listing whose page mentions a process model, minus the
ones the vendor's own file name marks as something else (logos, team photos, award badges, highlights,
banners). The remaining figures are tiled with their listing slug and file name; the sheet is what the
judgement is read off. Figures that look like a process-designer canvas are then opened at full size
(`--zoom N`).

  python ledgers/_creatio_mp_sheets.py            # build all sheets, print the index
  python ledgers/_creatio_mp_sheets.py --zoom 12  # also download figures 10..14 at full size
"""
import io
import json
import pathlib
import re
import sys
import urllib.request

from PIL import Image, ImageDraw, ImageOps

ELI = pathlib.Path(__file__).resolve().parents[1]
OUT = ELI / "ledgers" / "_creatio"
CACHE = OUT / "mpfigs"
BASE = "https://marketplace.creatio.com"
HDRS = {"User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/153.0.0.0 Safari/537.36 Edg/153.0.0.0"),
        "Referer": BASE + "/catalog"}
# the vendor's file names that cannot be a process model
NOISE = re.compile(r"logo|team|photo|avatar|portrait|ceo|founder|highlight|banner|badge|award|icon"
                   r"|headshot|author|signature|qrcode|qr[-_]|people|person|staff|speaker|pricing"
                   r"|partner|sponsor|testimonial|quote|star|rating|g2|capterra|forrester|gartner", re.I)
PER_SHEET = 36
COLS = 6
CW, CH = 300, 230


def cached_image(src):
    CACHE.mkdir(exist_ok=True)
    name = re.sub(r"[^A-Za-z0-9._-]", "_", src.split("/")[-1])[:120]
    p = CACHE / name
    if not p.exists() or p.stat().st_size < 800:
        with urllib.request.urlopen(urllib.request.Request(src, headers=HDRS), timeout=90) as f:
            p.write_bytes(f.read())
    return p


def collect():
    ctx = json.loads((OUT / "mp_figctx.json").read_text(encoding="utf-8"))
    pages = json.loads((OUT / "mp_pages.json").read_text(encoding="utf-8"))
    blogpages = json.loads((OUT / "mp_blog_pages.json").read_text(encoding="utf-8"))
    sel = []
    for link, figs in sorted(ctx.items()):
        p = pages.get(link) or blogpages.get(link) or {}
        byname = {i["src"].split("/")[-1]: i["src"] for i in (p.get("imgs") or [])}
        for f in figs:
            if NOISE.search(f["file"]):
                continue
            src = byname.get(f["file"]) or (BASE + "/sites/marketplace/files/" + f["file"])
            sel.append({"link": link, "file": f["file"], "heading": f["heading"],
                        "src": src, "alt": f.get("alt") or ""})
    return sel


def sheets(sel):
    OUT.mkdir(exist_ok=True)
    made = []
    for s in range(0, len(sel), PER_SHEET):
        part = sel[s:s + PER_SHEET]
        rows = (len(part) + COLS - 1) // COLS
        sheet = Image.new("RGB", (COLS * CW, rows * CH + 10), "white")
        d = ImageDraw.Draw(sheet)
        for k, f in enumerate(part):
            n = s + k + 1
            x, y = (k % COLS) * CW + 5, (k // COLS) * CH + 30
            try:
                im = Image.open(io.BytesIO(cached_image(f["src"]).read_bytes())).convert("RGB")
            except Exception as e:
                im = Image.new("RGB", (CW - 12, CH - 46), "#eee")
                ImageDraw.Draw(im).text((4, 4), "ERR %s" % type(e).__name__, fill="red")
            im = ImageOps.contain(im, (CW - 12, CH - 46))
            slug = f["link"].split("/app/")[-1].split("/blog/")[-1][:22]
            d.text((x, y - 24), "%d %s | %s" % (n, slug, f["file"][:34]), fill="black")
            sheet.paste(im, (x, y))
            d.rectangle([x - 2, y - 2, x + im.width + 2, y + im.height + 2], outline="blue")
        p = OUT / ("mp_sheet_%02d.png" % (s // PER_SHEET + 1))
        sheet.save(p)
        made.append((str(p), s + 1, s + len(part)))
    return made


def main():
    sel = collect()
    print("figures selected for the visual pass:", len(sel))
    (OUT / "mp_figsel.json").write_text(json.dumps(sel, indent=1, ensure_ascii=False), encoding="utf-8")
    for p, a, b in sheets(sel):
        print("  %s  (figures %d-%d)" % (p, a, b))
    if "--zoom" in sys.argv:
        i = int(sys.argv[sys.argv.index("--zoom") + 1])
        lo, hi = max(1, i - 2), min(len(sel), i + 2)
        for n in range(lo, hi + 1):
            f = sel[n - 1]
            print("ZOOM %d: %s" % (n, cached_image(f["src"])))


if __name__ == "__main__":
    main()
