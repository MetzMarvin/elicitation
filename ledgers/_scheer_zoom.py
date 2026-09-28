#!/usr/bin/env python3
"""Tile chosen scheer-pas figures at (near) native size, so the eye can settle a notation question.

  python ledgers/_scheer_zoom.py OUT_STEM COLS ROWS <file-name fragment> ...
Fragments are matched against ledgers/_scheer/figs/ ; the sheet is labelled with the figure's own
file name and pixel size, so a ruling can cite exactly what was looked at.
"""
import json
import pathlib
import sys

from PIL import Image, ImageDraw

OUT = pathlib.Path(__file__).resolve().parent / "_scheer"
FIGS = OUT / "figs"
MAN = json.loads((OUT / "figs_manifest.json").read_text(encoding="utf-8"))


def find(frag):
    hits = [m for m in MAN if frag.lower() in m["file"].lower()]
    return hits[0] if hits else None


def main():
    stem, cols, rows = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    frags = sys.argv[4:]
    TW, TH = 1180, 760
    sheet = Image.new("RGB", (cols * TW, rows * TH), (250, 250, 250))
    d = ImageDraw.Draw(sheet)
    for k, frag in enumerate(frags[:cols * rows]):
        m = find(frag)
        x, y = (k % cols) * TW, (k // cols) * TH
        if not m:
            d.text((x + 8, y + 8), "NO MATCH " + frag, fill=(200, 0, 0))
            continue
        p = FIGS / m["file"]
        try:
            im = Image.open(p).convert("RGB")
        except Exception as e:
            d.text((x + 8, y + 8), "ERR %s %s" % (m["file"], e), fill=(200, 0, 0))
            continue
        w, h = im.size
        sc = min((TW - 12) / w, (TH - 34) / h, 2.4)
        im = im.resize((max(1, int(w * sc)), max(1, int(h * sc))), Image.LANCZOS)
        sheet.paste(im, (x + 6, y + 30))
        d.rectangle([x, y, x + TW - 1, y + TH - 1], outline=(180, 180, 180))
        d.text((x + 6, y + 9), "%s  [%dx%d]" % (m["file"][:110], w, h), fill=(0, 0, 0))
        print("cell %d: %s (%dx%d)" % (k, m["file"], w, h))
    sheet.save("%s.png" % stem)
    print("wrote %s.png" % stem)


if __name__ == "__main__":
    main()
