---
n: 804
source: frends-docs
source_name: Frends documentation (docs.frends.com)
title: "OpenAI"
url: https://docs.frends.com/tasks/tasks/openai
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
needs_visual_check: false
bpmn_evidence: "BPMN 2.0: the figure asset is a bpmn-js export (the file begins \"<!-- created with bpmn-js / http://bpmn.io -->\" and carries 8 data-element-id attributes), so the notation is BPMN 2.0 by construction. The diagram is a linear flow of a start event, two tasks and an end event."
bpmn_evidence_quote: "Handle customer request"
ai_evidence: "The AI/LLM element is a task inside the process: \"Call ChatGPT with customer prompt\" calls OpenAI's ChatGPT to produce the customer response."
ai_evidence_quote: "By using the the HTTP trigger and CallChatGPT task we can create an integration"
artefacts:
  screenshot: 013_call-chatgpt-process.png
  assets: [013_call-chatgpt-process.png]
  bpmn_xml: []
  archive: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: "figure fetched from its native asset URL on the Frends documentation site and opened at full size on 2026-09-26"
judgment: true
---

## What the artefact is

`https://docs.frends.com/tasks/tasks/openai` (ledger row n=804), figure asset `/spaces/evBo49UTUjEN84O2WPl6/uploads/git-blob-d52bababe350ebc0aa0309358ab21f7baea300fc/chat-gpt.svg`.

## What the figure shows

BPMN diagram: a start event "Listen for requests on /help endpoint", a task "Call ChatGPT with customer prompt", a task "Create response for customer" and an end event, joined by sequence flows. (013_call-chatgpt-process.png)

## bpmn_evidence

BPMN 2.0: the figure asset is a bpmn-js export (the file begins "<!-- created with bpmn-js / http://bpmn.io -->" and carries 8 data-element-id attributes), so the notation is BPMN 2.0 by construction. The diagram is a linear flow of a start event, two tasks and an end event.

## ai_evidence

The AI/LLM element is a task inside the process: "Call ChatGPT with customer prompt" calls OpenAI's ChatGPT to produce the customer response.

## Notes for the researcher

- The capture was produced by rendering the vendor's own SVG in a browser and screenshotting it, because the asset is published as SVG and the corpus stores PNG captures; the SVG itself was downloaded unchanged.
- The smallest complete AI-in-BPMN example in the source: three nodes and two sequence flows.
- Found by scanning the text labels of all 123 bpmn-js task diagrams in the source: this is the only one whose labels name an AI service.
- Evidence read from the markdown twin https://docs.frends.com/tasks/tasks/openai.md.
