# -*- coding: utf-8 -*-
"""Download every unique marketing-host image once (paced), for the exhaustive
marketing sweep the orchestrator asked for."""
import io, json, os, re, time, urllib.request, hashlib

OUT = 'ledgers/loyjoy.raw/mkt_all'
os.makedirs(OUT, exist_ok=True)
assets = json.load(io.open('ledgers/_lj_mkt_allassets.json', encoding='utf-8'))
urls = sorted(assets)
print('unique assets', len(urls))

def key(u):
    b = u.split('/')[-1]
    stem, _, ext = b.rpartition('.')
    parts = stem.split('.')
    name = parts[0]
    h = parts[1][:8] if len(parts) > 1 else 'nohash'
    return '%s__%s.%s' % (re.sub(r'[^A-Za-z0-9_.-]', '_', name)[:70], h, ext)

have = set(os.listdir(OUT))
todo = []
for u in urls:
    if key(u) not in have:
        todo.append(u)
print('to download', len(todo))

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0'), ('Accept', 'image/*,*/*')]
from concurrent.futures import ThreadPoolExecutor
import threading
fails = []
lock = threading.Lock()
count = [0]
def one(u):
    dst = os.path.join(OUT, key(u))
    try:
        with opener.open('https://www.loyjoy.com' + u, timeout=30) as r:
            data = r.read()
        if len(data) < 50:
            raise ValueError('too small')
        open(dst, 'wb').write(data)
        with lock:
            count[0] += 1
            if count[0] % 100 == 0:
                print('%d/%d' % (count[0], len(todo)), flush=True)
    except Exception as e:
        with lock:
            fails.append((u, str(e)[:80]))
    time.sleep(0.3)
with ThreadPoolExecutor(max_workers=4) as ex:
    list(ex.map(one, todo))
done = count[0]
json.dump(fails, io.open('ledgers/_lj_mkt_allassets_fails.json', 'w'), indent=1)
sizes = [(f, os.path.getsize(os.path.join(OUT, f))) for f in os.listdir(OUT)]
print('downloaded', done, 'fails', len(fails), 'total files', len(sizes))
print('total bytes', sum(s for _, s in sizes))
