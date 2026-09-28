---
n: 31
source: bizagi
source_name: Bizagi (vendor documentation, help.bizagi.com)
source_type: vendor docs
title: AI Workers
url: https://help.bizagi.com/platform/en/ai_workers.htm
accessed: 2026-09-24
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: vendor figure of a BPMN pool/lane model with tasks Upload expenses, Submit expenses, Review purchase, Approve manager, Notify account payable and a Yes/No gateway
bpmn_evidence_quote: "Upload expenses, Submit expenses, Review purchase, Approve manager, Notify account payable"
ai_evidence: page text + the vendor figure
ai_evidence_quote: "Unlike traditional AI agents, AI Workers do not require programming, predefined specifications, or prompts."
artefacts:
  screenshot: 002_aiworkers15.png
  archive: 002_ai_workers.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1499
capture_method: curl of the vendor's own .png asset at its native URL (help.bizagi.com documentation image)
---

## What the page shows

The page ("AI Workers") carries a Bizagi Studio model of an expenses process: pool with
lanes for the employee and the approving side, tasks `Upload expenses`, `Submit expenses`,
`Review purchase`, `Approve manager` and `Notify account payable`, joined by a gateway
with `Yes` / `No` branches, split by the milestone columns `Attach`, `Approval`, `Notify`.
The second figure is the same model inside the Studio canvas with the `Submit expenses`
task selected, its `Element properties` panel open and the right-click menu open on
`Task type`.

## Observations (description only, no interpretation)

- **AI activity - function:** "AI Workers automatically populate editable fields in a
  form by analyzing field descriptions, applying business rules, and leveraging data
  already entered in previous editable fields." "Unlike traditional AI agents, AI Workers
  do not require programming, predefined specifications, or prompts."
- **AI activity - element type:** a task-level implementation binding: the AI Worker is
  chosen as the task's **Task type** in the modeler. It is not a BPMN element type of its
  own and no AI-specific node appears in the diagram.
- **Authority - downstream:** not visible on the page.
- **Authority - data:** the page says it writes form fields ("automatically populate
  editable fields in a form"); named fields are not visible in the figure.
- **Authority - control:** the approval gateway (`Review purchase` / `Approve manager`)
  is a human step in the same model; the page does not tie the worker's output to it.
- **Input provenance:** "field descriptions ... data already entered in previous editable
  fields" - i.e. the form itself; no document or message input is described.
- **Guards present:** the page documents a supervision setting elsewhere in the same
  section ("Supervised" / "Autonomous" / "Autonomy rule" appear on the AI Worker
  configuration figures of the same page); no guard is shown in the diagram.
- **Prompt / model detail visible:** the page states Workers "do not require ...
  prompts"; no model name on this page.

## Notes for the researcher

- The AI element here is invisible in the diagram; it is a *task property*. The second
  figure (`002_ai-worker-task-type-expenses_task-type-menu.png`) is the evidence that the
  binding is made in the modeler. Marked `capture_quality: legible` (1499 px).
