# -*- coding: utf-8 -*-
"""E0 rows for the vendor pages whose only figures are photographs or
illustrations: no artefact is published, so nothing can be judged in.

Selection (mechanical): the page is in cand_pages.json with no figure signal at
all - no image whose alt names a process/diagram/AI, and no OCR label in any of
its figures naming a BPMN construct or an AI element. The `figure_note` field
lists the page's actual figure alts and file names, so the researcher can audit
the call without re-opening the page.

usage: python ledgers/_flw_rows_e0mkt.py <out.json>
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, 'flowable.raw')
sys.path.insert(0, HERE)
from _flw_rows import clean, pick_quote  # noqa: E402

HOSTS = ('www.flowable.com', 'flowable.com', 'flowfest.flowable.com')


def main():
    out_path = sys.argv[1]
    scan = json.load(open(os.path.join(RAW, 'scan.json'), encoding='utf-8'))
    cand = json.load(open(os.path.join(RAW, 'cand_pages.json'), encoding='utf-8'))
    import html
    import collections
    imgn = collections.Counter()
    for u, v in scan.items():
        for i in v.get('imgs', []):
            imgn[html.unescape(i['u'])] += 1
    chrome = {u for u, c in imgn.items() if c >= 25}
    rows = []
    for n, c in sorted(cand.items(), key=lambda t: int(t[0])):
        if c['diag_alt'] or c['ai_alt'] or c['ocr_ai'] or c['ocr_dia']:
            continue
        host = c['url'].split('/')[2]
        if host not in HOSTS:
            continue
        v = scan[c['url']]
        figs = []
        for i in v.get('imgs', []):
            u = html.unescape(i['u'])
            if u in chrome:
                continue
            figs.append(((i.get('alt') or '').strip() or '(no alt)',
                         u.split('?')[0].rsplit('/', 1)[-1][:70]))
        note = '; '.join(f'{a} | {f}' for a, f in figs[:6]) or '(no figure)'
        t = clean(v.get('text') or '')
        ev = pick_quote(t) or (v.get('t') or c['url'])
        rows.append({'n': int(n), 'url': c['url'], 'title': (v.get('t') or '')[:120],
                     'verdict': 'EXCLUDE', 'reason': 'E0-no-artefact', 'judgment': False,
                     'evidence': ev[:220], 'record': None,
                     'figure_note': note[:400],
                     'needs_visual_check': False, 'needs_human_ruling': False,
                     'accessed': '2026-09-25'})
    json.dump(rows, open(out_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print(f'wrote {len(rows)} rows')
    for r in rows[:4]:
        print(' ', r['n'], '|', r['evidence'][:90], '||', r['figure_note'][:90])


if __name__ == '__main__':
    main()
