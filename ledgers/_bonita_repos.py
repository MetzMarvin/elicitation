#!/usr/bin/env python3
"""Linked example repositories (worker elicitation-6f).

The docs pages link to the connector repositories (github.com/bonitasoft/bonita-connector-ai,
...-ai-agent, ...-mistral-ocr). Those repositories are where the vendor publishes *example
processes that use an AI connector* - the artefact class the assignment asks for. This module
enumerates them honestly: the repo links are extracted from the crawled pages (never guessed),
each repo's default-branch tree is listed through the public GitHub API, and every `.bpmn`,
`.proc` and README file found becomes an item of the ledger population.

  python ledgers/_bonita_repos.py enumerate   # -> ledgers/_bonita/repos.json
"""
import json
import pathlib
import re
import sys
import time
import urllib.request

ELI = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ELI / "ledgers"))
import _bonita_rows as S  # noqa: E402

OUT = ELI / "ledgers" / "_bonita"
REPOS = OUT / "repos.json"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/126 Safari/537.36",
      "Accept": "application/vnd.github+json"}
GH = re.compile(r"https://github\.com/bonitasoft/([A-Za-z0-9._-]+)")
ARTEFACT = re.compile(r"\.bpmn$|\.proc$", re.I)
DOCFILE = re.compile(r"(^|/)README(\.\w+)?$|\.adoc$", re.I)


def linked_repos():
    found = {}
    for url, rec in S.records():
        h = S.html_of(rec)
        for m in GH.finditer(h):
            name = m.group(1)
            if name in ("bonita-doc", "bonita-documentation-site"):
                continue
            found.setdefault(name, set()).add(url)
    return found


def tree(repo, branch):
    u = "https://api.github.com/repos/bonitasoft/%s/git/trees/%s?recursive=1" % (repo, branch)
    d = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=UA),
                                          timeout=45).read().decode())
    return [t["path"] for t in d.get("tree", [])]


def enumerate_repos():
    found = linked_repos()
    out = {"linked_repos": {}, "items": []}
    for repo, pages in sorted(found.items()):
        paths, branch = None, None
        for br in ("main", "master"):
            try:
                paths = tree(repo, br)
                branch = br
                break
            except Exception as exc:  # noqa: BLE001
                last = repr(exc)[:70]
        if paths is None:
            print("  ERR %s %s" % (repo, last))
            out["linked_repos"][repo] = {"pages": sorted(pages), "status": "ERR " + last}
            continue
        arts = [p for p in paths if ARTEFACT.search(p)]
        docs = [p for p in paths if DOCFILE.search(p)]
        out["linked_repos"][repo] = {"pages": sorted(pages), "branch": branch,
                                     "files": len(paths), "artefacts": arts, "readme": docs}
        print("%-32s files=%4d artefacts=%d %s" % (repo, len(paths), len(arts), arts[:4]))
        raw = "https://raw.githubusercontent.com/bonitasoft/%s/%s/" % (repo, branch)
        for p in docs:
            out["items"].append({"kind": "readme", "repo": repo, "path": p, "url": raw + p,
                                 "page": "https://github.com/bonitasoft/%s/blob/%s/%s"
                                         % (repo, branch, p)})
        for p in arts:
            out["items"].append({"kind": "process-file", "repo": repo, "path": p,
                                 "url": raw + p,
                                 "page": "https://github.com/bonitasoft/%s/blob/%s/%s"
                                         % (repo, branch, p)})
        time.sleep(0.5)
    REPOS.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print("linked repos: %d | items: %d" % (len(out["linked_repos"]), len(out["items"])))
    for it in out["items"]:
        print("   %-13s %s" % (it["kind"], it["url"].split("/main/")[-1]))


if __name__ == "__main__":
    if sys.argv[1] == "enumerate":
        enumerate_repos()
