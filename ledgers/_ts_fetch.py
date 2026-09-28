"""Fetch the trisotech census population and reduce each page to a digest, one page per second.

The population (ledgers/trisotech.raw/population.json, built by _ts_pop.py) is the site's own
sitemap, deduplicated: two families, the release-notes family and the content pages.

What this writes:

  pages/<slug>.html        the raw page, content family only (the family the census judges item by
                           item; the digest is not enough to quote from)
  digests.jsonl            one JSON line per page, both families, appended as it goes and skipped
                           on re-run, so a fetch can be resumed. The digest is what the screening
                           pass reads: title, description, the standalone images with their alt
                           text, embeds, model-file links, the rendered text, and the counts.

Nothing here decides a verdict. It exists so the census can say, for every one of the 1622 sitemap
URLs, what the page actually carries.

Usage:
  python ledgers/_ts_fetch.py content|rn|all [--limit N]
"""
import json, os, re, sys, time, urllib.parse, urllib.request, html as htmllib

ELI = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ELI, "trisotech.raw")
PAGES = os.path.join(RAW, "pages")
DIGESTS = os.path.join(RAW, "digests.jsonl")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0 Safari/537.36")
RELEASE = re.compile(r"release-notes", re.I)

IMG = re.compile(r"<img\b[^>]*>", re.I)
SRC = re.compile(r'\b(?:data-src|srcset|src)=["\']([^"\']+)["\']', re.I)
ALT = re.compile(r'\balt=["\']([^"\']*)["\']', re.I)
IFRAME = re.compile(r"<iframe\b[^>]*>", re.I)
MODEL = re.compile(r'href=["\']([^"\']+\.(?:bpmn|dmn|cmmn|xml|zip|pdf|pptx))["\']', re.I)
SCRIPT = re.compile(r"<(script|style|noscript)\b.*?</\1>", re.S | re.I)
TAG = re.compile(r"<[^>]+>")
WS = re.compile(r"[ \t\r\f\v]+")

# WordPress chrome that is never a process artefact: theme furniture, avatars, tracking pixels,
# resized thumbnails of the same asset, and the site's own logo/icon set.
CHROME = re.compile(r"(wp-content/themes|wp-content/plugins|wp-includes|gravatar|/logo|logo-|"
                    r"favicon|spinner|placeholder|avatar|flag|/icons?/|pixel|1x1|"
                    r"trisotech-logo|menu-|search-|close-|arrow)", re.I)


def slug_of(url):
    return re.sub(r"[^a-z0-9]+", "-", urllib.parse.urlparse(url).path.strip("/").lower()) or "root"


def unescape(s):
    return htmllib.unescape(s or "")


def fetch(url, dest=None, tries=3):
    if dest and os.path.exists(dest) and os.path.getsize(dest) > 0:
        return open(dest, encoding="utf-8", errors="replace").read()
    last = None
    for _ in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA,
                                                       "Accept-Language": "en-US,en;q=0.9"})
            with urllib.request.urlopen(req, timeout=45) as r:
                data = r.read().decode("utf-8", "replace")
            if dest:
                os.makedirs(os.path.dirname(dest), exist_ok=True)
                open(dest, "w", encoding="utf-8").write(data)
            time.sleep(1.0)
            return data
        except Exception as exc:                       # noqa: BLE001 - recorded, not raised
            last = exc
            time.sleep(2.0)
    return None


def digest(url, t):
    """Everything the screening pass needs, and nothing else."""
    head = t[:t.lower().find("</head>")] if "</head>" in t.lower() else t[:20000]
    title = re.search(r"<title[^>]*>(.*?)</title>", head, re.S | re.I)
    desc = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']*)', head, re.I)
    og = re.search(r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']*)', head, re.I)
    body = t[t.lower().find("<body"):] if "<body" in t.lower() else t
    text = TAG.sub(" ", SCRIPT.sub(" ", body))
    text = WS.sub(" ", unescape(text))
    text = re.sub(r"\n{2,}", "\n", text).strip()
    imgs = []
    for tag in IMG.findall(body):
        src = SRC.search(tag)
        if not src:
            continue
        u = unescape(src.group(1))
        if u.startswith("//"):
            u = "https:" + u
        if not u.startswith("http"):
            continue
        if CHROME.search(u):
            continue
        a = ALT.search(tag)
        imgs.append({"url": u.split("?")[0], "alt": unescape(a.group(1)) if a else ""})
    seen, uniq = set(), []
    for i in imgs:
        k = re.sub(r"-\d+x\d+(?=\.\w+$)", "", i["url"])
        if k in seen:
            continue
        seen.add(k)
        i["url"] = k
        uniq.append(i)
    return {
        "url": url,
        "title": unescape(title.group(1)).strip() if title else "",
        "description": unescape(desc.group(1)).strip() if desc else "",
        "og_image": unescape(og.group(1)) if og else "",
        "figures": uniq,
        "n_iframes": len(IFRAME.findall(body)),
        "iframes": [unescape(SRC.search(x).group(1)) for x in IFRAME.findall(body)
                    if SRC.search(x)][:6],
        "model_links": sorted({unescape(x) for x in MODEL.findall(body)})[:8],
        "n_svg": body.count("<svg"),
        "words": len(re.findall(r"\w+", text)),
        "text": text[:14000],
    }


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else "all"
    limit = None
    if "--limit" in sys.argv:
        limit = int(sys.argv[sys.argv.index("--limit") + 1])
    pop = json.load(open(os.path.join(RAW, "population.json")))
    urls = []
    if mode in ("content", "all"):
        urls += [(u, "content") for u in pop["content"]]
    if mode in ("rn", "all"):
        urls += [(u, "rn") for u in pop["release_notes"]
                 if RELEASE.search(u)]
    done = set()
    if os.path.exists(DIGESTS):
        for ln in open(DIGESTS, encoding="utf-8"):
            try:
                done.add(json.loads(ln)["url"])
            except Exception:
                pass
    todo = [(u, fam) for u, fam in urls if u not in done]
    if limit:
        todo = todo[:limit]
    print("mode=%s  population=%d  already digested=%d  to fetch=%d"
          % (mode, len(urls), len(done), len(todo)), flush=True)
    ok = bad = 0
    with open(DIGESTS, "a", encoding="utf-8") as fh:
        for i, (u, fam) in enumerate(todo, 1):
            dest = os.path.join(PAGES, slug_of(u) + ".html") if fam == "content" else None
            t = fetch(u, dest)
            if t is None:
                fh.write(json.dumps({"url": u, "family": fam, "error": "fetch-failed"}) + "\n")
                fh.flush()
                bad += 1
            else:
                d = digest(u, t)
                d["family"] = fam
                fh.write(json.dumps(d, ensure_ascii=False) + "\n")
                fh.flush()
                ok += 1
            if i % 25 == 0:
                print("  %d/%d ok=%d bad=%d  %s" % (i, len(todo), ok, bad, u[-60:]), flush=True)
    print("fetched ok=%d bad=%d" % (ok, bad))


if __name__ == "__main__":
    main()
