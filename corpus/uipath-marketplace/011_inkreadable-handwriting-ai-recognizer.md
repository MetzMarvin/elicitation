---
n: 1720
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: "InkReadable - Handwriting AI Recognizer"
url: https://marketplace.uipath.com/listings/inkreadable-handwriting-ai-recognizer
accessed: 2026-09-28
verdict: UNCERTAIN
needs_human_ruling: true
question: "The listing's only possible diagram artefact is inside an embedded video that was not opened (operator no-media rule). Does the video show a BPMN process with an AI element, or should this listing be excluded?"
needs_visual_check: true
bpmn_evidence: none in the single listing image (publisher logo); the only possible artefact is an embedded YouTube video, not opened
bpmn_evidence_quote: "AI based Handwriting Recognition software."
ai_evidence: listing prose describes an AI/ML step in the automated process
ai_evidence_quote: "AI based Handwriting Recognition software."
artefacts:
  screenshot: 011_inkreadable-handwriting-ai-recognizer.png
  archive: 011_inkreadable-handwriting-ai-recognizer.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: fullpage-screenshot
capture_quality: legible
capture_width_px: 1500
capture_method: offline headless-Edge render of the archived listing HTML (scripts, styles and video iframes stripped, so no YouTube request); the listing has no image asset to download
---

## What the page shows

A partner solution for AI handwriting recognition by Natural Intelligent Technologies srl. Its only image is the publisher logo (no process artefact); it embeds one YouTube video, not opened.

## Observations (description only, no interpretation)

- **AI activity - function:** "AI based Handwriting Recognition"
- **AI activity - element type:** not visible on the page (no diagram on the page)
- **Authority - downstream:** not visible on the page
- **Authority - data:** not visible on the page
- **Authority - control:** not visible on the page
- **Input provenance:** not visible on the page
- **Guards present:** not visible on the page
- **Prompt / model detail visible:** none

## Notes for the researcher

Artefact inside a video; not opened per operator instruction 2026-09-26. The PNG is an offline render of the archived listing text, not a diagram. The listing type is "Partner Solution"; UiPath listings of this type ship Studio workflows, which are not BPMN, so the video most likely shows UiPath Studio or the vendor tool, but that was not verified.
