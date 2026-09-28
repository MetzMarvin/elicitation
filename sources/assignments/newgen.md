---
source: newgen
source_name: Newgen (NewgenONE platform: process modeling / BPM)
source_type: vendor site
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: YES (marketing-level)
  C2_native_bpmn20: YES
  C3_publicly_accessible: YES (marketing); docs unknown
  C4_enterprise_presence: YES
access: public
population_type: not established
population_estimate: 15
effort: small
needs_logged_in_browser: false
status: DONE (elicitation-3a, 2026-09-25; census + 475-page/1117-figure visual backstop complete, audit clean)
---

## Criteria evidence

- **C1 YES (marketing-level)**:
  https://newgensoft.com/platform/process-automation/process-modeling/ (2026-09-24):
  "Build orchestration-ready processes that connect AI agents, human teams, and enterprise
  systems." https://newgensoft.com/platform/business-process-management/: "Orchestrate
  end-to-end enterprise processes by unifying AI agents, business rules, human decisions,
  and enterprise systems."
- **C2 YES**: the process-modeling page says "Visually design simple to complex process
  models with both abstract and BPMN views".
- **C3**: marketing pages are public. Whether the product documentation is public was
  **not established**.
- **C4 YES**: a listed enterprise software vendor.

## First Pass 2 action: establish the population

Only marketing pages were reached. Find out whether Newgen publishes:
(a) public product docs, (b) a template/app marketplace, (c) blog posts with process
diagrams. If none contain diagrams, the census result is zero artefacts. Record that as
the finding.

## Entry points

- The two pages above
- "Tap the Power of GenAI for the Enterprise with…" (Newgen blog) and "NewgenONE Marvin
  GenAI for the Enterprise" (landing.newgensoft.com brochure): result titles, not opened
- The FAQ block on the BPM page ("What do you mean by process modelling in…")

## Known gotchas

- The pages are heavy marketing copy. Distinguish "AI agents *in* processes" from "GenAI
  to design and develop applications" (design-time, E2).
- The brochure on `landing.newgensoft.com` may be form-gated. If so, mark it `BLOCKED` and
  do not fill in the form.

## RESULT (elicitation-3a, 2026-09-25)

`python tools/audit.py newgen` -> `problems: none`.

- **Population 800**, closed as: the site's own 12 sub-sitemaps (607 URLs) **union** every
  in-site route they omit (193 further routes: the whole `/resources/` section, `/platform/`,
  `/solutions/`, `/company/`, `/csr/`, blog posts, country variants such as `/au` and `/in`),
  plus the three public `landing.newgensoft.com` brochure landings. All 800 fetched, all HTTP
  200, **0 BLOCKED** (the brochure is not form-gated). No keyword facet was used, so no
  unfiltered-facet check was required.
- **Ledger**: 800 rows -> EXCLUDE 728 (all `E0-no-artefact`, `judgment: false`),
  UNCERTAIN 72, INCLUDE 0, BLOCKED 0. `judgment_exclusion_share 0.0`.
- **Corpus** `corpus/newgen/`: 243 files = 72 records, 72 `.page.html` archives, 98 `.png`
  captures + 1 `.svg`, `.manifest.json`. All 72 records are `capture_quality: null` because
  this session could not render images; every UNCERTAIN row is `needs_visual_check: true`
  and `needs_human_ruling: true` with a page-specific question.
- **Channels proved complete on this site**: 0 downloadable `.bpmn/.dmn/.vsdx` links in 800
  pages and 304 documents; 0 pages with bpmn: XML; 0 pages with bpmn-js markup; 0 `<pre>`
  diagram blocks; 0 box-drawing sketches. **1 of 800** pages names BPMN
  (`/platform/process-automation/process-modeling/`), and **1 of 304** PDFs contains the
  string (the NewgenONE Marvin brochure — GenAI *writes* the model, design-time, so E2
  territory rather than an AI element inside a process).
- **The one open gap** (recorded in the ledger `note`): a diagram whose file name **and** alt
  text are both content-free, on a page that discusses only "workflow"/"process automation"
  rather than the process model itself. That broader set is 475 pages / 916 figures and could
  not be downloaded within the session; the strong-vocabulary set (34 pages / 87 figures) was
  fully downloaded and byte-measured.
- Nothing was excluded for being marketing material, small, simple, non-English, fictional,
  low quality, or similar to another item. No figure was excluded for being one the agent
  could not see.

## RESULT, DELTA 1 - visual passes closed (elicitation-3a, 2026-09-25)

`python tools/audit.py newgen` -> `problems: none`; `population 800, rows 800 (+74
superseded rows)`, `EXCLUDE 796, INCLUDE 3, UNCERTAIN 1`, `E0 786 / E1 10`,
`judgement exclusions 10 (1.2%)`, `review queue: visual-check=0 rulings=1`.

Both figure sets are now closed. The strong-vocabulary set (87 figures / 34 pages) was read
in the first pass; the broader set (**1117 figures / 508 pages**) was downloaded in full and
triage-viewed as 94 contact sheets with a per-tile sidecar. Every process-shaped or
unreadable tile was re-read at native size.

- **One new artefact** (the whole point of the backstop): row 513, page
  `/platform/process-automation/dynamic-case-management/`, was `E0-no-artefact` because its
  only process-named figure was a stock pictogram. The raw set holds a second asset on that
  page (`Dynamic-Case-Management-center-scaled-1.webp`, 2560x1057, alt text "arrow icon"),
  a real newgenONE Process Designer canvas in **"BPMN View"** on "Credit Card Issuance v6.0
  (Draft)": pool lane "Swimlane", stage bands Initiation / "AI assisted Data Processing" /
  Automation, start events Web/Mobile/Chatbot/Email, service task **"AI Rule Engine"** whose
  outgoing sequence flow is labelled **"AI Decisioning"**, gateways BOT_Decision / Exp_Dec /
  Checker_Dec / Maker_Dec, KYC Maker/Checker, Case Manager, call-out "Initiate Re-KYC".
  -> superseding row `INCLUDE`, new record
  `corpus/newgen/073_newgensoft-com-platform-process-automation-dynamic-case-management.md`
  (+ its capture).
- **One claimed hit rejected**: a worker reported a BPMN+AI canvas on row 517
  (`process-orchestration`). Reading that asset at native size shows the Process Management
  configuration table, exactly as the earlier pass had recorded. No row written; the episode
  is in the ledger's `self_audit_flips` as the lesson that contact-sheet triage screens
  candidates and never decides.
- Row 515 (`process-insights`) keeps its `UNCERTAIN` + `needs_human_ruling`; the backstop
  re-read the same asset at 1000x439 and sharpened the question (see the record): "Graphical
  View" icon-node map, clipped at its right edge in the asset itself, notation still
  unsettled.
- The 72 earlier `UNCERTAIN` rows resolved to exclusions with named evidence; every one is
  in the ledger, and the near-misses the researcher may want to eyeball (ML-pipeline node
  graphs rows 436/443, Content Intelligence data-flow row 446, InsureMO layered architecture
  row 484, Section 1071 decision-tree infographic row 688, the "Payer Operations BPaaS
  Automation with AI/ML/RPA" capability map rows 111/020) are listed in the header note.
- **Known limit, recorded in the ledger**: the sheet builder cannot rasterise SVG, so the 261
  SVG assets of the broader set were invisible as images. They were closed at file level -
  every one is a single-glyph icon, wordmark or embedded-raster collage, none carries a
  `<text>` node, and a token scan for bpmn/sequenceFlow/serviceTask found only base64
  payloads. No figure was excluded for being unreadable.

