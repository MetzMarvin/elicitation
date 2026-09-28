#!/usr/bin/env python3
"""Figures whose vendor file name or section heading itself suggests a process diagram."""
import json
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import _creatio_mp_sheets as S  # noqa: E402

NAME = re.compile(r"bpmn|process|workflow|diagram|scheme|flow|chart|designer|automation|architect"
                  r"|journey|map|tree|route|steps?", re.I)
HEAD = re.compile(r"process|workflow|diagram|flow|automation|business process|bpmn|designer", re.I)
figs = json.loads((pathlib.Path(__file__).resolve().parent / "_creatio" / "mp_figctx.json")
                  .read_text(encoding="utf-8"))
for link in sorted(figs):
    for f in figs[link]:
        if S.NOISE.search(f["file"]):
            continue
        if NAME.search(f["file"]) or HEAD.search(f.get("heading") or ""):
            print("%-58s %-38s under %-28s before: %s" % (
                link[:58], f["file"][:38], (f.get("heading") or "")[:28],
                re.sub(r"\s+", " ", (f.get("before") or ""))[-90:]))
