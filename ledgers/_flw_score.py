# -*- coding: utf-8 -*-
"""Merge the OCR shards and score every candidate figure.

The visual channel for this session is RapidOCR over the native-resolution asset
(Read on a PNG delivers no image content here - verified). This script turns the
OCR labels into the two signals the census actually needs:

  diagramness - do the labels inside the figure name BPMN constructs
                (gateway, start/end event, task, subprocess, lane, pool, ...)?
  ainess      - do the labels name an AI element inside the process
                (agent, AI, LLM, model names, prompt, classify/extract/summarise)?

Output: ledgers/flowable.raw/figscores.json
  {img_url: {n, size, diagram, ai, diagram_hits, ai_hits, labels, pages}}
"""
import json
import os
import re
import sys

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'flowable.raw')

DIAGRAM = re.compile(
    r'\b(gateway|start event|end event|boundary event|intermediate|sub-?process|'
    r'subprocess|call activity|user task|service task|script task|manual task|'
    r'business rule task|receive task|send task|task list|lane|pool|collaboration|'
    r'sequence flow|message flow|event|event-?based|exclusive|parallel|inclusive|'
    r'adhoc|ad-?hoc|process model|bpmn|dm n|decision table|terminate|timer|'
    r'error|signal|escalation|compensation|multi-?instance|milestone|stage)\b', re.I)
AI = re.compile(
    r'(?<![A-Za-z])(ai|a\.i\.|llm|gpt|openai|anthropic|claude|gemini|llama|mistral|'
    r'ollama|bedrock|agent\w*|agentic|prompt\w*|chatbot|copilot|assistant|genai|'
    r'generative|sentiment|classif\w*|embedding|vector store|rag|guardrail\w*)'
    r'(?![A-Za-z])', re.I)


MODELUI = re.compile(
    r'(?i)^(cancel|save|close|settings|prompt|description|required|label|name|key|type|'
    r'string|boolean|integer|double|localdate|array|default value|missing value|null value|'
    r'select\.\.\.|add operation|add input parameter|add output parameter|test the prompt|'
    r'edit input parameter|edit output parameter|mapping name|input|output|system message|'
    r'user message|test ai prompt response|properties|general|advanced|overview|search|'
    r'sign in|log in|login|username|password|filter|sort|edit|delete|create|new|next|back|'
    r'actions|status|category|documentation)$')


def kind(labels):
    """Rough figure kind from the labels drawn inside it."""
    if not labels:
        return 'illegible'
    txt = '\n'.join(labels)
    dh = len({m.group(0).lower() for m in DIAGRAM.finditer(txt)})
    ah = len({m.group(0).lower() for m in AI.finditer(txt)})
    ui = sum(1 for l in labels if MODELUI.match(l.strip()))
    longl = sum(1 for l in labels if len(l) > 120)
    if ui >= 3 and ui >= dh:
        return 'ui'
    if longl >= 2 and ui < 2:
        return 'textshot'
    if dh >= 2:
        return 'diagram'
    if len(labels) <= 3:
        return 'sparse'
    return 'other'


def score(labels):
    txt = '\n'.join(labels)
    dh = sorted({m.group(0).lower() for m in DIAGRAM.finditer(txt)})
    ah = sorted({m.group(0).lower() for m in AI.finditer(txt)})
    return dh, ah


def main():
    out = {}
    for i in range(5):
        p = os.path.join(RAW, f'ocr_s{i}.json')
        if not os.path.exists(p):
            print('missing', p, file=sys.stderr)
            continue
        for u, rec in json.load(open(p, encoding='utf-8')).items():
            out.setdefault(u, rec)
    print('merged imgs', len(out), flush=True)
    scores = {}
    for u, rec in out.items():
        labs = rec.get('labels') or []
        dh, ah = score(labs)
        scores[u] = {'size': rec.get('size'), 'n': rec.get('n', len(labs)),
                     'diagram': len(dh), 'ai': len(ah),
                     'diagram_hits': dh, 'ai_hits': ah, 'kind': kind(labs),
                     'labels': labs, 'pages': rec.get('pages', []),
                     'err': rec.get('err')}
    json.dump(scores, open(os.path.join(RAW, 'figscores.json'), 'w', encoding='utf-8'),
              ensure_ascii=False)
    both = {u: s for u, s in scores.items() if s['diagram'] >= 2 and s['ai'] >= 1}
    dia = {u: s for u, s in scores.items() if s['diagram'] >= 2}
    print(f'figures with >=2 diagram hits: {len(dia)}; of those also AI-ish: {len(both)}')
    print(f'figures with 0 legible labels: {sum(1 for s in scores.values() if not s["labels"])}')


if __name__ == '__main__':
    main()
