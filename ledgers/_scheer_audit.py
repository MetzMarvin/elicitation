#!/usr/bin/env python3
"""Calibrate the screen: the audit sample.

The mechanical screen excludes pages whose figure names and prose never name a process model. That
claim is a measurement, not an assumption: this script takes a deterministic sample of such pages
(every k-th page with figures, k chosen to give ~SAMPLE pages), downloads *all* their figures and
tiles them, so the eye can check whether a process diagram hides behind UI-ish attachment names.
The result (n figures looked at, n diagrams found) goes into the ledger header.

  python ledgers/_scheer_audit.py sample [SAMPLE]   # pick the pages + download their figures
  python ledgers/_scheer_audit.py sheet OUT COLS TW TH
"""
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
DEST = OUT / "audit"
MAN = OUT / "audit_manifest.json"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126 Safari/537.36"}


def sample(n_want=40):
    rows = []
    for f in sorted(PAGES.glob("*.html")):
        t = f.read_text(encoding="utf-8", errors="replace")
        b = S.body(t)
        fs = S.figs(t)
        if not fs:
            continue
        if re.search(S.PROC, b, re.I):
            continue  # prose-flagged pages are judged already
        if any(re.search(S.DIAGRAM_NAME, x["src"].split("/")[-1].split("?")[0], re.I) for x in fs):
            continue  # diagram-named pages are judged already
        page_url = "https://doc.scheer-pas.com/" + f.stem.replace("__", "/", 1).replace("__", "/")
        rows.append((f.stem, page_url,
                     [urllib.parse.urljoin(page_url, x["src"]) for x in fs]))
    if not rows:
        return []
    k = max(1, len(rows) // n_want)
    picked = rows[::k][:n_want]
    print("unflagged figure-pages: %d, step %d -> sampled %d (%d figures)"
          % (len(rows), k, len(picked), sum(len(p[2]) for p in picked)))
    return picked


def download(n_want=40):
    DEST.mkdir(parents=True, exist_ok=True)
    picked = sample(n_want)
    done = {m["url"].split("?")[0]: m for m in
            (json.loads(MAN.read_text(encoding="utf-8")) if MAN.exists() else [])
            if (DEST / m["file"]).exists()}
    man = list(done.values())
    for page, page_url, urls in picked:
        for url in urls:
            if url.split("?")[0] in done:
                continue
            name = url.split("/")[-1].split("?")[0]
            try:
                req = urllib.request.Request(url, headers=UA)
                with urllib.request.urlopen(req, timeout=60) as fh:
                    data = fh.read()
            except Exception as e:
                print("  ERR", name, repr(e)[:60], flush=True)
                continue
            p = DEST / ("%s__%s" % (page, name))
            if not p.exists():
                p.write_bytes(data)
            man.append({"page": page, "name": name, "url": url, "file": p.name, "bytes": len(data)})
            time.sleep(0.25)
        MAN.write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
        print("  page %s (%d figures so far)" % (page, len(man)), flush=True)
    print("audit sample: %d figures -> %s" % (len(man), DEST))


def sheet():
    from PIL import Image, ImageDraw
    stem, cols, tw, th = sys.argv[2], int(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5])
    man = [m for m in json.loads(MAN.read_text(encoding="utf-8")) if (DEST / m["file"]).exists()]
    rows = (len(man) + cols - 1) // cols
    sh = Image.new("RGB", (cols * tw, rows * th), (248, 248, 248))
    d = ImageDraw.Draw(sh)
    for k, m in enumerate(man):
        x, y = (k % cols) * tw, (k // cols) * th
        try:
            im = Image.open(DEST / m["file"]).convert("RGB")
        except Exception as e:
            d.text((x + 5, y + 5), "ERR", fill=(200, 0, 0))
            continue
        w, h = im.size
        sc = min((tw - 8) / w, (th - 22) / h, 2.0)
        sh.paste(im.resize((max(1, int(w * sc)), max(1, int(h * sc))), Image.LANCZOS), (x + 4, y + 18))
        d.rectangle([x, y, x + tw - 1, y + th - 1], outline=(165, 165, 165))
        d.text((x + 4, y + 5), "%d %s/%s" % (k + 1, m["page"].split("__")[-1][:16], m["name"][:30]),
               fill=(0, 0, 0))
    sh.save("%s.png" % stem)
    print("wrote %s.png (%d tiles)" % (stem, len(man)))


if __name__ == "__main__":
    if sys.argv[1] == "sample":
        download(int(sys.argv[2]) if len(sys.argv) > 2 else 40)
    elif sys.argv[1] == "list":
        for p, u, urls in sample(int(sys.argv[2]) if len(sys.argv) > 2 else 40):
            print(p, len(urls))
    elif sys.argv[1] == "sheet":
        sheet()
