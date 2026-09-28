#!/usr/bin/env python3
"""Retry the repo enumeration for the repos the first pass could not list (elicitation-6f).

The first pass (ledgers/_bonita_repos.py enumerate) hit the unauthenticated GitHub API rate
limit on 22 of the 64 linked repositories and 404 on 11 `.git`-suffixed URL variants of repos
that are already in the population under their plain name. This retries only the repos that
failed for a rate reason, merges what resolves back into ledgers/_bonita/repos.json, and leaves
the rest as ERR so the ledger can carry BLOCKED rows for them.

  python ledgers/_bonita_repos_retry.py
"""
import json
import pathlib
import sys
import time

ELI = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ELI / "ledgers"))
import _bonita_repos as R  # noqa: E402

REPOS = ELI / "ledgers" / "_bonita" / "repos.json"


def main():
    d = json.loads(REPOS.read_text(encoding="utf-8"))
    lr = d["linked_repos"]
    todo = [r for r, v in sorted(lr.items())
            if v.get("status", "ok") != "ok" and not r.endswith(".git")
            and "404" not in v["status"]]
    print("retrying %d repos" % len(todo))
    for repo in todo:
        paths, branch, last = None, None, None
        for br in ("main", "master"):
            try:
                paths = R.tree(repo, br)
                branch = br
                break
            except Exception as exc:  # noqa: BLE001
                last = repr(exc)[:80]
            time.sleep(1.0)
        old = lr[repo]
        if paths is None:
            print("  ERR  %-34s %s" % (repo, last))
            lr[repo] = {"pages": old["pages"], "status": "ERR " + last}
            continue
        arts = [p for p in paths if R.ARTEFACT.search(p)]
        docs = [p for p in paths if R.DOCFILE.search(p)]
        lr[repo] = {"pages": old["pages"], "branch": branch, "files": len(paths),
                    "artefacts": arts, "readme": docs}
        raw = "https://raw.githubusercontent.com/bonitasoft/%s/%s/" % (repo, branch)
        for p in docs:
            d["items"].append({"kind": "readme", "repo": repo, "path": p, "url": raw + p,
                               "page": "https://github.com/bonitasoft/%s/blob/%s/%s"
                                       % (repo, branch, p)})
        for p in arts:
            d["items"].append({"kind": "process-file", "repo": repo, "path": p, "url": raw + p,
                               "page": "https://github.com/bonitasoft/%s/blob/%s/%s"
                                       % (repo, branch, p)})
        print("  ok   %-34s files=%4d artefacts=%d %s" % (repo, len(paths), len(arts), arts[:3]))
        time.sleep(1.0)
    seen, items = set(), []
    for it in d["items"]:
        if it["url"] in seen:
            continue
        seen.add(it["url"])
        items.append(it)
    d["items"] = items
    REPOS.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")
    ok = [r for r, v in lr.items() if v.get("status", "ok") == "ok"]
    print("linked repos %d | resolved %d | items %d" % (len(lr), len(ok), len(items)))


if __name__ == "__main__":
    main()
