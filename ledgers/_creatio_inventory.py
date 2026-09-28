#!/usr/bin/env python3
"""Build the page inventory for the Creatio census from the cached HTML itself.

The crawler writes its survey only when it finishes, and the v10 tree is larger than one run's cap,
but every page it fetched is on disk in ledgers/_creatio/pages/. This script reads that cache:
it recovers each page's exact URL from its og:url tag, writes survey_cache.json in the crawler's
schema, and checks whether the in-scope subtrees are complete - every in-scope /guides/ link found
anywhere in the cached corpus must itself be a cached page. That check is what licenses treating the
in-scope population as closed while the out-of-scope crawl is still running.

  python ledgers/_creatio_inventory.py
"""
import json
import pathlib
import re
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:                                                 # noqa: BLE001
    pass

ELI = pathlib.Path(__file__).resolve().parents[1]
OUT = ELI / "ledgers" / "_creatio"
PAGES = OUT / "pages"
HOST = "https://academy.creatio.com"
SCOPE = ("/guides/no-code-customization/", "/guides/ai-studio/", "/guides/ai-development/")
KW = ["agent", "Agent", "AI ", "AI-", "LLM", "GenAI", "MCP", "copilot", "Copilot",
      "Artificial Intelligence", "machine learning", "Machine Learning", "generative",
      "Generative", "OpenAI", "Anthropic", "prompt", "Prompt", "intelligent", "Intelligent",
      "Creatio.ai", "Creatio AI"]


def slug(path):
    return re.sub(r"[^A-Za-z0-9._-]", "_", path.strip("/"))[:150]


survey, urls = [], set()
for f in sorted(PAGES.glob("*.html")):
    html = f.read_text(encoding="utf-8", errors="replace")
    m = re.search(r'og:url["\']?\s+content=["\']?([^"\'\s>]+)', html)
    url = (m.group(1) if m else "").split("?")[0].rstrip("/")
    if not url.startswith("http"):
        url = HOST + "/" + f.name[:-5]
    path = url.replace(HOST, "")
    t = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.S | re.I)
    text = " ".join(re.sub("<[^>]+>", " ", t).split())
    tm = re.search(r"<title[^>]*>(.*?)</title>", html, re.S | re.I)
    title = " ".join(re.sub("<[^>]+>", " ", tm.group(1)).split()) if tm else ""
    imgs = []
    for mm in re.finditer(r"<img\b[^>]*>", html, re.I):
        tag = mm.group(0)
        src = re.search(r'src=["\']?([^"\'\s>]+)', tag)
        alt = re.search(r'alt=["\']([^"\']*)', tag)
        if src:
            imgs.append({"src": src.group(1), "alt": alt.group(1) if alt else ""})
    survey.append({"url": url, "path": path, "status": "ok", "title": title,
                   "text_len": len(text), "text": text[:6000],
                   "kw": {k: text.count(k) for k in KW if text.count(k)}, "imgs": imgs})
    urls.add(path)

(OUT / "survey_cache.json").write_text(json.dumps(survey, indent=1, ensure_ascii=False),
                                       encoding="utf-8")
print(f"cached pages inventoried: {len(survey)}")

# completeness of the in-scope subtrees: every in-scope link in the corpus must be a cached page
SKIP = re.compile(r"(\.(?:png|jpg|jpeg|svg|css|js|pdf|zip)$|/e-learning|/training|/certification"
                  r"|/documents\?|/user/login|mailto:|tel:|^#|linkedin|twitter|facebook|youtube|"
                  r"/8\.\d|/9\.\d|/7\.\d|/8\.3|marketplace\.creatio|community\.creatio|"
                  r"creatio\.com/page|profile\.creatio\.com|/[0-9]+\.[0-9]+/)", re.I)
missing = set()
for f in PAGES.glob("*.html"):
    html = f.read_text(encoding="utf-8", errors="replace")
    for m in re.finditer(r'href=["\']?([^"\'\s>]+)', html):
        h = m.group(1).replace(HOST, "")
        if not h.startswith("/guides/"):
            continue
        h = h.split("#")[0].rstrip("/")
        if not any(h.startswith(p.rstrip("/")) for p in SCOPE):
            continue
        if SKIP.search(h):
            continue
        if h and slug(h) + ".html" not in {p.name for p in PAGES.glob("*.html")}:
            missing.add(h)
in_scope_cached = [s for s in survey if any(s["path"].startswith(p) for p in SCOPE)]
print(f"in-scope pages cached: {len(in_scope_cached)}")
print(f"in-scope links in the corpus with no cached page: {len(missing)}")
for h in sorted(missing)[:15]:
    print("   MISSING", h)
