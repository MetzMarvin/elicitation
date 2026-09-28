# -*- coding: utf-8 -*-
"""OCR pass for the Flowable census.

This session's model cannot receive image content (Read on a PNG returns nothing,
verified with both this model and a vision-capable subagent), so the visual channel
is replaced by OCR of the downloaded assets: the labels drawn inside a diagram are
the evidence the method actually needs (element labels, task names, model names).

usage: python ledgers/_flw_ocr.py <itemlist.json> <out.json>
itemlist.json: [[page_url, img_url], ...]
Output: {img_url: {"labels": [str], "n": int, "size": [w,h], "pages": [..]}}
Resumable: existing out.json is loaded and only missing images are processed.
"""
import json
import os
import sys
import time

from PIL import Image
from rapidocr_onnxruntime import RapidOCR

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'flowable.raw')
CACHE = os.path.join(RAW, 'imgcache')


def cache_path(u):
    import re
    return os.path.join(CACHE, re.sub(r'[^A-Za-z0-9]', '_', u)[-140:])


def main():
    items = json.load(open(sys.argv[1], encoding='utf-8'))
    outpath = sys.argv[2]
    out = json.load(open(outpath, encoding='utf-8')) if os.path.exists(outpath) else {}
    pages = {}
    for p, u in items:
        pages.setdefault(u, []).append(p)
    todo = [u for u in pages if u not in out]
    print(f'items={len(pages)} done={len(out)} todo={len(todo)}', flush=True)
    ocr = RapidOCR()
    n = 0
    for u in todo:
        p = cache_path(u)
        rec = {'labels': [], 'n': 0, 'size': None, 'pages': pages[u][:4]}
        if not os.path.exists(p):
            rec['err'] = 'no-cache'
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
            rec['labels'] = labs
            rec['n'] = len(labs)
        except Exception as e:  # noqa: BLE001
            rec['err'] = f'{type(e).__name__}:{e}'
        out[u] = rec
        n += 1
        if n % 10 == 0:
            json.dump(out, open(outpath, 'w', encoding='utf-8'))
            print(f'  {n}/{len(todo)} {u.rsplit("/", 1)[-1][:44]} labels={rec["n"]}', flush=True)
    json.dump(out, open(outpath, 'w', encoding='utf-8'))
    print('DONE', len(out), flush=True)


if __name__ == '__main__':
    main()
