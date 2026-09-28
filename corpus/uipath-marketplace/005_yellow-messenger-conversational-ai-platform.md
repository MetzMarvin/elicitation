---
n: 882
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: "Yellow Messenger Conversational AI Platform"
url: https://marketplace.uipath.com/listings/yellow-messenger-conversational-ai-platform
accessed: 2026-09-28
verdict: UNCERTAIN
needs_human_ruling: true
question: "The listing's only possible diagram artefact is inside an embedded video that was not opened (operator no-media rule). Does the video show a BPMN process with an AI element, or should this listing be excluded?"
needs_visual_check: true
bpmn_evidence: none on the listing (0 images); only artefact is an embedded YouTube video, not opened
bpmn_evidence_quote: "The pre-built integration takes the journey from the virtual assistant/Chatbot to the UiPath Orchestrator and then back to the Chatbot"
ai_evidence: listing prose describes an AI/ML step in the automated process
ai_evidence_quote: "Upload the scanned document to the chatbot, it captures & stores invoice data in the database"
artefacts:
  screenshot: 005_yellow-messenger-conversational-ai-platform.png
  archive: 005_yellow-messenger-conversational-ai-platform.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: fullpage-screenshot
capture_quality: legible
capture_width_px: 1500
capture_method: offline headless-Edge render of the archived listing HTML (scripts, styles and video iframes stripped, so no YouTube request); the listing has no image asset to download
---

## What the page shows

A connector between the Yellow Messenger chatbot and UiPath Orchestrator for invoice approval and sentiment analysis of uploaded reviews. The listing has no screenshots; it embeds one video (`youtube.com/embed/Pwzl6Szqrt4`).

## Observations (description only, no interpretation)

- **AI activity - function:** chatbot "captures & stores invoice data in the database"; "sentiment analysis for multiple reviews or feedback" by "our NLP engine"
- **AI activity - element type:** not visible on the page (no diagram on the page)
- **Authority - downstream:** UiPath Orchestrator ("from the virtual assistant/Chatbot to the UiPath Orchestrator and then back")
- **Authority - data:** invoice data "in the database"
- **Authority - control:** invoice approval
- **Input provenance:** scanned invoice uploaded to the chatbot; CSV of reviews
- **Guards present:** not visible on the page
- **Prompt / model detail visible:** none

## Notes for the researcher

Artefact inside a video; not opened per operator instruction 2026-09-26. The PNG is an offline
render of the archived listing text, not a diagram. The listing type is "Connector"; UiPath
listings of this type ship Studio workflows, which are not BPMN, so the video most likely shows
UiPath Studio or the vendor tool, but that was not verified.
