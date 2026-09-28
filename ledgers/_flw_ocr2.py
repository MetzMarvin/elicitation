# -*- coding: utf-8 -*-
"""Supplementary OCR pass (marketing / blog / training figures).

The first pass covered the docs figures and one marketing shard. This pass covers
the remaining non-chrome figures on the pages that mention AI, i.e. exactly the
pages where a "does this figure show a BPMN process?" question can change a verdict.

usage: python ledgers/_flw_ocr2.py <itemlist.json> <lo> <hi> <out.json>
Downloads any missing asset into flowable.raw/imgcache first (same cache key as
_flw_sheets.py / _flw_ocr.py), then OCRs slice [lo,hi) with RapidOCR.
Resumable: existing out.json is loaded and only missing images are processed.
"""
import json
import os
import re
import sys
import time
import urllib.request

from PIL import Image
from rapidocr_onnxruntime import RapidOCR

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, 'flowable.raw')
CACHE = os.path.join(RAW, 'imgcache')
UA = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/124.0 Safari/537.36 (research; master-thesis elicitation, read-only)'}


def cache_path(u):
    return os.path.join(CACHE, re.sub(r'[^A-Za-z0-9]', '_', u)[-140:])


def fetch(u):
    p = cache_path(u)
    if os.path.exists(p) and os.path.getsize(p) > 0:
        return p
    try:
        req = urllib.request.Request(u, headers=UA)
        with urllib.request.urlopen(req, timeout=40) as r:
            data = r.read()
    except Exception as e:  # noqa: BLE001
        open(p + '.fail', 'w').write(f'{u}\n{e}\n')
        return None
    open(p, 'wb').write(data)
    time.sleep(0.3)
    return p


def main():
    items = json.load(open(sys.argv[1], encoding='utf-8'))
    lo, hi = int(sys.argv[2]), int(sys.argv[3])
    outpath = sys.argv[4]
    os.makedirs(CACHE, exist_ok=True)
    pages = {}
    for p, u in items[lo:hi]:
        pages.setdefault(u, []).append(p)
    out = json.load(open(outpath, encoding='utf-8')) if os.path.exists(outpath) else {}
    todo = [u for u in pages if u not in out]
    print(f'slice={lo}:{hi} imgs={len(pages)} done={len(out)} todo={len(todo)}', flush=True)
    ocr = RapidOCR()
    n = 0
    for u in todo:
        rec = {'labels': [], 'n': 0, 'size': None, 'pages': pages[u][:4]}
        p = fetch(u)
        if not p:
            rec['err'] = 'fetch-failed'
            out[u] = rec
            continue
        try:
            im = Image.open(p)
            rec['size'] = [im.width, im.height]
            if im.width < 900:
                f = max(1, min(4, round(900 / max(im.width, 1))))
                im = im.resize((im.width * f, im.height * f), Image.LANCZOS)
            import numpy as np
            r, _ = ocr(np.array(im.convert('RGB')))
            labs = []
            for item in (r or []):
                if isinstance(item, (list, tuple)) and len(item) >= 2 and isinstance(item[1], str):
                    t = item[1].strip()
                    if t:
                        labs.append(t)
            rec['labels'], rec['n'] = labs, len(labs)
        except Exception as e:  # noqa: BLE001
            rec['err'] = f'{type(e).__name__}:{e}'
        out[u] = rec
        n += 1
        if n % 10 == 0:
            json.dump(out, open(outpath, 'w', encoding='utf-8'))
            print(f'  {n}/{len(todo)} labels={rec["n"]} {u.rsplit("/", 1)[-1][:40]}', flush=True)
    json.dump(out, open(outpath, 'w', encoding='utf-8'))
    print('DONE', len(out), flush=True)


if __name__ == '__main__':
    main()
