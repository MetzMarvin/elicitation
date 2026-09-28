#!/usr/bin/env python3
"""Supersede ledger row n=68 of scheer-pas (worker elicitation-6f).

Row 68 (/academy/latest/preparations-ai-tutorial-1, corpus record 001) was written as
UNCERTAIN with a ruling question. The question is answered by the census protocol, which puts
this class of artefact deliberately in scope:

  "diagrams where the AI element is only visible as a task *property* or implementation
   binding, not as a distinct BPMN element type"   (prompts/02_source-census.md, l.44-47)

The binding itself is published by the vendor (corpus record 002, the same tutorial's
"Step 3: Integrating the Agent to the Process"), so record 001 is INCLUDE and the page needs
no human ruling. Row n=68 stays in the ledger for audit; the last row for an `n` wins
(tools/audit.py).

  python ledgers/_scheer_correct_001.py          # preview
  python ledgers/_scheer_correct_001.py --write  # append superseding row + header + footer
"""
import json
import pathlib
import sys

ELI = pathlib.Path(__file__).resolve().parents[1]
LEDGER = ELI / "ledgers" / "scheer-pas.jsonl"
TODAY = "2026-09-25"

CLAUSE = ("diagrams where the AI element is only visible as a task *property* or implementation "
          "binding, not as a distinct BPMN element type")
NOTE = ("Supersedes the UNCERTAIN row for record 001: the ruling question it carried is answered by "
        "the census protocol, which puts exactly this artefact class deliberately in scope - "
        "\"" + CLAUSE + "\" (prompts/02_source-census.md, \"Deliberately in scope\"). The BPMN "
        "diagram is genuine BPMN 2.0, its service task 'Analyze customer request' is bound to the "
        "AI agent, and that binding is published by the vendor on a sibling page of the same "
        "tutorial (corpus record 002, 'Step 3: Integrating the Agent to the Process'), so the "
        "AI element is documented, not inferred. Verdict INCLUDE, no human ruling needed.")

ROW_EXTRA = {"supersedes_row": True, "prior_verdict": "UNCERTAIN", "correction": "rule 3 clause",
             "judged_from": "page read + its figures looked at + protocol clause + record 002"}


def main():
    lines = LEDGER.read_text(encoding="utf-8").splitlines()
    header = footer = None
    rows = {}
    for line in lines:
        if not line.strip():
            continue
        o = json.loads(line)
        if o.get("type") == "header":
            header = o
        elif o.get("type") == "footer":
            footer = o
        else:
            rows[o["n"]] = o
    old = rows[68]
    row = dict(old)
    row.update({"verdict": "INCLUDE", "reason": None, "judgment": True, "evidence": CLAUSE,
                "note": NOTE, "needs_visual_check": False, "needs_human_ruling": False,
                "question": None, "duplicate_of": None, "accessed": TODAY})
    row.update(ROW_EXTRA)

    print("n=68  %s -> %s" % (old["verdict"], row["verdict"]))
    print("  url      : %s" % row["url"])
    print("  record   : %s" % row["record"])
    print("  evidence : %s" % row["evidence"])
    print("  ruling?  : needs_human_ruling=%s question=%r" % (row["needs_human_ruling"],
                                                              row["question"]))

    hdr = dict(header)
    hdr["note"] = (header.get("note", "") + " Correction (elicitation-6f, 2026-09-25): row n=68 "
                   "(record 001) was superseded from UNCERTAIN to INCLUDE - the delegated-binding "
                   "question it raised is answered by the census protocol's \"Deliberately in "
                   "scope\" clause and by record 002, which publishes the binding.")
    ftr = dict(footer)
    rows[68] = row
    vals = list(rows.values())
    ftr["include"] = sum(1 for r in vals if r["verdict"] == "INCLUDE")
    ftr["uncertain"] = sum(1 for r in vals if r["verdict"] == "UNCERTAIN")
    ftr["exclude"] = {c: sum(1 for r in vals if r.get("reason") == c) for c in
                      ("E0-no-artefact", "E1-not-bpmn", "E2-no-ai-element", "E3-duplicate")}
    ftr["blocked"] = sum(1 for r in vals if r["verdict"] == "BLOCKED")
    judged = [r for r in vals if r.get("judgment") is True]
    jx = [r for r in judged if r["verdict"] == "EXCLUDE"]
    ftr["judgement_rows"] = len(judged)
    ftr["judgment_exclusion_share"] = round(len(jx) / len(vals), 3)
    ftr["corrections_superseding_rows"] = 1
    print("footer: include=%d uncertain=%d exclude=%s blocked=%d share=%.3f"
          % (ftr["include"], ftr["uncertain"], ftr["exclude"], ftr["blocked"],
             ftr["judgment_exclusion_share"]))

    if "--write" not in sys.argv:
        print("preview only")
        return 0
    with LEDGER.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")
        fh.write(json.dumps(hdr, ensure_ascii=False) + "\n")
        fh.write(json.dumps(ftr, ensure_ascii=False) + "\n")
    print("appended 1 superseding row + header + footer")
    return 0


if __name__ == "__main__":
    sys.exit(main())
