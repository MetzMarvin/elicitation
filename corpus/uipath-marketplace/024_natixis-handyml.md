---
n: 290
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: "Natixis - HandyML"
url: https://marketplace.uipath.com/listings/pua-virtual-handyml
accessed: 2026-09-28
verdict: UNCERTAIN
needs_human_ruling: true
question: "The listing's only possible diagram artefact is inside an embedded video that was not opened (operator no-media rule). Does the video show a BPMN process with an AI element, or should this listing be excluded?"
needs_visual_check: true
bpmn_evidence: none in the single listing image (title card); the only possible artefact is an embedded YouTube video, not opened
bpmn_evidence_quote: "Take data from an Excel file and train a supervised Machine Learning model."
ai_evidence: listing prose describes an AI/ML step in the automated process
ai_evidence_quote: "Non-datascientists users can now train machine learning models by simply asking their robot to do it for them."
artefacts:
  screenshot: 024_natixis-handyml.png
  archive: 024_natixis-handyml.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: fullpage-screenshot
capture_quality: legible
capture_width_px: 1500
capture_method: offline headless-Edge render of the archived listing HTML (scripts, styles and video iframes stripped, so no YouTube request); the listing has no image asset to download
---

## What the page shows

A Natixis solution in which a robot trains supervised ML models (regression/classification) from Excel data. Its only image is a 'HandyML' title card (no process artefact); it embeds one YouTube video, not opened.

## Observations (description only, no interpretation)

- **AI activity - function:** robot trains and applies supervised ML models ("train a supervised Machine Learning model")
- **AI activity - element type:** not visible on the page (no diagram on the page)
- **Authority - downstream:** not visible on the page
- **Authority - data:** not visible on the page
- **Authority - control:** not visible on the page
- **Input provenance:** not visible on the page
- **Guards present:** not visible on the page
- **Prompt / model detail visible:** none

## Notes for the researcher

Artefact inside a video; not opened per operator instruction 2026-09-26. The PNG is an offline render of the archived listing text, not a diagram. The listing type is "Solution"; UiPath listings of this type ship Studio workflows, which are not BPMN, so the video most likely shows UiPath Studio or the vendor tool, but that was not verified.
