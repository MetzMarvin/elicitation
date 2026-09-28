#!/usr/bin/env python3
"""Download the figures of the in-scope scheer-pas pages and tile them into contact sheets.

Every docs page offers a Markdown variant (`<path>.md`) whose body carries the page's own
attachment URLs, so the figure list is read from the page, never guessed. Figures go to
ledgers/_scheer/figs/, one contact sheet per group, at a size the eye can read.

  python ledgers/_scheer_figs.py download     # fetch the figures named in ledgers/_scheer/md/*.md
  python ledgers/_scheer_figs.py sheet OUT COLS TILE_W TILE_H  # tile them
"""
import json
import pathlib
import re
import sys
import time
import urllib.request

ELI = pathlib.Path(__file__).resolve().parents[1]
OUT = ELI / "ledgers" / "_scheer"
MD = OUT / "md"
FIGS = OUT / "figs"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126 Safari/537.36"}


def harvest():
    """(page-stem, alt, url) for every attachment a page's Markdown references."""
    rows = []
    for f in sorted(MD.glob("*.md")):
        t = f.read_text(encoding="utf-8")
        for m in re.finditer(r"!\[([^\]]*)\]\((https://doc\.scheer-pas\.com/__attachments/[^\)\s]+)\)", t):
            url = m.group(2)
            rows.append((f.stem, m.group(1), url))
    return rows


def download():
    FIGS.mkdir(parents=True, exist_ok=True)
    rows = harvest()
    print("figures referenced by the in-scope pages:", len(rows))
    man = []
    for k, (page, alt, url) in enumerate(rows, 1):
        name = url.split("/")[-1].split("?")[0]
        stem = "%s__%s" % (page.split("__")[-1], name)
        dest = FIGS / stem
        if not (dest.exists() and dest.stat().st_size > 1000):
            try:
                r = urllib.request.Request(url, headers=UA)
                with urllib.request.urlopen(r, timeout=60) as fh:
                    dest.write_bytes(fh.read())
            except Exception as e:
                print("  ERR", name, repr(e)[:80])
                time.sleep(1)
                continue
            time.sleep(1.0)
        man.append({"page": page, "alt": alt, "url": url, "file": stem,
                    "bytes": dest.stat().st_size})
    (OUT / "figs_manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
    print("cached:", len(man), "->", FIGS)


def sheet():
    from PIL import Image, ImageDraw
    stem, cols, tw, th = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    man = json.loads((OUT / "figs_manifest.json").read_text(encoding="utf-8"))
    man = [m for m in man if (FIGS / m["file"]).exists()]
    rows = (len(man) + cols - 1) // cols
    sh = Image.new("RGB", (cols * tw, rows * th), (250, 250, 250))
    d = ImageDraw.Draw(sh)
    for k, m in enumerate(man):
        x, y = (k % cols) * tw, (k // cols) * th
        try:
            im = Image.open(FIGS / m["file"]).convert("RGB")
        except Exception as e:
            d.text((x + 5, y + 5), "ERR %s" % e, fill=(200, 0, 0))
            continue
        w, h = im.size
        sc = min((tw - 10) / w, (th - 30) / h, 1.8)
        sh.paste(im.resize((max(1, int(w * sc)), max(1, int(h * sc))), Image.LANCZOS), (x + 5, y + 26))
        d.rectangle([x, y, x + tw - 1, y + th - 1], outline=(170, 170, 170))
        d.text((x + 5, y + 7), "%d %s [%dx%d]" % (k + 1, m["file"][:60], w, h), fill=(0, 0, 0))
        print("%-4d %-70s %s" % (k + 1, m["page"], m["file"]))
    sh.save("%s.png" % stem)
    print("wrote %s.png (%d tiles)" % (stem, len(man)))


if __name__ == "__main__":
    if sys.argv[1] == "download":
        download()
    elif sys.argv[1] == "sheet":
        sheet()
