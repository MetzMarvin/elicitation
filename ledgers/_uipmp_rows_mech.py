# -*- coding: utf-8 -*-
"""Append mechanical E2 rows for uipath-marketplace (elicitation-7b).

A row is mechanical E2 only if the listing page was fetched (HTTP 200, parsed) and its
listing text (name .. "Similar Listings", incl. tags, description, resources) contains
no hit of the deliberately broad AI regex in _uipmp_crawl.py.  Everything else is left
for judgement.  Skips any n that already has a ledger row.  Evidence = verbatim summary
sentence (<=25 words).
"""
import json, os, re, sys

ELI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(ELI, 'ledgers', 'uipath-marketplace.jsonl')
SCAN = os.path.join(ELI, 'ledgers', 'uipath-marketplace.raw', 'scan.jsonl')
sys.path.insert(0, os.path.join(ELI, 'ledgers'))
from _uipmp_crawl import AI  # same regex the crawl used

scan = {}
for l in open(SCAN, encoding='utf-8'):
    r = json.loads(l)
    if r['http'] == 200 or r['n'] not in scan:
        scan[r['n']] = r
have = set()
for l in open(LEDGER, encoding='utf-8'):
    o = json.loads(l)
    if o.get('type') is None:
        have.add(o['n'])


def quote(t):
    m = re.search(r'\n\s*Summary\s*\n\s*(.+)', t)
    s = (m.group(1) if m else t.split('\n', 1)[0]).strip()
    w = s.split()
    return ' '.join(w[:25])


added = 0
with open(LEDGER, 'a', encoding='utf-8', newline='\n') as fo:
    for n in sorted(scan):
        r = scan[n]
        if n in have or r['http'] != 200 or not r.get('title'):
            continue
        if AI.search(r['text']):
            continue
        row = {"n": n, "url": r['url'], "title": r['title'], "verdict": "EXCLUDE",
               "reason": "E2-no-ai-element", "judgment": False,
               "evidence": quote(r['text']),
               "judged_from": f"listing page GET (HTTP 200) 2026-09-28, ledgers/uipath-marketplace.raw/html/{n:04d}.html.gz; "
                              f"listing type '{r.get('type')}'; no AI/LLM keyword in listing text or tags (broad regex, _uipmp_crawl.AI); "
                              f"{len(r.get('media', []))} media asset(s) not viewed (mechanical E2)",
               "record": None, "needs_visual_check": False, "needs_human_ruling": False,
               "accessed": "2026-09-28"}
        fo.write(json.dumps(row, ensure_ascii=False) + '\n')
        added += 1
print('added', added)
