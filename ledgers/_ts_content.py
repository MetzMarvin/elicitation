"""trisotech: extract each page's *own content region* from the saved HTML.

The pages are WordPress; everything outside `<main data-pagefind-body>` is site chrome, and
inside it the "related content" carousels are marked `<section ... data-pagefind-weight="0.0">`.
Both carry other pages' titles, thumbnails and AI words, so screening the raw HTML made every
page look AI-flavoured (a false positive that would have inflated `n_ai` to 100% of the
population). This module keeps only what the page itself publishes.

  python ledgers/_ts_content.py build   -- writes trisotech.raw/content.json (resumable)
  python ledgers/_ts_content.py show <slug> [n]
"""
import json, os, re, sys, urllib.parse

ROOT = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ROOT, "trisotech.raw")
PAGES = os.path.join(RAW, "pages")
OUT = os.path.join(RAW, "content.json")


def slug(u):
    """Key pages by their whole path: /tag/bpmn/ and /bpmn/ are different pages and the
    last path segment alone collided on 9 such pairs (30 pages lost in the first build)."""
    p = urllib.parse.urlparse(u).path.strip("/")
    return re.sub(r"[^A-Za-z0-9._-]", "__", p) or "index"


def own_region(html):
    """The page's own published region: <main data-pagefind-body> minus weight-0 sections."""
    i = html.find("<main data-pagefind-body>")
    if i < 0:
        i = html.find("<body")
    j = html.find("</body>", i)
    m = html[i:j if j > 0 else len(html)]
    out, pos, depth = [], 0, 0
    for tag in re.finditer(r"<section\b[^>]*>|</section\s*>", m):
        if depth == 0 and 'data-pagefind-weight="0.0"' in tag.group(0):
            out.append(m[pos:tag.start()])
            pos, depth = tag.start(), 1
        elif depth:
            depth += -1 if tag.group(0).startswith("</") else 1
            if depth == 0:
                pos = tag.end()
    out.append(m[pos:])
    return "".join(out)


def text_of(region):
    t = re.sub(r"<(script|style|noscript)\b.*?</\1\s*>", " ", region, flags=re.S | re.I)
    t = re.sub(r"<br\s*/?>|</(p|div|li|h[1-6]|tr|td|section)>", "\n", t, flags=re.I)
    t = re.sub(r"<[^>]+>", " ", t)
    t = re.sub(r"&nbsp;?", " ", t)
    t = re.sub(r"&amp;", "&", t)
    t = re.sub(r"&#8217;|&rsquo;", "'", t)
    t = re.sub(r"&#8211;|&ndash;", "-", t)
    t = re.sub(r"&#8220;|&ldquo;", '"', t)
    t = re.sub(r"&#8221;|&rdquo;", '"', t)
    t = re.sub(r"&[a-z#0-9]{2,8};", " ", t)
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t.strip()


def imgs(region):
    out = []
    for m in re.finditer(r"<img\b[^>]*>", region, re.I):
        tag = m.group(0)
        src = re.search(r'\bsrc="([^"]+)"', tag)
        if not src:
            continue
        alt = re.search(r'\balt="([^"]*)"', tag)
        w = re.search(r'\bwidth="(\d+)"', tag)
        h = re.search(r'\bheight="(\d+)"', tag)
        out.append({"url": src.group(1), "alt": (alt.group(1) if alt else ""),
                    "w": int(w.group(1)) if w else 0, "h": int(h.group(1)) if h else 0})
    # de-duplicate by url, keeping the first
    seen, keep = set(), []
    for i in out:
        if i["url"] not in seen:
            seen.add(i["url"])
            keep.append(i)
    return keep


def build():
    from _ts_rows import AI, BPMN  # lexicons live with the row builder
    from _ts_fetch import CHROME   # the theme-furniture filter the first screen used
    digs = [json.loads(l) for l in open(os.path.join(RAW, "digests.jsonl"), encoding="utf-8")]
    cache = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}
    got = miss = 0
    for r in digs:
        s = slug(r["url"])
        if s in cache and "--rebuild" not in sys.argv:
            got += 1
            continue
        p = os.path.join(PAGES, s + ".html")
        if not os.path.exists(p):
            miss += 1
            continue
        h = open(p, encoding="utf-8").read()
        reg = own_region(h)
        t = text_of(reg)
        own = imgs(reg)
        clean = [i for i in own if not CHROME.search(i["url"])]
        ifr = re.findall(r'<iframe\b[^>]*\bsrc="([^"]+)"', reg, re.I)
        cache[s] = {
            "url": r["url"], "title": r.get("title"), "family": r.get("family"),
            "text": t, "words": len(t.split()),
            "imgs": own, "imgs_clean": clean,
            "iframes": ifr,
            "iframes_all": re.findall(r'<iframe\b[^>]*\bsrc="([^"]+)"', h, re.I),
            "pdfs": re.findall(r'href="([^"]+\.pdf)"', reg, re.I),
            "n_svg_own": len(re.findall(r"<svg\b", reg)),
            "n_svg_page": len(re.findall(r"<svg\b", h)),
            "ai_terms": sorted(set(m.group(0) for m in AI.finditer(t))),
            "n_ai": len(AI.findall(t)),
            "bpmn_terms": sorted(set(m.group(0).lower() for m in BPMN.finditer(t)))[:12],
            "n_bpmn": len(BPMN.findall(t)),
            "og_image": r.get("og_image"),
            "digest_figs": [f.get("url") if isinstance(f, dict) else f for f in (r.get("figures") or [])],
            "digest_iframes": r.get("iframes") or [],
        }
        got += 1
    json.dump(cache, open(OUT, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    from collections import Counter
    c = Counter(v["family"] for v in cache.values())
    print("content regions: %d (missing html: %d)  %s" % (got, miss, dict(c)))
    print("pages with own clean images: %d ; own iframes: %d of page-wide %d"
          % (sum(1 for v in cache.values() if v["imgs_clean"]),
             sum(1 for v in cache.values() if v["iframes"]),
             sum(1 for v in cache.values() if v["iframes_all"])))
    n_ai = sum(1 for v in cache.values() if v["n_ai"])
    print("pages whose OWN text carries an AI term: %d" % n_ai)


def show(s, n=4000):
    c = json.load(open(OUT, encoding="utf-8"))
    v = c[s]
    print("URL   ", v["url"])
    print("TITLE ", v["title"])
    print("AI    ", v["ai_terms"], "BPMN", v["bpmn_terms"])
    print("IMGS  ", json.dumps(v["imgs"], ensure_ascii=False)[:1200])
    print("IFR   ", v["iframes"][:6], "| page-wide:", len(v["iframes_all"]))
    print("PDFS  ", v["pdfs"][:6])
    print("TEXT  ", v["text"][:n])


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "build":
        build()
    elif cmd == "show":
        show(sys.argv[2], int(sys.argv[3]) if len(sys.argv) > 3 else 4000)
    else:
        print(__doc__)
