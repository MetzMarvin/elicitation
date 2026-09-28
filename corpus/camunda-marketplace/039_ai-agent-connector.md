---
n: 39
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: AI Agent Connector
url: https://marketplace.camunda.com/apps/522488/ai-agent-connector
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: BPMN diagram published as the listing's own screenshots, drawn with Camunda's element glyphs: start event -> exclusive gateway -> service task 'AI Agent Task' -> exclusive gateway 'Needs to call tools?' -> end event, with a 'Call tools' branch into an expanded sub-process 'Tools' (ad-hoc: tilde marker) holding 'Tool A' (-> message catch event 'Wait for message') and a 'User Task'; the path 'Tool call results' returns to the first gateway.
bpmn_evidence_quote: "Needs to call tools?"
ai_evidence: The service task 'AI Agent Task' carries the violet four-pointed-star element-template glyph (Camunda's agentic-AI connector template). The second published diagram shows the same pattern at process level: an expanded sub-process 'AI Agent' carrying that glyph and the ad-hoc marker, whose tools are 'Load user details', 'Load previous orders', 'Categorize input' (OpenAI glyph) and, in a dotted ad-hoc block, a message event -> 'Slack Team' (Slack glyph). The page states the model choice is the user's: 'Connect to various AI service providers including Anthropic, AWS Bedrock, Azure OpenAI, Google Vertex AI, OpenAI'.
ai_evidence_quote: "Empower AI agents with access to tools modeled as BPMN elements within an ad-hoc sub-process."
artefacts:
  screenshot: 039_ai-agent-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own screenshot (d3bql97l1ytoxn.cloudfront.net, screenshot/img4493780933607340061.png, 1500x853); native read at full size, and the overview asset (1100x538) read separately as the second diagram
---

## What the page shows

Camunda's own AI Agent Connector listing (Camunda Connectors Bundle, 8.8/8.9). The page explains that 'Camunda orchestrates AI agents, ensures their work is transparent' and that the connector adds agents to processes with multi-provider support, tool calling, customizable prompts, response formatting and event handling. Its two published diagrams are the two ways the agent is modelled: a service task that the process calls and loops back into while the agent asks for tools, and an expanded AI-agent sub-process whose tools are BPMN elements inside it.

## Observations (description only, no interpretation)

- **AI activity - function:** run an AI agent as a step of the process and let it call tools until it no longer needs them.
- **AI activity - element type:** a `serviceTask` ('AI Agent Task') bound to the agentic-AI element template, and an expanded ad-hoc sub-process ('AI Agent') that carries the same template; tools are ordinary BPMN elements inside the sub-process.
- **Authority - downstream:** the 'Needs to call tools?' gateway decides between ending the process and re-entering the tools sub-process; 'Tool call results' feeds the agent's result back.
- **Authority - data:** the tools are the data access ('Load user details', 'Load previous orders'); no data objects or variable bindings are visible.
- **Authority - control:** the two exclusive gateways and the ad-hoc sub-process boundary are the visible controls; a human step appears only as a tool ('User Task') the agent may call, not as a reviewer of the agent's output.
- **Input provenance:** the process start event (unspecified in the diagram); the tools supply the agent's context.
- **Guards present:** the page's features name 'Customizable prompts', 'Response formatting' and 'Event handling'; the diagrams show a tool loop rather than a guard on the agent's output.
- **Prompt / model detail visible:** no prompt text or model id in the artefacts; the page lists the supported providers and links the agentic-ai-aiagent documentation.

## Notes for the researcher

Two distinct diagrams are published (a 1500x853 and its 750x427 1x version of the tool-loop process, plus a 1100x538 overview showing the expanded 'AI Agent' container); the capture here is the tool-loop process at full size, and the container diagram is described above from the overview asset (raw/figs/039/asset_img3413129807889304746-2x.png). The violet star on 'AI Agent Task' is one of the anchors used to read that glyph elsewhere in this source.
