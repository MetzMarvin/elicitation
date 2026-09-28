"""Build the trisotech census population from the site's own sitemap, and say what is in it.

The assignment's entry point is https://www.trisotech.com/sitemap.xml. This script fetches it once,
parses every <loc>, deduplicates by URL (the sitemap repeats some entries with different lastmod),
splits the result into the release-notes family and everything else, and freezes the lists in
ledgers/trisotech.raw/population.json. Nothing is narrowed here: both lists are written out in full,
and the split is recorded so the ledger header can state exactly what was judged and what was not.

Usage:
  python ledgers/_ts_pop.py            fetch (cached) + write population.json + print the summary
  python ledgers/_ts_pop.py --show     print the summary from the cached sitemap only
"""
import json, os, re, sys, time, urllib.request

ELI = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ELI, "trisotech.raw")
SITEMAP = "https://www.trisotech.com/sitemap.xml"
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0 Safari/537.36")

RELEASE = re.compile(r"release-notes", re.I)   # every modeler family, not just the suite


def fetch(url, dest=None, tries=3):
    p = os.path.join(RAW, dest) if dest else None
    if p and os.path.exists(p) and os.path.getsize(p) > 0:
        return open(p, encoding="utf-8", errors="replace").read()
    last = None
    for _ in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=45) as r:
                data = r.read().decode("utf-8", "replace")
            if p:
                os.makedirs(RAW, exist_ok=True)
                open(p, "w", encoding="utf-8").write(data)
            time.sleep(1.0)
            return data
        except Exception as exc:                       # noqa: BLE001 - reported, not raised
            last = exc
            time.sleep(2.0)
    raise SystemExit("FAILED to fetch %s: %s" % (url, last))


def main():
    os.makedirs(RAW, exist_ok=True)
    xml = fetch(SITEMAP, "sitemap.xml")
    locs = re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", xml)
    uniq = list(dict.fromkeys(locs))                   # dedupe by URL, first occurrence wins
    rel = [u for u in uniq if RELEASE.search(u)]
    content = [u for u in uniq if not RELEASE.search(u)]
    out = {
        "source": "trisotech",
        "sitemap": SITEMAP,
        "fetched": time.strftime("%Y-%m-%d"),
        "loc_entries": len(locs),
        "unique_urls": len(uniq),
        "release_notes": rel,
        "content": content,
    }
    json.dump(out, open(os.path.join(RAW, "population.json"), "w", encoding="utf-8"), indent=0)
    print("sitemap <loc> entries:", len(locs))
    print("unique after deduplication:", len(uniq),
          "(repeats: %d)" % (len(locs) - len(uniq)))
    print("release-notes family:", len(rel))
    print("content pages:", len(content))
    ai = [u for u in content if re.search(r"ai|agent|genai|llm|copilot", u, re.I)]
    print("content pages with an AI-ish slug (facet cross-check only, NOT a filter):", len(ai))
    import collections
    pref = collections.Counter(re.sub(r"^https://www\.trisotech\.com", "", u).split("/")[1]
                               for u in content)
    print("content pages by first path segment:")
    for k, v in pref.most_common(20):
        print("   %5d  /%s/" % (v, k))
    print("   %5d  (root)" % pref.get("", 0))


if __name__ == "__main__":
    main()
