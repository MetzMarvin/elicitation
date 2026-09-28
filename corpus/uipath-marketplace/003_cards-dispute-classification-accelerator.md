---
n: 245
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: "UiPath Cards Dispute Classification for Banks"
url: https://marketplace.uipath.com/listings/cards-dispute-classification-accelerator
accessed: 2026-09-28
verdict: UNCERTAIN
needs_human_ruling: true
question: "The listing's only possible diagram artefact is inside an embedded video that was not opened (operator no-media rule). Does the video show a BPMN process with an AI element, or should this listing be excluded?"
needs_visual_check: true
bpmn_evidence: none on the listing (0 images); only artefact is an embedded YouTube video, not opened
bpmn_evidence_quote: "After the classification of a dispute, the workflow updates the case in the case management tool for further action to be taken."
ai_evidence: listing prose describes an AI/ML step in the automated process
ai_evidence_quote: "The model uses pre-trained Machine Learning models using NLP algorithms."
artefacts:
  screenshot: 003_cards-dispute-classification-accelerator.png
  archive: 003_cards-dispute-classification-accelerator.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: fullpage-screenshot
capture_quality: legible
capture_width_px: 1500
capture_method: offline headless-Edge render of the archived listing HTML (scripts, styles and video iframes stripped, so no YouTube request); the listing has no image asset to download
---

## What the page shows

An accelerator that "automates the classification of card disputes into standard codes"; an ML/NLP model classifies dispute requests, after which "the workflow updates the case in the case management tool". The listing has no screenshots; it embeds one video (`youtube.com/embed/4qvjkHnatAs`).

## Observations (description only, no interpretation)

- **AI activity - function:** "extracting relevant content from the dispute requests and classification of the requests into standard dispute types"
- **AI activity - element type:** not visible on the page (no diagram on the page)
- **Authority - downstream:** "the workflow updates the case in the case management tool for further action to be taken"
- **Authority - data:** the case in the case management tool
- **Authority - control:** "Next course of action on the dispute is taken based on this classification."
- **Input provenance:** "dispute requests are registered by customers through different channels"
- **Guards present:** not visible on the page
- **Prompt / model detail visible:** none

## Notes for the researcher

Artefact inside a video; not opened per operator instruction 2026-09-26. The PNG is an offline
render of the archived listing text, not a diagram. The listing type is "Solution"; UiPath
listings of this type ship Studio workflows, which are not BPMN, so the video most likely shows
UiPath Studio or the vendor tool, but that was not verified.
