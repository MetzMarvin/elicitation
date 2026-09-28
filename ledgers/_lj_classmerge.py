# -*- coding: utf-8 -*-
"""Merge classification fragments into ledgers/_lj_mkt_assetclass.json.

usage: python ledgers/_lj_classmerge.py <fragment.json> [...]
Fragments are flat {asset_name: {kind, ai, ...}} objects. Existing entries win
unless --force is passed before the fragment list.
Also accepts fragments keyed "<sheet>#<pos>", which are ignored here (those need
a sheet->asset-name mapping and are merged by a separate step).
"""
import io, json, os, sys

OUT = 'ledgers/_lj_mkt_assetclass.json'


def load(p):
    try:
        return json.load(io.open(p, encoding='utf-8'))
    except Exception as e:
        print('SKIP', p, type(e).__name__, str(e)[:80])
        return None


def main():
    force = '--force' in sys.argv
    files = [a for a in sys.argv[1:] if a != '--force']
    cur = json.load(io.open(OUT, encoding='utf-8'))
    # only accept keys that are real asset names of this source: any other key
    # (a sheet position like "f0_0.jpg#3", a typo) would become a phantom asset
    # that no page references and that silently hides a real unclassified one.
    known = set(json.load(io.open('ledgers/_lj_mkt_sheets.json', encoding='utf-8'))['bases'])
    before = set(cur)
    added = updated = ignored = 0
    junk = []
    for p in files:
        d = load(p)
        if not isinstance(d, dict):
            continue
        for k, v in d.items():
            if k not in known:
                junk.append(k)
                ignored += 1
                continue
            if not isinstance(v, dict) or 'kind' not in v:
                ignored += 1
                continue
            if k in cur and not force:
                continue
            if k in cur:
                updated += 1
            else:
                added += 1
            cur[k] = v
    json.dump(cur, io.open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('assetclass: %d -> %d entries (added %d, updated %d, ignored %d)'
          % (len(before), len(cur), added, updated, ignored))
    if junk:
        print('  rejected keys not matching any asset name:', junk[:20],
              '...' if len(junk) > 20 else '')


if __name__ == '__main__':
    main()
