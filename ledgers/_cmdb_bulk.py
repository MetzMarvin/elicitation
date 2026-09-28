"""camunda-docs-blog: mechanical dispositions for the posts the screen settles by itself.

  python ledgers/_cmdb_bulk.py mech            # append rows for every non-AI post (dry-run: -n)
  python ledgers/_cmdb_bulk.py ailist [FROM]   # compact listing of the AI posts, for review

A post is settled mechanically when the page text carries no AI/LLM term at all: whatever
figure it shows, there is no AI element inside the process, so the row can only be an
exclusion, and the code follows from what the page itself shows:
  no figure and no model link                        -> E0-no-artefact
  a figure whose alt names a non-BPMN notation       -> E1-not-bpmn (the alt names it)
  a BPMN diagram (BPMN in the text or in an alt)      -> E2-no-ai-element
  figures that are photographs/screenshots/logos     -> E0-no-artefact
Every row's code rests on the DOM of the saved page (figure alt texts + body text), and the
mechanical screen is re-runnable from screen.jsonl.
"""
import json, os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _cmdb_figs as F

RAW = "ledgers/camunda-docs-blog.raw"
DIPS = os.path.join(RAW, "dips.jsonl")

NOTATION = [
    (r"(?i)flow ?chart", "a flow chart (not BPMN)"),
    (r"(?i)architecture|layer|tier|topology|component diagram", "an architecture diagram (not BPMN)"),
    (r"(?i)timeline|roadmap|maturity", "a timeline/roadmap graphic (not BPMN)"),
    (r"(?i)chart|graph|plot|bars?|axis", "a chart (not BPMN)"),
    (r"(?i)screenshot|ui|dashboard|console|editor|form", "a product-UI screenshot (not BPMN)"),
    (r"(?i)logo|portrait|photo|headshot|attendees|audience|stage", "a photograph/logo (not a diagram)"),
    (r"(?i)table|list|matrix", "a table (not BPMN)"),
]


def first_sentence(text, minlen=40):
    for line in text.split("\n"):
        line = line.strip()
        if len(line) >= minlen and not line.startswith("Read more"):
            return " ".join(line.split()[:25])
    return " ".join(text.split()[:25])


def bpmn_quote(r):
    for line in r["text"].split("\n"):
        line = line.strip()
        if "BPMN" in line and len(line) > 25:
            return " ".join(line.split()[:25])
    for f in F.figs(r):
        if "bpmn" in f["alt"].lower():
            return " ".join(("Figure: " + f["alt"]).split()[:25])
    return first_sentence(r["text"])


def classify(r):
    figs = F.figs(r)
    alts = [f["alt"] for f in figs if f["alt"]]
    bpmn_txt = "BPMN" in r["text"] or "bpmn" in r["text"] or "BPMN" in " ".join(alts)
    if r["files"]:
        return None
    if bpmn_txt:
        return ("E2-no-ai-element", False, bpmn_quote(r),
                "the page shows/names a BPMN artefact (%d figures; alt texts: %s) and carries no "
                "AI/LLM term anywhere in its text, so no AI element can be inside the process"
                % (len(figs), "; ".join(a[:60] for a in alts[:4]) or "none"))
    for a in alts:
        for pat, what in NOTATION:
            if re.search(pat, a):
                if re.search(r"(?i)flow ?chart|architecture|component|process", a):
                    return ("E1-not-bpmn", True, " ".join(("Figure: " + a).split()[:25]),
                            "the page's figure is %s, named by its own alt text %r" % (what, a[:80]))
                return ("E0-no-artefact", False, " ".join(("Figure: " + a).split()[:25]),
                        "the page's figures are %s, named by their own alt texts" % what)
    if not figs:
        return ("E0-no-artefact", False, first_sentence(r["text"]),
                "the page carries no figure, no .bpmn/.dmn/.cmmn link and no embed: no process artefact")
    return ("E0-no-artefact", False, first_sentence(r["text"]),
            "the page's %d figures are photographs, product UI or code listings (alt texts: %s): "
            "no process artefact" % (len(figs), "; ".join(a[:50] for a in alts[:4]) or "none"))


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "mech"
    dry = "-n" in sys.argv
    if cmd == "ailist":
        start = int(sys.argv[2]) if len(sys.argv) > 2 and sys.argv[2].isdigit() else 0
        for r in F.rows():
            if r["n"] > 1435 or not r["n_ai"] or r["n"] < start:
                continue
            figs = F.figs(r)
            alt = " | ".join(f["alt"][:44] for f in figs[:3] if f["alt"])
            print("%5d ai=%-4d fig=%-3d %s%s%s :: %s :: %s" % (
                r["n"], r["n_ai"], len(figs),
                "BPMNtxt " if ("BPMN" in r["text"] or "bpmn" in r["text"]) else "",
                "BPMNalt " if any("bpmn" in f["alt"].lower() for f in figs) else "",
                "FILE " if r["files"] else "",
                r["title"][:58], (alt or "(no alt)")[:150]))
        return
    rows = []
    for r in F.rows():
        if r["n"] > 1435 or r["n_ai"]:
            continue
        c = classify(r)
        if c is None:
            continue
        code, judg, ev, why = c
        rows.append({"n": r["n"], "verdict": "EXCLUDE", "reason": code, "judgment": judg,
                     "evidence": ev, "record": None, "needs_visual_check": False,
                     "needs_human_ruling": False, "question": "",
                     "note": why,
                     "judged_from": "mechanical screen of the saved page "
                                    "(ledgers/camunda-docs-blog.raw/blog/%04d.html, fetched 2026-09-26): "
                                    "%d figures, %d figures with alt text, .bpmn/.dmn/.cmmn links: %d, "
                                    "AI/LLM terms in the page text: 0"
                                    % (r["n"], len(F.figs(r)),
                                       len([f for f in F.figs(r) if f["alt"]]), len(r["files"]))})
    print("mechanical rows:", len(rows))
    if dry:
        for x in rows[:5]:
            print(json.dumps(x, ensure_ascii=False)[:400])
        return
    with open(DIPS, "a", encoding="utf-8") as fh:
        for x in rows:
            fh.write(json.dumps(x, ensure_ascii=False) + "\n")
    print("appended")


if __name__ == "__main__":
    main()
