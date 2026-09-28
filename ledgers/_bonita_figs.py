#!/usr/bin/env python3
"""Figures of the bonitasoft/ofelia population: download, contact sheets, zooms.

Every figure of every crawled page is fetched once into ledgers/_bonita/figs/ (sha1[:12] names,
manifest with the page it came from), so a page can be judged from a contact sheet or, for
suspect tiles, re-read at native size / zoomed.

  python ledgers/_bonita_figs.py download
  python ledgers/_bonita_figs.py sheet OUT COLS TW TH [START COUNT]
  python ledgers/_bonita_figs.py zoom  OUT COLS TW TH <sha-or-name> ...
  python ledgers/_bonita_figs.py page  <url-substring>      # list the figures of matching pages
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
import _bonita_rows as S  # noqa: E402

OUT = ELI / "ledgers" / "_bonita"
DEST = OUT / "figs"
MAN = DEST / "manifest.json"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "Chrome/126 Safari/537.36"}


def cand():
    out = []
    for url, rec in S.records():
        for f in S.figs(S.region(url, S.html_of(rec))):
            src = f["src"]
            if not src or src.startswith("data:"):
                continue
            absu = urllib.parse.urljoin(url, src)
            out.append({"page": url, "name": f["name"], "alt": f["alt"],
                        "caption": f["caption"], "url": absu})
    return out


def download():
    DEST.mkdir(parents=True, exist_ok=True)
    rows = cand()
    man = json.loads(MAN.read_text(encoding="utf-8")) if MAN.exists() else []
    have = {m["url"] for m in man}
    todo = [r for r in rows if r["url"] not in have]
    print("pages %d | figures %d | cached %d | todo %d"
          % (len(S.records()), len(rows), len(man), len(todo)), flush=True)
    err = 0
    for k, r in enumerate(todo, 1):
        try:
            with urllib.request.urlopen(urllib.request.Request(r["url"], headers=UA),
                                        timeout=60) as fh:
                d = fh.read()
        except Exception as exc:  # noqa: BLE001
            print("  ERR %s %s" % (r["name"][:40], repr(exc)[:60]), flush=True)
            r["file"] = None
            r["error"] = repr(exc)[:80]
            man.append(r)
            err += 1
            time.sleep(0.8)
            continue
        f = DEST / ("%s__%s" % (hashlib.sha1(d).hexdigest()[:12], r["name"][:60]))
        if not f.exists():
            f.write_bytes(d)
        r["file"] = f.name
        r["bytes"] = len(d)
        man.append(r)
        if k % 20 == 0 or k == len(todo):
            MAN.write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
            print("  %d/%d last=%s" % (k, len(todo), r["name"][:40]), flush=True)
        time.sleep(0.5)
    MAN.write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
    print("downloaded %d | errors %d | manifest %d" % (len(todo) - err, err, len(man)))


def load_man():
    man = json.loads(MAN.read_text(encoding="utf-8"))
    return [m for m in man if m.get("file") and (DEST / m["file"]).exists()]


def sheet():
    from PIL import Image, ImageDraw
    stem, cols, tw, th = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    start = int(sys.argv[6]) if len(sys.argv) > 6 else 0
    count = int(sys.argv[7]) if len(sys.argv) > 7 else 60
    man = load_man()
    chunk = man[start:start + count]
    rows = (len(chunk) + cols - 1) // cols
    sh = Image.new("RGB", (cols * tw, max(1, rows) * th), (248, 248, 248))
    d = ImageDraw.Draw(sh)
    for k, m in enumerate(chunk):
        x, y = (k % cols) * tw, (k // cols) * th
        try:
            im = Image.open(DEST / m["file"])
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
        d.text((x + 4, y + 4), "%d %s [%dx%d]" % (start + k + 1, m["name"][:40], w, h),
               fill=(0, 0, 0))
        d.text((x + 4, y + 15), m["page"].split("//")[1][:52], fill=(90, 90, 90))
        print("%-4d %-42s %s" % (start + k + 1, m["name"][:42], m["page"]))
    sh.save("%s.png" % stem)
    print("wrote %s.png (%d tiles, %d-%d of %d)" % (stem, len(chunk), start + 1,
                                                    start + len(chunk), len(man)))


def zoom():
    from PIL import Image, ImageDraw
    stem, cols, tw, th = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    want = sys.argv[6:]
    man = load_man()
    picked = []
    for w in want:
        hits = [m for m in man if m["file"] == w or m["name"] == w or m["file"].startswith(w)]
        if hits:
            picked.append(hits[0])
        else:
            print("  MISSING", w)
    rows = (len(picked) + cols - 1) // cols
    sh = Image.new("RGB", (cols * tw, max(1, rows) * th), (248, 248, 248))
    d = ImageDraw.Draw(sh)
    for k, m in enumerate(picked):
        x, y = (k % cols) * tw, (k // cols) * th
        im = Image.open(DEST / m["file"])
        if im.mode in ("P", "RGBA", "LA"):
            im = im.convert("RGBA")
            bg = Image.new("RGB", im.size, (255, 255, 255))
            bg.paste(im, mask=im.split()[-1])
            im = bg
        im = im.convert("RGB")
        w, h = im.size
        sc = min((tw - 8) / w, (th - 30) / h, 3.0)
        sh.paste(im.resize((max(1, int(w * sc)), max(1, int(h * sc))), Image.LANCZOS),
                 (x + 4, y + 26))
        d.rectangle([x, y, x + tw - 1, y + th - 1], outline=(165, 165, 165))
        d.text((x + 4, y + 4), "%d %s [%dx%d]" % (k + 1, m["name"][:40], w, h), fill=(0, 0, 0))
        d.text((x + 4, y + 15), m["page"].split("//")[1][:52], fill=(90, 90, 90))
        print("%-3d %-44s %s" % (k + 1, m["name"][:44], m["page"]))
    sh.save("%s.png" % stem)
    print("wrote %s.png (%d tiles)" % (stem, len(picked)))


def page():
    sub = sys.argv[2]
    for m in load_man():
        if sub in m["page"]:
            print("%-58s %-46s %s" % (m["name"][:56], m["page"].split("//")[1][:70],
                                      (m.get("caption") or m.get("alt") or "")[:60]))


def psheet():
    """Contact sheet over the figures of the pages whose URL contains a substring."""
    from PIL import Image, ImageDraw
    stem, sub, cols, tw, th = sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5]), int(sys.argv[6])
    start = int(sys.argv[7]) if len(sys.argv) > 7 else 0
    count = int(sys.argv[8]) if len(sys.argv) > 8 else 60
    man = [m for m in load_man() if sub in m["page"]]
    chunk = man[start:start + count]
    rows = (len(chunk) + cols - 1) // cols
    sh = Image.new("RGB", (cols * tw, max(1, rows) * th), (248, 248, 248))
    d = ImageDraw.Draw(sh)
    for k, m in enumerate(chunk):
        x, y = (k % cols) * tw, (k // cols) * th
        try:
            im = Image.open(DEST / m["file"])
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
        d.text((x + 4, y + 4), "%d %s [%dx%d]" % (start + k + 1, m["name"][:40], w, h), fill=(0, 0, 0))
        d.text((x + 4, y + 15), m["page"].split("//")[1][:52], fill=(90, 90, 90))
        print("%-4d %-44s %s" % (start + k + 1, m["name"][:42], m["page"].split("//")[1][:66]))
    sh.save("%s.png" % stem)
    print("wrote %s.png (%d tiles of %d matching)" % (stem, len(chunk), len(man)))


if __name__ == "__main__":
    mode = sys.argv[1]
    {"download": download, "sheet": sheet, "zoom": zoom, "page": page, "psheet": psheet}[mode]()
