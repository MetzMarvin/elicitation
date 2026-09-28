---
n: 296
source: atamya
source_name: Atamya (www.atamya.com - Agentic PIM with an embedded bpmn.io / Flowable BPMN engine)
source_type: vendor product page
title: User and Workflow Management (product page)
url: https://www.atamya.com/en/atamya-product-cloud/user-and-workflow-management/
accessed: 2026-09-24
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "screenshot of a real bpmn.io editor canvas in the product: start event, exclusive gateways, tasks labelled in German, among them a task labelled 'KI-Uebersetzung' (AI translation)"
bpmn_evidence_quote: "BPMN can map almost any scenario - from automated translations to manual data updated and sending automatic email notifications."
ai_evidence: "the task labelled 'KI-Uebersetzung' in the editor screenshot; the page text names BPMN 2.0 as the notation"
ai_evidence_quote: "Workflow management pursuant to BPMN version 2.0"
artefacts:
  screenshot: 009_1_produkt-screenshot-workflow-management-intern.png
  assets: [009_2_produkt-graphic-workflow-management-extern-en.png]
  archive: 009_en_atamya-product-cloud_user-and-workflow-management.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: poor
capture_width_px: 640
capture_method: curl of the vendor's own wp-content/uploads asset at its native URL
---
## What the page shows

Four figures: a hero photo, a user-management screenshot, `produkt-screenshot-workflow-
management-intern.png` (a screenshot of the in-product BPMN editor - bpmn.io palette on the
left, canvas, properties panel; the in-product tab bar reads "Benutzerverwaltung -
Workflow-Definitionen - Uebersetzung") and `produkt-graphic-workflow-management-extern-en.png`
(an import/PIM/export diagram: ERP, PLM, DAM and "and many more..." flowing into PIM and out
to Shop, App, Print Tool and "and many more..."). The editor model runs start event ->
exclusive gateway -> source-language task -> text-pruefen task -> exclusive gateway ->
**KI-Uebersetzung** -> Pruefung -> Text -> exclusive gateway -> end event.

## Observations (description only, no interpretation)

- **AI activity - function:** AI translation of product text, sitting between a source-text
  step and a human review step.
- **AI activity - element type:** a task on a BPMN canvas; the page's own copy calls the
  notation "BPMN version 2.0" and says "BPMN can map almost any scenario - from automated
  translations to manual data updated...". The element type is named as a service task only
  on the site's AI pages.
- **Authority - downstream:** the AI task's output goes to a review task ("Pruefung").
- **Authority - data:** not visible in the figure.
- **Authority - control:** two exclusive gateways are drawn; conditions not legible.
- **Input provenance:** the first task is labelled with the source language, so the AI task
  consumes source text produced upstream in the same model.
- **Guards present:** the following review task is the human check; no formal guard drawn.
- **Prompt / model detail visible:** not on this page; the site's AI pages name DeepL as an
  optional translation binding.

## Notes for the researcher

- The same screenshot file is served on the German page of this section
  (`de/atamya-product-cloud/user-und-workflow-management/`), which is recorded as an E3 row.
- The import/export graphic on the same page is *not* BPMN (no events, no gateways, no
  sequence flows) - it is a system-landscape diagram and is what the page would have been
  excluded for if the editor screenshot were absent.
- Capture: vendor asset at its native 640 x 438 - well under the 1400 px bar, so
  `capture_quality: poor` by rule; the labels were legible, 'KI-Uebersetzung' included.
