---
n: 171
source: flows-for-apex
source_name: Flows for APEX (FlowQuest; flowsforapex.org docs, flowquest.net, GitHub)
source_type: vendor docs
title: Tutorial 8a - The Full Monty (the top half!) (BPMN model file)
url: https://raw.githubusercontent.com/flowsforapex/apex-flowsforapex/development/bpmn_tutorials/xml/Tutorial%208a%20-%20The%20Full%20Monty%20%28the%20top%20half%21%29_25.1.bpmn
accessed: 2026-09-24
verdict: UNCERTAIN
needs_human_ruling: true
question: "A service task is NAMED 'Gen AI Service Task' but carries apex:type='executePlsql' with a PL/SQL binding and no apex:aiService element - the name signals AI, the binding does not. Is the label alone enough for an AI element, or is this an E2 (AI only in the task name)?"
needs_visual_check: false
bpmn_evidence: BPMN 2.0 XML with bpmn:process, subProcess, userTask, scriptTask, serviceTask, businessRuleTask, boundary events and apex: extension elements
bpmn_evidence_quote: "<bpmn:process id=\"Process_Tutorial8a\" name=\"Tutorial8a - The Full Monty\">"
ai_evidence: a service task labelled "Gen AI Service Task"; its binding is apex:type="executePlsql" and no apex:aiService element is present
ai_evidence_quote: "<bpmn:serviceTask id=\"Activity_15j40yo\" name=\"Gen AI Service Task\" apex:type=\"executePlsql\">"
artefacts:
  screenshot: null
  archive: null
  bpmn_xml: 006_tutorial-8a-full-monty.bpmn
duplicate_of: null
access: public
capture_source: bpmn-xml
capture_quality: legible
capture_width_px: null
capture_method: raw.githubusercontent.com URL built from the repo tree listing obtained via the GitHub API (never guessed)
---

## What the page shows

The vendor's large "everything at once" teaching model: lanes "Department A Lane", "Department
B Lane"; tasks "standard Task", "Close Input Period and Proceed", "Process Message Payload",
"Option A", "Option B (default)", "Notify Manager of Termination"; a user task "userTask (call
APEX Approval Task)" `apex:type="apexPage"`; a script task "scriptTask (run a PL/SQL script)"
`apex:type="executePlsql"`; a business rule task "businessRules Task (run scoring model)"
`apex:type="executePlsql"`; nested sub-processes "Sub Process F", "Sub Process F1", "Sub Process
F2", "Parallel Iterating SubProcess*", "Sequentially Iterating SubProcess*", "Looping
SubProcess*"; boundary-event material; and a service task named "Gen AI Service Task".

## Observations (description only, no interpretation)

- **AI activity - function:** not stated in the model. The only AI signal is the element's name,
  "Gen AI Service Task".
- **AI activity - element type:** `bpmn:serviceTask` whose binding is
  `apex:type="executePlsql"` - a PL/SQL call, the same binding used by the model's ordinary
  script task and business rule task. No `apex:aiService`, no `apexAIGeneration` type and no AI
  extension element appears on the element.
- **Authority - downstream:** not visible on the page.
- **Authority - data:** not visible on the page.
- **Authority - control:** not visible on the page.
- **Input provenance:** not visible on the page.
- **Guards present:** none observed.
- **Prompt / model detail visible:** none - no prompt text, provider or model name.

## Notes for the researcher

This is the "name signals AI but the binding does not" case in its purest form: the model is a
teaching collage, so the AI-named task may be a placeholder for a GenAI demonstration that was
never wired, or a rename of a PL/SQL demo. Either way the element name would be read as an AI
element by anyone opening the file, so it is surfaced rather than excluded. The related
`Tutorial 4a` model (record 005) shows the same vendor pattern of AI-promising names over
placeholder bindings.
