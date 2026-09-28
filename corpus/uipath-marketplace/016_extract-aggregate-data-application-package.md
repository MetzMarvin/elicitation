---
n: 1757
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: "Extract & Aggregate Data from Application Package"
url: https://marketplace.uipath.com/listings/extract-and-aggregate-data-from-application-package
accessed: 2026-09-28
verdict: UNCERTAIN
needs_human_ruling: true
question: "Visio-style flowchart (sharp rectangles, labelled decision diamonds, no BPMN events) with Document Understanding classify/extract steps and human-validation gates. Does it count as a BPMN diagram? (Variant of the diagram in record 010, with a 'Performer Process' step.)"
needs_visual_check: false
bpmn_evidence: slide 'High level solution design': rectangles, 'Human Validation Needed' diamonds with Yes/No, no events or lanes; flowchart-style notation
bpmn_evidence_quote: "it digitizes, classifies, aggregates and extracts document details, and allows for business rule validation processes."
ai_evidence: boxes 'Document Understanding Process - Classify Document' and '... Extract Information'; prose on pre-trained ML package models and Forms AI
ai_evidence_quote: "extracts data from application forms for processing using Out-of-the-box Pre-trained ML Package Models for ACORD125 and ACORD126 forms"
artefacts:
  screenshot: 016_extract-aggregate-data-application-package.png
  archive: 016_extract-aggregate-data-application-package.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: marginal
capture_width_px: 1600
capture_method: python urllib GET of the original marketplace-cdn.uipath.com asset (cdn-cgi resize wrapper stripped); 1600 px is the native size; a 3x LANCZOS crop of the diagram region is saved as 016_extract-aggregate-data-application-package_diagram-crop-3x.png (3420 px)
---

## What the page shows

A Solution Accelerator for quote application processing (ACORD forms). Its second image, 'High level solution design': 'Dispatcher Process - Extracts Files From Specific Source - Upload As One Combined Document' (Shared Folder / Email / Other System) -> 'Document Understanding Process - Classify Document' -> diamond 'Human Validation Needed' (Yes -> 'Classification Validation - Human review of classification results') -> 'Document Understanding Process - Extract Information' -> diamond 'Human Validation Needed' (Yes -> 'Extraction Validation - Human review of extraction results') -> 'Performer Process - Validate Document Contents Against Other Documents / Applications' -> Yes -> 'Custom Application'; annotation 'Action Center Components'.

## Observations (description only, no interpretation)

- **AI activity - function:** 'Classify Document', 'Extract Information' (ML package models, Forms AI)
- **AI activity - element type:** rectangles labelled 'Document Understanding Process'
- **Authority - downstream:** 'Performer Process - Validate Document Contents Against Other Documents / Applications' -> 'Custom Application'
- **Authority - data:** extracted ACORD form fields
- **Authority - control:** diamonds 'Human Validation Needed'
- **Input provenance:** 'Extracts Files From Specific Source' via Shared Folder, Email, Other System
- **Guards present:** 'Classification Validation' and 'Extraction Validation' (human review, Action Center)
- **Prompt / model detail visible:** none

## Notes for the researcher

Same family as record 010 (n=1586) but a different diagram (Performer Process, combined-document upload), so recorded separately. Native asset 1600 px; the 3x crop is legible.
