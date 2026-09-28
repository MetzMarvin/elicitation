"""Fetch every page in the processmaker population, in whichever form it publishes.

Population = sitemap-en.xml (707 <loc>) U llms.txt (715 entries) = 716 items.

The `/docs/*` pages publish a server-rendered markdown twin (`<url>.md`, front matter +
article body + figure references), which is what the census screens offline. The
`/apidocs/*` pages have no markdown twin: they return HTML, so the same HTML the browser
gets is saved and its `editor360-preview-content` article is sliced out for screening.

Writes ledgers/processmaker.raw/pages/md/<slug>.md (markdown twin) and ledgers/processmaker.raw/pages/html/<slug>.html
(apidocs and anything else without a twin), plus ledgers/processmaker.raw/pages/fetch_log.jsonl.

Rate: the site answers in ~9 s per page, so 4 workers with a 0.5 s gap between submissions
keeps the offered load at well under one request per second - slower, in fact, than a single
reader clicking through the docs.
"""
import json, os, re, sys, threading, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

ELI = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ELI, "processmaker.raw/pages")
MD = os.path.join(RAW, "md")
HTML = os.path.join(RAW, "html")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0 Safari/537.36")


def slug(u):
    p = re.sub(r"^https://docs\.processmaker\.com", "", u).strip("/")
    return (p.replace("/", "__") or "root")


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                              "Referer": "https://docs.processmaker.com/"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.status, r.read().decode("utf-8", "replace")


def main():
    pop = json.load(open(os.path.join(RAW, "population.json")))
    os.makedirs(MD, exist_ok=True)
    os.makedirs(HTML, exist_ok=True)
    logpath = os.path.join(RAW, "fetch_log.jsonl")
    done = set()
    if os.path.exists(logpath):
        for ln in open(logpath, encoding="utf-8"):
            try:
                o = json.loads(ln)
                if o.get("kind"):
                    done.add(o["url"])
            except Exception:
                pass
    todo = [u for u in pop if u not in done]
    lock = threading.Lock()
    log = open(logpath, "a", encoding="utf-8")
    counts = {"ok": 0, "bad": 0}

    def one(u):
        base = slug(u)
        st, body, kind = -1, "", None
        for attempt, url in ((1, u + ".md"), (2, u.rstrip("/") or u)):
            if attempt == 1 and u.endswith(".md"):
                continue
            try:
                st, body = fetch(url)
            except Exception as e:
                st, body = -1, str(e)
                continue
            if st != 200:
                continue
            # The `/docs/*` twins open with YAML front matter; the `/apidocs/*` twins have
            # none and open with the Documentation Index banner. Both are markdown, and
            # testing only for front matter sent every apidocs page down the HTML path,
            # where the SPA bundle (not the article) was what got screened.
            if attempt == 1 and (body.lstrip().startswith("---")
                                 or body.lstrip().startswith("> ## Documentation Index")):
                kind = "md"
                break
            if "<article" in body or "<html" in body[:2000].lower():
                kind = "html"
                break
            st = 0
        if kind == "md":
            open(os.path.join(MD, base + ".md"), "w", encoding="utf-8").write(body)
        elif kind == "html":
            open(os.path.join(HTML, base + ".html"), "w", encoding="utf-8").write(body)
        with lock:
            counts["ok" if kind else "bad"] += 1
            log.write(json.dumps({"url": u, "status": st if kind else (st if st < 0 else 0),
                                  "kind": kind, "bytes": len(body)}) + "\n")
            log.flush()
            n = counts["ok"] + counts["bad"]
            if n % 40 == 0:
                print("%d/%d ok=%d bad=%d" % (n, len(todo), counts["ok"], counts["bad"]), flush=True)

    with ThreadPoolExecutor(max_workers=2) as ex:
        futs = []
        for u in todo:
            futs.append(ex.submit(one, u))
            time.sleep(0.6)
        for f in futs:
            f.result()
    print("DONE ok=%d bad=%d of %d (already had %d)" % (counts["ok"], counts["bad"], len(todo), len(done)))
    bad = [json.loads(l)["url"] for l in open(logpath, encoding="utf-8")
           if not json.loads(l).get("kind")]
    if bad:
        print("FAILED (%d):" % len(bad), bad[:20])



if __name__ == "__main__":
    main()
