---
n: 0
url: https://www.ofelia.com/ofelia-assistant
source: bonitasoft
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: >-
  The figure is Ofelia's own workflow view (a stack of step cards with a branch), not BPMN
  2.0: does a vendor's proprietary workflow depiction count as a process artefact for the
  census, or is it E1-not-bpmn?
bpmn_evidence: >-
  The figure `Ofelia_workflow.svg` draws a process view with real control flow - "Employee
  request" -> "Manager approval" -> a branch into "Finance review" and "Auto-approved" ->
  "Complete & notify" - but in the vendor's proprietary card notation (a dark card headed
  "Ofelia Workflow" with a green "Published" badge). There are no pools, lanes, events,
  gateways or sequence flows, and no bpmn-js provenance: on the notation test alone this
  would be E1-not-bpmn, and it is recorded as UNCERTAIN only because "a process depiction
  in proprietary notation" is the kind of near-miss the researcher may still want to see.
ai_evidence: >-
  No AI element is drawn in the workflow card. The page is the Ofelia Assistant product
  page and its other figure, `Visuel.svg`, is a chat mockup of the assistant ("Ofelia
  Agent"), so any AI on the page is the assistant being sold, not an AI element inside the
  drawn process.
artefacts:
  - screenshot: 014_ofelia-workflow-card.png
  - figure: the "Ofelia Workflow" card (Ofelia_workflow.svg)
capture_quality: legible
capture_width_px: 880
capture_height_px: 626
---

## What the page shows

The page's figure "Ofelia_workflow.svg" shows Ofelia's own workflow view: a dark card headed "Ofelia Workflow" with a green "Published" badge, and the drawn sequence "Employee request" -> "Manager approval" -> a branch into "Finance review" and "Auto-approved" -> "Complete & notify". It is a process depiction with named steps and real control flow (a branch and a merge), but in the vendor's proprietary card notation: no pools, lanes, events, gateways or sequence flows.

## Observations

- Notation: a proprietary workflow view (step cards with a branch).
- Evidence looked at: Ofelia_workflow.svg looked at in full (440x313) alongside the page's other figures (Visuel.svg: an Ofelia Agent chat mockup).
- The page is `/ofelia-assistant`; the figure is `Ofelia_workflow.svg` (440x313 as published; the capture is the same figure at 880x626).
- This is the pixel-level finding; the same wording is the ledger row for this page, so the two cannot disagree.

## Notes for the researcher

One of the five www.ofelia.com pages ruled UNCERTAIN in this source (records 012-016). The other 127 judged site pages are E0/E1/E2/E3 ledger rows without records.
