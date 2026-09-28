#!/usr/bin/env python3
"""Extract the article region of every fetched Creatio Academy page.

The Academy serves a big chrome (navbar, sidebar nav, footer) on every page, and that chrome
contains the strings "AI " and "Creatio AI" on every single page - scanning the whole rendered
text therefore produces false positives on ~40% of the site. This script keeps only the
<article> element, which is the guide content itself, plus the figures inside it.
"""
import json
import pathlib
import re

ELI = pathlib.Path(__file__).resolve().parents[1]
OUT = ELI / "ledgers" / "_creatio"
PAGES = OUT / "pages"

KW = ["agent", "Agent", "AI ", "AI-", "AI,", "AI.", "LLM", "GenAI", "MCP", "copilot", "Copilot",
      "Artificial Intelligence", "machine learning", "Machine Learning", "generative",
      "Generative", "OpenAI", "Anthropic", "prompt", "Prompt", "intelligent", "Intelligent",
      "Creatio.ai", "Creatio AI", "Call Creatio.ai", "Sub-agent", "sub-agent", "skill", "Skill",
      # widened after the first pass, so the AI screen cannot miss a synonym the vendor prefers
      "GPT", "Claude", "Gemini", "RAG", "embedding", "Embedding", "neural", "Neural",
      "sentiment", "summariz", "summaris", "assistant", "Assistant", "predict", "Predict",
      "auto-generated", "auto-generated", "Azure OpenAI", "vector search", "AI-powered",
      "AI-generated", "smart service", "Smart"]
BPMN_TERMS = ["BPMN", "bpmn", "gateway", "Gateway", "exclusive OR", "parallel AND", "inclusive OR",
              "sub-process", "subprocess", "sequence flow", "lane", "start event", "end event",
              "intermediate event", "boundary event", "process designer", "conditional flow",
              "default flow", "BPMN diagram"]


def article_of(html):
    m = re.search(r"<article\b.*?</article>", html, re.S | re.I)
    return m.group(0) if m else ""


def to_text(html):
    h = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", html, flags=re.S | re.I)
    return " ".join(re.sub("<[^>]+>", " ", h).split())


out = {}
for f in sorted(PAGES.glob("*.html")):
    html = f.read_text(encoding="utf-8", errors="replace")
    art = article_of(html)
    text = to_text(art) if art else ""
    # some pages put only the body in <article>; keep the <h1> if it fell outside
    m = re.search(r"<h1[^>]*>(.*?)</h1>", html, re.S | re.I)
    h1 = to_text(m.group(1)).strip() if m else ""
    if h1 and h1 not in text[:200]:
        text = (h1 + " " + text).strip()
    imgs = []
    for m in re.finditer(r"<img\b[^>]*>", art or html, re.I):
        tag = m.group(0)
        src = re.search(r'src=["\']?([^"\'\s>]+)', tag)
        alt = re.search(r'alt=["\']([^"\']*)', tag)
        if not src:
            continue
        # the text window around the figure: Academy captions are "Fig. N. ..." right after the
        # image, and the paragraph before it usually names what is shown
        before = to_text((art or html)[max(0, m.start() - 1600):m.start()])[-380:]
        after = to_text((art or html)[m.end():m.end() + 1600])[:380]
        imgs.append({"src": src.group(1), "alt": alt.group(1) if alt else "",
                     "text_before": before, "text_after": after})
    # The Academy repeats a breadcrumb trail inside <article> ("BPM tools Process elements
    # reference Events ... Version: 10 On this page <title>"), which puts the words "AI tools
    # Creatio.ai" into the article text of every page under the ai-tools subtree. Strip it, so
    # the keyword counts reflect the guide content and not the navigation trail.
    m = re.match(r"^.{0,400}?Version:\s*[\d.]+\s*On this page\s*", text)
    if m:
        text = text[m.end():].strip()
    out[f.name] = {
        "file": f.name, "has_article": bool(art), "h1": h1, "text_len": len(text),
        "text": text[:8000],
        "kw": {k: text.count(k) for k in KW if text.count(k)},
        "bpmn": {k: text.count(k) for k in BPMN_TERMS if text.count(k)},
        "imgs": imgs,
    }

(OUT / "articles.json").write_text(json.dumps(out, indent=1, ensure_ascii=False), encoding="utf-8")
n_art = sum(1 for v in out.values() if v["has_article"])
n_kw = sum(1 for v in out.values() if v["kw"])
n_kw_img = sum(1 for v in out.values() if v["kw"] and v["imgs"])
print(f"pages: {len(out)}  with <article>: {n_art}  article carries an AI keyword: {n_kw}"
      f"  of those with figures: {n_kw_img}")
print("\nAI-keyword pages in the article region that publish figures:")
for k, v in out.items():
    if v["kw"] and v["imgs"]:
        print(f"  {len(v['imgs']):3d} figs | {v['h1'][:52]:52s} | {sorted(v['kw'])}")
print("\nAI-keyword pages in the article region with NO figure:")
for k, v in out.items():
    if v["kw"] and not v["imgs"]:
        print(f"  {v['h1'][:60]:60s} | {sorted(v['kw'])}")
