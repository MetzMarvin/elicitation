#!/usr/bin/env python3
"""Print, for given marketplace listings, the evidence needed to write their ruling.
Usage: python ledgers/_creatio_mp_show.py /app/x /app/y ... [--figs]
"""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import _creatio_mp_rows as M  # noqa: E402

OUT = pathlib.Path(__file__).resolve().parent / "_creatio"
pages = json.loads((OUT / "mp_pages.json").read_text(encoding="utf-8"))
ctx = json.loads((OUT / "mp_figctx.json").read_text(encoding="utf-8"))

for link in sys.argv[1:]:
    if link.startswith("--"):
        continue
    p = pages.get(link)
    if not p or p.get("status") != "ok":
        print("=== %s  NOT CACHED" % link)
        continue
    b = re.sub(r"\s+", " ", M.body(p))
    print("\n=== %s | %s" % (link, p["title"]))
    print("TEXT: %s" % b[:900])
    for rx, lab in ((M.AI, "AI"), (M.PROC, "PROC")):
        seen = 0
        for m in re.finditer(rx, b, re.I):
            c = b[max(0, m.start() - 90):m.start() + 110]
            print("  %-4s %-22s ... %s" % (lab, m.group(0), c))
            seen += 1
            if seen >= 3:
                break
    figs = ctx.get(link) or []
    print("  FIGS: %s" % "; ".join(
        "%s%s[%s]" % (f["file"], ("/" + (f["alt"] or "")) if f.get("alt") else "",
                      (f.get("heading") or "")[:22]) for f in figs[:14]))
    if "--figs" in sys.argv:
        for f in figs:
            print("     %-42s under %-26s before: %s" % (f["file"][:42], (f.get("heading") or "")[:26],
                                                         (f.get("before") or "")[-150:]))
