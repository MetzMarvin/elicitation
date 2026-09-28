---
n: 16
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Intelligent Routing with AI
url: https://marketplace.camunda.com/apps/437115/intelligent-routing-with-ai
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: Decisive: the listing publishes its .bpmn. Process 'Intelligent-routing-with-openai' with six tasks, one of them AI-bound.
bpmn_evidence_quote: "<bpmn:process id="..." name="Intelligent-routing-with-openai""
ai_evidence: The service task 'Determine routing (AI)' carries `zeebe:modelerTemplate="io.camunda.connectors.OpenAI.v1"` (task type `io.camunda:http-json:1`); the page says 'It uses the OpenAI Connector to process signals within a business context'.
ai_evidence_quote: "It uses the OpenAI Connector to process signals within a business context"
artefacts:
  screenshot: null
  archive: null
  bpmn_xml: 016_intelligent-routing-with-ai.bpmn
duplicate_of: null
access: public
capture_source: bpmn-xml
capture_quality: legible
capture_width_px: null
capture_method: curl of the raw.githubusercontent.com .bpmn behind the listing's Modeler import link; XML read directly
---

## What the page shows

The same routing process as n=013 but bound to OpenAI: a customer enters an inquiry, 'Determine routing (AI)' classifies it, and the flow routes to 'Work on inquiry (Sales team)', '(Engineering team)', '(Legal team)' or '(default)'.

## Observations (description only, no interpretation)

- **AI activity - function:** the page says the blueprint 'exemplifies the use of AI to intelligently route customer inquiries to the appropriate department'.
- **AI activity - element type:** a `serviceTask` bound to the OpenAI connector element template.
- **Authority - downstream:** the four human queues.
- **Authority - control:** the routing gateway after the AI task.
- **Input provenance:** the customer's inquiry.
- **Guards present:** 'Approve or Reroute' is listed as a feature on the page.
- **Prompt / model detail visible:** not visible in the XML.

## Notes for the researcher

This listing carries no AI catalogue tag in the catalogue JSON (its facets are the generic connector ones) while its .bpmn contains an OpenAI-bound task - which is why the XML layer, not the page's tags, decided this row.
