---
n: 203
source: frends-docs
source_name: Frends documentation (docs.frends.com)
title: "Creating semi-deterministic AI Process"
url: https://docs.frends.com/guides/ai-features/creating-semi-deterministic-ai-process
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
needs_visual_check: false
bpmn_evidence: "BPMN 2.0 process diagram on the Frends Process Editor canvas. The page is explicit that the control flow stays BPMN: the structure, the step count and the branching conditions are designed, and only the reasoning inside a step is delegated to the AI."
bpmn_evidence_quote: "the BPMN flow, the number of steps, and the branching conditions are all defined by you"
ai_evidence: "The process diagram contains a native AI task (\"Categorize Ticket\") whose configuration names an AI model and a system prompt; the AI is a shape inside the BPMN flow and the outgoing gateway branches on the AI's own output."
ai_evidence_quote: "Frends supports embedding AI reasoning directly into your integration Processes using the Intelligent AI Connector shape."
artefacts:
  screenshot: 004_example-process-canvas.png
  assets: [004_example-process-canvas.png, 004_categorize-ticket-branch.png, 004_ai-connector-panel.png]
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

`https://docs.frends.com/guides/ai-features/creating-semi-deterministic-ai-process` (ledger row n=203), figure asset `/spaces/0p415NUmUmiF4ayjI81L/uploads/w23zyWQqa45Vh5h1wVXB/image.png`.

## What the figure shows

Process Editor canvas of "AI Example Process v0.11": Start, Analyze Ticket, a green Categorize Ticket (AI) task, an exclusive gateway branching to Raise Issue / Raise Support Request / Notify Support Lead / Alert Support, and an end event. (004_example-process-canvas.png); BPMN fragment: the AI task "Categorize Ticket" feeding an exclusive gateway with four labelled outgoing sequence flows (Technical Issue, Billing Inquiry, Low confidence, Unknown). (004_categorize-ticket-branch.png); AI Connector configuration panel: Service Type "Frends AI", AI Model Name "GPT - Data Classification", and a system prompt describing a support-ticket classification assistant. (004_ai-connector-panel.png)

## bpmn_evidence

BPMN 2.0 process diagram on the Frends Process Editor canvas. The page is explicit that the control flow stays BPMN: the structure, the step count and the branching conditions are designed, and only the reasoning inside a step is delegated to the AI.

## ai_evidence

The process diagram contains a native AI task ("Categorize Ticket") whose configuration names an AI model and a system prompt; the AI is a shape inside the BPMN flow and the outgoing gateway branches on the AI's own output.

## Notes for the researcher

- The clearest semi-deterministic example in the source: a deterministic BPMN skeleton with an AI reasoning step and human-facing branches inside it.
- The figure that carries the AI task has no AI wording in its caption, so it was classified by looking at the figure rather than from text.
- Evidence read from the markdown twin https://docs.frends.com/guides/ai-features/creating-semi-deterministic-ai-process.md.
