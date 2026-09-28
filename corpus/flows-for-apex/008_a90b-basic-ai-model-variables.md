---
n: 310
source: flows-for-apex
source_name: Flows for APEX (FlowQuest; flowsforapex.org docs, flowquest.net, GitHub)
source_type: vendor docs
title: A90b - Basic AI Model with Variables (BPMN model file, test/models)
url: https://raw.githubusercontent.com/flowsforapex/apex-flowsforapex/development/test/models/bpmn/A90b%20-%20Basic%20AI%20Model%20with%20Variables_0.bpmn
accessed: 2026-09-24
verdict: UNCERTAIN
needs_human_ruling: true
question: "The file is named 'Basic AI Model with Variables' and its process id is 'Process_90b_ai_variables', but no element carries any AI binding - the tasks are plain bpmn:task A-D. Is an AI-named test scaffold, with no AI element inside the process, an AI-enabled BPMN artefact or an E2?"
needs_visual_check: false
bpmn_evidence: BPMN 2.0 XML with bpmn:process, bpmn:task, start and end events - a linear A-B-C-D model
bpmn_evidence_quote: "<bpmn:process id=\"Process_90b_ai_variables\">"
ai_evidence: the only AI signal is the file name and the process id; no task carries an apex:type, apex:aiService or any AI extension element
ai_evidence_quote: "Process_90b_ai_variables"
artefacts:
  screenshot: null
  archive: null
  bpmn_xml: 008_a90b-basic-ai-model-variables.bpmn
duplicate_of: null
access: public
capture_source: bpmn-xml
capture_quality: legible
capture_width_px: null
capture_method: raw.githubusercontent.com URL built from the repo tree listing obtained via the GitHub API (never guessed)
---

## What the page shows

The same four-step linear model as record 007: start -> "Task A" -> "Task B" -> "Task C" ->
"Task D" -> end, with process id `Process_90b_ai_variables`. The name promises variables; no
variable elements appear on the activities in the file.

## Observations (description only, no interpretation)

- **AI activity - function:** not visible on the page. The file name is "A90b - Basic AI Model
  with Variables" and the process id is `Process_90b_ai_variables`, but no element states any AI
  behaviour.
- **AI activity - element type:** none - the four activities are plain `bpmn:task` (abstract
  tasks) with no implementation binding.
- **Authority - downstream:** not visible on the page.
- **Authority - data:** not visible on the page; despite the file name, no `apex:processVariable`
  or variable extension element is present on the activities.
- **Authority - control:** not visible on the page.
- **Input provenance:** not visible on the page.
- **Guards present:** none observed.
- **Prompt / model detail visible:** none.

## Notes for the researcher

Second of the three `A90*` test scaffolds (records 007-009); see record 007 for the group note.
