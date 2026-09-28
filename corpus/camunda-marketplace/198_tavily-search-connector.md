---
n: 198
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Tavily Search Connector
url: https://marketplace.camunda.com/apps/541302/tavily-search-connector
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: A published process diagram: message start event 'Received message on slack' -> exclusiveGateway -> serviceTask 'Agent' -> exclusiveGateway 'action needed?' -> serviceTask 'Reply on Slack thread' -> none end event, with an ad-hoc sub-process 'Handle actions' (expanded in the figure) containing the task 'Tavily Web search'; the 'action follow-up' branch runs from the first gateway into that container and the container feeds back into the 'action needed?' gateway. No .bpmn is downloadable.
bpmn_evidence_quote: "Tavily Web search"
ai_evidence: An agentic tool-loop: the task labelled 'Agent' carries the violet Camunda AI Agent glyph and the container 'Handle actions' holds this connector's task, i.e. the listing's own element is a tool the agent calls. The page states it: 'Tavily changes that with a search engine purpose-built for AI agents', 'Use this connector to extract web content in end-to-end business processes powered by Camunda', and the feature 'Allow AI agents to search the web'. Tags: 'AI Services', 'Agentic AI orchestration'.
ai_evidence_quote: "Tavily changes that with a search engine purpose-built for AI agents"
artefacts:
  screenshot: 198_tavily-search-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1100
capture_method: curl of the listing's own asset (d3bql97l1ytoxn.cloudfront.net, app_resources/541302/overview/img8154125624442612897-2x.png, 1100x578); native read at full size - a Camunda-branded process diagram
---

## What the page shows

The Tavily Search Connector (community connector by mathieu-stennier, connectors bundle). A Slack-triggered agent loop in which the LLM agent calls Tavily web search as one of its tools and replies in the Slack thread.

## Observations (description only, no interpretation)

- **AI activity - function:** the agent decides the action and calls the Tavily search tool; the tool itself retrieves real-time web content for the model.
- **AI activity - element type:** a serviceTask labelled 'Agent' with the Camunda AI Agent glyph, plus an ad-hoc sub-process 'Handle actions' acting as the agent's tool container, in which the Tavily task sits. The Tavily task itself is the connector call this listing publishes.
- **Authority - downstream:** the tool result returns into the 'action needed?' gateway, so the agent's next step depends on the search result; the outcome is posted back to Slack.
- **Authority - data:** the tool supplies web content (the connector's extract-web-content operation, per the page); no data objects are drawn.
- **Authority - control:** the gateway 'action needed?' with its two branches ('action needed' back into the tool container, and the reply path), plus the first gateway's 'action follow-up' branch.
- **Authority - control (human):** only the Slack reply, which a person reads; no user task and no approval gate is drawn.
- **Input provenance:** a Slack message triggers the process; the agent's prompt and the search query are not visible in the capture.
- **Guards present:** the agent's own decision gateway ('action needed?') is the only control point drawn; no iteration cap, no confidence threshold and no human approval appear.
- **Prompt / model detail visible:** none - no model, provider or prompt appears in the diagram, and no .bpmn is published.

## Notes for the researcher

The strongest agentic shape in this batch: the listing's own task is drawn inside the tool container of an AI Agent element, so the AI element is inside the process and the connector sits inside the loop rather than beside it. Compare n=160 (agentic process with a tool loop) and n=171 (ad-hoc tool container).
