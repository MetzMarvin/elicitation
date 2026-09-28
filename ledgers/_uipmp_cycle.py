# One processing cycle on newly fetched listings: mechanical E2 rows, media download, contact sheets,
# then print the still-unjudged AI-keyword listings with summary/AI context/media counts.
import json, os, re, subprocess, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
py = sys.executable
print(subprocess.run([py, '_uipmp_rows_mech.py'], capture_output=True, text=True, encoding='utf-8').stdout.strip().splitlines()[-1:])
L = [json.loads(l) for l in open('uipath-marketplace.jsonl', encoding='utf-8')][1:]
done = {r['n'] for r in L if 'n' in r}
S = {}
for l in open('uipath-marketplace.raw/scan.jsonl', encoding='utf-8'):
    r = json.loads(l)
    if r['http'] == 200: S[r['n']] = r
todo = sorted(n for n in S if n not in done)
print('judged', len(done), 'fetched-200', len(S), 'unjudged', len(todo))
if todo:
    print(subprocess.run([py, '_uipmp_media.py'], capture_output=True, text=True, encoding='utf-8').stdout.strip().splitlines()[-1:])
    subprocess.run([py, '_uipmp_view.py'] + [str(n) for n in todo], capture_output=True)
for n in todo:
    r = S[n]; t = r['text']
    m = re.search(r'\n\s*Summary\s*\n\s*(.+)', t)
    print(f"\n## {n} | {r['type']} | {r['title']} | {r['publisher']} | img {len(r['media'])} vid {len(r['video'])} bpmn {r['bpmn']}")
    print('  S:', (m.group(1).strip() if m else '')[:260])
    for k, v in list(r['ai'].items())[:4]: print('  AI', k, ':', ' '.join(v.split())[:170])
