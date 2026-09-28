---
n: 322
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: "Expert System - Cogito NLP for UiPath Platform"
url: https://marketplace.uipath.com/listings/expert-system-cogito-nlp-for-uipath-platform
accessed: 2026-09-28
verdict: UNCERTAIN
needs_human_ruling: true
question: "The listing's only possible diagram artefact is inside an embedded video that was not opened (operator no-media rule). Does the video show a BPMN process with an AI element, or should this listing be excluded?"
needs_visual_check: true
bpmn_evidence: no listing image; the only possible artefact is an embedded YouTube video, not opened
bpmn_evidence_quote: "With this connector you can bring AI into a RPA process."
ai_evidence: listing prose describes an AI/ML step in the automated process
ai_evidence_quote: "With this connector you can bring AI into a RPA process."
artefacts:
  screenshot: 026_expert-system-cogito-nlp.png
  archive: 026_expert-system-cogito-nlp.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: fullpage-screenshot
capture_quality: legible
capture_width_px: 1500
capture_method: offline headless-Edge render of the archived listing HTML (scripts, styles and video iframes stripped, so no YouTube request); the listing has no image asset to download
---

## What the page shows

An expert.ai (Expert System) connector bringing Cogito NLP document understanding and classification into UiPath RPA processes. The listing has no image; it embeds one YouTube video, not opened.

## Observations (description only, no interpretation)

- **AI activity - function:** NLP understanding/extraction and classification of documents ("Classify documents against specific customer taxonomies and behave accordingly")
- **AI activity - element type:** not visible on the page (no diagram on the page)
- **Authority - downstream:** not visible on the page
- **Authority - data:** not visible on the page
- **Authority - control:** not visible on the page
- **Input provenance:** not visible on the page
- **Guards present:** not visible on the page
- **Prompt / model detail visible:** none

## Notes for the researcher

Artefact inside a video; not opened per operator instruction 2026-09-26. The PNG is an offline render of the archived listing text, not a diagram. The listing type is "Connector"; UiPath listings of this type ship Studio workflows, which are not BPMN, so the video most likely shows UiPath Studio or the vendor tool, but that was not verified.
