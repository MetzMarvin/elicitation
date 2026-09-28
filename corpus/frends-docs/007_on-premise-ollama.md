---
n: 209
source: frends-docs
source_name: Frends documentation (docs.frends.com)
title: "How to use on-premise Ollama with AI Connector"
url: https://docs.frends.com/guides/ai-features/how-to-use-on-premise-ollama-with-ai-connector
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
needs_visual_check: false
bpmn_evidence: "BPMN 2.0 process diagram on the Frends Process Editor canvas: start event, HTTP Request task, AI Connector task and sequence flows."
bpmn_evidence_quote: "Configuring the AI Connector with your own Ollama installation can optimize your AI Process's performance and security."
ai_evidence: "The AI Connector is a shape inside the Process and is bound to an on-premise Ollama model, so the LLM is a task in the flow."
ai_evidence_quote: "Example of using Ollama service with AI Connector."
artefacts:
  screenshot: 007_ollama-process.png
  assets: [007_ollama-process.png]
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

`https://docs.frends.com/guides/ai-features/how-to-use-on-premise-ollama-with-ai-connector` (ledger row n=209), figure asset `/spaces/0p415NUmUmiF4ayjI81L/uploads/gi6BykU3DE3haCAn1h7q/image.png`.

## What the figure shows

Process Editor canvas: a Start, an HTTP Request task and an AI Connector shape labelled "Readout service request", with the AI Connector panel configured for an on-premise Ollama service. (007_ollama-process.png)

## bpmn_evidence

BPMN 2.0 process diagram on the Frends Process Editor canvas: start event, HTTP Request task, AI Connector task and sequence flows.

## ai_evidence

The AI Connector is a shape inside the Process and is bound to an on-premise Ollama model, so the LLM is a task in the flow.

## Notes for the researcher

- On-premise binding: the LLM runs on the customer's own server, which matters for the data-protection discussion.
- Evidence read from the markdown twin https://docs.frends.com/guides/ai-features/how-to-use-on-premise-ollama-with-ai-connector.md.
