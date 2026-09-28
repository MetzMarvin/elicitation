---
n: 311
source: flows-for-apex
source_name: Flows for APEX (FlowQuest; flowsforapex.org docs, flowquest.net, GitHub)
source_type: vendor docs
title: A90c - AI Gateway Routing Model (BPMN model file, test/models)
url: https://raw.githubusercontent.com/flowsforapex/apex-flowsforapex/development/test/models/bpmn/A90c%20-%20AI%20Gateway%20Routing%20Model_0.bpmn
accessed: 2026-09-24
verdict: UNCERTAIN
needs_human_ruling: true
question: "The file is named 'AI Gateway Routing Model', but the routing variable is set by a task named 'Set Routing Variable' and no element carries an AI binding - is AI in the name only (E2), or is this the vendor's routing-by-AI test scaffold?"
needs_visual_check: false
bpmn_evidence: BPMN 2.0 XML with bpmn:process, exclusive and inclusive gateways, join gateway, tasks and lanes ("Admin User")
bpmn_evidence_quote: "<bpmn:process id=\"Process_90c_ai_gateways\">"
ai_evidence: the only AI signal is the file name and the process id; the routing variable is set by an explicit task named "Set Routing Variable", not by any AI binding
ai_evidence_quote: "Set Routing Variable"
artefacts:
  screenshot: null
  archive: null
  bpmn_xml: 009_a90c-ai-gateway-routing.bpmn
duplicate_of: null
access: public
capture_source: bpmn-xml
capture_quality: legible
capture_width_px: null
capture_method: raw.githubusercontent.com URL built from the repo tree listing obtained via the GitHub API (never guessed)
---

## What the page shows

A gateway-routing model, process id `Process_90c_ai_gateways`. Elements as printed: "Set Process
Variables", "Set Routing Variable", an "Exclusive Gateway" routing to "Admin Task" (lane "Admin
User"), "High Priority Task" (route "High Priority"), "North Region Task" (route "North
Region"), "Approve Task" / "Reject Task" and a "Default Task" (route "Default"), converging on a
"Join Gateway" (inclusive) to the end.

## Observations (description only, no interpretation)

- **AI activity - function:** not visible on the page. The file name is "A90c - AI Gateway
  Routing Model" and the process id is `Process_90c_ai_gateways`, but no element states any AI
  behaviour.
- **AI activity - element type:** none - the routing decision is made by an explicit task named
  "Set Routing Variable" writing a control variable; there is no `apexAIGeneration` service task,
  no `apex:aiService` binding and no AI extension element.
- **Authority - downstream:** tasks "Admin Task", "High Priority Task", "North Region Task",
  "Approve Task", "Reject Task", "Default Task".
- **Authority - data:** a routing/control variable set by "Set Routing Variable" and by "Set
  Process Variables"; the file name suggests this variable is the slot an AI would populate.
- **Authority - control:** an exclusive gateway selects among the named routes; an inclusive
  "Join Gateway" converges them.
- **Input provenance:** not visible on the page.
- **Guards present:** none observed.
- **Prompt / model detail visible:** none.

## Notes for the researcher

Third of the three `A90*` test scaffolds (records 007-009) and the closest of the three to the
vendor's documented "Generate Process Routing" use case (record 001): it is a routing model whose
decision variable is set by an ordinary task. Whether it is intended as the AI-routing test
harness or is simply misnamed is the researcher's call.
