---
n: 12
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: AI Agent Chat Quick Start
url: https://marketplace.camunda.com/apps/587865/ai-agent-chat-quick-start
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: Decisive: the listing publishes its .bpmn. Process 'AI Agent Chat With Tools' with an `adHocSubProcess` named 'AI Agent' whose tools are four `serviceTask`s.
bpmn_evidence_quote: "<bpmn:process id="..." name="AI Agent Chat With Tools""
ai_evidence: The ad-hoc sub-process 'AI Agent' carries `zeebe:modelerTemplate="io.camunda.connectors.agenticai.aiagent.jobworker.v1"` (`type="io.camunda.agenticai:aiagent-job-worker:1"`); its tools are `serviceTask`s bound to `io.camunda.connectors.HttpJson.v2` ('List users', 'Search recipe', 'Jokes API', 'Get list of Tech Stuff').
ai_evidence_quote: "zeebe:modelerTemplate="io.camunda.connectors.agenticai.aiagent.jobworker.v1""
artefacts:
  screenshot: null
  archive: null
  bpmn_xml: 012_ai-agent-chat-quick-start.bpmn
duplicate_of: null
access: public
capture_source: bpmn-xml
capture_quality: legible
capture_width_px: null
capture_method: curl of the raw.githubusercontent.com .bpmn behind the listing's Modeler import link; XML read directly
---

## What the page shows

A chat quick-start. The page describes 'intelligent conversational agents powered by AI' that 'interact with users and execute actions using integrated tools within a business process', with 'human-AI interaction', captured feedback and actions triggered 'via embedded forms'. The XML shows the agent as an ad-hoc sub-process 'AI Agent' whose tools are four HTTP-JSON calls, plus a user task 'User Feedback'.

## Observations (description only, no interpretation)

- **AI activity - function:** the page says the agent processes chat requests, captures user feedback and triggers actions (sending emails, initiating tasks) through embedded forms.
- **AI activity - element type:** an AI-agent `adHocSubProcess` (job-worker binding) with tool `serviceTask`s inside it.
- **Authority - downstream:** the four tool tasks are the agent's callable tools; a user task 'User Feedback' consumes the interaction.
- **Authority - data:** not visible in the XML (no data objects); the tools fetch from external HTTP APIs.
- **Authority - control:** the user task 'User Feedback' and the ad-hoc sub-process boundary.
- **Input provenance:** the chat request from the user.
- **Guards present:** none observed beyond the human 'User Feedback' task.
- **Prompt / model detail visible:** not visible in the XML; the page links the Camunda agentic-orchestration getting-started guide.

## Notes for the researcher

The .bpmn file name is 'ai-agent-chat-with-tools.bpmn'; the listing points at the Camunda docs for the pattern rather than a repo.
