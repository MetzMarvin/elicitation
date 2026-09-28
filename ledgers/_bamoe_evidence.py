#!/usr/bin/env python3
"""Verbatim evidence dump for the ibm-bamoe docs half: one block per figure-bearing topic.

For each topic the screen flagged (a diagram-named figure, a bpmn marker, a dotfile, or an AI token
plus figures) this prints the sentences of the page's own content region that carry an AI token and
the ones that carry a process token, so every ledger row can quote the page verbatim instead of
recalling it. Snippets are capped at 25 words, which is the shared rules' quote limit.
"""
import json
import pathlib
import re

ELI = pathlib.Path(__file__).resolve().parents[1]
D = ELI / "ledgers" / "_bamoe"

AI = re.compile(r"\b(ai|a\.i\.|llm|gen\s?ai|generative|gpt-?[\d.]*|chat-?gpt|claude|anthropic|openai|"
                r"azure\s?openai|gemini|vertex|groq|mistral|ollama|cohere|deepseek|hugging\s?face|"
                r"bedrock|watsonx|watson|langflow|mcp|agent|agents|prompt|prompts|copilot|embedding|"
                r"vector|rag|machine learning|ml|model)\b", re.I)
PROC = re.compile(r"\b(bpmn|process diagram|workflow diagram|pool|lane|gateway|service task|user task|"
                  r"sub-?process|sequence flow|modell?er|modeler|canvas)\b", re.I)
TAG = re.compile(r"<[^>]+>")
WS = re.compile(r"\s+")


def text_of(html):
    t = re.sub(r"(?is)<(script|style)\b.*?</\1>", " ", html)
    t = TAG.sub(" ", t)
    t = (t.replace("&nbsp;", " ").replace("&amp;", "&").replace("&lt;", "<")
          .replace("&gt;", ">").replace("&quot;", '"').replace("&#39;", "'"))
    return WS.sub(" ", t).strip()


def sents(t):
    return re.split(r"(?<=[.!?])\s+", t)


def clip(s, n=25):
    return " ".join(s.split()[:n])


def main():
    content = json.loads((D / "content_9.5.x.json").read_text(encoding="utf-8"))
    screen = json.loads((D / "screen.json").read_text(encoding="utf-8"))
    for r in screen:
        figs = r["figures"]
        flagged = bool(r["diagram_named_figures"] or r["bpmn_markers"] or r["dotfiles"]
                       or (r["ai"] and figs))
        if not flagged:
            continue
        html = (content.get(r["href"]) or {}).get("html", "")
        t = text_of(html)
        ai_hits = [clip(s) for s in sents(t) if AI.search(s)][:3]
        pr_hits = [clip(s) for s in sents(t) if PROC.search(s)][:2]
        print("=" * 100)
        print("%s   |  %s  |  parent=%s" % (r["href"], r["label"], r["parent"]))
        print("figs(%d): %s" % (len(figs), " | ".join(f.split('/')[-1] for f in figs)))
        for s in ai_hits:
            print("   AI>  %s" % s)
        for s in pr_hits:
            print("   PR>  %s" % s)


if __name__ == "__main__":
    main()
