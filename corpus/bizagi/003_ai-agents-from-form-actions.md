---
n: 22
source: bizagi
source_name: Bizagi (vendor documentation, help.bizagi.com)
source_type: vendor docs
title: Execute AI Agents from Form Actions
url: https://help.bizagi.com/platform/en/ai_agents_form_actions.htm
accessed: 2026-09-24
verdict: UNCERTAIN
needs_human_ruling: true
question: "The AI Agent is executed from a form button, not from a BPMN task: is AI attached to the UI layer of a user task an in-process AI element for this study?"
needs_visual_check: true
bpmn_evidence: vendor figure: single-lane process, start event - user task Review Documents - end event
bpmn_evidence_quote: "Review Documents"
ai_evidence: page text + the vendor figure
ai_evidence_quote: "This feature integrates the use of Artificial Intelligence with the execution of Form Actions so that you can customize the actions needed in your business process."
artefacts:
  screenshot: 003_ai_agents_from_forms35.png
  archive: 003_ai_agents_form_actions.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: poor
capture_width_px: 1314
capture_method: curl of the vendor's own .png asset at its native URL (help.bizagi.com documentation image)
---

## What the page shows

The method page for "Execute AI Agents from Form Actions". A `Process Model` section
shows the example process used throughout the feature: a single pool, one lane, one user
task `Review Documents` between a start and an end event. The rest of the page is the
configuration procedure (form actions, buttons, variables).

## Observations (description only, no interpretation)

- **AI activity - function:** "This feature integrates the use of Artificial Intelligence
  with the execution of Form Actions so that you can customize the actions needed in your
  business process."
- **AI activity - element type:** not a BPMN element. The agent is executed by a **form
  button**: "buttons are implemented as the executors of AI Agent actions" (quoted on the
  worked-example pages of this branch).
- **Authority - downstream:** not visible on the page.
- **Authority - data:** the page describes writing the agent response into the case form
  variables; the figure shows no data objects.
- **Authority - control:** not visible on the page.
- **Input provenance:** files loaded into the form before the Agent button is clicked
  (per the worked-example pages).
- **Guards present:** none observed. The pages describe the button click as the trigger.
- **Prompt / model detail visible:** not visible on this page.

## Notes for the researcher

- The process model is a deliberate minimal example: one task, `Review Documents`. The
  AI sits in the form layer of that task, not on the flow.
- `needs_human_ruling` is set: the four worked-example pages of this branch
  (`..._compare`, `..._describe_image`, `..._sentiment_analysis`, `..._translate`) reuse
  the *same* figure (`ai_agents_from_forms09.png`) and are recorded as E3 duplicates of
  record 004; the branch's distinct content is the four different agents.
