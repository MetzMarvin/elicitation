# Record + offline-render capture + archive + ledger row for a video-only UNCERTAIN listing.
# usage: python _uipmp_vidrec.py @file.json   (list of {n, slug, ai_quote, bpmn_quote, shows, fn, down, data, ctrl, inp, guards})
import glob, gzip, json, os, re, struct, subprocess, sys
ELI = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C = os.path.join(ELI, 'corpus', 'uipath-marketplace')
scan = {}
for l in open(os.path.join(ELI, 'ledgers', 'uipath-marketplace.raw', 'scan.jsonl'), encoding='utf-8'):
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
    if d.get('png'):
        import shutil; shutil.copy(os.path.join(ELI, 'ledgers', 'uipath-marketplace.raw', 'media', d['png']), png)
    else:
        subprocess.run(['python', os.path.join(ELI, 'ledgers', '_uipmp_render.py'), str(n), png], check=True, capture_output=True)
    w = struct.unpack('>II', open(png, 'rb').read(24)[16:24])[0]
    open(os.path.join(C, base + '.page.html'), 'w', encoding='utf-8').write(
        gzip.open(os.path.join(ELI, 'ledgers', 'uipath-marketplace.raw', 'html', f'{n:04d}.html.gz'), 'rt', encoding='utf-8').read())
    vids = ', '.join('`' + v.replace('https://www.', '') + '`' for v in r['video'])
    q = d.get('q') or ("The listing's only possible diagram artefact is inside an embedded video that was not opened "
         "(operator no-media rule). Does the video show a BPMN process with an AI element, or should this listing be excluded?")
    md = f"""---
n: {n}
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: {json.dumps(r['title'], ensure_ascii=False)}
url: {r['url']}
accessed: 2026-09-28
verdict: UNCERTAIN
needs_human_ruling: true
question: {json.dumps(q)}
needs_visual_check: {'true' if d.get('nvc', True) else 'false'}
bpmn_evidence: {d.get('bpmn_ev', 'none on the listing (0 images); only artefact is an embedded YouTube video, not opened')}
bpmn_evidence_quote: {json.dumps(d['bpmn_quote'], ensure_ascii=False)}
ai_evidence: listing prose describes an AI/ML step in the automated process
ai_evidence_quote: {json.dumps(d['ai_quote'], ensure_ascii=False)}
artefacts:
  screenshot: {base}.png
  archive: {base}.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: {'original-asset' if d.get('png') else 'fullpage-screenshot'}
capture_quality: {d.get('cq', 'legible')}
capture_width_px: {w}
capture_method: {d.get('cm', 'offline headless-Edge render of the archived listing HTML (scripts, styles and video iframes stripped, so no YouTube request); the listing has no image asset to download')}
---

## What the page shows

{d['shows']} {d.get('media_note', 'The listing has no screenshots; it embeds one video (' + vids + ').')}

## Observations (description only, no interpretation)

- **AI activity - function:** {d.get('fn', NV)}
- **AI activity - element type:** {NV} (no diagram on the page)
- **Authority - downstream:** {d.get('down', NV)}
- **Authority - data:** {d.get('data', NV)}
- **Authority - control:** {d.get('ctrl', NV)}
- **Input provenance:** {d.get('inp', NV)}
- **Guards present:** {d.get('guards', NV)}
- **Prompt / model detail visible:** {d.get('model', 'none')}

## Notes for the researcher

{d.get('notes') or ('Artefact inside a video; not opened per operator instruction 2026-09-26. The PNG is an offline render of the archived listing text, not a diagram. The listing type is \"' + r['type'] + '\"; UiPath listings of this type ship Studio workflows, which are not BPMN, so the video most likely shows UiPath Studio or the vendor tool, but that was not verified.')}
"""
    open(os.path.join(C, base + '.md'), 'w', encoding='utf-8').write(md)
    row = {"n": n, "verdict": "UNCERTAIN", "judgment": True, "evidence": d['ai_quote'],
           "judged_from": d.get('jf') or f"listing GET html/{n:04d}.html.gz; 0 images; artefact inside a video; not opened per operator instruction 2026-09-26",
           "record": f"corpus/uipath-marketplace/{base}.md", "nvc": d.get('nvc', True), "nhr": True, "question": q}
    p = subprocess.run(['python', os.path.join(ELI, 'ledgers', '_uipmp_row.py'), json.dumps(row, ensure_ascii=False)],
                       capture_output=True, text=True, encoding='utf-8')
    print(base, w, p.stdout.strip(), p.stderr[-300:])
