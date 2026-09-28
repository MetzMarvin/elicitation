#!/usr/bin/env python3
"""Download one marketplace figure at full size:  python ledgers/_creatio_mp_getfig.py /app/x <name-fragment>"""
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import _creatio_mp_sheets as S  # noqa: E402

OUT = pathlib.Path(__file__).resolve().parent / "_creatio"
pages = json.loads((OUT / "mp_pages.json").read_text(encoding="utf-8"))
for arg in sys.argv[1:]:
    pass
pairs = [(sys.argv[i], sys.argv[i + 1]) for i in range(1, len(sys.argv) - 1, 2)]
for link, frag in pairs:
    p = pages.get(link) or {}
    want = []
    for i in (p.get("imgs") or []):
        base = i["src"].split("/")[-1]
        if frag.lower() in base.lower():
            want.append((base, i["src"]))
    if not want:
        print("NO MATCH %s %s" % (link, frag))
    for base, src in want:
        print("%s  %s" % (base, S.cached_image(src)))
