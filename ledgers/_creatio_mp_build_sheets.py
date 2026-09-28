#!/usr/bin/env python3
"""Rebuild the marketplace contact sheets at a higher density (the candidate set grew to 156 listings)."""
import json
import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import _creatio_mp_sheets as S  # noqa: E402

S.PER_SHEET, S.COLS, S.CW, S.CH = 56, 8, 240, 195
sel = S.collect()
(S.OUT / "mp_figsel.json").write_text(json.dumps(sel, indent=1, ensure_ascii=False), encoding="utf-8")
print("figures selected:", len(sel), flush=True)
for p, a, b in S.sheets(sel):
    print("  %s  (figures %d-%d)" % (p, a, b), flush=True)
