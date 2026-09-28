#!/usr/bin/env python3
"""Tile chosen marketplace figures at (near) native size, so the eye can settle a notation question.

  python ledgers/_creatio_mp_zoom.py OUT STEM 2 3  /app/x frag  /app/y frag ...
    OUT   = output stem (sheet file becomes OUT_01.png ...)
    STEM  = how many columns, rows are inferred from the pair count
Each argument pair is (listing link, file-name fragment). The images come from the same on-disk
cache the contact sheets use, so nothing is re-downloaded.
"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import _creatio_mp_sheets as S  # noqa: E402
from PIL import Image, ImageDraw  # noqa: E402

OUT = pathlib.Path(__file__).resolve().parent / "_creatio"
pages = json.loads((OUT / "mp_pages.json").read_text(encoding="utf-8"))
blog = json.loads((OUT / "mp_blog_pages.json").read_text(encoding="utf-8"))
ALL = dict(pages)
ALL.update(blog)


SEL = json.loads((OUT / "mp_figsel.json").read_text(encoding="utf-8"))


def find(link, frag):
    """A pair is either (link, name-fragment) or ("#N", "") - the Nth figure of the contact sheets."""
    if link.startswith("#"):
        e = SEL[int(link[1:]) - 1]
        link, frag = e["link"], e["file"]
    p = ALL.get(link) or {}
    for i in (p.get("imgs") or []):
        if frag.lower() in i["src"].split("/")[-1].lower():
            return i["src"]
    return None


def main():
    stem = sys.argv[1]
    cols = int(sys.argv[2])
    rows = int(sys.argv[3])
    pairs = [(sys.argv[i], sys.argv[i + 1]) for i in range(4, len(sys.argv) - 1, 2)]
    TW, TH = 1180, 760
    sheet = Image.new("RGB", (cols * TW, rows * TH), (250, 250, 250))
    d = ImageDraw.Draw(sheet)
    for k, (link, frag) in enumerate(pairs[:cols * rows]):
        src = find(link, frag)
        x, y = (k % cols) * TW, (k // cols) * TH
        label = "%s | %s" % (link, frag)
        if not src:
            d.text((x + 6, y + 6), "NO MATCH " + label, fill=(200, 0, 0))
            continue
        path = S.cached_image(src)
        try:
            im = Image.open(path).convert("RGB")
        except Exception as e:
            d.text((x + 6, y + 6), "ERR %s %s" % (label, e), fill=(200, 0, 0))
            continue
        w, h = im.size
        sc = min((TW - 12) / w, (TH - 34) / h, 2.2)
        im = im.resize((max(1, int(w * sc)), max(1, int(h * sc))), Image.LANCZOS)
        sheet.paste(im, (x + 6, y + 28))
        d.rectangle([x, y, x + TW - 1, y + TH - 1], outline=(180, 180, 180))
        d.text((x + 6, y + 8), "%s  [%dx%d]" % (label[:150], w, h), fill=(0, 0, 0))
        print("cell %d: %s" % (k, label))
    sheet.save("%s.png" % stem)
    print("wrote %s.png" % stem)


if __name__ == "__main__":
    main()
