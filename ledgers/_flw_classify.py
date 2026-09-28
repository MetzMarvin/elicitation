# -*- coding: utf-8 -*-
"""Per-page triage for the Flowable census.

Turns scan.json (+ figscores.json when the OCR pass has finished) into one line
per frontier URL with a proposed disposition and the evidence that supports it,
so the agent only has to read the review classes by hand.

Classes
  DEAD      http != 200                                    -> E0-no-artefact
  NOART     live, no candidate figure, no BPMN snippet      -> E0-no-artefact
  PRE       live, no figure, but a BPMN-looking snippet     -> review
  AI_NOFIG  live, AI text, no figure                        -> E0-no-artefact
  NOAI_FIG  live, figure, no AI keyword anywhere            -> E2-no-ai-element
  AI_FIG    live, AI text, figure                           -> review

usage: python ledgers/_flw_classify.py
writes ledgers/flowable.raw/triage2.tsv (all rows) and prints the class counts
plus a review shortlist for the AI_FIG and PRE classes.
"""
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, 'flowable.raw')
FRONTIER = os.path.join(HERE, 'flowable.frontier.txt')

STRONG = re.compile(
    r'(?<![A-Za-z])(AI|GPT|LLM|OpenAI|Anthropic|Claude|LangChain|MCP|agent\w*|agentic|'
    r'machine learning|embedding|vector store|prompt|chatbot|copilot|robot\w*|RAG|KI|'
    r'künstliche|Artificial Intelligence|Mistral|Ollama|Bedrock|Gemini|Llama|Hugging Face|'
    r'generative|GenAI|A2A|inference|fine-tun\w+|guardrail\w*|hallucinat\w+)(?![A-Za-z])', re.I)
AIPHRASE = re.compile(
    r'(?i)(ai agent|ai[- ]agent task|agent task|ai task|ai service|ai assistant|agentic|'
    r'orchestrator agent|utility agent|document agent|knowledge agent|external agent|'
    r'guardrail agent|evaluator agent|a2a agent|ai orchestration|ai-driven|ai activation|'
    r'ai chat|generative ai|genai|ai model|mcp server|agent element|ai element)')
BPMNW = re.compile(
    r'(?i)\b(bpmn|process model|process|task|gateway|sub-?process|ad-?hoc|lane|pool|'
    r'element|workflow|sequence flow|start event|end event|case model|cmmn|modeler|diagram)\b')
CUT = [' Sign up for updates', '\n Comments \n Platform', '© 20', 'This site is protected by reCAPTCHA',
       'Footer navigation', '\n Imprint', '\n Platform\n Docs']
NAVPRE = re.compile(r'^.{0,400}?Sign Up Now\s*\n', re.S)


def clean(t):
    for c in CUT:
        i = t.find(c)
        if i > 200:
            t = t[:i]
    t = NAVPRE.sub('', t, count=1)
    return t.strip()


def contexts(t, kw_re=STRONG, n=25):
    out, seen = [], set()
    for m in kw_re.finditer(t):
        a, b = max(0, m.start() - 130), min(len(t), m.end() + 180)
        c = re.sub(r'\s+', ' ', t[a:b]).strip()
        k = c[:50]
        if k in seen:
            continue
        seen.add(k)
        out.append(c)
        if len(out) >= n:
            break
    return out


def main():
    urls = [l.strip() for l in open(FRONTIER, encoding='utf-8') if l.strip()]
    scan = json.load(open(os.path.join(RAW, 'scan.json'), encoding='utf-8'))
    fs = {}
    p = os.path.join(RAW, 'figscores.json')
    if os.path.exists(p):
        fs = json.load(open(p, encoding='utf-8'))
    imgn = {}
    for u, v in scan.items():
        for i in v.get('imgs', []):
            imgn[i['u']] = imgn.get(i['u'], 0) + 1
    chrome = {u for u, c in imgn.items() if c >= 25}

    rows = []
    for n, u in enumerate(urls, 1):
        v = scan.get(u)
        if not v:
            rows.append((n, u, 'UNSCANNED', '', '', '', 0, 0))
            continue
        t = clean(v.get('text') or '')
        cls = ''
        if v['st'] != 200:
            cls = 'DEAD'
        figs = [i for i in v.get('imgs', []) if i['u'] not in chrome]
        snip = bool(v.get('pre') or v.get('svg') or v.get('viewer'))
        ai = v['ai_n'] > 0
        if cls == '':
            if figs and ai:
                cls = 'AI_FIG'
            elif figs:
                cls = 'NOAI_FIG'
            elif snip and ai:
                cls = 'PRE'
            elif ai:
                cls = 'AI_NOFIG'
            else:
                cls = 'NOART'
        hits = []
        if ai:
            for c in contexts(t):
                if AIPHRASE.search(c) and BPMNW.search(c):
                    hits.append(c)
        # figure signals
        fd = fa = 0
        for i in figs:
            s = fs.get(i['u'])
            if not s:
                continue
            if s['diagram'] >= 2:
                fd += 1
            if s['ai'] >= 1:
                fa += 1
        rows.append((n, u, cls, v.get('t', '')[:80], (hits[0][:200] if hits else ''),
                     len(figs), fd, fa))
    with open(os.path.join(RAW, 'triage2.tsv'), 'w', encoding='utf-8') as fh:
        for r in rows:
            fh.write('\t'.join(str(x).replace('\t', ' ') for x in r) + '\n')
    import collections
    cc = collections.Counter(r[2] for r in rows)
    print('classes:', dict(cc))
    rev = [r for r in rows if r[2] in ('AI_FIG', 'PRE', 'UNSCANNED')]
    print(f'review rows: {len(rev)}  (of which have an AI<->BPMN window: '
          f'{sum(1 for r in rev if r[4])})')
    print(f'review rows with a figure whose OCR names diagram constructs: '
          f'{sum(1 for r in rev if r[6])}')
    print(f'review rows with a figure whose OCR names AI: {sum(1 for r in rev if r[7])}')


if __name__ == '__main__':
    main()
