---
n: 5
source: frends-docs
source_name: Frends documentation (docs.frends.com)
title: "Model Context Protocol"
url: https://docs.frends.com/frends-development/agentic-ai/model-context-protocol
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
needs_visual_check: false
bpmn_evidence: "BPMN 2.0 process diagram on the Frends Process Editor canvas: start event, exclusive gateway, task shapes and sequence flows. The Process is published as an MCP Tool by adding the MCP Trigger shape."
bpmn_evidence_quote: "Any Frends Process can be published as an MCP Tool by adding the MCP Trigger shape to the Process."
ai_evidence: "The task shape inside the process is an Intelligent AI Connector configured with MCP Tools and fed by an MCP Trigger: an AI/LLM element inside the process, not beside it."
ai_evidence_quote: "AI Connector with MCP Tools enabled."
artefacts:
  screenshot: 003_mcp-trigger-process.png
  assets: [003_mcp-trigger-process.png, 003_ai-connector-mcp-tools.png]
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

`https://docs.frends.com/frends-development/agentic-ai/model-context-protocol` (ledger row n=5), figure asset `/spaces/QI65mBosbdweu563CvPI/uploads/uTECD5nta9TVhCuo7Rl7/image.png`.

## What the figure shows

Frends Process Editor canvas, Process "AP101 MCP Tool - Get Invoice Details": a Start event, an exclusive gateway, an AI Connector task labelled "Get invoice details for invoiceID", and an Output Reference shape, joined by sequence flows. (003_mcp-trigger-process.png); Process Editor canvas of a fuller Process whose AI Connector shape has its configuration panel open with MCP Tools listed. (003_ai-connector-mcp-tools.png)

## bpmn_evidence

BPMN 2.0 process diagram on the Frends Process Editor canvas: start event, exclusive gateway, task shapes and sequence flows. The Process is published as an MCP Tool by adding the MCP Trigger shape.

## ai_evidence

The task shape inside the process is an Intelligent AI Connector configured with MCP Tools and fed by an MCP Trigger: an AI/LLM element inside the process, not beside it.

## Notes for the researcher

- The page documents both directions of MCP: Frends Processes exposed as MCP Tools for AI to call, and the AI Connector consuming MCP Tools.
- The same two figures are also published on ledger row n=2 (Agentic AI); recorded again here because row n=5 is a different page.
- Evidence read from the markdown twin https://docs.frends.com/frends-development/agentic-ai/model-context-protocol.md.
