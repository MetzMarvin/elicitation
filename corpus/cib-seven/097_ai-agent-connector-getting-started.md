---
n: 97
source: cib-seven
source_name: CIB seven manual (docs.cibseven.org, /manual/latest/ pinned)
source_type: vendor documentation
title: Getting Started
url: https://docs.cibseven.org/manual/latest/reference/connect/ai-agent-connector/getting-started/
accessed: 2026-09-25
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "the page publishes the BPMN 2.0 XML of a service task bound to the AI Agent connector: <bpmn:serviceTask id='Task_Summarize' name='Summarize feedback' camunda:modelerTemplate='org.cibseven.connect.ai.agent' camunda:modelerTemplateVersion='1' implementation='##WebService'> with <bpmn:extensionElements><camunda:connector> and <camunda:connectorId>cibseven-ai-agent</camunda:connectorId>. The XML is the page's own published artefact, copied verbatim into the .bpmn capture next to this record."
bpmn_evidence_quote: "bpmn:serviceTask id='Task_Summarize' name='Summarize feedback' camunda:modelerTemplate='org.cibseven.connect.ai.agent'"
ai_evidence: "the AI element is inside the process: the service task is bound to the AI Agent connector (cibseven-ai-agent) and carries the agent parameters agentName=Summarizer, instruction 'Summarize the core concern in 10 words or less.', apiKey and the output parameter summaryResult."
ai_evidence_quote: "camunda:connectorId>cibseven-ai-agent / inputParameter name='agentName'>Summarizer / instruction>Summarize the core concern in 10 words or less."
artefacts:
  screenshot: null
  archive: null
  bpmn_xml: 097_ai-agent-connector-getting-started.bpmn
duplicate_of: null
access: public
capture_source: page asset from docs.cibseven.org (same-origin)
capture_quality: legible
capture_width_px: null
capture_method: plain GET of the page asset (ledgers/cib-seven.raw/img/), or the page's own XML block copied verbatim
---

## What the page shows

Verbatim from the page:

> "<bpmn:serviceTask id=\"Task_Summarize\" name=\"Summarize feedback\" camunda:modelerTemplate=\"org.cibseven.connect.ai.agent\" ...> ... <camunda:connectorId>cibseven-ai-agent</camunda:connectorId>"

## Artefact reading (native resolution unless stated)

- **BPMN:** the page publishes the BPMN 2.0 XML of a service task bound to the AI Agent connector: <bpmn:serviceTask id="Task_Summarize" name="Summarize feedback" camunda:modelerTemplate="org.cibseven.connect.ai.agent" camunda:modelerTemplateVersion="1" implementation="##WebService"> with <bpmn:extensionElements><camunda:connector> and <camunda:connectorId>cibseven-ai-agent</camunda:connectorId>. The XML is the page's own published artefact, copied verbatim into the .bpmn capture next to this record.
- **AI element:** the AI element is inside the process: the service task is bound to the AI Agent connector (cibseven-ai-agent) and carries the agent parameters agentName=Summarizer, instruction "Summarize the core concern in 10 words or less.", apiKey and the output parameter summaryResult.

## BPMN XML published on the page (verbatim capture)

```xml
<bpmn:serviceTask id="Task_Summarize" name="Summarize feedback"
 camunda:modelerTemplate="org.cibseven.connect.ai.agent"
 camunda:modelerTemplateVersion="1"
 implementation="##WebService">
 <bpmn:extensionElements>
 <camunda:connector>
 <camunda:inputOutput>
 <camunda:inputParameter name="agentName">Summarizer</camunda:inputParameter>
 <camunda:inputParameter name="message">Summarize: ${feedbackText}</camunda:inputParameter>
 <camunda:inputParameter name="instruction">Summarize the core concern in 10 words or less.</camunda:inputParameter>
 <camunda:inputParameter name="apiKey">${apiKey}</camunda:inputParameter>
 <camunda:outputParameter name="summaryResult">${output}</camunda:outputParameter>
 </camunda:inputOutput>
 <camunda:connectorId>cibseven-ai-agent</camunda:connectorId>
 </camunda:connector>
 </bpmn:extensionElements>
</bpmn:serviceTask>
```

## Notes for the researcher

There is no diagram on this page: the collectible artefact is the published BPMN XML itself, which is why the capture is a .bpmn file rather than a screenshot.
