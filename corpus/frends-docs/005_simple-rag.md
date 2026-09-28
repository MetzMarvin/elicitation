---
n: 205
source: frends-docs
source_name: Frends documentation (docs.frends.com)
title: "How to implement a simple RAG in Frends"
url: https://docs.frends.com/guides/ai-features/how-to-implement-a-simple-rag-in-frends
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
needs_visual_check: false
bpmn_evidence: "BPMN 2.0 process diagram on the Frends Process Editor canvas: start event, AI Connector task, exclusive gateway, downstream tasks and sequence flows."
bpmn_evidence_quote: "Retrieval-augmented generation at its simplest is a standard Frends Process with AI."
ai_evidence: "The AI Connector is a step inside the Process; the retrieved context is passed into it as part of the prompt, so the LLM sits in the BPMN flow."
ai_evidence_quote: "AI Connector and user prompt."
artefacts:
  screenshot: 005_rag-process-canvas.png
  assets: [005_rag-process-canvas.png]
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

`https://docs.frends.com/guides/ai-features/how-to-implement-a-simple-rag-in-frends` (ledger row n=205), figure asset `/spaces/0p415NUmUmiF4ayjI81L/uploads/TNmtk3pyVKvMhnJiD9x9/image.png`.

## What the figure shows

Process Editor canvas of "Frends BAG Example v0.01": a Start with an AI Connector shape labelled "Connects to the Question", an exclusive gateway and further HTTP/decision shapes, with the AI Connector panel open showing the user prompt. (005_rag-process-canvas.png)

## bpmn_evidence

BPMN 2.0 process diagram on the Frends Process Editor canvas: start event, AI Connector task, exclusive gateway, downstream tasks and sequence flows.

## ai_evidence

The AI Connector is a step inside the Process; the retrieved context is passed into it as part of the prompt, so the LLM sits in the BPMN flow.

## Notes for the researcher

- The page frames RAG as an ordinary Process, which is why the diagram rather than the configuration panels is the artefact of interest.
- Evidence read from the markdown twin https://docs.frends.com/guides/ai-features/how-to-implement-a-simple-rag-in-frends.md.
