---
source: trisotech
source_name: Trisotech (Digital Enterprise Suite — blog, webinars, connectors)
source_type: vendor site (blog + webinar library + connector catalogue)
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: YES
  C2_native_bpmn20: YES
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES
access: public
population_type: enumerable
population_estimate: 743
effort: large
needs_logged_in_browser: false
status: DONE
---

## Criteria evidence

- **C1 YES** — https://www.trisotech.com/bpmn-user-tasks-for-humans-and-ai-agents/
  (2026-09-22): "Modern workflow applications can assign tasks to humans, AI agents, or AI
  agents operating under human supervision within the same orchestrated process." Same
  page: "Attendees will learn how to model explicit responsibility, supervision, and
  handoff patterns between humans and AI agents while maintaining transparency, governance,
  and execution control within BPMN workflows."
- **C2 YES** — same page, and the vendor's whole product line is BPMN/DMN/CMMN standards
  tooling (OMG BPM+ family). The sitemap carries `/tag/bpmn/`, `/5-min-intro-to-bpmn/`,
  `/bpmn-in-action/`, `/standardizing-bpmn-labels/`, `/instance-alignment-in-bpmn/`,
  `/bpmn-modeling-with-method-and-style/`. Trisotech is a BPMN-notation vendor first.
- **C3 YES** — blog, webinar and connector pages served anonymously. Webinar *recordings*
  may sit behind a registration form — check per item and record `BLOCKED` if so, rather
  than excluding; the abstract page itself is public and is often evidence enough.
- **C4 YES** — Trisotech tooling is used by Mayo Clinic, Dana-Farber, Intermountain Health
  (case-study pages in the sitemap) and it is the tooling behind Bruce Silver's "BPMN
  Method and Style", which is the most widely cited practitioner BPMN methodology. Strong
  practitioner-discourse presence, which is exactly what C4 asks for.

## Entry points

- **`https://www.trisotech.com/sitemap.xml`** — the enumeration entry point. Parsed
  2026-09-22: **1625 `<loc>` entries**, of which **882 are `digital-enterprise-suite-release-notes-*`**
  and **743 are content pages**. 76 content pages have an AI-ish slug
  (`ai`, `agent`, `genai`, `llm`, `copilot`).
- `https://www.trisotech.com/blog/` — blog index
- `https://www.trisotech.com/webinars/` — webinar library (abstract + recording per item)
- `https://www.trisotech.com/presentations/` — presentation decks, often the same content
  as a webinar under a `-presentation` slug
- `https://www.trisotech.com/articles/`, `/infographics/`, `/in-the-news/`
- `https://www.trisotech.com/tag/ai/`, `/tag/bpmn/`, `/tag/automation/`, `/tag/process/`
- `https://www.trisotech.com/connector/` — connector catalogue, including
  `/openai-connector/`, `/eden-ai-connector/`, `/pinecone-connector/`,
  `/microsoft-text-analytics-api-v2-0-connector/`

## Enumeration instructions

1. Frontier = the **743 content pages** from the sitemap. **Drop the 882 release-notes
   pages from the frontier only if you first confirm they carry no diagrams** — spot-check
   five of them, record the check in the ledger header, and if any carries a diagram put
   all 882 back. Do not drop them on the assumption that release notes are boring.
2. Do **not** enumerate only the 76 AI-slug pages. That is a keyword filter on the
   population, which shared rules section 6 forbids. The 76 figure is recorded here purely
   so the facet cross-check is cheap.
3. Watch for the `-presentation` slug pairs (`/harness-genai-and-agentic-ai/` and
   `/harness-genai-and-agentic-ai-presentation/`). If the two carry the *same* diagram,
   the second is `E3-duplicate` with `duplicate_of` set. If the presentation carries extra
   slides with extra diagrams, it is a separate artefact. Check, do not assume.

## Artefact mechanics

- **Blog/article pages**: static diagram images. Capture the original asset at native
  resolution.
- **Webinar pages**: an abstract plus an embedded video. Diagrams live *inside* the video,
  which is the hardest capture case in the whole sample. If the abstract names BPMN
  elements (as the anchor page does) that is good prose evidence, verdict `UNCERTAIN` with
  `needs_visual_check: true` and a note that the artefact is a video frame. Do not
  transcribe videos.
- **Presentation pages**: often a slide deck, which may be the cheapest route to a clean
  diagram image for the same content as a webinar.
- **Connector pages** (`/openai-connector/` etc.) show the connector as a BPMN service task
  in a modelled process — likely a rich, under-noticed seam. Include the connector
  catalogue in the frontier.
- No downloadable `.bpmn` was confirmed on the public site in Pass 1; Trisotech's modeller
  is a SaaS product, so expect images rather than XML.

## Known gotchas

- **The release-notes noise ratio is extreme** (882 of 1625 URLs, 54%). Budget for it and
  do not let it look like the census stalled.
- Duplicate `<loc>` entries exist in the sitemap (e.g.
  `digital-enterprise-suite-release-notes-september-18-2026` appears twice with different
  `lastmod`). Deduplicate the frontier by URL and say so.
- Some sitemap `lastmod` values are internally inconsistent (2025 release notes dated
  2026). Do not use `lastmod` to scope the census.
- `/tag/*` URLs are index pages, not artefacts — they belong in `E0-no-artefact` if
  enumerated, not silently dropped.
- Trisotech content is heavily healthcare-flavoured (FHIR, HL7, clinical pathways). "Not
  enterprise-grade" and "domain-specific" are **not** exclusion grounds.

## Spot checks performed by Pass 1

Spot checks only, not verdicts:

- `/bpmn-user-tasks-for-humans-and-ai-agents/` — opened; carries both the C1 and C2 quotes.
  It is a **webinar** page, so its artefact is inside a video: a good early warning of the
  capture problem described above.
- `sitemap.xml` — fetched and counted (1625 / 882 / 743 / 76).

## RESUME

(empty — census finished; population exhausted, 1622/1622 rows)

## Census record (elicitation-6f, 2026-09-25; frontmatter set to `status: DONE` 2026-09-27)

**Status: DONE.** Population exhausted, 1622 of 1622 rows judged — re-checked 2026-09-27: the
ledger is 1624 lines (header + 1622 rows + footer), the frontier is 1622, `tools/audit.py
trisotech` → `problems: none`, and `ledgers/_ts_quotes.py` → **0 failures** (all 1622 evidence
strings tested against the page each row judges). Verdicts: EXCLUDE 1586 (E0-no-artefact 937,
E2-no-ai-element 610, E1-not-bpmn 38, E3-duplicate 1), INCLUDE 8, UNCERTAIN 28, BLOCKED 0;
judgement exclusions 53 (3.3%, under the 10% gate); review queue 25 `needs_visual_check`
(22 video pages, 2 decks, 1 figure) and 5 rulings; 36 corpus records. The frontmatter was the
last thing still on `READY` — the census itself was finished on 2026-09-25 and is unchanged.
`OPERATOR-TODO.md`: **P9** covers this source (the one gated webinar recording) and was closed by
the operator's 2026-09-26 ruling that recordings are not an admissible source for this pass, which
superseded all 22 video rows back to `UNCERTAIN` + `needs_visual_check`; the five open rulings are
the vendor-claim-vs-visible-element question described below.

### Population and method

`sitemap.xml` (1625 `<loc>`) de-duplicated to **1622 unique URLs**, frozen before any row was
judged: 854 release-note pages and 768 content pages. The assignment predicted 882/743/1625; the
delta (the 3 duplicate `<loc>` entries plus a different family split) is recorded in the ledger
header and was not reconciled — the population frozen is what was actually fetched and saved. Every
URL was fetched and its HTML kept in `ledgers/trisotech.raw/`, so every row rests on a page that was
really opened. **No keyword filter anywhere**: `sitemap lastmod` was ignored as untrustworthy, all
854 release notes stayed in the frontier until the family was cleared on evidence, and the AI-slug
facet the assignment warned about was never used (see the cross-check below).

Each page's *own* content region was extracted (`<main data-pagefind-body>`, minus the
related-content carousel) — screening raw HTML would make 100% of pages look AI-flavoured, because
the navigation and carousel carry other pages' titles and AI words. Unfiltered AI screen result: an
AI/LLM term appears in the own region of **146 of the 768 content pages**; the 76 AI-slug pages of
the assignment are a subset of those, and the AI-bearing pages *outside* that facet were judged in
the same pass, so nothing was lost by declining the facet.

Routes by which artefacts are published: 514 content pages carry images, 142 embed YouTube video,
106 embed SlideShare decks (2924 slides downloaded from the embeds' slide-image URLs), 4 are
text-only, 2 are dead deck embeds; **no `.bpmn`/`.dmn`/`.cmmn` file is published anywhere** in the
source (checked all 768 saved content pages), so notation had to be read from the drawings and their
labels.

**The deck seam, and the tooling trap it hid.** 105 of the 106 deck hosts publish the deck's per-slide
text (SlideShare `transcript` array), which is textual, cheap, stronger than a picture, and lets the
whole deck family be screened unfiltered — every slide of every deck, not a keyword subset. 43 decks
carry an AI/LLM term in their slide text (`trisotech.raw/deck_ai.txt`). The ledger's mechanical branch
(`ledgers/_ts_rows.py emit`) screens only the page's own text and its figure file names, so it cannot
see a deck's slide text at all: it produced 23 placeholder UNCERTAIN rows and factually wrong
mechanical notes for the rest. All **44 deck rows** (the 43 slide-AI decks plus
`5-min-intro-to-bpmn-presentation`, whose own page text narrates the AI task inside its diagram) were
therefore judged by hand in `batch7`, each with a verbatim quote from the page or the deck's per-slide
text and, where a diagram is the artefact, a full-size capture. 43 deck rows now carry
`judgment: true` (19 E1, 14 E2, 5 INCLUDE, 5 UNCERTAIN).

Documented deck-lexicon false positives (all dismissed with the quote in the row's note): **"Business
Agents"** — the SDMN actor-role column of the SDMN / Business & Digital Transformation slide, in four
insurance/banking decks; **"Handler Agents"** — the WfMC Workflow Reference Model's handler
components in the 2011 French BPM deck; **"predictive"/"PMML"** — prose about predictive-model
markup, not an AI element.

Ledger mechanics: `ledgers/_ts_rows.py emit` builds `trisotech.jsonl` (header + 1622 rows + footer)
and `trisotech.frontier.txt` (1622 lines) from `trisotech.raw/screen.json` + the append-only
`trisotech.raw/dispositions.jsonl` (164 rows, last row per key wins), applied from batch files by
`ledgers/_ts_rec.py`; `ledgers/_ts_quotes.py` is the evidence audit; `ledgers/_ts_deck2.py` /
`_ts_deck3.py` render slide sheets and read the per-slide text.

### Headline finding: this is the source where AI gets *inside* the BPMN diagram

Four distinct AI-in-process constructs are published here, all captured:

1. **AI as the performer of a BPMN user task.** The vendor's own construct: the task keeps its shape
   and gains an AI performer. Documented in prose and in the modeller's panel at record **026**, and
   drawn on the task itself in record **027** (the blue "AI Reviewer" performer badge on "Evaluate
   Appraisal Quality", twice: human-supervised and unsupervised).
2. **A prompt/LLM-execution task inside the process.** Records **028** ("Prompt Execution" plus the
   two prompt-building tasks and the prompt datastore, in a stress-test loop) and **029**
   ("Execute Term Prompt" / "Print Prompt" in the legal term-extraction pipeline).
3. **A task that invokes an ML model.** Record **030**: the "PMML Predictive Model Task" between the
   external service task and the clinical-measure task, which the vendor's own narration calls
   "a PMML or Predictive Model task (an AI kind of task)".
4. **An NLP/ML pipeline published as BPMN tasks.** Record **031**: "NLP Detection" → "Concept
   Lifting" → "Semantic Lifting", with the deck naming the pre-trained services behind them.

The counter-case is just as clear and is what the five open rulings are about: the vendor repeatedly
**asserts** AI agents inside pathways while the BPMN diagram it publishes for those pathways has no
AI element in it (record **033**: "AI agents act as performers within orchestrated pathways" /
"Agent as Performer", over a decision-and-data pipeline with no AI marker; record **036**: the
binding *catalogue* — "REST call to an LLM", "Agent as Performer", "Expose BPM+ Models as MCP
Servers" — drawn as BPMN task shapes with no process around them). Deciding whether the vendor's
claim or a visible element is required settles several rows at once.

### Verdicts

| | |
|---|---|
| rows | 1622 = population |
| EXCLUDE | 1586 — E0-no-artefact 937, E2-no-ai-element 610, E1-not-bpmn 38, E3-duplicate 1 |
| INCLUDE | 8 (3 figure artefacts, 5 deck artefacts) |
| UNCERTAIN | 28 (22 video pages, 5 decks, 1 figure) — all with full records |
| BLOCKED | 0 |
| judgement exclusions | 53 (3.3%) — the false-negative review queue, well under the 10% gate |

The 38 E1 rows are 19 decks, 18 figure pages and 1 video page; every one names in its note what the
drawing is instead (DMN/CMMN/SDMN models, architecture and layer drawings, decision canvases, AI
taxonomy slides, capability schematics). The release-note family is E0 on evidence: a mechanical
screen over all 854 (0 figures, 0 iframes, 0 own-region SVG, 0 model files) plus six pages rendered
and inspected by eye, all of them changelogs — and the family is dense with AI words ("AI Performers",
"AI Model Generators", "Anthropic Haiku model integration"), which is exactly why it was not dropped
by assumption or by keyword.

### The 36 records

- **22 video pages (004–025)** — the artefact lives inside the embedded video, so each is UNCERTAIN
  with `needs_visual_check` and a poster-frame capture: the honest verdict for "the diagram is real
  but only a frame of it is reachable without transcribing video". This is the single largest class of
  open items in the source and the method chapter should report it as such.
- **Deck artefacts (027–036)** — 5 INCLUDE, 5 UNCERTAIN; each carries a full-size capture of the
  diagram.
- **Figure artefacts (001, 003, 026)** — 3 INCLUDE; **002** (the digital-twin SDMN data-structure
  model) is UNCERTAIN on the same notation question the operator ruling covers.
- **E3 precedent:** the one duplicate is `ai-fhir-and-bpm-in-suicide-prevention-presentation`, which
  republishes record 001's two BPMN diagrams; `duplicate_of` names record 001. Similar-but-different
  diagrams (a deck and its webinar page, a blog figure and a deck slide) were deliberately **not**
  deduped — that is the reconciliation step's job.

### Evidence audit

`ledgers/trisotech.quotes.txt`: every `evidence` string in all 1622 rows tested as a contiguous
substring of the page's own text (whitespace and curly/straight quotes normalised), and for deck rows
also of that deck's published per-slide text — **0 failures**. Hand-judged rows were machine-checked
at build time too: `_ts_batch7.py` refuses to write a batch whose quotes are not verbatim substrings.
Two hand-written quotes from an earlier batch failed the first run (both joined two sentences across
intervening text) and were corrected in `batch8`; that correction is the reason the audit is clean
rather than merely passing.

### Caveats the researcher should know

1. **The connector seam posited in the assignment did not exist.** Checked: the connector *catalogue*
   is 15 brand logos with one-line blurbs (E0), and the individual connector pages are generated
   operation/parameter listings with no figure at all (`openai-connector`, `eden-ai-connector`,
   `microsoft-text-analytics-api-v2-0-connector` → E0, with the AI mention quoted and dismissed).
   Trisotech never publishes the connector as a BPMN service task on its public site.
2. **Two INCLUDE/UNCERTAIN calls rest on self-declared or notional diagrams** and are flagged in
   their records: 028's slide calls its model a "Notional BPMN Diagram", and 036's is a capability
   schematic with no process flow. Both were kept rather than excluded (the rule is "when in doubt,
   include"), and a reviewer can reclassify either without disturbing anything else.
3. **Deck slides were judged from the published per-slide text, five-column overview sheets and
   full-size views of the diagram slides** — not from a video of the talk. Where a diagram appears
   only inside the video and not on a slide, it is out of reach; that is the 22-row video class.
4. The deck slide *file* index and the transcript index are not always aligned in some decks; every
   capture in `corpus/trisotech/` was verified visually against its slide number before use.
5. Three duplicate `<loc>` entries exist in the sitemap and several `lastmod` values are internally
   inconsistent (2025 release notes dated 2026); neither was used to scope anything.

