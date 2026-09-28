#!/usr/bin/env python3
"""Enumerate and cache every page of doc.scheer-pas.com (the scheer-pas source).

The documentation site is a Confluence-backed Scroll Sites instance: every doc space publishes its
own complete page tree as JSON (`/<space>/latest/__pagetree.json`), which is this source's own
enumeration endpoint - an exact, finite population, not a search ranking. This script:

  1. lists the spaces from the docs home page (not guessed: extracted from the DOM),
  2. fetches each space's __pagetree.json and flattens it to page paths,
  3. fetches every page's HTML (~1 req/s) into ledgers/_scheer/pages/<slug>.html,
  4. writes ledgers/_scheer/index.json  - one object per page: space, title, path, url, status,
     bytes, figure count, and the page's own "version" (the docs selector's pinned version).

Resumable: pages already cached are skipped, so a re-run only fills gaps.

  python ledgers/_scheer_crawl.py            # crawl what is missing
  python ledgers/_scheer_crawl.py --trees    # only refresh the page trees (no page fetch)
"""
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request

BASE = "https://doc.scheer-pas.com"
OUT = pathlib.Path(__file__).resolve().parent / "_scheer"
PAGES = OUT / "pages"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126 Safari/537.36"}


def get(url, timeout=60, tries=4):
    """The host resets an occasional connection (WinError 10054) under a steady 1 req/s. Retry with
    backoff rather than letting one reset end the run."""
    last = None
    for k in range(tries):
        try:
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=timeout) as f:
                return f.status, f.read()
        except urllib.error.HTTPError as e:
            last = e
            if e.code in (403, 404, 410):
                raise
        except Exception as e:
            last = e
        time.sleep(2 + 3 * k)
    raise last


def spaces():
    """The doc spaces, extracted from the docs home page DOM (never guessed)."""
    _, b = get(BASE + "/")
    t = b.decode("utf-8", "replace")
    found = sorted({m.group(1) for m in re.finditer(r'href="(/[a-z0-9\-]+(?:/latest)?)"', t)})
    out = []
    for f in found:
        if f.startswith("/assets"):
            continue
        out.append(f.strip("/").replace("/latest", ""))
    return out


def tree(slug):
    """A space publishes its page tree as JSON. Most live under /<space>/latest/, but `help` and
    `release-notes` are un-versioned (their paths carry no /latest segment), so both are tried."""
    for url in ("%s/%s/latest/__pagetree.json" % (BASE, slug), "%s/%s/__pagetree.json" % (BASE, slug)):
        try:
            _, b = get(url)
        except urllib.error.HTTPError as e:
            last = "HTTP %s" % e.code
            continue
        (OUT / ("pagetree-%s.json" % slug)).write_bytes(b)
        return json.loads(b), None
    return None, last


def flatten(nodes, acc):
    for n in nodes:
        if n.get("path"):
            acc.append((n.get("title") or "", n["path"]))
        flatten(n.get("children") or [], acc)
    return acc


def main():
    PAGES.mkdir(parents=True, exist_ok=True)
    idx_path = OUT / "index.json"
    idx = json.loads(idx_path.read_text(encoding="utf-8")) if idx_path.exists() else {}
    for s in spaces():
        t, err = tree(s)
        if err:
            print("%-22s tree: %s" % (s, err))
            continue
        rows = flatten(t, [])
        print("%-22s pages: %d" % (s, len(rows)))
        for title, path in rows:
            idx.setdefault(path, {"space": s, "title": title, "path": path,
                                  "url": BASE + path, "status": None})
            idx[path]["title"] = title or idx[path].get("title")
            idx[path]["space"] = s
        time.sleep(0.6)
    idx_path.write_text(json.dumps(idx, ensure_ascii=False, indent=1), encoding="utf-8")
    print("index: %d pages" % len(idx))
    if "--trees" in sys.argv:
        return
    todo = [p for p in sorted(idx) if idx[p].get("status") != "ok"]
    print("to fetch: %d" % len(todo))
    for k, path in enumerate(todo, 1):
        rec = idx[path]
        dest = PAGES / (path.strip("/").replace("/", "__") + ".html")
        if dest.exists() and dest.stat().st_size > 2000:
            rec["status"] = "ok"
            rec["bytes"] = dest.stat().st_size
        else:
            try:
                s, b = get(BASE + path)
                dest.write_bytes(b)
                rec["status"] = "ok"
                rec["bytes"] = len(b)
            except urllib.error.HTTPError as e:
                rec["status"] = "http-%s" % e.code
            except Exception as e:
                rec["status"] = "err"
                rec["error"] = str(e)[:120]
            time.sleep(1.1)
        if k % 25 == 0 or k == len(todo):
            idx_path.write_text(json.dumps(idx, ensure_ascii=False, indent=1), encoding="utf-8")
            print("  %d/%d  %s  %s" % (k, len(todo), rec["status"], path[:70]), flush=True)
    bad = [p for p in idx if idx[p].get("status") != "ok"]
    print("done: %d cached, %d not ok" % (len(idx) - len(bad), len(bad)))
    for p in bad[:20]:
        print("   NOT OK", idx[p]["status"], p)


if __name__ == "__main__":
    main()
