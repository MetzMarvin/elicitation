---
n: 215
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Cohere Connector
url: https://marketplace.camunda.com/apps/836162/cohere-connector
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: A Web Modeler canvas with the element-template panel open: start event 'Feedback received' -> serviceTask 'Classify feedback' (selected, violet glyph) -> exclusiveGateway 'What kind of feedback?' -> 'Find relevant help articles' and 'Extract severity and summary' (both with the violet glyph) -> 'Draft grounded answer' -> gateways ('complaint', 'praise' labelled flows) -> end event 'Feedback handed'. The panel is the COHERE template: 'Cohere API key' bound to {{secrets.COHERE_API_KEY}}, Model 'Command R7B (fast, low cost)', 'Text to classify' = customerMessage, 'Allowed labels' = ["complaint", "question", "praise"], and the template's operation list ('Chat: ask Cohere', 'Chat: structured JSON output', 'Classify: label a text', 'Embeddings: embed texts', 'Rerank rank documents by relevance', 'Utility: list available models').
bpmn_evidence_quote: "Classify feedback"
ai_evidence: Every task in the published process is a Cohere model call: classification ('Classify feedback', labels ["complaint", "question", "praise"]), retrieval support ('Find relevant help articles'), extraction ('Extract severity and summary') and generation ('Draft grounded answer'). The page describes the connector as an element template on the native REST connector that can 'ask a model for an answer, force a schema-conformant JSON response, classify a text into your own labels for routing decisions', 'embed texts for semantic search', and 'rerank retrieved documents by relevance before an AI agent or a human sees them', with a 'Classify text for routing' feature whose output is enforced through a structured-output enum at temperature 0.
ai_evidence_quote: "ask a model for an answer, force a schema-conformant JSON response, classify a text into your own labels for routing decisions"
artefacts:
  screenshot: 215_cohere-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: listing-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own asset (d3bql97l1ytoxn.cloudfront.net, app_resources/836162/overview/img8033399267167366938-2x.png, 1100x518), read natively at full size
---

## What the page shows

The Cohere Connector (community listing, 8.8-8.10). Cohere's chat, structured-output, classification, embedding and rerank operations as a Camunda element template on the built-in REST connector; the published process routes customer feedback by an LLM label, retrieves help articles, summarises severity and drafts a grounded answer, ending in a human 'Feedback handed' step.

## Observations (description only, no interpretation)

- **AI activity - function:** classify the feedback into one of three allowed labels, find relevant help articles, extract severity and summary, and draft the answer text.
- **AI activity - element type:** serviceTasks bound to the COHERE element template (panel header 'COHERE' with a 'Template / Applied' indicator showing six operations), on top of the native REST connector.
- **AI activity - model named:** 'Command R7B (fast, low cost)' in the Model field, with a custom-model field available and a 'Utility: list available models' operation; the API key comes from a Camunda secret, {{secrets.COHERE_API_KEY}}.
- **Authority - downstream:** the gateway condition reads the label ('What kind of feedback?' with complaint / question / praise branches), and 'Draft grounded answer' consumes the retrieved articles - i.e. the model decides the route and writes the customer-facing text.
- **Authority - control:** the allowed-labels list with structured output at temperature 0 (the page: 'get back exactly one, enforced through a structured-output enum at temperature 0, so a gateway condition such as cohereLabel = "approve" just works'); a schema-conformant JSON guarantee for downstream automation.
- **Cost/token observability:** chat operations map Cohere's billed token counts into a process variable for Camunda Optimize reports.
- **Data reachable by the model:** the raw customer feedback message plus whatever retrieval hits are passed in for reranking; secrets stay in the cluster, no custom runtime.
- **Human role:** the end event 'Feedback handed' after the drafted answer - the human is the recipient, not a reviewer of the label.

## Notes for the researcher

The clearest routing-by-LLM example in this source: the model's label *is* the gateway condition, and the element template constrains the answer set to three strings, so the branching is only as reliable as the enum. Note the vendor ships the same task as an element template over Camunda's own REST connector, i.e. no separate runtime - and lists token accounting as a feature, which is unusual in this corpus.
