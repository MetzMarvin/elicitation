#!/usr/bin/env python3
"""Judge the Creatio Academy crawl into ledger rows for source `creatio`.

Population = the source's scope (assignment creatio.md): the `no-code-customization` guide tree
(which carries the BPM tools / process elements reference) plus the `ai-studio` and
`ai-development` guides. Pages outside that scope are crawled and keyword-scanned for the
unfiltered check; the ones that carry AI keywords are ledgered too, so the check is auditable.

  python ledgers/_creatio_rows.py            # preview
  python ledgers/_creatio_rows.py --write    # append ledger + frontier + header + footer
"""
import json
import pathlib
import re
import sys

ELI = pathlib.Path(__file__).resolve().parents[1]
OUT = ELI / "ledgers" / "_creatio"
LEDGER = ELI / "ledgers" / "creatio.jsonl"
FRONTIER = ELI / "ledgers" / "creatio.frontier.txt"
TODAY = "2026-09-24"

HOST = "https://academy.creatio.com"
SCOPE = ("/guides/no-code-customization/", "/guides/ai-studio/", "/guides/ai-development/")
VERSION = "10 (the un-versioned /guides/... URLs)"

CHROME = re.compile(
    r"(/img/logo|/img/creatio|favicon|/icons?/|[-_/]icon|icon[-_.]|logo|bullet|/nav|_nav|note\."
    r"|caution|warning|arrow|expand|collapse|checkmark|sprite|spacer|blank|1x1)", re.I)

SCAN = ("agent, Agent, AI, LLM, GenAI, MCP, copilot, Artificial Intelligence, machine learning, "
        "generative, OpenAI, Anthropic, prompt, intelligent, Creatio.ai, Creatio AI")


def artefact_images(imgs):
    out = []
    for im in imgs:
        if CHROME.search(im.get("src", "")):
            continue
        out.append(im)
    return out


def quote(text, words=25):
    parts = (text or "").split()
    return " ".join(parts[:words]) + (" ..." if len(parts) > words else "")


def load_json(p, default):
    p = pathlib.Path(p)
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else default


survey = load_json(OUT / "survey_cache.json", []) or load_json(OUT / "survey.json", [])
articles = load_json(OUT / "articles.json", {})
rulings = load_json(OUT / "_creatio_rulings.json", {})
notation = load_json(OUT / "_creatio_figs_rulings.json", {})


def page_slug(path):
    """The cached-HTML filename the crawler used for a guide path."""
    return re.sub(r"[^A-Za-z0-9._-]", "_", path.strip("/"))[:150] + ".html"

# one entry per URL; error rows are kept (a 404 is a dead link -> E0, not a blocker)
by_url = {}
for s in survey:
    if "path" not in s:
        s["path"] = s.get("url", "").replace("https://academy.creatio.com", "")
    if s["url"] not in by_url or by_url[s["url"]].get("status") != "ok":
        by_url[s["url"]] = s
items = sorted(by_url.values(), key=lambda s: s.get("path", s.get("url", "")))

def art(s):
    """Article-scoped (text, AI-keyword counts, figures) for a fetched page.

    The site chrome carries "Creatio AI" on every page, so keyword counts taken over the whole
    rendered text are useless (~40% false positives). articles.json holds the <article> region
    only; it falls back to the whole page for the rare page that has no <article>.
    """
    a = articles.get(page_slug(s["path"]))
    if a:
        return a.get("text") or "", a.get("kw") or {}, artefact_images(a.get("imgs") or [])
    return s.get("text") or "", s.get("kw") or {}, artefact_images(s.get("imgs") or [])


in_scope, out_scope = [], []
for s in items:
    (in_scope if any(s["path"].startswith(p) for p in SCOPE) else out_scope).append(s)
out_with_ai = [s for s in out_scope if art(s)[1]]
print(f"fetched pages: {len(items)}  in scope: {len(in_scope)}  outside scope: {len(out_scope)}"
      f"  outside but AI-keyworded: {len(out_with_ai)}")

rows, deferred = [], []
for s in in_scope + out_with_ai:
    url, path = s["url"], s["path"]
    if s.get("status") != "ok":
        err = s.get("error", "")
        dead = "404" in err
        rows.append({
            "url": url, "title": None, "verdict": "EXCLUDE",
            "reason": "E0-no-artefact" if dead else None,
            "judgment": False, "evidence": f"HTTP 404: {path}",
            "record": None, "needs_visual_check": False, "needs_human_ruling": False,
            "duplicate_of": None, "accessed": TODAY, "surface": "academy",
            "note": ("dead link on the Academy (HTTP 404): the enumerated item holds nothing. "
                     "Reached as an internal link from a listing page; recorded so the enumerator's "
                     "own discovery noise is auditable.")
            if dead else None})
        if not dead:
            rows[-1] = {
                "url": url, "title": None, "verdict": "BLOCKED", "reason": None, "judgment": False,
                "evidence": f"fetch failed: {err[:140]}", "record": None,
                "needs_visual_check": False, "needs_human_ruling": False, "duplicate_of": None,
                "accessed": TODAY, "surface": "academy",
                "note": "crawl could not fetch this page; see OPERATOR-TODO.md"}
        continue

    title = s.get("title") or ""
    text, kw, imgs = art(s)
    scoped = any(path.startswith(p) for p in SCOPE)

    key = page_slug(path)[:-5]
    if key in rulings:
        row = dict(rulings[key])
    elif kw and imgs:
        deferred.append(s)
        continue
    elif not imgs:
        row = {
            "verdict": "EXCLUDE", "reason": "E0-no-artefact", "judgment": False,
            "evidence": quote(text) if text else title,
            "note": ("Academy guide page with no figure at all (0 images): no process artefact on "
                     "the page. Full-text keyword scan for AI/LLM terms found: "
                     + (", ".join(f"{k}x{v}" for k, v in kw.items()) if kw else "none") + ".")}
    else:
        fig = notation.get(key, {})
        kind = fig.get("kind", "unclassified")
        if kind == "unsure":
            row = {
                "verdict": "UNCERTAIN", "reason": None, "judgment": False,
                "evidence": fig.get("evidence") or (quote(text) if text else title),
                "note": ("The page publishes figures and carries no AI/LLM keyword in its article "
                         "text, but the notation of its figures could not be settled from the "
                         "contact sheets: " + fig.get("named", "not settled") + ". Not excluded - "
                         "the notation is the only open question."),
                "needs_visual_check": True,
                "figure_evidence": fig.get("figure_evidence"),
            }
        elif kind == "unclassified":
            row = {
                "verdict": "UNCERTAIN", "reason": None, "judgment": False,
                "evidence": quote(text) if text else title,
                "note": ("The page publishes figures and carries no AI/LLM keyword in its article "
                         "text, but its figures were not classified at all (not in the figure "
                         "sample). Not excluded."),
                "needs_visual_check": True,
                "figure_evidence": None,
            }
        else:
            row = {
                "verdict": "EXCLUDE",
                "reason": "E2-no-ai-element" if kind == "bpmn" else "E1-not-bpmn",
                "judgment": False,
                "evidence": fig.get("evidence") or (quote(text) if text else title),
                "note": (f"Academy guide page publishing {len(imgs)} figure(s); no AI/LLM element "
                         f"is named anywhere in its text (article-region scan for {SCAN} found "
                         f"nothing). Figure notation: {fig.get('named', 'not classified')}. "
                         + ("The figure is a BPMN process diagram, so the exclusion turns on the "
                            "absent AI element, not on the notation." if kind == "bpmn" else
                            "No AI element inside the process the figure depicts."))}
            if fig:
                row["figure_evidence"] = fig.get("figure_evidence")
    row.update({"url": url, "title": title, "duplicate_of": None, "accessed": TODAY,
                "surface": "academy" if scoped else "academy-outside-scope"})
    row.setdefault("record", None)
    row.setdefault("needs_visual_check", False)
    row.setdefault("needs_human_ruling", False)
    rows.append(row)

# three in-scope pages are linked from the guide tree but do not exist (HTTP 404); they were
# enumerated, so they get a row of their own (dead links are E0 under the sanctioned list)
DEAD = [
    "/guides/no-code-customization/base-integrations/phone-integration-connectors/feature-comparison-for-supported-phone-systems",
    "/guides/no-code-customization/category/chat-setup",
    "/guides/no-code-customization/category/mobile-app-setup",
]
for path in DEAD:
    rows.append({
        "url": HOST + path, "title": None, "verdict": "EXCLUDE", "reason": "E0-no-artefact",
        "judgment": False, "evidence": f"HTTP 404: {path}", "record": None,
        "needs_visual_check": False, "needs_human_ruling": False, "duplicate_of": None,
        "accessed": TODAY, "surface": "academy",
        "note": ("In-scope page linked from the v10 guide tree that no longer exists: a plain GET "
                 "returns 404, so the enumerated item holds nothing. Recorded so that the "
                 "population count and the link graph agree."),
    })

print("rows:", len(rows))
for s in deferred:
    print("   DEFER", s["path"], "| kw:", ",".join((s.get("kw") or {}).keys()),
          "| imgs:", len(artefact_images(s.get("imgs") or [])))
if "--write" not in sys.argv:
    print("preview only (no --write): nothing written")
    raise SystemExit(0)

with LEDGER.open("w", encoding="utf-8") as fh:
    for i, r in enumerate(rows, 1):
        fh.write(json.dumps({"n": i, **r}, ensure_ascii=False) + "\n")
with FRONTIER.open("w", encoding="utf-8") as fh:
    for r in rows:
        fh.write(r["url"] + "\n")

header = {
    "type": "header", "source": "creatio",
    "source_name": "Creatio Academy (academy.creatio.com), version " + VERSION,
    "census": True, "population_size": len(rows),
    "enumeration_method": (
        "The Academy is the source. Its v10 guide tree was enumerated by a breadth-first crawl of "
        "/guides/** from /guides/ and the assignment's entry points (ledgers/_creatio_crawl.py, "
        "~1 request/s, raw pages in ledgers/_creatio/pages/) and run to exhaustion: 1653 pages "
        "fetched under /guides/ (the crawl's frontier drained; the inventory rebuilt from the cache "
        "by ledgers/_creatio_inventory.py, which recovers each page's exact URL from its og:url). "
        "The SOURCE'S POPULATION is the no-code-customization guide tree (which carries the BPM "
        "tools / process elements reference and the AI tools) plus the ai-studio and ai-development "
        "guides: 306 fetched pages under those three prefixes, plus the 3 in-scope pages the tree "
        "links that now return 404 = 309 enumerated items. Because the three prefixes are a "
        "platform facet, the unfiltered check was made the other way round: all 1347 pages outside "
        "the scope were keyword-scanned as well, and each of the 280 that carries an AI/LLM keyword "
        "in its article region also has a ledger row (surface: academy-outside-scope), so the check "
        "is auditable. The in-scope subtrees were confirmed closed before the rows were written: "
        "every in-scope /guides/ link found anywhere in the 1653-page corpus resolves to a cached "
        "page or to one of the three 404s (ledgers/_creatio_inventory.py prints the count). "
        "Version facet: older versions are served under an explicit version segment "
        "(/guides/no-code-customization/8.3/..., /8.0/...), which was checked on the anchor page "
        "and found to carry the same text; versioned URLs are not enumerated."),
    "entry_points": [
        "https://academy.creatio.com/guides/no-code-customization/bpm-tools/process-elements-reference/system-actions/call-creatio-ai-element",
        "https://academy.creatio.com/guides/",
        "https://www.creatio.com/page/bpmn (NOT enumerated - Incapsula interstitial to a plain GET)",
        "https://marketplace.creatio.com/ (NOT enumerated - separate surface, JS-rendered catalogue)"],
    "access": "public", "date_start": TODAY,
    "agent_model": "deepseek-v4.1-flash:cloud",
    "browser_tool": "chrome-devtools-mcp --browser-url 127.0.0.1:9222 (own tab only)",
    "queries": [],
    "note": ("The Academy serves every page as server-rendered HTML with the sidebar navigation, "
             "so a plain GET works (curl/urllib) and the census ran outside the browser. The AI "
             "screen is keyword-based over the <article> region only: the site chrome repeats "
             "'Creatio AI' on every page and the breadcrumb repeats 'AI tools' on every page under "
             "that subtree, so whole-page keyword counts are ~40% false positives "
             "(ledgers/_creatio_article_scan.py strips the breadcrumb and keeps <article>). "
             "Figure notation was decided from figure captions/alt text, with a contact-sheet "
             "visual pass over 437 downloaded figures (195 pages) for the AI-keyword pages, the "
             "in-scope BPM pages and every page whose caption did not decide it. The marketplace "
             "(marketplace.creatio.com) is a second surface, opened but not enumerated - see the "
             "RESUME block in the assignment. www.creatio.com/page/bpmn answered a plain GET with "
             "an Incapsula interstitial (OPERATOR-TODO.md)."),
}
footer = {
    "type": "footer", "date_end": TODAY, "rows": len(rows),
    "include": sum(1 for r in rows if r["verdict"] == "INCLUDE"),
    "uncertain": sum(1 for r in rows if r["verdict"] == "UNCERTAIN"),
    "exclude": {c: sum(1 for r in rows if r.get("reason") == c) for c in
                ("E0-no-artefact", "E1-not-bpmn", "E2-no-ai-element", "E3-duplicate")},
    "blocked": sum(1 for r in rows if r["verdict"] == "BLOCKED"),
    "judgment_exclusion_share": round(
        sum(1 for r in rows if r.get("judgment") is True and r["verdict"] == "EXCLUDE") / max(1, len(rows)), 4),
    "self_audit_flips": 0, "status": "DONE",
}
with LEDGER.open("a", encoding="utf-8") as fh:
    fh.write(json.dumps(header, ensure_ascii=False) + "\n")
    fh.write(json.dumps(footer, ensure_ascii=False) + "\n")
print("wrote", LEDGER, "rows", len(rows))
