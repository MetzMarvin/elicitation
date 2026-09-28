---
n: 322
source: frends-docs
source_name: Frends documentation (docs.frends.com)
title: "AI Connector"
url: https://docs.frends.com/reference/shapes/activity-shapes/ai-connector
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
needs_visual_check: false
bpmn_evidence: "BPMN 2.0 process diagram on the Frends Process Editor canvas: the AI Connector is a task shape inside the Process and its result is returned through a Return shape."
bpmn_evidence_quote: "For embedding AI operator into your Processes, a shape called Intelligent AI Connector can be used."
ai_evidence: "The AI Connector is the AI/LLM element inside the process; on this page it can also consume MCP Tools, which makes the AI step agentic inside an otherwise deterministic BPMN flow."
ai_evidence_quote: "creating a reasoning loop when Tools are used and making the AI agentic"
artefacts:
  screenshot: 011_native-ai-task.png
  assets: [011_native-ai-task.png, 011_result-reference.png]
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

`https://docs.frends.com/reference/shapes/activity-shapes/ai-connector` (ledger row n=322), figure asset `/spaces/1H5SQ92uIfBOYNIeoUAc/uploads/5fPjerUnP0sMIzN27y0H/screenshot-rocks - 2026-06-04T093652.477.png`.

## What the figure shows

Process Editor canvas with the Native AI shape ("Perform AI verification") in a Process, with the AI Connector configuration panel open. (011_native-ai-task.png); Process Editor canvas: the result reference value returning the AI task's result as the Process response. (011_result-reference.png)

## bpmn_evidence

BPMN 2.0 process diagram on the Frends Process Editor canvas: the AI Connector is a task shape inside the Process and its result is returned through a Return shape.

## ai_evidence

The AI Connector is the AI/LLM element inside the process; on this page it can also consume MCP Tools, which makes the AI step agentic inside an otherwise deterministic BPMN flow.

## Notes for the researcher

- The same figure as row n=321, but this is the shape's own reference page, so it is recorded separately.
- States the Frends 6.3 change: MCP Tools inside the AI Connector.
- Evidence read from the markdown twin https://docs.frends.com/reference/shapes/activity-shapes/ai-connector.md.
