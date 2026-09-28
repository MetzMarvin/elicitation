#!/usr/bin/env python3
"""Fetch and screen every process file found in the linked repositories (worker elicitation-6f).

The repository group is enumerated as one row per repository *plus one row per process file*
found in its tree (the design stated in _bonita_write.ENUMERATION_NOTE). This module fetches each
of those files from raw.githubusercontent (not the rate-limited API), keeps a local copy, and
records the facts a row needs: the file's sha1 (so identical fixtures published under two paths
can be ruled E3-duplicate rather than counted twice), the process/pool names declared in the XML,
and whether the file mentions any AI provider or model.

  python ledgers/_bonita_procfiles.py [--write]
"""
import hashlib
import json
import pathlib
import re
import sys
import time
import urllib.parse
import urllib.request

ELI = pathlib.Path(__file__).resolve().parents[1]
OUT = ELI / "ledgers" / "_bonita"
CACHE = OUT / "repos_trees.json"
STORE = OUT / "repos" / "procfiles"
FACTS = OUT / "procfiles.json"

AI = re.compile(
    r"\b(?:ai|a\.i\.|llm|gpt-?\d*|chat-?gpt|claude|anthropic|openai|azure-?openai|gemini|"
    r"vertex|groq|mistral|ollama|cohere|deepseek|hugging-?face|bedrock|watson|nvidia|"
    r"artificial intelligence|machine learning|prompt|agent)\b", re.I)
# The Bonita `.proc` serialisation uses the `process:` prefix and `<process:MainProcess>`; the BPMN2
# sample fixtures Bonita Studio ships were authored elsewhere and use the OMG `semantic:` prefix
# with a bare `<semantic:process>` (no name) and `<semantic:participant name=...>` pools. Both
# spellings have to be read, or those files look like they declare no process and no pools at all.
PROCESS = re.compile(r"<(?:process:MainProcess|bpmn2?:process|semantic:process|process)\b"
                     r"[^>]*?name=\"([^\"]+)\"")
POOL = re.compile(r"<(?:process:Pool|bpmn2?:participant|semantic:participant)\b"
                  r"[^>]*?name=\"([^\"]+)\"")
TASK = re.compile(r"<(?:process:ServiceTask|process:UserTask|bpmn2?:serviceTask|bpmn2?:userTask|"
                  r"bpmn2?:manualTask|bpmn2?:scriptTask|bpmn2?:task|semantic:serviceTask|"
                  r"semantic:userTask|semantic:manualTask|semantic:scriptTask|semantic:task)\b"
                  r"[^>]*?name=\"([^\"]+)\"")


def artefacts():
    cache = json.loads(CACHE.read_text(encoding="utf-8"))
    out = []
    for repo, rec in sorted(cache.items()):
        if "error" in rec:
            continue
        for p in rec.get("artefacts", []):
            q = "/".join(urllib.parse.quote(seg) for seg in p.split("/"))
            out.append({"repo": repo, "branch": rec["branch"], "path": p,
                        "url": "https://raw.githubusercontent.com/bonitasoft/%s/%s/%s"
                               % (repo, rec["branch"], q),
                        "page": "https://github.com/bonitasoft/%s/blob/%s/%s"
                                % (repo, rec["branch"], urllib.parse.quote(p))})
    return out


def main():
    # Some Studio fixtures declare process names outside cp1252 (the console's encoding); the census
    # must not abort on a print, so unencodable characters are replaced rather than raised.
    sys.stdout.reconfigure(errors="replace")
    write = "--write" in sys.argv
    STORE.mkdir(parents=True, exist_ok=True)
    items = artefacts()
    print("%d process files in the linked repositories" % len(items))
    facts = []
    for it in items:
        name = "%s__%s" % (it["repo"], re.sub(r"[^A-Za-z0-9._-]", "~", it["path"]))
        dest = STORE / name
        if dest.exists():
            body = dest.read_bytes()
        else:
            try:
                with urllib.request.urlopen(
                        urllib.request.Request(it["url"], headers={
                            "User-Agent": "elicitation-census"}), timeout=60) as r:
                    body = r.read()
            except Exception as exc:  # noqa: BLE001
                print("  ERR %s %s" % (it["path"], repr(exc)[:70]))
                facts.append({**it, "error": repr(exc)[:90], "sha1": None})
                time.sleep(0.4)
                continue
            if write:
                dest.write_bytes(body)
            time.sleep(0.4)
        text = body.decode("utf-8", errors="replace")
        sha = hashlib.sha1(body).hexdigest()
        ai = sorted({m.group(0).lower() for m in AI.finditer(text)})
        f = {**it, "sha1": sha, "bytes": len(body), "store": str(dest.relative_to(ELI)),
             "process_names": PROCESS.findall(text)[:3], "pools": POOL.findall(text)[:3],
             "tasks": TASK.findall(text)[:8], "ai_tokens": ai[:14],
             "bpmn": bool(re.search(r"<bpmn2?:|<process:MainProcess|<semantic:definitions", text))}
        facts.append(f)
        print("  %-6s %-28s %s  ai=%s" % ("AI!" if ai else "-", it["repo"],
                                          (f["process_names"] or ["?"])[0][:38], ",".join(ai[:5])))
    if write:
        FACTS.write_text(json.dumps(facts, ensure_ascii=False, indent=1), encoding="utf-8")
        print("written", FACTS)
    ok = [f for f in facts if f.get("sha1")]
    ai = [f for f in ok if f["ai_tokens"]]
    bysha = {}
    for f in ok:
        bysha.setdefault(f["sha1"], []).append(f)
    dups = {s: v for s, v in bysha.items() if len(v) > 1}
    print("files %d | fetched %d | with AI token %d | identical contents %d group(s)"
          % (len(facts), len(ok), len(ai), len(dups)))
    for f in ai:
        print("   AI  %s  %s" % (f["repo"], f["path"]))


if __name__ == "__main__":
    main()
