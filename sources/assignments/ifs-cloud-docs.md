---
source: ifs-cloud-docs
source_name: IFS Cloud (technical documentation, Business Process Automation)
source_type: vendor documentation
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: YES
  C2_native_bpmn20: YES
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES
access: public
population_type: enumerable
population_estimate: 45
effort: medium
needs_logged_in_browser: false
status: DONE (elicitation-74)
---

## Criteria evidence

- **C1 YES** — https://docs.ifs.com/techdocs/26r1/040_tailoring/500_business_process_automation/050_business_process_modeling/070_ifs_ai/
  (2026-09-22): "The IFS AI Task is a purpose-built enhancement introduced for IFS
  Workflows, enabling seamless integration of IFS Industrial AI use cases which support
  LLMs, pre-trained, and trainable models directly into Workflow designs." A named node
  type with its own documentation page, properties panel and "AI Invocation History".
- **C2 YES** — https://docs.ifs.com/techdocs/26r1/040_tailoring/500_business_process_automation/050_business_process_modeling/
  (2026-09-22): "This section is a collection of detailed guides teaching the reader the
  various intricacies of BPMN and our extensions to BPMN." A dedicated "Common BPMN
  Symbols" page sits under the same section.
- **C3 YES** — served anonymously; no login, no paywall. There is a JavaScript bot
  challenge (see gotchas) but it resolves itself.
- **C4 YES** — IFS is a large enterprise ERP/EAM vendor (aerospace & defence, energy,
  manufacturing, service management). Corroborating technical detail: IFS Workflows is
  built on Camunda — the IFS expression-language page links out to
  `https://docs.camunda.org/manual/7.19/user-guide/process-engine/expression-language/`.

## Entry points

- `https://docs.ifs.com/techdocs/26r1/040_tailoring/500_business_process_automation/` —
  the Business Process Automation section root. **This is the population root.**
- Its children, observed from the content-area links of the Business Process Modeling
  index page (real extracted hrefs, not guessed):
  - `.../050_business_process_modeling/` (index)
  - `.../050_business_process_modeling/010_ifs_process_enrichment/`
  - `.../050_business_process_modeling/020_ifs_projection/` (IFS API)
  - `.../050_business_process_modeling/030_ifs_rest_call/`
  - `.../050_business_process_modeling/040_ifs_failure_event/`
  - `.../050_business_process_modeling/050_common_bpmn_symbols/`
  - `.../050_business_process_modeling/060_expression_anguage/` (sic — the typo is in the
    real URL; do not "correct" it)
  - `.../050_business_process_modeling/070_ifs_ai/`
- Sibling sections visible in the left nav and required for the frontier: "Workflow
  Tooling", "Workflow Architecture", "Extending Workflow", "Workflow Administration",
  **"Workflow Examples"**, "Industry Specific Configurations".
- Release versions: the docs are versioned (`26r1`, and a "Release 26R1" switcher). Pick
  one release, record it in the ledger header, and stay in it.

## Enumeration instructions

1. **There is no sitemap.** `GET /techdocs/26r1/sitemap.xml` returns HTTP 200 but contains
   zero `<loc>` entries. Build the frontier from the left navigation tree of the Business
   Process Automation section instead, and say so in `enumeration_method`.
2. Enumerate the **whole** BPA section, not just `070_ifs_ai/`. "Workflow Examples" is the
   likeliest home of complete worked diagrams and must be expanded fully.
3. Record the release tag (`26r1`) in the ledger header. If a newer release exists at
   census time, note it; do not silently switch.

## Artefact mechanics

- Diagrams and UI captures are plain `.png` assets with generic filenames
  (`ifs_ai_task_property_panel.png`, `task_logo.png`, `properties_parameters.png`) and
  **no useful `alt` text** (`alt` is empty on the content images). So `alt` is not an
  evidence route here — use the prose, which names elements explicitly, plus the image
  asset itself.
- Capture the original `.png` URL at native resolution.
- The `070_ifs_ai/` page has an "Example Use Case" and a "Step-by-Step Guide" section —
  that is where the worked placement lives.
- No `bpmn-js` canvas and no downloadable `.bpmn` on the public docs.
  **CORRECTED by elicitation-74 (2026-09-24): this is false.** The BPA pages do link
  downloadable `.bpmn` resources under their `resources/` folders; five were found and
  fetched (`BpaSmartEditorAITaskExample.bpmn`, `enrichment_bpa.bpmn`, `update_company.bpmn`,
  `manage_etag_variable.bpmn`, `validate_age.bpmn`). The `070_ifs_ai/` page additionally
  prints the AI task's XML inline in the body. They are linked as plain `<a href>` items,
  not rendered in a `bpmn-js` canvas, which is why a visual scan of the page misses them.
  The strongest evidence route for this source is therefore the `.bpmn` XML, not the
  figures.

## Known gotchas

- **JavaScript bot challenge.** First load of any `docs.ifs.com` page serves
  "Verifying your browser … Solving challenge... (80000 attempts)". It clears on its own
  after roughly 8–12 seconds and then the real page renders in the same tab. Wait, do not
  retry, and do not record it as `BLOCKED` unless it fails to clear.
- Left-nav links in the shell include the entire IFS documentation set, not just the BPA
  section. Filter by path prefix when building the frontier, or you will enumerate
  thousands of unrelated ERP pages.
- The docs are versioned; the same page exists under several release numbers. Within one
  release that is not a duplicate problem, but do not mix releases.
- Note for the taxonomy work, not for the verdict: IFS is a Camunda-derived engine, so its
  diagrams may resemble Camunda's. That is not `E3-duplicate` — never dedupe across
  sources.

## Spot checks performed by Pass 1

Spot checks only, not verdicts:

- `.../070_ifs_ai/` — opened after the challenge cleared; IFS AI Task described, properties
  panel and "Example Use Case" sections present.
- `.../050_business_process_modeling/` — opened; carries the BPMN C2 quote and the full
  child-page list.

## RESUME

(complete — nothing to resume)

**Status 2026-09-24, agent elicitation-74: population exhausted, `tools/audit.py
ifs-cloud-docs` prints `problems: none`.**

- Ledger: `ledgers/ifs-cloud-docs.jsonl`, header `population_size: 49`, 49 census rows
  (+12 supersede rows), footer `status: COMPLETE`.
- Verdicts: `INCLUDE=1`, `UNCERTAIN=1`, `EXCLUDE=47`
  (`E0-no-artefact=15`, `E1-not-bpmn=6`, `E2-no-ai-element=26`), `BLOCKED=0`.
  Judgement-exclusion share 4.1% (convention stated in the footer `note`).
- Collected: n=24 `003_ifs-ai-task-smart-editor.md` (INCLUDE, `.bpmn` XML);
  n=16 `002_workflow-tooling-ai-task-signifier.md` (UNCERTAIN + one human ruling: a BPMN
  fragment whose service task carries the `[AI]` projection marker).
- The site's bot challenge never blocked: it clears by itself in ~8–12 s on first load of
  each page, as the assignment predicted. No `BLOCKED` rows were needed.
- Second gotcha found: the downloadable models are **zips** (`resources/*.zip`), and a plain
  `curl` of them returns `Access denied` (the challenge cookie is required). Fetch them
  in-page with `fetch()`; same for image assets if `get_network_request` is unavailable.
- Self-audit: 3 verdict changes (n=26 `E2`→`UNCERTAIN`→`E1`, n=10 `UNCERTAIN`→`E1`), and the
  judgement flags of the four UI-screenshot rows were corrected. All six `E1` figures were
  fetched and read. Raw evidence for excluded rows lives in `ledgers/ifs-cloud-docs.raw/`
  (`NNN` in `corpus/` is reserved for records).
- The bot-challenge note above stays valid for anyone re-censusing this source.
