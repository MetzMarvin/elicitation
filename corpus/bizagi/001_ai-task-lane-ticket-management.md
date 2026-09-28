---
n: 15
source: bizagi
source_name: Bizagi (vendor documentation, help.bizagi.com)
source_type: vendor docs
title: Execute AI Agents from Activity Actions
url: https://help.bizagi.com/platform/en/ai_agents_activity_actions.htm
accessed: 2026-09-24
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: vendor figure of a BPMN pool with three swimlanes (Support Agent / AI / Support Analyst) and milestone columns; AI Task nodes drawn in the AI lane
bpmn_evidence_quote: "Click the AI Task within your process where you want to configure the AI Agent."
ai_evidence: page text + the vendor figure
ai_evidence_quote: "Click the AI Task within your process where you want to configure the AI Agent."
artefacts:
  screenshot: 001_aiagents13.png
  archive: 001_ai_agents_activity_actions.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: poor
capture_width_px: 1390
capture_method: curl of the vendor's own .png asset at its native URL (help.bizagi.com documentation image)
---

## What the page shows

A Bizagi Studio process model for ticket handling: one pool (`Ticket Management`) with
three lanes - `Support Agent`, `AI`, `Support Analyst` - split by three milestone columns
(`Creation and classification`, `Analysis and solution`, `Closure`). The `AI` lane is a
lane of its own and holds four tasks drawn with an AI icon: `Classify ticket`,
`Prioritize ticket`, `Preliminary analysis`, `Update KB`. `Create ticket` sits in
`Support Agent`; `Ticket analysis` and `Ticket resolution` sit in `Support Analyst`. The
page text is a procedure: "Click the AI Task within your process where you want to
configure the AI Agent."

## Observations (description only, no interpretation)

- **AI activity - function:** the four AI-lane tasks; the page itself describes only the
  placement procedure, not what each task does ("Click the AI Task within your process
  where you want to configure the AI Agent.").
- **AI activity - element type:** `AI Task` - a Bizagi task type, not a BPMN standard
  element. The task-type reference page of the same documentation set defines it: "An AI
  Task is performed by an AI Agent." The agent is attached to it as an `Activity Action`
  (Business Rules > Activity actions), configured for On Enter / On Exit.
- **Authority - downstream:** not visible on the page.
- **Authority - data:** the `Update KB` task label only; no data objects shown.
- **Authority - control:** not visible on the page; no gateways are drawn in this figure.
- **Input provenance:** not visible on the page.
- **Guards present:** the page states a limit, not a guard: "Keep in mind that an AI Task
  allows only one AI Agent Activity Action."
- **Prompt / model detail visible:** not visible on this page. The AI Agents overview page
  of the same documentation set says the agents are "configured similarly to Generative
  Pre-trained Transformers (GPT), leverage Azure Open AI".

## Notes for the researcher

- Capture is the vendor's native asset, 1390 px wide - 10 px under the 1400 px bar, so
  `capture_quality: poor` by rule. All lane and task labels are legible at this size.
- The AI lane is a *swimlane*: the vendor models the AI as an organisational participant
  rather than as a task decoration. Worth a look when the taxonomy is fixed.
