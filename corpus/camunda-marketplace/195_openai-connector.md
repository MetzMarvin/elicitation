---
n: 195
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: OpenAI Connector
url: https://marketplace.camunda.com/apps/415542/openai-connector
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: A published process diagram: none start event -> serviceTask 'ask ChatGPT anything' -> serviceTask 'Use the moderation api' -> none end event, both tasks carrying the OpenAI connector glyph. No .bpmn is downloadable; the diagram is the listing's overview asset.
bpmn_evidence_quote: "ask ChatGPT anything"
ai_evidence: Both tasks in the published process are ChatGPT calls: 'ask ChatGPT anything' and 'Use the moderation api'. The page states the binding in its own words - 'Bring generative AI into business processes that are orchestrated by Camunda by sending natural language input to ChatGPT. Use OpenAI's Moderation API to screen inputs.' - and lists the features 'ChatGPT Integration' and 'Moderator API Integration'. The listing carries the tags 'AI Services' and 'Agentic AI orchestration'.
ai_evidence_quote: "Bring generative AI into business processes that are orchestrated by Camunda by sending natural language input to ChatGPT"
artefacts:
  screenshot: 195_openai-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1100
capture_method: curl of the listing's own asset (d3bql97l1ytoxn.cloudfront.net, app_resources/415542/overview/img5790612535366289591-2x.png, 1100x579); native read at full size - a Camunda-branded process diagram
---

## What the page shows

The OpenAI Connector (Camunda Services GmbH, out-of-the-box outbound connector, connectors bundle). Two LLM calls in a row: a chat/completion request and an input screening call against OpenAI's moderation endpoint.

## Observations (description only, no interpretation)

- **AI activity - function:** generation and moderation - the process sends natural-language input to ChatGPT, then screens it with OpenAI's Moderation API.
- **AI activity - element type:** two serviceTasks, each bound to the OpenAI connector's element template (the OpenAI glyph is drawn on both tasks); no agent element and no ad-hoc container.
- **Authority - downstream:** none drawn beyond the second call; the process ends after the moderation step.
- **Authority - data:** not shown - the diagram has no data objects and the connector's payload is not visible.
- **Authority - control:** none - no gateway, no branch, no threshold anywhere in the published model.
- **Authority - control (human):** none drawn; the model is fully automated from start to end event.
- **Input provenance:** not shown (a single start event).
- **Guards present:** none shown; the moderation call is the only screening step, and the page describes it as input screening rather than as a gate.
- **Prompt / model detail visible:** none - no model name, prompt or temperature is published; the page's demo is a Vimeo link that was not opened.

## Notes for the researcher

Minimal but unambiguous: a three-element process whose only two tasks are the LLM call and the moderation call, with the binding named in the page text. Same shape as the Amazon Textract connector (n=132) and the Azure OpenAI routing blueprint (n=112).
