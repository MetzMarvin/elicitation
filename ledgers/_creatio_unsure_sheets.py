#!/usr/bin/env python3
"""Contact sheets for the rows the caption classifier could not settle.

The notation classifier decided every page whose figure caption or surrounding paragraph names
either process-model notation or a UI surface. 38 rows stayed `unsure` (caption absent or
generic). Those are exactly the rows CLAUDE.md rule 5 sends to the researcher as UNCERTAIN +
needs_visual_check, so before writing them up the figures are pulled out and tiled with an
index label, and the figures are looked at once.

  python ledgers/_creatio_unsure_sheets.py            # build sheets + legend
"""
import json, pathlib, re, sys, urllib.request
from PIL import Image, ImageDraw

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ELI = pathlib.Path(__file__).resolve().parents[1]
OUT = ELI / "ledgers" / "_creatio"
FIGS = OUT / "figs"
UNS = OUT / "unsure"
UNS.mkdir(exist_ok=True)

CHROME = re.compile(r"(/img/logo|/img/creatio|favicon|/icons?/|[-_/]icon|icon[-_.]|logo|bullet|"
                    r"/nav|_nav|note\.|caution|warning|arrow|expand|collapse|checkmark|sprite|"
                    r"spacer|blank|1x1)", re.I)


def slug_of(url):
    return re.sub(r"[^A-Za-z0-9._-]", "_", url.replace("https://academy.creatio.com", "").strip("/"))[:150]


rows = []
for line in (ELI / "ledgers" / "creatio.jsonl").read_text(encoding="utf-8").splitlines():
    o = json.loads(line)
    if o.get("type") in ("header", "footer") or o.get("verdict") != "UNCERTAIN" or o.get("record"):
        continue
    rows.append(o)
print("unsure rows:", len(rows))

idx = json.loads((OUT / "figs_index.json").read_text(encoding="utf-8"))
have = {}
for f in idx:
    have.setdefault(f["slug"], []).append(f)
arts = json.loads((OUT / "articles.json").read_text(encoding="utf-8"))

legend, tiles = [], []
for i, r in enumerate(rows, 1):
    s = slug_of(r["url"]) + ".html"
    cands = [f for f in have.get(s, []) if (FIGS / f["file"]).exists()]
    # add article figures not yet downloaded
    a = arts.get(s)
    if a:
        got = {f["src"] for f in cands}
        for im in (a.get("imgs") or []):
            src = im.get("src") or ""
            if not src or src in got or CHROME.search(src):
                continue
            fn = f"{s}__u{len(cands)+1}.png"
            dest = FIGS / fn
            if not dest.exists():
                try:
                    req = urllib.request.Request(src if src.startswith("http") else "https://academy.creatio.com" + src,
                                                 headers={"User-Agent": "Mozilla/5.0 (thesis census; read-only)"})
                    dest.write_bytes(urllib.request.urlopen(req, timeout=30).read())
                except Exception as exc:
                    print("   dl fail", fn[-40:], type(exc).__name__)
                    continue
            cands.append({"file": fn, "slug": s, "src": src, "alt": im.get("alt", ""),
                          "text_before": im.get("text_before", ""), "text_after": im.get("text_after", "")})
            got.add(src)
    if not cands:
        print("   NO FIGURE", s)
        legend.append((i, r["n"], s, None, r["url"]))
        continue
    # biggest available figure is the most informative one
    def area(f):
        try:
            with Image.open(FIGS / f["file"]) as im:
                return im.width * im.height
        except Exception:
            return 0
    cands.sort(key=area, reverse=True)
    legend.append((i, r["n"], s, cands[0], r["url"]))
    tiles.append((i, FIGS / cands[0]["file"]))

COLS, ROWS_N, CELL = 4, 3, (620, 470)
per = COLS * ROWS_N
for sh in range((len(tiles) + per - 1) // per):
    chunk = tiles[sh * per:(sh + 1) * per]
    sheet = Image.new("RGB", (COLS * CELL[0], ROWS_N * CELL[1]), "white")
    d = ImageDraw.Draw(sheet)
    for k, (i, path) in enumerate(chunk):
        cx, cy = (k % COLS) * CELL[0], (k // COLS) * CELL[1]
        try:
            with Image.open(path) as im:
                im = im.convert("RGB")
                im.thumbnail((CELL[0] - 12, CELL[1] - 30))
                sheet.paste(im, (cx + 6, cy + 26))
        except Exception as exc:
            d.text((cx + 8, cy + 40), f"P{i}: open failed {exc}", fill="red")
        d.rectangle([cx + 2, cy + 2, cx + CELL[0] - 2, cy + CELL[1] - 2], outline="#999")
        d.text((cx + 8, cy + 8), f"P{i}", fill="black")
    p = OUT / f"unsure_sheet_{sh+1}.png"
    sheet.save(p)
    print("sheet", p.name, "tiles", len(chunk))

(OUT / "_unsure_legend.json").write_text(json.dumps(
    [{"p": i, "n": n, "slug": s, "file": (f or {}).get("file"), "alt": (f or {}).get("alt"),
      "text_before": (f or {}).get("text_before"), "text_after": (f or {}).get("text_after"),
      "url": u} for i, n, s, f, u in legend], ensure_ascii=False, indent=1), encoding="utf-8")
for i, n, s, f, u in legend:
    print(f"P{i:>2} n={n:<4} fig={(f or {}).get('file','-')[-46:]:<48} alt={((f or {}).get('alt') or '')[:70]!r}")
