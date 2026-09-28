#!/usr/bin/env python3
"""Audit the Step 1 elicitation ledgers.

Run from anywhere:  python <elicitation>/tools/audit.py [source-slug ...]

Checks per source ledger (notes/elicitation/ledgers/<slug>.jsonl):
  * ledger is valid JSONL with a header
  * row count vs population_size and vs the frontier file
  * verdict / exclusion-code vocabulary
  * every row carries evidence
  * every INCLUDE/UNCERTAIN row has a record file and a screenshot on disk
  * judgement-exclusion share (the rows where a false negative can hide)
and prints the researcher's review worklist first.

Exit code 1 if any hard violation is found, so it can gate a census as "done".
"""

import json
import sys
from collections import Counter
from pathlib import Path

# tools/audit.py sits directly inside the elicitation folder in both layouts
# (thesis repo notes/elicitation/ and the standalone working copy).
ELI = Path(__file__).resolve().parents[1]
LEDGERS = ELI / "ledgers"
CORPUS = ELI / "corpus"

VERDICTS = {"INCLUDE", "UNCERTAIN", "EXCLUDE", "BLOCKED"}
CODES = {"E0-no-artefact", "E1-not-bpmn", "E2-no-ai-element", "E3-duplicate"}


def load(path):
    header, rows, footer, bad = None, [], None, []
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError as exc:
            bad.append(f"line {i}: invalid JSON ({exc.msg})")
            continue
        kind = obj.get("type")
        if kind == "header":
            header = obj
        elif kind == "footer":
            footer = obj
        else:
            rows.append((i, obj))
    # Corrections are appended, never rewritten: the last row for an `n` wins.
    latest = {}
    for i, obj in rows:
        latest[obj.get("n", ("line", i))] = (i, obj)
    superseded = len(rows) - len(latest)
    rows = sorted(latest.values(), key=lambda t: t[0])
    return header, rows, footer, bad, superseded


def audit(path):
    slug = path.stem
    header, rows, footer, problems, superseded = load(path)
    print(f"\n=== {slug} ===")
    if header is None:
        problems.append("no header line: population and enumeration method undocumented")
        header = {}

    pop = header.get("population_size")
    census = header.get("census", True)
    verdicts = Counter(r.get("verdict") for _, r in rows)
    codes = Counter(r.get("reason") for _, r in rows if r.get("verdict") == "EXCLUDE")
    judged = [r for _, r in rows if r.get("judgment") is True]
    judgement_exclusions = [r for r in judged if r.get("verdict") == "EXCLUDE"]

    print(f"enumeration : {header.get('enumeration_method', '(missing)')}")
    print(f"population  : {pop}  census={census}  rows={len(rows)}"
          + (f"  (+{superseded} superseded rows)" if superseded else ""))
    print("verdicts    : " + ", ".join(f"{k}={v}" for k, v in sorted(verdicts.items())))
    if codes:
        print("exclusions  : " + ", ".join(f"{k}={v}" for k, v in sorted(codes.items())))
    if rows:
        share = len(judgement_exclusions) / len(rows)
        print(f"judgement exclusions: {len(judgement_exclusions)} ({share:.1%}) "
              f"<- review these to catch false negatives")
        accepted = {}
        acc_file = ELI / "tools" / "accepted_shares.json"
        if acc_file.exists():
            accepted = json.loads(acc_file.read_text(encoding="utf-8")).get(slug) or {}
        if accepted and len(judgement_exclusions) <= accepted.get("max_exclusions", -1):
            print(f"  share above 10% accepted by the operator on {accepted.get('accepted')} "
                  f"(tools/accepted_shares.json)")
        elif share > 0.10:
            problems.append(
                f"judgement-exclusion share {share:.1%} exceeds 10%: the agent judged "
                "instead of collecting; re-examine those rows")

    frontier = LEDGERS / f"{slug}.frontier.txt"
    if frontier.exists():
        n_frontier = len([l for l in frontier.read_text(encoding="utf-8").splitlines() if l.strip() and not l.lstrip().startswith("#")])
        if n_frontier != len(rows):
            problems.append(f"frontier has {n_frontier} items but ledger has {len(rows)} rows")
    elif census:
        problems.append("no frontier file: enumeration cannot be verified")

    if census and isinstance(pop, int) and pop != len(rows):
        problems.append(f"population_size={pop} but {len(rows)} rows: census incomplete")

    for ln, r in rows:
        v, code = r.get("verdict"), r.get("reason")
        where = f"line {ln} (n={r.get('n')})"
        if v not in VERDICTS:
            problems.append(f"{where}: unknown verdict {v!r}")
        if not (r.get("evidence") or "").strip():
            problems.append(f"{where}: no verbatim evidence")
        if v == "EXCLUDE":
            if code not in CODES:
                problems.append(f"{where}: exclusion code {code!r} outside the closed list")
            if code == "E3-duplicate" and not r.get("duplicate_of"):
                problems.append(f"{where}: E3 without duplicate_of")
            if r.get("needs_visual_check"):
                problems.append(f"{where}: EXCLUDE with needs_visual_check (rule 5: unresolved "
                                "image means UNCERTAIN, never EXCLUDE)")
            jf = str(r.get("judged_from") or "").lower()
            if code == "E1-not-bpmn" and ("not opened" in jf or "no figure opened" in jf):
                problems.append(f"{where}: E1 on figures nobody looked at (name the notation only "
                                "after viewing; unviewed + no AI keyword is mechanical E2)")
        if v in {"INCLUDE", "UNCERTAIN"}:
            rec = r.get("record")
            if not rec:
                problems.append(f"{where}: {v} without a record path")
                continue
            recpath = ELI / rec
            if not recpath.exists():
                problems.append(f"{where}: record missing on disk: {rec}")
            else:
                text = recpath.read_text(encoding="utf-8", errors="replace")
                for field in ("url:", "accessed:", "bpmn_evidence", "ai_evidence",
                              "screenshot:", "capture_quality"):
                    if field not in text:
                        problems.append(f"{where}: record {recpath.name} lacks {field}")
                nnn = recpath.stem.split("_", 1)[0]
                shots = (list(recpath.parent.glob(nnn + "_*.png"))
                         + list(recpath.parent.glob(nnn + "_*.bpmn")))
                if not shots:
                    problems.append(f"{where}: no capture (.png or .bpmn) next to {recpath.name}")
                import re as _re
                m = _re.search(r"^capture_quality:\s*(\S+)", text, _re.M)
                if m and m.group(1) not in ("legible", "marginal", "poor", "null"):
                    problems.append(f"{where}: capture_quality {m.group(1)!r} not in legible|marginal|poor")
        if r.get("needs_human_ruling") and not (r.get("question") or "").strip():
            problems.append(f"{where}: needs_human_ruling without a question")

    # NNN is reserved for records: every NNN_ file must share its number with exactly one record.
    cdir = CORPUS / slug
    if cdir.is_dir():
        recs = Counter(p.name.split("_", 1)[0] for p in cdir.glob("[0-9][0-9][0-9]_*.md"))
        referenced = {Path(r.get("record")).name for _, r in rows if r.get("record")}
        for p in cdir.glob("[0-9][0-9][0-9]_*.md"):
            if p.name not in referenced:
                problems.append(f"corpus/{slug}/{p.name}: record not referenced by any current ledger row")
        for k, c in recs.items():
            if c > 1:
                problems.append(f"corpus/{slug}: {c} records share number {k}")
        for p in cdir.iterdir():
            k = p.name.split("_", 1)[0]
            if p.suffix != ".md" and k.isdigit() and k not in recs:
                problems.append(f"corpus/{slug}/{p.name}: NNN {k} has no record (raw evidence goes to ledgers/{slug}.raw/)")

    visual = [r for _, r in rows if r.get("needs_visual_check")]
    rulings = [r for _, r in rows if r.get("needs_human_ruling")]
    blocked = [r for _, r in rows if r.get("verdict") == "BLOCKED"]
    print(f"review queue: visual-check={len(visual)} rulings={len(rulings)} "
          f"blocked={len(blocked)}")
    if footer and footer.get("status") == "RESUME":
        print("status      : RESUME (census was interrupted, not finished)")
    elif footer is None:
        print("status      : no footer line (session may not have closed cleanly)")

    if problems:
        print("problems:")
        for p in problems:
            print(f"  - {p}")
    else:
        print("problems: none")
    return problems, judgement_exclusions, visual, rulings


def main():
    wanted = sys.argv[1:]
    ledgers = sorted(LEDGERS.glob("*.jsonl"))
    if wanted:
        ledgers = [p for p in ledgers if p.stem in wanted]
    if not ledgers:
        print(f"no ledgers found in {LEDGERS}")
        return 0

    total_problems, total_judged, total_visual, total_rulings = 0, 0, 0, 0
    for path in ledgers:
        problems, judged, visual, rulings = audit(path)
        total_problems += len(problems)
        total_judged += len(judged)
        total_visual += len(visual)
        total_rulings += len(rulings)

    n_records = sum(len(list((CORPUS / p.stem).glob("[0-9]*.md"))) for p in ledgers)
    print(f"\n=== overall ===\nsources={len(ledgers)} records={n_records} "
          f"judgement-exclusions={total_judged} visual-checks={total_visual} "
          f"rulings={total_rulings} problems={total_problems}")
    print("corpus scope backstop is 60 examples (method sec:method:stopping_rule)")
    return 1 if total_problems else 0


if __name__ == "__main__":
    sys.exit(main())
