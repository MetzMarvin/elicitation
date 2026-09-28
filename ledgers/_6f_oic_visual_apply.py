#!/usr/bin/env python3
"""Append the visual-pass superseding rows for oracle-oic (worker elicitation-6f, 2026-09-24).

Corrections are appended, never rewritten: each new row repeats the `n` it corrects and
carries "supersedes_row": true. audit.py takes the last row per n.
"""
import json
import pathlib

ELI = pathlib.Path(__file__).resolve().parents[1]
LEDGER = ELI / "ledgers" / "oracle-oic.jsonl"
DECISIONS = ELI / "ledgers" / "_6f_oic_visual_decisions.json"
RAW = ELI / "ledgers" / "oracle-oic.raw"
CORPUS = ELI / "corpus" / "oracle-oic"
TODAY = "2026-09-24"

# last row per n, from the existing ledger
rows = []
for line in LEDGER.read_text(encoding="utf-8").splitlines():
    line = line.strip()
    if not line:
        continue
    obj = json.loads(line)
    if obj.get("type") in ("header", "footer"):
        continue
    rows.append(obj)
last = {}
for r in rows:
    if "n" in r:
        last[r["n"]] = r

decisions = json.loads(DECISIONS.read_text(encoding="utf-8"))["rows"]

new_rows = []
moved = []

for key in sorted(decisions, key=int):
    n = int(key)
    d = decisions[key]
    old = last[n]
    row = {
        "n": n,
        "url": old["url"],
        "title": old.get("title"),
        "verdict": "EXCLUDE",
        "reason": d["code"],
        "judgment": d["judgment"],
        "evidence": old.get("evidence"),
        "visual_evidence": d["visual"],
        "artifact_named": d["named"],
        "record": None,
        "needs_visual_check": False,
        "needs_human_ruling": False,
        "question": None,
        "duplicate_of": None,
        "accessed": TODAY,
        "supersedes_row": True,
        "note": old.get("note"),
    }
    if d.get("q2"):
        row["note"] = (
            "Q2 closed by the visual pass of 2026-09-24 (elicitation-6f): the figure named above is "
            "not BPMN 2.0 and the AI capability on the page is delivered as a native action inside "
            "Oracle Integration's proprietary flow notation, so E1-not-bpmn is the verdict and the "
            "open question is withdrawn. "
        ) + (old.get("note") or "")
    else:
        row["note"] = (
            "Visual pass 2026-09-24 (elicitation-6f): the capture staged next to this row was opened "
            "at native resolution and is not a BPMN 2.0 model; see visual_evidence for what it is. "
            "Record and captures moved out of corpus/ to ledgers/oracle-oic.raw/ (an EXCLUDE carries "
            "no record; see audit.py's own note that raw evidence goes to ledgers/<slug>.raw/). "
        ) + (old.get("note") or "")
    new_rows.append(row)

    # move the record + its captures out of corpus/
    nnn = d["nnn"]
    RAW.mkdir(exist_ok=True)
    for p in sorted(CORPUS.glob(nnn + "_*")):
        target = RAW / p.name
        p.replace(target)
        moved.append(p.name)

# the anchor post: the visual pass confirms the BPMN panel, so needs_visual_check is withdrawn
anchor = last[9]
new_rows.append({
    "n": 9,
    "url": anchor["url"],
    "title": anchor.get("title"),
    "verdict": "INCLUDE",
    "reason": None,
    "judgment": False,
    "evidence": anchor.get("evidence"),
    "visual_evidence": (
        "figure 3 'The same invoice process before and after' was opened at native resolution "
        "(1440x968) and the 'Before' panel is a real BPMN 2.0 model: a start event circle and a thick "
        "end event circle, two lanes ('AP lane', 'Approver lane'), tasks rounded rectangles ('receive', "
        "'extract', 'validate vendor', '3-way match', 'post', 'pay', 'clerk resolves', 'manager', "
        "'controller'), and two gateway diamonds labelled 'ok?' and '>10k?', with dashed sequence flows "
        "carrying the exception path. The 'After' panel of the same figure is not BPMN: it is an "
        "architecture diagram ('MCP App in the chat client', 'AP agent', 'MCP Gateway', then six tiles "
        "'Integration: submit', 'Integration: match', 'Decisions', 'Knowledge Base', 'HITL', "
        "'Integration: post'). Figure 1 ('Deterministic' / 'Probabilistic') is a stylised sequence "
        "illustration, not BPMN: 'receive -> validate -> agent: resolve -> approve -> post' plus a "
        "dashed 'exception queue' box, and 'agent follows the procedure -> receive validate approve "
        "post'. Figure 2 is an architecture box diagram."
    ),
    "record": "corpus/oracle-oic/004_the-future-of-oic-process-automation.md",
    "needs_visual_check": False,
    "needs_human_ruling": False,
    "question": None,
    "duplicate_of": None,
    "accessed": TODAY,
    "supersedes_row": True,
    "note": (
        "Visual pass 2026-09-24 (elicitation-6f) confirms the anchor: the page publishes a genuine "
        "BPMN 2.0 process model and an AI element in the ruled sense (agent as a step / agent holding "
        "control, Gate 1 ruling B3). Note for the abstraction step, description only: inside figure 3 "
        "the AI element sits in the 'After' panel and in the prose, not in the 'Before' BPMN panel. "
    ) + (anchor.get("note") or ""),
})

with LEDGER.open("a", encoding="utf-8") as fh:
    for row in new_rows:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")

print("appended superseding rows:", len(new_rows))
print("moved out of corpus/:", len(moved))
for name in moved:
    print("   ", name)
