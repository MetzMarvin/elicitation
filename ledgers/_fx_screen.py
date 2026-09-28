"""Screen every fetched flowx-ai page offline.

Reads ledgers/flowx-ai.raw/pages/*.md and writes ledgers/flowx-ai.raw/screen.json: one record per page
with the figure list (standalone images vs inline icons), the AI sentences, the process/BPMN
sentences, the word count, the docs version and the surface. Nothing here decides a verdict - it only
says which pages a human eye has to look at.

Two departures from the processmaker screen, both because this source is Mintlify rather than
Document360:

  * every page's markdown is the author's own (the `.md` twin), so there is no HTML slicing and no
    nav chrome to strip - the AI keyword census is over article text only;
  * the AI lexicon is wider, because FlowX.AI's own vocabulary for its AI features is `agent`,
    `agentic`, `node types` and the pre-built agent names (AI Analyst, AI Architect, AI Designer, AI
    Developer, AI Assistant), and its pre-5.9 pages call the same generation of features `ai-nodes`
    and `ai-core`. A narrow lexicon would have under-collected exactly the pages the source exists
    for.
"""
import json, os, re

ELI = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ELI, "flowx-ai.raw")
PAGES = os.path.join(RAW, "pages")
# While the per-page fetch is still running, the 373 v5.9 pages and the 120 release-note pages are
# already on disk from the site's own `llms-full.txt` bundle (see the ledger header). The screen reads
# the per-page twin when it has one and falls back to the bundle copy, so screening never waits on the
# fetch. The two are the same published markdown.
PAGES_FALLBACK = os.path.join(RAW, "pages_llmsfull")
OUT = os.path.join(RAW, "screen.json")

AI = re.compile(r"\b(ai|a\.i\.|llm|gen ai|generative ai|generative|gpt|openai|anthropic|claude|"
                r"gemini|watsonx|langchain|langflow|mcp|agent|agents|agentic|prompt|prompts|"
                r"embedding|embeddings|vector|rag|retrieval|machine learning|ml|"
                r"copilot|chatbot|chat interface|natural language|vision|"
                r"intelligent|intelligence|semantic|classification|classifier|extract|"
                r"speech.to.text|ocr|summaris|summariz|recommendation)\b", re.I)
PROC = re.compile(r"\b(bpmn|process model|process definition|process diagram|workflow|pool|lane|"
                  r"swimlane|gateway|service task|user task|sub-?process|sequence flow|"
                  r"designer|node|nodes|boundary event|start event|end event|"
                  r"intermediate event|message event|timer event|token)\b", re.I)
FIGLINE = re.compile(r"^\s*!\[[^\]]*\]\((https?://.+?)\)\s*$")
# Mintlify index/boilerplate that is not the page's own prose.
DROP = re.compile(r"llms\.txt|appendix\.mdx|copy page|was this page helpful", re.I)


def strip_front(t):
    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    fm = {}
    if m:
        for ln in m.group(1).splitlines():
            if ":" in ln:
                k, v = ln.split(":", 1)
                fm[k.strip()] = v.strip().strip('"')
        t = t[m.end():]
    return fm, t


def sentences(t):
    t = re.sub(r"!\[[^\]]*\]\([^\)]*\)", " ", t)          # drop image markup
    t = re.sub(r"\[([^\]]*)\]\([^\)]*\)", r"\1", t)        # links -> their visible text
    t = re.sub(r"<[^>]+>", " ", t)                         # Mintlify Card/Tooltip components
    t = re.sub(r"[`*>#|]", " ", t)
    t = re.sub(r"\s+", " ", t)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", t) if s.strip()]


def version_of(u):
    m = re.match(r"https://docs\.flowx\.ai/([^/]+)/", u)
    return m.group(1) if m else "root"


def surface_of(u):
    if "/_llms/" in u:
        return "llms-index"
    if version_of(u) == "release-notes":
        return "release-notes"
    return version_of(u)


def main():
    pop = json.load(open(os.path.join(RAW, "population.json")))
    recs, missing = [], []
    for u in pop:
        slug = re.sub(r"^https://docs\.flowx\.ai", "", u).strip("/").replace("/", "__") or "root"
        f = os.path.join(PAGES, slug + ".md")
        src = "twin"
        if not os.path.exists(f):
            f = os.path.join(PAGES_FALLBACK, slug + ".md")
            src = "llms-full"
        if not os.path.exists(f):
            missing.append(u)
            continue
        body = open(f, encoding="utf-8").read()
        fm, t = strip_front(body)
        if not fm.get("title"):
            m = re.search(r"(?m)^#\s+(.+?)\s*$", t)
            if m:
                fm["title"] = m.group(1).strip()
        figs = [m.group(1) for ln in t.splitlines() if (m := FIGLINE.match(ln))]
        inline = len(re.findall(r"!\[[^\]]*\]\(", t)) - len(figs)
        ss = sentences(t)
        ai_s, proc_s = [], []
        for s in ss:
            if DROP.search(s):
                continue
            if AI.search(s) and 8 <= len(s) <= 300:
                ai_s.append(s)
            if PROC.search(s) and 8 <= len(s) <= 300:
                proc_s.append(s)
        recs.append({
            "url": u, "slug": fm.get("slug", slug), "title": fm.get("title", ""),
            "version": version_of(u), "surface": surface_of(u),
            "figures": figs, "n_figures": len(figs), "n_inline_images": inline,
            "words": len(re.findall(r"\w+", t)),
            "ai": bool(ai_s), "proc": bool(proc_s),
            "ai_sentences": ai_s, "proc_sentences": proc_s[:6],
            "bytes": len(body), "file": slug + ".md", "src": src,
        })
    json.dump(recs, open(OUT, "w", encoding="utf-8"), indent=0)
    import collections
    print("screened", len(recs), "missing", len(missing))
    if missing:
        print("MISSING:", missing[:10])
    print("with figures:", sum(1 for r in recs if r["n_figures"]))
    print("ai pages:", sum(1 for r in recs if r["ai"]))
    print("ai AND figures:", sum(1 for r in recs if r["ai"] and r["n_figures"]))
    print("proc AND figures:", sum(1 for r in recs if r["proc"] and r["n_figures"]))
    print(collections.Counter(r["surface"] for r in recs))


if __name__ == "__main__":
    main()
