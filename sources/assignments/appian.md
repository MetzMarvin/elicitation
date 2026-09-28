---
source: appian
source_name: Appian (product documentation — AI Agents in process models)
source_type: vendor documentation
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: YES
  C2_native_bpmn20: NO (operator ruling 2026-09-25: the Appian process model is Appian's own
    proprietary notation, not BPMN 2.0)
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES
access: public
population_type: enumerable
population_estimate: 25
effort: medium
needs_logged_in_browser: false
status: OUT (C2) - operator ruling 2026-09-25, source ruled out entirely, no census run
---

## Criteria evidence

- **C1 YES** — https://docs.appian.com/suite/help/26.8/use-agents-in-a-process.html
  (2026-09-23): "Integrate your AI agents directly into your business workflows by calling
  them from a process model. This allows you to automate tasks that require generative AI,
  passing contextual data from your process and receiving structured outputs." The
  modelling instruction is explicit: "In your process model, drag the Execute AI Agent
  smart service from the node palette onto the canvas."
- **C2 YES** — https://docs.appian.com/suite/help/26.8/process_modeling.html (2026-09-23):
  "Business Process Model Notation (BPMN) is the standard by which anyone can graphically
  describe their business processes. With Appian, that model isn't just the starting point
  for building your process, it is the process."
- **C3 YES** — `docs.appian.com` served anonymously. The AI Agents pages carry "The
  capabilities described on this page are included in Appian's advanced and premium
  capability tiers. Usage limits may apply." That is a **licence** tier on the product, not
  a paywall on the documentation, so it is **not** a C3 failure. Record it, do not act on it.
- **C4 YES** — Appian is a major enterprise BPM/low-code vendor with its own academy
  (`academy.appian.com`) and community (`community.appian.com`), and it appears as a named
  integration in the UiPath Marketplace application directory.

## Entry points

- `https://docs.appian.com/suite/help/26.8/use-agents-in-a-process.html` — the anchor page
- Sibling pages confirmed by `site:` sweep on 2026-09-23 (titles read from the result list,
  **not opened** — reach them by navigation):
  - "Execute AI Agent Smart Service"
  - "Create and Configure an AI Agent"
  - "AI Agent Reference"
  - "Auditing AI Agent Usage"
  - "Troubleshooting AI agents"
  - "MCP System Tools Reference"
  - "Process Nodes and Smart Services"  ← the full node palette; high value
  - "Manage Processes [Appian Composer]"
- `https://docs.appian.com/suite/help/26.8/process_modeling.html` — process modelling
  overview, carries the C2 claim
- **Version-pinned docs**: the path carries `/26.8/`. Pin one version and record it.

- **Template gallery (added at Gate 1, 2026-09-24):** Appian's app/template gallery was never opened in Pass 1. Reach it by navigating from the vendor site (do not guess the URL) and enumerate it as a sub-population.

## Enumeration instructions

1. Frontier = the **AI Agents documentation branch** plus **"Process Nodes and Smart
   Services"** (the node palette reference, which is where the Execute AI Agent smart
   service sits alongside every other node). Enumerating only the AI branch would miss the
   palette context that makes the placement legible.
2. Pin the docs version (`26.8` at time of writing) and record it in the ledger header.
3. `community.appian.com` is a separate, non-enumerable population. Either scope it out
   explicitly or treat it as a `search-protocol` sub-stream with every query logged.

## Artefact mechanics

- Docs are conventional HTML with a heavy nav shell. **`document.body.innerText` returns the
  product mega-menu first** — target `main`/`.content`, or search the text for the page `h1`
  and slice from there, or you will record navigation chrome as evidence.
- Diagrams are static images of the Appian process modeller canvas. Capture at native
  resolution.
- Prose names nodes explicitly ("smart service", "node palette", "canvas"), which is good
  textual evidence.

## Known gotchas

- **The C2 caveat, and it is the important one for this source.** The same page that claims
  BPMN also says: "Your BPMN standard diagram is actually the perfect starting place for
  your Appian process model." That reads as a *translation* from BPMN into Appian's own node
  palette rather than native BPMN rendering. So the vendor-level C2 is YES, but at
  **artefact level** every diagram must be judged on its own: if a captured Appian process
  model turns out to use Appian-specific shapes rather than BPMN 2.0 notation, that is a
  legitimate `E1-not-bpmn` — **provided you name the notation**. If you cannot tell, the
  verdict is `UNCERTAIN` with `needs_visual_check: true`, never `E1`.
- Appian markets "Process Mining" and a "Process Mining Glossary" heavily. Mining pages are
  analytics, not process artefacts — expect `E0-no-artefact`.
- Appian also ships "Case Management Studio". Case models are not BPMN; judge and name.

## Spot checks performed by Pass 1

Spot checks only, not verdicts:

- `use-agents-in-a-process.html` — opened; full C1 quote and the node-palette instruction
  read from the page body.
- `process_modeling.html` — opened; both BPMN sentences read from the page body, including
  the translation caveat above.

## Ruling (operator, 2026-09-25): OUT (C2) — ruled out entirely

The operator ruled the whole source out on 2026-09-25 — *"Rule out appian entirely, its to
proprietary"* — and took over the crawl. **No census was run and no ledger exists for this
source.** The enumeration below was prepared but is moot; do not resume it.

- **C2 at source level was always the weak one**, and the assignment's own "Known gotchas"
  flagged exactly this: `process_modeling.html` frames BPMN as a *starting place* ("Your
  BPMN standard diagram is actually the perfect starting place for your Appian process
  model"), and `process-model-object.html` documents a **separate** "BPMN View" ("Display
  flow objects according to the BPMN specifications for process models and primitives") next
  to the default **"Enhanced View"** ("Display flow objects with markers on activity
  boundaries that indicate assignment"). A captured Appian process model is drawn in the
  Process Modeler's own shapes with Appian smart services in them; the BPMN rendering is a
  display mode of the same model, not the artefact notation. That is what the operator
  ruled on.
- **What was done before the ruling** (evidence retained, `ledgers/appian.raw/`): the
  population was established unfiltered from the site's own sitemap —
  `robots.txt` → `Sitemap: /suite/help/latest/sitemap.xml` → resolves to
  `/suite/help/26.8/sitemap.xml`, **6714 unique `<loc>`, 0 duplicates**. A digest crawler
  (`crawl.py`) reached **932 of 6714** pages (72 flagged candidates) and wrote
  `html/digest.tsv`, `html/quotes.tsv`, `html/imgs.tsv`, `html/links.tsv`,
  `html/cand/<idx>.html`. `rows.py` (verdict machinery) was written but **never run**;
  `ledgers/appian.jsonl` and `appian.frontier.txt` were **never created**.
- **Pages opened and their evidence, kept for the record** (`n` = 1-based sitemap index):
  - `use-agents-in-a-process.html` (n=167) — C1 in full: "Integrate your AI agents directly
    into your business workflows by calling them from a process model." and "In your process
    model, drag the Execute AI Agent smart service from the node palette onto the canvas."
    Its figure draws the AI node **inside** the process ("Case Intake Agent", robot icon).
  - `process_modeling.html` (n=4057) — the C2 claim and its caveat (quoted above); its
    figures are Process Modeler canvases whose palette lists BPMN element *names* (START
    EVENT, END EVENT, TIMER, RECEIVE MESSAGE, SEND MESSAGE, RULE, SUBPROCESS, SCRIPT TASK,
    USER INPUT TASK, AND) drawn in Appian's own shapes.
  - `process-model-object.html` (n=4055) — the BPMN View / Enhanced View distinction.
  - Document-AI tutorials whose drawn model carries an ML step: n=286 (`tutorial-process.png`,
    "Classify Documents" inside the flow), n=269 (`pattern-classify-extraction.png`,
    "Classify Documents" → XOR → per-document-type extraction), n=287
    (`doc_extraction_tutorial_process.png`). Marketing infographics found alongside them
    (n=173, n=282) are illustrations, not notation.
- **Why nothing is lost by the ruling:** every one of those diagrams is a *proprietary*
  Appian canvas, so under a source-level C2 ruling the census would have produced no
  INCLUDE-able artefact at all — only rows whose verdict turns on exactly the notation
  question the operator has now settled. The ruling removes that question instead of
  burying it in 6714 judgement rows.
- **No `BLOCKED` rows and no OPERATOR-TODO entry**: nothing was unreachable; the crawl was
  stopped because the source was ruled out, not because it was obstructed.

## RESUME

(not applicable — source ruled out; do not resume)

