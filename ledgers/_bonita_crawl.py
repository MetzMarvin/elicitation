#!/usr/bin/env python3
"""Enumerate and crawl the bonitasoft/ofelia source (worker elicitation-6f, 2026-09-25).

Enumeration source: the documentation portal publishes a sitemap index
(https://documentation.ofelia.com/sitemap.xml) with one sitemap per doc component, each
carrying an exact URL count - the "catalogue's own endpoint" case of the shared rules. The
marketing site does the same (https://www.ofelia.com/sitemap.xml, hreflang-triplicated).

Population (census=True):
  * documentation.ofelia.com, `latest` version of each of the 7 components
  * www.ofelia.com English pages (the hreflang en/x-default variant of each URL)
Older Antora versions (2026.1 ... 2023.1, /next/, /0/) are a *version facet* of the same
pages, not additional items; the pages that exist only in an older version are separately
screened (see `facet` mode) so nothing is silently dropped.

  python ledgers/_bonita_crawl.py enum           # build the population -> ledgers/_bonita/population.json
  python ledgers/_bonita_crawl.py facet          # what older versions hold that `latest` does not
  python ledgers/_bonita_crawl.py fetch          # crawl every URL -> ledgers/_bonita/pages/ + index.json
"""
import hashlib
import json
import pathlib
import re
import sys
import time
import urllib.request

ELI = pathlib.Path(__file__).resolve().parents[1]
OUT = ELI / "ledgers" / "_bonita"
PAGES = OUT / "pages"
POP = OUT / "population.json"
INDEX = OUT / "index.json"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                    "Chrome/126 Safari/537.36"}
DOCS = "https://documentation.ofelia.com"
SITE = "https://www.ofelia.com"
LATEST_COMPONENTS = ["bcd", "bonita", "cloud", "labs", "process-designer", "test-toolkit",
                     "ui-builder"]


def get(url, tries=3):
    last = None
    for _ in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=90) as fh:
                return fh.read().decode("utf-8", "replace")
        except Exception as exc:  # noqa: BLE001
            last = exc
            time.sleep(1.5)
    raise last


def locs(xml):
    return re.findall(r"<loc>([^<]+)</loc>", xml)


def older_only(doc_urls):
    """[(comp, version, url)] for doc pages that exist in an older version but not in `latest`.

    The version selector serves the same page at several versions (a facet, not extra items);
    a path that exists only under an older version is not covered by the `latest` census, so
    it is enumerated separately rather than silently dropped.
    """
    have = set()
    for u in doc_urls:
        comp = u.split("/")[3]
        if "/latest/" not in u:
            continue
        have.add(comp + "/" + u.split("/latest/", 1)[1])
    out = []
    for comp in LATEST_COMPONENTS:
        f = OUT / ("older_%s.json" % comp)
        if not f.exists():
            continue
        seen = set()
        for u in json.loads(f.read_text(encoding="utf-8")):
            m = re.search(r"/%s/([^/]+)/(.*)$" % re.escape(comp), u)
            if not m:
                continue
            key = comp + "/" + m.group(2)
            if key in have or key in seen:
                continue
            seen.add(key)
            out.append((comp, m.group(1), u))
    return out


def enumerate_population():
    OUT.mkdir(parents=True, exist_ok=True)
    idx = locs(get(DOCS + "/sitemap.xml"))
    groups, doc_urls = {}, {}
    for sm in idx:
        us = locs(get(sm))
        comp = re.search(r"sitemap-([a-z-]+)\.xml", sm).group(1)
        latest = [u for u in us if re.search(r"/%s/latest/" % re.escape(comp), u)]
        older = [u for u in us if u not in latest]
        groups[comp] = {"sitemap": sm, "total": len(us), "latest": len(latest),
                        "other_versions": len(older)}
        doc_urls[comp] = latest
        pathlib.Path(OUT / ("older_%s.json" % comp)).write_text(
            json.dumps(older, ensure_ascii=False, indent=1), encoding="utf-8")
    site_all = locs(get(SITE + "/sitemap.xml"))
    site_en = [u for u in site_all
               if not re.match(r"https://www\.ofelia\.com/(fr|es)(/|$)", u)]
    dd = {u: None for u in sum(doc_urls.values(), [])}
    old = older_only(sorted(dd))
    for _, _, u in old:
        dd[u] = None
    pop = {
        "read": "2026-09-25",
        "docs_sitemap_index": DOCS + "/sitemap.xml",
        "site_sitemap": SITE + "/sitemap.xml",
        "components": groups,
        "docs_latest": {"count": len(doc_urls["bonita"]) + sum(
            len(v) for k, v in doc_urls.items() if k != "bonita")},
        "docs_older_only": {"count": len(old),
                            "note": "paths published only under an older Antora version; "
                                    "enumerated so the version facet can be screened too",
                            "by_component": {c: sum(1 for x in old if x[0] == c)
                                             for c in LATEST_COMPONENTS}},
        "site": {"count": len(set(site_en)), "total_incl_locales": len(site_all)},
        "docs_urls": sorted(dd),
        "site_urls": sorted(set(site_en)),
    }
    pop["population_size"] = len(pop["docs_urls"]) + len(pop["site_urls"])
    OUT.mkdir(parents=True, exist_ok=True)
    POP.write_text(json.dumps(pop, ensure_ascii=False, indent=1), encoding="utf-8")
    print("docs components (latest): " + ", ".join(
        "%s=%d/%d" % (k, v["latest"], v["total"]) for k, v in sorted(groups.items())))
    print("docs latest urls: %d | docs older-only urls: %d | site en urls: %d | population: %d"
          % (len(doc_urls["bonita"]) + sum(len(v) for k, v in doc_urls.items() if k != "bonita"),
             len(old), len(pop["site_urls"]), pop["population_size"]))
    return pop


def facet():
    """Version facet: URL paths that exist only in an older version -> slug tokens to look at."""
    pop = json.loads(POP.read_text(encoding="utf-8"))
    old = older_only(pop["docs_urls"])
    ai = re.compile(r"ai-|agent|llm|openai|mistral|gpt|chat|intelligen", re.I)
    by = {}
    for comp, ver, u in old:
        by.setdefault(comp, []).append((ver, u))
    for comp, items in sorted(by.items()):
        hits = [u for _, u in items if ai.search(u.split("/", 4)[-1])]
        print("%-16s only-older: %3d | ai-ish slugs: %s" % (comp, len(items), hits or "-"))
    print("total only-older paths: %d" % len(old))


def fetch():
    pop = json.loads(POP.read_text(encoding="utf-8"))
    urls = pop["docs_urls"] + pop["site_urls"]
    PAGES.mkdir(parents=True, exist_ok=True)
    idx = json.loads(INDEX.read_text(encoding="utf-8")) if INDEX.exists() else {}
    todo = [u for u in urls if u not in idx]
    print("population %d | cached %d | todo %d" % (len(urls), len(idx), len(todo)), flush=True)
    for k, u in enumerate(todo, 1):
        rec = {"url": u}
        try:
            html = get(u, tries=2)
            f = PAGES / ("%s__%s.html" % (hashlib.sha1(u.encode()).hexdigest()[:12],
                                          re.sub(r"[^a-z0-9]+", "-", u.split("//")[1].lower())[:60]))
            f.write_text(html, encoding="utf-8")
            rec.update({"file": f.name, "bytes": len(html), "status": 200,
                        "title": (re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I) or
                                  [None, ""])[1].strip()[:120]})
        except Exception as exc:  # noqa: BLE001
            rec.update({"file": None, "status": "ERR", "error": repr(exc)[:120]})
        idx[u] = rec
        if k % 25 == 0 or k == len(todo):
            INDEX.write_text(json.dumps(idx, ensure_ascii=False, indent=1), encoding="utf-8")
            print("  %d/%d  last=%s %s" % (k, len(todo), rec.get("status"),
                                           u.split("//")[1][:70]), flush=True)
        time.sleep(1.0)
    INDEX.write_text(json.dumps(idx, ensure_ascii=False, indent=1), encoding="utf-8")
    bad = [r for r in idx.values() if r.get("status") != 200]
    print("fetched %d | failures %d" % (len(idx), len(bad)))
    for r in bad[:20]:
        print("  FAIL", r["url"], r.get("status"), r.get("error", ""))


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "enum"
    if mode == "enum":
        enumerate_population()
    elif mode == "facet":
        facet()
    elif mode == "fetch":
        fetch()
