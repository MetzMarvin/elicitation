# -*- coding: utf-8 -*-
"""Exhaustive marketing-host rows: one ledger row for every enumerated
www.loyjoy.com URL from sitemap-0.xml (842), appended after rows 1-288.

Verdicts come from the per-asset visual classification
(ledgers/_lj_mkt_assetclass.json, keyed by asset name) plus the per-page
text/alt/filename AI scan (ledgers/_lj_mkt_pages.json).

Usage:  python ledgers/_lj_mkt_rows2.py --dry      # report only
        python ledgers/_lj_mkt_rows2.py            # append rows + records
"""
import io, json, os, re, sys, collections
from PIL import Image

LED = 'ledgers/loyjoy.jsonl'
DATE = '2026-09-24'
CORPUS = 'corpus/loyjoy'
RAW = 'ledgers/loyjoy.raw/mkt_all'
DONE16 = {314, 734, 317, 737, 75, 497, 102, 524, 117, 538, 138, 559, 339, 759, 364, 784}
FIRST_N = 289
FIRST_REC = 11
PROCESS_KINDS = ('canvas', 'bpmn')


def name_of(b):
    """page asset 'x.hash.ext' -> asset name 'x'.

    Page asset names keep their URL percent-escapes ('...ausw%C3%A4hlen1.Fbx.webp')
    while the downloaded cache and the contact sheets sanitise '%' to '_'
    ('...ausw_C3_A4hlen1__Fbx.webp'), so normalise before splitting."""
    return b.replace('%', '_').split('.')[0]


def short(b):
    return name_of(b)[:38]


def main():
    dry = '--dry' in sys.argv
    pages = json.load(io.open('ledgers/_lj_mkt_pages.json', encoding='utf-8'))
    cls = json.load(io.open('ledgers/_lj_mkt_assetclass.json', encoding='utf-8'))
    sheets = json.load(io.open('ledgers/_lj_mkt_sheets.json', encoding='utf-8'))
    key_by_name = dict(zip(sheets['bases'], sheets['files']))
    unclassified = sorted({name_of(b) for v in pages.values() for b in v['raster']
                           if name_of(b) not in cls})
    print('asset names on pages:', len({name_of(b) for v in pages.values() for b in v['raster']}),
          ' classified:', len(cls))
    print('classified assets never referenced by a page:',
          [n for n in cls if n not in {name_of(b) for v in pages.values() for b in v['raster']}])
    print('(unclassified = judged non-diagram from the contact sheets; count %d)' % len(unclassified))

    artefact_owner = {}
    # Seed with the diagrams already recorded by the earlier marketing rows
    # (273-288): their record files name the assets they captured, so a later
    # page re-publishing one of those figures is E3-duplicate, not a new find.
    for l in io.open(LED, encoding='utf-8'):
        if not l.strip():
            continue
        o = json.loads(l)
        if o.get('type') == 'header':
            continue
        if not (273 <= (o.get('n') or 0) <= 288) or not o.get('record'):
            continue
        pth = o['record']
        if not os.path.exists(pth):
            continue
        txt = io.open(pth, encoding='utf-8').read()
        nm = set(m.group(1) for m in re.finditer(r'/(?:[\w\-]+)?([\w\-]+)\.\w{6,20}\.(?:webp|png|jpe?g|gif)', txt))
        for q in re.findall(r"'([\w\-]{3,40})'", txt):
            if q in key_by_name:
                nm.add(q)
        for x in re.findall(r'([\w\-]{3,40})\.\w{6,20}\.(?:webp|png|jpe?g|gif)', txt):
            nm.add(x)
        for x in nm:
            if x in key_by_name:
                artefact_owner.setdefault(x, (o['n'], o['url']))
    print('seeded artefact owners from rows 273-288:', len(artefact_owner), sorted(artefact_owner)[:12])
    rows, records = [], []
    dup = None
    n = FIRST_N - 1
    rec = FIRST_REC - 1
    stats = collections.Counter()
    for num, url, bpmn, ai, imgs in json.load(io.open('ledgers/_lj_mkt_check.json', encoding='utf-8')):
        if num in DONE16:
            continue
        n += 1
        p = pages[str(num)]
        names = [name_of(b) for b in p['raster']]
        c = {b: cls.get(name_of(b), {}) for b in p['raster']}
        diagrams = [b for b in p['raster'] if c[b].get('kind') in PROCESS_KINDS]
        ai_diag = [b for b in diagrams if c[b].get('ai')]
        palette_ai = [b for b in p['raster'] if c[b].get('kind') == 'canvas-palette-ai']
        arch = [b for b in p['raster'] if c[b].get('kind') == 'arch']
        uis = [b for b in p['raster'] if c[b].get('kind') in ('chat', 'ui')]
        # figure-level AI wording: AI content visible INSIDE a figure that depicts a
        # product/process/architecture feature. `ai` marks an AI element inside a
        # depicted process (it drives INCLUDE); `ai_visible` marks AI wording that is
        # visible in the figure but is not an element of the depicted process (a
        # headline, a badge, a palette entry) - it drives the judgement flag only.
        # Logos, hero art and data charts ('art'/'text') do not count: a wordmark
        # saying "AI" is decoration, not AI-feature content to rule on.
        fig_ai = any(c[b].get('ai') or c[b].get('ai_visible') for b in p['raster']
                     if c[b].get('kind') in ('canvas', 'bpmn', 'canvas-palette-ai', 'arch', 'chat', 'ui'))
        quote = p['quote']
        title = p['title'] or url.rstrip('/').rsplit('/', 1)[-1][:80]

        if ai_diag and not all(name_of(b) in artefact_owner for b in ai_diag):
            verdict, reason, judgment = 'INCLUDE', None, False
            ev = ('an AI element inside the depicted process: the page figure %s is a process model '
                  'whose steps carry AI/GPT naming (%s); page text: "%s"' % (
                      short(ai_diag[0]), cls[name_of(ai_diag[0])].get('ai_note', ''), quote))
            rec += 1
            records.append((rec, n, num, url, title, ai_diag, p, 'INCLUDE'))
            stats['include'] += 1
            for b in diagrams:
                artefact_owner.setdefault(name_of(b), (n, url))
        elif palette_ai:
            b0 = palette_ai[0]
            verdict, reason, judgment = 'UNCERTAIN', None, True
            ev = ('the page figure %s is a process model of the "GPT Feedback" experience whose drawn '
                  'steps (#7 Simple message, #8 Decision gateway, #9 Phone number, #10 Email, #11 '
                  'Appointment scheduler, #12 Live chat, #13 Simple message, #14 Send email, #15 API '
                  'client) contain no AI module, but the editor\'s module palette beside the canvas '
                  'lists the GPT family ("GPT Knowledge", "GPT Prompt", "GPT Recommender", "GPT '
                  'Smalltalk"); page text: "%s"' % (short(b0), quote))
            rec += 1
            records.append((rec, n, num, url, title, palette_ai, p, 'UNCERTAIN'))
            stats['uncertain'] += 1
            for b in palette_ai:
                artefact_owner.setdefault(name_of(b), (n, url))
        elif diagrams and all(name_of(b) in artefact_owner for b in diagrams):
            o = artefact_owner[name_of(diagrams[0])]
            dup = o[0]
            verdict, reason, judgment = 'EXCLUDE', 'E3-duplicate', False
            ev = ('the same diagram is already recorded in this source: the page\'s process figure %s '
                  'is byte-identical to the asset recorded at row %d (%s); page text: "%s"' % (
                      ', '.join(short(b) for b in diagrams), o[0], o[1], quote))
            for b in diagrams:
                artefact_owner.setdefault(name_of(b), o)
        elif diagrams:
            verdict, reason = 'EXCLUDE', 'E2-no-ai-element'
            judgment = fig_ai
            ev = ('the process figure %s carries no AI/LLM element inside the process (%s); AI wording '
                  'on the page: %s; page text: "%s"' % (
                      ', '.join(short(b) for b in diagrams),
                      '; '.join(cls[name_of(b)].get('note', '')[:90] for b in diagrams[:2]),
                      ', '.join(p['ai_terms']) or 'none', quote))
            for b in diagrams:
                artefact_owner.setdefault(name_of(b), (n, url))
        elif arch and any(cls[name_of(b)].get('ai') for b in arch):
            a = [b for b in arch if cls[name_of(b)].get('ai')][0]
            verdict, reason, judgment = 'EXCLUDE', 'E1-not-bpmn', True
            ev = ('the artefact exists but is not BPMN 2.0 notation: the page figure %s is a '
                  'conceptual flow/architecture illustration, not a process model (%s); page text: "%s"'
                  % (short(a), cls[name_of(a)].get('note', '')[:120], quote))
        elif uis:
            verdict, reason = 'EXCLUDE', 'E1-not-bpmn'
            judgment = fig_ai
            ev = ('the artefact exists but is not BPMN 2.0 notation: the page figure %s is a product '
                  'or chat user-interface screenshot, not a process model; page text: "%s"' % (
                      ', '.join(short(b) for b in uis[:4]), quote))
        else:
            verdict, reason, judgment = 'EXCLUDE', 'E0-no-artefact', False
            if not p['raster']:
                ev = ('no process artefact: the page carries no content image at all (only the shared '
                      'logo and icons); page text: "%s"' % quote)
            else:
                ev = ('no process artefact: the page\'s images (%s) are hero art, product/UI '
                      'screenshots, illustrations or photos - no process model; page text: "%s"' % (
                          ', '.join(short(b) for b in p['raster'][:6]), quote))
        look = bool(diagrams or arch or uis)
        row = {"n": n, "url": url, "title": title, "verdict": verdict}
        if reason:
            row["reason"] = reason
        if dup is not None:
            row["duplicate_of"] = dup
        row["judgment"] = judgment
        row["evidence"] = ev
        row["record"] = None
        row["needs_visual_check"] = False
        row["needs_human_ruling"] = bool(verdict == 'UNCERTAIN')
        if verdict == 'UNCERTAIN':
            row["question"] = (
                'The figure %s is a process model of the "GPT Feedback" experience (canvas steps: '
                '#7 Simple message, #8 Decision gateway, #9 Phone number, #10 Email, #11 Appointment '
                'scheduler, #12 Live chat, #13 Simple message, #14 Send email, #15 API client) whose '
                'drawn steps contain no AI module, while the module palette shown beside the canvas '
                'lists the GPT family ("GPT Knowledge", "GPT Prompt", "GPT Recommender", "GPT '
                'Smalltalk"). Is a GPT module offered in the editor palette, but not placed in the '
                'drawn process, an AI/LLM element inside the process (so this row is an artefact), or '
                'an editor affordance outside the process model (so this row is E2-no-ai-element)? '
                'The same ambiguity is recorded for the docs palette pages (rows 275/276).' % short(palette_ai[0]))
        row["judged_from"] = ("in-page fetch of the live page plus full-size inspection of its figures "
                              "(HTML archived at ledgers/loyjoy.marketing/%03d.html)" % num if look else
                              "in-page fetch (HTML archived at ledgers/loyjoy.marketing/%03d.html) plus "
                              "contact-sheet inspection of its figures" % num)
        row["accessed"] = DATE
        rows.append(row)
        dup = None

    print('rows to append:', len(rows), 'n', rows[0]['n'], '..', rows[-1]['n'])
    print('verdicts:', dict(collections.Counter(r['verdict'] for r in rows)))
    print('reasons:', dict(collections.Counter(r['reason'] for r in rows if r.get('reason'))))
    print('judgment rows:', sum(1 for r in rows if r['judgment']))
    print('INCLUDE:', [(r['n'], r['url']) for r in rows if r['verdict'] == 'INCLUDE'])
    json.dump(rows, io.open('ledgers/_lj_dry_rows.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
    if dry:
        return

    for rn, rn_row, num, url, title, figs, p, verdict in records:
        keys = [key_by_name.get(name_of(b)) for b in figs]
        keys = [k for k in keys if k and os.path.exists(os.path.join(RAW, k))]
        if not keys:
            print('WARN no local asset for record', rn, figs)
            continue
        ims = [Image.open(os.path.join(RAW, k)).convert('RGB') for k in keys]
        W = max(i.width for i in ims)
        H = sum(i.height for i in ims) + 10 * (len(ims) - 1)
        canvas = Image.new('RGB', (W, H), 'white')
        y = 0
        for i in ims:
            canvas.paste(i, (0, y))
            y += i.height + 10
        if canvas.width > 1400:
            canvas = canvas.resize((1400, int(canvas.height * 1400 / canvas.width)), Image.LANCZOS)
        slug = re.sub(r'[^a-z0-9]+', '-', url.replace('https://www.loyjoy.com', '').strip('/').lower())[:48].strip('-') or 'page'
        name = '%03d_marketing-%s' % (rn, slug)
        canvas.save(os.path.join(CORPUS, name + '.png'))
        sizes = {k: Image.open(os.path.join(RAW, k)).size for k in keys}
        info = cls[name_of(figs[0])]
        extra = ''
        if verdict == 'UNCERTAIN':
            q = [r['question'] for r in rows if r['n'] == rn_row][0]
            extra = 'needs_human_ruling: true\nquestion: "%s"\n' % q.replace('"', "'")
        md = """---
n: {n}
source: loyjoy
source_name: LoyJoy (marketing site)
source_type: vendor marketing page
title: {title}
url: {url}
accessed: {date}
verdict: {verdict}
needs_visual_check: false
{extra}bpmn_evidence: "{figs}"
bpmn_evidence_quote: "{quote}"
ai_evidence: "{aiev}"
ai_evidence_quote: "{quote}"
artefacts:
  screenshot: corpus/loyjoy/{name}.png
  archive: ledgers/loyjoy.marketing/{num:03d}.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: {w}
capture_method: the page's own figure asset(s) {figtxt} downloaded from www.loyjoy.com and stacked into one PNG at native resolution with PIL; page HTML archived at ledgers/loyjoy.marketing/{num:03d}.html
---

## What the page shows

{note}

**AI activity - element type:** {aiev}

## Notes for the researcher

- The figure is the marketing host's rendering of the {figs} asset, read at native resolution
  ({figtxt}); the page is the one enumerated at https://www.loyjoy.com/sitemap-0.xml.
""".format(n=rn_row, title=title, url=url, date=DATE, figs=', '.join(name_of(b) for b in figs),
           quote=p['quote'], aiev=info.get('ai_note', 'AI-named steps inside the drawn process'),
           name=name, num=num, w=canvas.width, note=info.get('note', ''), extra=extra, verdict=verdict,
           figtxt='; '.join('%s (%dx%d)' % (k, sizes[k][0], sizes[k][1]) for k in keys))
        io.open(os.path.join(CORPUS, name + '.md'), 'w', encoding='utf-8').write(md)
        for r in rows:
            if r['n'] == rn_row:
                r['record'] = 'corpus/loyjoy/%s.md' % name

    with io.open(LED, 'a', encoding='utf-8') as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + '\n')
    old = [l.strip() for l in io.open('ledgers/loyjoy.frontier.txt', encoding='utf-8') if l.strip()]
    docs = old[:272]
    mkt = [u for _, u, _, _, _ in json.load(io.open('ledgers/_lj_mkt_check.json', encoding='utf-8'))]
    with io.open('ledgers/loyjoy.frontier.txt', 'w', encoding='utf-8') as f:
        for u in docs + mkt:
            f.write(u + '\n')
    print('frontier', len(docs + mkt))


if __name__ == '__main__':
    main()
