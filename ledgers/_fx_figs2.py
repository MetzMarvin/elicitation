"""Download every figure referenced by the census's E1 rows, hash it, and collapse duplicates.

The E1 rows are the ones whose note claims something about the page's figures. 530 rows reference
thousands of figure URLs; many of those URLs are the same file, and many different URLs are the same
bytes (the version trees re-publish identical PNGs). This script turns the reference list into a
deduplicated *work list*: one entry per distinct image, with the rows that need it.

Writes:
  figures/<sha1[:10]>_<name>.<ext>   one file per distinct image
  figs_inventory.json                {sha: {urls, rows, name, bytes, w, h, ai_rows, plain_rows}}
  figs_progress.jsonl                append-only fetch log, so a re-run resumes

Usage:
  python ledgers/_fx_figs2.py download [--limit N] [--only ai|all]
  python ledgers/_fx_figs2.py show
"""
import hashlib, json, os, re, sys, time, urllib.parse, urllib.request

ELI = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ELI, "flowx-ai.raw")
FIGS = os.path.join(RAW, "figures2")
INV = os.path.join(RAW, "figs_inventory.json")
PROG = os.path.join(RAW, "figs_progress.jsonl")
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/131.0 Safari/537.36")


def rows_e1():
    out = []
    for ln in open(os.path.join(ELI, "flowx-ai.jsonl"), encoding="utf-8"):
        r = json.loads(ln)
        if r.get("type") or r.get("reason") != "E1-not-bpmn":
            continue
        out.append(r)
    return out


def build_refs():
    """{url: {"rows": [...], "ai_rows": [...], "alt": str}} over all E1 rows."""
    figs = json.load(open(os.path.join(RAW, "figmeta.json")))
    refs = {}
    for r in rows_e1():
        ai = "ai=True" in (r.get("screen") or "")
        for f in (figs.get(r["url"]) or []):
            e = refs.setdefault(f["url"], {"rows": [], "ai_rows": [], "alt": f.get("alt", "")})
            e["rows"].append(r["n"])
            if ai:
                e["ai_rows"].append(r["n"])
    return refs


def name_of(u):
    n = urllib.parse.unquote(os.path.basename(urllib.parse.urlparse(u).path)) or "img"
    return re.sub(r"[^A-Za-z0-9._-]", "_", n)[:60]


def fetch(u):
    req = urllib.request.Request(u, headers={"User-Agent": UA, "Referer": "https://docs.flowx.ai/"})
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read()


def download(limit=None, only="all"):
    refs = {u: e for u, e in build_refs().items() if only == "all" or e["ai_rows"]}
    os.makedirs(FIGS, exist_ok=True)
    done = set()
    if os.path.exists(PROG):
        for ln in open(PROG, encoding="utf-8"):
            try:
                done.add(json.loads(ln)["url"])
            except Exception:
                pass
    todo = [u for u in refs if u not in done]
    if limit:
        todo = todo[:limit]
    print("distinct figure URLs: %d | already tried: %d | to fetch: %d"
          % (len(refs), len(done), len(todo)), flush=True)
    ok = bad = 0
    with open(PROG, "a", encoding="utf-8") as fh:
        for i, u in enumerate(todo, 1):
            rec = {"url": u, "name": name_of(u)}
            try:
                data = fetch(u)
                sha = hashlib.sha1(data).hexdigest()
                ext = os.path.splitext(name_of(u))[1].lower() or ".png"
                rec.update({"sha": sha, "bytes": len(data), "file": sha[:10] + "_" + name_of(u)})
                p = os.path.join(FIGS, rec["file"])
                if not os.path.exists(p):
                    open(p, "wb").write(data)
                ok += 1
            except Exception as exc:                       # noqa: BLE001
                rec["error"] = str(exc)[:120]
                bad += 1
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
            fh.flush()
            if i % 20 == 0:
                print("  %d/%d ok=%d bad=%d" % (i, len(todo), ok, bad), flush=True)
            time.sleep(0.35)
    print("fetched ok=%d bad=%d" % (ok, bad))


def build_inventory():
    refs = build_refs()
    by_sha = {}
    for ln in open(PROG, encoding="utf-8"):
        rec = json.loads(ln)
        u = rec["url"]
        e = refs.get(u)
        if e is None or "sha" not in rec:
            continue
        d = by_sha.setdefault(rec["sha"], {"urls": [], "rows": [], "ai_rows": [], "file": rec["file"],
                                           "bytes": rec["bytes"], "names": []})
        d["urls"].append(u)
        d["rows"] += e["rows"]
        d["ai_rows"] += e["ai_rows"]
        d["names"].append(rec["name"])
    for d in by_sha.values():
        d["rows"] = sorted(set(d["rows"]))
        d["ai_rows"] = sorted(set(d["ai_rows"]))
        d["names"] = sorted(set(d["names"]))[:4]
    json.dump(by_sha, open(INV, "w", encoding="utf-8"), indent=0)
    print("distinct images (by sha1):", len(by_sha))
    print("  needed by an ai=True E1 row:", sum(1 for d in by_sha.values() if d["ai_rows"]))
    print("  needed only by ai=False E1 rows:", sum(1 for d in by_sha.values() if not d["ai_rows"]))
    print("  bytes on disk: %.1f MB" % (sum(d["bytes"] for d in by_sha.values()) / 1e6))
    return by_sha


def main():
    cmd = sys.argv[1]
    if cmd == "download":
        only = "ai" if "--only" in sys.argv and sys.argv[sys.argv.index("--only") + 1] == "ai" else "all"
        limit = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else None
        download(limit, only)
    elif cmd == "show":
        build_inventory()
    elif cmd == "inv":
        build_inventory()


if __name__ == "__main__":
    main()
