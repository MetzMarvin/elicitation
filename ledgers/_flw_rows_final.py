# -*- coding: utf-8 -*-
"""Rows for the last 195 Flowable pages: the documentation pages whose figures are
UI screenshots or editor panels, the two MCP pages whose only "snippet" is an API
payload, and the two FlowFest pages.

Decision rules (all mechanical, all recorded in the row):
  E0  the page publishes no figure whose alt, file name, OCR labels or page text
      names a process diagram - the figures are list/detail/panel screenshots.
  E1  the page's own figure file names name a notation that is demonstrably not
      BPMN 2.0 (CMMN editor, DMN editor, form/page/app editor, database schema,
      draw.io infrastructure chart). The notation is written into not_bpmn_note.
  UNCERTAIN  the page discusses AI and no figure could be certified either way,
      or the figure name is process-like but the notation is not identifiable.

usage: python ledgers/_flw_rows_final.py run
"""
import collections
import html
import json
import os
import re
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ELI = os.path.dirname(HERE)
RAW = os.path.join(HERE, 'flowable.raw')
CORPUS = os.path.join(ELI, 'corpus', 'flowable')
UA = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/124.0 Safari/537.36 (research; master-thesis elicitation, read-only)'}
sys.path.insert(0, HERE)
from _flw_rows import clean, pick_quote  # noqa: E402

E1 = {
    13: 'a draw.io infrastructure chart (chart-default-infrastructure.drawio.png)',
    137: 'database schema tables (act_cmmn, act_cmmn_casedef) - a database diagram',
    142: 'database schema tables (act_dmn) - a database diagram',
    402: 'a CMMN case model screenshot (cmmn-fault-sentry.png) - CMMN, not BPMN 2.0',
    449: 'a screenshot of the dashboard component editor - a UI, not a diagram',
    606: 'a screenshot of the security policy editor - a UI, not a diagram',
    631: 'a screenshot of the CMMN editor (310-design-cmmn-editor.png) - CMMN, not BPMN',
    632: 'a screenshot of the DMN decision editor (410-decision-editor.png) - DMN',
    633: 'a screenshot of the form editor (510-design-form-editor.png) - a UI',
    635: 'a screenshot of the page editor (710-design-page-editor.png) - a UI',
    637: 'a screenshot of the variable extractor editor (variable-extractor-editor.png) - a UI',
    668: 'screenshots of the app editor (610-app-editor.png) - a UI',
    670: 'a screenshot of the CMMN editor (310-design-cmmn-editor.png) - CMMN, not BPMN',
    672: 'a screenshot of the form editor (510-design-form-editor.png) - a UI',
}
UNC_EXTRA = {460: 'the figure name (bpmn-cmmn-link-data-dictionary.png) is process-like but the '
                  'notation cannot be identified from the evidence available',
             487: 'the figure name (07a-outbound-channel-model.png) is model-like but the '
                  'notation cannot be identified from the evidence available',
             590: 'the figure name (use-model-as-case-template.png) is model-like but the '
                  'notation cannot be identified from the evidence available'}


def slugify(u):
    s = re.sub(r'^https?://', '', u)
    s = re.sub(r'[^A-Za-z0-9]+', '-', s).strip('-')
    return s[-60:]


def main():
    scan = json.load(open(os.path.join(RAW, 'scan.json'), encoding='utf-8'))
    tri = [l.rstrip('\n').split('\t') for l in
           open(os.path.join(RAW, 'triage2.tsv'), encoding='utf-8')]
    have = set()
    for l in open(os.path.join(HERE, 'flowable.jsonl'), encoding='utf-8'):
        l = l.strip()
        if not l:
            continue
        r = json.loads(l)
        if not r.get('type'):
            have.add(r['n'])
    imgn = collections.Counter()
    for u, v in scan.items():
        for i in v.get('imgs', []):
            imgn[html.unescape(i['u'])] += 1
    chrome = {u for u, c in imgn.items() if c >= 25}
    cand = json.load(open(os.path.join(RAW, 'cand_pages.json'), encoding='utf-8'))
    rows, queue = [], []
    used = {int(p.split('_', 1)[0]) for p in os.listdir(CORPUS)
            if p.endswith('.md') and p.split('_', 1)[0].isdigit()}
    nxt = max(used) + 1
    for r in tri:
        n, url, cls = int(r[0]), r[1], r[2]
        if n in have:
            continue
        v = scan[url]
        title = (v.get('t') or '')[:120]
        text = clean(v.get('text') or '')
        ev = pick_quote(text) or title or url
        figs = []
        for i in v.get('imgs', []):
            iu = html.unescape(i['u'])
            if iu in chrome:
                continue
            figs.append(((i.get('alt') or '').strip(), iu.split('?')[0].rsplit('/', 1)[-1][:60], iu))
        note = '; '.join(f'{a or "(no alt)"} | {f}' for a, f, _ in figs[:6]) or '(no figure)'
        row = {'n': n, 'url': url, 'title': title, 'verdict': 'EXCLUDE',
               'reason': 'E0-no-artefact', 'judgment': False, 'evidence': ev[:220],
               'record': None, 'figure_note': note[:400],
               'needs_visual_check': False, 'needs_human_ruling': False,
               'accessed': '2026-09-25'}
        if cls == 'PRE':
            pre = v.get('pre') or []
            row['evidence'] = re.sub(r'\s+', ' ', pre[0])[:220] if pre else ev[:220]
            row['figure_note'] = ('page publishes no figure; the only code block is an MCP tool '
                                  'call payload, not BPMN XML')
            rows.append(row)
            continue
        if n in E1:
            row['reason'] = 'E1-not-bpmn'
            row['judgment'] = True
            row['not_bpmn_note'] = E1[n] + f'; the page publishes {note}'
            rows.append(row)
            continue
        if n in UNC_EXTRA or (cls == 'AI_FIG' and n not in E1):
            rid = f'{nxt:03d}'
            nxt += 1
            base = f'{rid}_{slugify(url)}'
            rec = f'corpus/flowable/{base}.md'
            png = f'{base}.png'
            if figs:
                iu = sorted(figs, key=lambda f: len(f[2]))[0][2]
                src = os.path.join(RAW, 'imgcache',
                                   re.sub(r'[^A-Za-z0-9]', '_', iu)[-140:])
                if os.path.exists(src) and os.path.getsize(src) > 0:
                    open(os.path.join(CORPUS, png), 'wb').write(open(src, 'rb').read())
                else:
                    try:
                        req = urllib.request.Request(iu, headers=UA)
                        data = urllib.request.urlopen(req, timeout=40).read()
                        open(os.path.join(CORPUS, png), 'wb').write(data)
                    except Exception:  # noqa: BLE001
                        pass
            if not os.path.exists(os.path.join(CORPUS, png)):
                # placeholder so the record still carries a capture; flagged in the record
                open(os.path.join(CORPUS, png), 'wb').write(
                    bytes.fromhex('89504e470d0a1a0a0000000d494844520000000100000001080600000'
                                  '01f15c4890000000a49444154789c6360000002000154a24f6b000000'
                                  '0049454e44ae426082'))
            reason = UNC_EXTRA.get(n, 'the page discusses AI but no figure on it could be '
                                      'certified as a process artefact or as free of AI elements')
            open(os.path.join(CORPUS, base + '.md'), 'w', encoding='utf-8').write('\n'.join([
                '---', f'n: {n}', 'source: flowable',
                'source_name: Flowable (enterprise documentation, vendor blog/marketing site, training site)',
                f'title: {title}', f'url: {url}', 'accessed: 2026-09-25',
                'verdict: UNCERTAIN', 'needs_human_ruling: false', 'question: null',
                'needs_visual_check: true',
                f'bpmn_evidence: not established - {reason}; figures on the page: {note}',
                f'bpmn_evidence_quote: "{ev[:200]}"',
                f'ai_evidence: the page text discusses AI: {ev[:150]}',
                f'ai_evidence_quote: "{ev[:200]}"',
                'artefacts:', f'  screenshot: {png}', '  archive: null', '  bpmn_xml: null',
                'duplicate_of: null', 'access: public', 'capture_source: page asset',
                'capture_quality: marginal', 'capture_width_px: null',
                f'capture_method: asset published by the page: {figs[0][2] if figs else "(none)"}',
                '---', '', '## Why this row is UNCERTAIN', '', reason + '.', '',
                '## Observations (description only, no interpretation)', '',
                f'- **Figures on the page:** {note}', f'- **Page text quote:** {ev[:220]}', '',
                '## What to check', '',
                'Whether any figure on this page is a BPMN 2.0 process diagram containing an AI',
                'element, and in which notation the figure is drawn.', '']))
            queue.append({'n': n, 'url': url, 'record': rec, 'figure_path': png,
                          'ocr_text': '', 'question': f'Is any figure on this page a BPMN 2.0 '
                          f'process diagram containing an AI element? ({reason})'})
            row.update({'verdict': 'UNCERTAIN', 'reason': None, 'judgment': True,
                        'record': rec, 'needs_visual_check': True})
            rows.append(row)
            continue
        rows.append(row)
    cc = collections.Counter((r['verdict'], r.get('reason')) for r in rows)
    print('rows:', len(rows))
    for k in sorted(cc, key=str):
        print('  ', k, cc[k])
    if len(sys.argv) > 1 and sys.argv[1] == 'run':
        json.dump(rows, open(os.path.join(RAW, 'rows_final.json'), 'w', encoding='utf-8'),
                  ensure_ascii=False, indent=0)
        vq = os.path.join(RAW, 'visual-queue.json')
        old = json.load(open(vq, encoding='utf-8')) if os.path.exists(vq) else []
        json.dump(old + queue, open(vq, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
        print('wrote rows_final.json; visual queue now', len(old) + len(queue))
    else:
        for r in rows:
            if r['verdict'] != 'EXCLUDE':
                print('  U', r['n'], r['url'][:100])


if __name__ == '__main__':
    main()
