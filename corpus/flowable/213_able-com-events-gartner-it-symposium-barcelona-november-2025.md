---
n: 1135
source: flowable
source_name: Flowable (enterprise documentation, vendor blog/marketing site, training site)
title: Gartner IT Symposium/Xpo™ 2025 conference in Barcelona, Spain
url: https://www.flowable.com/events/gartner-it-symposium-barcelona-november-2025
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "The conference photograph image_18719280 shows an IT Xpo stage screen running the Flowable Design modeller with a drawn process model whose labels are unreadable at every zoom: does any task inside that model carry an AI/LLM element, and is the notation BPMN 2.0 rather than CMMN?"
needs_visual_check: false
bpmn_evidence: not established from the page text; the page is about process/case modelling: EVENT // NOVEMBER 10– 13, 2025 // Gartner IT Symposium/Xpo™ 2025 conference in Barcelona, Spain
bpmn_evidence_quote: "EVENT // NOVEMBER 10– 13, 2025 // Gartner IT Symposium/Xpo™ 2025 conference in Barcelona, Spain"
ai_evidence: not established: the page is a conference page whose prose contains no AI mention; twelve of its 22 figures are speaker portraits, seven are vendor SVG logos/badges whose text nodes carry campaign taglines rather than diagram content, and the remainder are conference and booth photographs. The one model-bearing photograph, image_18719280, shows the Flowable Design modeller on a stage screen with labels unreadable at every zoom, so no AI/LLM element inside that model can be confirmed or ruled out - see the question. The census line here previously read "the page text discusses AI: EVENT // NOVEMBER 10-13, 2025..." - templated, false, corrected 2026-09-26.
ai_evidence_quote: none - the page contains no AI mention to quote.
artefacts:
  screenshot: 213_able-com-events-gartner-it-symposium-barcelona-november-2025.png
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

- **Figures on the page:** (no alt) | blues-brothers-2.svg; _R7A0156-2-Micha Kiener_web_hs | _R7A0156-2-Micha_Kiener_web_hs.jpg; (no alt) | blues-brothers-1.svg; Sebastian Rojas - Pre-Sales Engineer | Sebastian_Rojas_retoc.jpg
- **OCR labels of the captured figure:** (none legible)
- **Page text quote:** EVENT // NOVEMBER 10– 13, 2025 // Gartner IT Symposium/Xpo™ 2025 conference in Barcelona, Spain
- **Captured asset:** https://images.ctfassets.net/chja9v5uur3u/2zCYIlKIW1hsWWCrIdbg6g/ea746451d4342d19eacdfac949ad5fab/blues-brothers-2.svg (0x0)

## What to check

Whether the captured figure (or another figure on the page) is a BPMN 2.0 process
diagram and whether an AI/LLM element sits inside that process.

## Visual pass observations (sighted, elicitation-aa 2026-09-25)

All 22 figures the page publishes were fetched at native resolution with
`ledgers/flowable.raw/s7_figfetch.py` and looked at. Twelve are speaker portraits
(`Robert_Barlecaj.jpg`, `Roger_Brunner-_MG_7606.jpg`, `Sebastian_Rojas_retoc.jpg`,
`Sofia_Battilana.jpg`, `Stephan_Aina_web.jpg`, `_R7A0156-2-Micha_Kiener_web_hs.jpg`,
`flowable_emruli-agim_portrait_web.jpg`, `flowable_maier-simon_portrait_web-1.jpg`), seven
are vendor SVGs read as text rather than as images (`blues-brothers-1.svg`,
`blues-brothers-2.svg`, `evel-green.svg`, `flow-pistols.svg`, `flow-pistols2-05.svg`,
`moss-documentation.svg`) whose `<text>` nodes are campaign taglines, i.e. logos/badges and
not diagrams, and one is an iStock conference-hall photograph.

Four of the conference photos were examined natively. `image_15949086` is a man at the swag
table; `image_27906633` is the booth with a monitor whose screen is a blue-headed UI carrying
a white text/list panel, with no diagram on it (cropped at native resolution to confirm);
`image_96829430` is the counter and swag area; `image_8286775` is a stage slide of prose
about best-in-class case management.

`image_18719280` (1920x970, "IT Xpo Stage") is the one figure that carries a process artefact:
the stage screen shows the Flowable Design web modeller in a browser with a real drawn model -
a framed canvas, nested labelled rectangles, event circles, a curved sequence flow and a small
diamond. That is BPMN 2.0 structure rather than CMMN 1.1 (no cut-corner stages, no sentry
diamonds straddling a plan-item border, no folder-shaped case plan model). No label in the
model is legible at 4x magnification (the screen is photographed at an oblique distance), so
whether an AI/LLM element sits inside the process could not be resolved. Recorded as UNCERTAIN
with `needs_human_ruling`, not as `E2`, because the AI question is unanswered rather than
answered negatively.
