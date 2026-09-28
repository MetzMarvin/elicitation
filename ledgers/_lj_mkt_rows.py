# -*- coding: utf-8 -*-
"""Exhaustive marketing-host rows: one ledger row for every enumerated
www.loyjoy.com URL (842), appended after the 16 already-judged artefact pages.

Verdicts come from the per-asset classification written by the visual sweep
(ledgers/_lj_mkt_assetclass.json) plus the page-level AI token scan."""
import io, json, os, re, collections

LED = 'ledgers/loyjoy.jsonl'
DATE = '2026-09-24'
DONE16 = {314, 734, 317, 737, 75, 497, 102, 524, 117, 538, 138, 559, 339, 759, 364, 784}

def load(p):
    b = open(p, 'rb').read()
    for enc in ('utf-8', 'cp1252', 'latin-1'):
        try:
            return b.decode(enc)
        except UnicodeDecodeError:
            pass
    return b.decode('utf-8', 'replace')

AI = re.compile(r'\bAI\b|\bKI\b|\bGPT\b|\bLLM\b|\bNLU\b|artificial intelligence|k(?:ü|u)nstliche'
                r'|generative|intelligen|agentic|ChatGPT|Claude|Copilot|machine learning', re.I)
JUNK = re.compile(r'Skip to main content|So funktioniert es|Einloggen|Book a demo|Sign in|Cookie'
                  r'|Newsletter|Hinweis zum Alter|On this page|\||^Previous |^Next ')

def page_bits(n):
    raw = load('ledgers/loyjoy.marketing/%03d.html' % n)
    body = re.sub(r'(?is)<(script|style|svg|noscript|head|header|nav|footer|aside)[^>]*>.*?</\1>', ' ', raw)
    t = re.sub(r'\s+', ' ', re.sub(r'(?s)<[^>]+>', ' ', body))
    t = re.sub(r'&[a-z#0-9]+;', ' ', t)
    t = re.sub(r'\s+', ' ', t)
    alts = ' '.join(re.findall(r'alt="([^"]*)"', raw))
    srcs = re.findall(r'(?:src|href)="(/[^"]+\.(?:webp|png|jpg|jpeg|gif|svg))"', raw)
    uniq = []
    for s in srcs:
        if s not in uniq:
            uniq.append(s)
    files = [s.split('/')[-1] for s in uniq]
    raster = [f for f in files if not f.lower().endswith('.svg')]
    hit = bool(AI.search(t)) or bool(AI.search(alts)) or bool(AI.search(' '.join(raster)))
    # quote: first sentence 7..45 words that is not chrome
    q = ''
    for s in re.split(r'(?<=[.!?]) ', t):
        s = s.strip()
        if not (20 <= len(s) <= 320) or JUNK.search(s):
            continue
        w = s.split()
        if 7 <= len(w) <= 45:
            q = ' '.join(w[:25])
            break
    if not q:
        q = ' '.join(t.split()[:20])
    m = re.search(r'<title[^>]*>(.*?)</title>', raw, re.S)
    title = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', m.group(1))).strip() if m else ''
    m = re.search(r'<h1[^>]*>(.*?)</h1>', raw, re.S)
    if m:
        h = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', m.group(1))).strip()
        if h:
            title = h
    return dict(text=t, title=title, quote=q, raster=raster, has_ai=hit,
                ai_terms=sorted(set(x.group(0) for x in AI.finditer(t + ' ' + alts + ' ' + ' '.join(raster))))[:6])

def short(f):
    return f.split('.')[0][:40]

def main():
    chk = json.load(io.open('ledgers/_lj_mkt_check.json', encoding='utf-8'))
    cls = json.load(io.open('ledgers/_lj_mkt_assetclass.json', encoding='utf-8'))
    rows = []
    n = 288
    stats = collections.Counter()
    for num, url, bpmn, ai, imgs in chk:
        if num in DONE16:
            continue
        n += 1
        b = page_bits(num)
        raster = [f for f in b['raster'] if not f.startswith('loyjoy.')]
        c = [cls.get(f, {}) for f in raster]
        diagrams = [f for f, x in zip(raster, c) if x.get('diagram')]
        ai_diag = [f for f, x in zip(raster, c) if x.get('diagram') and x.get('ai')]
        chat = [f for f, x in zip(raster, c) if x.get('chat')]
        figdesc = ', '.join(short(f) for f in raster[:6]) or 'none'
        if ai_diag:
            verdict, reason, judgment = 'INCLUDE', None, False
            ev = ('AI element inside a depicted process: figure(s) %s show a process diagram whose '
                  'elements include AI/GPT-named content; page text: "%s"' % (
                      ', '.join(short(f) for f in ai_diag), b['quote']))
            stats['include'] += 1
        elif diagrams:
            verdict, reason, judgment = 'EXCLUDE', 'E2-no-ai-element', bool(b['has_ai'])
            ev = ('the process figure(s) %s contain no AI/LLM element inside the process (AI wording '
                  'on the page: %s); page text: "%s"' % (
                      ', '.join(short(f) for f in diagrams),
                      ', '.join(b['ai_terms']) or 'none',
                      b['quote']))
        elif chat and not raster:
            verdict, reason, judgment = 'EXCLUDE', 'E1-not-bpmn', bool(b['has_ai'])
            ev = ('the artefact exists but is not BPMN 2.0 notation: the page\'s figure(s) %s are '
                  'chat-interface screenshots; page text: "%s"' % (
                      ', '.join(short(f) for f in chat), b['quote']))
        else:
            if not raster:
                verdict, reason, judgment = 'EXCLUDE', 'E0-no-artefact', False
                ev = ('no process artefact: the page carries no content image at all (only the shared '
                      'logo/icons); page text: "%s"' % b['quote'])
            else:
                verdict, reason, judgment = 'EXCLUDE', 'E0-no-artefact', False
                ev = ('no process artefact: the page\'s images are %s (hero art, product/UI screenshots '
                      'or photos - no process model); page text: "%s"' % (figdesc, b['quote']))
        row = {"n": n, "url": url, "title": b['title'] or url.rstrip('/').rsplit('/', 1)[-1][:80],
               "verdict": verdict}
        if reason:
            row["reason"] = reason
        row["judgment"] = judgment
        row["evidence"] = ev
        row["record"] = None
        row["needs_visual_check"] = False
        row["needs_human_ruling"] = False
        row["judged_from"] = "curl fetch, archived HTML (ledgers/loyjoy.marketing/%03d.html)" % num
        row["accessed"] = DATE
        rows.append(row)
    print('new marketing rows', len(rows), 'first n', rows[0]['n'], 'last n', rows[-1]['n'])
    print('INCLUDE rows:', stats['include'])
    with io.open(LED, 'a', encoding='utf-8') as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    # frontier: 272 docs + 842 marketing, in ledger order
    old = [l.strip() for l in io.open('ledgers/loyjoy.frontier.txt', encoding='utf-8') if l.strip()]
    docs = old[:272]
    mkt = [u for _, u, _, _, _ in chk]
    with io.open('ledgers/loyjoy.frontier.txt', 'w', encoding='utf-8') as f:
        for u in docs + mkt:
            f.write(u + '\n')
    print('frontier', len(docs + mkt))

if __name__ == '__main__':
    main()
