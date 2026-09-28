# -*- coding: utf-8 -*-
"""Append ledger rows to ledgers/<slug>.jsonl from a JSON array (or JSONL) file.

usage: python ledgers/_flw_append.py ledgers/flowable.jsonl rows.json
`rows.json` is a JSON array of row objects. Appends one JSON object per line,
immediately (the caller is expected to run this as it judges, not once at the end).
"""
import json
import os
import sys


def main():
    led = sys.argv[1]
    src = sys.argv[2]
    rows = json.load(open(src, encoding='utf-8'))
    have = set()
    if os.path.exists(led):
        for line in open(led, encoding='utf-8'):
            line = line.strip()
            if not line:
                continue
            try:
                o = json.loads(line)
            except Exception:  # noqa: BLE001
                continue
            if 'n' in o:
                have.add(o['n'])
    added = 0
    with open(led, 'a', encoding='utf-8') as fh:
        for r in rows:
            if r.get('n') in have:
                print('skip existing n=', r.get('n'))
                continue
            fh.write(json.dumps(r, ensure_ascii=False) + '\n')
            added += 1
    print(f'appended={added}')


if __name__ == '__main__':
    main()
