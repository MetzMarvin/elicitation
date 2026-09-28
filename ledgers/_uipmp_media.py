# Download listing media (original CDN asset) for AI-keyword listings; 1 req / 5 s; stop on 429/challenge.
import json, os, re, sys, time, urllib.request
RAW = 'uipath-marketplace.raw'; UA = {'User-Agent': 'Mozilla/5.0 (research; master-thesis elicitation, read-only)'}
sys.path.insert(0, '.'); from _uipmp_crawl import AI
idx = os.path.join(RAW, 'media', 'index.jsonl')
done = set()
if os.path.exists(idx):
    for l in open(idx, encoding='utf-8'): done.add(json.loads(l)['src'])
scan = {}
for l in open(os.path.join(RAW, 'scan.jsonl'), encoding='utf-8'):
    r = json.loads(l)
    if r['http'] == 200: scan[r['n']] = r
todo = []
for n in sorted(scan):
    r = scan[n]
    if not AI.search(r['text']): continue
    for k, src in enumerate(r['media']):
        if re.search(r'\.(mp4|webm)(\?|$)', src, re.I) or 'youtu' in src: continue
        orig = re.sub(r'^https?://(www\.)?uipath\.com/cdn-cgi/image/[^/]*/', '', src)
        if src not in done: todo.append((n, k, src, orig))
print('todo', len(todo), flush=True)
with open(idx, 'a', encoding='utf-8') as fo:
    for n, k, src, orig in todo:
        ext = os.path.splitext(orig.split('?')[0])[1].lower() or '.img'
        path = os.path.join(RAW, 'media', f'{n:04d}_{k}{ext}')
        try:
            with urllib.request.urlopen(urllib.request.Request(orig, headers=UA), timeout=40) as resp:
                data = resp.read(); code = resp.status
        except urllib.error.HTTPError as e:
            code, data = e.code, b''
            if e.code == 429 or e.headers.get('Cf-Mitigated'):
                print('STOP', code, orig, flush=True); break
        if data: open(path, 'wb').write(data)
        fo.write(json.dumps({'n': n, 'k': k, 'src': src, 'orig': orig, 'http': code, 'file': path if data else None, 'bytes': len(data)}) + '\n'); fo.flush()
        time.sleep(5)
print('done', flush=True)
