---
n: 156
source: flows-for-apex
source_name: Flows for APEX (FlowQuest; flowsforapex.org docs, flowquest.net, GitHub)
source_type: vendor docs
title: Tutorial 4d - Using an AI Service Task (BPMN model file)
url: https://raw.githubusercontent.com/flowsforapex/apex-flowsforapex/development/bpmn_tutorials/xml/Tutorial%204d%20-%20Using%20an%20AI%20Service%20Task_25.1.bpmn
accessed: 2026-09-24
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: BPMN 2.0 XML with bpmn:process, bpmn:serviceTask, bpmn:userTask and an explicit apex: extension namespace
bpmn_evidence_quote: "<bpmn:process id=\"Process_14di6413\" name=\"Tutorial 4d - Adding AI\">"
ai_evidence: two service tasks declared with apex:type="apexAIGeneration" and named "(Gen AI)", each carrying an apex:aiService binding
ai_evidence_quote: "bpmn:serviceTask id=\"Activity_1yar0ho\" name=\"Assess Likelihood of Fraud (Gen AI)\" apex:type=\"apexAIGeneration\""
artefacts:
  screenshot: null
  archive: null
  bpmn_xml: 004_tutorial-4d-ai-service-task.bpmn
duplicate_of: null
access: public
capture_source: bpmn-xml
capture_quality: legible
capture_width_px: null
capture_method: raw.githubusercontent.com URL built from the repo tree listing obtained via the GitHub API (never guessed)
---

## What the page shows

The lossless source model for the taxpayer-fraud process documented at
flowsforapex.org/latest/ai-service-task/ (record 001). Process name "Tutorial 4d - Adding AI".
Elements: a task "Set up Data"; a user task "Human Review" (`apex:type="apexPage"`); a service
task "Assess Likelihood of Fraud (Gen AI)" and a service task "Generate Request for More Info
(Gen AI)", both `apex:type="apexAIGeneration"`; a service task "Send Email"
(`apex:type="sendMail"`); outcomes named "OK", "EMAIL", "HUMAN", "FRAUD", "Fraud Found", "No
Fraud Found".

## Observations (description only, no interpretation)

- **AI activity - function:** a text annotation in the model reads "Our first AI Service Call. We
  ask the AI Service to look at the taxpayer information, and return (as a Colon separated list)
  one or more of - EMAIL (for more i...". The setup step's annotation reads: "Set Up Step. This
  Step uses BEFORE TASK variable expressions to: - set the APEX AI Service to be used to
  'F4A_AI_SERVICE' ... - set the AI temperature to 0 to get a repeatable, accurate result - sets
  up the system prompt including data about a taxpayer with high salary, high spending, ..."
- **AI activity - element type:** `bpmn:serviceTask` with the extension attribute
  `apex:type="apexAIGeneration"` - the AI nature is a task binding, not a distinct node type.
- **Authority - downstream:** the AI tasks feed the outcome labels OK / EMAIL / HUMAN / FRAUD and
  the human task "Human Review"; a further service task "Send Email" (`apex:type="sendMail"`) is
  bound downstream.
- **Authority - data:** the AI Service is bound through a process variable -
  `<apex:aiService><apex:expressionType>processVariable</apex:expressionType><apex:expression>
  pv_ai_service</apex:expression>` - as is the temperature (`apex:aiTemperature` with
  `<apex:expression>pv_temperature</apex:expression>`). The second AI task binds `PV_AI_SERVICE`
  and pre-populates variables with `apex:beforeTask` / `apex:processVariable` blocks.
- **Authority - control:** the returned label list is consumed by the process's routing to the
  four named outcomes, with "Human Review" on the human branch.
- **Input provenance:** instance data assembled by the "Set up Data" step and by the
  `apex:beforeTask` variable expressions; the system prompt is described as including "data
  about a taxpayer with high salary, high spending".
- **Guards present:** the user task "Human Review"; the instruction to set the AI temperature to
  0 "to get a repeatable, accurate result"; and a documented JSON-only response constraint (see
  record 001).
- **Prompt / model detail visible:** the AI service is referenced by a variable name
  (`F4A_AI_SERVICE` / `pv_ai_service`), so no provider or model name is hard-coded in the model.
  The temperature is set to 0. The system prompt's content is described in the annotation but
  not inlined verbatim in the XML.

## Notes for the researcher

Highest-value artefact in this source after record 003: the XML is lossless and shows the
binding attribute directly. Almost certainly the same process as the docs artefact (record 001),
published on the repo surface; identity is left to reconciliation.
