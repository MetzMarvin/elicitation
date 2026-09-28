---
n: 112
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Intelligent Routing with Azure OpenAI
url: https://marketplace.camunda.com/apps/444799/intelligent-routing-with-azure-openai
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: BPMN process published twice over: as the overview asset (a Web Modeler canvas) and as a downloadable .bpmn reached through the listing's own Modeler import link (intelligent routing with Azure AI, process name 'Intelligent-routing-with-openai'). Read from the XML: serviceTask 'Determine routing (AI)' between the user task 'Enter inquiry (customer)' and the gateway 'route to which department?', which fans out to 'Work on inquiry (default)', '(Sales team)', '(Engineering team)' and '(Legal team)'.
bpmn_evidence_quote: "route to which department?"
ai_evidence: Decisive, from the .bpmn itself: the routing service task carries modelerTemplate 'io.camunda.connectors.AzureOpenAI.outbound.v1' and the element name 'Determine routing (AI)'. The page's own copy names the provider and the intended control loop: 'Design loops with human feedback and ask Azure OpenAI to improve its decisions'.
ai_evidence_quote: "Design loops with human feedback and ask Azure OpenAI to improve its decisions"
artefacts:
  screenshot: 112_intelligent-routing-with-azure-openai.png
  archive: null
  bpmn_xml: 112_intelligent-routing-with-azure-openai.bpmn
duplicate_of: null
access: public
capture_source: bpmn-xml
capture_quality: legible
capture_width_px: 1100
capture_method: curl of the listing's own overview asset (d3bql97l1ytoxn.cloudfront.net, app_resources/444799/overview/img5705495903151401030-2x.png, 1100x515) and of the .bpmn the listing's Modeler import link points at (raw.githubusercontent.com/camunda/camunda-platform-tutorials/main/solutions/ai-intelligent-routing/Intelligent routing with Azure AI.bpmn); the image read natively at full size, the XML read directly
---

## What the page shows

A Camunda blueprint for intelligent routing with Azure OpenAI. The listing publishes the model twice over - as its overview screenshot and as a downloadable .bpmn - and the process routes an incoming customer inquiry through one Azure OpenAI task in front of four departmental work queues, with two escape events ('retry with feedback', 'route to different team') that send the case back for another attempt.

## Observations (description only, no interpretation)

- **AI activity - function:** the routing decision - 'Task Intelligence - Leverage process flows and decisions to route requests to the appropriate department or system'.
- **AI activity - element type:** one `serviceTask` bound to the Azure OpenAI connector element template (`io.camunda.connectors.AzureOpenAI.outbound.v1`, Zeebe type `io.camunda:http-json:1`); no agent element and no ad-hoc container.
- **Authority - downstream:** the four 'Work on inquiry' queues, chosen by the AI task's output through the gateway.
- **Authority - data:** the customer's inquiry text, entered in 'Enter inquiry (customer)'; no data objects are drawn.
- **Authority - control:** the gateway 'route to which department?' after the AI task, and the two escape paths back into the queue.
- **Authority - control (human):** the customer intake task and the four departmental 'Work on inquiry' tasks - every AI routing decision ends in a human queue.
- **Input provenance:** the inquiry the customer enters.
- **Guards present:** the two escape events ('retry with feedback', 'route to different team'), which the page frames as its human-feedback loop.
- **Prompt / model detail visible:** the page names the provider and the GPT-3/4 family; the XML names no model id or prompt - that configuration lives in the connector's own properties.

## Notes for the researcher

Correction to the batch-5 record, which said no .bpmn was downloadable: this listing does publish one, and it gives XML-grade proof of the binding. It also corrects a near-miss - the overview screenshot of this listing is byte-identical to n=016's (md5 c21428980bee), which looked like an E3 duplicate until the XML showed the two listings publish different models (Azure OpenAI here, OpenAI at n=016). Shared screenshot, different artefact: not a duplicate.
