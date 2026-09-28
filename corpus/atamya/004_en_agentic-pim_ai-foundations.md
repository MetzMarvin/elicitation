---
n: 243
source: atamya
source_name: Atamya (www.atamya.com - Agentic PIM with an embedded bpmn.io / Flowable BPMN engine)
source_type: vendor product page
title: ATAMYA AI Foundations
url: https://www.atamya.com/en/agentic-pim/ai-foundations/
accessed: 2026-09-24
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "page claim plus six figures, one of which is a BPMN model on a white canvas whose first branch holds a robot-face task and whose later branches hold gear-marked tasks"
bpmn_evidence_quote: "Every AI call in ATAMYA is a native BPMN service task."
ai_evidence: "page text claiming AI is a BPMN element: 'Every AI call in ATAMYA is a native BPMN service task.'"
ai_evidence_quote: "Every AI call in ATAMYA is a native BPMN service task."
artefacts:
  screenshot: 004_1_website-agentic-pim-ai-strategie-diagramm-workflow.png
  assets: [004_2_website-agentic-pim-ai-strategie-knowledge-layer-diagram-en.png]
  archive: 004_en_agentic-pim_ai-foundations.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: poor
capture_width_px: 1281
capture_method: curl of the vendor's own wp-content/uploads asset at its native URL
---
## What the page shows

Six figures: a knowledge-layer diagram, `...ai-strategie-diagramm-workflow.png` (a white
canvas on a dark page holding a BPMN model: start event, exclusive gateway, a branch to a
robot-face task and a branch to a yellow task, second exclusive gateway, a yellow task, a
document task, a parallel gateway splitting to two gear-marked tasks, second parallel
gateway, a person task (orange) and a lock-marked task, then the end event), an
LLM-model-choice diagram, a governance graphic, a knowledge-layer/memory diagram and an
AI-agents diagram.

## Observations (description only, no interpretation)

- **AI activity - function:** the page's opening claim is the placement claim quoted above;
  the workflow figure's first branch carries the robot-face glyph, the rest of the model
  carries service-task (gear) and user-task (person) glyphs.
- **AI activity - element type:** "native BPMN service task" (page text). The figure itself
  is icon-only, so the element type is asserted by the copy, not drawn in the diagram.
- **Authority - downstream / data / control:** not stated on the page; the model's own
  control flow (X and + gateways) is visible but unlabelled.
- **Input provenance:** not visible in the workflow figure.
- **Guards present:** the page's governance figure is about guardrails, but no guard is
  visible inside the process.
- **Prompt / model detail visible:** the LLM-model-choice figure names model choice as a
  design decision; no prompt is shown.

## Notes for the researcher

- The record exists because of the page text, not because of the drawing: the drawing is a
  labelled-less BPMN model. The German twin page (`de/agentic-pim/ai-fundament/`) states the
  same claim in German and shares four of these figures as *identical files*, so it gets its
  own record (007) rather than an E3 row - the two knowledge-layer diagrams differ.
- Capture: vendor assets, 1281 x 875 (shared workflow file) - under the 1400 px bar,
  `capture_quality: poor` by rule.
