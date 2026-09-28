---
n: 944
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: IN-D Payables
url: https://marketplace.uipath.com/listings/in-d-payables
accessed: 2026-09-28
verdict: UNCERTAIN
needs_human_ruling: true
question: "Informal box-and-arrow process diagram with two colour bands labelled \"IN-D Payables\" and \"UiPath\" (lane-like), no BPMN events or gateway symbols, branching expressed as arrow labels on a confidence score. Does it count as a BPMN diagram?"
needs_visual_check: false
bpmn_evidence: process diagram with two labelled colour bands (lane-like) and rounded task boxes; no start/end events, no gateway shapes; notation is informal, not recognisably BPMN 2.0
bpmn_evidence_quote: "a threshold can be set in the workflow to decide upon whether to accept the extracted data as such or needed to get validated manually"
ai_evidence: box "Invoice Digitization" - "Thanks to Cognitive OCR for template-free and stamp/dirt-proof invoice data capture"; branch labels "IN-D feels less confident about the data capture" / "IN-D feels highly confident about the data capture"
ai_evidence_quote: "IN-D AI engine uses machine learning and computer vision technologies to digitize and extract necessary data from invoices"
artefacts:
  screenshot: 009_in-d-payables.png
  archive: 009_in-d-payables.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: marginal
capture_width_px: 1280
capture_method: python urllib GET of the original marketplace-cdn.uipath.com asset (cdn-cgi wrapper stripped), saved as PNG; 1280 px is the native size, no larger original exists; all box labels legible
---

## What the page shows

A UiPath snippet connecting to the IN-D Payables invoice-extraction engine. The third listing
image is a process diagram in two colour bands: the upper band labelled "IN-D Payables"
contains "Invoice Digitization" and "Validation UI"; the lower band labelled "UiPath" contains
"Invoice Received", "Invoice Sourcing", "Approval Workflow" and "Post-approval steps". The other
two images are UI screenshots captioned "Validate: IN-D automatically extracts data from
invoices" and "Dashboard: Invoice batches are listed here". The page also embeds one YouTube
video (`youtube.com/embed/_vlav2QnfL4`), not opened.

## Observations (description only, no interpretation)

- **AI activity - function:** "Invoice Digitization - Thanks to Cognitive OCR for template-free
  and stamp/dirt-proof invoice data capture"; page prose: "The engine also gives a confidence
  score for each attribute".
- **AI activity - element type:** a rounded box inside the "IN-D Payables" band (no BPMN task
  type visible).
- **Authority - downstream:** arrow labelled "IN-D feels highly confident about the data capture"
  goes to "Approval Workflow" ("Custom workflow to do 2,3,4-way matching and get approvals via
  email or custom dashboards"), then "Post-approval steps" ("All post-approval steps such as
  update CRM, accounting software and to initiate payments").
- **Authority - data:** extracted invoice attributes ("more than 15 general attributes and all
  the table information").
- **Authority - control:** the confidence score decides the path: "IN-D feels less confident
  about the data capture" -> "Validation UI" ("Drag-and-play intuitive UI that notifies for
  validation on low confidence score"); "highly confident" -> "Approval Workflow".
- **Input provenance:** "Invoice Received - Invoice raised by vendors, PO/Non-PO invoice and
  even multi-page invoices"; "Invoice Sourcing - Receive Invoices from vendors via emails or any
  other channels both single invoices or in batches".
- **Guards present:** "Validation UI" on low confidence (human validation); "Approval Workflow"
  after extraction.
- **Prompt / model detail visible:** none; "IN-D AI engine uses machine learning and computer
  vision technologies".

## Notes for the researcher

The diagram is a vendor marketing graphic, not a modeller export; the band labels read like
pools/lanes, but there are no BPMN events or gateway symbols, so the notation call is left to
you. Native asset is 1280 px wide, labels legible. The YouTube embed was not opened (operator
no-media rule 2026-09-26).
