---
n: 175
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Mistral Connector
url: https://marketplace.camunda.com/apps/469787/mistral-connector
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: BPMN diagram published as the listing's own asset (Camunda Web Modeler, canvas with the selected task's properties panel open); no .bpmn downloadable. Read natively: start event -> serviceTask 'Ask Mistral anything' (selected, carrying the Mistral logo glyph and the connector's element-template marker) -> end event.
bpmn_evidence_quote: "Ask Mistral anything"
ai_evidence: The task is an LLM call, and the published properties panel shows its configuration: template 'MISTRAL' / 'Ask Mistral anything', Operation 'Text Generation', Model 'mistral-large-latest' ('ID of the model to use'), a Messages field holding the prompt ('Imagine Mistral and Camunda as the superheroes of your business processes, automating tasks and saving the day with their combined powers!'), Response Format 'Text' and a connection timeout. The page's own copy names the model family: 'Integrate Mistral, a state-of-the-art language model developed by Mistral AI, into business processes that are orchestrated and automated by Camunda'.
ai_evidence_quote: "Integrate Mistral, a state-of-the-art language model developed by Mistral AI, into business processes that are orchestrated and automated by Camunda"
artefacts:
  screenshot: 175_mistral-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own asset (d3bql97l1ytoxn.cloudfront.net, app_resources/469787/overview/img7982564004038865606-2x.png, 1100x632); native read at full size - a Camunda Web Modeler canvas with the task's properties panel open
---

## What the page shows

The Mistral Connector (Camunda Services GmbH, outbound connector). The listing publishes a minimal model - start, one Mistral text-generation service task, end - as the demonstration of how the connector is used inside a process, with the task's configuration visible in the panel.

## Observations (description only, no interpretation)

- **AI activity - function:** text generation by a hosted Mistral large language model.
- **AI activity - element type:** an ordinary `serviceTask` labelled 'Ask Mistral anything', bound to the vendor's connector template (Mistral logo glyph on the canvas); no agent element and no ad-hoc container.
- **Authority - downstream:** the end event - the published model has no branch after the model call.
- **Authority - data:** none drawn; the panel's Messages field carries the prompt and the response format is set to text.
- **Authority - control:** none - no gateway, so no drawn guard around the LLM call.
- **Authority - control (human):** none in the model.
- **Input provenance:** the prompt typed into the task's Messages field.
- **Guards present:** none drawn.
- **Prompt / model detail visible:** yes, unusually complete for a minimal model - model id 'mistral-large-latest', operation 'Text Generation', the prompt text itself, response format and connection timeout.

## Notes for the researcher

Minimal three-element model, but the AI element is fully visible in the published properties panel: model id, operation and the prompt. Recorded INCLUDE on the same basis as the other connector listings in this source whose template binding is shown.
