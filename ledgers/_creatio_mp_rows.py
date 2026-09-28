#!/usr/bin/env python3
"""Judge the Creatio Marketplace population (524 catalogue items + 13 blog articles) into rows.

Population: the catalogue's own JSON endpoint POST /search/ai with ai_filter null reports
`numFound: 524` - the exact, unfiltered total (see ledgers/_creatio_mp_crawl.py). Every item's
listing page is server-rendered and was cached. The blog index walks `?page=N` to exhaustion (13
articles).

The judgement is mechanical, from the cached page (judged_from: marketplace-cache), because 537
listing pages cannot each be opened by eye:
  * no figure in the listing body                 -> E0-no-artefact
  * figures, no process-model language anywhere   -> E1-not-bpmn (the figures are named in the row)
  * figures + process-model language, no AI token -> E2-no-ai-element
  * figures + process-model language + AI token   -> CANDIDATE: its figures are looked at by eye,
                                                     one by one, before a verdict is written
The AI screen runs over the listing body text, every image alt attribute and every image file name.
Note the two false-positive families of this surface, both found while screening: the privacy-policy
boilerplate "The App Developer will process your data" and the marketing phrase "the process of X"
contain the word *process* without naming a process model.

  python ledgers/_creatio_mp_rows.py            # report the candidate set, write nothing
  python ledgers/_creatio_mp_rows.py --write    # append rows for everything but the candidates
"""
import json
import pathlib
import re
import sys

ELI = pathlib.Path(__file__).resolve().parents[1]
OUT = ELI / "ledgers" / "_creatio"
LEDGER = ELI / "ledgers" / "creatio.jsonl"
TODAY = "2026-09-24"

# a process MODEL is claimed by these, not by "process your data", "the process of onboarding", the
# commerce "payment gateways" or the "Business Process Element" compatibility tag (kept separately)
PROC = (r"\bBPMN\b|process designer|business process|business processes|sub-?process|\bgateways?\b"
        r"|process model|process diagram|workflow diagram|process automation|process element")
TAG_BPE = r"Business Process Element"
# the listing's own feature tags: "Business Process Element" means the app adds an element to the
# process designer, "AI Workflow" means the app works with Creatio's AI Workflow feature. Either can
# introduce a process artefact the body text never mentions, so both put an item in the eye pass.
TAG_EYES = r"Business Process Element|AI Workflow"
EYES = re.compile("(?:" + PROC + "|" + TAG_EYES + ")", re.I)
# the AI screen, same family of tokens as the Academy pass, minus the chrome-only ones
AI = (r"\bAI\b|AI-|AI,|AI\.|AI'|\bA\.I\.|\bLLM\b|GenAI|MCP|copilot|Copilot|Artificial Intelligence"
      r"|machine learning|Machine Learning|generative|OpenAI|Anthropic|\bGPT|Claude|Gemini|\bRAG\b"
      r"|neural|sentiment|Creatio AI|Creatio\.ai|Sub-agent|sub-agent|AI-powered|AI-generated"
      r"|vector search|predictive|prediction|AI Agent|AI agent|AI Agents")
# This surface's own vocabulary needs care: in Creatio an "agent" is normally a *human* CRM user
# ("agent workspace", "agent productivity", "Agent desktop"), so the bare words agent/agents and the
# softer tokens (summariz*, embedding, assistant) are screened but printed with their context for the
# eye rather than treated as decisive on their own.
SOFT = r"agents?|assistant|summariz|summaris|embedding"
# the site chrome carries some of these on every page, so the screen must not read the nav
CHROME_CUT = re.compile(r"^(.*?)\s*(?=Bestsellers|Certified|Install Overview|Product overview)", re.S)


def body(p):
    """The listing's own content, with the site chrome (nav, facet lists) cut off if recognisable."""
    t = p.get("text") or ""
    m = re.search(r"(Install|Overview|Product description|Description)", t)
    return t[m.start():] if m else t


def figs(p):
    return p.get("imgs") or []


def hay_of(p):
    return " ".join([body(p)] + [(i.get("alt") or "") for i in figs(p)]
                    + [i["src"].split("/")[-1] for i in figs(p)])


def quote(p, rx, maxw=25):
    """A verbatim sentence of the listing containing `rx`, else the first sentence of its body."""
    t = re.sub(r"\s+", " ", body(p))
    sents = re.split(r"(?<=[.!?])\s", t)
    for s in sents:
        if re.search(rx, s, re.I) and len(s.split()) >= 4:
            w = s.split()
            return " ".join(w[:maxw]) + (" ..." if len(w) > maxw else "")
    w = t.split()
    return " ".join(w[:maxw]) + (" ..." if len(w) > maxw else "")


def names(p, k=6):
    ns = [i["src"].split("/")[-1].replace("%2520", " ").replace("%20", " ") for i in figs(p)]
    return "; ".join(ns[:k]) + (" ..." if len(ns) > k else "")


def main():
    items = json.loads((OUT / "mp_items.json").read_text(encoding="utf-8"))
    pages = json.loads((OUT / "mp_pages.json").read_text(encoding="utf-8"))
    blog = json.loads((OUT / "mp_blog_index.json").read_text(encoding="utf-8"))
    blogpages = json.loads((OUT / "mp_blog_pages.json").read_text(encoding="utf-8")) \
        if (OUT / "mp_blog_pages.json").exists() else {}
    census = [("app", i["link"], i) for i in items["items"]] + \
             [("blog", b, None) for b in blog["articles"]]
    print("population: %d items (%d apps + %d blog articles)" % (
        len(census), len(items["items"]), len(blog["articles"])))

    cand, cls = [], {}
    for kind, link, it in census:
        p = (pages if kind == "app" else blogpages).get(link)
        if not p or p.get("status") != "ok":
            cls["blocked"] = cls.get("blocked", 0) + 1
            print("  NO CACHED PAGE:", link)
            continue
        hay = hay_of(p)
        pr = bool(re.search(PROC, hay, re.I))
        ai = [k for k in re.findall(AI, hay, re.I)]
        soft = [k for k in re.findall(SOFT, hay, re.I)]
        key = ("proc" if pr else "noproc") + ("_ai" if ai else "_noai")
        cls[key] = cls.get(key, 0) + 1
        cls["soft_" + ("y" if soft else "n")] = cls.get("soft_" + ("y" if soft else "n"), 0) + 1
        if not figs(p):
            cls["E0"] = cls.get("E0", 0) + 1
        elif pr and (ai or soft):
            cand.append((link, p["title"], len(figs(p)), sorted(set(ai))[:5], sorted(set(soft))[:5]))
    print("classes:", cls)
    print("\ncandidates (process-model language AND an AI-ish token): %d" % len(cand))
    for l, t, k, a, s in cand:
        print("   %-70s imgs=%-3d hard=%s soft=%s" % (l[:70], k, a, s))
    # contexts of the decisive tokens, for the eye: strong tokens first, then the soft ones
    if "--context" in sys.argv:
        for l, t, k, a, s in cand:
            p = (pages if l.startswith("/app/") else blogpages)[l]
            print("\n---", l)
            for rx in (AI, SOFT):
                for m in re.finditer(rx, body(p), re.I):
                    c = re.sub(r"\s+", " ", body(p)[max(0, m.start() - 70):m.start() + 70])
                    print("    %-8s ... %s" % (m.group(0), c))
                    break
    if "--write" in sys.argv:
        print("(write path is added after the visual pass over the candidates)")
    return cand


if __name__ == "__main__":
    main()
