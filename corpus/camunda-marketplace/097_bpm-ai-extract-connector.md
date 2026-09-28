---
n: 97
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: BPM AI Extract Connector
url: https://marketplace.camunda.com/apps/428850/bpm-ai-extract-connector
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: BPMN diagram published as the listing's overview asset (Camunda Web Modeler, Implement tab); no .bpmn downloadable. Read natively: start event 'Document received' -> 'Classify document' -> exclusive gateway 'Type?' -> (Invoice branch) 'Extract invoice number & total' -> 'send to accounting', (Application branch) 'Extract details' -> exclusive gateway 'Is English?' with a 'No' branch to a translation activity. Annotations on the extraction task read 'PDF path or url in input variable' and 'Specify JSON schema'.
bpmn_evidence_quote: "Extract invoice number & total"
ai_evidence: The AI element is the extraction task itself, and its binding is visible in the published properties panel: 'BPM AI EXTRACT CONNECTOR' with Model = LLM set to 'OpenAI GPT-4' (OCR Model and Speech Recognition Model are None), an input variable doc = /opt/bpm-ai/doc.pdf, a Data Extraction output schema naming `invoiceNum` and `total`, Extraction Mode 'Single' and an output mapping `invoice = result`. The page states 'The BPM AI Extract Connector uses AI models to extract information from any unstructured data based on a custom JSON output schema' and offers 'Accountable, Hallucination-free Extraction' by switching from generative models (named as OpenAI's GPT-4) to specialized extraction models.
ai_evidence_quote: "The BPM AI Extract Connector uses AI models to extract information from any unstructured data based on a custom JSON output schema"
artefacts:
  screenshot: 097_bpm-ai-extract-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own overview asset (d3bql97l1ytoxn.cloudfront.net, overview/img1797679321922276478-2x.png, 856x660); native read at full size - the asset is a Web Modeler screenshot with the task's properties panel open
---

## What the page shows

holisticon's (CAMUNDA SERVICES GmbH) BPM AI Extract Connector listing (Partner, 8.4, 'Extract critical information using AI'). The page describes an outbound connector that turns PDFs, images, audio or plain text into structured process variables against a caller-defined JSON schema, with a choice of generative or specialized extraction models. Its published artefact is a Web Modeler screenshot of a document-classification process in which the extraction task is configured and highlighted.

## Observations (description only, no interpretation)

- **AI activity - function:** extract structured fields (invoice number, total) from an unstructured document according to a JSON schema.
- **AI activity - element type:** an ordinary task bound to the BPM AI Extract Connector element template; the model choice (LLM = OpenAI GPT-4) is set in the properties panel, not in a dedicated AI element.
- **Authority - downstream:** the gateway 'Is English?' and the translation activity consume the extraction result; the 'Invoice' branch routes it to 'send to accounting'.
- **Authority - data:** the input document (variable `doc`, path /opt/bpm-ai/doc.pdf) and the output variable `invoice`; the schema defines exactly which fields are extracted.
- **Authority - control:** two exclusive gateways ('Type?', 'Is English?') route by document type and language, but neither guards the extraction's accuracy; no confidence threshold or human review is visible.
- **Input provenance:** the start event 'Document received'; the classification task runs before extraction.
- **Guards present:** the output schema itself (a fixed JSON contract) and the page's offer of specialized non-generative models for verbatim extraction; nothing in the model checks the model's output.
- **Prompt / model detail visible:** the model is visible (OpenAI GPT-4); no prompt text is shown, only the schema and the input variable.

## Notes for the researcher

This is the strongest AI evidence in the batch: the connector's own properties panel is published, so the AI binding is a visible configuration rather than a page claim. The researcher may want to note the contrast with n=102 (same vendor, same template family): here the model is chosen explicitly, and the page discusses hallucination risk and offers a non-generative alternative.
