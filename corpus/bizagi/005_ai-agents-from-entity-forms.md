---
n: 3
source: bizagi
source_name: Bizagi (vendor documentation, help.bizagi.com)
source_type: vendor docs
title: Execute AI Agents from Entity Forms
url: https://help.bizagi.com/platform/en/ai-agents-from-entity-forms.htm
accessed: 2026-09-24
verdict: UNCERTAIN
needs_human_ruling: true
question: "The AI Agent runs when an entity form is shown at a process node: is an AI element placed in the form layer (not on the flow) in scope?"
needs_visual_check: false
bpmn_evidence: vendor figure: BPMN pool with Search lane, start event, parallel gateway, activity, second gateway
bpmn_evidence_quote: "Sharing variable: Document"
ai_evidence: page text + the vendor figure
ai_evidence_quote: "This capability enhances the flexibility of AI integration by allowing you to trigger AI Agents from a wide variety of form types used across your application."
artefacts:
  screenshot: 005_aientityforms20.png
  archive: 005_ai-agents-from-entity-forms.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1916
capture_method: curl of the vendor's own .png asset at its native URL (help.bizagi.com documentation image)
---

## What the page shows

The page shows an Entity-Form-based process model: a pool with a `Search` lane, a start
event, a parallel gateway, a sub-process/activity and a second gateway, with the Bizagi
`Define Forms` wizard open over the canvas and a `Sharing variable: Document` property.
The page text describes triggering AI Agents from entity forms.

## Observations (description only, no interpretation)

- **AI activity - function:** "This capability enhances the flexibility of AI integration
  by allowing you to trigger AI Agents from a wide variety of form types used across your
  application." The page lists use cases ("Examples of AI Agents in Entity Forms").
- **AI activity - element type:** not a BPMN element - the agent is triggered from an
  Entity form attached to a process node (the wizard shown is the form definition).
- **Authority - downstream:** not visible on the page.
- **Authority - data:** the wizard shows a shared variable (`Document`); the agent's
  output mapping is not visible in the figure.
- **Authority - control:** the model contains two gateways, but the page does not tie the
  agent's result to either.
- **Input provenance:** entity form fields and the shared variable; not described further.
- **Guards present:** none observed on the page.
- **Prompt / model detail visible:** not visible on this page.

## Notes for the researcher

- `needs_human_ruling` is set: placement in the form layer rather than on the flow.
- Capture is the vendor's native asset, 1916 px wide (`capture_quality: legible`).
