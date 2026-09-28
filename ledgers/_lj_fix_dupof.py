# -*- coding: utf-8 -*-
"""Fill duplicate_of on the marketing E3 rows appended by _lj_mkt_rows2.py.

The builder's E3 evidence text already names the owning row
("... is byte-identical to the asset recorded at row <n> (<url>)"), because it
was written from the artefact_owner map.  So duplicate_of is recovered from the
row's own evidence rather than guessed.  Verifies the named row is a real row
in the ledger and reports anything that does not resolve.

usage: python ledgers/_lj_fix_dupof.py [--dry]
"""
import io, json, re, sys

LED = 'ledgers/loyjoy.jsonl'


def main():
    dry = '--dry' in sys.argv
    lines = [l for l in io.open(LED, encoding='utf-8') if l.strip()]
    parsed = [json.loads(l) for l in lines]
    known = {r.get('n') for r in parsed if r.get('n')}
    fixed = unresolved = 0
    for i, r in enumerate(parsed):
        if r.get('reason') != 'E3-duplicate' or r.get('duplicate_of'):
            continue
        m = re.search(r'recorded at row (\d+) \(', r.get('evidence', ''))
        if not m or int(m.group(1)) not in known:
            print('UNRESOLVED n=%s: %s' % (r.get('n'), r.get('evidence', '')[:120]))
            unresolved += 1
            continue
        r['duplicate_of'] = int(m.group(1))
        # rewrite the line in place, preserving key order (duplicate_of now
        # present, so put it after record for readability)
        parsed[i] = r
        fixed += 1
    print('E3 rows given duplicate_of: %d   unresolved: %d' % (fixed, unresolved))
    if dry or not fixed:
        return
    with io.open(LED, 'w', encoding='utf-8', newline='\n') as f:
        for r in parsed:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')


if __name__ == '__main__':
    main()
