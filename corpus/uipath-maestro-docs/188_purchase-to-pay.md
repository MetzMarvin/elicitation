---
n: 188
source: uipath-maestro-docs
source_name: UiPath Maestro user guide (docs.uipath.com)
source_type: vendor documentation
title: Purchase to pay use case
url: https://docs.uipath.com/maestro/automation-cloud/latest/user-guide/purchase-to-pay
accessed: 2026-09-25
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "BPMN diagram of a purchase-to-pay process: task cards with BPMN task-type icons, exclusive and event-based gateways, boundary timer/message events, end event 'Invoice Processing Complete'."
bpmn_evidence_quote: "purchase to pay"
ai_evidence: "The task 'Invoice Dispute Analysis (3rd Party AI Agent)' is part of the process flow, on the No branch of 'Match Successful?'; its card carries the circular UiPath agent marker."
ai_evidence_quote: "Invoice Dispute Analysis (3rd Party AI Agent)"
artefacts:
  screenshot: 188_maestro-purchase-to-pay-596757-570dbd8a.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: page asset at its native URL (dev-assets.cms.uipath.com, .webp converted to .png) or the page's own downloadable model file
capture_quality: legible
capture_width_px: 1245
capture_method: plain GET of the figure asset listed on the page (ledgers/uipath-maestro-docs.raw/img/)
---

## What the page shows

Verbatim from the page:

> "Purchase to pay use case link Purchase-to-pay process use case in Maestro, covering end-to-end procurement automation from purchase requisition through supplier payment."

## Judgement

Use-case BPMN diagram with one task explicitly named after its AI implementation.

## Artefact reading (native resolution unless stated)

- **BPMN:** BPMN diagram of a purchase-to-pay process: task cards with BPMN task-type icons, exclusive and event-based gateways, boundary timer/message events, end event "Invoice Processing Complete".
- **AI element:** The task "Invoice Dispute Analysis (3rd Party AI Agent)" is part of the process flow, on the No branch of "Match Successful?"; its card carries the circular UiPath agent marker.

- `188_maestro-purchase-to-pay-596757-570dbd8a.png` - the whole P2P diagram; the agent task is on the No branch

## Notes for the researcher

Figure alt text on the page (verbatim): 'purchase to pay'
