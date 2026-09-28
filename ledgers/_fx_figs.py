"""Download the figures of named flowx-ai pages, or explicit figure URLs, and lay them on a sheet.

Two uses:

  python ledgers/_fx_figs.py slug <slug> [<slug> ...]     every figure of those pages
  python ledgers/_fx_figs.py url  <url> [<url> ...]       those exact image URLs

Files land in ledgers/flowx-ai.raw/figures/<slug>/NNN_<name>.<ext> ('url' mode uses the image's own
last path segment as its directory). `--sheet <out.png>` lays what was downloaded on a grid with
"NNN of M  <name>" captions, so a whole page's figures can be read in one look. Sheet mode reads
whatever is already in the directories, so it can be re-run without re-downloading.
"""
import os, re, sys, time, urllib.parse, urllib.request

ELI = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ELI, "flowx-ai.raw")
PAGES = os.path.join(RAW, "pages")
FALLBACK = os.path.join(RAW, "pages_llmsfull")
FIGS = os.path.join(RAW, "figures")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0 Safari/537.36")
FIGLINE = re.compile(r"^\s*!\[[^\]]*\]\((https?://.+?)\)\s*$")


def page_figures(slug):
    for d in (PAGES, FALLBACK):
        f = os.path.join(d, slug + ".md")
        if os.path.exists(f):
            body = open(f, encoding="utf-8").read()
            out, seen = [], set()
            for ln in body.splitlines():
                m = FIGLINE.match(ln)
                if m:
                    u = m.group(1).split("#")[0]
                    if u not in seen:
                        seen.add(u)
                        out.append(u)
            return out
    return None


def fetch(u, dest):
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        return "cached", os.path.getsize(dest)
    req = urllib.request.Request(u, headers={"User-Agent": UA, "Referer": "https://docs.flowx.ai/"})
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            data = r.read()
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        open(dest, "wb").write(data)
        time.sleep(0.3)
        return "ok", len(data)
    except Exception as exc:                       # noqa: BLE001 - reported, not raised
        return "FAIL %s" % exc, 0


def sheet(dirs, out):
    from PIL import Image, ImageDraw
    tiles = []
    for d in dirs:
        p = os.path.join(FIGS, d)
        if not os.path.isdir(p):
            continue
        for f in sorted(os.listdir(p)):
            if f.startswith("cap_") or not f.lower().endswith((".png", ".gif", ".jpg", ".jpeg", ".svg")):
                continue
            tiles.append((d, f, os.path.join(p, f)))
    if not tiles:
        print("nothing to lay out")
        return
    COL, W, CAP = 3, 560, 26
    imgs = []
    for d, f, path in tiles:
        try:
            im = Image.open(path).convert("RGB")
        except Exception:
            continue
        im.thumbnail((W, 100000))
        imgs.append((("figure %s of %s   %s/%s" % (f[:3], len(tiles), d, f[4:])), im))
    rows = (len(imgs) + COL - 1) // COL
    rh = [0] * rows
    for i, (cap, im) in enumerate(imgs):
        rh[i // COL] = max(rh[i // COL], im.height + CAP)
    canvas = Image.new("RGB", (COL * W, sum(rh) + 8), "white")
    dr = ImageDraw.Draw(canvas)
    y = 0
    for r in range(rows):
        x = 0
        for c in range(COL):
            i = r * COL + c
            if i >= len(imgs):
                break
            cap, im = imgs[i]
            dr.text((x + 6, y + 6), cap[:88], fill="black")
            canvas.paste(im, (x + 6, y + CAP))
            x += W
        y += rh[r]
    canvas.save(out)
    print("sheet:", out, canvas.size, "tiles:", len(imgs))


def main():
    mode = sys.argv[1]
    args = [a for a in sys.argv[2:] if not a.startswith("--")]
    sheet_out = None
    if "--sheet" in sys.argv:
        sheet_out = sys.argv[sys.argv.index("--sheet") + 1]
        args = [a for a in args if a != sheet_out]
    if mode == "slug":
        for s in args:
            urls = page_figures(s)
            if urls is None:
                print("MISSING page:", s)
                continue
            d = s.replace("/", "__")
            for i, u in enumerate(urls, 1):
                name = urllib.parse.unquote(os.path.basename(urllib.parse.urlparse(u).path)) or "img"
                st, n = fetch(u, os.path.join(FIGS, d, "%03d_%s" % (i, name)))
                print("%-4s %7d  %s/%03d_%s" % (st, n, d, i, name))
    elif mode == "url":
        for i, u in enumerate(args, 1):
            name = urllib.parse.unquote(os.path.basename(urllib.parse.urlparse(u).path)) or "img"
            d = "url"
            st, n = fetch(u, os.path.join(FIGS, d, "%03d_%s" % (i, name)))
            print("%-4s %7d  %s/%03d_%s" % (st, n, d, i, name))
    if sheet_out:
        dirs = [s.replace("/", "__") for s in args] if mode == "slug" else ["url"]
        sheet(dirs, sheet_out)


if __name__ == "__main__":
    main()
