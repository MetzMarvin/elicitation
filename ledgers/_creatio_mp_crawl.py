#!/usr/bin/env python3
"""Enumerate and cache the Creatio Marketplace catalogue (second surface of the creatio source).

The catalogue page (marketplace.creatio.com/catalog, "Over 524 results") loads its cards from its own
JSON endpoint, seen in the network panel while scrolling the catalogue in the real browser:

    POST https://marketplace.creatio.com/search/ai
    {"sort":"popularity","ai_filter":null,"search":null,"facets":{},"offset":0,"count":20}
    -> {"numFound": 524, "results": [...], ...}

`numFound` is the catalogue's own exact total, i.e. the population. `ai_filter` is left null: this is
the UNFILTERED enumeration (the platform's own `is_ai` flag is recorded per item and used only as a
screen, never to narrow the population - shared rules section 6).

Every app page is server-rendered HTML to a plain GET (no Incapsula challenge on this host, unlike
www.creatio.com), so each item's listing page is cached too: its text, its figures (src + alt) and its
image file names are what the judgement runs on.

  python ledgers/_creatio_mp_crawl.py            # catalogue only (items.json)
  python ledgers/_creatio_mp_crawl.py --pages    # then every listing page (mp_pages.json)

Outputs: ledgers/_creatio/mp_items.json, ledgers/_creatio/mp_pages.json
"""
import json
import pathlib
import re
import sys
import time
import urllib.request

ELI = pathlib.Path(__file__).resolve().parents[1]
OUT = ELI / "ledgers" / "_creatio"
BASE = "https://marketplace.creatio.com"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/153.0.0.0 Safari/537.36 Edg/153.0.0.0")
HDRS = {"User-Agent": UA, "Accept-Language": "en-GB,en;q=0.9", "Accept": "*/*"}
RATE = 1.1


def post_search(offset, count=20, tries=3):
    body = json.dumps({"sort": "popularity", "ai_filter": None, "search": None, "facets": {},
                       "offset": offset, "count": count}).encode()
    h = dict(HDRS, **{"Content-Type": "application/json", "Origin": BASE,
                      "Referer": BASE + "/catalog"})
    for a in range(tries):
        try:
            req = urllib.request.Request(BASE + "/search/ai", data=body, headers=h)
            with urllib.request.urlopen(req, timeout=60) as f:
                return json.loads(f.read())
        except Exception as e:
            print("  retry", offset, type(e).__name__, e, flush=True)
            time.sleep(3 * (a + 1))
    raise RuntimeError("catalogue offset %d failed" % offset)


def catalogue():
    first = post_search(0)
    total = first["numFound"]
    items, seen = [], set()
    d = first
    offset = 0
    while True:
        for it in d["results"]:
            if it["link"] in seen:
                continue
            seen.add(it["link"])
            items.append({k: it.get(k) for k in ("link", "title", "developer", "is_ai", "categories",
                                                 "labels", "rating", "rating_count", "upcoming",
                                                 "description")})
        print("  offset %-4d items %-4d / %d" % (offset, len(items), total), flush=True)
        offset += 20
        if offset >= total or not d["results"]:
            break
        time.sleep(RATE)
        d = post_search(offset)
    (OUT / "mp_items.json").write_text(json.dumps(
        {"source": "https://marketplace.creatio.com/catalog", "endpoint": BASE + "/search/ai",
         "request_body": {"sort": "popularity", "ai_filter": None, "search": None, "facets": {},
                          "offset": "<0..%d>" % (offset - 20), "count": 20},
         "numFound": total, "items": items}, indent=1, ensure_ascii=False), encoding="utf-8")
    print("catalogue: %d items written (numFound %d)" % (len(items), total), flush=True)
    return items


def main_seg(html):
    m = re.search(r"<main[^>]*>(.*?)</main>", html, re.S)
    seg = m.group(1) if m else html
    seg = re.sub(r"<script.*?</script>|<style.*?</style>|<!--.*?-->", " ", seg, flags=re.S)
    return seg


def page(link):
    url = BASE + link
    for a in range(3):
        try:
            req = urllib.request.Request(url, headers=HDRS)
            with urllib.request.urlopen(req, timeout=60) as f:
                html = f.read().decode("utf-8", "replace")
            break
        except Exception as e:
            if a == 2:
                return {"url": url, "status": "error", "error": "%s: %s" % (type(e).__name__, e)}
            time.sleep(3 * (a + 1))
    seg = main_seg(html)
    imgs = []
    for tag in re.findall(r"<img[^>]*>", seg):
        src = re.search(r'src="([^"]+)"', tag)
        if not src:
            continue
        s = src.group(1)
        if re.search(r"(/labels/|/mp-icon|/styles/detailed_logo/|\.svg(\?|$))", s):
            continue
        if re.search(r"/sites/marketplace/files/", s):
            imgs.append({"src": s if s.startswith("http") else BASE + s,
                         "alt": (re.search(r'alt="([^"]*)"', tag) or [None, ""])[1]})
    txt = re.sub(r"<[^>]+>", " ", seg)
    txt = (txt.replace("&nbsp;", " ").replace("&amp;", "&").replace("&#039;", "'")
              .replace("&quot;", '"').replace("&gt;", ">").replace("&lt;", "<"))
    txt = re.sub(r"\s+", " ", txt).strip()
    m = re.search(r'property="og:url" content="([^"]+)"', html)
    return {"url": m.group(1) if m else url, "status": "ok", "bytes": len(html),
            "title": (re.search(r"<title>(.*?)</title>", html, re.S) or [None, ""])[1].strip(),
            "text": txt[:12000], "imgs": imgs, "text_len": len(txt)}


def pages(items):
    P = OUT / "mp_pages.json"
    cached = json.loads(P.read_text(encoding="utf-8")) if P.exists() else {}
    todo = [it for it in items if it["link"] not in cached]
    print("listing pages: %d to fetch (%d cached)" % (len(todo), len(cached)), flush=True)
    for i, it in enumerate(todo, 1):
        cached[it["link"]] = page(it["link"])
        if i % 20 == 0 or i == len(todo):
            P.write_text(json.dumps(cached, ensure_ascii=False), encoding="utf-8")
            print("  fetched %d/%d (saved)" % (i, len(todo)), flush=True)
        time.sleep(RATE)
    P.write_text(json.dumps(cached, ensure_ascii=False), encoding="utf-8")
    ok = sum(1 for v in cached.values() if v.get("status") == "ok")
    print("pages cached: %d ok of %d" % (ok, len(cached)), flush=True)


if __name__ == "__main__":
    items = catalogue() if not (OUT / "mp_items.json").exists() else json.loads(
        (OUT / "mp_items.json").read_text(encoding="utf-8"))["items"]
    print("items:", len(items))
    if "--pages" in sys.argv:
        pages(items)
