---
n: 23
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Agentic Logistics Services: Exception-Driven Order-to-Execution
url: https://marketplace.camunda.com/apps/791608/agentic-logistics-services-exception-driven-order-to-execution
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: Camunda Web Modeler canvas published as a listing asset; no .bpmn downloadable. Read natively: start event 'Shipment Request Email Recieved', three ad-hoc sub-processes (each with the tilde marker), end event 'Shipment Fully Processed'.
bpmn_evidence_quote: "Shipment Fully Processed"
ai_evidence: Three ad-hoc sub-processes, each carrying the violet four-pointed-star element-template glyph and each named after an agent: 'Information Agent', 'Shipment Planning Agent', 'Shipment Booking Agent'. Their contents are tool tasks ('Tool: Draft Email', 'Tool: Query Carrier API', 'Tool: Calculate Route Optimization', 'Tool: Present Options to Customer', 'Tool: Transmit EDI 204', 'Tool: Update ERP'), and the page's text frames the listing as 'Agentic Logistics Services' with an 'orchestration layer'.
ai_evidence_quote: "Shipment Planning Agent"
artefacts:
  screenshot: 023_agentic-logistics-services.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own overview asset (also at 1x as the overview image); native read at 1100x438
---

## What the page shows

An exception-driven order-to-execution flow for a logistics provider. A shipment request email starts the process; the 'Information Agent' extracts data (ABBYY IDP) and queries the DOT database; the 'Shipment Planning Agent' queries the carrier API, calculates route optimization, drafts emails and presents options to the customer; the 'Shipment Booking Agent' drafts and sends emails, transmits EDI 204, generates BOL and labels and updates the ERP. The process ends as 'Shipment Fully Processed'.

## Observations (description only, no interpretation)

- **AI activity - function:** each agent's work is expressed as the tools it may call; the page says the solution covers 'order receipt through to execution, exceptions, escalations and resolution' with 'Intelligent Order Intake using ABBYY'.
- **AI activity - element type:** three `adHocSubProcess` elements carrying the AI-agent glyph - the same element type as n=006's job-worker agent - with their tools as ordinary service tasks inside.
- **Authority - downstream:** the tools listed above, including three that write to outside systems ('Tool: Send Email', 'Tool: Transmit EDI 204', 'Tool: Update ERP').
- **Authority - data:** the DOT database (via 'Tool: Query DOT Database'), the carrier API, the ERP.
- **Authority - control:** no gateways are drawn between the three agents; the sequence is linear. The page mentions SLA-driven prioritization and an 'Operations Cockpit'.
- **Input provenance:** the shipment request email, plus documents parsed by ABBYY IDP.
- **Guards present:** none observed in the diagram; the page lists 'Single Orchestration layer for all operational exceptions and audit trail' as an outcome.
- **Prompt / model detail visible:** not visible on the page.

## Notes for the researcher

Vendor-listed as a partner 'Solution Accelerator' and 'Listing Only'; the diagram is the only artefact published. The agent boxes are ad-hoc sub-processes, i.e. this source shows the job-worker AI agent in the same visual form here and in n=006's XML.
