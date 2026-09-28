---
n: 4
source: frends-docs
source_name: Frends documentation (docs.frends.com)
title: "Intelligent AI Connector"
url: https://docs.frends.com/frends-development/agentic-ai/intelligent-ai-connector
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
needs_visual_check: false
bpmn_evidence: "The first capture is the Frends Process Editor canvas: a BPMN activity box carrying the AI Connector, an arrowed sequence flow entering it, and the editor's shape palette beside it. The page's own vocabulary is BPMN 2.0 - verbatim “BPMN 2.0 with AI Connector enables AI Orchestrations.” and “The whole process for multiple different ticket cases can be written as a series of prompts, decisions, and actions” - and the vendor's Process shape reference (opened 2026-09-26 on this source) documents “Export BPMN XML” as “exporting the BPMN diagram for the Frends Process in XML format”."
bpmn_evidence_quote: "BPMN 2.0 with AI Connector enables AI Orchestrations."
ai_evidence: "The AI element is the shape itself, configured inside the process: the capture shows the AI Connector shape on the canvas with its User Prompt (“I want you to act as a customer service...” with Subject/Message bindings) and its System prompts section. The page states verbatim “It allows the AI to participate in your Processes by performing actions you have specified as prompts, in the location of the Process you need to” and “Instead of requiring a human decision for categorizing an incoming message into tech or sales support cases, AI Connector with LLM models can read and categorize the message for you automatically.”"
ai_evidence_quote: "It allows the AI to participate in your Processes by performing actions you have specified as prompts, in the location of the Process you need to."
artefacts:
  screenshot: 002_ai-connector-shape-in-the-process-editor.png
  assets: [002_ai-connector-shape-in-the-process-editor.png, 002_invoice-exception-process-with-native-ai-task.png]
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

`https://docs.frends.com/frends-development/agentic-ai/intelligent-ai-connector` (ledger row n=4), figure asset `/spaces/QI65mBosbdweu563CvPI/uploads/p1WkDaJCqsOSxicyXuyp/screenshot-rocks (76).png`.
Also used on ledger rows: n=2.

## What the figure shows

the AI Connector shape (labelled 'Categorize the incoming message') on the Process Editor canvas, with an incoming sequence flow, and the shape's Prompts / Options / Configuration panel open on User Prompt and System prompts (002_ai-connector-shape-in-the-process-editor.png); a complete BPMN 2.0 process diagram on the same canvas with a Native AI Task inside it (002_invoice-exception-process-with-native-ai-task.png)

## bpmn_evidence

The first capture is the Frends Process Editor canvas: a BPMN activity box carrying the AI Connector, an arrowed sequence flow entering it, and the editor's shape palette beside it. The page's own vocabulary is BPMN 2.0 - verbatim “BPMN 2.0 with AI Connector enables AI Orchestrations.” and “The whole process for multiple different ticket cases can be written as a series of prompts, decisions, and actions” - and the vendor's Process shape reference (opened 2026-09-26 on this source) documents “Export BPMN XML” as “exporting the BPMN diagram for the Frends Process in XML format”.

## ai_evidence

The AI element is the shape itself, configured inside the process: the capture shows the AI Connector shape on the canvas with its User Prompt (“I want you to act as a customer service...” with Subject/Message bindings) and its System prompts section. The page states verbatim “It allows the AI to participate in your Processes by performing actions you have specified as prompts, in the location of the Process you need to” and “Instead of requiring a human decision for categorizing an incoming message into tech or sales support cases, AI Connector with LLM models can read and categorize the message for you automatically.”

## Notes for the researcher

- This is the same figure as record 001's second capture, re-published on the Intelligent AI Connector page: the same diagram is recorded once, at this row, and row n=2 cites it. Both rows stay in the ledger (they are two enumerated pages), but the corpus record is not duplicated.
- The AI Connector is the vendor's own building block for putting an LLM step inside a BPMN process; this page is its description page, which is why it is the clearest INCLUDE in the source together with row n=2.
- The third figure on the page (“AI Connector with MCP Tools enabled.”) shows agentic-mode configuration of the same shape and is recorded in the row's evidence rather than as a separate record.
