# -*- coding: utf-8 -*-
"""Compact digest of the pages the cib-seven census has to judge by hand.

Prints, for every page in scan.json that has (a) a strong AI/LLM/agent keyword in
its visible text, or (b) a <pre> block naming BPMN/connector vocabulary, or
(c) a downloadable .bpmn/.dmn/.cmmn file:
    n  url  | len images pre files
    AI hits: kw @ ctx
    PRE: snippet

usage: python ledgers/_cib_digest.py [--only docs|mkt] [--kw]
"""
import io, json, os, re, sys

RAW = 'ledgers/cib-seven.raw'
NAV = 'ledgers/cib.raw/nav_latest.txt'
DOCS = 'https://docs.cibseven.org'
STRONG = re.compile(r'(?<![A-Za-z])(AI|A\.I\.|GPT|LLM|LLMs|OpenAI|Anthropic|Claude|LangChain|MCP|agent|agents|agentic|KI|künstliche|Artificial Intelligence|Mistral|Ollama|Bedrock|RAG|chatbot|copilot|robot\w*|knowledge base|embedding|vector store|prompt)(?![A-Za-z])', re.I)


def main():
    want = sys.argv[1] if len(sys.argv) > 1 else ''
    scan = json.load(io.open(os.path.join(RAW, 'scan.json'), encoding='utf-8'))
    docs = [DOCS + l.strip() for l in io.open(NAV, encoding='utf-8') if l.strip()]
    mkt = sorted(json.load(io.open(os.path.join(RAW, 'mkt_pages.json'), encoding='utf-8')))
    order = docs + mkt
    for n, u in enumerate(order, 1):
        v = scan.get(u)
        if not v or v.get('error'):
            continue
        if want == 'docs' and u not in docs:
            continue
        if want == 'mkt' and u in docs:
            continue
        txt = v.get('text') or ''
        hits = []
        for m in STRONG.finditer(txt):
            hits.append((m.group(0), re.sub(r'\s+', ' ', txt[max(0, m.start() - 70):m.end() + 70])))
        pre = v.get('pre') or []
        files = v.get('files') or []
        if not hits and not pre and not files:
            continue
        print('%d %s' % (n, u))
        print('   len %d imgs %d pre %d files %s viewer %s' % (v.get('len', 0), len(v.get('imgs') or []), len(pre), files, v.get('viewer')))
        seen = set()
        for kw, ctx in hits[:8]:
            k = ctx[:40]
            if k in seen:
                continue
            seen.add(k)
            print('   AI[%s] %s' % (kw, ctx[:200]))
        for p in pre[:3]:
            print('   PRE: %s' % p[:260])
        print()


if __name__ == '__main__':
    main()
