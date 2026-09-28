#!/usr/bin/env python3
"""Canonicalise + finish the linked-repository enumeration (worker elicitation-6f).

Two defects in the first pass (`_bonita_repos.py`):

  1. the same repository is linked both as `X` and as `X.git`, which the first pass recorded as
     two keys - one of them 404ing. They are one item; here they are merged under `X`.
  2. the tree was only requested for branches `main` and `master`. Eleven repositories use a
     different default branch (`dev`, `1.0`, `1.3`, `4.0`), so they were recorded as
     unreachable when in fact the API answers fine. Here the default branch is read from the
     repository endpoint and the tree fetched from it.

Writes ledgers/_bonita/repos.json in place (same schema) and prints the canonical census.

  python ledgers/_bonita_repos_fix.py [--write]
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
UA = {"User-Agent": "elicitation-census", "Accept": "application/vnd.github+json"}
ARTEFACT = re.compile(r"\.bpmn$|\.proc$", re.I)
DOCFILE = re.compile(r"(^|/)README(\.\w+)?$|\.adoc$", re.I)


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=45) as r:
        return json.loads(r.read().decode("utf-8"))


def canon(name):
    return name[:-4] if name.endswith(".git") else name


def main():
    write = "--write" in sys.argv
    old = json.loads(REPOS.read_text(encoding="utf-8"))
    merged = {}
    for name, rec in old["linked_repos"].items():
        c = canon(name)
        e = merged.setdefault(c, {"pages": set(), "status": rec.get("status"),
                                  "branch": rec.get("branch"), "files": rec.get("files"),
                                  "artefacts": rec.get("artefacts", []),
                                  "readme": rec.get("readme", [])})
        e["pages"] |= set(rec["pages"])
        if "status" not in rec:  # a successful variant wins over a failed one
            e["status"] = None
            e["branch"] = rec.get("branch")
            e["files"] = rec.get("files")
            e["artefacts"] = rec.get("artefacts", [])
            e["readme"] = rec.get("readme", [])
    print("linked keys %d -> canonical %d" % (len(old["linked_repos"]), len(merged)))

    retried = []
    for name, e in sorted(merged.items()):
        if e["status"] is None:
            continue
        try:
            d = get("https://api.github.com/repos/bonitasoft/%s" % name)
            br = d["default_branch"]
            time.sleep(0.6)
            t = get("https://api.github.com/repos/bonitasoft/%s/git/trees/%s?recursive=1"
                    % (name, br))
            paths = [x["path"] for x in t.get("tree", [])]
        except Exception as exc:  # noqa: BLE001
            e["status"] = "ERR " + repr(exc)[:70]
            print("  ERR  %-32s %s" % (name, e["status"]))
            time.sleep(1.0)
            continue
        e.update({"status": None, "branch": br, "files": len(paths),
                  "artefacts": [p for p in paths if ARTEFACT.search(p)],
                  "readme": [p for p in paths if DOCFILE.search(p)]})
        retried.append(name)
        print("  OK   %-32s branch=%-6s files=%4d artefacts=%d %s"
              % (name, br, len(paths), len(e["artefacts"]), e["artefacts"][:3]))
        time.sleep(1.0)

    items = []
    for name, e in sorted(merged.items()):
        if e["status"] is not None:
            continue
        raw = "https://raw.githubusercontent.com/bonitasoft/%s/%s/" % (name, e["branch"])
        for p in e["readme"] + e["artefacts"]:
            items.append({"kind": "process-file" if ARTEFACT.search(p) else "readme",
                          "repo": name, "path": p, "url": raw + p,
                          "page": "https://github.com/bonitasoft/%s/blob/%s/%s"
                                  % (name, e["branch"], p)})
    out = {"linked_repos": {k: ({**v, "pages": sorted(v["pages"])} if v["status"] is None
                                else {"pages": sorted(v["pages"]), "status": v["status"]})
                            for k, v in merged.items()},
           "items": items}
    resolved = sum(1 for v in merged.values() if v["status"] is None)
    print("canonical repos %d | resolved %d | unreachable %d | items %d | retried %d"
          % (len(merged), resolved, len(merged) - resolved, len(items), len(retried)))
    print("unreachable:", [k for k, v in sorted(merged.items()) if v["status"] is not None])
    procs = [i for i in items if i["kind"] == "process-file"]
    print("process files (%d):" % len(procs))
    for i in procs:
        print("   %s" % i["page"])
    if write:
        REPOS.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
        print("written", REPOS)


if __name__ == "__main__":
    main()
