---
n: 132
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Amazon Textract Connector
url: https://marketplace.camunda.com/apps/473161/amazon-textract-connector
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: BPMN diagram published as the listing's own asset (Camunda Web Modeler, Implement view, autosaved); no .bpmn downloadable. Read natively: start event 'Start' -> one service task -> end event 'End'.
bpmn_evidence_quote: "Extract data from document"
ai_evidence: The process's only task is the connector call under test, and the page names the AI service it invokes: 'Amazon Textract is a machine learning (ML) service that automatically extracts text, handwriting, layout elements, and data from scanned documents'. The task carries the connector's element-template glyph at its top-left.
ai_evidence_quote: "Amazon Textract is a machine learning (ML) service that automatically extracts text, handwriting, layout elements, and data from scanned documents"
artefacts:
  screenshot: 132_amazon-textract-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own asset (d3bql97l1ytoxn.cloudfront.net, app_resources/473161/overview/img3457117868907388911-2x.png, 1100x590); native read at full size - a Camunda Web Modeler Implement view
---

## What the page shows

The Amazon Textract Connector (Camunda Services GmbH, outbound connector). The listing publishes a minimal model in the Camunda Web Modeler Implement view - a start event, the connector's service task, and an end event - as the demonstration of how the connector is used inside a process.

## Observations (description only, no interpretation)

- **AI activity - function:** text, handwriting, layout and data extraction from scanned documents, by the Amazon Textract ML service.
- **AI activity - element type:** an ordinary `serviceTask` labelled 'Extract data from document' with the connector's element-template glyph; no agent element and no ad-hoc container.
- **Authority - downstream:** the end event 'End' - the model shows the extracted result leaving the process without a further branch.
- **Authority - data:** none drawn; the page's feature list says the connector processes document types and returns extracted data as process variables.
- **Authority - control:** none - the published model has no gateway, so there is no drawn guard or escalation around the AI call.
- **Authority - control (human):** none in the model; the page's second feature ('reducing manual work and increasing accuracy in document-centric processes') leaves human review outside the drawn process.
- **Input provenance:** the scanned document handed to the connector.
- **Guards present:** none drawn in the published model.
- **Prompt / model detail visible:** none - the model names no OCR mode, feature type or configuration.

## Notes for the researcher

The published artefact is a three-element model, i.e. the smallest possible shape that still shows the AI call inside a process. Recorded as INCLUDE: the connector's task is drawn inside a BPMN process, and the page names the ML service behind it. If the method wants to weight artefacts by how much process surrounds the AI element, this is a minimal one.
