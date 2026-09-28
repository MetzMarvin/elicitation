#!/usr/bin/env python3
"""Fetch and screen the documentation files of the linked repositories (elicitation-6f).

The repo group of the population is enumerated as one row per repository plus one row per
process file (ledgers/_bonita_repos.py). This downloads every documentation file that
enumeration found and screens each one for the markers that would make the repo publish a
process artefact of its own:

  * an embedded BPMN/mermaid/PlantUML diagram of a process,
  * an image whose name or alt text names a process diagram,
  * a `.bpmn`/`.proc` file in the repo (already enumerated as its own item).

  python ledgers/_bonita_repos_screen.py fetch     # -> ledgers/_bonita/repos/*.md
  python ledgers/_bonita_repos_screen.py screen    # marker table over what was fetched
"""
import json
import pathlib
import re
import sys
import time
import urllib.request

ELI = pathlib.Path(__file__).resolve().parents[1]
D = ELI / "ledgers" / "_bonita"
CACHE = D / "repos"
REPOS = D / "repos.json"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/126 Safari/537.36"}

MARKERS = [
    ("mermaid", re.compile(r"```mermaid", re.I)),
    ("plantuml", re.compile(r"@startuml|```plantuml", re.I)),
    ("bpmn-code", re.compile(r"```bpmn|<\?xml[^>]*bpmn|bpmn:process", re.I)),
    ("bpmn-word", re.compile(r"\bBPMN\b|\bbpmn\b|\.bpmn\b|\.proc\b", re.I)),
    ("diagram-word", re.compile(r"diagram|flowchart|process model|\bpool\b|\blane\b|\bgateway\b",
                                re.I)),
    ("diagram-image", re.compile(r"!\[[^\]]*\b(diagram|process|flow|bpmn|architecture)\b[^\]]*\]"
                                 r"\([^)]+\)", re.I)),
    ("ai-word", re.compile(r"\bAI\b|\bLLM\b|artificial intelligence|OpenAI|Anthropic|Mistral|"
                           r"Gemini|Cohere|Groq|DeepSeek|Ollama|Hugging", re.I)),
]


def fetch():
    CACHE.mkdir(parents=True, exist_ok=True)
    items = json.loads(REPOS.read_text(encoding="utf-8"))["items"]
    n = 0
    for it in items:
        dest = CACHE / re.sub(r"[^A-Za-z0-9._-]+", "~", it["repo"] + "__" + it["path"])
        n += 1
        if dest.exists():
            continue
        try:
            raw = urllib.request.urlopen(urllib.request.Request(it["url"], headers=UA),
                                         timeout=45).read()
        except Exception as exc:  # noqa: BLE001
            print("ERR %s %s" % (it["url"][:80], repr(exc)[:60]))
            continue
        dest.write_bytes(raw)
        time.sleep(0.8)
    print("fetched %d items into %s" % (len(list(CACHE.glob('*'))), CACHE))


def screen():
    items = json.loads(REPOS.read_text(encoding="utf-8"))["items"]
    by_repo = {}
    for it in items:
        dest = CACHE / re.sub(r"[^A-Za-z0-9._-]+", "~", it["repo"] + "__" + it["path"])
        if not dest.exists():
            continue
        t = dest.read_text(encoding="utf-8", errors="replace")
        hits = [name for name, rx in MARKERS if rx.search(t)]
        by_repo.setdefault(it["repo"], []).append((it["path"], hits, len(t)))
    for repo in sorted(by_repo):
        rows = by_repo[repo]
        hot = [r for r in rows if ("mermaid" in r[1] or "plantuml" in r[1] or "bpmn-code" in r[1]
                                   or "diagram-image" in r[1])]
        flag = "HOT" if hot else ("ai" if any("ai-word" in r[1] for r in rows) else "   ")
        print("%s %-42s docs=%-3d %s" % (flag, repo, len(rows),
              "; ".join("%s[%s]" % (p[-40:], ",".join(h)) for p, h, _ in hot[:3])
              or ("ai in: " + ", ".join(p[-34:] for p, h, _ in rows if "ai-word" in h)[:90])))


if __name__ == "__main__":
    {"fetch": fetch, "screen": screen}[sys.argv[1]]()
