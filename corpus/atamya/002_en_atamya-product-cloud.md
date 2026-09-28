---
n: 227
source: atamya
source_name: Atamya (www.atamya.com - Agentic PIM with an embedded bpmn.io / Flowable BPMN engine)
source_type: vendor product page
title: ATAMYA Product Cloud (product overview)
url: https://www.atamya.com/en/atamya-product-cloud/
accessed: 2026-09-24
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "screenshot of the ATAMYA Product Cloud BPMN modeller: a real bpmn.io canvas with a palette, a properties panel and a model whose tasks are labelled, including a task labelled 'KI-Uebersetzung' (AI translation)"
bpmn_evidence_quote: "Workflow management pursuant to BPMN version 2.0"
ai_evidence: "the task labelled 'KI-Uebersetzung' (AI translation) in the workflow figure"
ai_evidence_quote: "Workflow management pursuant to BPMN version 2.0"
artefacts:
  screenshot: 002_website-atamya-product-cloud-image-workflow-management.png
  assets: []
  archive: 002_en_atamya-product-cloud.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: poor
capture_width_px: 640
capture_method: curl of the vendor's own wp-content/uploads asset at its native URL
---
## What the page shows

The English product-cloud overview shows four product screenshots; the fourth,
`website-atamya-product-cloud-image-workflow-management.png`, is a screenshot of the
vendor's own BPMN editor (the bpmn.io canvas furniture is visible: element palette on the
left, canvas in the middle, properties panel on the right, in-product navigation "Startseite
| Benutzerverwaltung | Workflow-Definitionen | Uebersetzung"). The model on the canvas runs
start event -> exclusive gateway -> source-language task -> review task -> exclusive gateway
-> **KI-Uebersetzung** -> review -> text -> exclusive gateway -> end event. German labels are
kept in the English figure, so the AI task is labelled in German. The same file is served on
the German page of the same section (recorded there as an E3 duplicate).

## Observations (description only, no interpretation)

- **AI activity - function:** the task labelled `KI-Uebersetzung` (AI translation) sits in
  the middle of the model, between two review steps; the page copy around it only claims
  "Workflow management pursuant to BPMN version 2.0".
- **AI activity - element type:** a BPMN task on the canvas - not a BPMN standard type; the
  label names the work, not the element type. The page does not say which engine element it
  is (the ai-powered-workflows page of the same site calls these "native service tasks").
- **Authority - downstream:** not visible on this page; the task output flows into a task
  labelled "Pruefung" (review).
- **Authority - data:** not visible.
- **Authority - control:** two exclusive gateways are visible in the model, but their
  conditions are not legible in the figure.
- **Input provenance:** the model's first task is labelled with the source language
  (`Quell-Sprache`), i.e. the AI task consumes the source text.
- **Guards present:** not visible; the following task is a human review step.
- **Prompt / model detail visible:** not visible on this page. Elsewhere the site states the
  translation task can be bound to DeepL ("Dedizierter Uebersetzungs-Task, optional mit
  DeepL").

## Notes for the researcher

- Strongest atamya candidate after record 009: an AI element is *named inside the process*
  and the process is a live bpmn.io model, not a marketing redraw.
- Capture: the vendor's asset at its native 640 x 437 - well under the 1400 px bar, so
  `capture_quality: poor` by rule; the task labels were legible at native size in the review.
