---
n: 1804
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: "Trade Finance Documents - Data Extraction"
url: https://marketplace.uipath.com/listings/document-examination-and-review
accessed: 2026-09-28
verdict: UNCERTAIN
needs_human_ruling: true
question: "Visio-style flowchart with two containers ('1. Dispatcher Process Template - Collect Trade Finance Docs', '2. Document Understanding Process'), queue/storage icons and a Validation Station, no BPMN events or gateways; AI = GenAI/ML extraction per the listing. Does it count as a BPMN diagram? (The same diagram is re-drawn on n=1805.)"
needs_visual_check: true
bpmn_evidence: slide 'High level solution design': two containers with rectangles, a D-shaped 'Extract and Filter Trade Finance Files' symbol, queue and storage-bucket icons, 'Validation Station'; small labels, flowchart-style notation
bpmn_evidence_quote: "allows for rapid human in the loop review and input where necessary."
ai_evidence: box 'Digitize Docs and Extract Data' inside '2. Document Understanding Process'; prose 'It uses GenAI pre-trained models, for efficient data extraction'
ai_evidence_quote: "It uses GenAI pre-trained models, for efficient data extraction, however it is also adaptable to other various models."
artefacts:
  screenshot: 018_trade-finance-documents-data-extraction.png
  archive: 018_trade-finance-documents-data-extraction.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: marginal
capture_width_px: 1600
capture_method: python urllib GET of the original marketplace-cdn.uipath.com asset (cdn-cgi resize wrapper stripped); 1600 px is the native size; a 3x LANCZOS crop of the diagram region is saved as 018_trade-finance-documents-data-extraction_diagram-crop-3x.png (3420 px)
---

## What the page shows

A Trade Finance Solution Accelerator for extracting data from Letters of Credit, Bills of Lading, Insurance Certificates etc. Its second image, 'High level solution design': container '1. Dispatcher Process Template - Collect Trade Finance Docs' ('Custom Filtering configuration' -> 'Extract and Filter Trade Finance Files' -> 'Custom Logic' -> 'Add a queue item for each documents and upload them to Storage bucket') -> 'Storage bucket' / 'Trade Finance Docs Queues' -> container '2. Document Understanding Process' ('Digitize Docs and Extract Data' -> 'Custom Data Parsing Logic' -> 'Create assigned Document Validation' -> 'Validation Station' -> 'Custom Logic'), with side notes 'User will validate the documents & data and select the related PO/ other aggregated information' and 'UiPath Validation Station'.

## Observations (description only, no interpretation)

- **AI activity - function:** 'Digitize Docs and Extract Data' (GenAI pre-trained models per prose)
- **AI activity - element type:** rectangle 'Digitize Docs and Extract Data' in the Document Understanding container
- **Authority - downstream:** 'Custom Data Parsing Logic' -> 'Create assigned Document Validation' -> 'Validation Station' -> 'Custom Logic'
- **Authority - data:** 'the required data (100's of data points) from Trade Finance post transaction documents' (prose)
- **Authority - control:** 'Validation Station' (human) before 'Custom Logic'
- **Input provenance:** 'extracts documents from a Location (network drive, application, etc.) and then filters and processes them' (diagram note)
- **Guards present:** 'User will validate the documents & data and select the related PO/ other aggregated information' (UiPath Validation Station)
- **Prompt / model detail visible:** none

## Notes for the researcher

Labels are small; the 3x crop is readable for the main boxes, side notes are marginal (needs_visual_check for those). A re-drawn copy of the same diagram (identical labels, slightly different layout) is on 'Trade Finance - Create Letters of Credit' (n=1805, ledger E3 of this record).
