#!/usr/bin/env python3
"""Cache what the ledger needs to know about the linked repositories (worker elicitation-6f).

The GitHub API is unauthenticated here, so it rate-limits (60 req/hour) and a live call at build
time would sometimes answer 403 and make a reachable repository look blocked. This gathers, once,
the four things the census needs per repository - default branch, file count, every `.bpmn`/
`.proc` path found in the tree, and every README/`.adoc` path - and caches them to
ledgers/_bonita/repos_trees.json. The ledger build then reads the cache and never touches the
network. A repository that still cannot be read keeps its error and becomes a BLOCKED row.

The first pass (`_bonita_repos.py`) already recorded exactly these fields for the repositories it
could reach, so they are seeded from ledgers/_bonita/repos.json and only the gaps are fetched.

  python ledgers/_bonita_repos_trees.py [--only NAME ...] [--force]
"""
import json
import pathlib
import re
import sys
import time
import urllib.request

ELI = pathlib.Path(__file__).resolve().parents[1]
OUT = ELI / "ledgers" / "_bonita"
REPOS = OUT / "repos.json"
CACHE = OUT / "repos_trees.json"
UA = {"User-Agent": "elicitation-census", "Accept": "application/vnd.github+json"}
ARTEFACT = re.compile(r"\.bpmn$|\.proc$", re.I)
DOCFILE = re.compile(r"(^|/)README(\.\w+)?$|\.adoc$", re.I)


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def canon(name):
    return name[:-4] if name.endswith(".git") else name


def seed_from_repos_json():
    """{repo: entry} from the first pass, canonicalised and reduced to the fields we keep.

    Note: `_bonita_repos_fix.py --write` stores a successful repository with an explicit
    `"status": null`, so a truthiness test - not `"status" not in rec` - is what separates a
    reached repository from an error here.
    """
    out = {}
    for name, rec in json.loads(REPOS.read_text(encoding="utf-8"))["linked_repos"].items():
        c = canon(name)
        e = out.setdefault(c, {})
        if rec.get("status"):
            e.setdefault("error", rec["status"])
        else:
            e.pop("error", None)
            e.update({"branch": rec.get("branch"), "files": rec.get("files"),
                      "artefacts": rec.get("artefacts", []), "readme": rec.get("readme", [])})
    return out


def main():
    force = "--force" in sys.argv
    only = [a for a in sys.argv[1:] if not a.startswith("--")]
    cache = seed_from_repos_json()
    if CACHE.exists():
        # A reading beats a remembered failure whatever the source: the seed carries the first
        # pass's 403s, and `setdefault` alone let those errors outlive the successful re-reads
        # already in CACHE, which then caused a pointless (and rate-limiting) refetch that
        # replaced good readings with fresh 403s. Non-error entries therefore overwrite.
        for k, v in json.loads(CACHE.read_text(encoding="utf-8")).items():
            if "error" not in v or k not in cache:
                cache[k] = v
    known = len(cache)
    todo = [r for r in sorted(cache) if (r in only or not only) and ("error" in cache[r])]
    if force:
        todo = sorted(cache)
    print("%d repos known, %d to fetch" % (known, len(todo)))
    for name in todo:
        try:
            d = get("https://api.github.com/repos/bonitasoft/%s" % name)
            br = d["default_branch"]
            time.sleep(0.6)
            t = get("https://api.github.com/repos/bonitasoft/%s/git/trees/%s?recursive=1"
                    % (name, br))
            paths = [x["path"] for x in t.get("tree", [])]
            cache[name] = {"branch": br, "files": len(paths),
                           "artefacts": [p for p in paths if ARTEFACT.search(p)],
                           "readme": [p for p in paths if DOCFILE.search(p)]}
            print("  OK   %-32s branch=%-6s files=%5d artefacts=%3d"
                  % (name, br, len(paths), len(cache[name]["artefacts"])))
        except Exception as exc:  # noqa: BLE001
            if "files" in cache.get(name, {}):
                # The API refused a later retry (403 rate limit). The last successful reading is
                # still the truth about that tree, so it is kept rather than downgraded to BLOCKED.
                print("  KEEP %-32s %s (earlier reading kept)" % (name, repr(exc)[:60]))
            else:
                cache[name] = {"error": repr(exc)[:90]}
                print("  ERR  %-32s %s" % (name, cache[name]["error"]))
        time.sleep(1.1)
    CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=1), encoding="utf-8")
    bad = [k for k, v in cache.items() if "error" in v]
    art = sum(len(v.get("artefacts", [])) for v in cache.values())
    print("cached %d repos | unreachable %d | process files %d" % (len(cache), len(bad), art))
    print("unreachable:", bad)
    print("written", CACHE)


if __name__ == "__main__":
    main()
