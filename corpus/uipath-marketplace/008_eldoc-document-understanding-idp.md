---
n: 890
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: "elDoc Document Understanding (IDP & OCR)"
url: https://marketplace.uipath.com/listings/eldoc-idp-client
accessed: 2026-09-28
verdict: UNCERTAIN
needs_human_ruling: true
question: "elDoc advertises \"BPM functionalities\" and shows a \"Processes library\"; the listing images only show a stage table (eDocRecoBot Recognition -> human Validation -> eDocConverterBot Conversion), no diagram. Is there a BPMN model behind it (possibly in the two unopened videos), and does it count?"
needs_visual_check: true
bpmn_evidence: no diagram in the 8 images (UI only); "Assigned process" stage table and "Processes library" menu entry; vendor prose names "BPM functionalities"; 2 YouTube videos not opened
bpmn_evidence_quote: "shipped with Document Management and BPM functionalities"
ai_evidence: listing prose describes an AI/ML step in the automated process
ai_evidence_quote: "Intelligent data capture and recognition from scanned & digitally generated documents (PDFs, images), shipped with Document Management and BPM functionalities."
artefacts:
  screenshot: 008_eldoc-document-understanding-idp.png
  archive: 008_eldoc-document-understanding-idp.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: marginal
capture_width_px: 1906
capture_method: python urllib GET of the original marketplace-cdn.uipath.com GIF (cdn-cgi wrapper stripped), first frame saved as PNG with PIL; the 'Assigned process' table text is small
---

## What the page shows

The elDoc IDP connector: "UiPath Robot uploads documents to elDoc IDP using REST API", "elDoc IDP performs data extraction & recognition", then the robot downloads structured results "for further data processing (e.g.: cross-validation, posting to SAP or Nav, etc.)". The eight listing images (five stills, three animated GIFs of 84/120/72 frames, sampled at 8 frames each) show the elDoc web UI: "Document: Recognition Document (Archive)" with recognised fields and confidence values, a side menu with "Workflow library" / "Processes library", and an "Assigned process" table with stages 1 "eDocRecoBot" - "Recognition", 2 "David Torres" - "Validation", 3 "eDocConverterBot" - "Conversion", 4 - "Validation". No process diagram is visible. Two YouTube videos are embedded (`youtube.com/embed/hmocKQh9_D8`, `youtube.com/embed/Mla4BsnrlzE`), not opened.

## Observations (description only, no interpretation)

- **AI activity - function:** "data extraction & recognition" by elDoc IDP ("Intelligent OCR, ICR, OMR", "document forms classification"); stage 1 "Recognition" is assigned to "eDocRecoBot"
- **AI activity - element type:** not visible on the page (no diagram on the page)
- **Authority - downstream:** "UiPath Robot downloads strcutured results from elDoc IDP using REST API for further data processing (e.g.: cross-validation, posting to SAP or Nav, etc.)"
- **Authority - data:** recognised document fields (e.g. Amount, Account No, Reference with per-field confidence values shown in the UI)
- **Authority - control:** stage 2 and 4 "Validation" assigned to a named human user after recognition/conversion
- **Input provenance:** "scanned & digitally generated documents (PDFs, images)" uploaded by the UiPath robot
- **Guards present:** human "Validation" stages in the Assigned process table
- **Prompt / model detail visible:** none

## Notes for the researcher

Artefact partly inside two videos; not opened per operator instruction 2026-09-26. The animated GIFs were inspected by sampling 8 frames each. The capture is the first frame of media 0890_5.gif, which shows the Assigned process table; it is a UI screenshot, not a diagram.
