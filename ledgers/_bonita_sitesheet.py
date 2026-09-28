#!/usr/bin/env python3
"""Contact sheets over the figures of *judged* site pages only (worker elicitation-6f).

  python ledgers/_bonita_sitesheet.py OUT COLS TW TH [START COUNT]
  python ledgers/_bonita_sitesheet.py list          # the figure list, numbered
  python ledgers/_bonita_sitesheet.py hot           # only figures whose name looks diagram-ish
"""
import json
import pathlib
import re
import sys
import urllib.parse

ELI = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ELI / "ledgers"))
import _bonita_rows as S  # noqa: E402

D = ELI / "ledgers" / "_bonita" / "figs"
MAN = D / "manifest.json"
HOT = re.compile(r"bpmn|diagram|process|workflow|orchestrat|screen|studio|model|dash|flow", re.I)


def files():
    """[manifest row] for figures referenced by judged site pages, one row per file."""
    judged = set()
    for url, rec in S.records():
        if "documentation." in url:
            continue
        sc = S.screen(url, S.html_of(rec))
        if S.tier(url, sc) == "judged":
            judged.add(url)
            for f in sc["figure_meta"]:
                if f["src"]:
                    judged.add(urllib.parse.urljoin(url, f["src"]))
    man = json.loads(MAN.read_text(encoding="utf-8"))
    out, seen = [], set()
    for m in man:
        if m["url"] in judged and m.get("file") and (D / m["file"]).exists():
            if m["file"] in seen:
                continue
            seen.add(m["file"])
            out.append(m)
    return out


def sheet():
    from PIL import Image, ImageDraw
    stem, cols, tw, th = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    start = int(sys.argv[6]) if len(sys.argv) > 6 else 0
    count = int(sys.argv[7]) if len(sys.argv) > 7 else 60
    man = [m for m in files() if not m["name"].lower().endswith(".svg")]
    svg = [m for m in files() if m["name"].lower().endswith(".svg")]
    chunk = man[start:start + count]
    rows = (len(chunk) + cols - 1) // cols
    sh = Image.new("RGB", (cols * tw, max(1, rows) * th), (248, 248, 248))
    d = ImageDraw.Draw(sh)
    for k, m in enumerate(chunk):
        x, y = (k % cols) * tw, (k // cols) * th
        try:
            im = Image.open(D / m["file"])
            if im.mode in ("P", "RGBA", "LA"):
                im = im.convert("RGBA")
                bg = Image.new("RGB", im.size, (255, 255, 255))
                bg.paste(im, mask=im.split()[-1])
                im = bg
            im = im.convert("RGB")
        except Exception:  # noqa: BLE001
            d.text((x + 5, y + 5), "ERR", fill=(200, 0, 0))
            continue
        w, h = im.size
        sc = min((tw - 8) / w, (th - 30) / h, 2.0)
        sh.paste(im.resize((max(1, int(w * sc)), max(1, int(h * sc))), Image.LANCZOS),
                 (x + 4, y + 26))
        d.rectangle([x, y, x + tw - 1, y + th - 1], outline=(165, 165, 165))
        nm = re.sub(r"^[0-9a-f]{20,}_", "", urllib.parse.unquote(m["name"]))
        d.text((x + 4, y + 4), "%d %s [%dx%d]" % (start + k + 1, nm[-44:], w, h), fill=(0, 0, 0))
        d.text((x + 4, y + 15), m["page"].split("//")[1][:52], fill=(90, 90, 90))
        print("%-4d %-46s %s" % (start + k + 1, nm[-44:], m["page"]))
    sh.save("%s.png" % stem)
    print("wrote %s.png (%d tiles, %d-%d of %d raster; %d svg omitted)"
          % (stem, len(chunk), start + 1, start + len(chunk), len(man), len(svg)))


def hot():
    for k, m in enumerate(files(), 1):
        nm = re.sub(r"^[0-9a-f]{20,}_", "", urllib.parse.unquote(m["name"]))
        if HOT.search(nm):
            print("%-4d %-46s %s" % (k, nm[-44:], m["page"]))


def listing():
    for k, m in enumerate(files(), 1):
        nm = re.sub(r"^[0-9a-f]{20,}_", "", urllib.parse.unquote(m["name"]))
        print("%-4d %-46s %s" % (k, nm[-44:], m["page"].split("//")[1][:60]))


def rlist():
    """The raster-only numbering used by `sheet` (SVGs are listed separately)."""
    for k, m in enumerate([x for x in files() if not x["name"].lower().endswith(".svg")], 1):
        nm = re.sub(r"^[0-9a-f]{20,}_", "", urllib.parse.unquote(urllib.parse.unquote(m["name"])))
        print("%-4d %-46s %s" % (k, nm[-46:], m["page"].split("//")[1][:60]))
    for k, m in enumerate([x for x in files() if x["name"].lower().endswith(".svg")], 1):
        nm = re.sub(r"^[0-9a-f]{20,}_", "", urllib.parse.unquote(urllib.parse.unquote(m["name"])))
        print("svg%-4d %-44s %s" % (k, nm[-44:], m["page"].split("//")[1][:60]))


if __name__ == "__main__":
    mode = sys.argv[1]
    {"sheet": sheet, "hot": hot, "list": listing, "rlist": rlist}[mode]()
