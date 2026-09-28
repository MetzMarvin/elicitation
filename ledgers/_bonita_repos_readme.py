#!/usr/bin/env python3
"""Fetch any linked repository's README that the first screening pass did not cache.

`_bonita_repogroup.readme_quote` quotes the first substantive line of a repository's README as the
repository row's evidence, and the ledger build must not touch the network. This tops the local
cache (ledgers/_bonita/repos/) up from raw.githubusercontent - not the rate-limited API - for the
repositories the earlier passes never reached (they were listed as unreachable then).

  python ledgers/_bonita_repos_readme.py [--write]
"""
import json
import pathlib
import sys
import time
import urllib.parse
import urllib.request

ELI = pathlib.Path(__file__).resolve().parents[1]
OUT = ELI / "ledgers" / "_bonita"
CACHE = OUT / "repos"
TREES = OUT / "repos_trees.json"


def main():
    write = "--write" in sys.argv
    trees = json.loads(TREES.read_text(encoding="utf-8"))
    have = {p.name for p in CACHE.iterdir()} if CACHE.exists() else set()
    missing = []
    for repo, rec in sorted(trees.items()):
        if "error" in rec:
            continue
        readmes = rec.get("readme") or []
        if not readmes:
            print("  NO-README-PATH %s (tree has %d files)" % (repo, rec.get("files", 0)))
            continue
        names = [repo + "__" + p.replace("/", "~") for p in readmes]
        if not any(n in have for n in names):
            missing.append((repo, readmes[0], names[0]))
    print("%d repositories need a README fetched" % len(missing))
    for repo, path, name in missing:
        url = "https://raw.githubusercontent.com/bonitasoft/%s/%s/%s" % (
            repo, trees[repo]["branch"], "/".join(urllib.parse.quote(s) for s in path.split("/")))
        try:
            with urllib.request.urlopen(urllib.request.Request(
                    url, headers={"User-Agent": "elicitation-census"}), timeout=60) as r:
                body = r.read()
        except Exception as exc:  # noqa: BLE001
            print("  ERR %-32s %s" % (repo, repr(exc)[:70]))
            time.sleep(0.5)
            continue
        print("  OK  %-32s %-24s %d bytes" % (repo, path, len(body)))
        if write:
            (CACHE / name).write_bytes(body)
        time.sleep(0.4)


if __name__ == "__main__":
    main()
