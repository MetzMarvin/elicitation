---
n: 317
source: uipath-maestro-docs
source_name: UiPath Maestro user guide (docs.uipath.com)
source_type: vendor documentation
title: Using agents in Maestro
url: https://docs.uipath.com/maestro/automation-suite/2.2510/user-guide/using-agents-in-maestro
accessed: 2026-09-25
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "BPMN service task 'VALIDATE against State requirement' shown in the Studio Web properties panel of the Maestro BPMN modeller (Service task, General, Implementation, Inputs, Outputs, Update variables)."
bpmn_evidence_quote: "Properties panel of a Service task named VALIDATE against State requirement"
ai_evidence: "The panel sets Action = 'Start and wait for agent' with an 'Agent *' selector under it; the page states 'Agents are represented in Maestro BPMN workflows as Service Tasks.'"
ai_evidence_quote: "Agents are represented in Maestro BPMN workflows as Service Tasks."
artefacts:
  screenshot: 317_maestro-start-and-wait-for-agent-properties-587972-5.png, 317_maestro-start-and-wait-for-agent-properties2-587968.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: page asset at its native URL (dev-assets.cms.uipath.com, .webp converted to .png) or the page's own downloadable model file
capture_quality: marginal
capture_width_px: 834
capture_method: plain GET of the figure asset listed on the page (ledgers/uipath-maestro-docs.raw/img/)
---

## What the page shows

Verbatim from the page:

> "Using agents in Maestro link Agent integration within Maestro BPMN workflows, where agents are invoked as Service Tasks with input parameters and return output for"

## Judgement

The 2.2510 line publishes a page whose whole subject is agents as BPMN service tasks, with the properties panel showing the agent binding. The Cloud URL of the same slug redirects to integrating-systems-and-data, so this artefact exists on the 2.2510 line only.

## Artefact reading (native resolution unless stated)

- **BPMN:** BPMN service task "VALIDATE against State requirement" shown in the Studio Web properties panel of the Maestro BPMN modeller (Service task, General, Implementation, Inputs, Outputs, Update variables).
- **AI element:** The panel sets Action = "Start and wait for agent" with an "Agent *" selector under it; the page states "Agents are represented in Maestro BPMN workflows as Service Tasks."

- `317_maestro-start-and-wait-for-agent-properties-587972-5.png` - Service task, Action = Start and wait for agent
- `317_maestro-start-and-wait-for-agent-properties2-587968.png` - the second agent properties capture

## Notes for the researcher

Figure alt text on the page (verbatim): 'Start and wait for agent Properties' | 'Start and wait for agent Properties2' | 'inputs and outputs'
