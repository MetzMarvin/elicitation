---
n: 13
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Intelligent Routing with Hugging Face
url: https://marketplace.camunda.com/apps/444798/intelligent-routing-with-hugging-face
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: Decisive: the listing publishes its .bpmn (the same file is linked twice). Process 'Intelligent-routing-with-openai' with six tasks, one of them AI-bound.
bpmn_evidence_quote: "<bpmn:process id="..." name="Intelligent-routing-with-openai""
ai_evidence: The service task 'Determine routing (AI)' carries `zeebe:modelerTemplate="io.camunda.connectors.HuggingFace.v1"` (task type `io.camunda:http-json:1`), i.e. the routing decision is made by a Hugging Face model call. The page calls it 'intelligent rout[ing]' with 'Task Intelligence' and 'Approve or Reroute'.
ai_evidence_quote: "zeebe:modelerTemplate="io.camunda.connectors.HuggingFace.v1""
artefacts:
  screenshot: null
  archive: null
  bpmn_xml: 013_intelligent-routing-hugging-face.bpmn
duplicate_of: null
access: public
capture_source: bpmn-xml
capture_quality: legible
capture_width_px: null
capture_method: curl of the raw.githubusercontent.com .bpmn behind the listing's Modeler import link; XML read directly
---

## What the page shows

An inquiry-routing process. A customer enters an inquiry (user task 'Enter inquiry (customer)'), the service task 'Determine routing (AI)' classifies it, and the flow routes to one of four human queues: 'Work on inquiry (Sales team)', '(Engineering team)', '(Legal team)' or '(default)'.

## Observations (description only, no interpretation)

- **AI activity - function:** the page says the blueprint 'empowers your business processes with intelligent rout[ing]', operationalizing AI/ML 'with Hugging Face, known of its cutting-edge natural language processing models'.
- **AI activity - element type:** a `serviceTask` bound to the Hugging Face connector element template.
- **Authority - downstream:** the four user tasks that receive the routed inquiry.
- **Authority - control:** the gateway(s) that split on the AI's routing decision (not resolved in the XML task list alone).
- **Input provenance:** the customer's own inquiry text (user task 'Enter inquiry (customer)').
- **Guards present:** the page lists 'Approve or Reroute' as a capability; the diagram's human queues are the receiving steps.
- **Prompt / model detail visible:** not visible in the XML; the model itself is chosen in the connector's properties, which the published file does not carry.

## Notes for the researcher

Process id/name says 'openai' while the bound template is HuggingFace.v1 and the file is named Intelligent_routing_with_HuggingFace.bpmn - the blueprint appears to have been forked. The listing links the 'ai-intelligent-routing' tutorial in camunda-platform-tutorials (the same repo as n=016's OpenAI variant), so n=013 and n=016 publish the same process shape with different model connectors; they are separate listings with separate .bpmn files, not duplicates.
