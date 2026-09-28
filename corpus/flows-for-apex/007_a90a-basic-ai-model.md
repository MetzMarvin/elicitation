---
n: 309
source: flows-for-apex
source_name: Flows for APEX (FlowQuest; flowsforapex.org docs, flowquest.net, GitHub)
source_type: vendor docs
title: A90a - Basic AI Model (BPMN model file, test/models)
url: https://raw.githubusercontent.com/flowsforapex/apex-flowsforapex/development/test/models/bpmn/A90a%20-%20Basic%20AI%20Model_0.bpmn
accessed: 2026-09-24
verdict: UNCERTAIN
needs_human_ruling: true
question: "The file is named 'Basic AI Model' and its process id is 'Process_90a_ai_basic', but no element carries any AI binding - the tasks are plain bpmn:task A-D. Is an AI-named test scaffold, with no AI element inside the process, an AI-enabled BPMN artefact or an E2?"
needs_visual_check: false
bpmn_evidence: BPMN 2.0 XML with bpmn:process, bpmn:task, start and end events - a linear A-B-C-D model
bpmn_evidence_quote: "<bpmn:process id=\"Process_90a_ai_basic\">"
ai_evidence: the only AI signal is the file name and the process id; no task carries an apex:type, apex:aiService or any AI extension element
ai_evidence_quote: "Process_90a_ai_basic"
artefacts:
  screenshot: null
  archive: null
  bpmn_xml: 007_a90a-basic-ai-model.bpmn
duplicate_of: null
access: public
capture_source: bpmn-xml
capture_quality: legible
capture_width_px: null
capture_method: raw.githubusercontent.com URL built from the repo tree listing obtained via the GitHub API (never guessed)
---

## What the page shows

A four-step linear model: start -> "Task A" -> "Task B" -> "Task C" -> "Task D" -> end. Process
id `Process_90a_ai_basic`. Nothing else is in the file.

## Observations (description only, no interpretation)

- **AI activity - function:** not visible on the page. The file name is "A90a - Basic AI Model"
  and the process id is `Process_90a_ai_basic`, but no element states any AI behaviour.
- **AI activity - element type:** none - the four activities are plain `bpmn:task` (abstract
  tasks), which carry no implementation binding at all as shipped.
- **Authority - downstream:** not visible on the page.
- **Authority - data:** not visible on the page.
- **Authority - control:** not visible on the page.
- **Input provenance:** not visible on the page.
- **Guards present:** none observed.
- **Prompt / model detail visible:** none.

## Notes for the researcher

Part of a three-file `A90*` group in the repo's `test/models/bpmn/` directory (records 007-009),
all named "AI ... Model" with AI-flavoured process ids and no AI element inside. They are almost
certainly the vendor's test scaffolding for the AI feature, which is why they are surfaced as
UNCERTAIN rather than excluded: they are exactly what a researcher searching the repo for AI
models would land on, and their absence from the ledger would be an invisible gap.
