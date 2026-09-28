---
n: 160
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: AI Message Delivery Service
url: https://marketplace.camunda.com/apps/583287/ai-message-delivery-service
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: BPMN process published twice over: as the overview asset (a canvas capture) and as a downloadable .bpmn (process 'Message Delivery Service'). Read from the XML: start event 'Message Needs to be Delivered' -> exclusive gateway -> serviceTask 'AI Task Agent' -> exclusive gateway 'Do we need to run some tools?' with the yes-branch entering the ad-hoc sub-process 'NIall's Tools' (holding the user task 'Deliver message by Hand') and looping back to the joining gateway, and the no-branch going to the end event 'Message Delivered'.
bpmn_evidence_quote: "AI Task Agent"
ai_evidence: Decisive, from the .bpmn's own extension elements: the service task 'AI Task Agent' carries modelerTemplate 'io.camunda.connectors.agenticai.aiagent.v1' - Camunda's agentic-AI agent template - and the tool-calling loop around it is drawn explicitly: the gateway 'Do we need to run some tools?' feeds the ad-hoc sub-process 'NIall's Tools' whose only task is a human one ('Deliver message by Hand'). In the capture the task carries the violet agentic-AI glyph and the ad-hoc container shows its '~' marker. The page's own copy names the pattern: 'Use this blueprint to get started with Camunda's agentic AI capabilities'.
ai_evidence_quote: "Use this blueprint to get started with Camunda's agentic AI capabilities"
artefacts:
  screenshot: 160_ai-message-delivery-service.png
  archive: null
  bpmn_xml: 160_ai-message-delivery-service.bpmn
duplicate_of: null
access: public
capture_source: bpmn-xml
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own asset (d3bql97l1ytoxn.cloudfront.net, app_resources/583287/overview/img12131779544551099132-2x.png, 1100x506) and of the .bpmn reached through the listing's own Modeler import link; the image read natively at full size, the XML read directly
---

## What the page shows

The AI Message Delivery Service (Camunda Services GmbH, blueprint). The listing publishes an agentic message-delivery process: an AI agent task decides whether tools are needed and, when they are, works inside an ad-hoc sub-process that contains a single human task.

## Observations (description only, no interpretation)

- **AI activity - function:** agentic message delivery - an AI agent task with a tool-calling loop over an ad-hoc sub-process of available tools.
- **AI activity - element type:** a `serviceTask` labelled 'AI Task Agent' bound to Camunda's `io.camunda.connectors.agenticai.aiagent.v1` template, plus the ad-hoc sub-process 'NIall's Tools' as its tool container.
- **Authority - downstream:** the end event 'Message Delivered' on the no-tools branch, and the loop back through the tool sub-process on the tools branch.
- **Authority - data:** none drawn.
- **Authority - control:** the exclusive gateway 'Do we need to run some tools?', which the agent task's outcome feeds - the drawn tool-invocation guard.
- **Authority - control (human):** the user task 'Deliver message by Hand' inside 'NIall's Tools' - a human tool the agent may call, not a reviewer of the agent.
- **Input provenance:** the message to be delivered ('Message Needs to be Delivered').
- **Guards present:** the tool-calling gateway; no approval or confidence gate is drawn.
- **Prompt / model detail visible:** none - the XML names the agent template but no model, provider or prompt; the tool sub-process contains a single human task.

## Notes for the researcher

The cleanest agentic artefact in this batch: the AI agent template is named in the process file itself and the surrounding tool-calling structure is drawn. Worth noting for the corpus that the agent's only tool is a human task, i.e. the agent's authority is to decide whether to delegate to a person.
