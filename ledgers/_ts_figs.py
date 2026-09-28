"""trisotech: download the figures published by the content pages and tile them for eye review.

  python ledgers/_ts_figs.py dl      -- download every figure into trisotech.raw/figures/
  python ledgers/_ts_figs.py sheets  -- 4-per-sheet contact sheets at >=900 px
  python ledgers/_ts_figs.py inv     -- print the inventory (page -> figures, with AI/BPMN prose flags)
"""
import json, os, re, sys, time, urllib.parse, urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ROOT, "trisotech.raw")
FIGS = os.path.join(RAW, "figures")
SHEETS = os.path.join(RAW, "fig_sheets")
OWN_SHEETS = os.path.join(RAW, "own_sheets")
FURN = re.compile(r"(shadow|banner-|thumb|-Header\.|Photo|picture|avatar|Tile-|quote-|creative-commons|icon|logo|graph-footer|-des\.|standard-thumb|OMG-logo|-scaled|fancybox|BruceSilver|Sandy-Kemsley|john-svirbely|stefaan-lambrecht|Trisotech-|spacer|divider|background|fancybox)", re.I)
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0 Safari/537.36")

AI = re.compile(r"\b(ai|a\.i\.|llm|llms|gpt|genai|generative|agent|agents|agentic|machine learning|"
                r"neural|intelligent|intelligence|chatbot|copilot|automation|automated|"
                r"natural language|decision model|dmn|predictive|inference)\b", re.I)
BPMN = re.compile(r"\b(bpmn|bpmn 2\.0|process diagram|process model|pool|lane|gateway|service task|"
                  r"user task|sub-?process|event|choreograph|cmmn)\b", re.I)


def pages():
    d = [json.loads(l) for l in open(os.path.join(RAW, "digests.jsonl"), encoding="utf-8")]
    return [r for r in d if r.get("family") == "content"]


def local(u):
    """Filesystem name for a figure URL, stable and collision-free."""
    p = urllib.parse.urlparse(u)
    name = urllib.parse.unquote(p.path.strip("/").split("/")[-1])
    name = re.sub(r"[^A-Za-z0-9._-]", "_", name) or "img"
    tag = re.sub(r"[^A-Za-z0-9]", "", p.path)[-40:]
    return (tag + "__" + name)[:140]


def dl():
    os.makedirs(FIGS, exist_ok=True)
    got = fail = 0
    urls = []
    seen = set()
    for r in pages():
        for f in (r.get("figures") or []):
            u = f.get("url") if isinstance(f, dict) else f
            if u and u not in seen:
                seen.add(u)
                urls.append(u)
    print("distinct figure urls: %d" % len(urls))
    for i, u in enumerate(urls, 1):
        p = os.path.join(FIGS, local(u))
        if os.path.exists(p) and os.path.getsize(p) > 500:
            got += 1
            continue
        try:
            data = urllib.request.urlopen(
                urllib.request.Request(u, headers={"User-Agent": UA}), timeout=45).read()
            open(p, "wb").write(data)
            got += 1
        except Exception as e:
            fail += 1
            print("  FAIL %s %s" % (u, e))
        time.sleep(1.0)
        if i % 25 == 0:
            print("  %d/%d" % (i, len(urls)))
    print("figures on disk: %d (fail %d)" % (got, fail))


def sheets(per=4, width=1000):
    from PIL import Image, ImageDraw
    os.makedirs(SHEETS, exist_ok=True)
    urls = []
    for r in pages():
        for f in (r.get("figures") or []):
            u = f.get("url") if isinstance(f, dict) else f
            if u and u not in urls:
                urls.append(u)
    have = [(u, os.path.join(FIGS, local(u))) for u in urls]
    have = [(u, p) for u, p in have if os.path.exists(p)]
    n = 0
    for i in range(0, len(have), per):
        chunk = have[i:i + per]
        ims = []
        for u, p in chunk:
            try:
                im = Image.open(p).convert("RGB")
            except Exception:
                continue
            if im.width < 8 or im.height < 8:
                continue
            sc = min(width / im.width, 1200 / im.height, 3.0)
            ims.append((os.path.basename(p)[:70], im.resize((int(im.width * sc), int(im.height * sc)))))
        if not ims:
            continue
        H = sum(im.height + 20 for _, im in ims)
        W = max(im.width for _, im in ims)
        sheet = Image.new("RGB", (W, H), "white")
        dr = ImageDraw.Draw(sheet)
        y = 0
        for name, im in ims:
            sheet.paste(im, (0, y + 18))
            dr.text((2, y + 3), name, fill="black")
            y += im.height + 20
        n += 1
        sheet.save(os.path.join(SHEETS, "s%02d.png" % n))
    print("sheets: %d from %d figures" % (n, len(have)))
    return n


def inv():
    for i, r in enumerate(pages(), 1):
        figs = r.get("figures") or []
        if not figs:
            continue
        t = r.get("text") or ""
        ai = bool(AI.search(t))
        bp = bool(BPMN.search(t))
        print("%3d %-78s figs=%d ai=%s bpmn=%s" % (i, r["url"].replace("https://www.trisotech.com/", ""),
                                                   len(figs), ai, bp))
        for f in figs:
            u = f.get("url") if isinstance(f, dict) else f
            alt = (f.get("alt") or "") if isinstance(f, dict) else ""
            print("      %s   |alt: %s" % (local(u), alt[:100]))


def own_urls():
    """Every non-chrome image the pages publish in their own content region, in page order."""
    c = json.load(open(os.path.join(RAW, "content.json"), encoding="utf-8"))
    seq, seen = [], set()
    for s, v in c.items():
        if v.get("family") != "content":
            continue
        for i in v.get("imgs_clean") or []:
            u = i["url"]
            if u.startswith("//"):
                u = "https:" + u
            if not u.startswith("http"):
                u = "https://www.trisotech.com" + ("" if u.startswith("/") else "/") + u
            if u in seen:
                continue
            seen.add(u)
            seq.append({"page": s, "url": u, "alt": i.get("alt") or "",
                        "w": i.get("w") or 0, "h": i.get("h") or 0})
    return seq


def own_dl():
    os.makedirs(FIGS, exist_ok=True)
    seq = own_urls()
    print("own images: %d" % len(seq))
    got = fail = 0
    for i, r in enumerate(seq, 1):
        p = os.path.join(FIGS, local(r["url"]))
        if os.path.exists(p) and os.path.getsize(p) > 300:
            got += 1
            continue
        try:
            data = urllib.request.urlopen(
                urllib.request.Request(r["url"], headers={"User-Agent": UA}), timeout=45).read()
            open(p, "wb").write(data)
            got += 1
        except Exception as e:
            fail += 1
            print("  FAIL %s %s" % (r["url"], e))
        time.sleep(0.9)
        if i % 100 == 0:
            print("  %d/%d" % (i, len(seq)))
    print("own images on disk: %d (fail %d)" % (got, fail))


def own_sheets(width=250, maxh=170, cols=6):
    """Page-grouped contact sheets of the pages' non-furniture images.

    The Trisotech blog template puts a hero image, an author portrait and a "related content"
    carousel on every post; those are furniture, not artefacts. FURN names them so the sheets
    show what the page itself is *about*. Every image that survives the filter is looked at, and
    the ones it drops are spot-checked in one page-wide pass (see trisotech.raw/furniture-check).
    """
    from PIL import Image, ImageDraw
    os.makedirs(OWN_SHEETS, exist_ok=True)
    seq = own_urls()
    keep = [r for r in seq if not FURN.search(r["url"])]
    dropped = [r for r in seq if FURN.search(r["url"])]
    rows = []
    for r in keep:
        p = os.path.join(FIGS, local(r["url"]))
        if not os.path.exists(p) or os.path.getsize(p) < 300:
            continue
        try:
            im = Image.open(p)
            w, h = im.size
        except Exception:
            continue
        rows.append((r, p, w, h))
    print("own images: %d total, %d furniture, %d on disk to look at"
          % (len(seq), len(dropped), len(rows)))
    index, n = [], 0
    for page in dict.fromkeys(r["page"] for r, _, _, _ in rows):
        grp = [x for x in rows if x[0]["page"] == page]
        for start in range(0, len(grp), 12):
            chunk = grp[start:start + 12]
            grows = (len(chunk) + cols - 1) // cols
            sheet = Image.new("RGB", (cols * width, grows * (maxh + 30)), "white")
            dr = ImageDraw.Draw(sheet)
            for k, (r, p, w, h) in enumerate(chunk):
                try:
                    im = Image.open(p).convert("RGB")
                except Exception:
                    continue
                sc = min((width - 6) / max(im.width, 1), (maxh - 6) / max(im.height, 1), 2.0)
                im = im.resize((max(1, int(im.width * sc)), max(1, int(im.height * sc))))
                x = (k % cols) * width + 3
                y = (k // cols) * (maxh + 30) + 24
                sheet.paste(im, (x, y))
                n += 1
                index.append({"n": n, "page": page, "url": r["url"], "alt": r["alt"],
                              "w": w, "h": h})
                dr.text((x, y - 22), "%d  %s" % (n, r["url"].rsplit("/", 1)[-1][:30]), fill="black")
                dr.text((x, y - 11), "%dx%d  %s" % (w, h, r["alt"][:22]), fill="black")
            name = "%02d_%s.png" % (len(index) and start // 12 + 1 or 1, page[:46])
            sheet.save(os.path.join(OWN_SHEETS, name))
            print("  %-70s %d tiles" % (name, len(chunk)))
    json.dump(index, open(os.path.join(RAW, "own_index.json"), "w", encoding="utf-8"),
              indent=1, ensure_ascii=False)
    json.dump([{"page": r["page"], "url": r["url"]} for r in dropped],
              open(os.path.join(RAW, "furniture.json"), "w", encoding="utf-8"),
              indent=1, ensure_ascii=False)
    print("sheets: looked-at images indexed: %d" % len(index))


def ai_sheets(width=250, maxh=170, cols=6, only=None):
    """Contact sheets for the pages that carry an AI/LLM signal (text, figure filename).

    Those are the pages where the *artefact* half of the test can plausibly pass; every other
    content page is a mechanical E2/E0 (see the ledger header). One sheet per page for the
    page's non-furniture images, plus one "furniture" sheet per page for the images the
    furniture filter drops, so the filter cannot hide a diagram.
    """
    from PIL import Image, ImageDraw
    from _ts_rows import AI
    OUT = os.path.join(RAW, "ai_sheets")
    FUR = os.path.join(RAW, "ai_furn")
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(FUR, exist_ok=True)
    sc = json.load(open(os.path.join(RAW, "screen.json"), encoding="utf-8"))
    sig = []
    for r in sc:
        if r["family"] != "content":
            continue
        # bucket-agnostic on purpose: a video or deck page still publishes its own images, and a
        # diagram can sit there under a webinar abstract or a slide cover.
        if not AI.search(" ".join([r["text"]] + list(r["own_imgs"]))):
            continue
        if only and r["slug"] not in only:
            continue
        sig.append(r)
    idx, n_skipped = [], 0
    for r in sig:
        page = r["slug"]
        ims = [x for x in own_urls() if x["page"] == page]
        keep = [x for x in ims if not FURN.search(x["url"])]
        drop = [x for x in ims if FURN.search(x["url"])]
        for kind, group, dest in (("own", keep, OUT), ("furn", drop, FUR)):
            tiles = []
            for x in group:
                p = os.path.join(FIGS, local(x["url"]))
                if not os.path.exists(p) or os.path.getsize(p) < 300:
                    n_skipped += 1
                    continue
                try:
                    im = Image.open(p).convert("RGB")
                except Exception:
                    n_skipped += 1
                    continue
                tiles.append((x, im))
            if not tiles:
                continue
            grows = (len(tiles) + cols - 1) // cols
            sheet = Image.new("RGB", (cols * width, grows * (maxh + 30)), "white")
            dr = ImageDraw.Draw(sheet)
            for k, (x, im) in enumerate(tiles):
                sc2 = min((width - 6) / max(im.width, 1), (maxh - 6) / max(im.height, 1), 2.0)
                im2 = im.resize((max(1, int(im.width * sc2)), max(1, int(im.height * sc2))))
                px = (k % cols) * width + 3
                py = (k // cols) * (maxh + 30) + 24
                sheet.paste(im2, (px, py))
                dr.text((px, py - 22), "%s/%d  %s" % (kind, k + 1,
                                                      x["url"].rsplit("/", 1)[-1][:30]), fill="black")
                dr.text((px, py - 11), "%dx%d %s" % (im.width, im.height, x["alt"][:22]),
                        fill="black")
                idx.append({"kind": kind, "page": page, "i": k + 1, "url": x["url"],
                            "alt": x["alt"]})
            name = "%s__%s.png" % (page[:52], kind)
            sheet.save(os.path.join(dest, name))
            print("  %-72s %d tiles" % (name, len(tiles)))
    json.dump(idx, open(os.path.join(RAW, "ai_index.json"), "w", encoding="utf-8"),
              indent=1, ensure_ascii=False)
    print("AI-signal figure pages: %d  tiles indexed: %d  tiles missing on disk: %d"
          % (len(sig), len(idx), n_skipped))


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "ai-sheets":
        ai_sheets(only=set(sys.argv[2:]) or None)
    elif cmd == "dl":
        dl()
    elif cmd == "sheets":
        sheets()
    elif cmd == "inv":
        inv()
    elif cmd == "own-dl":
        own_dl()
    elif cmd == "own-sheets":
        own_sheets()
    elif cmd == "own-list":
        for i, r in enumerate(own_urls(), 1):
            print("%4d %-32s %-70s %s" % (i, r["page"][:32], r["url"].rsplit("/", 1)[-1][:70],
                                          r["alt"][:30]))
    else:
        print(__doc__)
