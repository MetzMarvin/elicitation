---
source: agilepoint
source_name: AgilePoint NX (documentation.agilepoint.com)
source_type: vendor documentation
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: YES
  C2_native_bpmn20: NO (operator ruling 2026-09-24: AgilePoint activity-icon notation with BPMN attributes)
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES
access: public
population_type: enumerable
population_estimate: 15
effort: small
needs_logged_in_browser: false
status: OUT-C2 (not surveyed; kept for audit trail)
---

## Criteria evidence

- **C1 YES**: https://documentation.agilepoint.com/1000/appbuilder/cloudenvShapeN8nInvokeAgent.html
  (2026-09-24): the "Invoke Agent (n8n) activity" is a process activity ("You can configure
  whether this activity waits for other activities before it runs"; "Full documentation
  coming soon"). The result list also shows "Image Classification - Initiate Subprocess
  activity", "OpenAI Compatible LLM" and "AI Control Tower".
- **C2 UNCLEAR**: https://documentation.agilepoint.com/1000/startup/cloudglossaryBpmnProperties.html:
  "Each activity has an optional set of properties for the BPMN standard." That describes
  BPMN *attributes* attached to AgilePoint's own activity shapes. Whether the canvas renders
  BPMN 2.0 notation is open. This is the same kind of question as Pega (B12).
- **C3 YES**, **C4 YES** (an established enterprise low-code/BPM vendor).

## The deciding check

One screenshot of an AgilePoint process canvas: BPMN shapes (events, gateways, rounded
tasks, lanes) or AgilePoint-specific activity icons? Record the notation by name.

## Entry points

- The AI activity pages under `/1000/appbuilder/` (their file names start with
  `cloudenvShape…`)
- The AgilePoint NX Connector for n8n examples page (linked from the anchor)
- `agilepoint.com/composable-appgen` (marketing, not opened)

## RESUME

(empty)
