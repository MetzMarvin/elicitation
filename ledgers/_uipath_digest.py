# -*- coding: utf-8 -*-
"""Text digest of the UiPath Maestro crawl, for page-by-page judging.

CLAUDE.md prefers textual/DOM evidence over the picture; this source's figure
alt text is descriptive English written by the vendor ("BPMN diagram of the invoice
processing process showing all tasks, gateways, and flow paths"), so the alt text
decides many calls before any image is opened.

usage: python ledgers/_uipath_digest.py <mode>
  figs   page + every figure (file stem, size hint, alt) - the triage list
  ai     page + AI keyword hits with context (the pages needing a ruling)
  bpmn   page + figures whose alt names BPMN, plus <pre> blocks and model files
  files  page + downloadable model files / inline svg counts
"""
import io, json, os, re, sys

RAW = 'ledgers/uipath-maestro-docs.raw'
PREFIX = '/maestro/automation-cloud/latest'
BPMN_ALT = re.compile(r'bpmn|process diagram|diagram of the|gateway|pool|lane|subprocess',
                      re.I)


def stem(src):
    return re.sub(r'^\d+-', '', os.path.basename(src or '')).replace('.webp', '')


def main():
    mode = (sys.argv[1] if len(sys.argv) > 1 else 'figs')
    scan = json.load(io.open(os.path.join(RAW, 'scan.json'), encoding='utf-8'))
    for i, p in enumerate(sorted(scan), 1):
        v = scan[p]
        if v.get('err'):
            print('%d %s ERR %s' % (i, p, v['err']))
            continue
        imgs = [im for im in (v.get('imgs') or []) if im.get('src')]
        pre = v.get('pre') or []
        files = v.get('files') or []
        if mode == 'figs':
            if not imgs:
                continue
            print('%d %s  [%s]' % (i, p, v.get('t')))
            for im in imgs:
                print('    %-46s %s' % (stem(im['src'])[:46], (im.get('alt') or im.get('cap') or '')[:150]))
        elif mode == 'ai':
            if not v.get('ai'):
                continue
            print('%d %s  [%s]  imgs=%d' % (i, p, v.get('t'), len(imgs)))
            seen = set()
            for h in v['ai'][:10]:
                k = h['ctx'][:45]
                if k in seen:
                    continue
                seen.add(k)
                print('    AI[%s] %s' % (h['kw'], h['ctx'][:190]))
        elif mode == 'bpmn':
            hits = [im for im in imgs if BPMN_ALT.search(im.get('alt') or '')]
            if not hits and not files:
                continue
            print('%d %s  [%s]' % (i, p, v.get('t')))
            for im in hits:
                print('    FIG %-42s %s' % (stem(im['src'])[:42], (im.get('alt') or '')[:140]))
            for f in files:
                print('    FILE %s' % f)
            for q in pre[:2]:
                if re.search(r'<(?:bpmn:)?\w*(?:Task|Event|Gateway|process)\b', q):
                    print('    PRE %s' % re.sub(r'\s+', ' ', q)[:220])
        elif mode == 'files':
            if not files and not v.get('svg'):
                continue
            print('%d %s  [%s] svg=%s files=%s' % (i, p, v.get('t'), v.get('svg'), files))


if __name__ == '__main__':
    main()
