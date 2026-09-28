---
n: 897
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: "IntelliDockers - URL Web Scrapper"
url: https://marketplace.uipath.com/listings/intellidockers-url-web-scrapper
accessed: 2026-09-28
verdict: UNCERTAIN
needs_human_ruling: true
question: "The listing's only possible diagram artefact is inside an embedded video that was not opened (operator no-media rule). Does the video show a BPMN process with an AI element, or should this listing be excluded?"
needs_visual_check: true
bpmn_evidence: none on the listing (0 images); only artefact is an embedded YouTube video, not opened
bpmn_evidence_quote: "Extracts just the relevant text out of a given online news or blog article."
ai_evidence: listing prose describes an AI/ML step in the automated process
ai_evidence_quote: "The engine's processing technology is based on Deep Learning and Neural Networks AI."
artefacts:
  screenshot: 006_intellidockers-url-web-scrapper.png
  archive: 006_intellidockers-url-web-scrapper.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: fullpage-screenshot
capture_quality: legible
capture_width_px: 1500
capture_method: offline headless-Edge render of the archived listing HTML (scripts, styles and video iframes stripped, so no YouTube request); the listing has no image asset to download
---

## What the page shows

A custom activity that sends an article URL to an IntelliDockers engine and returns the article text as JSON. The listing has no screenshots; it embeds one video (`youtube.com/embed/3q1vD7wokDo`).

## Observations (description only, no interpretation)

- **AI activity - function:** "extract only the relevant text of a given article, leaving behind the ads, comments"
- **AI activity - element type:** not visible on the page (no diagram on the page)
- **Authority - downstream:** not visible on the page
- **Authority - data:** "(Output) JsonResult : This is the result string as JSON."
- **Authority - control:** not visible on the page
- **Input provenance:** "(Input) ArticleURL : The URL address of the article" (fetched online page)
- **Guards present:** not visible on the page
- **Prompt / model detail visible:** none

## Notes for the researcher

Artefact inside a video; not opened per operator instruction 2026-09-26. The PNG is an offline
render of the archived listing text, not a diagram. The listing type is "Activity"; UiPath
listings of this type ship Studio workflows, which are not BPMN, so the video most likely shows
UiPath Studio or the vendor tool, but that was not verified.
