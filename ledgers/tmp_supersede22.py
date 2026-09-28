"""Corrected second pass: same 22 superseding rows, with an honest qualifier.

The qualifier must not claim raw frames exist for every recording: the on-disk frame dirs
cover 18 of the 20 recordings that were inspected before the operator's ruling, so the
note says what was actually done (inspected earlier the same day) and points at the raw
evidence directory generically.
"""
import json, os

RAW = "ledgers/trisotech.raw"
live = json.load(open(os.path.join(RAW, "video_live22.json"), encoding="utf-8"))

# slugs judged from the recording earlier on 2026-09-26, before the operator's ruling
inspected = set()
for line in open(os.path.join(RAW, "video_disp.jsonl"), encoding="utf-8"):
    r = json.loads(line)
    if r.get("supersedes"):
        continue
    inspected.add(r["key"])
inspected.add("optimizing-preoperative-assessments")

NOTE = "artefact inside a video; video not opened per operator instruction 2026-09-26"
QUAL = (" (this recording was inspected earlier the same day, before that instruction; whatever "
        "was captured then stays as raw evidence under ledgers/trisotech.raw/video/ for the "
        "human visual check)")
RULE = ("; source ruling 2026-09-26 (operator, relayed by elicitation-5a): recordings are not an "
        "admissible evidence source, so this row is UNCERTAIN + needs_visual_check and rests only "
        "on what the host page itself shows")

rows = []
for slug, r in sorted(live.items()):
    base = (r.get("note") or "").strip()
    note = (base + " " if base else "") + NOTE + (QUAL if slug in inspected else "")
    rows.append({
        "key": slug,
        "verdict": "UNCERTAIN",
        "code": "",
        "judgment": True,
        "record": r.get("record"),
        "capture": None,
        "needs_visual_check": True,
        "needs_human_ruling": False,
        "question": "",
        "evidence": r.get("evidence"),
        "note": note,
        "judged_from": (r.get("judged_from") or "").rstrip(". ") + RULE,
        "supersedes": "pass-2 video verdict",
    })

with open(os.path.join(RAW, "video_disp.jsonl"), "a", encoding="utf-8") as fh:
    for row in rows:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")
print("appended", len(rows), "corrected rows; inspected set:", len(inspected))
print(sorted(inspected))
