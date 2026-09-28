"""camunda-docs-blog: build ledgers/camunda-docs-blog.jsonl from the screen + dispositions.

Pipeline (mirrors the other pass-2 ledgers):
  ledgers/camunda-docs-blog.raw/screen.jsonl   one row per fetched post (text, imgs, files)
  ledgers/camunda-docs-blog.raw/dips.jsonl     append-only dispositions, last row per n wins
  -> ledgers/camunda-docs-blog.jsonl           header + one row per frontier item + footer

Usage:
  python ledgers/_cmdb_rows.py emit      # write the ledger
  python ledgers/_cmdb_rows.py check     # quote/coverage checks only
"""
import json, os, re, sys, collections

import _cmdb_verify as V

RAW = "ledgers/camunda-docs-blog.raw"
FRONTIER = "ledgers/camunda-docs-blog.frontier.txt"
LEDGER = "ledgers/camunda-docs-blog.jsonl"
ACCESSED = "2026-09-26"
CODES = ["E0-no-artefact", "E1-not-bpmn", "E2-no-ai-element", "E3-duplicate"]


def norm(s):
    return re.sub(r"\s+", " ", s or "").strip()


def load():
    frontier = []
    for l in open(FRONTIER, encoding="utf-8"):
        l = l.rstrip("\n")
        if not l:
            continue
        n, url = l.split("\t", 1)
        frontier.append((int(n), url.strip()))
    screen = {}
    p = os.path.join(RAW, "screen.jsonl")
    if os.path.exists(p):
        for l in open(p, encoding="utf-8"):
            try:
                r = json.loads(l)
            except Exception:
                continue
            screen[r["n"]] = r
    dips = {}
    p = os.path.join(RAW, "dips.jsonl")
    if os.path.exists(p):
        for l in open(p, encoding="utf-8"):
            l = l.strip()
            if not l:
                continue
            r = json.loads(l)
            dips[r["n"]] = r
    return frontier, screen, dips


def hay(s):
    """What a row's evidence may be quoted from: the saved page's text, the alt texts and
    captions of its figures, and the XML of any model it links - the same haystack the record
    verifier uses, so the two cannot disagree about what 'verbatim' means."""
    return V.haystack(s)


def check(frontier, screen, dips):
    bad = 0
    for n, d in sorted(dips.items()):
        s = screen.get(n)
        if s is None:
            if d.get("verdict") != "BLOCKED":
                print("!! n=%d has a disposition but no screen row" % n)
                bad += 1
            continue
        # both sides through the verifier's normaliser: it folds case and unicode, so a
        # quote is compared as words rather than as bytes
        q = V.norm(d.get("evidence"))
        if q and q not in hay(s):
            print("!! n=%d quote not found on the page: %r" % (n, d.get("evidence")[:70]))
            bad += 1
        v = d.get("verdict")
        if v == "EXCLUDE":
            if d.get("reason") not in CODES:
                print("!! n=%d EXCLUDE without a closed-list reason" % n)
                bad += 1
            if d.get("reason") == "E3-duplicate" and not d.get("duplicate_of"):
                print("!! n=%d E3 without duplicate_of" % n)
                bad += 1
            if d.get("needs_visual_check"):
                print("!! n=%d EXCLUDE carrying needs_visual_check" % n)
                bad += 1
        if v in ("INCLUDE", "UNCERTAIN"):
            rec = d.get("record") or ""
            text = ""
            if rec and os.path.exists(rec):
                text = open(rec, encoding="utf-8", errors="replace").read()
            for field in ("url:", "accessed:", "bpmn_evidence", "ai_evidence", "screenshot:", "capture_quality"):
                if field not in text:
                    print("!! n=%d record lacks %s" % (n, field))
                    bad += 1
        if d.get("needs_human_ruling") and not norm(d.get("question")):
            print("!! n=%d needs_human_ruling without a question" % n)
            bad += 1
    missing = [n for n, _ in frontier if n not in dips]
    print("checked %d dispositions, %d problems; %d frontier items still unjudged"
          % (len(dips), bad, len(missing)))
    if missing:
        print("first unjudged:", missing[:10])
    return bad


def emit(frontier, screen, dips):
    hdr = None
    p = os.path.join(RAW, "header.json")
    if os.path.exists(p):
        hdr = json.load(open(p, encoding="utf-8"))
    if hdr is None:
        print("no header.json - refusing to emit"); return
    lines = [hdr]
    counts = collections.Counter()
    codes = collections.Counter()
    judged = vis = rul = blocked = 0
    for n, url in frontier:
        d = dips.get(n)
        if d is None:
            continue
        s = screen.get(n, {})
        row = {"n": n, "url": url, "title": (s.get("title") or "")[:180],
               "verdict": d["verdict"], "reason": d.get("reason") or None,
               "judgment": bool(d.get("judgment")), "evidence": d.get("evidence"),
               "record": d.get("record") or None,
               "needs_visual_check": bool(d.get("needs_visual_check")),
               "needs_human_ruling": bool(d.get("needs_human_ruling")),
               "question": d.get("question") or None,
               "note": d.get("note") or None,
               "judged_from": d.get("judged_from") or None,
               "accessed": ACCESSED}
        if d["verdict"] == "EXCLUDE" and d.get("reason") == "E3-duplicate":
            row["duplicate_of"] = d.get("duplicate_of")
        if d["verdict"] == "BLOCKED":
            row["blocker"] = d.get("blocker")
        row = {k: v for k, v in row.items() if v is not None or k in
               ("n", "url", "verdict", "judgment", "needs_visual_check", "needs_human_ruling")}
        lines.append(row)
        counts[d["verdict"]] += 1
        if d["verdict"] == "EXCLUDE":
            codes[d["reason"]] += 1
        if d.get("judgment"):
            judged += 1
        if d.get("needs_visual_check"):
            vis += 1
        if d.get("needs_human_ruling"):
            rul += 1
        if d["verdict"] == "BLOCKED":
            blocked += 1
    rows = len(lines) - 1
    flips = None
    p = os.path.join(RAW, "self_audit.json")
    if os.path.exists(p):
        flips = json.load(open(p, encoding="utf-8")).get("flips")
    foot = {"type": "footer", "date_end": ACCESSED, "rows": rows,
            # template keys (templates/ledger.md) first, then the detail this source needed
            "include": counts["INCLUDE"], "uncertain": counts["UNCERTAIN"],
            "exclude": dict(codes), "blocked": counts["BLOCKED"],
            "judgment_exclusion_share": round(
                sum(1 for l in lines[1:] if l["judgment"] and l["verdict"] == "EXCLUDE") / rows, 4)
            if rows else 0,
            "self_audit_flips": flips,
            "status": "COMPLETE" if rows >= hdr.get("population_size", 0) else "RESUME",
            "population_size": hdr.get("population_size"),
            "verdicts": dict(counts), "exclusions": dict(codes),
            "judged": judged,
            "needs_visual_check": vis, "needs_human_ruling": rul}
    lines.append(foot)
    with open(LEDGER, "w", encoding="utf-8") as fh:
        for l in lines:
            fh.write(json.dumps(l, ensure_ascii=False) + "\n")
    print("wrote %s: %d rows" % (LEDGER, rows))
    print(json.dumps(foot, ensure_ascii=False))


if __name__ == "__main__":
    f, s, d = load()
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    if cmd == "check":
        check(f, s, d)
    else:
        check(f, s, d)
        emit(f, s, d)
