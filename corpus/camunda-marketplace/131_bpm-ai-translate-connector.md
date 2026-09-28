---
n: 131
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: BPM AI Translate Connector
url: https://marketplace.camunda.com/apps/428848/bpm-ai-translate-connector
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: BPMN diagram published as the listing's own asset (Camunda Web Modeler, Implement view, properties panel open); no .bpmn downloadable. Read natively: start event -> 'Classify document' -> gateway 'Type?' -> the 'Invoice' branch ('Extract invoice number & total' -> 'Send to accounting' -> end 'Invoice processed') and the 'Application' branch ('Extract details' -> gateway 'Is English?' -> 'Translate Application' -> end).
bpmn_evidence_quote: "Translate Application"
ai_evidence: The process's translation step is bound to the connector template 'BPM AI TRANSLATE CONNECTOR' / 'Translate Application', and the properties panel open in the capture shows the binding: Template 'Applied', Translation Model 'Opus-MT (local)' - a neural machine-translation model - with LLM, OCR Model and Speech Recognition Model all set to 'None'. The page's own copy calls it AI: 'Using advanced AI, it translates text in various formats into any language'.
ai_evidence_quote: "Using advanced AI, it translates text in various formats into any language"
artefacts:
  screenshot: 131_bpm-ai-translate-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own asset (d3bql97l1ytoxn.cloudfront.net, app_resources/428848/overview/img4570296722247938288-2x.png, 856x660); native read at full size - a Camunda Web Modeler screenshot with the task's properties panel open
---

## What the page shows

The BPM AI Translate Connector (Camunda Services GmbH, connector template). The listing publishes one model: a document-classification flow ('Classify document', gateway 'Type?') that either extracts an invoice's number and total and sends it to accounting, or extracts the document details and translates them when they are not in English.

## Observations (description only, no interpretation)

- **AI activity - function:** machine translation of extracted document text when the gateway 'Is English?' answers No.
- **AI activity - element type:** an ordinary `serviceTask` labelled 'Translate Application', bound to the vendor's connector template; no agent element, no ad-hoc container.
- **Authority - downstream:** 'Send to accounting' (invoice branch) and the application branch's end event, reached only through the translation task when the text is not English.
- **Authority - data:** the process variable passed in as '= { text: application.body }' and written back as '= { textTranslated: result.text }'; no data objects are drawn.
- **Authority - control:** the gateways 'Type?' and 'Is English?' - the second is the only gate in front of the AI task.
- **Authority - control (human):** none visible in the published model; both branches run without a user task.
- **Input provenance:** the incoming document body ('application.body'), extracted by 'Extract details'.
- **Guards present:** the 'Is English?' gateway, which keeps the AI task out of the English path; no other guard is drawn.
- **Prompt / model detail visible:** the properties panel names the model - 'Opus-MT (local)' - and shows the target language 'English' and the input/output variable mapping; the LLM slot is explicitly 'None'.

## Notes for the researcher

Meets the artefact criteria on both layers: the published model is BPMN, and the AI element is inside the process - not merely described on the page - because the capture shows the task's properties panel with the translation model bound. Worth noting for the corpus: this listing's AI element is a local translation model (Opus-MT) rather than an LLM service, and the LLM slot is deliberately 'None'.
