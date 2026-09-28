---
n: 0
url: https://www.ofelia.com/product/it-hub
source: bonitasoft
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: >-
  The figure is a boxes-and-arrows agent-runtime diagram, not BPMN 2.0, but it does show
  an AI agent sequence with control flow: is such a proprietary agent diagram inside the
  artefact criteria (BPMN 2.0 only), or a find in its own right?
bpmn_evidence: >-
  The figure `Frame 2147263655.svg` is a boxes-and-arrows architecture diagram of the
  Ofelia agent runtime, not a BPMN 2.0 model. It is a Figma-style export with zero
  `<text>` nodes and no bpmn-js provenance, so the box labels below were read from the
  pixels. Its boxes are: "User message (Slack / Teams)" -> "Tool Mapping Agent (Intent
  classifier)" -> "User confirms action" -> "Action Agent (Exec. procedures)", "Answerer
  Agent (RAG responses)", "Out-of-scope (Graceful decline)", "Action Result (Feedback
  format)", with "Knowledge Retrieval System" (Vector Search / Knowledge Graph / Key-value
  Lookup), "Deterministic Execution -> BPA Engine Handoff", "Action execution (API calls
  under user token)", "Workflow Orchestration (BPMN sequencing & SLA)" and "Grounded
  Response". One box names BPMN ("BPMN sequencing & SLA") and one names an engine handoff,
  but the drawing itself is an architecture diagram.
ai_evidence: >-
  The AI is the subject of the diagram rather than an element inside a process: three of
  the boxes are agents ("Tool Mapping Agent (Intent classifier)", "Action Agent (Exec.
  procedures)", "Answerer Agent (RAG responses)") and one is the knowledge store they
  retrieve from ("Knowledge Retrieval System" with "Vector Search / Knowledge Graph /
  Key-value Lookup"). The page's other figures are a layered architecture stack
  (`dev-engine_visual.svg`) and a nested security stack (`Image Container.svg`).
artefacts:
  - screenshot: 015_ofelia-agent-runtime-diagram.png
  - figure: the Ofelia agent-runtime diagram (Frame 2147263655.svg)
capture_quality: legible
capture_width_px: 1400
capture_height_px: 801
---

## What the page shows

The page's figure "Frame 2147263655.svg" is a boxes-and-arrows diagram of the Ofelia agent runtime, and the boxes are AI agents: "User message (Slack / Teams)" -> "Tool Mapping Agent (Intent classifier)" -> "User confirms action" -> "Action Agent (Exec. procedures)", "Answerer Agent (RAG responses)", "Out-of-scope (Graceful decline)", "Action Result (Feedback format)", with a "Knowledge Retrieval System" (Vector Search / Knowledge Graph / Key-value Lookup), "Deterministic Execution -> BPA Engine Handoff", "Action execution (API calls under user token)", "Workflow Orchestration (BPMN sequencing & SLA)" and "Grounded Response". It names BPMN inside one of its boxes, but the drawing itself is an architecture diagram, not a BPMN 2.0 model. The page's other figures are a layered architecture stack (dev-engine_visual) and a nested security stack (Image Container).

## Observations

- Notation: a boxes-and-arrows architecture diagram.
- Evidence looked at: Frame 2147263655.svg looked at in full (774x443), with dev-engine_visual.svg and Image Container.svg.
- The page is `/product/it-hub`; the figure is `Frame 2147263655.svg` (774x443 as published; the capture is the same figure at 1400x801).
- This is the pixel-level finding; the same wording is the ledger row for this page, so the two cannot disagree.

## Notes for the researcher

One of the five www.ofelia.com pages ruled UNCERTAIN in this source (records 012-016). The other 127 judged site pages are E0/E1/E2/E3 ledger rows without records.
