---
n: 252
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: "UiPath Digital Claims Chatbot for Life Insurance"
url: https://marketplace.uipath.com/listings/uipath-digital-claims-chatbot-for-life-insurance
accessed: 2026-09-28
verdict: UNCERTAIN
needs_human_ruling: true
question: "The listing's only possible diagram artefact is inside an embedded video that was not opened (operator no-media rule). Does the video show a BPMN process with an AI element, or should this listing be excluded?"
needs_visual_check: true
bpmn_evidence: no listing image; the only possible artefact is an embedded YouTube video, not opened
bpmn_evidence_quote: "Accelerator provides pre-built workflow and services for digitizing the Life Insurance claims submission and status inquiry processing through Chatbots."
ai_evidence: listing prose describes an AI/ML step in the automated process
ai_evidence_quote: "Accelerator provides pre-built workflow and services for digitizing the Life Insurance claims submission and status inquiry processing through Chatbots."
artefacts:
  screenshot: 023_digital-claims-chatbot-life-insurance.png
  archive: 023_digital-claims-chatbot-life-insurance.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: fullpage-screenshot
capture_quality: legible
capture_width_px: 1500
capture_method: offline headless-Edge render of the archived listing HTML (scripts, styles and video iframes stripped, so no YouTube request); the listing has no image asset to download
---

## What the page shows

An Internal Labs solution accelerator for life-insurance claims submission and status inquiry via chatbots (kore.ai integration). The listing has no image; it embeds one YouTube video, not opened.

## Observations (description only, no interpretation)

- **AI activity - function:** chatbot front end for claims submission and status inquiry (kore.ai)
- **AI activity - element type:** not visible on the page (no diagram on the page)
- **Authority - downstream:** not visible on the page
- **Authority - data:** not visible on the page
- **Authority - control:** not visible on the page
- **Input provenance:** not visible on the page
- **Guards present:** not visible on the page
- **Prompt / model detail visible:** none

## Notes for the researcher

Artefact inside a video; not opened per operator instruction 2026-09-26. The PNG is an offline render of the archived listing text, not a diagram. The listing type is "Solution"; UiPath listings of this type ship Studio workflows, which are not BPMN, so the video most likely shows UiPath Studio or the vendor tool, but that was not verified.
