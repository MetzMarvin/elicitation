---
n: 100
source: cib-seven
source_name: CIB seven manual (docs.cibseven.org, /manual/latest/ pinned)
source_type: vendor documentation
title: Retrieval-Augmented Generation (RAG)
url: https://docs.cibseven.org/manual/latest/reference/connect/ai-agent-connector/rag/
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: Same question as the examples page: this is the connector XML of a knowledge-ingestor service task, published without the enclosing <bpmn:serviceTask>. Collected as a process artefact or not?
needs_visual_check: false
bpmn_evidence: "the page publishes the BPMN extension-element XML of the service task that ingests documents into the knowledge base: <camunda:connector> with <camunda:connectorId>cibseven-knowledge-ingestor</camunda:connectorId>, input parameters content=${documentText}, source=${documentSource}, pgHost, pgDatabase, pgUser and output parameter ingestedChunks=${chunksIngested}. Same shape as the examples page: connector XML without the enclosing <bpmn:serviceTask>. Copied verbatim into the .bpmn capture next to this record."
bpmn_evidence_quote: "camunda:connectorId>cibseven-knowledge-ingestor</camunda:connectorId>"
ai_evidence: "the AI element is the knowledge-ingestor connector inside the process: it is the retrieval step that feeds the agent, configured (content, chunking, embedding) inside a service task."
ai_evidence_quote: "inputParameter name='content'>${documentText} (cibseven-knowledge-ingestor connector configuration)"
artefacts:
  screenshot: null
  archive: null
  bpmn_xml: 100_ai-agent-connector-rag.bpmn
duplicate_of: null
access: public
capture_source: page asset from docs.cibseven.org (same-origin)
capture_quality: legible
capture_width_px: null
capture_method: plain GET of the page asset (ledgers/cib-seven.raw/img/), or the page's own XML block copied verbatim
---

## What the page shows

Verbatim from the page:

> "<camunda:connector> <camunda:connectorId>cibseven-knowledge-ingestor</camunda:connectorId> ... <camunda:inputParameter name=\"content\">${documentText}</camunda:inputParameter>"

## Artefact reading (native resolution unless stated)

- **BPMN:** the page publishes the BPMN extension-element XML of the service task that ingests documents into the knowledge base: <camunda:connector> with <camunda:connectorId>cibseven-knowledge-ingestor</camunda:connectorId>, input parameters content=${documentText}, source=${documentSource}, pgHost, pgDatabase, pgUser and output parameter ingestedChunks=${chunksIngested}. Same shape as the examples page: connector XML without the enclosing <bpmn:serviceTask>. Copied verbatim into the .bpmn capture next to this record.
- **AI element:** the AI element is the knowledge-ingestor connector inside the process: it is the retrieval step that feeds the agent, configured (content, chunking, embedding) inside a service task.

## BPMN XML published on the page (verbatim capture)

```xml
<camunda:connector>
  <camunda:connectorId>cibseven-knowledge-ingestor</camunda:connectorId>
  <camunda:inputOutput>
    <camunda:inputParameter name="content">${documentText}</camunda:inputParameter>
    <camunda:inputParameter name="source">${documentSource}</camunda:inputParameter>
    <camunda:inputParameter name="pgHost">localhost</camunda:inputParameter>
    <camunda:inputParameter name="pgDatabase">postgres</camunda:inputParameter>
    <camunda:inputParameter name="pgUser">my_user</camunda:inputParameter>
    <camunda:inputParameter name="pgPassword">${pgPassword}</camunda:inputParameter>
    <camunda:outputParameter name="ingestedChunks">${chunksIngested}</camunda:outputParameter>
  </camunda:inputOutput>
</camunda:connector>
```
