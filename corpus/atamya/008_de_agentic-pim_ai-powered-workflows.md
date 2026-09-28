---
n: 279
source: atamya
source_name: Atamya (www.atamya.com - Agentic PIM with an embedded bpmn.io / Flowable BPMN engine)
source_type: vendor product page
title: AI Powered Workflows (German page)
url: https://www.atamya.com/de/agentic-pim/ai-powered-workflows/
accessed: 2026-09-24
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "page claim plus five German figures, among them the AI-tasks chain and the workflow hero render"
bpmn_evidence_quote: "Er ist ein BPMN Service Task - genau wie 'Objekt aktivieren', 'Merkmalswert bearbeiten' oder 'mit Shopware synchronisieren'."
ai_evidence: "page text binding AI to a BPMN element: 'Bei ATAMYA arbeitet sie direkt im Prozess - als nativer Service Task, orchestriert von einer vollwertigen BPMN-Engine.'"
ai_evidence_quote: "Bei ATAMYA arbeitet sie direkt im Prozess - als nativer Service Task, orchestriert von einer vollwertigen BPMN-Engine."
artefacts:
  screenshot: 008_1_website-agentic-pim-diagramm-workflow-AI-tasks-de.png
  assets: [008_2_website-agentic-pim-diagramm-workflow-hero-de.png]
  archive: 008_de_agentic-pim_ai-powered-workflows.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: poor
capture_width_px: 1281
capture_method: curl of the vendor's own wp-content/uploads asset at its native URL
---
## What the page shows

The German twin of record 003 with its own German figures: the AI-tasks chain
(`website-agentic-pim-diagramm-workflow-AI-tasks-de.png`), the workflow hero render, the
AI-based-decisions figure, the expression-language figure and the human-in-the-loop figure.

## Observations (description only, no interpretation)

- **AI activity - function:** the same five AI task functions as the English page
  (generation, extraction, enrichment, translation, decisions).
- **AI activity - element type:** stated in the text, twice: "als nativer Service Task,
  orchestriert von einer vollwertigen BPMN-Engine" and "Er ist ein BPMN Service Task - genau
  wie "Objekt aktivieren", "Merkmalswert bearbeiten" oder "mit Shopware synchronisieren"."
- **Authority - downstream:** "Sobald ein neues Produkt angelegt wird, erstellt ein erster
  AI-Task die Produktbeschreibung."
- **Authority - data:** not visible in the figures; the English twin's expression-language
  figure shows the bound attributes.
- **Authority - control:** "Retries, Timeouts, Fallback-Pfade" are named in the text as
  automatic handling of a failing provider; no guard is drawn.
- **Input provenance:** an AI task is triggered by a data event (product creation).
- **Guards present:** human-in-the-loop is one of the five figures.
- **Prompt / model detail visible:** the translation task is bound to DeepL "optional".

## Notes for the researcher

- Kept as a record rather than folded into record 003 because the figures are German
  renders (different files) and the corpus is language-tagged; the diagram content is the
  same model family.
- Capture: vendor assets, 1281 x 875 (this page's own German AI-tasks chain) - under the
  1400 px bar, `capture_quality: poor`.
