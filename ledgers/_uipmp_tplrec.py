# Record writer for Maestro / agent templates that could not be opened in Studio Web
# (operator ruling 2026-09-28: opening creates/rewrites tenant drafts; no Studio Web).
# usage: python _uipmp_tplrec.py @file.json   items: {n, slug, media (optional file in raw/media or null),
#   bpmn_quote, ai_quote, shows, fn, down, data, ctrl, inp, guards, model, notes, jf, verdict (default UNCERTAIN),
#   question (default = ruling question), nvc (default true), cq}
import glob, gzip, json, os, struct, subprocess, sys
from PIL import Image
ELI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ELI, 'ledgers', 'uipath-marketplace.raw')
C = os.path.join(ELI, 'corpus', 'uipath-marketplace')
RULING_Q = ("Maestro/agent template not opened in Studio Web (operator ruling 2026-09-28: opening creates a tenant "
            "draft); task bindings not inspected. Does any task bind an agent/LLM?")
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
    png = os.path.join(C, base + '.png')
    if d.get('media'):
        im = Image.open(os.path.join(RAW, 'media', d['media'])); im.seek(0); im.convert('RGB').save(png)
        cs, cm = 'original-asset', 'python urllib GET of the original marketplace-cdn.uipath.com asset (cdn-cgi wrapper stripped)'
    else:
        subprocess.run(['python', os.path.join(ELI, 'ledgers', '_uipmp_render.py'), str(n), png], check=True, capture_output=True)
        cs, cm = 'fullpage-screenshot', 'offline headless-Edge render of the archived listing HTML (scripts, styles and video iframes stripped); the listing has no diagram image'
    w = struct.unpack('>II', open(png, 'rb').read(24)[16:24])[0]
    open(os.path.join(C, base + '.page.html'), 'w', encoding='utf-8').write(
        gzip.open(os.path.join(RAW, 'html', f'{n:04d}.html.gz'), 'rt', encoding='utf-8').read())
    q = d.get('question') or RULING_Q
    verdict = d.get('verdict', 'UNCERTAIN')
    vn = (' The page embeds ' + str(len(r['video'])) + ' YouTube video(s), not opened (operator no-media rule 2026-09-26).') if r['video'] else ''
    md = f"""---
n: {n}
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: {json.dumps(r['title'], ensure_ascii=False)}
url: {r['url']}
accessed: 2026-09-28
verdict: {verdict}
needs_human_ruling: true
question: {json.dumps(q, ensure_ascii=False)}
needs_visual_check: {'false' if d.get('nvc') is False else 'true'}
bpmn_evidence: {d.get('bpmn_ev', 'listing prose states the template is a Maestro process modelled in BPMN; the diagram itself is only in Studio Web, not opened')}
bpmn_evidence_quote: {json.dumps(d['bpmn_quote'], ensure_ascii=False)}
ai_evidence: {d.get('ai_ev', 'listing prose on agentic orchestration / agents; per-task Action bindings not inspected')}
ai_evidence_quote: {json.dumps(d['ai_quote'], ensure_ascii=False)}
artefacts:
  screenshot: {base}.png
  archive: {base}.page.html
  bpmn_xml: null
duplicate_of: null
access: free-account
capture_source: {cs}
capture_quality: {d.get('cq', 'marginal')}
capture_width_px: {w}
capture_method: {cm}; {w} px
---

## What the page shows

{d['shows']}{vn}

## Observations (description only, no interpretation)

- **AI activity - function:** {d.get('fn', NV)}
- **AI activity - element type:** {d.get('etype', NV + ' (per-task Action bindings live in Studio Web, not inspected)')}
- **Authority - downstream:** {d.get('down', NV)}
- **Authority - data:** {d.get('data', NV)}
- **Authority - control:** {d.get('ctrl', NV)}
- **Input provenance:** {d.get('inp', NV)}
- **Guards present:** {d.get('guards', NV)}
- **Prompt / model detail visible:** {d.get('model', 'none')}

## Notes for the researcher

{d.get('notes', '')} Studio Web inspection was stopped by operator ruling on 2026-09-28 because opening a
template or draft creates or rewrites tenant files; the July precedent study (notes/uipath-promotion-pattern/
analysis.md, marketplace-templates-editor/README.md) may already hold this template's binding count.
"""
    open(os.path.join(C, base + '.md'), 'w', encoding='utf-8').write(md)
    row = {"n": n, "verdict": verdict, "judgment": True, "evidence": d['ai_quote'], "judged_from": d['jf'],
           "record": f"corpus/uipath-marketplace/{base}.md", "nvc": d.get('nvc', True) is not False, "nhr": True, "question": q}
    p = subprocess.run(['python', os.path.join(ELI, 'ledgers', '_uipmp_row.py'), json.dumps(row, ensure_ascii=False)],
                       capture_output=True, text=True, encoding='utf-8')
    print(base, w, p.stdout.strip(), p.stderr[-300:])
