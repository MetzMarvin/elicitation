---
n: 135
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Google Gemini Connector
url: https://marketplace.camunda.com/apps/477727/google-gemini-connector
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: BPMN diagram published as the listing's own asset (Camunda Web Modeler, Implement view); no .bpmn downloadable. Read natively: start event 'Start' -> one service task -> end event 'End'.
bpmn_evidence_quote: "Ask Google Gemini anything"
ai_evidence: The process's only task is the Gemini call, labelled 'Ask Google Gemini anything' and carrying Gemini's four-pointed-star glyph. The page's own copy states the integration directly: 'The Google Gemini connector enables seamless interaction between Camunda-powered business processes and Gemini so you can integrate AI into automated processes'.
ai_evidence_quote: "The Google Gemini connector enables seamless interaction between Camunda-powered business processes and Gemini so you can integrate AI into automated processes"
artefacts:
  screenshot: 135_google-gemini-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own asset (d3bql97l1ytoxn.cloudfront.net, app_resources/477727/overview/img3590724590501131737-2x.png, 1031x660); native read at full size - a Camunda Web Modeler Implement view
---

## What the page shows

The Google Gemini Connector (Camunda Services GmbH, outbound connector). The listing publishes a minimal Web Modeler model - start event, the Gemini service task, end event - plus the connector's element template; the page describes conversational and generative AI use in processes ('Enable Gemini Interactions', 'Enable real-time, text-based interactions with Gemini').

## Observations (description only, no interpretation)

- **AI activity - function:** a real-time conversational call to Google Gemini from inside the process.
- **AI activity - element type:** an ordinary `serviceTask` carrying Gemini's star glyph and the connector's element-template binding; no agent element and no ad-hoc container.
- **Authority - downstream:** the end event 'End'; the published model has no branch after the AI call.
- **Authority - data:** none drawn.
- **Authority - control:** none - no gateway, so no drawn guard around the model call.
- **Authority - control (human):** none in the model; the page's feature list describes enablement and interaction steps but no human review.
- **Input provenance:** the prompt supplied to the connector task.
- **Guards present:** none drawn.
- **Prompt / model detail visible:** none in the published model; the page names Gemini (formerly Bard) and its conversational/generative capability but no model version.

## Notes for the researcher

One of the three Camunda Services connector listings in this batch whose published model is the connector-under-test in its minimal form (see n=132, n=131). The AI element is inside the process and the page names the service, so it meets the criteria; the artefact carries no control structure around the AI call.
