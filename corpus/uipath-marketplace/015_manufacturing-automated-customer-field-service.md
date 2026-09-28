---
n: 1742
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: "Manufacturing – Automated Customer & Field Service"
url: https://marketplace.uipath.com/listings/manufacturing-automated-customer-and-field-service
accessed: 2026-09-28
verdict: UNCERTAIN
needs_human_ruling: true
question: "Visio-style multi-container flowchart (Dispatcher, Document Understanding Process, Performer; decision diamonds, an 'End' terminator) with ML classification, sentiment analysis and Azure OpenAI per the listing; most labels are illegible in the published image. Does it count as a BPMN diagram?"
needs_visual_check: true
bpmn_evidence: slide 'High level overview of the Solution Accelerator': three containers ('1.a. Dispatcher Process Template - Extract Emails and Files', '2. Document Understanding Process', '3. Performer') with boxes and diamonds; labels mostly too small to read
bpmn_evidence_quote: "the final part of the Solution Accelerator uses AI components distribuited across the data flow"
ai_evidence: legible boxes 'Digitize Document', 'Classify Document', 'UiPath Action Center'; title slide lists 'Ticket priority value suggestion, based on Email Sentiment Analysis' and 'Auto-fill option during ticket configuration (using Azure OpenAI)'
ai_evidence_quote: "the final part of the Solution Accelerator uses AI components distribuited across the data flow to improve the experience of customers and field technicians."
artefacts:
  screenshot: 015_manufacturing-automated-customer-field-service.png
  archive: 015_manufacturing-automated-customer-field-service.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: poor
capture_width_px: 1600
capture_method: python urllib GET of the original marketplace-cdn.uipath.com asset (cdn-cgi resize wrapper stripped); 1600 px is the native size; a 3x LANCZOS crop of the diagram region is saved as 015_manufacturing-automated-customer-field-service_diagram-crop-3x.png (3420 px)
---

## What the page shows

A Solution Accelerator for manufacturing customer and field service (email processing, Salesforce cross-matching, SAP, ServiceNow ticket creation). Its second image shows a tall three-container flowchart on a laptop screen: '1.a. Dispatcher Process Template - Extract Emails and Files', '2. Document Understanding Process' (legible: 'Digitize Document', 'Classify Document', two 'UiPath Action Center' markers), '3. Performer' (ending in an 'End' terminator).

## Observations (description only, no interpretation)

- **AI activity - function:** 'Email Sentiment Analysis' for ticket priority, 'Auto-fill option during ticket configuration (using Azure OpenAI)', Document Understanding extraction (title slide and prose)
- **AI activity - element type:** rectangles inside containers; AI steps not individually legible
- **Authority - downstream:** 'Automated data consolidation from all systems sources + Automated ServiceNow ticket creation' (title slide)
- **Authority - data:** ServiceNow incident ticket; equipment details from SAP Plant Maintenance
- **Authority - control:** decision diamonds (labels illegible)
- **Input provenance:** 'retrieval of emails containing product information, either text or image'
- **Guards present:** two 'UiPath Action Center' markers in the Document Understanding container
- **Prompt / model detail visible:** 'Azure OpenAI' named on the title slide

## Notes for the researcher

Native asset 1600 px with the diagram very small inside a laptop mock-up; the 3x crop does not make most labels legible.
