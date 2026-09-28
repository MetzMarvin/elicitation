---
n: 96
source: cib-seven
source_name: CIB seven manual (docs.cibseven.org, /manual/latest/ pinned)
source_type: vendor documentation
title: Examples & Tutorials
url: https://docs.cibseven.org/manual/latest/reference/connect/ai-agent-connector/examples/
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: This page prints the <camunda:connector> extension-element XML of four AI-agent service tasks but not the enclosing <bpmn:serviceTask> element that the getting-started page prints. Does a connector-configuration fragment count as a collected process artefact, or does only the full BPMN element count?
needs_visual_check: false
bpmn_evidence: "the page publishes four XML blocks, each the <camunda:connector> / <camunda:inputOutput> extension-element configuration of one AI-agent service task (agentName InvoiceExtractor; McpAgent with mcpServers; Orchestrator with toolClasses ...ProcessStarterTool; and a chat-memory variant with useChatMemory/memoryId). The blocks are BPMN extension elements, but the page prints them as fragments: it does not show the enclosing <bpmn:serviceTask> element that the getting-started page shows. Copied verbatim into the .bpmn capture next to this record."
bpmn_evidence_quote: "camunda:inputParameter name='agentName'>InvoiceExtractor</camunda:inputParameter>"
ai_evidence: "the AI elements are inside the process configuration: four configured agents (invoice extraction with a JSON output schema, an MCP-server agent, an orchestrator that starts another process as a tool, and an agent with chat memory)."
ai_evidence_quote: "inputParameter name='agentName'>McpAgent ... inputParameter name='mcpServers'>[{'name': 'engine', 'url': 'http://localhost:8080/mcp'}]"
artefacts:
  screenshot: null
  archive: null
  bpmn_xml: 096_ai-agent-connector-examples.bpmn
duplicate_of: null
access: public
capture_source: page asset from docs.cibseven.org (same-origin)
capture_quality: legible
capture_width_px: null
capture_method: plain GET of the page asset (ledgers/cib-seven.raw/img/), or the page's own XML block copied verbatim
---

## What the page shows

Verbatim from the page:

> "<camunda:inputParameter name=\"agentName\">InvoiceExtractor</camunda:inputParameter> <camunda:inputParameter name=\"instruction\">Extract the invoice as JSON..."

## Artefact reading (native resolution unless stated)

- **BPMN:** the page publishes four XML blocks, each the <camunda:connector> / <camunda:inputOutput> extension-element configuration of one AI-agent service task (agentName InvoiceExtractor; McpAgent with mcpServers; Orchestrator with toolClasses ...ProcessStarterTool; and a chat-memory variant with useChatMemory/memoryId). The blocks are BPMN extension elements, but the page prints them as fragments: it does not show the enclosing <bpmn:serviceTask> element that the getting-started page shows. Copied verbatim into the .bpmn capture next to this record.
- **AI element:** the AI elements are inside the process configuration: four configured agents (invoice extraction with a JSON output schema, an MCP-server agent, an orchestrator that starts another process as a tool, and an agent with chat memory).

## BPMN XML published on the page (verbatim capture)

```xml
<!-- example 1: the extensionElements XML of one AI Agent service task -->
<camunda:inputParameter name="agentName">InvoiceExtractor</camunda:inputParameter>
<camunda:inputParameter name="instruction">Extract the invoice as JSON: {"invoiceNumber": string, "total": number, "currency": string, "dueDate": string}. Use null for unknown fields.</camunda:inputParameter>
<camunda:inputParameter name="message">${invoiceText}</camunda:inputParameter>
<camunda:outputParameter name="invoiceJson">${output}</camunda:outputParameter>

<!-- example 2: the extensionElements XML of one AI Agent service task -->
<camunda:inputParameter name="agentName">McpAgent</camunda:inputParameter>
<camunda:inputParameter name="message">${userMessage}</camunda:inputParameter>
<camunda:inputParameter name="mcpServers">[{"name": "engine", "url": "http://localhost:8080/mcp"}]</camunda:inputParameter>
<camunda:outputParameter name="agentOutput">${output}</camunda:outputParameter>
<camunda:outputParameter name="agentOutput_aiMeta">${outputAiMeta}</camunda:outputParameter>

<!-- example 3: the extensionElements XML of one AI Agent service task -->
<camunda:inputParameter name="agentName">Orchestrator</camunda:inputParameter>
<camunda:inputParameter name="toolClasses">org.cibseven.connect.ai.agent.impl.ProcessStarterTool</camunda:inputParameter>
<camunda:inputParameter name="message">Start the process "process-as-a-tool" and read its output variables whose names start with "out_".</camunda:inputParameter>
<camunda:outputParameter name="agentOutput">${output}</camunda:outputParameter>

<!-- example 4: the extensionElements XML of one AI Agent service task -->
<camunda:inputParameter name="useChatMemory">${true}</camunda:inputParameter>
<camunda:inputParameter name="memoryId">${execution.getVariable('memoryId')}</camunda:inputParameter>
<camunda:inputParameter name="message">${feedback}</camunda:inputParameter>
<camunda:outputParameter name="agentOutput">${output}</camunda:outputParameter>
<camunda:outputParameter name="memoryId">${memoryId}</camunda:outputParameter>
```
