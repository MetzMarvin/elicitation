#!/usr/bin/env python3
"""Enumerate + fetch the Creatio Academy guide tree (version 10).

Version pinning: the Academy serves version 10 at the un-versioned URLs
(/guides/no-code-customization/...) and older versions under an explicit version segment
(/guides/no-code-customization/8.3/...). This crawler keeps only the un-versioned v10 URLs.

Read-only GETs at ~1 request/second. Writes raw HTML to ledgers/_creatio/pages/ and a survey
JSON with title, text, figure inventory and keyword counts.

  python ledgers/_creatio_crawl.py --probe 20     # size the tree, fetch at most 20 pages
  python ledgers/_creatio_crawl.py --cap 2500     # full crawl
"""
import argparse
import collections
import json
import pathlib
import re
import time
import sys
import urllib.request

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ELI = pathlib.Path(__file__).resolve().parents[1]
OUT = ELI / "ledgers" / "_creatio"
PAGES = OUT / "pages"
PAGES.mkdir(parents=True, exist_ok=True)
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/128 Safari/537.36")
HOST = "https://academy.creatio.com"

SEEDS = [
    "/guides/",
    "/guides/no-code-customization/category/customization-tools",
    "/guides/no-code-customization/category/ai-tools",
    "/guides/no-code-customization/category/bpm-tools",
    "/guides/no-code-customization/category/business-process-setup",
    "/guides/no-code-customization/category/process-elements-reference",
    "/guides/no-code-customization/category/process-examples",
    "/guides/no-code-customization/category/process-element-use-cases",
    "/guides/no-code-customization/category/system-actions",
    "/guides/no-code-customization/category/user-actions",
    "/guides/no-code-customization/category/events",
    "/guides/no-code-customization/category/gateways",
    "/guides/no-code-customization/category/sub-processes",
    "/guides/no-code-customization/category/business-process-flows-and-connecting-objects",
    "/guides/ai-studio/creatio-ai-studio-overview",
    "/guides/ai-development/creatio-ai-toolkit-overview",
    "/guides/no-code-customization/bpm-tools/process-elements-reference/system-actions/call-creatio-ai-element",
]

SKIP = re.compile(r"(\.(?:png|jpg|jpeg|svg|css|js|pdf|zip)$|/e-learning|/training|/certification"
                  r"|/documents\?|/user/login|mailto:|tel:|^#|linkedin|twitter|facebook|youtube|"
                  r"/8\.\d|/9\.\d|/7\.\d|/8\.3|marketplace\.creatio|community\.creatio|"
                  r"creatio\.com/page|profile\.creatio\.com)", re.I)

KW = ["agent", "Agent", "AI ", "AI-", "LLM", "GenAI", "MCP", "copilot", "Copilot",
      "Artificial Intelligence", "machine learning", "Machine Learning", "generative",
      "Generative", "OpenAI", "Anthropic", "prompt", "Prompt", "intelligent", "Intelligent",
      "Creatio.ai", "Creatio AI"]


def fetch(u):
    r = urllib.request.Request(u, headers={"User-Agent": UA, "Accept": "text/html"})
    with urllib.request.urlopen(r, timeout=45) as resp:
        return resp.read().decode("utf-8", "replace")


def links_of(html):
    out = set()
    for m in re.finditer(r'href=["\']?([^"\'\s>]+)', html):
        h = m.group(1)
        if h.startswith("/guides/") or h.startswith(HOST + "/guides/"):
            h = h.replace(HOST, "")
            if not SKIP.search(h):
                out.add(h.split("#")[0].rstrip("/") or "/")
    return out


def slug(u):
    return re.sub(r"[^A-Za-z0-9._-]", "_", u.strip("/"))[:150] + ".html"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--probe", type=int, default=0)
    ap.add_argument("--cap", type=int, default=3000)
    args = ap.parse_args()
    limit = args.probe or args.cap

    queue = collections.deque(SEEDS)
    seen = set()
    survey = []
    fetched = 0
    while queue and fetched < limit:
        path = queue.popleft()
        if path in seen:
            continue
        seen.add(path)
        url = HOST + path
        dest = PAGES / slug(path)
        try:
            if dest.exists():
                html = dest.read_text(encoding="utf-8", errors="replace")
            else:
                html = fetch(url)
                dest.write_text(html, encoding="utf-8")
                fetched += 1
                time.sleep(0.9)
        except Exception as exc:                                   # noqa: BLE001
            survey.append({"url": url, "status": "error", "error": f"{type(exc).__name__}: {exc}"})
            print("ERR", path, exc, flush=True)
            time.sleep(0.9)
            continue

        for l in links_of(html):
            if l not in seen:
                queue.append(l)

        t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.S | re.I)
        text = " ".join(re.sub("<[^>]+>", " ", t).split())
        m = re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I)
        title = " ".join(re.sub("<[^>]+>", " ", m.group(1)).split()) if m else ""
        imgs = []
        for m in re.finditer(r"<img\b[^>]*>", html, re.I):
            tag = m.group(0)
            src = re.search(r'src=["\']?([^"\'\s>]+)', tag)
            alt = re.search(r'alt=["\']([^"\']*)', tag)
            if src:
                imgs.append({"src": src.group(1), "alt": alt.group(1) if alt else ""})
        survey.append({
            "url": url, "path": path, "status": "ok", "title": title, "text_len": len(text),
            "kw": {k: text.count(k) for k in KW if text.count(k)},
            "bpmn": {k: text.count(k) for k in
                     ["BPMN", "bpmn", "gateway", "Gateway", "exclusive OR", "parallel AND",
                      "inclusive OR", "sub-process", "subprocess", "sequence flow", "lane",
                      "start event", "end event", "task", "process designer"] if text.count(k)},
            "imgs": imgs, "text": text[:6000],
        })
        if fetched % 25 == 0:
            print(f"fetched={fetched} queued={len(queue)} seen={len(seen)}", flush=True)

    (OUT / "survey.json").write_text(json.dumps(survey, indent=1, ensure_ascii=False),
                                     encoding="utf-8")
    print(f"pages fetched this run: {fetched}  urls seen: {len(seen)}  queued left: {len(queue)}",
          flush=True)
    print("survey items:", len(survey), flush=True)


if __name__ == "__main__":
    main()
