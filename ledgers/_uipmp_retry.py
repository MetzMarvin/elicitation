# -*- coding: utf-8 -*-
"""Rate-limit-compliant retry of the uipath-marketplace listings that got HTTP 429 (elicitation-7b, 2026-09-28).

Operator protocol (b), via elicitation-5a:
  * first request is a single probe, only >= 60 min after the last 429 (08:16:03 GMT);
    probe challenged -> stop (caller waits another 60 min; second failed probe = give up scripting);
  * probe 200 -> resume at <= 1 request / 5 s;
  * any 429 / Cf-Mitigated -> exponential backoff 60 s, 120 s, 240 s ...;
    three consecutive challenges -> stop for good;
  * same User-Agent as the first crawl; no proxy, no header spoofing, no IP rotation.
Appends to raw/scan.jsonl (the last row per n wins downstream). Log: raw/retry.log
"""
import gzip, json, os, sys, time, urllib.request, urllib.error
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _uipmp_crawl import parse, RAW, FRONTIER, OUT, UA

LOG = os.path.join(RAW, 'retry.log')


def log(*a):
    s = time.strftime('%H:%M:%S', time.gmtime()) + ' ' + ' '.join(map(str, a))
    print(s, flush=True)
    open(LOG, 'a', encoding='utf-8').write(s + '\n')


def fetch(u):
    try:
        with urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=40) as resp:
            return resp.status, resp.read().decode('utf-8', 'replace'), resp.geturl(), False
    except urllib.error.HTTPError as e:
        return e.code, '', u, bool(e.headers.get('Cf-Mitigated')) or e.code == 429
    except Exception as e:
        return 'ERR ' + str(e)[:80], '', u, False


def main():
    urls = [l.strip() for l in open(FRONTIER, encoding='utf-8') if l.strip()]
    best = {}
    for l in open(OUT, encoding='utf-8'):
        r = json.loads(l)
        if r['http'] == 200 or r['n'] not in best: best[r['n']] = r['http']
    todo = [i for i in range(1, len(urls) + 1) if best.get(i) != 200]
    log('todo', len(todo))
    consecutive, backoff, first = 0, 60, True
    with open(OUT, 'a', encoding='utf-8') as fo:
        k = 0
        while k < len(todo):
            i = todo[k]; u = urls[i - 1]
            t0 = time.time()
            code, s, final, challenged = fetch(u)
            if challenged:
                consecutive += 1
                log('CHALLENGE', code, i, u, 'consecutive', consecutive)
                if first:
                    log('probe challenged -> stop; wait >= 60 min before the next probe'); return 2
                if consecutive >= 3:
                    log('three consecutive challenges -> stop for good'); return 3
                time.sleep(backoff); backoff *= 2
                continue  # retry the same item after backoff
            first = False; consecutive = 0; backoff = 60
            if s:
                with gzip.open(os.path.join(RAW, 'html', f'{i:04d}.html.gz'), 'wt', encoding='utf-8') as g:
                    g.write(s)
            r = parse(i, u, code, s); r['final_url'] = final; r['retry'] = True
            fo.write(json.dumps(r, ensure_ascii=False) + '\n'); fo.flush()
            if k % 50 == 0: log('ok', k, i, code, r.get('title'))
            k += 1
            time.sleep(max(0, 5.0 - (time.time() - t0)))
    log('done'); return 0


if __name__ == '__main__':
    sys.exit(main())
