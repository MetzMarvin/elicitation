---
n: 8
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Retail Returns Management
url: https://marketplace.camunda.com/apps/775482/retail-returns-management
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: Camunda Web Modeler canvas published as a listing asset; no .bpmn downloadable. Read natively: start and end events, exclusive gateways, a large dashed ad-hoc sub-process, and service tasks whose labels are legible at 1500px.
bpmn_evidence_quote: "Close the return ticket"
ai_evidence: Three service tasks are labelled after the AI: 'AI fraud check', 'AI visual inspection' and 'AI in the ticket system', each carrying the same violet four-pointed-star element-template glyph at its top-left corner; the large dashed ad-hoc sub-process carries that glyph too. The page describes 'AI-powered returns management' with 'predictive analytics, computer vision, and intelligent automation'.
ai_evidence_quote: "AI fraud check"
artefacts:
  screenshot: 008_retail-returns-management.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own asset (d3bql97l1ytoxn.cloudfront.net); native read at 1500x574 plus 7x zoom crops of the AI elements
---

## What the page shows

A retail returns process. After the return request is received, the flow quality-checks the order and branches into an 'AI fraud check' service task, then 'AI visual inspection', then 'AI in the ticket system', before the physical path (product pickup, stock check, replacement/refund/refurbish branches) and a closing task that closes the return ticket. A large dashed ad-hoc sub-process holds the downstream logistics and disposition work.

## Observations (description only, no interpretation)

- **AI activity - function:** the element names state the AI's jobs - fraud checking, visual inspection of the returned item, and feeding the ticket system; the page adds 'predictive analytics, computer vision, and intelligent automation'.
- **AI activity - element type:** ordinary `serviceTask`s carrying the AI element-template glyph, and an `adHocSubProcess` carrying the same glyph.
- **Authority - downstream:** the physical-return path (pickup, stock check, replacement/refund handling, 'Close the return ticket').
- **Authority - data:** not visible on the page.
- **Authority - control:** the exclusive gateways after 'Is Eligible?' and around the stock/quality checks.
- **Input provenance:** the returned order (start event 'Return order quality check').
- **Guards present:** none observed on the drawn AI path; the page lists 'Human Task orchestration' among its catalogue facets but the diagram shows no human step between the AI tasks.
- **Prompt / model detail visible:** not visible on the page.

## Notes for the researcher

Listing is 'Listing Only' (Solution Accelerator) by TechMahindra; the page's 'View Screenshots' link points at /apps/775482/screenshots but no further diagram is published. The three AI-named tasks were each confirmed at 7x zoom, since the AI evidence here is an element-template glyph plus the element's own label.
