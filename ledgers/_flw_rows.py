# -*- coding: utf-8 -*-
"""Emit ledger rows for the mechanical Flowable classes.

usage: python ledgers/_flw_rows.py <out.json> <CLASS> [CLASS ...]

DEAD     -> E0-no-artefact   (dead link; the 404 body is the evidence)
NOART    -> E0-no-artefact   (no figure and no BPMN snippet on the page)
AI_NOFIG -> E0-no-artefact   (page discusses AI but publishes no artefact)
NOAI_FIG -> E2-no-ai-element (page shows a figure, no AI keyword anywhere on it)
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, 'flowable.raw')
CUT = [' Sign up for updates', '\n Comments \n Platform', '© 20',
       'This site is protected by reCAPTCHA', 'Footer navigation', '\n Imprint',
       '\n Platform\n Docs', 'Skip to Main Content Improve your experience']
NAVPRE = re.compile(r'^.{0,500}?Sign Up Now\s*\n', re.S)
BPMNW = re.compile(r'(?i)\b(task|gateway|process|model|bpmn|sub-?process|event|lane|pool|step)\b')

DEAD_EV = {
    'training': 'Error - Flowable',
    'marketing': 'The page you were looking for could not be found.',
}


def clean(t):
    for c in CUT:
        i = t.find(c)
        if i > 200:
            t = t[:i]
    return NAVPRE.sub('', t, count=1).strip()


SENT = re.compile(r'(?<=[.?!])\s+(?=[A-Z"“])')


def pick_quote(t, prefer=BPMNW, nmin=6, nmax=25):
    """A single line of the page's own text, taken whole, so the quote is verbatim:
    the line structure of the extracted text is preserved, nothing is joined across
    a newline. Prefers a line that names a BPMN construct; falls back to the first
    full sentence of a usable length, then to the first words of the text."""
    lines = [l.strip() for l in (t or '').split('\n')]
    cands = []
    for l in lines:
        if not l:
            continue
        for s in SENT.split(l):
            s = s.strip().strip('​').strip()
            if not s or len(s.split()) > nmax:
                continue
            cands.append(s)
    for s in cands:
        if nmin <= len(s.split()) <= nmax and prefer and prefer.search(s) \
                and s[0].isupper():
            return s
    for s in cands:
        if nmin <= len(s.split()) <= nmax and s.endswith(('.', ':', '?')) and s[0].isupper():
            return s
    for s in cands:
        if 4 <= len(s.split()) <= nmax and s[0].isupper():
            return s
    # last resort: the verbatim first 25 words of the first substantial line
    for l in lines:
        w = l.split()
        if len(w) >= 4:
            return ' '.join(w[:nmax])
    return (t or '').strip()[:200]


def main():
    out_path = sys.argv[1]
    classes = set(sys.argv[2:])
    scan = json.load(open(os.path.join(RAW, 'scan.json'), encoding='utf-8'))
    tri = [l.rstrip('\n').split('\t') for l in open(os.path.join(RAW, 'triage2.tsv'),
                                                    encoding='utf-8')]
    rows = []
    for r in tri:
        n, url, cls = int(r[0]), r[1], r[2]
        if cls not in classes:
            continue
        v = scan.get(url, {})
        title = v.get('t', '')
        if cls == 'DEAD':
            ev = DEAD_EV['training'] if 'training.flowable.com' in url else DEAD_EV['marketing']
            rows.append({'n': n, 'url': url, 'title': title, 'verdict': 'EXCLUDE',
                         'reason': 'E0-no-artefact', 'judgment': False, 'evidence': ev,
                         'record': None, 'needs_visual_check': False,
                         'needs_human_ruling': False, 'accessed': '2026-09-25'})
            continue
        t = clean(v.get('text') or '')
        ev = pick_quote(t)
        if not ev:
            ev = title or url
        rows.append({'n': n, 'url': url, 'title': title, 'verdict': 'EXCLUDE',
                     'reason': 'E0-no-artefact' if cls in ('NOART', 'AI_NOFIG')
                     else 'E2-no-ai-element',
                     'judgment': False, 'evidence': ev[:220], 'record': None,
                     'needs_visual_check': False, 'needs_human_ruling': False,
                     'accessed': '2026-09-25'})
    json.dump(rows, open(out_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print(f'wrote {len(rows)} rows to {out_path}')
    for r in rows[:5]:
        print(' ', r['n'], r['reason'], '|', r['evidence'][:110])


if __name__ == '__main__':
    main()
