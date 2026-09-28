---
n: 655
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: "Skew Corrector using Machine Learning"
url: https://marketplace.uipath.com/listings/skew-corrector-using-machine-learning
accessed: 2026-09-28
verdict: UNCERTAIN
needs_human_ruling: true
question: "The listing's only possible diagram artefact is inside an embedded video that was not opened (operator no-media rule). Does the video show a BPMN process with an AI element, or should this listing be excluded?"
needs_visual_check: true
bpmn_evidence: none in the single listing image (logo banner); the only possible artefact is an embedded YouTube video, not opened
bpmn_evidence_quote: "The purpose of this project is to educate the end users on how to use UiPath MLSkill Activity with AI Center to correct the skewness in images."
ai_evidence: listing prose describes an AI/ML step in the automated process
ai_evidence_quote: "The objective of this ML project is to correct the skewness in the image files using UiPath AI Center."
artefacts:
  screenshot: 032_skew-corrector-machine-learning.png
  archive: 032_skew-corrector-machine-learning.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: fullpage-screenshot
capture_quality: legible
capture_width_px: 1500
capture_method: offline headless-Edge render of the archived listing HTML (scripts, styles and video iframes stripped, so no YouTube request); the listing has no image asset to download
---

## What the page shows

An Internal Labs solution using an AI Center ML skill to de-skew document images before OCR. Its only image is a UiPath logo banner (no process artefact); it embeds one YouTube video, not opened.

## Observations (description only, no interpretation)

- **AI activity - function:** ML skill corrects image skew before OCR extraction
- **AI activity - element type:** not visible on the page (no diagram on the page)
- **Authority - downstream:** not visible on the page
- **Authority - data:** not visible on the page
- **Authority - control:** not visible on the page
- **Input provenance:** not visible on the page
- **Guards present:** not visible on the page
- **Prompt / model detail visible:** none

## Notes for the researcher

Artefact inside a video; not opened per operator instruction 2026-09-26. The PNG is an offline render of the archived listing text, not a diagram. The listing type is "Solution"; UiPath listings of this type ship Studio workflows, which are not BPMN, so the video most likely shows UiPath Studio or the vendor tool, but that was not verified.
