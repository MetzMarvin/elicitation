"""camunda-docs-blog: the native-resolution pass over every `needs_visual_check` row.

The flag means "I read the figure at full resolution and still could not settle it". A
contact-sheet thumbnail read at 340 px does not qualify: the figure has to be opened at
native width first (02b). This script keeps that pass resumable.

  python ledgers/_cmdb_vis.py remaining            # the rows still to look at, next first
  python ledgers/_cmdb_vis.py show N [N..]         # the capture path(s) and page facts for those rows
  python ledgers/_cmdb_vis.py put N                # one row's disposition, read from stdin (JSON)
  python ledgers/_cmdb_vis.py build                # append the dispositions to raw/dips.jsonl

Every disposition is appended to ledgers/camunda-docs-blog.raw/visual-progress.jsonl the
moment it is made, so a fresh agent can resume from that file alone.
"""
import json, os, sys

RAW = "ledgers/camunda-docs-blog.raw"
WORK = os.path.join(RAW, "visual-worklist.json")
PROG = os.environ.get("CMDB_PROG") or os.path.join(RAW, "visual-progress.jsonl")
DIPS = os.path.join(RAW, "dips.jsonl")


def stdin_json():
    """A disposition can be piped in on stdin or, safer against shell quoting, read from a
    file path given as the second argument."""
    for a in sys.argv[2:]:
        if os.path.exists(a):
            return json.load(open(a, encoding="utf-8"))
    return json.load(sys.stdin)


def work():
    return json.load(open(WORK, encoding="utf-8"))


def done():
    """Every disposition logged so far, from the main log and any per-worker log beside it."""
    import glob
    out = {}
    for path in sorted(glob.glob(os.path.join(RAW, "visual-progress*.jsonl"))):
        for line in open(path, encoding="utf-8"):
            line = line.strip()
            if line:
                r = json.loads(line)
                out[r["n"]] = r
    return out


def remaining(cmd_nums=None):
    d = done()
    rows = [w for w in work() if w["n"] not in d]
    if cmd_nums:
        rows = [w for w in rows if w["n"] in cmd_nums]
    return rows


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "remaining"
    nums = [int(a) for a in sys.argv[2:] if a.isdigit()]
    if cmd == "remaining":
        d, w = done(), work()
        print("%d of %d rows still to look at" % (len([x for x in w if x["n"] not in d]), len(w)))
        for x in remaining(nums):
            print("  %5d  %-9s n_ai=%-4s %s" % (x["n"], x["verdict"], x["n_ai"], x["record"]))
        return
    if cmd == "show":
        screen = {json.loads(l)["n"]: json.loads(l)
                  for l in open(os.path.join(RAW, "screen.jsonl"), encoding="utf-8")}
        for x in work():
            if x["n"] in nums:
                s = screen[x["n"]]
                print("n=%d  %s  (%s)" % (x["n"], s["title"], x["verdict"]))
                print("   png: %s" % x["png"])
                print("   url: %s" % s["url"])
                print("   n_ai=%d  alts: %s" % (s["n_ai"], [a[:70] for a in
                      [i.get("alt") or "" for i in s.get("imgs") or []] if a][:4]))
        return
    if cmd == "put":
        rec = stdin_json()
        rec.setdefault("at", "2026-09-26")
        with open(PROG, "a", encoding="utf-8", newline="\n") as fh:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print("logged n=%s -> %s%s" % (rec["n"], rec["verdict"], rec.get("reason") or ""))
        return
    if cmd == "putauto":
        # the common case: the verdict is unchanged, so the row may keep the record's own
        # verified-verbatim quote as its evidence; only the disposition and the note are new
        import _cmdb_verify as V
        rec = stdin_json()
        n = rec["n"]
        rows = json.load(open(os.path.join(RAW, "records.json"), encoding="utf-8"))
        path = rows.get(str(n))
        fm = V.frontmatter(path)[0] if path else {}
        if rec.get("evidence") is None:
            rec["evidence"] = (fm.get("ai_evidence_quote") if rec["verdict"] != "EXCLUDE"
                               else fm.get("bpmn_evidence_quote")) or fm.get("bpmn_evidence_quote")
        rec["record"] = path if rec["verdict"] != "EXCLUDE" else None
        if rec["verdict"] == "UNCERTAIN":
            rec.setdefault("question", fm.get("question"))
        rec.setdefault("needs_visual_check", rec["verdict"] == "UNCERTAIN")
        rec.setdefault("at", "2026-09-26")
        with open(PROG, "a", encoding="utf-8", newline="\n") as fh:
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print("logged n=%s -> %s%s | evidence: %s" % (n, rec["verdict"], rec.get("reason") or "",
                                                      (rec.get("evidence") or "")[:70]))
        return
    if cmd == "brief":
        # one small text brief per row still to look at, so a worker opens a page's facts
        # (url, alts, the record's verified quotes, every AI sentence on the page) without
        # having to run a script per row; the figure itself is then read natively.
        import re
        screen = {json.loads(l)["n"]: json.loads(l)
                  for l in open(os.path.join(RAW, "screen.jsonl"), encoding="utf-8")}
        rows = json.load(open(os.path.join(RAW, "records.json"), encoding="utf-8"))
        import _cmdb_verify as V
        bdir = os.path.join(RAW, "visual-briefs")
        os.makedirs(bdir, exist_ok=True)
        todo = remaining(nums)
        for x in todo:
            s = screen[x["n"]]
            fm = {}
            if rows.get(str(x["n"])):
                fm = V.frontmatter(rows[str(x["n"])])[0]
            txt = re.sub(r"\s+", " ", s.get("text") or "")
            sents = [q.strip() for q in re.split(r"(?<=[.!?])\s+", txt)
                     if re.search(r"\b(AI|LLM|GPT|agent|agentic|model|prompt|machine learning|ML)\b", q, re.I)]
            L = ["# n=%d  %s  (current verdict: %s)" % (x["n"], x["title"], x["verdict"]),
                 "url: %s" % s["url"], "figure: %s" % x["png"],
                 "record: %s" % (x["record"] or "(none)"),
                 "page AI-word count: %d" % (s.get("n_ai") or 0),
                 "record bpmn_evidence_quote: %s" % (fm.get("bpmn_evidence_quote") or ""),
                 "record ai_evidence_quote: %s" % (fm.get("ai_evidence_quote") or ""),
                 "", "## figure alt texts on the page"]
            for i in (s.get("imgs") or []):
                if i.get("alt"):
                    L.append("- %s" % i["alt"][:200])
            L += ["", "## sentences on the page mentioning AI terms (up to 14)"]
            for q in sents[:14]:
                L.append("- %s" % q[:400])
            open(os.path.join(bdir, "%d.md" % x["n"]), "w", encoding="utf-8",
                 newline="\n").write("\n".join(L) + "\n")
        print("wrote %d briefs to %s" % (len(todo), bdir))
        return
    if cmd == "build":
        d = done()
        rows = json.load(open(os.path.join(RAW, "records.json"), encoding="utf-8"))
        recs = {int(k): v for k, v in rows.items()}
        n = 0
        with open(DIPS, "a", encoding="utf-8", newline="\n") as fh:
            for x in sorted(d.values(), key=lambda r: r["n"]):
                row = {"n": x["n"], "verdict": x["verdict"], "reason": x.get("reason") or None,
                       "judgment": bool(x.get("judgment")), "evidence": x.get("evidence"),
                       "record": x.get("record") or recs.get(x["n"]),
                       "needs_visual_check": bool(x.get("needs_visual_check")),
                       "needs_human_ruling": x["verdict"] == "UNCERTAIN",
                       "question": x.get("question"), "note": x.get("note"),
                       "judged_from": x.get("judged_from") or
                       "native-resolution read of the record's captured figure, "
                       "ledgers/camunda-docs-blog.raw/visual-progress.jsonl",
                       "supersedes_row": True}
                fh.write(json.dumps({k: v for k, v in row.items() if v is not None or k == "n"},
                                    ensure_ascii=False) + "\n")
                n += 1
        print("appended %d superseding dispositions" % n)
        return
    print(__doc__)


if __name__ == "__main__":
    main()
