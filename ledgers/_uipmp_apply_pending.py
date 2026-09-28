# Apply staged judgements written while Bash was unavailable (elicitation-7b, 2026-09-28).
# Resolves placeholders: "@SUMMARY" -> first <=25 words of the listing Summary; "@AIHIT:<kw>" -> 25-word window
# around the AI keyword hit; "@RECORD1733" -> record written here for n=1733. Idempotent per n (skips n already in ledger
# with the same verdict).
import json, os, re, subprocess, sys
ELI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
L = os.path.join(ELI, 'ledgers')
RAW = os.path.join(L, 'uipath-marketplace.raw')
scan = {}
for l in open(os.path.join(RAW, 'scan.jsonl'), encoding='utf-8'):
    r = json.loads(l)
    if r['http'] == 200: scan[r['n']] = r
last = {}
for l in open(os.path.join(L, 'uipath-marketplace.jsonl'), encoding='utf-8'):
    o = json.loads(l)
    if o.get('type') is None: last[o['n']] = o


def summ(n):
    m = re.search(r'\n\s*Summary\s*\n\s*(.+)', scan[n]['text'])
    return ' '.join(m.group(1).split()[:25])


def aihit(n, kw):
    t = ' '.join(scan[n]['text'].split())
    i = t.lower().find(kw.lower())
    w = t[max(0, i - 120):i + 120].split()[1:-1]
    k = next(j for j, x in enumerate(w) if kw.lower() in x.lower())
    return ' '.join(w[max(0, k - 12):k + 12])


def res(v, n):
    if v == '@SUMMARY': return summ(n)
    if isinstance(v, str) and v.startswith('@AIHIT:'): return aihit(n, v[7:])
    return v


# 1) record for n=1733 (render-type, via _uipmp_vidrec.py)
if last.get(1733, {}).get('verdict') != 'UNCERTAIN':
    vb = [{"n": 1733, "slug": "studio-web-twilio-ai-sms-salesforce-lead", "ai_quote": summ(1733), "bpmn_quote": summ(1733),
           "shows": "A Studio Web template: when a new Lead is created in Salesforce, send it an AI-generated SMS via Twilio (tags include 'openai', 'text generation').",
           "media_note": "The listing has no screenshots and no video; the template itself lives in Studio Web and was not opened (operator ruling 2026-09-28: opening creates a tenant draft).",
           "bpmn_ev": "none on the listing (0 images, 0 video); Studio Web workflow template, not opened",
           "q": "Studio Web workflow template (not a Maestro/BPMN template) not opened in Studio Web (operator ruling 2026-09-28: opening creates a tenant draft); the listing has no image. Is a Studio Web workflow in scope at all, and does its 'AI generated SMS' step count?",
           "jf": "listing GET html/1733.html.gz; 0 media, 0 video; Studio Web template not opened (operator ruling 2026-09-28)",
           "fn": "'AI generated SMS message' (tags 'openai', 'text generation')", "down": "SMS via Twilio to the new Lead",
           "inp": "new Lead record created in Salesforce",
           "notes": "Studio Web workflow templates are UiPath low-code workflows; whether they are BPMN was not verifiable without opening the template, which the operator ruled out. The PNG is an offline render of the archived listing text."}]
    open(os.path.join(RAW, 'vidrec_1733.json'), 'w', encoding='utf-8').write(json.dumps(vb, ensure_ascii=False))
    print(subprocess.run(['python', os.path.join(L, '_uipmp_vidrec.py'), '@' + os.path.join(RAW, 'vidrec_1733.json')], capture_output=True, text=True, encoding='utf-8').stdout)

# 2) plain rows
rows = []
for d in json.load(open(os.path.join(RAW, 'pending_rows1.json'), encoding='utf-8')):
    if d['n'] == 1733 or last.get(d['n'], {}).get('verdict') == d['verdict']: continue
    d = {k: res(v, d['n']) for k, v in d.items()}
    rows.append(d)
if rows:
    p = subprocess.run(['python', os.path.join(L, '_uipmp_row.py'), json.dumps(rows, ensure_ascii=False)], capture_output=True, text=True, encoding='utf-8')
    print(p.stdout, p.stderr[-800:])

# 3) diagram records
items = []
for d in json.load(open(os.path.join(RAW, 'diagrec_batch2.json'), encoding='utf-8')):
    if last.get(d['n'], {}).get('verdict') == 'UNCERTAIN': continue
    items.append({k: res(v, d['n']) for k, v in d.items()})
if items:
    open(os.path.join(RAW, 'diagrec_batch2_resolved.json'), 'w', encoding='utf-8').write(json.dumps(items, ensure_ascii=False))
    p = subprocess.run(['python', os.path.join(L, '_uipmp_diagrec.py'), '@' + os.path.join(RAW, 'diagrec_batch2_resolved.json')], capture_output=True, text=True, encoding='utf-8')
    print(p.stdout, p.stderr[-800:])
