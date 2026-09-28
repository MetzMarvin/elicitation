#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Case-B superseding rows for the flowx-ai E1 re-judgement: the 206 E1 rows whose page does
discuss AI, now re-judged after every figure on those pages was opened by eye.

The first build excluded these pages as `E1-not-bpmn` from the page's *figure count* alone, and
its note named a category ("product UI screenshots of the vendor's own screens") for images
nobody had looked at. That is the one error this census must not make: a BPMN canvas carrying an
AI element would be a false negative. The figures were therefore looked at, in contact sheets of
four tiles at >=900 px (`ledgers/flowx-ai.raw/sheets/`, 135 sheets, 538 tiles), and each figure's
disposition is logged in `ledgers/flowx-ai.raw/visual-progress.jsonl`:

    ui          product UI screenshot / form / table / listing / dashboard / chat / code editor
    drawn       a drawn diagram that is not BPMN (architecture box, state chart, D2, proprietary canvas)
    bpmn-noai   BPMN 2.0 notation, no AI element inside the diagram
    bpmn-ai     BPMN 2.0 notation with an AI element inside the diagram          (none occurred)
    bpmn-prose  BPMN 2.0 notation, the page's AI talk is prose only              (none occurred)
    unclear     cannot tell what the figure shows                                (none occurred)
    broken      the file is unreadable                                           (none occurred)

The decision rule, applied per page (the last row for an `n` wins; corrections are appended):

    bpmn-naming diagram fence        -> UNCERTAIN + needs_human_ruling + a record   (3 pages)
    any `drawn` tile                 -> E1-not-bpmn, judgment true, the note names the
                                        non-BPMN artefact and the AI elements seen inside it
    any `bpmn-noai` tile             -> E2-no-ai-element (a BPMN diagram with no AI element
                                        inside it); judgment = whether a real AI term survives
                                        the named false positives
    a Mermaid fence, no image        -> E1-not-bpmn, judgment true (a rendered, drawn diagram
                                        in the vendor's own notation, not BPMN 2.0)
    an ASCII fence, no image         -> E1-not-bpmn, judgment false (a text/code listing)
    no image and no diagram fence    -> E0-no-artefact, mechanical
    every tile `ui`                  -> E1-not-bpmn, judgment false (02b rule: a UI screenshot,
                                        form, table or code listing is not a drawn diagram)

Because every `drawn` tile in this source is the vendor's *own* canvas (Integration Designer,
Agent Builder, Workflow canvas) or an architecture box chart, and the BPMN tiles carry no AI
node, the case-B re-judgement yields no INCLUDE and no `bpmn-ai` tile. The three pages that
publish a process diagram in Mermaid whose nodes are BPMN element names *and* which contain AI
node names are the open question, and they are records.

Usage
  python ledgers/_fx_caseb.py --dry          print the plan (classes, judgment counts)
  python ledgers/_fx_caseb.py                append the superseding rows
  python ledgers/_fx_caseb.py --fence-check  dump the diagram fences of the no-image pages
"""
import json, os, re, sys

ELI = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(ELI, "flowx-ai.raw")
LEDGER = os.path.join(ELI, "flowx-ai.jsonl")
sys.path.insert(0, ELI)
from _fx_class import AILEX, page_text                              # noqa: E402

JUDGED_FROM_SHEETS = ("eye examination of every figure this page publishes, tiled in the contact "
                      "sheets ledgers/flowx-ai.raw/sheets/ (4 tiles per sheet, >=900 px); each "
                      "figure's disposition is logged in ledgers/flowx-ai.raw/visual-progress.jsonl")
JUDGED_FROM_FENCE = ("the diagram the page itself publishes is its own source text (a diagram "
                     "fence), read verbatim from the page; the page publishes no image")

FAILED_FIGS = {  # S3 AccessDenied: the vendor's object is no longer world-readable (OPERATOR-TODO P8)
    103, 221, 285, 500, 567, 667, 674, 929}

# ---------------------------------------------------------------- the false positives

FP_PATTERNS = [
    r"(?i)flowx\.?ai", r"(?i)docs\.flowx\.ai", r"ai\.flowx\.[a-z0-9._\-]+",
    r"(?i)user-agent", r"(?i)\bprompt(s|ed|ing)?\b", r"(?i)\bclassification(s)?\b",
    r"(?i)\bretrieval\b", r"(?i)\bintelligent\b", r"(?i)\bintelligence\b",
    r"(?i)\bsemantic\b", r"(?i)\bsummari[sz]\w*", r"(?i)\brecommendation\w*", r"(?i)\bvector\b",
]
# words that match the AI lexicon but are ordinary English / product nouns
ORDINARY = {"agent", "agents", "model", "models", "ocr", "copilot", "chat"}
PROSE_AI = re.compile(r"(?i)\b(ai agent|ai agents|ai assistant|ai assistant|ai platform|ai core|"
                      r"llm|llms|ai designer|ai developer|ai analyst|mcp|embedding|embeddings|"
                      r"knowledge base|natural language|ai-powered|ai model|machine learning)\b")


def body_text(url):
    try:
        t, _ = page_text(url)
        return t
    except Exception:                                                # noqa: BLE001
        return ""


def ai_hits(url):
    """Surviving AI-lexicon hits that are not the named false positives, with their context.

    Each hit is classed: `navlink` (a navigation/sidebar link title to another page), `ordinary`
    (an ordinary English word, e.g. `Support agent`, `two main classifications`), or `prose`
    (the page is actually talking about AI)."""
    t = body_text(url)
    for p in FP_PATTERNS:
        t = re.sub(p, " ", t)
    out = []
    for m in AILEX.finditer(t):
        lo, hi = max(0, m.start() - 60), min(len(t), m.end() + 60)
        ctx = re.sub(r"\s+", " ", t[lo:hi]).strip()
        term = m.group(0)
        cls = "prose"
        if "](" in ctx or re.match(r"^\s*[-*]\s*\[", ctx):
            cls = "navlink"
        elif term.lower() in ORDINARY and not PROSE_AI.search(ctx):
            cls = "ordinary"
        out.append({"term": term, "ctx": ctx, "class": cls})
    return out


def real_ai(url):
    hits = ai_hits(url)
    return [h for h in hits if h["class"] == "prose"], hits


# ---------------------------------------------------------------- facts per row

def figs_and_tiles():
    inv = json.load(open(os.path.join(RAW, "figs_inventory.json"), encoding="utf-8"))
    u2sha = {}
    for sha, d in inv.items():
        for u in d["urls"]:
            u2sha[u] = sha
    prog = {}
    for ln in open(os.path.join(RAW, "visual-progress.jsonl"), encoding="utf-8"):
        r = json.loads(ln)
        prog[r["sha"]] = r          # last row for a sha wins
    fm = json.load(open(os.path.join(RAW, "figmeta.json"), encoding="utf-8"))
    return fm, u2sha, prog


def tiles_of(url, fm, u2sha, prog):
    """[(name, class, note)] for the figures of this page, in page order."""
    out = []
    for f in fm.get(url) or []:
        sha = u2sha.get(f["url"])
        p = prog.get(sha)
        out.append((f["url"].split("/")[-1], (p or {}).get("class", "?"), (p or {}).get("note", "")))
    return out


def current_rows():
    for ln in open(LEDGER, encoding="utf-8"):
        r = json.loads(ln)
        if not r.get("type"):
            yield r


def case_b():
    """The case-B population: the *latest* row for each n, where that row is still E1-not-bpmn.

    Only the last row for an `n` counts (the census's superseding convention), otherwise this
    function would re-emit the rows this module already appended."""
    last = {}
    for r in current_rows():
        last[r["n"]] = r
    return [r for r in last.values()
            if r.get("reason") == "E1-not-bpmn" and "ai=True" in (r.get("screen") or "")]


# ---------------------------------------------------------------- the notes

BPMN_PROSES = re.compile(r"(?i)\b(bpmn|user task|service task|send message task|receive message task|"
                         r"business rule|exclusive gateway|parallel gateway|start event|end event|"
                         r"boundary event|intermediate event|sub-?process|swimlane)\b")


def bpmn_quote(url):
    """A verbatim sentence from the page that names a BPMN element, for the row's evidence."""
    t = re.sub(r"\s+", " ", body_text(url))
    best = ""
    for sent in re.split(r"(?<=[.!?])\s+", t):
        if BPMN_PROSES.search(sent) and 25 < len(sent) < 240 and not sent.startswith("- ["):
            if "Process Designer" in sent or "BPMN" in sent:
                return sent.strip()
            best = best or sent.strip()
    return best


def fname(n):
    """A figure's file name, cleaned for the note: drop the URL fragment/query and decode %20."""
    from urllib.parse import unquote
    return unquote(n.split("#")[0].split("?")[0])


def fnote(name, note):
    """'name (what it is)', without repeating the file name inside its own note."""
    n = fname(name)
    t = (note or "").strip()
    for pre in (n, name):
        if t.lower().startswith(pre.lower()):
            t = t[len(pre):].lstrip(" -:–").strip()
    return "%s (%s)" % (n, t[:90]) if t else n


def q(s, limit=25):
    w = s.split()
    return " ".join(w[:limit]) + ("..." if len(w) > limit else "")


MARKUP = re.compile(r"[<>\[\]|]|\*\*")   # markdown/JSX markup; a single `code span` is allowed


def best_quote(url, terms):
    """A clean verbatim prose sentence from the page naming one of `terms`, <=25 words.

    The body view the classifier uses is screened, not the raw MDX twin: the twin's header carries
    the host's own boilerplate ("Documentation Index ... https://docs.flowx.ai/llms.txt"), which is
    site chrome and not this page's words. A sentence carrying markdown or JSX markup is never
    returned - a `**bold**` or an `<Info>` tag is not something the page *says* in prose. When only
    marked-up sentences match, the caller falls back to quoting the bare term."""
    try:
        t = page_text(url)[0]
    except Exception:                                                # noqa: BLE001
        return ""
    t = re.sub(r"\s+", " ", t)
    pat = re.compile("|".join(re.escape(x) for x in terms if x), re.I)
    for s in re.split(r"(?<=[.!?])\s+", t):
        if not pat.search(s):
            continue
        s = s.strip().lstrip("-*#>").strip()
        if not (30 < len(s) < 240) or MARKUP.search(s) or "Documentation Index" in s:
            continue
        return q(s)
    return ""


def note_e1_drawn(tiles, url):
    dr = [t for t in tiles if t[1] == "drawn"]
    names = "; ".join(fnote(t[0], t[2]) for t in dr[:3])
    real, hits = real_ai(url)
    what = ("Drawn figure(s) seen by eye, with what each turned out to be: %s. None of them is a "
            "rendered BPMN 2.0 canvas: they are the vendor's own canvases or the page's own "
            "illustrations and architecture charts, as named above. " % names)
    if any(t[1] == "bpmn-noai" for t in tiles):
        what += ("The page's BPMN 2.0 figures (%s) are separate from these and carry no AI element, "
                 "checked on the same sheets. "
                 % ", ".join(fname(t[0]) for t in tiles if t[1] == "bpmn-noai")[:120])
    if real:
        term = ", ".join(sorted({x["term"] for x in real})[:6])
        qt = best_quote(url, sorted({x["term"] for x in real}) + PROSE_AI.findall(real[0]["ctx"]))
        frag = ('quoted from the page: "%s"' % qt) if qt else ('the bare term "%s"' % real[0]["term"])
        what += ("The page's AI subject matter is real - terms that survive the named false "
                 "positives: %s, %s - but it sits in the vendor's own canvases named above, not in a "
                 "BPMN 2.0 diagram, which is why this artefact is not BPMN. The AI talk is %s."
                 % (term, frag,
                    OVERRIDE_REFERS.get(url, "the platform's AI features described in page prose")))
    return what


def note_e1_ui(tiles, url):
    names = ", ".join(fname(t[0]) for t in tiles[:6])
    return ("Figure(s) seen by eye: %s. Each is a product UI screenshot or recording of the vendor's "
            "own screens (forms, tables, pickers, listings), not a drawn diagram, so no notation is "
            "being named for an image whose content is unexamined: a screenshot of a UI is not a "
            "BPMN artefact and not a diagram at all." % names)


def note_e1_fence(url, kind, quote, names_bpmn=False):
    s = ("The page publishes no image; the artefact its screen counted is a diagram fence in the "
         "page's own published source, read verbatim. It opens \"%s\": it is %s, not BPMN 2.0 "
         "notation, so it cannot carry a BPMN process element of any kind." % (quote, kind))
    if not names_bpmn:
        s += (" Its text was screened for BPMN element names (pool, lane, gateway, user task, service "
              "task, send/receive message task, business rule, start/end event, sub-process) and "
              "carries none.")
    return s


def raw_page(url):
    rel = url.replace("https://docs.flowx.ai", "").lstrip("/")
    p = os.path.join(RAW, "pages", rel.replace("/", "__") + ".md")
    return p if os.path.exists(p) else None


def page_fences(url):
    """[(lang, body)] parsed line-wise from the page's own published markdown twin.

    Note: this must read the raw twin. `page_text` is the *classifier's* body view and has the
    fenced blocks already stripped, so parsing it finds no diagram at all."""
    p = raw_page(url)
    if not p:
        return []
    t = open(p, encoding="utf-8").read()
    out, cur = [], None
    for ln in t.split("\n"):
        s = ln.strip()
        if s.startswith("```"):
            if cur is None:
                cur = [s[3:].strip(), []]
            else:
                out.append((cur[0], "\n".join(cur[1])))
                cur = None
            continue
        if cur is not None:
            cur[1].append(ln)
    return out


ARROW = re.compile(r"(?i)(-->|->|→|⇒)")
DIAGRAM_LANGS = {"mermaid", "graph", "flowchart", "d2", "plantuml", "dot"}


def diagram_fence(url):
    """The page's diagram fence, if it publishes one: (kind, quote, names_bpmn_terms).

    kind is 'mermaid' (a rendered, drawn diagram in the page's own notation) or 'ascii' (an
    arrow sketch written in the page's own text, which is a text listing, not a drawing)."""
    for lang, body in page_fences(url):
        lines = [x for x in body.split("\n") if x.strip()]
        if not lines:
            continue
        dialect = (lang.split() or [""])[0].lower()   # "mermaid theme={...}" -> "mermaid"
        is_dia = dialect in DIAGRAM_LANGS or ARROW.search(body)
        if not is_dia:
            continue
        kind = "mermaid" if dialect in DIAGRAM_LANGS else "ascii"
        head = next((x for x in lines if re.search(r"(?i)(flowchart|graph [A-Z]{2}|sequenceDiagram|"
                                                   r"stateDiagram|erDiagram|classDiagram)", x)),
                    lines[0])
        quote = head.strip()[:60]
        names = sorted({w.group(0).lower() for w in BPMN_PROSES.finditer(body)})
        return kind, quote, bool(names), len(lines)
    return None, "", False, 0


def note_e0(url):
    return ("The page publishes no image and no diagram fence: its screen counted an artefact that "
            "does not exist on the page as built. No figure was required for this verdict.")


def note_e2(tiles, url, real, hits):
    bn = ", ".join(fname(t[0]) for t in tiles if t[1] == "bpmn-noai")[:160]
    ui = len([t for t in tiles if t[1] == "ui"])
    s = ("BPMN 2.0 figure(s) seen by eye: %s. They are the BPMN Process Designer's own elements and "
         "carry no AI node: the palette offers none. " % bn)
    if ui:
        s += "The page's other %d figure(s) are product UI screenshots, not diagrams. " % ui
    if real:
        qt = best_quote(url, sorted({x["term"] for x in real}) + PROSE_AI.findall(real[0]["ctx"]))
        frag = ('quoted from the page: "%s"' % qt) if qt else ('the bare term "%s"' % real[0]["term"])
        s += ("The page's AI talk is prose, not an element inside the diagram, %s - it is about "
              "%s." % (frag, OVERRIDE_REFERS.get(url, "the platform's AI features in general")))
    else:
        terms = sorted({h["term"] for h in hits})[:6]
        s += ("Its AI-lexicon hits are the named false positives (%s), not AI mentions: %s."
              % (", ".join(terms), "navigation link titles to other pages on this site"
                 if hits and all(h["class"] == "navlink" for h in hits)
                 else "ordinary English words and navigation link titles"))
    return s


# what each page's surviving AI prose is actually about (hand-read, one line each)
OVERRIDE_REFERS = {
    "https://docs.flowx.ai/4.7.x/docs/platform-deep-dive/ai-core/ai-core-overview":
        "the platform's AI Core architecture page, not the BPMN figure below it",
    "https://docs.flowx.ai/4.7.x/setup-guides/flowx-engine-setup-guide/engine-setup":
        "an environment variable for the separate AI Developer agent process, a different runtime",
    "https://docs.flowx.ai/5.9/ai-platform/pre-built-agents/overview":
        "the design-time AI assistants (Config-time agents) built into FlowX Designer",
    "https://docs.flowx.ai/5.9/docs/building-blocks/ui-designer/ui-designer":
        "a UI Designer chat component for AI agent conversations, a UI building block",
    "https://docs.flowx.ai/5.9/docs/platform-deep-dive/integrations/incoming-webhooks":
        "how the platform stores provider secrets for LLM integrations, an infrastructure note",
    "https://docs.flowx.ai/release-notes/v5.x/v5.3.0-december-2025/v5.3.0-december-2025":
        "the release's new AI platform capabilities (MCP integration, Custom Agent nodes, Knowledge "
        "Base), announced on a release-notes page, not an in-diagram element",
}


def build(dry=False):
    fm, u2sha, prog = figs_and_tiles()
    fence = json.load(open(os.path.join(RAW, "fences.json"), encoding="utf-8"))
    cls = {d["url"]: d for d in json.load(open(os.path.join(RAW, "classify.json"),
                                                 encoding="utf-8"))}
    out, plan = [], []
    for r in case_b():
        url = r["url"]
        tiles = tiles_of(url, fm, u2sha, prog)
        n_bpmn_fence = (cls.get(url) or {}).get("n_bpmn_fence", 0)
        kind, fquote, f_names_bpmn, f_lines = diagram_fence(url)
        real, hits = real_ai(url)
        row = dict(r)
        row["supersedes_row"] = True
        if n_bpmn_fence or (f_names_bpmn and not tiles):
            continue                                    # handled as records, not here
        elif any(t[1] == "drawn" for t in tiles):
            row.update(reason="E1-not-bpmn", judgment=True, judged_from=JUDGED_FROM_SHEETS,
                       note=note_e1_drawn(tiles, url), figures_looked_at=[fname(t[0]) for t in tiles],
                       screen=(r.get("screen") or "") + " | figures opened by eye: drawn")
            plan.append("E1-drawn")
        elif any(t[1] == "bpmn-noai" for t in tiles):
            row.update(reason="E2-no-ai-element", judgment=bool(real), judged_from=JUDGED_FROM_SHEETS,
                       note=note_e2(tiles, url, real, hits),
                       figures_looked_at=[fname(t[0]) for t in tiles],
                       screen=(r.get("screen") or "") + " | figures opened by eye: bpmn-noai")
            plan.append("E2-bpmn" + ("-ai-prose" if real else "-fp-only"))
        elif not tiles and kind == "mermaid":
            row.update(reason="E1-not-bpmn", judgment=True, judged_from=JUDGED_FROM_FENCE,
                       note=note_e1_fence(url, "a Mermaid diagram (a rendered flowchart in the "
                                               "vendor's own notation)", fquote),
                       figures_looked_at=None,
                       screen=(r.get("screen") or "") + " | no image on the page; diagram fence read")
            row["evidence"] = '"%s"' % fquote
            plan.append("E1-mermaid")
        elif not tiles and kind == "ascii":
            row.update(reason="E1-not-bpmn", judgment=False, judged_from=JUDGED_FROM_FENCE,
                       note=note_e1_fence(url, "an arrow sketch written out as text", fquote),
                       figures_looked_at=None,
                       screen=(r.get("screen") or "") + " | no image on the page; diagram fence read")
            row["evidence"] = '"%s"' % fquote
            plan.append("E1-ascii")
        elif not tiles:
            row.update(reason="E0-no-artefact", judgment=False, judged_from=JUDGED_FROM_FENCE,
                       note=note_e0(url), figures_looked_at=None, screen=r.get("screen"))
            plan.append("E0")
        else:
            row.update(reason="E1-not-bpmn", judgment=False, judged_from=JUDGED_FROM_SHEETS,
                       note=note_e1_ui(tiles, url), figures_looked_at=[fname(t[0]) for t in tiles],
                       screen=(r.get("screen") or "") + " | figures opened by eye: ui only")
            plan.append("E1-ui")
        if int(r["n"]) in FAILED_FIGS:
            row["note"] += (" One figure on this page is an S3 object the vendor has made private "
                            "(AccessDenied); see OPERATOR-TODO P8. The verdict does not rest on it.")
        bq = bpmn_quote(url)
        if bq and bq not in (row.get("evidence") or ""):
            row["evidence"] = "\"%s\" | superseded row evidence: %s" % (bq, row.get("evidence", ""))
        out.append(row)
    from collections import Counter
    print("case-B rows re-emitted: %d" % len(out))
    print("plan:", dict(Counter(plan)))
    print("judgment true: %d   false: %d" % (sum(1 for r in out if r["judgment"]),
                                             sum(1 for r in out if not r["judgment"])))
    last = {}
    for ln in open(LEDGER, encoding="utf-8"):
        rr = json.loads(ln)
        if not rr.get("type"):
            last[rr["n"]] = rr
    fresh = [r for r in out
             if not (last.get(r["n"], {}).get("supersedes_row")
                     and last[r["n"]]["reason"] == r["reason"]
                     and last[r["n"]]["judgment"] == r["judgment"]
                     and last[r["n"]].get("note") == r.get("note"))]
    if len(fresh) != len(out):
        print("already current (not re-appended): %d of %d" % (len(out) - len(fresh), len(out)))
        out = fresh
    if dry:
        for r in out:
            if r["judgment"] and r["reason"] == "E2-no-ai-element":
                print("\nn=%s %s\n  %s" % (r["n"], r["url"], r["note"][:400]))
        return out
    with open(LEDGER, "a", encoding="utf-8") as fh:
        for r in out:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    print("appended to %s" % LEDGER)
    return out


def fence_check():
    """The diagram fences of the no-image pages: what are they, and do they name BPMN elements?"""
    import _fx_class
    fm, u2sha, prog = figs_and_tiles()
    for r in sorted(case_b(), key=lambda x: int(x["n"])):
        url = r["url"]
        if tiles_of(url, fm, u2sha, prog):
            continue
        try:
            t, _ = _fx_class.page_text(url)
        except Exception:                                            # noqa: BLE001
            continue
        found = []
        for m in re.finditer(r"```(\w*)\n(.*?)```", t, re.S):
            lang, body = m.group(1), m.group(2)
            words = len(body.split())
            bpmn = sorted({w.group(0).lower() for w in re.finditer(BPMN_PROSES, body)})
            if words > 6 and (lang.lower() in ("mermaid", "text", "bash", "") or bpmn):
                found.append((lang or "(none)", words, bpmn, body[:100].replace("\n", " ")))
        if found:
            print("n=%s %s" % (r["n"], url.replace("https://docs.flowx.ai", "")))
            for lang, words, bpmn, head in found:
                print("    fence lang=%-8s words=%-4d bpmn=%-40s %s"
                      % (lang, words, ",".join(bpmn)[:40], head[:70]))


def main():
    if "--fence-check" in sys.argv:
        fence_check()
    else:
        build("--dry" in sys.argv)


if __name__ == "__main__":
    main()
