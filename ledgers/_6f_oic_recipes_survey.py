#!/usr/bin/env python3
"""Crawl the six OCI Process Automation recipe books (docs surface, part 2).

The recipes index (recipes.html) links six recipes; each link resolves through
oracle.com/pls/topic/lookup to a small docs book under .../process-automation/<slug>/.
This script enumerates each book's toc.htm (anchors stripped) and fetches every topic.
"""
import json
import pathlib
import re
import time
import urllib.parse
import urllib.request

ELI = pathlib.Path(__file__).resolve().parents[1]
OUT = ELI / "ledgers" / "_6f_docs"
PAGES = OUT / "pages"
PAGES.mkdir(parents=True, exist_ok=True)
BASE = "https://docs.oracle.com/en/cloud/paas/process-automation/"
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128 Safari/537.36"

resolve = json.loads((OUT / "recipe_resolve.json").read_text(encoding="utf-8"))
slugs = {}
for name, info in resolve.items():
    frag = urllib.parse.urlparse(info["final"])
    parts = [p for p in frag.path.split("/") if p]
    slugs[name] = {"book": parts[-2], "target": parts[-1], "anchor": frag.fragment,
                   "entry": info["link"]}

items = []
for name, s in slugs.items():
    items.append((name, BASE + s["book"] + "/index.html", "recipe-book-landing"))
    toc_path = OUT / ("recipe_%s.toc.htm" % s["book"])
    links = set([s["target"]])
    if toc_path.exists():
        t = toc_path.read_text(encoding="utf-8", errors="replace")
        for m in re.finditer(r'href="([^"?]+\.html?)(?:#[^"]*)?"', t):
            l = m.group(1)
            if not l.startswith("http") and not l.startswith("/"):
                links.add(l)
    for l in sorted(links):
        items.append((name, BASE + s["book"] + "/" + l, "recipe-topic"))

print("recipe items:", len(items), flush=True)

KW = ["agent", "Agent", "AI ", "AI-", "LLM", "GenAI", "MCP", "copilot", "Copilot",
      "Artificial Intelligence", "Document Understanding", "document understanding",
      "intelligent", "Intelligent", "machine learning", "Machine Learning",
      "generative", "Generative", "OpenAI", "Anthropic", "prompt", "Prompt"]
BPMN_TERMS = ["BPMN", "bpmn", "process diagram", "gateway", "Gateway", "lane", "Lane",
              "swimlane", "sequence flow", "subprocess", "sub-process", "event", "Event",
              "boundary", "decision model", "process designer", "Process Designer"]


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                              "Accept": "text/html,application/xhtml+xml"})
    with urllib.request.urlopen(req, timeout=45) as r:
        return r.read().decode("utf-8", "replace")


survey = []
for i, (name, url, kind) in enumerate(items, 1):
    slug = urllib.parse.urlparse(url).path.replace("/en/cloud/paas/", "").replace("/", "__")
    dest = PAGES / slug
    try:
        if dest.exists():
            html = dest.read_text(encoding="utf-8", errors="replace")
        else:
            html = fetch(url)
            dest.write_text(html, encoding="utf-8")
            time.sleep(1.0)
    except Exception as exc:                                   # noqa: BLE001
        survey.append({"i": i, "url": url, "kind": kind, "recipe": name, "status": "error",
                       "error": f"{type(exc).__name__}: {exc}"})
        print(f"{i} ERROR {url} {exc}", flush=True)
        time.sleep(1.0)
        continue
    m = re.search(r"<title>(.*?)</title>", html, re.S)
    title = " ".join(re.sub("<[^>]+>", " ", m.group(1)).split()) if m else ""
    body = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.S | re.I)
    text = " ".join(re.sub("<[^>]+>", " ", body).split())
    imgs = []
    for m in re.finditer(r"<img\b[^>]*>", html, re.I):
        tag = m.group(0)
        src = re.search(r'src="([^"]+)"', tag)
        alt = re.search(r'alt="([^"]*)"', tag)
        if src:
            imgs.append({"src": src.group(1), "alt": alt.group(1) if alt else ""})
    survey.append({"i": i, "url": url, "kind": kind, "recipe": name, "status": "ok",
                   "title": title, "text_len": len(text),
                   "kw": {k: text.count(k) for k in KW if text.count(k)},
                   "bpmn": {k: text.count(k) for k in BPMN_TERMS if text.count(k)},
                   "imgs": imgs, "text_head": text[:300],
                   "text_ai": [text[max(0, mm.start() - 250):mm.end() + 250]
                               for k in ("AI ", "Document Understanding", "intelligent",
                                         "Intelligent", "agent", "Agent")
                               for mm in list(re.finditer(re.escape(k), text))[:2]][:6]})
    print(f"{i}/{len(items)} {kind} {title[:60]}", flush=True)

(OUT / "survey_recipes.json").write_text(json.dumps(survey, indent=1, ensure_ascii=False),
                                         encoding="utf-8")
print("done recipe items:", len(survey), flush=True)
