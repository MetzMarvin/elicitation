---
n: 1586
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: Utility Bills - Generic
url: https://marketplace.uipath.com/listings/utility-bills-generic
accessed: 2026-09-28
verdict: UNCERTAIN
needs_human_ruling: true
question: "Visio-style flowchart (sharp-cornered filled rectangles, labelled decision diamonds with Yes/No arcs, no start/end events, a database icon as sink) showing ML classification/extraction with human-validation gates. Does it count as a BPMN diagram? The same diagram is re-used on 14 further Document Understanding accelerator listings (recorded as E3 duplicates of this record)."
needs_visual_check: false
bpmn_evidence: process diagram slide titled "Utility Bills - Generic Diagram"; rectangles, decision diamonds with Yes/No, no events, no lanes; notation looks like a classic flowchart, not recognisably BPMN 2.0
bpmn_evidence_quote: "Digitize documents, classify them, extracting the document details, and running business rule validation."
ai_evidence: boxes "Document Understanding Process - Classify Document" and "Document Understanding Process - Extract Information"; page prose on the ML model
ai_evidence_quote: "This accelerator is an out-of-the-box ML model for seamless processing, retrieval, and validation of Utility Bills."
artefacts:
  screenshot: 010_utility-bills-generic.png
  archive: 010_utility-bills-generic.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: marginal
capture_width_px: 1200
capture_method: python urllib GET of the original marketplace-cdn.uipath.com asset (cdn-cgi wrapper stripped); 1200 px is native and the diagram occupies a laptop mock-up on the slide, so labels are small; a 3x LANCZOS crop of the diagram region is saved as 010_utility-bills-generic_diagram-crop-3x.png (1560 px) and is legible
---

## What the page shows

A UiPath Document Understanding solution accelerator for utility bills. The second listing
image is a slide "Utility Bills - Generic Diagram" showing a flow: "Dispatcher Process -
Extracts files from specific source" receives from "Shared Folder", "Email", "Other System" ->
"Document Understanding Process - Classify Document" -> diamond "Human Validation Needed"
(Yes -> "Classification Validation - Human review of classification results"; No ->) ->
"Document Understanding Process - Extract Information" -> diamond "Human Validation Needed"
(Yes -> "Extraction Validation - Human review of extraction results"; No ->) -> diamond "Data
Entry Via Application" -> Yes -> "Custom Application". A red annotation "Action Center
Components" points at the two green validation boxes. The other images are a title slide
("1. Retrieve documents from a Data Source ... 2. Digitize documents, classify them, extracting
the document details, and running business rule validation. 3. (Optionally) process the
document using the extracted fields."), sample bills, and a deployment-guide cover.

## Observations (description only, no interpretation)

- **AI activity - function:** "Classify Document" and "Extract Information" by the "Document
  Understanding Process"; prose: "The Document Understanding (DU) model is trained to extract
  crucial data from this type of document. This model can extract up to 22 distinct fields".
- **AI activity - element type:** rectangles in the flowchart labelled "Document
  Understanding Process".
- **Authority - downstream:** "Data Entry Via Application" -> "Custom Application".
- **Authority - data:** extracted fields ("Billing Name, Billing Address, Vendor Name ...
  Meter Usage, Meter ID").
- **Authority - control:** diamonds "Human Validation Needed" route classification and
  extraction results either to human validation or straight on; diamond "Data Entry Via
  Application".
- **Input provenance:** "Dispatcher Process - Extracts files from specific source" via "Shared
  Folder", "Email", "Other System"; prose: "Retrieve documents from a Data Source (like an email
  inbox, a network drive, or a third-party application)".
- **Guards present:** "Classification Validation - Human review of classification results" and
  "Extraction Validation - Human review of extraction results" (annotated "Action Center
  Components"); prose "running business rule validation".
- **Prompt / model detail visible:** none; "Specialized AI models tailored to particular
  document types"; dependency "UiPath.DocumentUnderstanding.ML.Activities: [1.17.0]".

## Notes for the researcher

This exact diagram (pixel-identical diagram region, or the same diagram re-placed inside the
laptop mock-up) appears on 14 more Document Understanding accelerator listings from UiPath:
n = 1588, 1589, 1591, 1592, 1593, 1594, 1596, 1598, 1601, 1603, 1604, 1605, 1607, 1608. They are
ledger rows `E3-duplicate` with `duplicate_of` this record. If you rule this diagram in, those
listings are 14 further publications of the same artefact.
