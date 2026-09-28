#!/usr/bin/env python3
"""Look at the figures of the pages whose *article region mentions AI* but which sit outside
RULINGS and whose figures are not diagram-named.

Those pages are exactly the ones the screen would exclude mechanically (E0) even though their
prose talks about AI: the highest-value blind spot in this source, because if any of them publishes
an AI-enabled process diagram behind a UI-ish attachment name, the screen would never surface it.

  python ledgers/_scheer_aipp.py download   # fetch those figures    -> ledgers/_scheer/aipp/
  python ledgers/_scheer_aipp.py sheet OUT COLS TW TH START COUNT
"""
import hashlib
import json
import pathlib
import sys
import time
import urllib.parse
import urllib.request

ELI = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ELI / "ledgers"))
import _scheer_build as B  # noqa: E402
import _scheer_rows as S  # noqa: E402

DEST = ELI / "ledgers" / "_scheer" / "aipp"
MAN = DEST / "manifest.json"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126 Safari/537.36"}


def pages():
    """[(path, meta)] for the AI-mentioning pages that are not hand-ruled."""
    out = []
    for path, meta in B.records():
        if path in B.W.RULINGS:
            continue
        sc = B.screen(path)
        if sc and sc["ai"]:
            out.append((path, meta))
    return out


def cand():
    out = []
    for path, meta in pages():
        t = B.html_of(path)
        for x in S.figs(t or ""):
            name = x["src"].split("/")[-1].split("?")[0]
            out.append((path, name, urllib.parse.urljoin(meta["url"], x["src"])))
    return out


def download():
    DEST.mkdir(parents=True, exist_ok=True)
    rows = cand()
    man = json.loads(MAN.read_text(encoding="utf-8")) if MAN.exists() else []
    have = {m["url"].split("?")[0] for m in man}
    print("AI-mentioning pages: %d | figures: %d | already have: %d" % (len(pages()), len(rows), len(have)))
    todo = [r for r in rows if r[2].split("?")[0] not in have]
    miss = 0
    for path, name, url in todo:
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as fh:
                d = fh.read()
        except Exception as e:
            print("  ERR", name, repr(e)[:50], flush=True)
            miss += 1
            time.sleep(0.8)
            continue
        f = DEST / ("%s__%s" % (hashlib.sha1(d).hexdigest()[:12], name))
        if not f.exists():
            f.write_bytes(d)
        man.append({"page": path, "name": name, "url": url, "file": f.name, "bytes": len(d)})
        MAN.write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
        time.sleep(0.6)
    print("errors %d | total cached %d" % (miss, len(man)))


def sheet():
    from PIL import Image, ImageDraw
    stem, cols, tw, th = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    start = int(sys.argv[6]) if len(sys.argv) > 6 else 0
    count = int(sys.argv[7]) if len(sys.argv) > 7 else 64
    man = [m for m in json.loads(MAN.read_text(encoding="utf-8")) if (DEST / m["file"]).exists()]
    man.sort(key=lambda m: (m["page"], m["name"]))
    chunk = man[start:start + count]
    rows = (len(chunk) + cols - 1) // cols
    sh = Image.new("RGB", (cols * tw, max(1, rows) * th), (248, 248, 248))
    d = ImageDraw.Draw(sh)
    for k, m in enumerate(chunk):
        x, y = (k % cols) * tw, (k // cols) * th
        try:
            im = Image.open(DEST / m["file"]).convert("RGB")
        except Exception:
            d.text((x + 5, y + 5), "ERR", fill=(200, 0, 0))
            continue
        w, h = im.size
        sc = min((tw - 8) / w, (th - 26) / h, 2.0)
        sh.paste(im.resize((max(1, int(w * sc)), max(1, int(h * sc))), Image.LANCZOS), (x + 4, y + 22))
        d.rectangle([x, y, x + tw - 1, y + th - 1], outline=(165, 165, 165))
        d.text((x + 4, y + 4), "%d %s [%dx%d]" % (k + 1, m["name"][:38], w, h), fill=(0, 0, 0))
        d.text((x + 4, y + 13), m["page"].split("/")[-1][:46], fill=(90, 90, 90))
        print("%-3d %-44s %s" % (k + 1, m["name"][:44], m["page"]))
    sh.save("%s.png" % stem)
    print("wrote %s.png (tiles %d-%d of %d)" % (stem, start + 1, start + len(chunk), len(man)))


def zoom():
    """A big-tile sheet of named figures, picked by attachment name (first match per name)."""
    from PIL import Image, ImageDraw
    stem, cols, tw, th = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    want = sys.argv[6:]
    man = [m for m in json.loads(MAN.read_text(encoding="utf-8")) if (DEST / m["file"]).exists()]
    picked = []
    for nm in want:
        for m in man:
            if m["name"] == nm:
                picked.append(m)
                break
        else:
            print("  MISSING", nm)
    rows = (len(picked) + cols - 1) // cols
    sh = Image.new("RGB", (cols * tw, max(1, rows) * th), (248, 248, 248))
    d = ImageDraw.Draw(sh)
    for k, m in enumerate(picked):
        x, y = (k % cols) * tw, (k // cols) * th
        im = Image.open(DEST / m["file"])
        if im.mode in ("P", "RGBA"):
            im = im.convert("RGBA")
            bg = Image.new("RGB", im.size, (255, 255, 255))
            bg.paste(im, mask=im.split()[-1])
            im = bg
        im = im.convert("RGB")
        w, h = im.size
        sc = min((tw - 8) / w, (th - 26) / h, 2.0)
        sh.paste(im.resize((max(1, int(w * sc)), max(1, int(h * sc))), Image.LANCZOS), (x + 4, y + 22))
        d.rectangle([x, y, x + tw - 1, y + th - 1], outline=(165, 165, 165))
        d.text((x + 4, y + 4), "%d %s [%dx%d]" % (k + 1, m["name"][:60], w, h), fill=(0, 0, 0))
        d.text((x + 4, y + 13), m["page"], fill=(90, 90, 90))
        print("%-3d %-52s %s" % (k + 1, m["name"], m["page"]))
    sh.save("%s.png" % stem)
    print("wrote %s.png (%d tiles)" % (stem, len(picked)))


if __name__ == "__main__":
    if sys.argv[1] == "download":
        download()
    elif sys.argv[1] == "sheet":
        sheet()
    elif sys.argv[1] == "zoom":
        zoom()
