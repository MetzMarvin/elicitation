---
n: 23
source: flows-for-apex
source_name: Flows for APEX (FlowQuest; flowsforapex.org docs, flowquest.net, GitHub)
source_type: vendor docs
title: Configure an AI Service Task
url: https://flowsforapex.org/latest/ai-service-task/
accessed: 2026-09-24
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: figure image on the page (ai-service-task-tax-example-diagram.png, 2166x1174) plus prose naming BPMN elements; the same process is published as lossless BPMN XML in the vendor repo (see record 004)
bpmn_evidence_quote: "Add a Service Task into your BPMN diagram"
ai_evidence: service task whose Task Type property is set to APEX AI Generation; the task labels carry "(Gen AI)"
ai_evidence_quote: "Task Type. Select APEX AI Generation and open the APEX Human Task section."
artefacts:
  screenshot: 001_ai-service-task-tax-example-diagram.png
  archive: 001_ai-service-task.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 2166
capture_method: curl -L on the /assets/images/... src read from the page DOM (never guessed); a second asset, 001_ai-service-task-config-panel.png (1594x1376), shows the same task's configuration panel
---

## What the page shows

A taxpayer-fraud example process. A service task "Assess Likelihood of Fraud (Gen AI)" and a
second service task "Generate Request for More Info (Gen AI)" sit in a process that branches
through a gateway to the outcomes "ok (no suspicion)", "email (request more information)",
"human (flag for human review)" and "fraud (confirmed fraud based on inconsistencies)", with a
user task "Human Review" on the human branch. The page states: "The Flows for APEX AI Service
Task allows you to call Generative AI Services as a workflow step." Configuration is by task
property: "Task Type. Select APEX AI Generation and open the APEX Human Task section."

## Observations (description only, no interpretation)

- **AI activity - function:** generates a routing/labelling decision. The page's own use-case
  heading is "Generate Process Routing / Recommended Course of Action", expanded as: "In some
  applications, you can use GenAI to recommend a course of action in your process. This can
  then be combined with a BPMN Gateway to direct process flow." A second documented use case is
  "Generate Document".
- **AI activity - element type:** an ordinary BPMN service task; the AI nature is carried by the
  task's `Task Type` property ("APEX AI Generation"), not by a distinct node type. In the vendor
  repo the same construct appears as `<bpmn:serviceTask ... apex:type="apexAIGeneration">`.
- **Authority - downstream:** the example prompt asks the model to return labels, and the process
  routes on them: "- ok (no suspicion) - email (request more information) - human (flag for
  human review) - fraud (confirmed fraud based on inconsistencies)". The service task is wired to
  a gateway and, on the "human" branch, to the user task "Human Review".
- **Authority - data:** the prompt asks for "an additional field called rationale into the JSON
  with the reason for the labels". The response is bound to a process variable; the settings
  "can accept a value as: static value ... a process variable".
- **Authority - control:** a gateway consumes the AI output to direct process flow; the human
  branch is a user task named "Human Review".
- **Input provenance:** the process data of the running instance (the taxpayer's case data),
  supplied through process variables. The page names a pre-requisite: "The AI Service Task is
  implemented using APEX AI infrastructure, so you need to define an AI Service in APEX."
- **Guards present:** human review - the label "human (flag for human review)" on its own branch,
  reached through the gateway; and the prompt instruction "Respond only with a valid JSON
  object."
- **Prompt / model detail visible:** the page shows the prompt-shaping instruction "e.g.,
  'Respond only with a valid JSON object.'" and that all three AI settings accept "static value"
  or "a process variable". No provider or model name is printed on this page; those appear in
  the repo XML (record 004) and in the 26.1 autonomous-agent artefact (record 003).

## Notes for the researcher

The page renders the same model as `bpmn_tutorials/xml/Tutorial 4d - Using an AI Service
Task_25.1.bpmn` in the vendor repo (record 004). They are almost certainly the same process
published on two surfaces, but the docs image and the XML are not byte-comparable, so both are
recorded and the identity call is left to reconciliation. The second asset saved here
(`001_ai-service-task-config-panel.png`) is the configuration-panel screenshot showing the
`Task Type` / AI Service / prompt fields - it is the only view of the binding itself, since the
diagram image alone does not reveal that these tasks are AI-backed.
