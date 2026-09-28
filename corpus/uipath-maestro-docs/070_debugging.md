---
n: 70
source: uipath-maestro-docs
source_name: UiPath Maestro user guide (docs.uipath.com)
source_type: vendor documentation
title: Debugging
url: https://docs.uipath.com/maestro/automation-cloud/latest/user-guide/debugging
accessed: 2026-09-25
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "BPMN 2.0 diagram on the Maestro canvas in a debug session: message start event 'New Contact Created', send task 'Get Contact Details', service task 'Contact-Validation-Agent' with the agent marker, exclusive/parallel gateways, service tasks 'Langchain - Company Research...', 'Lead Scoring Agent' and 'Salesforce Summary Agent', user task 'Curate contact and Validate', end event 'Process Complete'."
bpmn_evidence_quote: "Tooltip 'Click to add a breakpoint' on a process element"
ai_evidence: "Four of the process steps are agents, named as such on the canvas and annotated: 'UiPath Agent - Contact Validation before proceeding to next steps', 'Langchain Company research Agent', 'UiPath Lead Scoring Agent', 'Salesforce Agent to get Contact summary details'. The execution trail lists 'Contact-Validation-Agent (Service task)' followed by 'Agent run - Contact Validation Agent'."
ai_evidence_quote: "Agent run - Contact Validation Agent"
artefacts:
  screenshot: 070_maestro-docs-image-587615-0f84a671.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: page asset at its native URL (dev-assets.cms.uipath.com, .webp converted to .png) or the page's own downloadable model file
capture_quality: legible
capture_width_px: 2493
capture_method: plain GET of the figure asset listed on the page (ledgers/uipath-maestro-docs.raw/img/)
---

## What the page shows

Verbatim from the page:

> "Debugging link Debug agentic processes in Maestro using the Debug and Debug step-by-step options, including context menu test controls on the start event."

## Judgement

The debugging page publishes a full agent-rich BPMN process (four agent service tasks) plus its execution trail. Read at native resolution.

## Artefact reading (native resolution unless stated)

- **BPMN:** BPMN 2.0 diagram on the Maestro canvas in a debug session: message start event "New Contact Created", send task "Get Contact Details", service task "Contact-Validation-Agent" with the agent marker, exclusive/parallel gateways, service tasks "Langchain - Company Research...", "Lead Scoring Agent" and "Salesforce Summary Agent", user task "Curate contact and Validate", end event "Process Complete".
- **AI element:** Four of the process steps are agents, named as such on the canvas and annotated: "UiPath Agent - Contact Validation before proceeding to next steps", "Langchain Company research Agent", "UiPath Lead Scoring Agent", "Salesforce Agent to get Contact summary details". The execution trail lists "Contact-Validation-Agent (Service task)" followed by "Agent run - Contact Validation Agent".

- `070_maestro-docs-image-587615-0f84a671.png` - the whole agent process canvas with the debug trail

## Notes for the researcher

Figure alt text on the page (verbatim): 'Test Configuration - Selection' | 'Debug configuration panel showing Solution resources tab' | 'Project arguments tab in the Debug configuration panel' | 'Debugging panel showing execution in progress' | 'Execution trail tab showing step details and variable values' | 'Breakpoint indicator on a process element in the canvas'
