# Diagram record writer for uipath-marketplace listings whose own images carry a process diagram.
# usage: python _uipmp_diagrec.py @file.json
# item keys: n, slug, media (file in raw/media), crop [x0,y0,x1,y1] (optional, saved 3x as *_diagram-crop-3x.png),
#   verdict (UNCERTAIN|INCLUDE), question, nvc (bool), cq (legible|marginal|poor), bpmn_ev, bpmn_quote, ai_ev, ai_quote,
#   shows, fn, etype, down, data, ctrl, inp, guards, model, notes, jf
import glob, gzip, json, os, struct, subprocess, sys
from PIL import Image
ELI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ELI, 'ledgers', 'uipath-marketplace.raw')
C = os.path.join(ELI, 'corpus', 'uipath-marketplace')
scan = {}
for l in open(os.path.join(RAW, 'scan.jsonl'), encoding='utf-8'):
    r = json.loads(l)
    if r['http'] == 200: scan[r['n']] = r
NV = 'not visible on the page'
arg = sys.argv[1]
items = json.loads(open(arg[1:], encoding='utf-8').read() if arg.startswith('@') else arg)
for d in items:
    n = d['n']; r = scan[n]
    nnn = '%03d' % (max([int(os.path.basename(p)[:3]) for p in glob.glob(os.path.join(C, '[0-9][0-9][0-9]_*.md'))] + [0]) + 1)
    base = f"{nnn}_{d['slug']}"
    im = Image.open(os.path.join(RAW, 'media', d['media'])); im.seek(0); im = im.convert('RGB')
    im.save(os.path.join(C, base + '.png'))
    w = im.width
    crop_note = ''
    if d.get('crop'):
        c = im.crop(tuple(d['crop'])); c = c.resize((c.width * 3, c.height * 3), Image.LANCZOS)
        c.save(os.path.join(C, base + '_diagram-crop-3x.png'))
        crop_note = f"; a 3x LANCZOS crop of the diagram region is saved as {base}_diagram-crop-3x.png ({c.width} px)"
    open(os.path.join(C, base + '.page.html'), 'w', encoding='utf-8').write(
        gzip.open(os.path.join(RAW, 'html', f'{n:04d}.html.gz'), 'rt', encoding='utf-8').read())
    vids = r['video']
    vnote = (' The page also embeds ' + str(len(vids)) + ' YouTube video(s), not opened (operator no-media rule 2026-09-26).') if vids else ''
    md = f"""---
n: {n}
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: {json.dumps(r['title'], ensure_ascii=False)}
url: {r['url']}
accessed: 2026-09-28
verdict: {d.get('verdict', 'UNCERTAIN')}
needs_human_ruling: {'true' if d.get('question') else 'false'}
question: {json.dumps(d['question'], ensure_ascii=False) if d.get('question') else 'null'}
needs_visual_check: {'true' if d.get('nvc') else 'false'}
bpmn_evidence: {d['bpmn_ev']}
bpmn_evidence_quote: {json.dumps(d['bpmn_quote'], ensure_ascii=False)}
ai_evidence: {d['ai_ev']}
ai_evidence_quote: {json.dumps(d['ai_quote'], ensure_ascii=False)}
artefacts:
  screenshot: {base}.png
  archive: {base}.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: {d.get('cq', 'marginal')}
capture_width_px: {w}
capture_method: python urllib GET of the original marketplace-cdn.uipath.com asset (cdn-cgi resize wrapper stripped); {w} px is the native size{crop_note}
---

## What the page shows

{d['shows']}{vnote}

## Observations (description only, no interpretation)

- **AI activity - function:** {d.get('fn', NV)}
- **AI activity - element type:** {d.get('etype', NV)}
- **Authority - downstream:** {d.get('down', NV)}
- **Authority - data:** {d.get('data', NV)}
- **Authority - control:** {d.get('ctrl', NV)}
- **Input provenance:** {d.get('inp', NV)}
- **Guards present:** {d.get('guards', NV)}
- **Prompt / model detail visible:** {d.get('model', 'none')}

## Notes for the researcher

{d.get('notes', '')}
"""
    open(os.path.join(C, base + '.md'), 'w', encoding='utf-8').write(md)
    row = {"n": n, "verdict": d.get('verdict', 'UNCERTAIN'), "judgment": True, "evidence": d['ai_quote'] if d['ai_quote'] in ' '.join(r['text'].split()) else d['bpmn_quote'],
           "judged_from": d['jf'], "record": f"corpus/uipath-marketplace/{base}.md", "nvc": bool(d.get('nvc')),
           "nhr": bool(d.get('question'))}
    if d.get('question'): row['question'] = d['question']
    p = subprocess.run(['python', os.path.join(ELI, 'ledgers', '_uipmp_row.py'), json.dumps(row, ensure_ascii=False)],
                       capture_output=True, text=True, encoding='utf-8')
    print(base, w, p.stdout.strip(), p.stderr[-400:])
