---
n: 228
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: AI Agent Chat with MCP Tools
url: https://marketplace.camunda.com/apps/682919/ai-agent-chat-with-mcp-tools
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: A downloadable .bpmn 'ai-agent-chat-with-mcp': userTask 'User Feedback' -> an adHocSubProcess named 'AI Agent' (bound to io.camunda.connectors.agenticai.aiagent.jobworker.v1, io.camunda.agenticai:aiagent-job-worker:1) whose interior holds the tool tasks 'OpenMemory', 'Filesystem', 'Deepwiki', 'Time' and 'Superflux Product Calculation' (serviceTasks bound to io.camunda.connectors.agenticai.mcp.client.v0 / mcp.remoteclient.v0, types io.camunda.agenticai:mcpclient:0 and io.camunda.agenticai:mcpremoteclient:0), plus userTask 'Ask for confirmation' on the filesystem path, subProcess 'Event_Sub_Process' and an inbound 'Handle message' start.
bpmn_evidence_quote: "AI Agent"
ai_evidence: The process is built around an agent element: an adHocSubProcess 'AI Agent' whose template is Camunda's agentic AI Agent job worker, wired to MCP tool connectors, with the model supplied through the Camunda-provided LLM endpoint (secrets.CAMUNDA_PROVIDED_LLM_API_ENDPOINT / _API_KEY) and an openaiCompatible provider block. The page says 'Orchestrate AI chat with MCP tools', 'Let the agent discover and call tools exposed by MCP servers, so you can extend chat beyond Q&A to complete real tasks', 'Add human approval for filesystem actions :: Route filesystem tool calls through a confirmation task so a user can approve or deny execution before any file operation runs', 'Persist and recall important context' (the OpenMemory tool) and 'Iterate until the user is satisfied'.
ai_evidence_quote: "Let the agent discover and call tools exposed by MCP servers, so you can extend chat beyond Q&A to complete real tasks."
artefacts:
  screenshot: null
  archive: null
  bpmn_xml: 228_ai-agent-chat-with-mcp-tools.bpmn
duplicate_of: null
access: public
capture_source: bpmn-xml
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own .bpmn (reached through the listing's own resource link), read directly. The listing's only published image is a 230x230 icon whose pixels are all-black under a transparent alpha channel, so the file - not the figure - is the capture
---

## What the page shows

AI Agent Chat with MCP Tools (Camunda, open source, blueprint/quick start, 8.8). A chat process in which a Camunda AI Agent calls tools exposed by MCP servers (filesystem, memory, wiki, time, a product calculation), asks the user to confirm filesystem actions, collects feedback and loops back until the user is satisfied.

## Observations (description only, no interpretation)

- **AI activity - function:** run the chat (receive the message, decide which tool to call, produce the reply) and call each MCP tool - filesystem operations, memory persistence/recall, wiki lookup, time, and a product calculation.
- **AI activity - element type:** an adHocSubProcess 'AI Agent' bound to the agentic AI Agent job-worker template, containing tool serviceTasks bound to the MCP client and MCP remote-client templates - i.e. the agent is a *container* over its tools, not a single task.
- **AI activity - models named:** none by id; the file binds the Camunda-provided LLM endpoint and API key secrets with an 'openaiCompatible' provider configuration.
- **Authority - downstream:** the agent decides which tool runs inside the ad-hoc container and what reply the chat returns; the filesystem tool call is routed through the userTask 'Ask for confirmation' before execution.
- **Authority - control:** a human approval task in front of filesystem writes, plus the feedback loop (userTask 'User Feedback' -> back into the agent) - the user's satisfaction is the loop's exit condition; an event sub-process handles inbound messages.
- **Tool reachability:** filesystem access, a persistent memory store (OpenMemory), an external documentation/wiki tool (Deepwiki), a clock, and an in-process product calculation - the widest tool surface in this batch.
- **Data reachable by the model:** the chat messages, the agent context carried across turns (agent.context, agent.responseText) and whatever the tools read or write - including files on the filesystem, gated by the confirmation task.
- **Human role:** confirm filesystem tool calls; supply feedback that decides whether the loop continues.

## Notes for the researcher

The most capable agentic artefact in this source: an AI Agent ad-hoc sub-process with MCP tools inside it, a human confirmation gate in front of filesystem actions, and a feedback loop that keeps the chat going until the user is satisfied. Two reading notes: the tool set is fixed in the file (OpenMemory, Filesystem, Deepwiki, Time, 'Superflux Product Calculation'), so the agent's reach is enumerable from the model rather than from a configuration panel; and the model itself comes from the Camunda-provided LLM endpoint secrets, so the record cannot name a provider. The listing publishes no usable figure, which is why the artefact captured is the .bpmn.
