---
n: 1136
source: flowable
source_name: Flowable (enterprise documentation, vendor blog/marketing site, training site)
title: Gartner IT Symposium/Xpo™ 2025 conference in Orlando, Florida
url: https://www.flowable.com/events/gartner-it-symposium-orlando-october-2025
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "The booth photograph image_61335740 shows a demo monitor at the Flowable booth whose screen is almost entirely occluded by a visitor's head; the visible sliver is a pale UI panel with a green element and a list-like side bar: was that monitor showing a BPMN process model with an AI/LLM element inside it, and can the occluded content be resolved by any means?"
needs_visual_check: false
bpmn_evidence: not established from the page text; the page is about process/case modelling: EVENT // OCTOBER 20– 23, 2025 // Gartner IT Symposium/Xpo™ 2025 conference in Orlando, Florida
bpmn_evidence_quote: "EVENT // OCTOBER 20– 23, 2025 // Gartner IT Symposium/Xpo™ 2025 conference in Orlando, Florida"
ai_evidence: not established: the page is a conference page whose prose contains no AI mention; ten of its 21 figures are speaker portraits, seven are vendor SVG logos/badges, one is an iStock photograph of an ocean sunset, and the rest are booth photographs. The one monitor photograph, image_61335740, is almost entirely occluded by a visitor's head, so whether it showed a BPMN process model with an AI/LLM element cannot be resolved from the published image - see the question. The census line here previously read "the page text discusses AI: EVENT // OCTOBER 20-23, 2025..." - templated, false, corrected 2026-09-26.
ai_evidence_quote: none - the page contains no AI mention to quote.
artefacts:
  screenshot: 214_lowable-com-events-gartner-it-symposium-orlando-october-2025.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: poor
capture_width_px: 0
capture_method: urllib download of https://images.ctfassets.net/chja9v5uur3u/2zCYIlKIW1hsWWCrIdbg6g/ea746451d4342d19eacdfac949ad5fab/blues-brothers-2.svg (asset published by the page); labels inside read with RapidOCR, this session cannot receive image content
---

## Why this row is UNCERTAIN

The page publishes figures and mentions AI, but the figure that would decide the
verdict could not be certified from the evidence this session can read (the DOM, the
page text, and OCR labels). Per CLAUDE.md section 5 an unresolved figure is UNCERTAIN
with needs_visual_check, never an exclusion.

## Observations (description only, no interpretation)

- **Figures on the page:** (no alt) | blues-brothers-2.svg; _R7A0156-2-Micha Kiener_web_hs | _R7A0156-2-Micha_Kiener_web_hs.jpg; (no alt) | blues-brothers-1.svg; (no alt) | evel-green.svg
- **OCR labels of the captured figure:** (none legible)
- **Page text quote:** EVENT // OCTOBER 20– 23, 2025 // Gartner IT Symposium/Xpo™ 2025 conference in Orlando, Florida
- **Captured asset:** https://images.ctfassets.net/chja9v5uur3u/2zCYIlKIW1hsWWCrIdbg6g/ea746451d4342d19eacdfac949ad5fab/blues-brothers-2.svg (0x0)

## What to check

Whether the captured figure (or another figure on the page) is a BPMN 2.0 process
diagram and whether an AI/LLM element sits inside that process.

## Visual pass observations (sighted, elicitation-aa 2026-09-25)

All 21 figures the page publishes were fetched at native resolution with
`ledgers/flowable.raw/s7_figfetch.py` and looked at. Ten are speaker portraits, seven are
vendor SVGs whose `<text>` nodes carry campaign taglines rather than diagram content
(`blues-brothers-1.svg`, `blues-brothers-2.svg`, `darwin.svg`, `evel-green.svg`,
`flow-pistols2-05.svg`, `flowy-happy.svg`, `moss.svg` - logos/badges, not artefacts), and one
is an iStock stock photograph of an ocean sunset.

Five conference photographs were examined natively. `image_62387093` is the empty booth
panorama whose monitor carries only the decorative pink "FIND YOUR FLOW" swirl (cropped at
native resolution to confirm - no diagram). `image_14481283` is the booth group photograph
whose visible screen is a blue slide with a large percentage figure. `image_88320462` is the
breakout-session room showing a text slide, "FUTURE DIRECTIONS / Come and talk to us at booth
626". `image_81691251` is a group photograph with a monitor reduced to a blue sliver behind a
head. `image_61335740` shows two people at the demo counter; the monitor they face is
occluded by a head and the surviving sliver is a pale UI panel with a green element and a
list-like side bar, unreadable at 6x magnification.

No figure therefore presents a legible process model. The verdict is UNCERTAIN rather than
E0/E2 because one demo monitor could have been the Design modeller and its content is cut off
by occlusion rather than demonstrably absent.
