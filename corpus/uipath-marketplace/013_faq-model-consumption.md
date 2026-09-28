---
n: 1740
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: "FAQ Model Consumption"
url: https://marketplace.uipath.com/listings/faq-model-consumption
accessed: 2026-09-28
verdict: UNCERTAIN
needs_human_ruling: true
question: "Visio-style flowchart (sharp-cornered rectangles, labelled decision diamonds with Yes/No, no BPMN events) with Document Understanding classify/extract steps and human-validation gates. Does it count as a BPMN diagram? (The same diagram is re-used on n=1746.)"
needs_visual_check: false
bpmn_evidence: slide 'High level solution design': rectangles, decision diamonds 'Human Validation Needed' with Yes/No arcs, no events or lanes; flowchart-style notation
bpmn_evidence_quote: "Find answers using partial search, semantic search or using LLM model(s)."
ai_evidence: boxes 'Document Understanding Vendor Matching Process - Classify Documents (W9)' and '... Extract Documents Information (W9)'; page prose on LLM and sentiment models
ai_evidence_quote: "Find answers using partial search, semantic search or using LLM model(s)."
artefacts:
  screenshot: 013_faq-model-consumption.png
  archive: 013_faq-model-consumption.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: marginal
capture_width_px: 1600
capture_method: python urllib GET of the original marketplace-cdn.uipath.com asset (cdn-cgi resize wrapper stripped); 1600 px is the native size; a 3x LANCZOS crop of the diagram region is saved as 013_faq-model-consumption_diagram-crop-3x.png (3420 px)
---

## What the page shows

A Solution Accelerator for FAQ model consumption (semantic and sentiment analysis in support automation). Its second image, 'High level solution design', shows: 'Email Dispatcher Process - Extracts Vendor Information and Documents (W9) from Email Inbox' -> 'Document Understanding Vendor Matching Process - Classify Documents (W9)' -> diamond 'Human Validation Needed' (Yes -> 'Classification Validation - Human review of classification results') -> 'Document Understanding Vendor Matching Process - Extract Documents Information (W9)' -> diamond 'Human Validation Needed' (Yes -> 'Extraction Validation - Human review of extraction results') -> 'Finalizer Process - Post W9 and Vendor Data to SAP' -> 'SAP', with 'Update Original Request' back-arrow; red annotation 'Action Center Components'. The diagram content concerns W9 vendor documents, not FAQ handling.

## Observations (description only, no interpretation)

- **AI activity - function:** 'Classify Documents (W9)' and 'Extract Documents Information (W9)'; prose: 'Find answers using partial search, semantic search or using LLM model(s). Interpret answer sentiment and offer possible responses.'
- **AI activity - element type:** rectangles labelled 'Document Understanding Vendor Matching Process'
- **Authority - downstream:** 'Finalizer Process - Post W9 and Vendor Data to SAP'
- **Authority - data:** vendor W9 data posted to SAP
- **Authority - control:** diamonds 'Human Validation Needed' route results to human validation or onwards
- **Input provenance:** 'Extracts Vendor Information and Documents (W9) from Email Inbox'
- **Guards present:** 'Classification Validation - Human review of classification results', 'Extraction Validation - Human review of extraction results' (Action Center)
- **Prompt / model detail visible:** dependency 'UiPath.MicrosoftAzureOpenAI.IntegrationService.Activities: 7.1.0'

## Notes for the researcher

The diagram region is pixel-identical on the 'Vendor Document Verification' listing (n=1746, ledger E3 of this record). Native asset 1600 px; the diagram sits in a laptop mock-up, the 3x crop is legible.
