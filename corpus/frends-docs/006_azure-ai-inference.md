---
n: 208
source: frends-docs
source_name: Frends documentation (docs.frends.com)
title: "How to use Azure AI Inference service with AI Connector"
url: https://docs.frends.com/guides/ai-features/how-to-use-azure-ai-inference-service-with-ai-connector
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
needs_visual_check: false
bpmn_evidence: "BPMN 2.0 process diagram on the Frends Process Editor canvas: start event, AI Connector task, sequence flows to the following tasks."
bpmn_evidence_quote: "Configuring the AI Connector with your own Azure AI Inference service can optimize your AI Process's performance and security."
ai_evidence: "The AI Connector is a task shape in the Process and the panel binds it to an Azure AI Inference service, i.e. an external LLM behind the shape."
ai_evidence_quote: "Example of using Azure AI Inference service with AI Connector."
artefacts:
  screenshot: 006_azure-ai-process.png
  assets: [006_azure-ai-process.png]
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

`https://docs.frends.com/guides/ai-features/how-to-use-azure-ai-inference-service-with-ai-connector` (ledger row n=208), figure asset `/spaces/0p415NUmUmiF4ayjI81L/uploads/FpD8qLebqPxOK8uJslQ8/screenshot-rocks - 2025-09-25T091547.464.png`.

## What the figure shows

Frends Control Panel with the Process Editor open on "Analyze & Deliver Invoices to SAP v0.1": a Start, an AI Connector shape and the following tasks, with the AI Connector panel showing an Azure AI Inference service configuration. (006_azure-ai-process.png)

## bpmn_evidence

BPMN 2.0 process diagram on the Frends Process Editor canvas: start event, AI Connector task, sequence flows to the following tasks.

## ai_evidence

The AI Connector is a task shape in the Process and the panel binds it to an Azure AI Inference service, i.e. an external LLM behind the shape.

## Notes for the researcher

- Vendor-specific LLM binding (Azure) rather than the default Frends AI service - useful if the thesis wants service-type variation.
- Evidence read from the markdown twin https://docs.frends.com/guides/ai-features/how-to-use-azure-ai-inference-service-with-ai-connector.md.
