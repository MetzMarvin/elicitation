# Append rows from a JSON list file one by one via _uipmp_row.py; report failures, skip n already in the ledger.
import json, os, subprocess, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
done = {json.loads(l).get('n') for l in open('uipath-marketplace.jsonl', encoding='utf-8')}
for d in json.load(open(sys.argv[1], encoding='utf-8')):
    if d['n'] in done and not d.get('supersedes_row'): print('skip', d['n']); continue
    d.setdefault('accessed', '2026-09-28')
    p = subprocess.run([sys.executable, '_uipmp_row.py', json.dumps(d, ensure_ascii=False)], capture_output=True, text=True, encoding='utf-8')
    print(p.stdout.strip() or ('FAIL %s %s' % (d['n'], p.stderr.strip().splitlines()[-1:])))
