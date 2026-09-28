#!/usr/bin/env python3
"""Download the *suspect* figures - the ones whose own attachment name names a process model.

These are the figures that decide a page's ruling, so they are the ones looked at. The set is
bounded by the screen (ledgers/_scheer_build.py), duplicated attachments are deduplicated by
content hash, and the contact sheets are labelled with the figure's own name and pixel size, so a
ruling can cite exactly what was looked at.

  python ledgers/_scheer_figs2.py download        # suspect figures of every cached page
  python ledgers/_scheer_figs2.py sheet OUT COLS TILE_W TILE_H
"""
import hashlib
import json
import pathlib
import re
import sys
import time
import urllib.parse
import urllib.request

ELI = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ELI / "ledgers"))
import _scheer_rows as S  # noqa: E402

OUT = ELI / "ledgers" / "_scheer"
PAGES = OUT / "pages"
DEST = OUT / "suspect"
MAN = OUT / "suspect_manifest.json"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126 Safari/537.36"}


def candidates():
    """[(page-stem, figure-name, absolute URL)] for every suspect figure of every cached page."""
    out, seen = [], set()
    for f in sorted(PAGES.glob("*.html")):
        t = f.read_text(encoding="utf-8", errors="replace")
        page_url = "https://doc.scheer-pas.com/" + f.stem.replace("__", "/", 1).replace("__", "/")
        for x in S.figs(t):
            name = x["src"].split("/")[-1].split("?")[0]
            if not re.search(S.DIAGRAM_NAME, name, re.I):
                continue
            url = urllib.parse.urljoin(page_url, x["src"])
            key = url.split("?")[0]
            if key in seen:
                continue
            seen.add(key)
            out.append((f.stem, name, url))
    return out


def download():
    DEST.mkdir(parents=True, exist_ok=True)
    rows = candidates()
    done = {}
    if MAN.exists():
        done = {m["url"].split("?")[0]: m for m in json.loads(MAN.read_text(encoding="utf-8"))
                if (DEST / m["file"]).exists()}
    print("suspect figures on cached pages:", len(rows), "already cached:", len(done))
    man = list(done.values())
    todo = [(p, n, u) for p, n, u in rows if u.split("?")[0] not in done]
    for k, (page, name, url) in enumerate(todo, 1):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as fh:
                data = fh.read()
        except Exception as e:
            print("  ERR", name, repr(e)[:70])
            time.sleep(1)
            continue
        sha = hashlib.sha1(data).hexdigest()[:12]
        dest = DEST / ("%s__%s" % (sha, name))
        if not dest.exists():
            dest.write_bytes(data)
        man.append({"page": page, "name": name, "url": url, "sha": sha, "file": dest.name,
                    "bytes": len(data)})
        if k % 25 == 0:
            print("  %d/%d" % (k, len(rows)), flush=True)
        time.sleep(1.0)
    MAN.write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
    uniq = len(set(m["sha"] for m in man))
    print("downloaded/cached %d, unique by content %d -> %s" % (len(man), uniq, DEST))


def sheet():
    from PIL import Image, ImageDraw
    from _scheer_figclass import FIGCLASS
    stem, cols, tw, th = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    start = int(sys.argv[6]) if len(sys.argv) > 6 else 0
    count = int(sys.argv[7]) if len(sys.argv) > 7 else 60
    man = json.loads(MAN.read_text(encoding="utf-8"))
    seen, uniq = set(), []
    for m in sorted(man, key=lambda m: m["name"]):
        if m["sha"] in seen or m["name"] in FIGCLASS:
            continue          # already classified: the sweep only shows what is still open
        seen.add(m["sha"])
        if (DEST / m["file"]).exists():
            uniq.append(m)
    chunk = uniq[start:start + count]
    rows = (len(chunk) + cols - 1) // cols
    sh = Image.new("RGB", (cols * tw, rows * th), (248, 248, 248))
    d = ImageDraw.Draw(sh)
    for k, m in enumerate(chunk):
        x, y = (k % cols) * tw, (k // cols) * th
        try:
            im = Image.open(DEST / m["file"]).convert("RGB")
        except Exception as e:
            d.text((x + 5, y + 5), "ERR %s" % e, fill=(200, 0, 0))
            continue
        w, h = im.size
        sc = min((tw - 8) / w, (th - 24) / h, 2.0)
        sh.paste(im.resize((max(1, int(w * sc)), max(1, int(h * sc))), Image.LANCZOS), (x + 4, y + 20))
        d.rectangle([x, y, x + tw - 1, y + th - 1], outline=(165, 165, 165))
        d.text((x + 4, y + 6), "%d %s [%dx%d]" % (k + 1, m["name"][:44], w, h), fill=(0, 0, 0))
        print("%-4d %-50s %s" % (k + 1, m["name"], m["page"]))
    sh.save("%s.png" % stem)
    print("wrote %s.png (unclassified tiles 1-%d, %d still open in total)"
          % (stem, len(chunk), len(uniq)))


if __name__ == "__main__":
    if sys.argv[1] == "download":
        download()
    elif sys.argv[1] == "sheet":
        sheet()
