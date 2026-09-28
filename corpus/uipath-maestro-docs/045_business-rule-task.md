---
n: 45
source: uipath-maestro-docs
source_name: UiPath Maestro user guide (docs.uipath.com)
source_type: vendor documentation
title: Business rule task (Preview)
url: https://docs.uipath.com/maestro/automation-cloud/latest/user-guide/business-rule-task
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: Is a Studio Web properties-panel screenshot showing the Action list of a BPMN task (including "Start and wait for agent" and "Start and wait for external agent") an acceptable process artefact for this source, or does it fail E1-not-bpmn because it is not a process diagram? The same question covers the other five task-reference pages in this ledger.
needs_visual_check: false
bpmn_evidence: "The BPMN element itself (its task-type icon) plus the Studio Web properties panels of that element: General, the Action dropdown under Implementation, Inputs, Outputs, 'Add new' and the 'Set variable value' option."
bpmn_evidence_quote: "Available actions dropdown in the Business Rule Task Properties panel"
ai_evidence: "The Action dropdown lists 'Start and wait for agent', 'Start and wait for external agent', 'Start agentic process' and 'Start and wait for agentic process'; the page text reads 'Start and wait for agent  Starts a UiPath agent (a reusable logic block) and waits for it to finish execution.'"
ai_evidence_quote: "Start and wait for agent : Starts a UiPath agent (a reusable logic block) and waits for it to finish execution."
artefacts:
  screenshot: 045_maestro-service-task-properties-actions-588780-75494.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: page asset at its native URL (dev-assets.cms.uipath.com, .webp converted to .png) or the page's own downloadable model file
capture_quality: marginal
capture_width_px: 639
capture_method: plain GET of the figure asset listed on the page (ledgers/uipath-maestro-docs.raw/img/)
---

## What the page shows

Verbatim from the page:

> "Business rule task (Preview) link Business rule task element in Maestro for executing DMN 1.3 Business Rules stored in Orchestrator, including implementation type and action"

## Judgement

Reference page for one BPMN task type. The page's figures are the BPMN task icon and Studio Web properties panels, one of which is the Action dropdown; that dropdown lists agent actions, so the page documents which implementations a BPMN task of this type can be bound to. It is not a process diagram, which is why it is not recorded as a plain include.

## Artefact reading (native resolution unless stated)

- **BPMN:** The BPMN element itself (its task-type icon) plus the Studio Web properties panels of that element: General, the Action dropdown under Implementation, Inputs, Outputs, "Add new" and the "Set variable value" option.
- **AI element:** The Action dropdown lists "Start and wait for agent", "Start and wait for external agent", "Start agentic process" and "Start and wait for agentic process"; the page text reads "Start and wait for agent  Starts a UiPath agent (a reusable logic block) and waits for it to finish execution."

- `045_maestro-service-task-properties-actions-588780-75494.png` - the Action dropdown of this BPMN task type

## Notes for the researcher

Figure alt text on the page (verbatim): 'Business rule task icon' | 'Available actions dropdown in the Business rule task Properties panel' | 'Add new output option in the Business rule task Properties panel' | 'Add Variable dialog' | 'Set variable value option in the Business rule task'
