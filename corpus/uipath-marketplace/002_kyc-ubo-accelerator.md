---
n: 242
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: "UiPath KYC (Ultimate Beneficial Owner) Accelerator"
url: https://marketplace.uipath.com/listings/uipath-kyc-ultimate-beneficial-owner-accelerator
accessed: 2026-09-28
verdict: UNCERTAIN
needs_human_ruling: true
question: "The listing's only possible diagram artefact is inside an embedded video that was not opened (operator no-media rule). Does the video show a BPMN process with an AI element, or should this listing be excluded?"
needs_visual_check: true
bpmn_evidence: none on the listing (0 images); only artefact is an embedded YouTube video, not opened
bpmn_evidence_quote: "This process is an integral part of the Anti-Money Laundering or similar regulatory Risk Assessment"
ai_evidence: listing prose describes an AI/ML step in the automated process
ai_evidence_quote: "Pre trained extraction models based on real world public data set such as proxy statements"
artefacts:
  screenshot: 002_kyc-ubo-accelerator.png
  archive: 002_kyc-ubo-accelerator.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: fullpage-screenshot
capture_quality: legible
capture_width_px: 1500
capture_method: offline headless-Edge render of the archived listing HTML (scripts, styles and video iframes stripped, so no YouTube request); the listing has no image asset to download
---

## What the page shows

An accelerator that "extracts ultimate beneficial owners from SEC Def 14A (Proxy documents), runs these list of owners through sanctions screening and politically exposed person (PEP) checks." Dependency listed: "Evolution.AI". The listing has no screenshots; it embeds one video (`youtube.com/embed/j4aqBw79B_Q`).

## Observations (description only, no interpretation)

- **AI activity - function:** "Pre trained extraction models based on real world public data set such as proxy statements" extract beneficial owners
- **AI activity - element type:** not visible on the page (no diagram on the page)
- **Authority - downstream:** "runs these list of owners through sanctions screening and politically exposed person (PEP) checks"
- **Authority - data:** "the KYC record" / client profile
- **Authority - control:** not visible on the page
- **Input provenance:** SEC Def 14A proxy documents
- **Guards present:** not visible on the page
- **Prompt / model detail visible:** none

## Notes for the researcher

Artefact inside a video; not opened per operator instruction 2026-09-26. The PNG is an offline
render of the archived listing text, not a diagram. The listing type is "Solution"; UiPath
listings of this type ship Studio workflows, which are not BPMN, so the video most likely shows
UiPath Studio or the vendor tool, but that was not verified.
