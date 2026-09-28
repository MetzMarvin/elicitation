---
n: 102
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: BPM AI Compose Connector
url: https://marketplace.camunda.com/apps/428849/bpm-ai-compose-connector
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: BPMN diagram published as the listing's overview asset (Camunda Web Modeler, Implement tab); no .bpmn downloadable. Read natively: an exclusive gateway 'Is English?' with a 'Yes' branch through 'Process Application' to 'Compose reply', and a 'No' branch through 'Translate Application'; 'Compose reply' feeds a mail step ('send mail') and the process ends at 'Application processed', with a second end state 'Invoice processed' at the top of the canvas.
bpmn_evidence_quote: "Compose reply"
ai_evidence: The AI element is the text-generation task 'Compose reply', bound to the BPM AI Compose Connector, and its generation settings are visible in the published properties panel: Type 'E-Mail/Letter', Style 'Formal', Tone 'Friendly', Language = `application.language`, Length 'Adequate', Variance 'None', and a template reading 'Dear {applicant}, {thank for the application} {communicate the decision on the application}'. The page states 'This Connector uses Large Language Models (LLMs) to generate content, ensures consistency in tone and style, and supports multiple languages' and that templates keep process variables 'without exposing them to the LLM'.
ai_evidence_quote: "This Connector uses Large Language Models (LLMs) to generate content, ensures consistency in tone and style, and supports multiple languages"
artefacts:
  screenshot: 102_bpm-ai-compose-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own overview asset (d3bql97l1ytoxn.cloudfront.net, overview/img4686213859023712455-2x.png, 856x660); native read at full size - the asset is a Web Modeler screenshot with the task's properties panel open
---

## What the page shows

holisticon's (CAMUNDA SERVICES GmbH) BPM AI Compose Connector listing (Partner, 8.4, 'Compose text with generative AI'). The page describes an outbound connector that writes emails, chat messages and other text with an LLM from input variables and templates, with adjustable tone, style, length and variance. Its published artefact is a Web Modeler screenshot of an application-handling process whose reply is composed by the connector.

## Observations (description only, no interpretation)

- **AI activity - function:** generate the text of a reply (e-mail/letter) from process variables and a template.
- **AI activity - element type:** an ordinary task bound to the BPM AI Compose Connector element template; the LLM parameters are set in the properties panel.
- **Authority - downstream:** the composed text feeds the mail step ('send mail', 'send mail'-annotated icons) and the process ends at 'Application processed'.
- **Authority - data:** the input variables `applicant` (application.name) and `decision` (userTaskResult.decision); the composed text leaves the process as an e-mail.
- **Authority - control:** the 'Is English?' gateway routes non-English applications to 'Translate Application' before composing; no review or approval gate is drawn around the generated text.
- **Authority - control (human):** the decision itself comes from a user task (userTaskResult.decision), so the human decides and the LLM only phrases it.
- **Input provenance:** the application (name) and the human decision; the template supplies the structure.
- **Guards present:** the template with variable placeholders, and the page's note that variables are not exposed to the LLM (an injection guard); Variance 'None' makes the output focused and deterministic.
- **Prompt / model detail visible:** the prompt template is visible as a property; the model id is not shown on this listing's screenshot.

## Notes for the researcher

The AI task here is downstream of a human decision - the user task supplies `decision` and the LLM renders it - which makes this listing a useful counterpart to the extraction connector (n=097) from the same vendor. The page's template feature is explicitly an injection guard ('without exposing them to the LLM'), visible in the properties panel as the template field.
