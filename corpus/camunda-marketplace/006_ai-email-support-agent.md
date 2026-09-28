---
n: 6
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: AI Email Support Agent
url: https://marketplace.camunda.com/apps/522492/ai-email-support-agent
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: Decisive: the listing publishes its .bpmn (imported through modeler.cloud.camunda.io). Process 'Agent Blueprint (Long Term Memory)' with an `adHocSubProcess` 'Handle customer request' and a `serviceTask` 'Agent as a Judge'.
bpmn_evidence_quote: "<bpmn:adHocSubProcess ... name="Handle customer request""
ai_evidence: Two AI element-template bindings inside the process: the ad-hoc sub-process 'Handle customer request' carries `zeebe:modelerTemplate="io.camunda.connectors.agenticai.aiagent.jobworker.v1"` (`zeebe:taskDefinition type="io.camunda.agenticai:aiagent-job-worker:1"`), and the service task 'Agent as a Judge' carries `zeebe:modelerTemplate="io.camunda.connectors.agenticai.aiagent.v1"` (`type="io.camunda.agenticai:aiagent:1"`). Four more tasks bind `io.camunda.connectors.EmbeddingsVectorDB.v1`.
ai_evidence_quote: "zeebe:modelerTemplate="io.camunda.connectors.agenticai.aiagent.v1""
artefacts:
  screenshot: 006_ai-email-support-agent.png
  archive: null
  bpmn_xml: 006_ai-email-support-agent.bpmn
duplicate_of: null
access: public
capture_source: bpmn-xml
capture_quality: legible
capture_width_px: null
capture_method: curl of the raw.githubusercontent.com .bpmn the listing's Modeler import link points at; XML read directly
---

## What the page shows

An AI email support loop. The page describes it as orchestrating 'an AI-driven email conversation in Camunda 8.8-alpha4' over the generic Camunda email connector, drafting replies with an AI agent and enriching them from a vector database. The XML shows the agent as an ad-hoc sub-process 'Handle customer request' whose tools are email and vector-database tasks, a separate 'Agent as a Judge' service task on the main path, knowledge-base read/write tasks, a user task 'Ask loan specialist', a sub-process 'Human controlled request' and a user task 'Finalize case manually'.

## Observations (description only, no interpretation)

- **AI activity - function:** the page says the AI agent drafts replies 'enriched with short-term variables and long-term memory chunks from the Camunda Vector Database Connector', with 'BPMN-defined guardrails around token use, sentiment, or other criteria'.
- **AI activity - element type:** an AI-agent `adHocSubProcess` (job-worker binding) plus a second AI-agent `serviceTask` ('Agent as a Judge'); the agent's tools are ordinary service tasks bound to the email and vector-database connectors.
- **Authority - downstream:** 'Final answer to customer and close support' (email connector), the user tasks 'Handle customer request', 'Review case resolution', 'Finalize case manually', and the gateway after 'Agent as a Judge' that routes to 'Finalize case manually'.
- **Authority - data:** the vector database (EmbeddingsVectorDB tasks 'Save answer in knowledge base', 'Query knowledge base', 'Save customer interaction in long term memory', 'Fetch past conversations from customer').
- **Authority - control:** the exclusive gateways around 'Agent as a Judge' and the 'Agent solved?' decision; the human sub-process 'Human controlled request'.
- **Input provenance:** the inbound email connector (`io.camunda.connectors.inbound.EmailMessageStart.v1` / `inbound.EmailIntermediate.v1`) - the customer's email body.
- **Guards present:** an explicit judging agent ('Agent as a Judge'), human escalation tasks, and the page's mention of 'BPMN-defined guardrails around token use, sentiment, or other criteria'.
- **Prompt / model detail visible:** the page names the agent framework ('LangChain 4j'); the XML carries element-template bindings and task names but no prompt text or model id.

## Notes for the researcher

Page version note: 'Camunda 8.8-alpha4'. The 'Agent as a Judge' service task is the reference that anchors the four-pointed-star glyph used to identify AI-agent elements in this source's figure-only listings (see the n=022 record).
