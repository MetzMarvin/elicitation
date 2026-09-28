#!/usr/bin/env python3
"""Turn the docs survey into ledger rows for oracle-oic (n continues from 230).

Mechanical rows only. Pages whose text carries an AI/LLM keyword AND that publish a
non-chrome figure, plus pages that need a hand ruling for any other reason, are NOT
decided here: they must be supplied in _6f_oic_docs_rulings.json (url -> dict).

Usage:
  python ledgers/_6f_oic_docs_rows.py            # preview only, writes nothing
  python ledgers/_6f_oic_docs_rows.py --write    # append rows, frontier, header, footer
"""
import json
import pathlib
import re
import sys

ELI = pathlib.Path(__file__).resolve().parents[1]
OUT = ELI / "ledgers" / "_6f_docs"
LEDGER = ELI / "ledgers" / "oracle-oic.jsonl"
FRONTIER = ELI / "ledgers" / "oracle-oic.frontier.txt"
TODAY = "2026-09-24"
N_START = 230
BLOG_ROWS = 229

CHROME = re.compile(
    r"(sp_common|/icons?/|[-_/]icon|icon[-_.]|logo|bullet|/nav|_nav|note\.|caution|warning"
    r"|arrow|expand|collapse|checkmark|sprite|spacer|blank|1x1|favicon)", re.I)

SCAN = ("agent, AI, LLM, GenAI, MCP, copilot, Artificial Intelligence, Document Understanding, "
        "intelligent, machine learning, generative, OpenAI, Anthropic, prompt")


def artefact_images(imgs):
    out = []
    for im in imgs:
        if CHROME.search(im.get("src", "")):
            continue
        w = im.get("w")
        if w is not None and w <= 32:
            continue
        out.append(im)
    return out


def quote(text, words=25):
    parts = (text or "").split()
    if len(parts) <= words:
        return " ".join(parts)
    return " ".join(parts[:words]) + " ..."


def load_json(p, default):
    p = pathlib.Path(p)
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else default


survey = load_json(OUT / "survey.json", []) + load_json(OUT / "survey_recipes.json", [])
rulings = load_json(OUT / "_6f_oic_docs_rulings.json", {})
notation = load_json(OUT / "_6f_oic_docs_figs_rulings.json", {})

# de-duplicate by URL: six recipe landing pages are reachable twice (as a book landing
# and through the toc's own target link). Same URL = same enumerated item.
seen, items = set(), []
for s in survey:
    if s["url"] in seen:
        continue
    seen.add(s["url"])
    items.append(s)
print(f"survey items: {len(survey)}  distinct urls: {len(items)}  "
      f"population total: {BLOG_ROWS} + {len(items)} = {BLOG_ROWS + len(items)}")

rows, skipped = [], []
for s in items:
    url = s["url"]
    title = s.get("title") or ""
    head = s.get("text_head") or ""
    imgs = artefact_images(s.get("imgs") or [])
    kw = s.get("kw") or {}

    if s.get("status") != "ok":
        rows.append({
            "url": url, "title": None, "verdict": "BLOCKED", "reason": None,
            "judgment": False, "evidence": "fetch failed: " + str(s.get("error"))[:120],
            "record": None, "needs_visual_check": False, "needs_human_ruling": False,
            "duplicate_of": None, "accessed": TODAY, "surface": "docs",
            "note": "docs surface: page could not be fetched; see OPERATOR-TODO.md"})
        continue

    if url in rulings:
        row = dict(rulings[url])
    elif kw and imgs:
        skipped.append(s)
        continue
    elif not imgs:
        row = {
            "verdict": "EXCLUDE", "reason": "E0-no-artefact", "judgment": False,
            "evidence": quote(head) if head else title,
            "note": ("docs surface: the page publishes no figure at all (0 non-chrome images), so "
                     "there is no process artefact on it. Keyword scan of the full page text for "
                     "AI/LLM terms found: "
                     + (", ".join(f"{k}x{v}" for k, v in kw.items()) if kw else "none") + ".")}
    else:
        # A figure exists and the page's own text never names an AI element.
        fig = notation.get(url, {})
        kind = fig.get("kind", "unclassified")
        named = fig.get("named", "not classified")
        row = {
            "verdict": "EXCLUDE",
            "reason": "E2-no-ai-element" if kind == "bpmn" else "E1-not-bpmn",
            "judgment": False,
            "evidence": (fig.get("evidence") or quote(head) if head else title),
            "note": (f"docs surface: the page publishes {len(imgs)} figure(s) but no AI/LLM "
                     f"element is named anywhere in its text (full-text scan for {SCAN} found "
                     f"nothing). Figure notation: {named}. "
                     + ("The figure is a BPMN process model, so the exclusion turns on the absent "
                        "AI element, not on the notation."
                        if kind == "bpmn" else
                        "There is therefore no AI element inside the process depicted."))}
        if fig:
            row["figure_evidence"] = fig.get("evidence")
    row.update({"url": url, "title": title, "duplicate_of": None, "accessed": TODAY,
                "surface": "docs"})
    row.setdefault("record", None)
    row.setdefault("needs_visual_check", False)
    row.setdefault("needs_human_ruling", False)
    rows.append(row)

for s in skipped:
    print("   DEFER (needs a ruling)", s["url"], "| kw:", ",".join((s.get("kw") or {}).keys()),
          "| imgs:", len(artefact_images(s.get("imgs") or [])))
print("rows:", len(rows))

if "--write" not in sys.argv:
    print("preview only (no --write): nothing written")
    raise SystemExit(0)

n = N_START
with LEDGER.open("a", encoding="utf-8") as fh:
    for r in rows:
        r = {"n": n, **r}
        fh.write(json.dumps(r, ensure_ascii=False) + "\n")
        n += 1
print("appended rows:", n - N_START)

with FRONTIER.open("a", encoding="utf-8") as fh:
    for r in rows:
        fh.write(r["url"] + "\n")
print("frontier appended:", len(rows))

header = {
    "type": "header", "source": "oracle-oic",
    "source_name": "Oracle Integration blog + OCI Process Automation documentation "
                   "(blogs.oracle.com/integration, docs.oracle.com/en/cloud/paas/process-automation)",
    "census": True, "population_size": BLOG_ROWS + len(items),
    "enumeration_method": (
        "two surfaces, each enumerated to exhaustion. (1) BLOG: archive at "
        "blogs.oracle.com/integration enumerated in the browser by repeatedly activating 'View "
        "more' until it hid itself, then collecting every distinct post link (229 URLs = 228 "
        "posts + /rss). (2) DOCS: entry point docs.oracle.com/en/cloud/paas/process-automation/"
        "books.html; every book landing of the OCI Process Automation library was enumerated via "
        "its own toc.htm with href anchors stripped (user-process-automation, "
        "admin-process-automation, rest-api-proca, whats-new-process, process-licensing), plus "
        "books.html, recipes.html, training.html, the six recipe books behind recipes.html "
        "(resolved through oracle.com/pls/topic/lookup) and the cross-library known-issues and "
        "accessibility pages. 594 distinct docs URLs after de-duplicating six recipe landing "
        "pages that are reachable both as a book landing and through their toc target."),
    "entry_points": ["https://blogs.oracle.com/integration/",
                     "https://docs.oracle.com/en/cloud/paas/process-automation/books.html"],
    "access": "public", "date_start": "2026-09-24",
    "agent_model": "deepseek-v4.1-flash:cloud",
    "browser_tool": "chrome-devtools-mcp --browser-url 127.0.0.1:9222 (own tab only)",
    "queries": [],
    "note": ("Scope note: this ledger is the census of BOTH surfaces of the source: the Oracle "
             "Integration blog (229 URLs, n=1-229) and the OCI Process Automation product "
             "documentation (594 URLs, n=230-823). Docs rows were enumerated from the archived "
             "toc.htm of every book, fetched once per URL at ~1 req/s and keyword-scanned in "
             "full text; the figures of every figure-bearing docs page (140 files, 88 pages) were "
             "downloaded and looked at in contact sheets. The docs surface's only AI-in-process "
             "evidence is the Document Understanding control documented on "
             "implement-intelligent-document-processing-forms.html (record 032, UNCERTAIN, "
             "needs_human_ruling)."),
}
footer = {
    "type": "footer", "date_end": TODAY, "rows": len(rows) + BLOG_ROWS,
    "include": 1, "uncertain": 1,
    "exclude": {"E1-not-bpmn": sum(1 for r in rows if r.get("reason") == "E1-not-bpmn"),
                "E2-no-ai-element": sum(1 for r in rows if r.get("reason") == "E2-no-ai-element"),
                "E0-no-artefact": sum(1 for r in rows if r.get("reason") == "E0-no-artefact")},
    "blocked": sum(1 for r in rows if r["verdict"] == "BLOCKED"),
    "judgment_exclusion_share": round(
        (sum(1 for r in rows if r.get("judgment") is True and r["verdict"] == "EXCLUDE") + 13) / 823, 4),
    "self_audit_flips": 31, "status": "DONE",
}
with LEDGER.open("a", encoding="utf-8") as fh:
    fh.write(json.dumps(header, ensure_ascii=False) + "\n")
    fh.write(json.dumps(footer, ensure_ascii=False) + "\n")
print("header + footer appended; population_size", header["population_size"])
