---
n: 0
url: https://www.ofelia.com/downloads
source: bonitasoft
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: >-
  The figure is a Bonita Studio illustration with an AI Assistant panel: does a
  design-time assistant panel inside a Studio mockup count as an AI element *in a
  process*, or is it design-time AI (E2)?
bpmn_evidence: >-
  The figure is a Figma export, so no `<text>` node and no bpmn-js provenance comment
  survive: the notation had to be read from the pixels. What the mockup draws is two lanes
  - "Risk Assessment Lane" (start -> Verify -> Review) and "Compliance Lane" (Check ->
  end) - inside a Bonita Studio window frame. Lanes and tasks are drawn, but this is the
  vendor's own product mockup, not a BPMN 2.0 model; there are no pools, events, gateways
  or sequence flows of the BPMN kind.
ai_evidence: >-
  The AI is visible in the drawing as a product panel, not as a process element: the
  Studio window shows an "AI Assistant" beside the lanes, whose cards read "Process
  Suggestion - Add parallel gateway for faster review", "Risk Analysis - Bottleneck
  detected at approval step", "Compliance Check - GDPR compliant, SOC 2 ready" and "Action
  Required - Review timeout configuration". The AI is design-time advice about the model,
  not an AI element inside a running process.
artefacts:
  - screenshot: 013_bonita-studio-ai-assistant-illu.png
  - figure: the Bonita Studio illustration with its AI Assistant panel (Bonita_studio_illu.svg)
capture_quality: legible
capture_width_px: 944
capture_height_px: 752
---

## What the page shows

The page's figure "Bonita_studio_illu.svg" is a Bonita Studio mockup (a Figma export: every text is drawn as a path, no <text> node survives, and the file carries no bpmn-js provenance). Inside it: a "Risk Assessment Lane" (start -> Verify -> Review) and a "Compliance Lane" (Check -> end) beside an "AI Assistant" panel whose cards read "Process Suggestion - Add parallel gateway for faster review", "Risk Analysis - Bottleneck detected at approval step", "Compliance Check - GDPR compliant, SOC 2 ready" and "Action Required - Review timeout configuration". The lanes are drawn, but the notation is the vendor's own mockup, not BPMN 2.0 - and the AI sits in the design-time assistant, not in a process element.

## Observations

- Notation: a Figma-drawn product mockup, texts as paths.
- Evidence looked at: Bonita_studio_illu.svg looked at in full (472x376) and its own prose read.
- The page is `/downloads`, the Bonita Studio download page; the figure is `Bonita_studio_illu.svg` (472x376 as published; the capture is the same figure at 944x752).
- This is the pixel-level finding; the same wording is the ledger row for this page, so the two cannot disagree.

## Notes for the researcher

One of the five www.ofelia.com pages ruled UNCERTAIN in this source (records 012-016). The other 127 judged site pages are E0/E1/E2/E3 ledger rows without records.
