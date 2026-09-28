---
n: 218
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Amazon Bedrock Connector
url: https://marketplace.camunda.com/apps/449589/amazon-bedrock-connector
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: A complete published process, drawn on a Modeler canvas: start event 'Customer Query Submission' -> serviceTask 'AI Query Analysis' (violet AI glyph) -> serviceTask 'AI Response Generation' (violet AI glyph) -> userTask 'Human Agent Escalation' (human glyph) -> userTask 'Customer Feedback Collection' (human glyph) -> serviceTask 'Process Improvement' (violet AI glyph) -> end event 'Process Complete'. Five tasks in a single end-to-end path, three of them carrying the AI glyph and two the human one.
bpmn_evidence_quote: "AI Response Generation"
ai_evidence: The connector is the AWS Bedrock outbound connector (vendor Camunda, open source, 8.6, categories 'AI Services' and 'Agentic AI orchestration') and every non-human task in the figure is AI-bound. The page states it two ways: the heading 'Integrate Leading AI Models Into Processes' and the 'Converse' feature - 'Bring a conversational agent into your business processes, using any model available on Amazon Bedrock' - alongside an 'Invoke Model' feature for 'a custom request to any model that is available on Amazon Bedrock'. A second published image is the template's own violet agent icon (197x186).
ai_evidence_quote: "Bring a conversational agent into your business processes, using any model available on Amazon Bedrock."
artefacts:
  screenshot: 218_amazon-bedrock-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: listing-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own assets (d3bql97l1ytoxn.cloudfront.net, app_resources/830622/overview/img1518293777993457878-2x.png, 1100x395, plus the 197x186 template icon img6171336492150799519-2x.png), both read natively at full size
---

## What the page shows

The Amazon Bedrock Connector (Camunda, open source, 8.6). Any Bedrock-hosted model as a Camunda connector task, shown here in a published customer-support process where the query is analysed and answered by AI, escalated to a human when needed, and the feedback folded back into a 'Process Improvement' task.

## Observations (description only, no interpretation)

- **AI activity - function:** analyse the incoming customer query, generate the response, and - after the human escalation and feedback steps - improve the process from that feedback.
- **AI activity - element type:** serviceTasks (connector tasks bound to the Bedrock element template, whose own icon is published as a separate image); the human steps are userTasks with the human glyph.
- **AI activity - models named:** none in the figure or the page beyond 'any model available on Amazon Bedrock' - the model choice is delegated to the connector configuration, which the listing does not show.
- **Authority - downstream:** the AI-generated response is what the human agent is handed for escalation, and the 'Process Improvement' task writes back into the process - a self-modifying loop rather than a one-shot answer.
- **Authority - control:** the only control visible is the human escalation task ('Human Agent Escalation') and the feedback collection task; no gateway, threshold or validation task appears on the published path.
- **Data reachable by the model:** the customer query as submitted; the page's 'Invoke Model' operation leaves the request body to the modeler.
- **Human role:** 'Human Agent Escalation' (intervene when the AI answer is not enough) and 'Customer Feedback Collection' (the input to the improvement step).

## Notes for the researcher

A connector listing that publishes a *complete* process rather than a template panel - and the published process is a loop: AI answers, a human escalates, feedback feeds a further AI task called 'Process Improvement'. Note the listing never names a model; the bedrock model id lives in the unmapped connector properties, so the record can only say which family of models is reachable, not which one runs. The figure's violet glyph is the same AI-element glyph anchored at n=198 (figs/198).
