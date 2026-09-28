---
n: 834
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: "RPABotPro - RPA Bill Processing Bot"
url: https://marketplace.uipath.com/listings/rpa-bill-processing-bot
accessed: 2026-09-28
verdict: UNCERTAIN
needs_human_ruling: true
question: "The listing's only possible diagram artefact is inside an embedded video that was not opened (operator no-media rule). Does the video show a BPMN process with an AI element, or should this listing be excluded?"
needs_visual_check: true
bpmn_evidence: none in the two listing images (award badge, logo); the only possible artefact is an embedded YouTube video, not opened
bpmn_evidence_quote: "Highly configurable workflow automation rules"
ai_evidence: listing prose describes an AI/ML step in the automated process
ai_evidence_quote: "Bill capture is processed with OCR technology to 95%+ character level accuracy"
artefacts:
  screenshot: 007_rpabotpro-bill-processing-bot.png
  archive: 007_rpabotpro-bill-processing-bot.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: fullpage-screenshot
capture_quality: legible
capture_width_px: 1500
capture_method: offline headless-Edge render of the archived listing HTML (scripts, styles and video iframes stripped, so no YouTube request); the listing has no image asset to download
---

## What the page shows

A "Bill Processing Bot" (UiPath solution) with "Automated data capture and data entry", "Approval and exception resolution"; tags include "ai", "Artifical Intelligence", "machine-learning". Its two images are a "2019 Artificial Intelligence Awards" badge and the RpaBotPro logo (no process artefact); it embeds one video (`youtube.com/embed/_Tw_aV9vvTI`).

## Observations (description only, no interpretation)

- **AI activity - function:** "Bill capture is processed with OCR technology"
- **AI activity - element type:** not visible on the page (no diagram on the page)
- **Authority - downstream:** not visible on the page
- **Authority - data:** not visible on the page
- **Authority - control:** "Approval and exception resolution"
- **Input provenance:** "from a scanning device if the invoice is paper-based, or from an electronic file, such as a PDF or email"
- **Guards present:** "All document actions are saved in archived log files, providing audit support"
- **Prompt / model detail visible:** none

## Notes for the researcher

Artefact inside a video; not opened per operator instruction 2026-09-26. The PNG is an offline render of the archived listing text, not a diagram. The listing type is "Solution"; UiPath listings of this type ship Studio workflows, which are not BPMN, so the video most likely shows UiPath Studio or the vendor tool, but that was not verified.
