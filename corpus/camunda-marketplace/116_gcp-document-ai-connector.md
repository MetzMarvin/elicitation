---
n: 116
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: GCP Document AI Connector
url: https://marketplace.camunda.com/apps/820092/gcp-document-ai-connector
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: The page describes an AI-bound element inside the process - a Camunda service task that submits PDFs and images to a Google Cloud Document AI processor and returns OCR text, entities, tables and confidence scores as process variables - but the listing publishes no BPMN artefact at all (screenshots list is empty; its only image is the partner's 230x69 HCLTech wordmark) and it is tagged 'Listing Only'. Is a described-but-unpublished AI service task enough to record this listing, or is it E0-no-artefact?
needs_visual_check: false
bpmn_evidence: No BPMN artefact on the page, and none downloadable: the listing's screenshots list is empty, `links` is empty, and its single published image is the partner's wordmark. The listing is tagged 'Listing Only'. The connector's task is described only in prose ('directly from a Camunda service task'), so no process model exists to inspect.
bpmn_evidence_quote: "Listing Only"
ai_evidence: The AI binding is stated explicitly for an element inside the process: 'Submit PDF documents and image files such as PNG and JPEG to Google Cloud Document AI processors directly from a Camunda service task', with results 'returned as structured process variables' including 'OCR text, named entities, table data, and confidence scores' that downstream steps consume 'without manual parsing'. The page also says the connector 'brings Google Cloud Document AI natively into Camunda processes'. None of it is visible: no diagram, no canvas and no element template is published.
ai_evidence_quote: "Submit PDF documents and image files such as PNG and JPEG to Google Cloud Document AI processors directly from a Camunda service task"
artefacts:
  screenshot: 116_gcp-document-ai-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 230
capture_method: curl of the listing's only image (d3bql97l1ytoxn.cloudfront.net, thumbs_112/img16974186475810180814-2x.png, 230x69 - the 'HCLTech' wordmark); native read at full size. No diagram is published, so the partner wordmark is the only capturable artefact.
---

## What the page shows

HCLTech's listing for a Google Cloud Document AI connector (Partner, 'Listing Only', tagged 'AI Services' and 'Outbound Connector'). The page describes a connector that submits documents to a Document AI processor from a Camunda service task, authenticates through Google Cloud OAuth 2.0, runs asynchronously via job workers and returns structured extraction results. It publishes no diagram.

## Observations (description only, no interpretation)

- **AI activity - function:** extract text, entities, tables and confidence scores from PDFs and images via Google Cloud Document AI.
- **AI activity - element type:** described as a Camunda `serviceTask` / outbound connector; the artefact itself is not published, so its element type is not verifiable.
- **Authority - downstream:** 'downstream process steps' are named as consumers of the extracted values; no model is published.
- **Authority - data:** document bytes in Base64 plus the returned extraction fields; no data objects are drawn.
- **Authority - control:** the page advertises 'built-in retry handling' and asynchronous execution; no gateway, threshold or reviewer is shown.
- **Authority - control (human):** none mentioned; the stated benefit is that values are used 'without manual parsing'.
- **Input provenance:** process variables carrying a PDF or image, submitted by the task.
- **Guards present:** none visible - only retry handling is described.
- **Prompt / model detail visible:** the processor is named (Google Cloud Document AI) but no processor id, model or prompt is shown.

## Notes for the researcher

This is the batch's clearest case of CLAUDE.md's 'implementation might be AI-bound but is not visible'. Document AI is unambiguously an AI service and the page places its call inside a Camunda service task, but the listing (tagged 'Listing Only') publishes no process artefact at all - compare the Ollama listing (n=058), recorded UNCERTAIN on the same reasoning, and the ABBYY Vantage connector (n=085), which is an INCLUDE only because it does publish a canvas showing 'Upload File to ABBYY Vantage'. E2 is not available here because there is no artefact to judge.
