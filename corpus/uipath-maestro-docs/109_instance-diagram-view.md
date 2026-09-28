---
n: 109
source: uipath-maestro-docs
source_name: UiPath Maestro user guide (docs.uipath.com)
source_type: vendor documentation
title: Instance diagram view
url: https://docs.uipath.com/maestro/automation-cloud/latest/user-guide/instance-diagram-view
accessed: 2026-09-25
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "BPMN diagram of the process Maestro.Contact.to.Opportunity rendered as an instance diagram view: per-element execution counts, P50 heatmap shading, exclusive/parallel gateways, message start event, end event 'Process Complete'."
bpmn_evidence_quote: "Heatmap view with elements shaded from blue (shortest) to red (longest) based on P50 duration"
ai_evidence: "Agent service tasks 'Contact-Validation-Agent' (circular agent marker on the card), 'Langchain - Company Research Agent', 'Lead Scoring Agent', 'Salesforce Summary Agent', each with an agent bracket annotation."
ai_evidence_quote: "Screenshot of the instance diagram view with a heatmap"
artefacts:
  screenshot: 109_maestro-docs-image-588287-46bb05f6.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: page asset at its native URL (dev-assets.cms.uipath.com, .webp converted to .png) or the page's own downloadable model file
capture_quality: legible
capture_width_px: 2486
capture_method: plain GET of the figure asset listed on the page (ledgers/uipath-maestro-docs.raw/img/)
---

## What the page shows

Verbatim from the page:

> "Instance diagram view link Visual indicators in the instance diagram view, showing completed, in-progress, and faulted instance counts by icon color for each process step."

## Judgement

Instance diagram view of the same agent process, with execution counts and a P50 heatmap; the agent tasks and their markers stay visible. Read at native resolution.

## Artefact reading (native resolution unless stated)

- **BPMN:** BPMN diagram of the process Maestro.Contact.to.Opportunity rendered as an instance diagram view: per-element execution counts, P50 heatmap shading, exclusive/parallel gateways, message start event, end event "Process Complete".
- **AI element:** Agent service tasks "Contact-Validation-Agent" (circular agent marker on the card), "Langchain - Company Research Agent", "Lead Scoring Agent", "Salesforce Summary Agent", each with an agent bracket annotation.

- `109_maestro-docs-image-588287-46bb05f6.png` - the heatmap instance view of the agent process

## Notes for the researcher

Figure alt text on the page (verbatim): 'Diagram showing execution counts with colored icons per step' | 'Execution duration tooltip showing average, minimum, maximum, P95, and P99 for a step' | 'Heatmap view with elements shaded from blue (shortest) to red (longest) based on P50 duration'
