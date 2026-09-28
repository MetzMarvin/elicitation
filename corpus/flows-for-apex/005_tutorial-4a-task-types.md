---
n: 153
source: flows-for-apex
source_name: Flows for APEX (FlowQuest; flowsforapex.org docs, flowquest.net, GitHub)
source_type: vendor docs
title: Tutorial 4a - Tasks Get Your Work Done! (BPMN model file)
url: https://raw.githubusercontent.com/flowsforapex/apex-flowsforapex/development/bpmn_tutorials/xml/Tutorial%204a%20-%20Tasks%20Get%20Your%20Work%20Done%21_25.1.bpmn
accessed: 2026-09-24
verdict: UNCERTAIN
needs_human_ruling: true
question: "The service task is named 'Use me to call AI or send an email' but ships with apex:type='executePlsql' and apex:plsqlCode 'null;' - i.e. no AI binding as shipped. Does a blank scaffold whose task is designed to be AI-bound by the implementer count as an AI element (per the prompt's 'blank template diagrams' clause), or is it an E2?"
needs_visual_check: false
bpmn_evidence: BPMN 2.0 XML with bpmn:task, bpmn:userTask, bpmn:scriptTask, bpmn:serviceTask, bpmn:businessRuleTask and apex: extension elements
bpmn_evidence_quote: "<bpmn:process id=\"Tutorial4\" name=\"Task Types Tutorial\">"
ai_evidence: a service task whose NAME promises AI ("Use me to call AI or send an email") but whose binding is a placeholder PL/SQL call; the model's documentation text names GenAI as the intended binding
ai_evidence_quote: "serviceTask - Use me to call AI or send an email"
artefacts:
  screenshot: null
  archive: null
  bpmn_xml: 005_tutorial-4a-task-types.bpmn
duplicate_of: null
access: public
capture_source: bpmn-xml
capture_quality: legible
capture_width_px: null
capture_method: raw.githubusercontent.com URL built from the repo tree listing obtained via the GitHub API (never guessed)
---

## What the page shows

The "Task Types Tutorial" model - the vendor's catalogue of every BPMN task type in one diagram.
Tasks as printed: "This is a standard Task", "This is a Manual Task", "This is a standard Task",
"UserTask - I can call an APEX Human Task ( Action or Approval )", "scriptTask - I can run a
PL/SQL script", "serviceTask - Use me to call AI or send an email", "UserTask - I can call an
APEX page in your app", "UserTask - I can use Simple Form to collect some data", "BusinessRule
Task - use me to run a ML model", "ReceiveTask - receives a message from another process",
"SendTask - sends a message to another process".

## Observations (description only, no interpretation)

- **AI activity - function:** the service task's own label says "Use me to call AI or send an
  email". The model's documentation block states: "...such as GenAI, messaging, email, etc. In
  this release, you can use these to: - call a GenAI service, such as GPT, to recommend a
  decision or to generate a document - run a PL/SQL procedure that you provide (similar to a
  scriptTask) - send..."
- **AI activity - element type:** `bpmn:serviceTask`, but as shipped its binding is
  `apex:type="executePlsql"` with `<apex:plsqlCode>null;</apex:plsqlCode>` - a placeholder, not
  an AI binding. A separate `bpmn:businessRuleTask` named "BusinessRule Task - use me to run a
  ML model" is likewise `apex:type="executePlsql"` with `null;` (ML, not LLM).
- **Authority - downstream:** not visible on the page.
- **Authority - data:** not visible on the page; the PL/SQL placeholder is literally `null;`.
- **Authority - control:** not visible on the page.
- **Input provenance:** not visible on the page.
- **Guards present:** none observed.
- **Prompt / model detail visible:** none - no prompt text, provider or model name in the file.
  The documentation text names "GPT" only as an example of a GenAI service.

## Notes for the researcher

This is the sanctioned "blank template whose tasks can be bound to an AI agent by the
implementer" case, but the label promises AI while the shipped binding is a PL/SQL placeholder,
so the verdict is UNCERTAIN and the question above is for the researcher. The parallel docs
surface for this tutorial is flowsforapex.org/latest/tasks/, whose only artefact is a
pre-AI task-type strip image (record 010).
