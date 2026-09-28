---
n: 2
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Accounts Payable Invoice Processing
url: https://marketplace.camunda.com/apps/461194/accounts-payable-invoice-processing
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: The listing publishes no diagram and its only artefact is the 'Watch Demo' video (https://www.youtube.com/watch?v=leNII7Utgn0), which I did not open per the operator instruction of 2026-09-26. Does the video show a BPMN diagram, and if so should it be collected from the video rather than marked no-artefact?
needs_visual_check: true
bpmn_evidence: No BPMN artefact on the page, and none downloadable. The listing publishes one image only (a 230x194 app thumbnail, captured) and no screenshots; its process content is entirely a demo video, which I did not open.
bpmn_evidence_quote: "Watch Demo"
ai_evidence: The AI claim is prose, not a process element: the details line 'AI-driven invoice processing', the overview's 'This solution uses AI models for high accuracy and maximum straight-through (also known as no-touch) processing of invoices', and the feature 'The solution automates process steps using generative AI'. None of this is a process artefact and no diagram is published to show where such an element would sit.
ai_evidence_quote: "The solution automates process steps using generative AI"
artefacts:
  screenshot: 002_accounts-payable-invoice-processing.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 230
capture_method: curl of the listing's own image resource (d3bql97l1ytoxn.cloudfront.net, thumbs_112/img6180175011740821898-2x.png, 230x194) - the listing's only published image; native read in full
---

## What the page shows

A Cognizant accounts-payable solution listing ('Listing Only', Solution Accelerator). The page describes an AP invoice process - receiving, recording and routing invoices, executing payments - orchestrated on Camunda, with OCR data extraction, generative-AI process steps, rule-based fraud detection, an exception-management process, SAP/ERP integration and approvals. Nothing of that process is published as a diagram: the page's only media are one app thumbnail and the 'Watch Demo' video.

## Observations (description only, no interpretation)

- **AI activity - function:** stated in prose only ('AI models', 'generative AI', 'semantic search based on generative AI').
- **AI activity - element type:** not visible - no process is published.
- **Authority - downstream / data / control:** not visible.
- **Input provenance:** named as invoices arriving from purchasing/AP systems; no artefact shows it.
- **Guards present:** the page names 'built-in exception management', 'dynamic, multi-level approvals for exceptions' and 'end-to-end audit trail'; none is shown in a model.
- **Prompt / model detail visible:** none.

## Notes for the researcher

Superseded the earlier E0-no-artefact row for this listing after the operator's video instruction: with the video excluded from inspection I cannot assert that the listing holds no artefact. Capture is the app thumbnail the listing publishes; the substantive artefact, if any, is inside https://www.youtube.com/watch?v=leNII7Utgn0.
