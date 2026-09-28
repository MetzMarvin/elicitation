---
n: 133
source: uipath-maestro-docs
source_name: UiPath Maestro user guide (docs.uipath.com)
source_type: vendor documentation
title: Multi-instance markers
url: https://docs.uipath.com/maestro/automation-cloud/latest/user-guide/markers-implementation
accessed: 2026-09-25
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "BPMN service task inside a subprocess with a sequential multi-instance marker; the figures are the element toolbar, the properties panels of those BPMN elements, the execution trail and the outputs section of the marked BPMN task."
bpmn_evidence_quote: "Use markers to configure a task to run once for each element in a List variable"
ai_evidence: "The captured properties panel shows the Action section with 'Start and wait for agent' selected and an agent configured; the prose runs 'Action: Select Start and wait for agent. Agent: Select the agent responsible for validating invoices.'"
ai_evidence_quote: "Action: Select Start and wait for agent. Agent: Select the agent responsible for validating invoices."
artefacts:
  screenshot: 133_agent-implementation-a84a9e65.png, 133_subprocess-properties-3fbf8456.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: page asset at its native URL (dev-assets.cms.uipath.com, .webp converted to .png) or the page's own downloadable model file
capture_quality: legible
capture_width_px: 1942
capture_method: plain GET of the figure asset listed on the page (ledgers/uipath-maestro-docs.raw/img/)
---

## What the page shows

Verbatim from the page:

> "Multi-instance markers link Configure multi-instance markers in Maestro to run a task once per item in a collection, sequentially or in parallel."

## Judgement

BPMN modelling pattern (multi-instance service task) whose implementation is an agent, evidenced by the properties panel and the prose.

## Artefact reading (native resolution unless stated)

- **BPMN:** BPMN service task inside a subprocess with a sequential multi-instance marker; the figures are the element toolbar, the properties panels of those BPMN elements, the execution trail and the outputs section of the marked BPMN task.
- **AI element:** The captured properties panel shows the Action section with "Start and wait for agent" selected and an agent configured; the prose runs "Action: Select Start and wait for agent. Agent: Select the agent responsible for validating invoices."

- `133_agent-implementation-a84a9e65.png` - Action = Start and wait for agent, with the agent selector filled
- `133_subprocess-properties-3fbf8456.png` - the service task inside the subprocess, properties panel open

## Notes for the researcher

Figure alt text on the page (verbatim): 'Element toolbar above a task in Maestro with the Select markers button highlighted.' | 'Screenshot showing a task with the sequential multi-instance marker applied and the Properties panel open with the Multi-instance section expanded.' | 'Screenshot of the Inputs section in the Properties panel, showing a workflow input parameter mapped to iterator.item.' | 'Screenshot of a Service task inside a subprocess with the Properties panel open, showing the iterator item expression entered in the Inputs field.' | 'Screenshot of the Action section in the Properties panel showing Start and wait for agent selected with an agent configured.' | 'Screenshot of the Inputs section in the Properties panel, showing a workflow input parameter mapped to iterator.item.'
