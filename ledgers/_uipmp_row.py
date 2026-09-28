# Append one judged ledger row: python _uipmp_row.py '<json with n, verdict, reason, judgment, evidence, judged_from, ...>'
import json, os, sys
ELI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
scan = {}
for l in open(os.path.join(ELI, 'ledgers', 'uipath-marketplace.raw', 'scan.jsonl'), encoding='utf-8'):
    r = json.loads(l); scan[r['n']] = r
with open(os.path.join(ELI, 'ledgers', 'uipath-marketplace.jsonl'), 'a', encoding='utf-8', newline='\n') as fo:
    for arg in sys.argv[1:]:
        for d in (json.loads(arg) if arg.strip().startswith('[') else [json.loads(arg)]):
            s = scan[d['n']]
            row = {"n": d['n'], "url": s['url'], "title": s.get('title'), "verdict": d['verdict'],
                   "reason": d.get('reason'), "judgment": d['judgment'], "evidence": d['evidence'],
                   "judged_from": d['judged_from'], "record": d.get('record'),
                   "needs_visual_check": d.get('nvc', False), "needs_human_ruling": d.get('nhr', False),
                   "accessed": d.get('accessed', '2026-09-28')}
            for k in ('question', 'duplicate_of', 'blocker', 'supersedes_row'):
                if k in d: row[k] = d[k]
            assert len(row['evidence'].split()) <= 25, ('evidence too long', d['n'])
            row['evidence'] = ' '.join(row['evidence'].split())
            assert row['evidence'] in ' '.join(s.get('text', '').split()) or d.get('ev_src'), ('evidence not verbatim in listing text', d['n'])
            fo.write(json.dumps(row, ensure_ascii=False) + '\n')
            print('row', d['n'], row['verdict'], row['reason'])
