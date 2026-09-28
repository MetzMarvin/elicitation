---
n: 278
source: atamya
source_name: Atamya (www.atamya.com - Agentic PIM with an embedded bpmn.io / Flowable BPMN engine)
source_type: vendor product page
title: AI-Fundament (German AI Foundations page)
url: https://www.atamya.com/de/agentic-pim/ai-fundament/
accessed: 2026-09-24
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "page claim plus six figures, one of which is a BPMN model (start event, X and + gateway diamonds, robot-face task, gear-marked service tasks, person-marked user task) on a white canvas"
bpmn_evidence_quote: "Jeder AI-Aufruf in ATAMYA ist ein nativer BPMN Service Task."
ai_evidence: "page text claiming AI is a BPMN element: 'Jeder AI-Aufruf in ATAMYA ist ein nativer BPMN Service Task.'"
ai_evidence_quote: "Jeder AI-Aufruf in ATAMYA ist ein nativer BPMN Service Task."
artefacts:
  screenshot: 007_1_website-agentic-pim-ai-strategie-diagramm-pim-knowledge-layer-de.png
  assets: [007_2_website-agentic-pim-ai-strategie-diagramm-workflow.png]
  archive: 007_de_agentic-pim_ai-fundament.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: poor
capture_width_px: 1280
capture_method: curl of the vendor's own wp-content/uploads asset at its native URL
---
## What the page shows

The German AI Foundations page: the same claim set as the English page ("AI im Prozess,
nicht daneben"), with a German knowledge-layer diagram of its own plus four figures that are
byte-identical to the English page's files, among them the BPMN workflow model described in
record 004.

## Observations (description only, no interpretation)

- **AI activity - function:** the page lists AI steps that run inside the process
  ("AI-Ergebnisse fliessen direkt in Entscheidungen ein", several AI steps in parallel or
  iteratively).
- **AI activity - element type:** "nativer BPMN Service Task" (page text).
- **Authority - downstream:** "die KI darf nur, was User oder Workflow erlauben" - the
  workflow is the authority that permits AI actions.
- **Authority - data / control:** not visible inside the figure; the model's gateways are
  unlabelled.
- **Input provenance:** not visible in the workflow figure.
- **Guards present:** the page names guardrails as a governance topic, not as process guards.
- **Prompt / model detail visible:** not on this page.

## Notes for the researcher

- The German page carries four files that are shared (identical) with the English page and
  two German-only diagrams; because the figure sets differ, this page is a record of its own
  and not an E3 row. If the corpus counts artefacts per diagram rather than per page, the
  workflow model here is the same diagram as record 004's - the ledger says so in the note.
- Capture: vendor assets, native 1280 x 874 (this page's own knowledge-layer diagram) and
  1281 x 875 (the workflow model shared with the English page) - both under the 1400 px bar,
  `capture_quality: poor` by rule.
