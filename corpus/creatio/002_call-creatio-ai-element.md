---
n: 151
source: creatio
source_name: Creatio Academy (academy.creatio.com), version 10 - process elements reference / system actions
source_type: vendor product documentation
title: Call Creatio.ai process element
url: https://academy.creatio.com/guides/no-code-customization/bpm-tools/process-elements-reference/system-actions/call-creatio-ai-element
accessed: 2026-09-24
verdict: UNCERTAIN
needs_human_ruling: true
question: "This is the source's own anchor page for the in-process AI element: it documents the 'Call Creatio.ai' business process element that integrates Sub-agents into a process, including its skill parameters and its result handling. But the two figures it publishes are the element's setup area (Fig. 1) and a parameter-collection illustration (Fig. 2) - the page publishes NO BPMN diagram in which the element appears, and the section's neighbouring element pages do publish process fragments. Does the source contribute an artefact here (prose-and-panel-documented AI element inside a process, capture = the element panels), or does the absence of a published process model make this E1 (the artefacts are UI panels, not BPMN) or E0? I recorded UNCERTAIN rather than excluding because the AI element is inside the process rather than adjacent to it, and a wrong exclusion here is unrecoverable (shared rules 1 and 2)."
bpmn_evidence: "NONE - and this is the finding. Neither of the page's two figures is a process diagram: Fig. 1 is the element's setup area in the process designer ('Fig. 1 Setup area of the Call Creatio.ai element') and Fig. 2 illustrates working with a collection of records in the element's parameters ('Fig. 2 Work with a collection of records'). The archived page text names the element's own properties (Which skill to call, How to process the result, Result handling) but never draws the process the element is placed in. Compare the sibling page 'Implement prediction models', which does publish the process model (corpus record 001)."
bpmn_evidence_quote: "Fig. 1 Setup area of the Call Creatio.ai element"
ai_evidence: "The element itself is the AI element: 'Use the Call Creatio.ai business process element to integrate Creatio Sub-agents into any business process.' It is configured by choosing the Sub-agent to call ('Select a skill to call in the element setup area') and by deciding how the Sub-agent's result is processed - the page documents the collection/result modes and their limitations."
ai_evidence_quote: "integrate Creatio Sub-agents into any business process"
artefacts:
  screenshot: 002_call-creatio-ai-element_fig1.png
  screenshot_2: 002_call-creatio-ai-element_fig2.png
  archive: null
  bpmn_xml: null
capture_source: figure-as-published
capture_quality: legible
capture_width_px: 1264
capture_method: "the page's own two figures, downloaded from the Academy CDN and kept unmodified; the wider of the two (Fig. 2, 1264x448) is the one the capture width refers to"
duplicate_of: null
access: public
---

## What the page shows

The element-reference page for **Call Creatio.ai**, the process element that puts a Creatio.ai Sub-agent
inside a business process:

> "Use the Call Creatio.ai business process element to integrate Creatio Sub-agents into any business
> process. Before you configure this element, make sure you have a corresponding Sub-agent set up."

The page is a configuration reference. It lists the element's parameters (which skill to call, how the
result is processed), notes that "Select a skill to call in the element setup area" is the first step, and
then documents the result-handling modes and their limits, e.g. that a parameter "can only be used when the
Sub-agent ..." (Fig. 2 is the illustration for that section).

Neither figure is a process model. Fig. 1 is the element's setup area - the panel in which the skill is
chosen - and Fig. 2 is a parameter/collection illustration.

## Observations (description only, no interpretation)

- **AI activity - function:** the process delegates a step to a Sub-agent (a configured Creatio.ai agent)
  and consumes its result.
- **AI activity - element type:** a *system action* element of the process designer, i.e. a task in the
  process model in every respect except that this page does not draw the model.
- **AI activity - model binding:** the binding is to a Sub-agent configured elsewhere ("Learn more: Develop
  Creatio Sub-agent"); the element itself selects the skill and the result mode.
- **Authority - downstream:** the page's whole subject is result handling - how the Sub-agent's output is
  written back into the process's data.
- **Authority - control:** the process controls invocation (it is a task, scheduled by the process), but the
  page does not describe any check on the Sub-agent's answer before it is consumed.
- **Guards present:** none described on this page - no confidence threshold, no human confirmation.
- **Input provenance:** the vendor's own agent platform; the Sub-agent is configured by the customer.
- **Availability:** the page carries no availability gate of its own.

## Notes for the researcher

The boundary question is the same one raised by the OCI Process Automation "Intelligent Document
Processing" page (source oracle-oic, record 032): **an AI element that the product places inside a process,
documented in prose and panels, without a published process model.** Here the situation is sharper, because
this page *is* the anchor page named in this source's assignment and because the sibling pages of the same
reference section do publish process fragments - so the absence of a diagram on this page is a property of
the page, not of the section.

If the method counts prose-and-panel documentation of an in-process AI element, this page is corpus
material and the capture is the two panels. If the method requires a published process model, the page is
E1 (UI panels, not BPMN notation) and the nearest corpus item for this element is record 001, where the ML
element is drawn as a task.
