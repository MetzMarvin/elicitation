#!/usr/bin/env python3
"""For each marketplace listing whose page mentions a process model, record what each figure sits under.

The 537 listing pages cannot each be opened by eye, and on this surface the figures carry no captions
and no alt text - only vendor file names. What the page does give is structure: every figure sits in a
section under a heading ("Key features", "Business process automation", "AI-powered search", ...).
This script re-fetches the candidate listings (those whose body/alt/file names contain a process-model
token) and records, per figure: its file name, its alt, the nearest preceding heading, and the 240
characters of text just before it. The visual pass then looks only at figures whose surrounding
evidence suggests a diagram, and at the file names that suggest one outright.

  python ledgers/_creatio_mp_figctx.py            # uses the candidate list it computes itself
"""
import html as htmlmod
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
HDRS = {"User-Agent": UA, "Accept-Language": "en-GB,en;q=0.9"}

sys.path.insert(0, str(ELI / "ledgers"))
from _creatio_mp_rows import EYES, PROC, TAG_BPE, AI, body  # noqa: E402  (the same screens)


def strip(t):
    t = re.sub(r"<script.*?</script>|<style.*?</style>|<!--.*?-->", " ", t, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    t = htmlmod.unescape(t)
    return re.sub(r"\s+", " ", t).strip()


def fig_ctx(html):
    m = re.search(r"<main[^>]*>(.*?)</main>", html, re.S)
    seg = m.group(1) if m else html
    heads = [(h.start(), strip(h.group(1))[:120]) for h in
             re.finditer(r"<h[2-5][^>]*>(.*?)</h[2-5]>", seg, re.S)]
    out = []
    for im in re.finditer(r"<img[^>]*>", seg):
        tag = im.group(0)
        src = re.search(r'src="([^"]+)"', tag)
        if not src or not re.search(r"/sites/marketplace/files/", src.group(1)):
            continue
        if re.search(r"(/labels/|/mp-icon|/styles/detailed_logo/|\.svg(\?|$))", src.group(1)):
            continue
        prev = [h for h in heads if h[0] < im.start()]
        before = strip(seg[max(0, im.start() - 400):im.start()])[-240:]
        out.append({"file": src.group(1).split("/")[-1],
                    "alt": (re.search(r'alt="([^"]*)"', tag) or [None, ""])[1],
                    "heading": prev[-1][1] if prev else None,
                    "before": before})
    return out


def fetch(link):
    url = BASE + link
    for a in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=HDRS), timeout=60) as f:
                return f.read().decode("utf-8", "replace")
        except Exception:
            time.sleep(3 * (a + 1))
    return ""


def candidates():
    items = json.loads((OUT / "mp_items.json").read_text(encoding="utf-8"))["items"]
    pages = json.loads((OUT / "mp_pages.json").read_text(encoding="utf-8"))
    blog = json.loads((OUT / "mp_blog_index.json").read_text(encoding="utf-8"))["articles"]
    out = []
    for it in items:
        p = pages.get(it["link"])
        if not p or p.get("status") != "ok":
            continue
        hay = " ".join([p.get("text", "")] + [(i.get("alt") or "") for i in p.get("imgs", [])]
                       + [i["src"].split("/")[-1] for i in p.get("imgs", [])])
        if EYES.search(hay):
            out.append(it["link"])
    return out, blog


def main():
    links, blog = candidates()
    P = OUT / "mp_figctx.json"
    cached = json.loads(P.read_text(encoding="utf-8")) if P.exists() else {}
    todo = [l for l in links + blog if l not in cached]
    print("candidate listings: %d apps + %d blog articles; %d to fetch" % (
        len(links), len(blog), len(todo)), flush=True)
    for i, l in enumerate(todo, 1):
        cached[l] = fig_ctx(fetch(l))
        if i % 10 == 0 or i == len(todo):
            P.write_text(json.dumps(cached, ensure_ascii=False), encoding="utf-8")
            print("  fetched %d/%d (saved)" % (i, len(todo)), flush=True)
        time.sleep(1.1)
    P.write_text(json.dumps(cached, ensure_ascii=False), encoding="utf-8")
    tot = sum(len(v) for v in cached.values())
    print("figure contexts cached: %d listings, %d figures" % (len(cached), tot))


if __name__ == "__main__":
    main()
