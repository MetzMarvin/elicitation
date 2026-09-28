---
n: 279
source: loyjoy
source_name: LoyJoy (marketing site, blog)
source_type: vendor marketing page
title: Unser neues Release macht BPMN-Prozessautomatisierung zum Vergnügen
url: https://www.loyjoy.com/de/blog/new-release-makes-bpmn-process-automation-fun/
accessed: 2026-09-24
verdict: UNCERTAIN
needs_visual_check: true
needs_human_ruling: false
bpmn_evidence: "the page embeds a YouTube video whose poster frame is a screenshot of the LoyJoy process editor: the 'Modules' palette on the left (control-flow diamonds, event and essential tiles) and a canvas with the editor's rounded module boxes, exclusive gateways, a 'Drop module' placeholder and a '#1 ...' label; the editor's left navigation is also visible (Experiences, NLU, Push, Live). The poster is published at 600 x 600 px and the video frame is blurred behind the play button, so the palette entries and the module labels cannot be read"
bpmn_evidence_quote: "Modelliere und pflege komplexere Geschäftsprozesse mit Gateways."
ai_evidence: "unresolved: the poster cannot be read at 600 x 600 px, so I cannot tell whether a GPT/AI module appears in the palette or in the drawn process. The page prose is about the release's BPMN features (gateways, process automation) and carries no AI element that I could tie to the figure"
ai_evidence_quote: "Unsere Top 5 Highlights auf einen Blick"
artefacts:
  screenshot: corpus/loyjoy/010_blog-video-poster-unreadable.png
  archive: ledgers/loyjoy.marketing/102.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: poor
capture_width_px: 600
capture_method: curl of the page's YouTube poster asset https://www.loyjoy.com/_astro/WYnxC36CFkFmE1TJRQC1RfnF6rI.CdSK3yVi_1d0HL.webp (600 x 600 native), converted to PNG with PIL. The video itself (YouTube embed) was not opened - the poster is the only published still. Page HTML archived to ledgers/loyjoy.marketing/102.html
---

## What the page shows

The German blog post for the 2022 release. Its only figure-bearing element is an embedded YouTube
video whose **poster frame is an editor screenshot**: "Modules" palette on the left, canvas on the
right with rounded module boxes, X-diamond gateways, a "#1 ..." label and a "Drop module"
placeholder, and the editor's left navigation (Experiences, NLU, Push, Live).

**Why UNCERTAIN / needs_visual_check.** At 600 x 600 px, blurred behind the play button, neither
the palette entries nor the module labels can be read. Rule 5 forbids excluding an unresolved image
and rule 3 forbids E2 on an ambiguous AI question, so the row is recorded for a human look (the
original video would settle it).

## Observations (description only, no interpretation)

- **AI activity - function:** unknown (unresolved).
- **AI activity - element type:** unknown; the visible structure is a process canvas in the editor's
  notation plus the module palette.
- **Authority - downstream / data / control:** not readable.
- **Input provenance:** not readable.
- **Guards present:** not readable.
- **Prompt / model detail visible:** none visible.

## Notes for the researcher

- The English twin `/en/blog/new-release-makes-bpmn-process-automation-fun/` embeds the **same poster
  file** (identical content hash) and is recorded as `E3-duplicate`.
- Everything I could resolve is in the capture; the video's later frames are the only way to read the
  palette, and opening a YouTube embed was outside this read-only pass.
