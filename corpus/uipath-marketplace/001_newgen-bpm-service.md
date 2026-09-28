---
n: 73
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: Newgen - BPM service
url: https://marketplace.uipath.com/listings/newgen-bpm-service
accessed: 2026-09-28
verdict: UNCERTAIN
needs_human_ruling: false
question: null
needs_visual_check: true
bpmn_evidence: none in the three listing images (UiPath Studio Sequence + Manage Packages dialogs); the listing describes iBPS "process workflow" and embeds one YouTube video that was not opened
bpmn_evidence_quote: "These activities are the part of the process workflow defined in iBPS."
ai_evidence: only the tag "intelligent-bpm" and the phrase "routing the work items between manual and automated activity intelligently"; no AI element visible in the images
ai_evidence_quote: "switching and routing the work items between manual and automated activity intelligently"
artefacts:
  screenshot: 001_newgen-bpm-service.png
  archive: 001_newgen-bpm-service.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: marginal
capture_width_px: 1280
capture_method: python urllib GET of the original marketplace-cdn.uipath.com asset (cdn-cgi resize wrapper stripped); 1280 px is the native size, no larger original exists
---

## What the page shows

A UiPath activity pack by Newgen that lets UiPath robots call Newgen iBPS workflow activities
("Newgen.iBPS.Activities enable UiPath to “talk” to Newgen applications"). The three listing
images show UiPath Studio: a Manage Packages dialog listing `Newgen.iBPS.Activities`, and a
UiPath Sequence "Main" with "Get Asset", "Get Asset", "Get iBPS Configuration", "Connect",
"Assign Files = new DirectoryInfo(...)". The page also embeds one YouTube video
(`youtube.com/embed/ut9XdmAEsX8`).

## Observations (description only, no interpretation)

- **AI activity - function:** not visible on the page. The only AI-adjacent wording is the
  tag "intelligent-bpm" and "routing the work items between manual and automated activity
  intelligently".
- **AI activity - element type:** not visible on the page.
- **Authority - downstream:** "invoke the iBPS workflow activities in UiPath studio" (Create
  WorkItem, Complete WorkItem, Add Document, Get Document, per the package description in the
  Manage Packages dialog).
- **Authority - data:** iBPS work items and documents (package description in the image).
- **Authority - control:** "load distribution between bot and human along with, exception
  handling (Technical and Functional)".
- **Input provenance:** not visible on the page.
- **Guards present:** not visible on the page.
- **Prompt / model detail visible:** none.

## Notes for the researcher

Artefact inside a video; not opened per operator instruction 2026-09-26. Newgen iBPS is a BPM
suite, so the video may show an iBPS process model; the images do not. First judged as E1
(UiPath Sequence notation) in the same session, then flipped to UNCERTAIN because the unopened
video is the only place a BPMN artefact could sit (superseding ledger row).
