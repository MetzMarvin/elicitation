---
n: 97
source: uipath-maestro-docs
source_name: UiPath Maestro user guide (docs.uipath.com)
source_type: vendor documentation
title: Implementing a complex process
url: https://docs.uipath.com/maestro/automation-cloud/latest/user-guide/how-to-complex-process
accessed: 2026-09-25
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "BPMN diagram of the invoice processing process showing all tasks, gateways, and flow paths: start event 'Invoice received' -> service task 'Invoice to PO matching' -> exclusive gateway 'Is resolution required?' -> (Yes) service task 'Resolve discrepancies' with the circular UiPath agent marker and an 'Agent' bracket annotation -> ... -> user task 'Invoice approval' -> service task 'Post invoice to SAP' -> end event 'Invoice processed'; rejects go to send task 'Notify vendor'."
bpmn_evidence_quote: "BPMN diagram of the invoice processing process showing all tasks, gateways, and flow paths"
ai_evidence: "The AI element sits inside the process: the service task 'Resolve discrepancies' is bracketed 'Agent' in the diagram (the same glyph marks the second, non-agent 'Resolve discrepancies' task as 'Action Center Action app'). The page instructs: 'Add Agent as an annotation to indicate this will be an agent task.'"
ai_evidence_quote: "Add Agent as an annotation to indicate this will be an agent task."
artefacts:
  screenshot: 097_maestro-process-diagram-599989-7f31b59a.png, 097_maestro-all-instances-view-complex-process-599937-67.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: page asset at its native URL (dev-assets.cms.uipath.com, .webp converted to .png) or the page's own downloadable model file
capture_quality: legible
capture_width_px: 2146
capture_method: plain GET of the figure asset listed on the page (ledgers/uipath-maestro-docs.raw/img/)
---

## What the page shows

Verbatim from the page:

> "Implementing a complex process link Build a complex Maestro process combining multiple automations, human approvals, and AI agents with decision logic and governance at scale."

## Judgement

BPMN 2.0 invoice process whose service task "Resolve discrepancies" carries the UiPath agent marker and an "Agent" bracket annotation; the same page also publishes the instance view of that process. Read at native resolution.

## Artefact reading (native resolution unless stated)

- **BPMN:** BPMN diagram of the invoice processing process showing all tasks, gateways, and flow paths: start event "Invoice received" -> service task "Invoice to PO matching" -> exclusive gateway "Is resolution required?" -> (Yes) service task "Resolve discrepancies" with the circular UiPath agent marker and an "Agent" bracket annotation -> ... -> user task "Invoice approval" -> service task "Post invoice to SAP" -> end event "Invoice processed"; rejects go to send task "Notify vendor".
- **AI element:** The AI element sits inside the process: the service task "Resolve discrepancies" is bracketed "Agent" in the diagram (the same glyph marks the second, non-agent "Resolve discrepancies" task as "Action Center Action app"). The page instructs: "Add Agent as an annotation to indicate this will be an agent task."

- `097_maestro-process-diagram-599989-7f31b59a.png` - the full process diagram (agent task + "Agent" bracket)
- `097_maestro-all-instances-view-complex-process-599937-67.png` - the same process in the instance view

## Notes for the researcher

Figure alt text on the page (verbatim): 'BPMN diagram of the invoice processing process showing all tasks, gateways, and flow paths' | 'Import schema dialog in Data Fabric' | 'import button data fabric' | 'Create new dropdown with Import option in Studio Web' | 'Update entities option in the Data Manager' | 'agentic orchestration type process'
