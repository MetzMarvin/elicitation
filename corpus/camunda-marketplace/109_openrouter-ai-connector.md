---
n: 109
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: OpenRouter AI Connector
url: https://marketplace.camunda.com/apps/643615/openrouter-ai-connector
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: BPMN diagram published as the listing's overview asset (Camunda Web Modeler, Implement tab); no .bpmn downloadable. Read natively: start event -> the single service task 'Free AI Agent' -> end event, with the task's properties panel open beside it. The only other published image is the connector's small app icon.
bpmn_evidence_quote: "Free AI Agent"
ai_evidence: The AI element is the process's only task, and its binding is visible in the published properties panel: template 'Free AI Agents Connector' with the description 'Execute AI-driven task completions using OpenRouter's Free diverse language models', a Model payload set to 'Llama Maverick', a Prompt reading 'explain Camunda 8 in one word?', and an OpenRouter API key as authentication. The page says 'Execute AI-driven task completion using OpenRouter's free diverse language models' and offers 'Unified access to multiple AI models - Call popular AI models such as OpenAI GPT, Meta Llama, Google Gemini, Mistral, and Qwen'.
ai_evidence_quote: "Execute AI-driven task completion using OpenRouter's free diverse language models"
artefacts:
  screenshot: 109_openrouter-ai-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1100
capture_method: curl of the listing's own overview asset (d3bql97l1ytoxn.cloudfront.net, overview/img9202337933599946560-2x.png, 1100x471); native read at full size - a Web Modeler screenshot with the task's properties panel open
---

## What the page shows

A community OpenRouter AI connector listing (Community, Camunda Connectors Bundle, 8.8/8.9, 'Execute AI-driven task completion'). The page presents a free-tier connector that calls models hosted by OpenRouter - GPT, Llama, Gemini, Mistral, Qwen - configured with the user's own API key through Camunda secrets, and its published artefact is a Web Modeler screenshot of that task configured with a model and a prompt.

## Observations (description only, no interpretation)

- **AI activity - function:** run a prompt against a language model and return the completion as the process result.
- **AI activity - element type:** one `serviceTask` bound to the 'Free AI Agents Connector' element template - an ordinary task, not an AI-agent or ad-hoc element.
- **Authority - downstream:** none - the task is the process's only activity between the start and end events, and nothing consumes or checks its output in the published model.
- **Authority - data:** the prompt text ('explain Camunda 8 in one word?') is the only input shown; no process variables are mapped in the visible panel.
- **Authority - control:** none - no gateway, no human review and no error path in the published model.
- **Input provenance:** a literal prompt typed into the task's properties, not a process variable.
- **Guards present:** none visible; the page's other stated feature is API-key handling through Camunda secrets.
- **Prompt / model detail visible:** both are visible - Model 'Llama Maverick', Prompt 'explain Camunda 8 in one word?'.

## Notes for the researcher

The published screenshot also shows an OpenRouter API-key value inside the authentication field - a credential the vendor exposed in its own listing image. It is recorded here as an observation only; the value is deliberately not reproduced in this record, and the capture is the vendor's own published asset, unmodified. The model configured ('Llama Maverick') is one of OpenRouter's free experimental models, so this is a prompt-in/answer-out AI task with no guardrails drawn around it.
