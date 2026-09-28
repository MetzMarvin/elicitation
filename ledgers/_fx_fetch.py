"""Fetch every page in the flowx-ai population as raw markdown.

Population = sitemap.xml (926 <loc>) U llms.txt (386 unique entries) = 934 items, frozen in
ledgers/flowx-ai.raw/population.json before any row was judged. See the ledger header for why the
population is the whole of docs.flowx.ai (all four published version trees plus the release-notes
archive) rather than the pinned version alone.

docs.flowx.ai is Mintlify: every page publishes its own markdown twin at `<url>.md` (the site says so
itself in llms.txt: "append .md to any page URL for markdown"), so the census screens the author's own
markdown rather than a scraped HTML rendering. Writes ledgers/flowx-ai.raw/pages/<slug>.md plus
ledgers/flowx-ai.raw/pages/fetch_log.jsonl. Idempotent: re-running skips what the log already has.

Rate: 4 workers with a 0.4 s gap between submissions, i.e. the offered load stays around one request
per second, slower than a reader clicking through the docs.
"""
import json, os, re, sys, threading, time, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor

ELI = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ELI, "flowx-ai.raw")
PAGES = os.path.join(RAW, "pages")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0 Safari/537.36")


def slug(u):
    """docs.flowx.ai/5.9/docs/building-blocks/process/process -> 5.9__docs__building-blocks__process__process"""
    p = re.sub(r"^https://docs\.flowx\.ai", "", u).strip("/")
    return p.replace("/", "__") or "root"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Referer": "https://docs.flowx.ai/"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.status, r.read().decode("utf-8", "replace")


def main():
    pop = json.load(open(os.path.join(RAW, "population.json")))
    os.makedirs(PAGES, exist_ok=True)
    logpath = os.path.join(RAW, "fetch_log.jsonl")
    done = set()
    if os.path.exists(logpath):
        for ln in open(logpath, encoding="utf-8"):
            try:
                o = json.loads(ln)
                if o.get("status") == 200:
                    done.add(o["url"])
            except Exception:
                pass
    todo = [u for u in pop if u not in done]
    print("population %d, already fetched %d, to fetch %d" % (len(pop), len(done), len(todo)))
    lock = threading.Lock()
    log = open(logpath, "a", encoding="utf-8")
    counts = {"ok": 0, "bad": 0}

    def one(u):
        # The 11 `/_llms/*` items are the site's own machine-readable indexes; their markdown is the
        # URL itself, not `<url>.md`. Every other page is Mintlify and publishes a `.md` twin.
        target = u if "/_llms/" in u else u + ".md"
        try:
            status, body = fetch(target)
            kind = "md"
        except urllib.error.HTTPError as exc:
            status, body, kind = exc.code, "", "error"
        except Exception as exc:                       # noqa: BLE001 - the log records the reason
            status, body, kind = 0, "", "error:%s" % exc
        with lock:
            if status == 200 and body.strip():
                open(os.path.join(PAGES, slug(u) + ".md"), "w", encoding="utf-8").write(body)
                counts["ok"] += 1
            else:
                counts["bad"] += 1
            log.write(json.dumps({"url": u, "target": target, "status": status, "kind": kind,
                                  "bytes": len(body)}) + "\n")
            log.flush()
            if (counts["ok"] + counts["bad"]) % 25 == 0:
                print("  %d ok, %d bad" % (counts["ok"], counts["bad"]), flush=True)
        time.sleep(0.4)

    with ThreadPoolExecutor(max_workers=4) as ex:
        list(ex.map(one, todo))
    log.close()
    print("fetched ok=%d bad=%d" % (counts["ok"], counts["bad"]))


if __name__ == "__main__":
    main()
