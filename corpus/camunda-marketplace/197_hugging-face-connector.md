---
n: 197
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Hugging Face Connector
url: https://marketplace.camunda.com/apps/439557/hugging-face-connector
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: A Camunda Modeler capture (project 'New BPMN Diagram', Design tab, 'Autosaved'): none start event -> serviceTask 'call Lama' -> none end event. The task carries the Hugging Face connector glyph (the hugging-face emoji used as the element template's icon); no .bpmn is downloadable.
bpmn_evidence_quote: "call Lama"
ai_evidence: The single task in the model calls a Hugging Face model. The page names the capability and the route: 'This Connector enables you to integrate machine learning into BPMN-based processes by using the Hugging Face Inference API', listing the model families 'BERT, GPT (including OpenAI's GPT-3), and DistilBERT' and the use cases 'text classification, translation, summarization'. Tags: 'AI Services', 'Agentic AI orchestration'.
ai_evidence_quote: "This Connector enables you to integrate machine learning into BPMN-based processes by using the Hugging Face Inference API"
artefacts:
  screenshot: 197_hugging-face-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1100
capture_method: curl of the listing's own asset (d3bql97l1ytoxn.cloudfront.net, app_resources/439557/overview/img7886259821214759615-2x.png, 1100x549); native read at full size - a Camunda Modeler canvas
---

## What the page shows

The Hugging Face Connector (Camunda Services GmbH, out-of-the-box outbound connector). A single model-inference call placed directly in the process, with the model chosen in the connector's configuration.

## Observations (description only, no interpretation)

- **AI activity - function:** model inference - the process calls a Hugging Face model ('call Lama' - a Llama model, by the label) through the Inference API.
- **AI activity - element type:** one serviceTask carrying the Hugging Face element-template glyph; no agent element, no container, no gateway.
- **Authority - downstream:** none drawn; the task's result is the process's only output.
- **Authority - data:** not shown - no data objects, and the payload fields are not visible in the capture.
- **Authority - control:** none - the model has no branch or threshold.
- **Authority - control (human):** none drawn; fully automated path from start to end.
- **Input provenance:** not shown (a bare start event).
- **Guards present:** none shown.
- **Prompt / model detail visible:** the model is named only in the task label ('call Lama'); no prompt, parameters or template configuration is visible, and no .bpmn is published to inspect.

## Notes for the researcher

The AI binding here is the connector's identity rather than a visible model field: the task's label names a model family and the template glyph is drawn, but the payload is not shown. Recorded INCLUDE on the same basis as the OpenAI connector (n=195) - the connector's whole purpose is the model call it makes inside the process.
