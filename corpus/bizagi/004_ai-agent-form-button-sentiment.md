---
n: 25
source: bizagi
source_name: Bizagi (vendor documentation, help.bizagi.com)
source_type: vendor docs
title: Analyze file sentiment
url: https://help.bizagi.com/platform/en/ai_agents_form_actions_sentiment_analysis.htm
accessed: 2026-09-24
verdict: UNCERTAIN
needs_human_ruling: true
question: "The AI Agent is bound to a form button in the process form, not to a BPMN element: is that placement in scope, or only task-bound AI?"
needs_visual_check: false
bpmn_evidence: vendor figure: single-lane process, start event - user task Review Documents - end event
bpmn_evidence_quote: "Review Documents"
ai_evidence: page text + the vendor figure
ai_evidence_quote: "In this process, buttons are implemented as the executors of AI Agent actions."
artefacts:
  screenshot: 004_ai_agents_from_forms09.png
  archive: 004_ai_agents_form_actions_sentiment_analysis.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: poor
capture_width_px: 766
capture_method: curl of the vendor's own .png asset at its native URL (help.bizagi.com documentation image)
---

## What the page shows

A worked example of an AI Agent bound to a form button, on a one-task process. The
`Process Model` section shows pool `Execute AI Agents`, one lane, start event -> user
task `Review Documents` -> end event - the identical figure used by the other three
worked examples of the branch. The remaining figures are the form, the Agent button and
the runtime result.

## Observations (description only, no interpretation)

- **AI activity - function:** the example agent "analyzes the sentiment from a text
  file" ("This article explains the step-by-step of how to configure the AI Agent in the
  form actions through the example of the Agent that analyzes the sentiment from a text
  file.").
- **AI activity - element type:** form-action binding - "In this process, buttons are
  implemented as the executors of AI Agent actions." The task `Review Documents` is an
  ordinary user task; the AI is executed from the form UI.
- **Authority - downstream:** not visible on the page.
- **Authority - data:** the response is stored in the case data; the page states the
  answer "should be modeled as extended String attributes to view a complete response".
- **Authority - control:** not visible on the page.
- **Input provenance:** a text file uploaded to the form before the Agent button is
  clicked ("Once the files have been loaded and the Agent buttons are clicked, the
  execution of the file analysis is triggered.").
- **Guards present:** none observed.
- **Prompt / model detail visible:** not on this page; the agent editor pages of the same
  branch show Model, Prompt, Prompt variables, Input/Output.

## Notes for the researcher

- Same figure as record 003 (`ai_agents_from_forms35.png` is *not* used here; this page
  uses `ai_agents_from_forms09.png`). Both figures are single-task example processes.
- `needs_human_ruling` is set: this is the boundary case named in the assignment brief
  (AI on the UI layer of a user task).
