---
n: 865
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: "Different Format Invoice Data Extraction"
url: https://marketplace.uipath.com/listings/different-format-invoice-data-extraction
accessed: 2026-09-28
verdict: UNCERTAIN
needs_human_ruling: true
question: "The listing's only possible diagram artefact is inside an embedded video that was not opened (operator no-media rule). Does the video show a BPMN process with an AI element, or should this listing be excluded?"
needs_visual_check: true
bpmn_evidence: none on the listing (0 images); only artefact is an embedded YouTube video, not opened
bpmn_evidence_quote: "This is a complete solution workflow in which you can input your documents"
ai_evidence: listing prose describes an AI/ML step in the automated process
ai_evidence_quote: "Classify Document Scope Data Extraction Scope Present Validation Station"
artefacts:
  screenshot: 004_different-format-invoice-data-extraction.png
  archive: 004_different-format-invoice-data-extraction.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: fullpage-screenshot
capture_quality: legible
capture_width_px: 1500
capture_method: offline headless-Edge render of the archived listing HTML (scripts, styles and video iframes stripped, so no YouTube request); the listing has no image asset to download
---

## What the page shows

A Document Understanding workflow; the page lists its steps: "Get Files", "Load Taxonomy", "Digitize Document", "Classify Document Scope", "Data Extraction Scope", "Present Validation Station", "Export Extraction Results". The listing has no screenshots; it embeds one video (`youtube.com/embed/H8y65QbsMRw`).

## Observations (description only, no interpretation)

- **AI activity - function:** "Classify Document Scope" and "Data Extraction Scope" (dependencies UiPath.DocumentUnderstanding.ML.Activities, UiPath.IntelligentOCR.Activities)
- **AI activity - element type:** not visible on the page (no diagram on the page)
- **Authority - downstream:** "Export Extraction Results"
- **Authority - data:** not visible on the page
- **Authority - control:** "Present Validation Station" follows extraction
- **Input provenance:** input documents of different formats
- **Guards present:** "Present Validation Station" (named as a step; its behaviour is not described)
- **Prompt / model detail visible:** none

## Notes for the researcher

Artefact inside a video; not opened per operator instruction 2026-09-26. The PNG is an offline
render of the archived listing text, not a diagram. The listing type is "Solution"; UiPath
listings of this type ship Studio workflows, which are not BPMN, so the video most likely shows
UiPath Studio or the vendor tool, but that was not verified.
