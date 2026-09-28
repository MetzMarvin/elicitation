---
n: 1098
source: flowable
source_name: Flowable (enterprise documentation, vendor blog/marketing site, training site)
title: Finovate Fall 2026 I Flowable
url: https://www.flowable.com/events/finovate-fall-2026
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "The booth photograph image_17523769 shows a monitor running Flowable Design with a BPMN 2.0 process model whose labels are unreadable at every zoom: does any task inside that process carry an AI/LLM element, and is the notation BPMN rather than CMMN?"
needs_visual_check: false
bpmn_evidence: not established from the page text; the page is about process/case modelling: EVENT // SEPTEMBER 9 - 11, 2026 // FinovateFall 2026
bpmn_evidence_quote: "EVENT // SEPTEMBER 9 - 11, 2026 // FinovateFall 2026"
ai_evidence: not established: the page is a conference page whose prose contains no AI mention; eight of its nine figures are speaker portraits, an abstract orange ribbon, conference-room and booth photographs and a swag bag. The ninth, image_17523769, is a photograph of a monitor running the Flowable Design modeller with a BPMN 2.0 model on it, but its labels are unreadable at every zoom level, so no AI/LLM element inside that process can be confirmed or ruled out - see the question. The census line here previously read "the page text discusses AI: EVENT // SEPTEMBER 9 - 11, 2026..." - templated, false, corrected 2026-09-26.
ai_evidence_quote: none - the page contains no AI mention to quote.
artefacts:
  screenshot: 205_www-flowable-com-events-finovate-fall-2026.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: poor
capture_width_px: 1920
capture_method: urllib download of https://images.ctfassets.net/chja9v5uur3u/7hs87HreYEjx3TY1iJQeN3/ffeccad06fc02d87f7d2a5a737352616/finovateFall-hero.jpg?fm=webp&q=75&bg=rgb%3Affffff&w=1920 (asset published by the page); labels inside read with RapidOCR, this session cannot receive image content
---

## Why this row is UNCERTAIN

The page publishes figures and mentions AI, but the figure that would decide the
verdict could not be certified from the evidence this session can read (the DOM, the
page text, and OCR labels). Per CLAUDE.md section 5 an unresolved figure is UNCERTAIN
with needs_visual_check, never an exclusion.

## Observations (description only, no interpretation)

- **Figures on the page:** (no alt) | finovateFall-hero.jpg; Patrick-Züst-Senior-Solution-Architect-Flowable-Platform-Profile-Picture | Patrick_Zuest-Senior_Solution_Architect_Flowable_P; flow-pistols | flow-pistols.svg; (no alt) | Dan_Raquel.jpg
- **OCR labels of the captured figure:** (none legible)
- **Page text quote:** EVENT // SEPTEMBER 9 - 11, 2026 // FinovateFall 2026
- **Captured asset:** https://images.ctfassets.net/chja9v5uur3u/7hs87HreYEjx3TY1iJQeN3/ffeccad06fc02d87f7d2a5a737352616/finovateFall-hero.jpg?fm=webp&q=75&bg=rgb%3Affffff&w=1920 (1920x1080)

## What to check

Whether the captured figure (or another figure on the page) is a BPMN 2.0 process
diagram and whether an AI/LLM element sits inside that process.

## Visual pass observations (sighted, elicitation-aa 2026-09-25)

Looked at all 9 figures the page publishes, at native resolution (fetched with
`ledgers/flowable.raw/s7_figfetch.py`, which adds the Referer the shared tooling lacks).
Eight are speaker portraits (`Patrick_Zuest...`, `Dan_Raquel.jpg`, `John_Clark.jpg`,
`Louis_Briton.jpeg`), an abstract orange ribbon (`finovateFall-hero.jpg`), conference-room
and booth photos, and a Flowable swag bag.

The ninth, `image_17523769` (1920x2560), is a photograph of the Flowable booth: the
monitor on the stand runs the Flowable Design web modeller in a browser
(`design.flowable.com`, palette toolbar visible top-right) and displays a real drawn
process model. Zoomed 7x, the model shows a pool frame with an inner lane band,
rounded-rectangle tasks each with a small icon, circle events, diamond gateways,
sequence flows, an intermediate/boundary event circle, and two collapsed sub-process
boxes carrying a `+` marker. That is BPMN 2.0 structure, not CMMN 1.1: there are no
cut-corner stages, no sentry diamonds straddling a plan-item border, and no folder-shaped
case plan model.

No label anywhere in the model is legible at any magnification (the photo is oblique and
the monitor is shot at an angle), so whether an AI/LLM element sits inside the process
could not be resolved from the image. Recorded as UNCERTAIN with `needs_human_ruling`, not
as `E2`, because the AI question is unanswered rather than answered negatively.

