"""trisotech: fetch the SlideShare slide images behind the 108 presentation pages.

Stage 1  python ledgers/_ts_decks.py keys    -- fetch each embed_code page, save HTML, write decks.json
Stage 2  python ledgers/_ts_decks.py slides  -- download every slide image of every deck
Stage 3  python ledgers/_ts_decks.py sheet <slug> [...]  -- contact sheets for named decks

Resumable: an embed already saved is not re-fetched; a slide already on disk is not re-downloaded.
~1 request / second.
"""
import json, os, re, sys, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ROOT, "trisotech.raw")
DECK_HTML = os.path.join(RAW, "decks")
SLIDES = os.path.join(RAW, "slides")
DECK_JSON = os.path.join(RAW, "decks.json")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0 Safari/537.36")


def get(url, tries=3):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            return urllib.request.urlopen(req, timeout=45).read()
        except Exception as e:
            if i == tries - 1:
                raise
            time.sleep(3 + 3 * i)


def slug_of(url):
    s = urllib.parse.urlparse(url).path.strip("/").split("/")[-1]
    return s or "index"


def keys():
    """Read the SlideShare keys out of the page digests and fetch each embed page."""
    os.makedirs(DECK_HTML, exist_ok=True)
    digs = [json.loads(l) for l in open(os.path.join(RAW, "digests.jsonl"), encoding="utf-8")]
    decks = {}
    if os.path.exists(DECK_JSON):
        decks = json.load(open(DECK_JSON, encoding="utf-8"))
    todo = []
    for r in digs:
        for f in (r.get("iframes") or []):
            m = re.search(r"embed_code/key/([A-Za-z0-9]+)", f)
            if m:
                todo.append((m.group(1), r))
    print("deck pages in digests: %d" % len(todo))
    for i, (key, r) in enumerate(todo):
        slug = slug_of(r["url"])
        path = os.path.join(DECK_HTML, key + ".html")
        if not os.path.exists(path):
            url = "https://www.slideshare.net/slideshow/embed_code/key/" + key
            try:
                html = get(url).decode("utf-8", "replace")
            except Exception as e:
                print("  FAIL %s %s %s" % (key, slug, e))
                continue
            open(path, "w", encoding="utf-8").write(html)
            time.sleep(1.0)
        html = open(path, encoding="utf-8").read()
        imgs = sorted(set(re.findall(r"https://image\.slidesharecdn\.com/[^\"'\s\\]+", html)))
        # keep the largest variant of each slide, in slide order
        byname = {}
        for u in imgs:
            name = u.rsplit("/", 1)[-1]
            stem = re.sub(r"-\d+\.jpg$", "", name)
            byname.setdefault(stem, []).append(u)
        slides = []
        for stem, urls in byname.items():
            pick = max(urls, key=lambda u: int(re.search(r"-(\d+)\.jpg$", u).group(1))
                       if re.search(r"-(\d+)\.jpg$", u) else 0)
            slides.append(pick)
        def order(u):
            m = re.search(r"-(\d+)-\d+\.jpg$", u.rsplit("/", 1)[-1])
            return int(m.group(1)) if m else 0
        slides.sort(key=order)
        title = ""
        m = re.search(r'<title>(.*?)</title>', html, re.S)
        if m:
            title = re.sub(r"\s+", " ", m.group(1)).strip()
        decks[slug] = {"key": key, "url": r["url"], "page_title": r["title"],
                       "deck_title": title, "n_slides": len(slides), "slides": slides}
        print("  [%d/%d] %-58s slides=%d" % (i + 1, len(todo), slug[:58], len(slides)))
    json.dump(decks, open(DECK_JSON, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    n = [d["n_slides"] for d in decks.values()]
    print("decks: %d   slides: %d (min %d, max %d)" % (len(decks), sum(n), min(n), max(n)))


def slides():
    decks = json.load(open(DECK_JSON, encoding="utf-8"))
    os.makedirs(SLIDES, exist_ok=True)
    total = done = fail = 0
    for slug, d in decks.items():
        out = os.path.join(SLIDES, slug[:90])
        os.makedirs(out, exist_ok=True)
        for i, u in enumerate(d["slides"], 1):
            total += 1
            p = os.path.join(out, "%02d.jpg" % i)
            if os.path.exists(p):
                done += 1
                continue
            try:
                data = get(u)
                open(p, "wb").write(data)
                done += 1
            except Exception as e:
                fail += 1
                print("  FAIL %s %02d %s" % (slug[:50], i, e))
            time.sleep(0.5)
        print("  %-58s %d" % (slug[:58], len(os.listdir(out))))
    print("slides downloaded: %d/%d  (fail %d)" % (done, total, fail))


def sheet(*slugs):
    from PIL import Image, ImageDraw
    decks = json.load(open(DECK_JSON, encoding="utf-8"))
    os.makedirs(os.path.join(RAW, "sheets"), exist_ok=True)
    for slug in slugs:
        d = decks.get(slug)
        if not d:
            print("no deck %s" % slug)
            continue
        files = sorted(f for f in os.listdir(os.path.join(SLIDES, slug[:90])) if f.endswith(".jpg"))
        cols, cw = 5, 310          # 1550 px wide: the vision pipeline caps at ~1568
        ch = int(cw * 9 / 16)
        rows = (len(files) + cols - 1) // cols
        im = Image.new("RGB", (cols * cw, rows * (ch + 18)), "white")
        dr = ImageDraw.Draw(im)
        for i, f in enumerate(files):
            s = Image.open(os.path.join(SLIDES, slug[:90], f)).convert("RGB")
            s.thumbnail((cw - 4, ch - 4))
            x, y = (i % cols) * cw + 2, (i // cols) * (ch + 18) + 2
            im.paste(s, (x, y))
            dr.text((x + 2, y + ch - 2), f, fill="black")
        p = os.path.join(RAW, "sheets", slug[:90] + ".png")
        im.save(p)
        print("%s  %d slides  %s" % (p, len(files), im.size))




def mini(*slugs, per=16, width=300):
    """Small 16-per-sheet overview of a deck: enough to spot diagram slides cheaply."""
    from PIL import Image, ImageDraw
    out = os.path.join(RAW, "mini")
    os.makedirs(out, exist_ok=True)
    decks = json.load(open(DECK_JSON, encoding="utf-8"))
    if not slugs:
        slugs = list(decks)
    todo = [s for s in slugs if os.path.isdir(os.path.join(SLIDES, s[:90]))]
    made = []
    for slug in todo:
        d = os.path.join(SLIDES, slug[:90])
        files = sorted(f for f in os.listdir(d) if f.endswith(".jpg"))
        cols, cw, ch = 4, width, int(width * 9 / 16)
        for i in range(0, len(files), per):
            chunk = files[i:i + per]
            rows = (len(chunk) + cols - 1) // cols
            im = Image.new("RGB", (cols * cw, rows * (ch + 14)), "white")
            dr = ImageDraw.Draw(im)
            for k, f in enumerate(chunk):
                im2 = Image.open(os.path.join(d, f)).convert("RGB")
                im2 = im2.resize((cw - 2, ch - 2))
                x, y = (k % cols) * cw + 1, (k // cols) * (ch + 14) + 12
                im.paste(im2, (x, y))
                dr.text((x + 1, y - 11), f.replace(".jpg", ""), fill="black")
            name = "%s__%02d.png" % (slug[:70], i // per + 1)
            im.save(os.path.join(out, name))
            made.append(os.path.join(out, name))
    print(len(made), "mini sheets")
    for m in made:
        print(m)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "keys":
        keys()
    elif cmd == "slides":
        slides()
    elif cmd == "mini":
        mini(*sys.argv[2:])
    elif cmd == "sheet":
        sheet(*sys.argv[2:])
    else:
        print(__doc__)
