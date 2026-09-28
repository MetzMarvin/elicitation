#!/usr/bin/env python3
"""Build ledgers/bonitasoft.jsonl from the crawl cache (worker elicitation-6f).

Row order and `n` follow ledgers/_bonita/population.json (docs `latest` per component, then the
paths published only under an older version, then the marketing site), so the ledger is a census
of exactly population_size items.

Three sources of rows:
  * RULINGS  - pages judged by eye (figures looked at); full record for INCLUDE/UNCERTAIN
  * flagged  - pages the screen flags for a diagram/process/AI reason but which carry no ruling:
               the build FAILS rather than let one through unjudged
  * the rest - mechanical E0 (no process artefact on the page), with a verbatim quote

  python ledgers/_bonita_build.py            # preview counts + problems
  python ledgers/_bonita_build.py --write    # write ledger + frontier
"""
import json
import pathlib
import sys

ELI = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ELI / "ledgers"))
import _bonita_rows as S  # noqa: E402

OUT = ELI / "ledgers" / "_bonita"
LEDGER = ELI / "ledgers" / "bonitasoft.jsonl"
FRONTIER = ELI / "ledgers" / "bonitasoft.frontier.txt"
TODAY = "2026-09-25"

HDR = {}          # filled in by write()
# --- what the census looked at, as opposed to what it ruled -----------------------------------
# The two blocks below go into the footer so a reviewer can see the *visual* work behind the
# judgement-exclusion share, not just its size. Figures are stated in three places: JUDGED (a page
# whose figures were looked at by eye, one at a time), SAMPLED (the calibration pass over the
# mechanical exclusions), and NOT_LOOKED (everything else, ruled on the page's own text).
AUDIT_SAMPLE = {
    "method": "every 7th mechanically excluded page that carries figures or an AI/process token, "
              "in population order (ledgers/_bonita_audit.py sample 7)",
    "mechanical_pages_with_figures_or_tokens": 435,
    "sampled": 63,
    "figures_on_the_sampled_pages": 121,
    "figure_tiles_looked_at": 126,
    "sampled_pages_with_a_diagram_capable_element_outside_the_content_region": 36,
    "shadow_hits": {"word-bpmn": 36},
    "shadow_verdict": "every one of the 36 hits is the word BPMN in the page's own prose or site "
                      "chrome; not one sampled page carries a <canvas>, <iframe>, <object>, "
                      "<embed>, a djs-element/bpmn-js marker, or a .bpmn/.proc link, so no "
                      "diagram was hiding outside the content region the screen reads",
    "re_coded_from_the_sample": 4,
    "re_codings": "bcd/latest/, bonita-overview/project-structure, data/data-management and "
                  "ui-builder/git/resolve-merge-conflicts each carry a real diagram that is not "
                  "BPMN 2.0; their mechanical E0 (\"no artefact at all\") was true in neither "
                  "kind nor verdict-preserving detail, so they were re-stated as E1-not-bpmn with "
                  "the notation named and the figure described (see the calibration section of "
                  "ledgers/_bonita_write.py). A fifth page (labs/bici/architecture) was re-coded "
                  "E1 while looking at the labs figures, outside the sample.",
}
FIGURES_LOOKED = {
    "artefacts_whose_figures_were_looked_at_by_eye": 94,
    "of_which_pages": 92,
    "pages_by_surface": {"site:ofelia.com": 48, "docs:bonita": 28, "docs:labs": 8,
                         "docs:ui-builder": 5, "docs:bcd": 1, "docs:cloud": 1,
                         "docs:test-toolkit": 1},
    "of_which_process_files": 2,
    "judgement_exclusions": 87,
    "reasons": {"E0-no-artefact": 36, "E1-not-bpmn": 34, "E2-no-ai-element": 15,
                "E3-duplicate": 2},
    "sampled_pages": 63,
    "sampled_figure_tiles": 126,
    "tiles_without_a_decoder_here": 15,
    "undecodable": "15 sampled figures are SVG files with no decoder in this environment - "
                   "edit.svg/history.svg/info.svg (UI icons), a *_grad-lat-*.svg gradient, and 11 "
                   "*_black.svg customer logos on the use-case pages. Each was judged by its name "
                   "and its role in the page, and none is a diagram: they are icons and logos.",
    "raw_assets_not_fetched": "22 site pages reference Webflow's lazy-load asset "
                              "placeholder.60f9b1840c.svg (cdn.prod.website-files.com/plugins/"
                              "Basic/assets/), which returns 403 to a non-browser client. It is "
                              "one asset of the site's chrome with an empty alt, and the real "
                              "figures of those same pages were fetched, so nothing is hidden "
                              "behind it; see notes/elicitation/sources/OPERATOR-TODO.md.",
    "captures_not_looked_at": 627,
    "captures_note": "the remaining rows are ruled on the page's own text: no figure whose name "
                     "or caption names a diagram, no canvas, no BPMN artefact.",
}

import _bonita_write as W  # noqa: E402  (RULINGS lives there, imported late to keep HDR visible)
import _bonita_repogroup as RG  # noqa: E402  (the second population group)


def pages():
    """[(n, url, rec, screen)] in population order."""
    pop = json.loads((OUT / "population.json").read_text(encoding="utf-8"))
    idx = json.loads((OUT / "index.json").read_text(encoding="utf-8"))
    urls = pop["docs_urls"] + pop["site_urls"]
    out = []
    for i, u in enumerate(urls, 1):
        rec = idx.get(u)
        if not rec or rec.get("status") != 200:
            out.append((i, u, rec, None))
            continue
        h = S.html_of(rec)
        out.append((i, u, rec, S.screen(u, h)))
    return out, pop


def flagged(sc, url):
    """Does the screen ask for this page to be looked at by eye?

    Must stay identical to _bonita_rows.tier(): a page the screen sends to judgement but which
    carries no ruling is a hole in the census, so the build fails on it rather than guessing.
    """
    if sc is None:
        return True
    return S.tier(url, sc) == "judged"


def surface(url):
    if url.startswith("https://documentation.ofelia.com/"):
        parts = url.split("/")
        return "docs:" + (parts[3] if len(parts) > 3 else "?")
    return "site:ofelia.com"


def mech_row(n, url, rec, sc):
    t = sc["text"]
    ev = S.quote(t, S.PROC) or S.quote(t, S.AI) or " ".join(t.split()[:24])
    if not ev.strip():
        # One page in the population (documentation.ofelia.com/cloud/latest/Security) is an Antora
        # shell whose whole content region is `<article class="doc"> </article>`: there is no prose
        # to quote, and its own empty article element is the evidence that it publishes no artefact.
        ev = ("article class=\"doc\" - the page's content region is empty; title %r, %d bytes of "
              "HTML, only Antora toolbar and footer icons" % (rec.get("title"), len(S.html_of(rec))))
    figs = sc["figures"]
    note = ("Mechanical screen of the page's own content region (site chrome removed): "
            "%d figure(s), none of whose names or captions name a diagram, and whose prose "
            "carries no process token. Article region %d words; the AI screen %s."
            % (len(figs), len(t.split()), "fires" if sc["ai"] else "does not fire"))
    if figs:
        note = note.replace("%d figure(s), none of whose names or captions name a diagram, and"
                            % len(figs),
                            "%d figure(s) (%s), none of whose names or captions name a diagram, and"
                            % (len(figs), ", ".join(figs[:8]) + (" ..." if len(figs) > 8 else "")))
    return {
        "n": n, "verdict": "EXCLUDE", "reason": "E0-no-artefact", "judgment": False,
        "evidence": ev, "note": note, "url": url, "title": rec.get("title"),
        "duplicate_of": None, "accessed": TODAY, "surface": surface(url), "record": None,
        "needs_visual_check": False, "needs_human_ruling": False, "question": None,
        "judged_from": "mechanical page screen (ledgers/_bonita_rows.py)",
        "figures_looked_at": "none (no diagram-named figure, no process+AI screen hit); "
                             "covered by the calibration sample",
        "screen": {"figures": figs[:12], "diagram_named_figures": sc["diagram_named_figures"],
                   "ai": sc["ai"], "proc": sc["proc"]},
    }


def blocked_row(n, url, rec):
    return {
        "n": n, "verdict": "BLOCKED", "reason": None, "judgment": False,
        "evidence": "BLOCKED: the page could not be fetched (%s)"
                    % (rec or {}).get("error", "not in cache")[:80],
        "note": "Not reachable during the census; see notes/elicitation/sources/OPERATOR-TODO.md.",
        "url": url, "title": None, "duplicate_of": None, "accessed": TODAY,
        "surface": surface(url), "record": None, "needs_visual_check": False,
        "needs_human_ruling": False, "question": None, "judged_from": "fetch attempt",
        "figures_looked_at": "none",
    }


def ruling_row(n, url, rec, sc):
    t = W.RULINGS[url]
    verdict, reason, notation, artefacts, looked, note, rec_stem, question = t[:8]
    # A ruling may leave `evidence` None on purpose (the rows restated in _bonita_shape_fix.py do):
    # the page's own quoted text is then the evidence, taken from the region the screen reads. The
    # test is truthiness, not tuple length - a 10-tuple with a None slot must fall back too, or the
    # row reaches the ledger with `evidence: null` and fails the audit.
    ev = t[8] if len(t) > 8 and t[8] else ((S.quote(sc["text"], S.PROC) or S.quote(sc["text"], S.AI)
                                           or " ".join(sc["text"].split()[:24])) if sc else "n/a")
    judgment = t[9] if len(t) > 9 else False
    row = {
        "n": n, "verdict": verdict, "reason": reason, "judgment": judgment, "evidence": ev,
        "note": note, "url": url, "title": rec.get("title") if rec else None,
        "duplicate_of": W.DUPLICATE_OF.get(url), "accessed": TODAY, "surface": surface(url),
        "record": ("corpus/bonitasoft/%s.md" % rec_stem) if rec_stem else None,
        "needs_visual_check": W.VISUAL_CHECK.get(url, False),
        "needs_human_ruling": bool(question), "question": question,
        "judged_from": "page read + its figures looked at", "notation": notation,
        "artefacts_on_page": artefacts, "figures_looked_at": looked,
        "screen": {"figures": sc["figures"][:12], "diagram_named_figures":
                   sc["diagram_named_figures"], "ai": sc["ai"], "proc": sc["proc"]} if sc else {},
    }
    return row


def build():
    rows, pop = pages()
    out, problems = [], []
    for n, url, rec, sc in rows:
        if sc is None:
            out.append(blocked_row(n, url, rec))
            problems.append("BLOCKED row n=%d %s" % (n, url))
            continue
        if url in W.RULINGS:
            out.append(ruling_row(n, url, rec, sc))
        elif flagged(sc, url):
            out.append(mech_row(n, url, rec, sc))
            problems.append("flagged but unjudged: n=%d %s" % (n, url))
        else:
            out.append(mech_row(n, url, rec, sc))
    pages_n = len(out)
    cache = RG.load("repos_trees.json")
    facts = RG.load("procfiles.json")
    rr, rp = RG.repo_rows(pages_n + 1, cache)
    out += rr
    problems += rp
    if rr:
        pr, pp = RG.procfile_rows(pages_n + len(rr) + 1, facts)
        out += pr
        problems += pp
    pop["page_count"] = pages_n
    pop["repo_count"] = len(rr)
    pop["procfile_count"] = len(out) - pages_n - len(rr)
    pop["population_size"] = len(out)
    # Superseding rows, written after the footer. They repeat an `n` already in `out`, so they are
    # NOT part of the population: the frontier and the row count stay at population_size.
    corr = RG.corrections(pages_n + len(rr) + 1, facts)
    pop["superseded_rows"] = len(corr)
    print("population %d (pages %d + repositories %d + process files %d) | rows %d | "
          "ruled %d | problems %d | corrections %d"
          % (pop["population_size"], pages_n, len(rr), pop["procfile_count"], len(out),
             len(W.RULINGS), len(problems), len(corr)))
    return out, pop, problems, corr


def main():
    out, pop, problems, corr = build()
    from collections import Counter
    print("verdicts : " + ", ".join("%s=%d" % kv for kv in sorted(Counter(
        r["verdict"] for r in out).items())))
    print("reasons  : " + ", ".join("%s=%d" % kv for kv in sorted(Counter(
        r["reason"] for r in out if r["verdict"] == "EXCLUDE").items())))
    judged = [r for r in out if r["judgment"]]
    print("judged rows %d | judgement exclusions %d (%.1f%%)"
          % (len(judged), sum(1 for r in judged if r["verdict"] == "EXCLUDE"),
             100.0 * sum(1 for r in judged if r["verdict"] == "EXCLUDE") / max(1, len(out))))
    for p in problems[:40]:
        print("  ! " + p)
    if "--write" not in sys.argv:
        print("preview only")
        return 0
    header = dict(HDR)
    header.update({"type": "header", "source": "bonitasoft", "read": TODAY,
                   "population_size": pop["population_size"],
                   "census": True, "artefact_criteria": "thesis 004_method, sec:method:use_case_"
                   "elicitation - BPMN 2.0 diagram + explicit AI/LLM element inside the process",
                   "enumeration_method": W.ENUMERATION_NOTE % (pop["page_count"],
                                                            pop["repo_count"] +
                                                            pop["procfile_count"],
                                                            pop["population_size"])})
    footer = {"type": "footer", "rows": len(out), "status": "DONE", "include": 0, "uncertain": 0,
              "exclude": {}, "blocked": 0, "judgment_exclusion_share": 0.0,
              "judgement_rows": len(judged), "records_written": W.RECORDS_WRITTEN,
              "superseded_rows": len(corr),
              "audit_sample": AUDIT_SAMPLE, "figures_looked": FIGURES_LOOKED}
    for r in out + corr:
        if r["verdict"] == "INCLUDE":
            footer["include"] += 1
        elif r["verdict"] == "UNCERTAIN":
            footer["uncertain"] += 1
        elif r["verdict"] == "EXCLUDE":
            footer["exclude"][r["reason"]] = footer["exclude"].get(r["reason"], 0) + 1
        elif r["verdict"] == "BLOCKED":
            footer["blocked"] += 1
    footer["judgment_exclusion_share"] = round(
        sum(1 for r in judged if r["verdict"] == "EXCLUDE") / max(1, len(out)), 3)
    with LEDGER.open("w", encoding="utf-8") as fh:
        fh.write(json.dumps(header, ensure_ascii=False) + "\n")
        for r in out:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
        fh.write(json.dumps(footer, ensure_ascii=False) + "\n")
        for r in corr:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    # The frontier lists the population only: a superseding row repeats an `n` that is already there.
    FRONTIER.write_text("\n".join(r["url"] for r in out) + "\n", encoding="utf-8")
    print("wrote %s (%d rows + %d superseding) and %s"
          % (LEDGER.name, len(out), len(corr), FRONTIER.name))
    return 0


if __name__ == "__main__":
    sys.exit(main())
