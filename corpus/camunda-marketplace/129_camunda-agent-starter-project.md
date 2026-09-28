---
n: 129
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Camunda Agent Starter Project
url: https://marketplace.camunda.com/apps/829718/camunda-agent-starter-project
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: BPMN diagram published as the listing's overview asset; no .bpmn downloadable. Read natively: start event 'Request has come in for agent' -> an expanded ad-hoc sub-process 'Your Camunda Agent' (tilde marker at its lower edge, violet element glyph at its top-left) -> end event 'Request has been addressed'. Inside the sub-process, a dashed container 'Default Tools' holds 'Create Message for User', message events 'Send request' and 'Send Message', 'Response From user', 'Calculate Wait time', an exclusive gateway, a timer 'Wait for Next Communication', 'Get the Current Time and date' and 'Case Update'; below it a second, empty dashed container is annotated 'Put your new tools in here'.
bpmn_evidence_quote: "Put your new tools in here"
ai_evidence: The AI element is the ad-hoc sub-process 'Your Camunda Agent', carrying Camunda's violet four-pointed-star element-template glyph (the agentic-AI template) and the ad-hoc marker; its tools are ordinary BPMN elements inside the container. The page states 'Connect an AI agent to a Camunda process using the included BPMN template. The blueprint demonstrates how to wire agent tool calls into a service task' and 'Expose time and date as a tool available to the agent during process execution', with waits resumed 'based on incoming events' and end-user communication 'via Slack message events'.
ai_evidence_quote: "Connect an AI agent to a Camunda process using the included BPMN template"
artefacts:
  screenshot: 129_camunda-agent-starter-project.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1100
capture_method: curl of the listing's own overview asset (d3bql97l1ytoxn.cloudfront.net, overview/img3693877949706366534-2x.png, 1100x587); native read at full size
---

## What the page shows

Camunda's Agent Starter Project blueprint (Community, 'Start building Camunda agents quickly'). The page describes a working agent template - the same shape the AI Agent Connector documents - with three pre-built capabilities (time/date retrieval, process wait behaviour via native events, and Slack end-user communication) and an empty container for the user's own tools.

## Observations (description only, no interpretation)

- **AI activity - function:** run an AI agent whose tools are BPMN elements - here a message composer, a clock lookup and a wait-for-communication timer.
- **AI activity - element type:** an expanded ad-hoc sub-process carrying the violet agentic-AI element-template glyph; tools are ordinary tasks and events inside the dashed 'Default Tools' container.
- **Authority - downstream:** the sub-process is the process's only activity and the end event 'Request has been addressed' is the process result; nothing checks the agent's output.
- **Authority - data:** the tools (time/date, message events) are the agent's data access; no data objects or variable mappings are visible.
- **Authority - control:** within the sub-process, an exclusive gateway and an intermediate timer 'Wait for Next Communication' sequence the tools; no reviewer, threshold or error path is drawn.
- **Authority - control (human):** the end user participates as a message partner ('Send request', 'Response From user'), i.e. as a conversation partner, not as an approver of the agent's output.
- **Input provenance:** the start event 'Request has come in for agent'; the request's origin is not modelled.
- **Guards present:** none drawn; the empty 'Put your new tools in here' container is the extension point the page advertises.
- **Prompt / model detail visible:** none in the diagram; the page names no model or prompt, leaving the agent's connector to the user.

## Notes for the researcher

This is the starter-template counterpart to Camunda's AI Agent Connector listing (n=039): the same modelling pattern - an ad-hoc sub-process whose tools are BPMN elements - but published as a template whose tools are a message composer, a clock and a wait timer rather than the agent connector's tool-calling loop. The violet glyph and the ad-hoc marker are both visible in the capture.
