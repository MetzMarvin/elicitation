#!/usr/bin/env python3
"""Build the scheer-pas ledger from the crawled page cache.

  python ledgers/_scheer_build.py --survey   # what the screen fires on, page by page (writes
                                             #   nothing)
  python ledgers/_scheer_build.py --write    # write ledgers/scheer-pas.jsonl + .frontier.txt

Population order is the page trees' own order (space by space, page by page), so row n = the
n-th item of the frontier and of the population.

Screen: a page is *diagram-flagged* if any of its figures has a diagram-shaped attachment name
(DIAGRAM_NAME) or if its article prose carries a process-model token (PROC).

  * diagram-flagged pages  -> row derived from the site-wide sweep's classification of that
                             page's diagram-named figures (FIGCLASS below): a real BPMN model
                             gives E2 / UNCERTAIN, a proprietary execution model gives E1, UI
                             screenshots give E0. `judgment` is True where a diagram was rejected
                             (that is where a false negative can hide), False for E0-by-screen.
  * every other page       -> mechanical E0-no-artefact row naming exactly what the screen saw.

Hand-written per-page rulings in `_scheer_write.RULINGS` take precedence over the derived ones
(the source's AI-tutorial subtree, whose pages were read individually).
"""
import json
import pathlib
import re
import sys

ELI = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ELI / "ledgers"))
import _scheer_rows as S  # noqa: E402
import _scheer_write as W  # noqa: E402
from _scheer_figclass import FIGCLASS  # noqa: E402

OUT = W.OUT
PAGES = W.PAGES
TODAY = W.TODAY
SPACES = ["academy", "administration", "analyzer", "api-management", "bpaas", "bridge",
          "business-modeler", "designer", "getting-started", "help", "installation-guides",
          "pas-code", "process-mining", "release-notes"]

# --- the site-wide sweep of diagram-named figures ----------------------------------------------
# FIGCLASS (ledgers/_scheer_figclass.py) records, per attachment name, what the sweep sheets showed
# the figure to be: "bpmn" = a process model in the Designer's BPMN editor, "exec" = a proprietary
# xUML activity / behaviour diagram, "ui" = a Designer or web UI screenshot, "doc" = a non-UI
# illustration. Each page's row below is derived from it and cites the names.

# --- calibration of the screen ------------------------------------------------------------------
# The mechanical exclusions claim "no process artefact on this page". That claim is measured, not
# assumed: a deterministic every-k-th sample of exactly those pages (figures, but no diagram-shaped
# attachment name and no process token in the prose) has all its figures downloaded and looked at
# (ledgers/_scheer_audit.py). Numbers below are filled in from that pass.
AUDIT_SAMPLE = {
    "method": ("deterministic every-k-th sample of the pages excluded mechanically by the screen; "
               "ALL their figures downloaded (ledgers/_scheer_audit.py) and tiled in contact "
               "sheets (ledgers/_scheer/au_s0..s3.png), to test the screen's blind spot: a "
               "diagram behind a UI-ish attachment name on a page that never names a process"),
    "sample_step": 9, "candidate_pages": 389,
    "pages_looked_at": 40, "figures_looked_at": 228, "figures_sampled": 230,
    "diagrams_found": 7, "diagram_pages": 5, "bpmn_diagrams_found": 0,
    "diagram_finds": (
        "7 diagram figures on 5 pages, none of them BPMN 2.0, so the screen's blind spot for "
        "*BPMN* artefacts is 0 in this sample: /academy/latest/building-a-new-service-structure-md18 "
        "(rename_gettitleservice_1.png: xUML implementation diagram), "
        "/business-modeler/latest/panels (Pannels_Overview.png, Closing_Pannels.png: Business "
        "Modeler canvas with an event-driven process chain), /designer/latest/adapters "
        "(connector_adapter.png: architecture/integration illustration), "
        "/designer/latest/classtoxml (class_address_xml_mapping.png, grafik-20240729-090728.png: "
        "UML class diagrams), /designer/latest/creating-an-implementation-factory "
        "(implementation_factory.png: UML class diagram). All 5 pages are re-coded from E0 to "
        "E1-not-bpmn in _scheer_write.RULINGS, with the notation named; none of them mentions AI."),
    "failed_fetches": ("2 of the 230 sampled figures could not be fetched (connection reset, both "
                       "on installation-guides pages); they are counted as not looked at."),
    "sheet": "ledgers/_scheer/au_s0.png .. au_s3.png (228 tiles) + au_z1.png (zoom of the 10 "
             "diagram candidates)",
    "read": "2026-09-25",
}

FIGURES_LOOKED = {
    "in_scope_ai_subtree_contact_sheets": 75,
    "sweep_diagram_named_figures": 748,
    "sweep_unique_by_content": 662,
    "ai_mentioning_pages_pass": 264,
    "audit_sample": 228,
    "note": ("The four passes are separate lenses, so their counts overlap and are not added: "
             "748 diagram-named (suspect) figure attachments site-wide, 662 of them unique by "
             "content, all classified in sweep sheets (_scheer_figs2.py, _scheer_figclass.py); "
             "75 figures of the source's AI tutorial + AI reference subtree read in contact "
             "sheets; 264 figures of the 53 AI-mentioning pages outside RULINGS (the mechanical "
             "screen's blind spot, looked at 2026-09-25 -> records/row changes in the rulings); "
             "228 figures of the 40-page audit sample of the mechanically excluded pages."),
}


def records():
    idx = json.loads((OUT / "index.json").read_text(encoding="utf-8"))
    order = []
    for space in SPACES:
        for path, meta in idx.items():
            if meta.get("space") == space:
                order.append((path, meta))
    return order


def html_of(path):
    f = PAGES / (path.strip("/").replace("/", "__") + ".html")
    return f.read_text(encoding="utf-8", errors="replace") if f.exists() else None


def first_sentence(b):
    for s in re.split(r"(?<=[.!?])\s|\n", b):
        s = " ".join(s.split())
        if len(s.split()) >= 5:
            w = s.split()
            return " ".join(w[:25]) + (" ..." if len(w) > 25 else "")
    return " ".join(b.split()[:25])


def fig_name(f):
    return f["src"].split("/")[-1].split("?")[0]


def screen(path):
    t = html_of(path)
    if t is None:
        return None
    b = S.body(t)
    fs = S.figs(t)
    suspect = [fig_name(f) for f in fs if re.search(S.DIAGRAM_NAME, fig_name(f), re.I)]
    proc = re.search(S.PROC, b, re.I)
    ai = re.search(S.AI, b, re.I)
    return {"body": b, "figs": [fig_name(f) for f in fs], "suspect": suspect,
            "proc": proc.group(0) if proc else None, "ai": bool(ai),
            "flagged": bool(suspect) or bool(proc) or bool(ai),
            "words": len(b.split()), "first": first_sentence(b),
            "proc_quote": S.quote(b, S.PROC), "ai_quote": S.quote(b, S.AI)}


def base_row(n, path, meta, sc, **extra):
    row = {"n": n, "verdict": "EXCLUDE", "reason": "E0-no-artefact", "judgment": False,
           "evidence": sc["first"], "note": "", "url": meta["url"], "title": meta["title"],
           "duplicate_of": None, "accessed": TODAY, "surface": meta["space"], "record": None,
           "needs_visual_check": False, "needs_human_ruling": False, "question": None,
           "judged_from": "scheer-page-screen"}
    row.update(extra)
    return row


def mechanical_row(n, path, meta, sc):
    if not sc["figs"]:
        saw = "no figure at all (0 <img> in the page's article region)"
    else:
        saw = ("%d figure(s), none of whose attachment names names a diagram and whose prose "
               "carries no process-model token: %s"
               % (len(sc["figs"]), ", ".join(sc["figs"][:8]) +
                  (" ..." if len(sc["figs"]) > 8 else "")))
    note = ("Mechanical screen of the page's own article region (site chrome removed): " + saw +
            ". Article region %d words; the AI screen %s." %
            (sc["words"], "fires" if sc["ai"] else "does not fire"))
    return base_row(n, path, meta, sc, note=note)


def ruling_row(n, path, meta, sc):
    """A row from a hand-written ruling in _scheer_write.RULINGS (the source's AI subtree)."""
    t = W.RULINGS[path]
    verdict, reason, notation, artefacts, looked, note, rec, question = t[:8]
    ev = t[8] if len(t) > 8 else sc["proc_quote"]
    row = base_row(n, path, meta, sc, verdict=verdict, reason=reason, judgment=True,
                   notation=notation, artefacts_on_page=artefacts, figures_looked_at=looked,
                   note=note, needs_human_ruling=bool(question), question=question,
                   record=("corpus/scheer-pas/%s.md" % rec) if rec else None,
                   judged_from="page read + its figures looked at",
                   screen={"figures": sc["figs"], "diagram_named_figures": sc["suspect"],
                           "prose_process_token": sc["proc"]})
    if ev:
        row["evidence"] = ev
    return row


def derived_row(n, path, meta, sc):
    """The row for a diagram-flagged page, from the sweep's classification of its figures."""
    cats = {}
    for nm in sc["suspect"]:
        cats.setdefault(FIGCLASS.get(nm, "unknown"), []).append(nm)
    looked = ("the page's diagram-named figures (%s) in the site-wide sweep sheets"
              % ", ".join(sc["suspect"])[:400]) if sc["suspect"] else "none (no diagram-named figure)"
    row = base_row(n, path, meta, sc, figures_looked_at=looked)
    if sc["proc_quote"]:
        row["evidence"] = sc["proc_quote"]

    if "bpmn" in cats:
        # a genuine BPMN model: these pages are ruled one by one (W.RULINGS or the AI-token test)
        if sc["ai"]:
            row.update(verdict="UNCERTAIN", needs_human_ruling=True, question=(
                "This page publishes BPMN 2.0 notation (%s) and its article region also carries "
                "an AI/LLM mention (%r). Does that AI mention name an element inside the BPMN "
                "process shown - i.e. is this an AI-enabled process artefact - or does it refer "
                "to something else on the page (an AI feature of the Designer, AI on the roadmap, "
                "AI-generated documentation)? A reading of the page is needed to settle it."
                % (", ".join(cats["bpmn"]), sc["ai_quote"])),
                judged_from="scheer-page-screen + sweep of the page's diagram-named figures",
                notation="BPMN 2.0 (Scheer PAS Designer BPMN editor)",
                artefacts_on_page="BPMN model(s)/notation: %s" % ", ".join(cats["bpmn"]),
                note=("The page's diagram-named figures are BPMN 2.0 notation and its article "
                      "region carries an AI/LLM mention; because the AI element may or may not be "
                      "inside the process shown, this row is handed to the researcher rather than "
                      "excluded."))
        else:
            row.update(verdict="EXCLUDE", reason="E2-no-ai-element", judgment=True,
                       judged_from="scheer-page-screen + sweep of the page's diagram-named figures",
                       notation="BPMN 2.0 (Scheer PAS Designer BPMN editor)",
                       artefacts_on_page="BPMN model(s): %s" % ", ".join(cats["bpmn"]),
                       note=("The page publishes BPMN 2.0 notation (%s) and its article region "
                             "carries no AI/LLM mention at all (the AI screen does not fire), so "
                             "the BPMN figures it publishes contain no AI element and there is no "
                             "AI mention to dismiss." % ", ".join(cats["bpmn"])))
        return row

    if cats.get("exec") or cats.get("other"):
        # E1 rows carry judgment=False, as in this corpus's other ledgers: what settled them is the
        # notation of the page's figures, recorded per name, not a collected-then-rejected
        # candidate. `judged_from` keeps that provenance visible.
        kinds = []
        if cats.get("exec"):
            kinds.append("xUML execution models / activity diagrams")
        if cats.get("other"):
            kinds.append("diagrams in other non-BPMN notations")
        row.update(verdict="EXCLUDE", reason="E1-not-bpmn", judgment=False, judged_from=
                   "scheer-page-screen + sweep of the page's diagram-named figures",
                   notation=("proprietary Scheer PAS notation, not BPMN 2.0: " + " and ".join(kinds)),
                   artefacts_on_page="%s: %s" % (" and ".join(kinds),
                                                 ", ".join(cats.get("exec", []) + cats.get("other", []))),
                   note=("The page's diagram-named figures are %s, not BPMN 2.0: %s. The prose "
                         "screen fired on %r."
                         % (" and ".join(kinds),
                            ", ".join(cats.get("exec", []) + cats.get("other", [])), sc["proc"])))
        return row

    if cats.get("ui") or cats.get("doc"):
        row.update(judged_from="scheer-page-screen + sweep of the page's diagram-named figures",
                   note=("The page's diagram-named figures are Designer/web UI screenshots, not "
                         "diagrams: %s. The prose screen fired on %r."
                         % (", ".join(cats.get("ui", []) + cats.get("doc", [])), sc["proc"])))
        return row

    row.update(judged_from="scheer-page-screen + sweep of the page's diagram-named figures",
               note=("No diagram-named figure on the page; its %d figure(s) are %s. The prose "
                     "screen fired on %r." % (len(sc["figs"]), ", ".join(sc["figs"][:10]), sc["proc"])))
    return row


def header(pop):
    return {
        "type": "header", "source": "scheer-pas",
        "source_name": "Scheer PAS documentation (doc.scheer-pas.com), version latest = 26.2",
        "census": True, "population_size": pop,
        "enumeration_method": (
            "The help site is a Scroll-Sites/Confluence docs portal that publishes each doc "
            "space's complete page tree as JSON: /<space>/latest/__pagetree.json, and "
            "/<space>/__pagetree.json for the two un-versioned spaces (help, release-notes). The "
            "14 spaces enumerated from the portal home gave academy 152, administration 122, "
            "analyzer 59, api-management 79, bpaas 0, bridge 0, business-modeler 74, designer "
            "574, getting-started 7, help 44, installation-guides 82, pas-code 41, process-mining "
            "35, release-notes 64 = 1333 pages, which is the population. Every page was fetched "
            "and cached (ledgers/_scheer_crawl.py, ~1 request/s, raw HTML in "
            "ledgers/_scheer/pages/, index in ledgers/_scheer/index.json), and every page has a "
            "row. Version facet: the version selector serves 26.2 as 'latest' and the versioned "
            "URLs (/designer/25.3/...) are the same pages, not additional items - checked on "
            "/designer/__pagetree.json, whose page list matches /designer/latest/__pagetree.json "
            "one to one. Keyword facets were not used to narrow anything: the AI screen "
            "(ledgers/_scheer_rows.py) was run over every page's article region, and the pages it "
            "and the process screen fire on are judged by eye, not filtered out."),
        "entry_points": [
            "https://doc.scheer-pas.com/ (portal home, the space list)",
            "https://doc.scheer-pas.com/academy/latest/ai-tutorials",
            "https://doc.scheer-pas.com/designer/latest/using-ai-agents",
            "https://doc.scheer-pas.com/academy/latest/__pagetree.json (the enumeration endpoint)",
        ],
        "access": "public",
        "date_start": TODAY,
        "agent_model": "deepseek-v4.1-flash:cloud",
        "browser_tool": "chrome-devtools-mcp --browser-url 127.0.0.1:9222 (own tab only)",
        "note": (
            "The site renders its chrome (docs nav, cookie notice, the 'Ask the PAS Chatbot!' "
            "banner) on every page, and that chrome carries AI words; all screens therefore run "
            "on the page's own <article id=\"content\"> region only. The screen that decides a "
            "row: a page whose figures' attachment names or whose prose name a process model "
            "(BPMN / process model / gateway / pool / lane / execution model / activity diagram / "
            "start event / ...) is judged by eye; every figure whose attachment name names a "
            "diagram was downloaded site-wide and classified in sweep sheets "
            "(ledgers/_scheer_figs2.py); every other page is excluded mechanically by the screen. "
            "The screen's residual risk - a process diagram hidden behind a UI-ish attachment "
            "name on a page that never names a process - is measured by the audit sample below "
            "rather than assumed away."),
    }


def build(write=False):
    recs = records()
    rows, missing, unclassified, unresolved = [], [], set(), []
    for n, (path, meta) in enumerate(recs, 1):
        sc = screen(path)
        if sc is None:
            missing.append((n, path))
            continue
        if path in W.RULINGS:
            rows.append(ruling_row(n, path, meta, sc))
            continue
        if not sc["flagged"]:
            rows.append(mechanical_row(n, path, meta, sc))
            continue
        for nm in sc["suspect"]:
            if nm not in FIGCLASS:
                unclassified.add(nm)
        r = derived_row(n, path, meta, sc)
        if r["verdict"] != "EXCLUDE":
            unresolved.append((n, path, r))
        rows.append(r)

    flagged = [r for r in rows if r.get("judgment") or r["verdict"] != "EXCLUDE"]
    print("pages %d | rows %d | cache misses %d" % (len(recs), len(rows), len(missing)))
    print("verdicts: " + ", ".join("%s=%d" % (k, sum(1 for r in rows if r["verdict"] == k))
                                   for k in ["EXCLUDE", "UNCERTAIN", "INCLUDE", "BLOCKED"]))
    print("reasons: " + ", ".join("%s=%d" % (k, sum(1 for r in rows if r["reason"] == k))
                                  for k in ["E0-no-artefact", "E1-not-bpmn", "E2-no-ai-element"]))
    print("judgement rows: %d (%.1f%% of rows)"
          % (len(flagged), 100.0 * len(flagged) / max(1, len(rows))))
    if unclassified:
        print("UNCLASSIFIED figure names (still to sweep): %d, e.g. %s"
              % (len(unclassified), list(sorted(unclassified))[:6]))
    for n, path, r in unresolved:
        print("  RESOLVE n=%-5d %-70s %s" % (n, path, r["verdict"]))
    if missing:
        print("CACHE MISSES (crawl incomplete): %d, first 3: %s"
              % (len(missing), [p for _, p in missing[:3]]))
    if write:
        if missing or unresolved or unclassified:
            print("refusing to write: %d cache misses, %d unresolved rows, %d unclassified names"
                  % (len(missing), len(unresolved), len(unclassified)))
            return
        counts = {k: sum(1 for r in rows if r["reason"] == k)
                  for k in ["E0-no-artefact", "E1-not-bpmn", "E2-no-ai-element", "E3-duplicate"]}
        hdr = header(len(recs))
        hdr["audit_sample"] = AUDIT_SAMPLE
        footer = {
            "type": "footer", "date_end": TODAY, "rows": len(rows),
            "include": sum(1 for r in rows if r["verdict"] == "INCLUDE"),
            "uncertain": sum(1 for r in rows if r["verdict"] == "UNCERTAIN"),
            "exclude": counts, "blocked": 0,
            "judgment_exclusion_share": round(
                len([r for r in rows if r.get("judgment") and r["verdict"] == "EXCLUDE"])
                / max(1, len(rows)), 4),
            "judgement_rows": sum(1 for r in rows if r.get("judgment")),
            "status": "DONE",
            "records_written": sorted(p.stem for p in (ELI / "corpus" / "scheer-pas").glob("[0-9][0-9][0-9]_*.md")),
            "figures_looked_at": FIGURES_LOOKED,
            "surfaces": {sp: sum(1 for r in rows if r["surface"] == sp) for sp in SPACES},
        }
        W.LEDGER.write_text(
            json.dumps(hdr, ensure_ascii=False) + "\n" +
            "\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + "\n" +
            json.dumps(footer, ensure_ascii=False) + "\n", encoding="utf-8")
        W.FRONTIER.write_text("\n".join("%d\t%s" % (r["n"], r["url"]) for r in rows) + "\n",
                              encoding="utf-8")
        print("wrote %d rows + header + footer -> %s" % (len(rows), W.LEDGER))


if __name__ == "__main__":
    build(write="--write" in sys.argv)
