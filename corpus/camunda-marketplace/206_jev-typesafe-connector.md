---
n: 206
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Jev (TypeSafe) Connector
url: https://marketplace.camunda.com/apps/871712/jev-typesafe-connector
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: A Camunda Modeler capture: none start event -> serviceTask 'Jev' (selected, the template applied) -> none end event, with the properties panel open: header 'JEV (TYPESAFE) / Jev', Documentation, Template 'Applied', Authentication, Payload (Model 'jev-latest', State '...'), and a 'Questions' field holding a JSON judgement schema. No .bpmn is downloadable.
bpmn_evidence_quote: "JEV (TYPESAFE)"
ai_evidence: The task binds a model ('jev-latest') and passes it a free-text input (a customer message) together with a structured question schema whose answer types are 'choice', 'score' and 'noun' (department routing with per-option criteria, a frustration score from 'Calm, just stating facts' to 'Very angry, strong language', an urgency question). The page: 'Use TypeSafe's Jev model to classify, score, or judge any piece of text or structured data, and get back reliable, structured answers your process can act on directly' and 'Route work, prioritize cases, or trigger reviews using Camunda gateway conditions instead of parsing free-form AI text'.
ai_evidence_quote: "Use TypeSafe's Jev model to classify, score, or judge any piece of text or structured data"
artefacts:
  screenshot: 206_jev-typesafe-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 812
capture_method: curl of the listing's own asset (d3bql97l1ytoxn.cloudfront.net, app_resources/871712/overview/image9123711561270603054-2x.png, 812x660); native read at full size - a Camunda Modeler canvas with the task's properties panel open
---

## What the page shows

The Jev (TypeSafe) Connector (community connector by maff). A single classification call in the process: a text or record goes to TypeSafe's Jev model together with a question schema, and the structured verdict comes back as process data for gateway conditions.

## Observations (description only, no interpretation)

- **AI activity - function:** classification/scoring - the model answers a schema of questions about the input ('department', 'frustration', 'is_urgent') whose answers are meant to drive routing.
- **AI activity - element type:** one serviceTask bound to the 'JEV (TYPESAFE)' element template; no agent element and no container.
- **Authority - downstream:** the answers are process variables; the page describes routing on 'Camunda gateway conditions instead of parsing free-form AI text', so the model's verdict is designed to steer the flow.
- **Authority - data:** the model receives a free-text customer message (the panel's State field holds an example message) plus the question schema with its own criteria text per answer option.
- **Authority - control:** no gateway is drawn in the capture; the page describes gateway conditions as the intended consumer of the answers.
- **Authority - control (human):** none drawn; a single task between start and end.
- **Input provenance:** a text field ('State') holding the message to be judged; no retrieval or context documents are shown.
- **Guards present:** none drawn in the model; the question schema's enumerated criteria and the 'score' type are the only structuring of the model's judgement.
- **Prompt / model detail visible:** visible - model 'jev-latest', the input text, and the full question schema including per-option criteria and the constraint that the urgency answer be a 'noun'.

## Notes for the researcher

Notably close to the corpus's AI-bound decisioning interest: the model is asked for structured, enumerated judgements rather than free text, and the page frames it explicitly as an alternative to parsing LLM prose. Same evidence class as n=097 and n=202 (binding visible in the properties panel).
