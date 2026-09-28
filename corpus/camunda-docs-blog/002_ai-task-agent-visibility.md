---
n: 300
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: The Benefits of BPMN AI Agents
url: https://camunda.com/blog/2025/05/benefits-bpmn-ai-agents/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: the post's own rendered diagram, read at full width (figure 1, alt "Ai-agent-visibility-bpmn-camunda"): start event "Message Needs to be Delivered", rounded-rectangle tasks, two exclusive gateways with X markers, a sequence-flow loop back to the first gateway, an end event "Message Delivered", and a sub-process container labelled "Niall's Tools"
bpmn_evidence_quote: "The diagram above shows a BPMN process that has implemented an AI agent."
ai_evidence: task "AI Task Agent" carrying the purple AI connector icon, sitting between the gateway and the exclusive gateway "Do we need to run some tools?"; the ad-hoc sub-process "Niall's Tools" holds the tool tasks "Send Slack Message", "Send an Email" and "Get More Info" - the AI element is a first-class BPMN task inside the process
ai_evidence_quote: "The agent logic is contained within the AI Task Agent activity and the tools it has access to is displayed with an ad-hoc sub-process."
artefacts:
  screenshot: 002_ai-task-agent-visibility.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1400
capture_method: chrome-devtools-mcp page fetch; the figure's cdn.sanity.io URL decoded out of the page's /_next/image proxy, downloaded at w=1400, first frame of the GIF converted to PNG
---

## What the page shows

The post argues that AI agents should be modelled in BPMN rather than as a black box, and
its first figure is the model it argues from: a "Message Needs to be Delivered" start event
into the task "Create Prompt", an exclusive gateway, the task "AI Task Agent", and a second
exclusive gateway labelled "Do we need to run some tools?" whose "Yes" branch enters the
sub-process "Niall's Tools" - containing "Send Slack Message", "Send an Email" and "Get More
Info" - and loops back into the first gateway, with "No" going to the end event "Message
Delivered". The AI element is therefore a named BPMN task in the middle of an ordinary
process, and the tools it may invoke are a sub-process container. The second figure is the
same process as an Optimize heatmap ("The diagram above shows a heatmap which shows which
tools take the longest to run").

## Observations (description only, no interpretation)

- **AI activity - function:** "your agent will find out only in runtime what tools are at its
  disposal"; the page frames the agent as understanding its purpose and rules, having tools,
  and keeping state.
- **AI activity - element type:** a task labelled "AI Task Agent" plus an ad-hoc sub-process
  holding the tools; "The agent logic is contained within the AI Task Agent activity and the
  tools it has access to is displayed with an ad-hoc sub-process."
- **Authority - downstream:** the agent's tool set as printed in the diagram: "Send Slack
  Message", "Send an Email", "Get More Info". The gateway "Do we need to run some tools?"
  routes back into the tool container.
- **Authority - data:** `not visible on the page` (the diagram shows labels only; no
  variables or data objects are printed).
- **Authority - control:** the exclusive gateways before and after the agent task, and the
  human-visible Optimize heatmap used to evaluate tool duration.
- **Input provenance:** "Create Prompt" is the step that forms the agent's input; the page
  does not say what the message content is.
- **Guards present:** process-level guardrails only - the agent sits inside a BPMN process
  with gateways around it; "you're still adding a completely dynamic aspect to your process".
- **Prompt / model detail visible:** `not visible on the page` - no model name, prompt text
  or parameter is printed; the page only says the LLM can be swapped ("it lets you switch out
  the agent's own LLM for the latest and greatest").

## Notes for the researcher

This is the clearest vendor argument for the pattern the thesis is about, and the diagram
is legible at full width - the "AI Task Agent" task carries the AI connector's icon, so the
AI element is visually distinct from the ordinary tasks around it. The `_cmdb_rec` figure
list for this post also shows two further figures (maintainability, performance) that are
the same model annotated; only the first is captured.
