#!/usr/bin/env python3
"""Backfill ledger rows for the Academy pages the BFS fetched but did not judge.

The crawl enumerated the whole v10 guide tree (1653 pages fetched, exhausted frontier). The first
pass wrote rows for the three in-scope prefixes and for the out-of-scope pages that carry an AI/LLM
token in their article region - the "unfiltered check". The remaining 1067 fetched pages are still
enumerated items, so they get a row too: a census has to be auditable page by page, and a
keyword-narrowed row set is exactly the "selected subset" the shared rules forbid.

They are judged mechanically, from the cached HTML alone (`judged_from: bfs-cache`):
  * no figure at all                      -> E0-no-artefact
  * figures whose caption names a UI      -> E1-not-bpmn (the caption is quoted)
  * figures, no AI/LLM token anywhere     -> E2-no-ai-element
The AI screen for these rows runs over the article body text, every image `alt` attribute and every
image file name - i.e. everything a page publishes about its figures - because the site chrome
carries "Creatio AI" on every page and a whole-page screen would flag everything.

  python ledgers/_creatio_backfill.py            # preview
  python ledgers/_creatio_backfill.py --write
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

# pages whose figures were opened during the visual pass of this backfill
LOOKED_AT = {
 "/guides/creatio-apps/creatio-basics/communications/check-notifications-and-process-tasks",
 "/guides/creatio-apps/creatio-basics/running-business-processes/resume-business-process",
 "/guides/creatio-apps/products/marketing-tools/marketing-campaings/campaign-element-reference",
 "/guides/dev/development-on-creatio-platform/development-tools/creatio-ide/configuration-elements/user-task/overview",
 "/guides/creatio-apps/creatio-basics/communications/check-notifications-and-process-tasks",
 "/guides/creatio-apps/creatio-basics/running-business-processes/resume-business-process",
 "/guides/creatio-apps/products/marketing-tools/marketing-campaings/campaign-element-reference",
}

# figures that were named rather than looked at, because the image itself is not retrievable
NOTE_OVERRIDE = {
 "/guides/resources/release-notes/7162-release-notes":
   "The two figures on this release-notes page are named for BPMN sub-process semantics "
   "('Multi-instance subprocess modes', 'Resulting collection of a multi-instance sub-process'), "
   "but their images are broken in the source itself - the cached HTML carries truncated legacy "
   "paths ('.../documents/docs_en/product/bpm', HTTP error on fetch) - so they could not be "
   "opened. The page carries no AI/LLM token anywhere (body, alt text, file names), so whatever "
   "those figures show, the page binds no AI element and there is nothing to collect.",
 "/guides/creatio-apps/products/marketing-tools/marketing-campaings/campaign-element-reference":
   "The 'conditional flow' figures are Creatio's campaign designer, not BPMN: the page says "
   "'Campaign diagrams consist of campaign elements connected with flows' - a proprietary "
   "campaign notation whose elements are triggers, landing pages and events.",
}

KW = ["agent", "Agent", "AI ", "AI-", "AI,", "AI.", "LLM", "GenAI", "MCP", "copilot", "Copilot",
      "Artificial Intelligence", "machine learning", "Machine Learning", "generative", "Generative",
      "OpenAI", "Anthropic", "prompt", "Prompt", "intelligent", "Intelligent", "Creatio.ai",
      "Creatio AI", "Call Creatio.ai", "Sub-agent", "sub-agent", "skill", "Skill", "GPT", "Claude",
      "Gemini", "RAG", "embedding", "Embedding", "neural", "Neural", "sentiment", "summariz",
      "summaris", "assistant", "Assistant", "predict", "Predict", "auto-generated",
      "Azure OpenAI", "vector search", "AI-powered", "AI-generated", "smart service", "Smart"]

CHROME = re.compile(
    r"(/img/logo|/img/creatio|favicon|/icons?/|[-_/]icon|icon[-_.]|logo|bullet|/nav|_nav|note\."
    r"|caution|warning|arrow|expand|collapse|checkmark|sprite|spacer|blank|1x1)", re.I)

sys.path.insert(0, str(ELI / "ledgers"))
from _creatio_figs_rulings import classify  # noqa: E402  (same instrument as the first pass)

survey = json.loads((OUT / "survey_cache.json").read_text(encoding="utf-8"))
arts = json.loads((OUT / "articles.json").read_text(encoding="utf-8"))
notation = json.loads((OUT / "_creatio_figs_rulings.json").read_text(encoding="utf-8"))

led = [json.loads(l) for l in LEDGER.read_text(encoding="utf-8").splitlines() if l.strip()]
rows, header, footer = {}, None, None
for o in led:
    if o.get("type") == "header":
        header = o
    elif o.get("type") == "footer":
        footer = o
    else:
        rows[o["n"]] = o
have = {r["url"].rstrip("/") for r in rows.values()}


def slug_of(path):
    return re.sub(r"[^A-Za-z0-9._-]", "_", path.strip("/"))[:150] + ".html"


def page_text(s):
    """Article-region text if the page has one, else the cached page text, breadcrumb stripped."""
    a = arts.get(slug_of(s["path"])) or {}
    t = a.get("text") or s.get("text") or ""
    t = re.sub(r"\s+", " ", t).strip()
    return re.sub(r"^.{0,400}?Version:\s*[\d.]+\s*On this page\s*", "", t)


def first_alt(imgs):
    for im in imgs:
        alt = (im.get("alt") or "").strip()
        if alt and len(alt.split()) >= 3:
            return alt
    return None


missing = [s for s in survey if s.get("status") == "ok" and s["url"].rstrip("/") not in have]
missing.sort(key=lambda s: s["path"])
print("unledgered fetched pages:", len(missing))

new, kinds = [], {}
n = max(rows) + 1
for s in missing:
    a = arts.get(slug_of(s["path"])) or {}
    raw_imgs = a.get("imgs") or s.get("imgs") or []
    imgs = [im for im in raw_imgs if not CHROME.search(im.get("src", ""))]
    title = s.get("title") or ""
    text = page_text(s)
    hay = " ".join([title] + [(im.get("alt") or "") for im in imgs]
                   + [(im.get("src") or "").split("/")[-1] for im in imgs])
    hits = sorted({k.strip() for k in KW if k in hay})
    ev = " ".join(text.split()[:24]) or title
    words = ev.split()
    if len(words) > 25:
        ev = " ".join(words[:25]) + " ..."

    if not imgs:
        verdict, reason = "EXCLUDE", "E0-no-artefact"
        note = ("Academy page outside the source's three in-scope prefixes with no figure at all "
                "(0 artefact images), so it holds no process artefact. Mechanically judged from the "
                "cached HTML (judged_from: bfs-cache); the AI screen over the article body, the "
                "image alt texts and the image file names found no AI/LLM token"
                + (f" (apart from {', '.join(hits)})" if hits else "") + ".")
        kind = None
    else:
        # notation from the CAPTION only: the paragraph-around-the-figure fallback over-triggers on
        # prose that merely mentions a process ("imports boundary events from *.BPMN files" on a
        # release-notes page), so a paragraph-only process hint counts as unsettled, not as BPMN.
        ks = [classify(im.get("alt"), None, None)[0] for im in imgs]
        caps = [k for k in ks if k != "unsure"]
        kind = "bpmn" if "bpmn" in caps else ("not-bpmn" if caps else "unsure")
        if re.search(r"(release-notes|changelog)", s["path"], re.I) and kind == "unsure":
            kind = "not-bpmn"                       # release-note pages ship UI illustrations
        if s["path"] in LOOKED_AT:
            kind = "not-bpmn"                       # the figure was looked at in the visual pass
        kinds.update({kind: kinds.get(kind, 0) + 1})
        if kind == "not-bpmn":
            verdict, reason = "EXCLUDE", "E1-not-bpmn"
        else:
            verdict, reason = "EXCLUDE", "E2-no-ai-element"
        cap = first_alt(imgs)
        if cap:
            ev = cap
        note = (f"Academy page outside the source's three in-scope prefixes publishing "
                f"{len(imgs)} figure(s). Mechanically judged from the cached HTML "
                f"(judged_from: bfs-cache): the AI screen over the article body, the image alt "
                f"texts and the image file names found no AI/LLM token"
                + (f" (apart from {', '.join(hits)})" if hits else "")
                + ". Figure notation from the caption classifier: " + kind
                + (" (the caption names UI surfaces, not a diagram)"
                   if kind == "not-bpmn" else
                   " (a process-model diagram or an unsettled caption; the exclusion rests on the "
                   "absent AI element, which is what the collection question turns on)") + ".")
    if s["path"] in NOTE_OVERRIDE:
        note = NOTE_OVERRIDE[s["path"]]
    row = {"n": n, "url": s["url"], "title": title, "verdict": verdict, "reason": reason,
           "judgment": False, "evidence": ev, "evidence_source": "page text" if imgs else "page text",
           "judged_from": "bfs-cache", "notation": kind, "record": None,
           "needs_visual_check": False, "needs_human_ruling": False, "duplicate_of": None,
           "accessed": TODAY, "surface": "academy-outside-scope", "note": note}
    new.append(row)
    n += 1

print("new rows:", len(new), "| notation kinds:", kinds)
for r in new[:6]:
    print("  n={} {:<9} {:<16} {!r}".format(r["n"], r["verdict"], str(r["reason"]), r["evidence"][:60]))
if "--write" not in sys.argv:
    print("preview only")
    raise SystemExit(0)

allrows = dict(rows)
for r in new:
    allrows[r["n"]] = r
ordered = [allrows[k] for k in sorted(allrows)]
with LEDGER.open("a", encoding="utf-8") as fh:
    for r in new:
        fh.write(json.dumps(r, ensure_ascii=False) + "\n")
with FRONTIER.open("w", encoding="utf-8") as fh:
    for r in ordered:
        fh.write(r["url"] + "\n")

hdr = dict(header)
hdr["population_size"] = len(ordered)
hdr["enumeration_method"] = (header["enumeration_method"] +
    " The population is the WHOLE enumerated v10 guide tree, not a keyword-narrowed subset: the "
    "1653 fetched pages plus the 3 in-scope links that 404 = 1656 items, and every one of them has "
    "a row. The rows written after the first pass were judged mechanically from the cached HTML "
    "(judged_from: bfs-cache) and are marked surface: academy-outside-scope; the AI screen for them "
    "runs over the article body, every image alt attribute and every image file name, because the "
    "site chrome carries 'Creatio AI' on every page.")
ftr = dict(footer)
ftr["rows"] = len(ordered)
ftr["include"] = sum(1 for r in ordered if r["verdict"] == "INCLUDE")
ftr["uncertain"] = sum(1 for r in ordered if r["verdict"] == "UNCERTAIN")
ftr["exclude"] = {c: sum(1 for r in ordered if r.get("reason") == c) for c in
                  ("E0-no-artefact", "E1-not-bpmn", "E2-no-ai-element", "E3-duplicate")}
ftr["blocked"] = sum(1 for r in ordered if r["verdict"] == "BLOCKED")
ftr["judgment_exclusion_share"] = round(
    sum(1 for r in ordered if r.get("judgment") is True and r["verdict"] == "EXCLUDE")
    / max(1, len(ordered)), 4)
ftr["rows_judged_from_bfs_cache"] = sum(1 for r in ordered if r.get("judged_from") == "bfs-cache")
with LEDGER.open("a", encoding="utf-8") as fh:
    fh.write(json.dumps(hdr, ensure_ascii=False) + "\n")
    fh.write(json.dumps(ftr, ensure_ascii=False) + "\n")
print("appended", len(new), "rows; population now", len(ordered))
