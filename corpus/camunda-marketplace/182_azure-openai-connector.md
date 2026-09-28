---
n: 182
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Azure OpenAI Connector
url: https://marketplace.camunda.com/apps/439558/azure-openai-connector
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: BPMN diagram published as the listing's own asset (Camunda Web Modeler, canvas with palette, autosaved); no .bpmn downloadable. Read natively: start event -> serviceTask 'call GPT-3.5' (carrying the connector's element-template glyph) -> end event.
bpmn_evidence_quote: "call GPT-3.5"
ai_evidence: The task's own label names the model it calls: 'call GPT-3.5'. The page names the provider and the models: 'The Azure OpenAI Connector offers a powerful, user-friendly solution for integrating advanced AI capabilities directly into Camunda processes', and its feature list says 'Utilize any Azure OpenAI model, such as GPT-3.5, Codex, or DALL-E, within Camunda processes'.
ai_evidence_quote: "Utilize any Azure OpenAI model, such as GPT-3.5, Codex, or DALL-E, within Camunda processes"
artefacts:
  screenshot: 182_azure-openai-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own asset (d3bql97l1ytoxn.cloudfront.net, app_resources/439558/overview/img6708534234637972493-2x.png, 1100x514); native read at full size - a Camunda Web Modeler canvas
---

## What the page shows

The Azure OpenAI Connector (Camunda Services GmbH, outbound connector). The listing publishes a minimal model - start, the GPT call, end - as the demonstration of how the connector is used inside a process.

## Observations (description only, no interpretation)

- **AI activity - function:** a call to an Azure OpenAI model (the task is labelled 'call GPT-3.5').
- **AI activity - element type:** an ordinary `serviceTask` bound to the vendor's connector template; no agent element and no ad-hoc container.
- **Authority - downstream:** the end event - the published model has no branch after the model call.
- **Authority - data:** none drawn.
- **Authority - control:** none - no gateway in the published model.
- **Authority - control (human):** none in the model.
- **Input provenance:** the prompt or payload configured in the connector task.
- **Guards present:** none drawn.
- **Prompt / model detail visible:** the model family is in the element's own label ('call GPT-3.5'); no prompt, temperature or deployment is visible in the published canvas.

## Notes for the researcher

Minimal three-element connector model, included on the strength of the element's own label plus the page's model list. Together with n=175 (Mistral), n=177 (Perplexity), n=178 (Glean) and n=162 (UiPath), this batch shows the connector-listing pattern in this source: a start event, the AI-bound task, an end event, and no drawn control around the AI call.
