#!/usr/bin/env python3
"""Enumerate + fetch every page of the OCI Process Automation documentation surface.

Read-only GETs, one request per second (shared-rules conduct). Writes the raw HTML into
ledgers/_6f_docs/pages/ and a survey JSON with title, text, images and keyword counts.
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

BOOKS = ["user-process-automation", "admin-process-automation", "rest-api-proca",
         "whats-new-process", "process-licensing"]

# ---- build the item list -------------------------------------------------
items = []          # (url, kind, book)


def add(url, kind, book):
    if url not in {u for u, _, _ in items}:
        items.append((url, kind, book))


for b in BOOKS:
    add(BASE + b + "/index.html", "book-landing", b)
    toc = OUT / (b + ".toc.htm")
    if toc.exists():
        t = toc.read_text(encoding="utf-8", errors="replace")
        links = sorted(set(re.findall(r'href="([^"#?:]+\.html?)"', t)))
        for l in links:
            if l.startswith("http") or l.startswith("/"):
                continue
            add(BASE + b + "/" + l, "topic", b)

add(BASE + "books.html", "landing", "books")
add(BASE + "recipes.html", "recipes", "books")
add(BASE + "training.html", "training", "books")
add("https://docs.oracle.com/en/cloud/paas/application-integration/known-issues/processes-issues.html",
    "known-issues", "books")
add("https://docs.oracle.com/en/accessibility/index.html", "accessibility", "books")

print("items to fetch:", len(items), flush=True)

KW = ["agent", "Agent", "AI ", "AI-", "LLM", "GenAI", "MCP", "copilot", "Copilot",
      "Artificial Intelligence", "Document Understanding", "document understanding",
      "intelligent", "Intelligent", "machine learning", "Machine Learning",
      "generative", "Generative", "OpenAI", "Anthropic", "prompt", "Prompt"]
BPMN_TERMS = ["BPMN", "bpmn", "process diagram", "Process diagram", "gateway", "Gateway",
              "lane", "Lane", "swimlane", "sequence flow", "subprocess", "sub-process",
              "event", "boundary", "decision model", "process designer", "Process Designer"]


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                              "Accept": "text/html,application/xhtml+xml"})
    with urllib.request.urlopen(req, timeout=45) as r:
        raw = r.read()
    return raw.decode("utf-8", "replace")


survey = []
for i, (url, kind, book) in enumerate(items, 1):
    slug = urllib.parse.urlparse(url).path.replace("/en/cloud/paas/", "").replace("/", "__")
    dest = PAGES / slug
    try:
        if dest.exists():
            html = dest.read_text(encoding="utf-8", errors="replace")
        else:
            html = fetch(url)
            dest.write_text(html, encoding="utf-8")
            time.sleep(1.0)
        status = "ok"
    except Exception as exc:                                  # noqa: BLE001
        survey.append({"i": i, "url": url, "kind": kind, "book": book, "status": "error",
                       "error": f"{type(exc).__name__}: {exc}"})
        print(f"{i}/{len(items)} ERROR {url} {exc}", flush=True)
        time.sleep(1.0)
        continue

    title = ""
    m = re.search(r"<title>(.*?)</title>", html, re.S)
    if m:
        title = " ".join(re.sub("<[^>]+>", " ", m.group(1)).split())
    body = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.S | re.I)
    text = " ".join(re.sub("<[^>]+>", " ", body).split())
    imgs = []
    for m in re.finditer(r"<img\b[^>]*>", html, re.I):
        tag = m.group(0)
        src = re.search(r'src="([^"]+)"', tag)
        alt = re.search(r'alt="([^"]*)"', tag)
        w = re.search(r'width="(\d+)"', tag)
        h = re.search(r'height="(\d+)"', tag)
        if src:
            imgs.append({"src": src.group(1), "alt": (alt.group(1) if alt else ""),
                         "w": (int(w.group(1)) if w else None),
                         "h": (int(h.group(1)) if h else None)})
    survey.append({
        "i": i, "url": url, "kind": kind, "book": book, "status": status,
        "title": title, "text_len": len(text),
        "kw": {k: text.count(k) for k in KW if text.count(k)},
        "bpmn": {k: text.count(k) for k in BPMN_TERMS if text.count(k)},
        "imgs": imgs,
        "text_head": text[:400],
        "text_ai": [
            text[max(0, mm.start() - 200):mm.end() + 200]
            for k in ("AI ", "Document Understanding", "agent", "Agent", "LLM", "MCP")
            for mm in list(re.finditer(re.escape(k), text))[:2]
        ][:6],
    })
    if i % 25 == 0:
        print(f"{i}/{len(items)} ...", flush=True)

(OUT / "survey.json").write_text(json.dumps(survey, indent=1, ensure_ascii=False), encoding="utf-8")
print("done. pages:", len(survey), "errors:", sum(1 for s in survey if s["status"] != "ok"), flush=True)
