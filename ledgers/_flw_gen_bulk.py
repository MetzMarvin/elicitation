# -*- coding: utf-8 -*-
"""Bulk rows + records for the Flowable pages whose figures could not certify a
BPMN artefact. Follows the rules in CLAUDE.md section 5 and the orchestrator's
OCR ruling: a figure that OCR could not certify, or that carries AI-ish labels,
is UNCERTAIN with needs_visual_check, never an exclusion.

Decision per page (classes AI_FIG / NOAI_FIG only):
  E0  every figure OCR-scored, no figure names a BPMN construct or an AI element,
      and (for marketing pages) no image alt names a process/AI either.
  E2  a figure names BPMN constructs, no figure names an AI element, and the page
      text contains no AI word at all (mechanical, judgment false).
  UNCERTAIN  anything unresolved: a figure with AI labels, a figure naming BPMN
      constructs on a page that does discuss AI, or a figure OCR never scored.

usage: python ledgers/_flw_gen_bulk.py plan|run
writes corpus/flowable/NNN_*.md, corpus/flowable/NNN_*.png,
       ledgers/flowable.raw/rows_bulk.json, ledgers/flowable.raw/visual-queue.json
"""
import collections
import html
import json
import os
import re
import sys
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ELI = os.path.dirname(HERE)
RAW = os.path.join(HERE, 'flowable.raw')
CORPUS = os.path.join(ELI, 'corpus', 'flowable')
CACHE = os.path.join(RAW, 'imgcache')
UA = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/124.0 Safari/537.36 (research; master-thesis elicitation, read-only)'}
sys.path.insert(0, HERE)
from _flw_rows import clean, pick_quote  # noqa: E402

AI = re.compile(r'(?<![A-Za-z])(ai|a\.i\.|llm|gpt|openai|anthropic|claude|gemini|llama|mistral|'
                r'ollama|bedrock|agent\w*|agentic|prompt\w*|chatbot|copilot|assistant|genai|'
                r'generative|sentiment|classif\w*|embedding|vector store|rag|guardrail\w*)'
                r'(?![A-Za-z])', re.I)
BPMN_ELEM = re.compile(r'(?i)\b(start event|end event|boundary event|intermediate|user task|'
                       r'service task|script task|manual task|business rule task|receive task|'
                       r'send task|sub-?process|call activity|exclusive gateway|parallel gateway|'
                       r'inclusive gateway|event-?based gateway|complex gateway|pool|lane|'
                       r'sequence flow|message flow|ad-?hoc|case plan model|stage|milestone|'
                       r'bpmn|process model|modeler|task list)\b')


def slugify(u):
    s = re.sub(r'^https?://', '', u)
    s = re.sub(r'[^A-Za-z0-9]+', '-', s).strip('-')
    return s[-60:]


def cache_path(u):
    return os.path.join(CACHE, re.sub(r'[^A-Za-z0-9]', '_', u)[-140:])


def fetch(u):
    p = cache_path(u)
    if os.path.exists(p) and os.path.getsize(p) > 0:
        return p
    try:
        req = urllib.request.Request(u, headers=UA)
        with urllib.request.urlopen(req, timeout=40) as r:
            data = r.read()
        os.makedirs(CACHE, exist_ok=True)
        open(p, 'wb').write(data)
        time.sleep(0.3)
        return p
    except Exception:  # noqa: BLE001
        return None


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else 'plan'
    scan = json.load(open(os.path.join(RAW, 'scan.json'), encoding='utf-8'))
    cand = json.load(open(os.path.join(RAW, 'cand_pages.json'), encoding='utf-8'))
    fs = {}
    for f in ['figscores.json']:
        p = os.path.join(RAW, f)
        if os.path.exists(p):
            fs.update(json.load(open(p, encoding='utf-8')))
    for i in range(6):  # any extra completed shards
        p = os.path.join(RAW, f'ocr_all{i}.json')
        if os.path.exists(p):
            fs.update(json.load(open(p, encoding='utf-8')))
    for pre in ('ocr_dn', 'ocr_dc'):
        for i in range(3):
            p = os.path.join(RAW, f'{pre}{i}.json')
            if os.path.exists(p):
                fs.update(json.load(open(p, encoding='utf-8')))
    # rescore on the fly (same rules as _flw_score.py)
    import importlib.util
    spec = importlib.util.spec_from_file_location('score', os.path.join(HERE, '_flw_score.py'))
    S = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(S)
    for u, rec in list(fs.items()):
        if 'kind' in rec:
            continue
        labs = rec.get('labels') or []
        dh, ah = S.score(labs)
        rec.update({'diagram': len(dh), 'ai': len(ah), 'diagram_hits': dh, 'ai_hits': ah,
                    'kind': S.kind(labs)})
    imgn = collections.Counter()
    for u, v in scan.items():
        for i in v.get('imgs', []):
            imgn[html.unescape(i['u'])] += 1
    chrome = {u for u, c in imgn.items() if c >= 25}
    DIAG_ALT = re.compile(r'(?i)\b(process|workflow|bpmn|diagram|flow|gateway|task|lane|model|'
                          r'path|branch|step)s?\b')

    decisions, rows, queue = {}, [], []
    nnn = 4
    for num, c in sorted(cand.items(), key=lambda t: int(t[0])):
        if not (c['diag_alt'] or c['ai_alt'] or c['ocr_ai'] or c['ocr_dia']):
            continue
        num = int(num)
        v = scan[c['url']]
        figs = []
        for i in v.get('imgs', []):
            iu = html.unescape(i['u'])
            if iu in chrome:
                continue
            figs.append((iu, (i.get('alt') or '').strip()))
        sc = [(iu, a, fs.get(iu)) for iu, a in figs]
        ai_figs = [(iu, a, s) for iu, a, s in sc if s and s.get('ai', 0) >= 1]
        dia_figs = [(iu, a, s) for iu, a, s in sc if s and s.get('diagram', 0) >= 2]
        unscored = [(iu, a) for iu, a, s in sc if not s]
        unread = [(iu, a, s) for iu, a, s in sc if s and (not s.get('labels') or s.get('err'))]
        text = clean(v.get('text') or '')
        ai_text = bool(AI.search(text))
        # ---------------- decision
        if ai_figs or unscored or unread:
            verdict, reason = 'UNCERTAIN', None
        elif dia_figs:
            verdict, reason = ('EXCLUDE', 'E2-no-ai-element') if not ai_text \
                else ('UNCERTAIN', None)
        else:
            verdict, reason = 'EXCLUDE', 'E0-no-artefact'
        if verdict == 'UNCERTAIN' and not ai_text and not ai_figs and not unscored and not unread \
                and not dia_figs:
            verdict, reason = 'EXCLUDE', 'E0-no-artefact'
        decisions[num] = verdict
        evq = pick_quote(text) or (v.get('t') or c['url'])
        fig_note = '; '.join(f'{a or "(no alt)"} | {iu.split("?")[0].rsplit("/", 1)[-1][:50]}'
                             for iu, a, _ in (ai_figs + dia_figs + unread)[:4]) \
            or '; '.join(f'{a or "(no alt)"} | {iu.split("?")[0].rsplit("/", 1)[-1][:50]}'
                         for iu, a in figs[:4])
        ocr_txt = ''
        for iu, a, s in (ai_figs + dia_figs)[:1]:
            ocr_txt = ' | '.join((s or {}).get('labels', [])[:16])[:400]
        if verdict == 'EXCLUDE':
            rows.append({'n': num, 'url': c['url'], 'title': (v.get('t') or '')[:120],
                         'verdict': 'EXCLUDE', 'reason': reason, 'judgment': False,
                         'evidence': evq[:220], 'record': None, 'figure_note': fig_note[:400],
                         'needs_visual_check': False, 'needs_human_ruling': False,
                         'accessed': '2026-09-25'})
            continue
        # ---------------- record + capture
        best = (ai_figs or dia_figs or unread or [(iu, a, None) for iu, a in figs])
        order = {}
        for iu, a, s in best:
            order.setdefault(iu, (a, s))
        # prefer a figure with AI labels, then diagram labels, then the largest
        pick = None
        for iu, (a, s) in order.items():
            if s and s.get('ai'):
                pick = (iu, a, s)
                break
        if not pick:
            for iu, (a, s) in order.items():
                if s and s.get('diagram', 0) >= 2:
                    pick = (iu, a, s)
                    break
        if not pick:
            for iu, (a, s) in order.items():
                pick = (iu, a, s)
                break
        if not pick:
            verdict = 'EXCLUDE'
            rows.append({'n': num, 'url': c['url'], 'title': (v.get('t') or '')[:120],
                         'verdict': 'EXCLUDE', 'reason': 'E0-no-artefact', 'judgment': False,
                         'evidence': evq[:220], 'record': None, 'figure_note': fig_note[:400],
                         'needs_visual_check': False, 'needs_human_ruling': False,
                         'accessed': '2026-09-25'})
            continue
        iu, alt, s = pick
        rid = f'{nnn:03d}'
        base = f'{rid}_{slugify(c["url"])}'
        rec = f'corpus/flowable/{base}.md'
        png = f'{base}.png'
        q = ('The page publishes figures that could not be read well enough to decide whether a '
             'BPMN process diagram on it contains an AI element. Does any figure here show a BPMN '
             'process containing an AI/LLM element?')
        if mode == 'run':
            os.makedirs(CORPUS, exist_ok=True)
            if not os.path.exists(os.path.join(CORPUS, png)):
                src = fetch(iu)
                if src:
                    open(os.path.join(CORPUS, png), 'wb').write(open(src, 'rb').read())
            size = (s or {}).get('size') or [0, 0]
            cq = 'legible' if (s and s.get('n', 0) >= 8) else \
                ('marginal' if (s and s.get('n', 0) > 0) else 'poor')
            lines = [
                '---',
                f'n: {num}',
                'source: flowable',
                'source_name: Flowable (enterprise documentation, vendor blog/marketing site, training site)',
                f'title: {(v.get("t") or "")[:120]}',
                f'url: {c["url"]}',
                'accessed: 2026-09-25',
                'verdict: UNCERTAIN',
                'needs_human_ruling: false',
                'question: null',
                'needs_visual_check: true',
                f'bpmn_evidence: {("figure captions, alt text or OCR labels naming BPMN constructs: " + fig_note) if dia_figs else "not established from the page text; the page is about process/case modelling: " + evq[:150]}',
                f'bpmn_evidence_quote: "{evq[:200]}"',
                f'ai_evidence: {("labels inside the figure name an AI element: " + ocr_txt) if ocr_txt else ("the page text discusses AI: " + evq[:150])}',
                f'ai_evidence_quote: "{(ocr_txt or evq)[:200]}"',
                'artefacts:',
                f'  screenshot: {png}',
                f'  archive: null',
                '  bpmn_xml: null',
                'duplicate_of: null',
                'access: public',
                'capture_source: original-asset',
                f'capture_quality: {cq}',
                f'capture_width_px: {size[0]}',
                f'capture_method: urllib download of {iu} (asset published by the page); labels inside read with RapidOCR, this session cannot receive image content',
                '---',
                '',
                '## Why this row is UNCERTAIN',
                '',
                'The page publishes figures and mentions AI, but the figure that would decide the',
                'verdict could not be certified from the evidence this session can read (the DOM, the',
                'page text, and OCR labels). Per CLAUDE.md section 5 an unresolved figure is UNCERTAIN',
                'with needs_visual_check, never an exclusion.',
                '',
                '## Observations (description only, no interpretation)',
                '',
                f'- **Figures on the page:** {fig_note}',
                f'- **OCR labels of the captured figure:** {ocr_txt or "(none legible)"}',
                f'- **Page text quote:** {evq[:220]}',
                f'- **Captured asset:** {iu} ({size[0]}x{size[1]})',
                '',
                '## What to check',
                '',
                'Whether the captured figure (or another figure on the page) is a BPMN 2.0 process',
                'diagram and whether an AI/LLM element sits inside that process.',
                '',
            ]
            open(os.path.join(CORPUS, base + '.md'), 'w', encoding='utf-8').write('\n'.join(lines))
        queue.append({'n': num, 'url': c['url'], 'record': rec, 'figure_path': png,
                      'ocr_text': ocr_txt, 'question': q})
        rows.append({'n': num, 'url': c['url'], 'title': (v.get('t') or '')[:120],
                     'verdict': 'UNCERTAIN', 'reason': None, 'judgment': True,
                     'evidence': evq[:220], 'record': rec, 'figure_note': fig_note[:400],
                     'needs_visual_check': True, 'needs_human_ruling': False,
                     'question': None, 'accessed': '2026-09-25'})
        nnn += 1
    cc = collections.Counter(decisions.values())
    print('decisions:', dict(cc))
    print('rows:', len(rows), 'records:', nnn - 4)
    if mode == 'run':
        json.dump(rows, open(os.path.join(RAW, 'rows_bulk.json'), 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=0)
        json.dump(queue, open(os.path.join(RAW, 'visual-queue.json'), 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=0)
        print('wrote rows_bulk.json and visual-queue.json')


if __name__ == '__main__':
    main()
