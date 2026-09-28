---
n: 213
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: BPM AI Decide Connector
url: https://marketplace.camunda.com/apps/428851/bpm-ai-decide-connector
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: A Web Modeler canvas with the element-template panel open. The visible fragment runs 'Document received' start event -> serviceTask 'Classify document' (selected, template 'BPM AI DECIDE CONNECTOR') -> a parallel / multi-instance fan-out into serviceTask 'Extract invoice number & total' and serviceTask 'Extract details' (the latter two drawn with the violet document glyph), with an 'Application' branch leaving the gateway. The panel shows the template's own fields: Input Variables {doc: "/opt/bpm-ai/doc.pdf"}, Decision Strategy 'Fast', Question/Task 'What kind of document is that?', Output Type 'String', Possible Values ["INVOICE", "APPLICATION", "OTHER"].
bpmn_evidence_quote: "Classify document"
ai_evidence: The template is an AI decision element with three model fields visible in the panel: Model / LLM 'OpenAI GPT-4', OCR Model 'Tesseract (local)', Speech Recognition Model 'OpenAI Whisper API' - i.e. an LLM call, a local OCR engine and a hosted speech model inside one task. The page describes the same element: the connector 'uses AI to analyze process variables and documents, provides explanations for decisions, and estimates confidence levels', with features 'Automated Decisions and Classification', 'Explainability and Confidence Estimation' (a confidence threshold defers to a human), 'Multimodal Support' (PDFs, images, audio), 'Integrated OCR Capabilities' and 'On-premises Support' for local AI models. The vendor is CAMUNDA SERVICES GmbH and the listing carries the 'AI Services' and 'Agentic AI orchestration' categories.
ai_evidence_quote: "The BPM AI Decide Connector uses AI to analyze process variables and documents, provides explanations for decisions, and estimates confidence levels"
artefacts:
  screenshot: 213_bpm-ai-decide-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: listing-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own asset (d3bql97l1ytoxn.cloudfront.net, app_resources/429.../overview/img9120571457029537901-2x.png, 856x660), read natively at full size
---

## What the page shows

The BPM AI Decide Connector (CAMUNDA SERVICES GmbH, open source, 8.4). A single connector task that answers a decision question - here a document-classification question - by calling an LLM, optionally OCR-ing or transcribing the input, and returning one of a declared set of output values plus a confidence estimate and a reasoning description.

## Observations (description only, no interpretation)

- **AI activity - function:** classify an incoming document into one of three declared values ("INVOICE", "APPLICATION", "OTHER") by asking the model 'What kind of document is that?'; the panel's Input Variables map the file path '/opt/bpm-ai/doc.pdf' into the call.
- **AI activity - element type:** a serviceTask bound to an element template (panel header 'BPM AI DECIDE CONNECTOR'), i.e. a connector task; the same glyph also appears on the two downstream extraction tasks.
- **AI activity - models named:** Model / LLM 'OpenAI GPT-4'; OCR Model 'Tesseract (local)'; Speech Recognition Model 'OpenAI Whisper API' - a mixed local/hosted stack chosen in one panel.
- **Authority - downstream:** the classification is the branch value: the canvas fans out to 'Extract invoice number & total' and 'Extract details' on the 'Application' path, so the model's label steers which extraction runs.
- **Authority - control:** the page's own 'Explainability and Confidence Estimation' feature: a reasoning description for each AI decision and a configurable confidence threshold above/below which the process defers to a human; the panel's Decision Strategy is set to 'Fast'.
- **Guardrails named on the page:** the confidence threshold, the declared Possible Values list (the model may only answer one of them), and the local-model option for privacy.
- **Data reachable by the model:** the document itself (PDF path or URL), scanned images and audio if the multimodal/OCR/ASR fields are used.
- **Human role:** not an element in the fragment; the page's confidence-threshold feature is where a human is meant to take over.

## Notes for the researcher

An open-source Camunda Services connector that puts a model choice, an OCR engine and a speech model in one task panel, with the decision question and the allowed answer set declared as template fields - the clearest example in this source of a decision task whose *answer space* is constrained by the element template rather than by a gateway condition. Worth the researcher's eye: 'On-premises Support' advertises local AI models 'for basic use cases', so the same task can be AI-bound with no external provider.
