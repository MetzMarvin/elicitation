---
n: 1741
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: "Know Your Customer"
url: https://marketplace.uipath.com/listings/know-your-customer
accessed: 2026-09-28
verdict: UNCERTAIN
needs_human_ruling: true
question: "Visio-style multi-container flowchart (containers '1.a. Dispatcher Process Template', '2. Document Understanding Process', decision diamonds, no BPMN events visible) with ML classification and Action Center validation; most labels are illegible in the published image. Does it count as a BPMN diagram, and does it need a manual re-read from the deployment guide?"
needs_visual_check: true
bpmn_evidence: slide 'High level overview of the automated framework': containers with process boxes and decision diamonds; labels mostly too small to read
bpmn_evidence_quote: "Digitize KYC Documents, classify, extract document details, running business rule validations."
ai_evidence: legible boxes 'Digitize File', 'Classify Documents', diamond 'Classification Validation Required?'; prose on pre-trained ML package models
ai_evidence_quote: "This process uses Out-of-the-box Pre-trained ML Package Models for Passports, ID Cards, Utility Bills, Bank Statements, and 4056T Forms"
artefacts:
  screenshot: 014_know-your-customer-accelerator.png
  archive: 014_know-your-customer-accelerator.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: poor
capture_width_px: 1200
capture_method: python urllib GET of the original marketplace-cdn.uipath.com asset (cdn-cgi resize wrapper stripped); 1200 px is the native size; a 3x LANCZOS crop of the diagram region is saved as 014_know-your-customer-accelerator_diagram-crop-3x.png (3270 px)
---

## What the page shows

A KYC Solution Accelerator. Its third image, 'High level overview of the automated framework', shows a flowchart on a laptop screen; legible labels include '1.a. Dispatcher Process Template - Extract Email Attachments', 'Inbox', '2. Document Understanding Process', 'Retrieve File from Storage Bucket', 'Digitize File', 'Classify Documents', 'Classification Validation Required?', 'UiPath Action Center'. The rest is too small to read.

## Observations (description only, no interpretation)

- **AI activity - function:** classification and extraction with 'Out-of-the-box Pre-trained ML Package Models'
- **AI activity - element type:** rectangles inside the '2. Document Understanding Process' container
- **Authority - downstream:** not visible on the page
- **Authority - data:** not visible on the page
- **Authority - control:** diamond 'Classification Validation Required?'
- **Input provenance:** 'Retrieving KYC Documents from a Data Source (like an email inbox, a network drive, or a third-party application)'
- **Guards present:** UiPath Action Center validation (icon and label visible)
- **Prompt / model detail visible:** none

## Notes for the researcher

Native asset only 1200 px wide with the diagram inside a laptop mock-up; even the 3x crop leaves most labels illegible. The full diagram is presumably in the accelerator's deployment guide, which is not on the listing page.
