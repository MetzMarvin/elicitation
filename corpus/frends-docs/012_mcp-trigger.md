---
n: 360
source: frends-docs
source_name: Frends documentation (docs.frends.com)
title: "MCP Trigger"
url: https://docs.frends.com/reference/triggers/mcp-trigger
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: true
question: "The MCP Trigger is an AI-facing interface shape at the start of the Process rather than an AI task inside the flow: does it count as an AI element inside the process for the corpus?"
needs_visual_check: false
bpmn_evidence: "BPMN 2.0 process diagram on the Frends Process Editor canvas: the MCP Trigger is drawn as the Process's start (trigger) shape, followed by gateway and task shapes and sequence flows."
bpmn_evidence_quote: "In order to expose a Frends Process as a callable tool for AI agents and Large Language Models (LLMs), MCP Trigger can be used."
ai_evidence: "The trigger shape turns the whole BPMN Process into a tool that an AI agent can call: the AI element is the interface the process is published through, rather than a task inside it."
ai_evidence_quote: "MCP Trigger in Frends Process Editor."
artefacts:
  screenshot: 012_mcp-trigger-process.png
  assets: [012_mcp-trigger-process.png]
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

`https://docs.frends.com/reference/triggers/mcp-trigger` (ledger row n=360), figure asset `/spaces/1H5SQ92uIfBOYNIeoUAc/uploads/6fmn06JprPj4kVAteohz/image.png`.

## What the figure shows

Process Editor canvas of "Trigger Example v0.0.1": a green MCP Trigger shape at the start of the Process, feeding an exclusive gateway, an HTTP Request task and a Return shape, with the MCP Trigger panel open. (012_mcp-trigger-process.png)

## bpmn_evidence

BPMN 2.0 process diagram on the Frends Process Editor canvas: the MCP Trigger is drawn as the Process's start (trigger) shape, followed by gateway and task shapes and sequence flows.

## ai_evidence

The trigger shape turns the whole BPMN Process into a tool that an AI agent can call: the AI element is the interface the process is published through, rather than a task inside it.

## Notes for the researcher

- Boundary case: the AI here is the caller of the process rather than a task inside it. Included because the MCP Trigger is a shape in the process diagram and the page states it exists for AI agents and LLMs.
- Evidence read from the markdown twin https://docs.frends.com/reference/triggers/mcp-trigger.md.
