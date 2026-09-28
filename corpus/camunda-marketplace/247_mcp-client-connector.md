---
n: 247
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: MCP Client Connector
url: https://marketplace.camunda.com/apps/682917/mcp-client-connector
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: A complete published process, drawn on a canvas: start -> gateway -> an adHocSubProcess named 'AI Agent' (violet glyph) holding three tool tasks - 'Documentation', 'Memory', 'Time Conversions' - and, nested inside it, an event sub-process 'MCP with user confirmation' that contains start -> exclusiveGateway 'Needs confirmation?' -> serviceTask 'Filesystem' (on the 'no' branch) and userTask 'Ask for confirmation' -> gateway 'Execution allowed?' -> end 'MCP execution not allowed'; the agent's output goes to userTask 'User Feedback' -> gateway 'User satisfied?' -> 'yes' ends the process, 'no - we follow up' loops back into the gateway before the agent.
bpmn_evidence_quote: "Needs confirmation?"
ai_evidence: The listing is Camunda's MCP Client Connector (categories 'AI Services', 'Agentic AI orchestration', 8.8/8.9) and the published figure shows the agent container it exists for: an adHocSubProcess 'AI Agent' whose tool tasks are the connector's own MCP calls. The page frames it as 'Integrate Model Context Protocol (MCP) clients with agentic orchestration so your AI agent can discover and call tools provided by MCP servers', with features 'Connect AI agents to MCP tools', 'Filter and govern tool access', 'Add human approval steps' and 'Call MCP operations without an agent', and the overview heading 'Orchestrate MCP tool use with AI'.
ai_evidence_quote: "Integrate Model Context Protocol (MCP) clients with agentic orchestration so your AI agent can discover and call tools provided by MCP servers"
artefacts:
  screenshot: 247_mcp-client-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: listing-asset
capture_quality: legible
capture_width_px: 1056
capture_method: curl of the listing's own assets (d3bql97l1ytoxn.cloudfront.net, app_resources/682917/overview/img14199206004623531588-2x.png, 1056x660, plus the 230x230 element-template icon img13748040525169125872-2x.png), both read natively at full size
---

## What the page shows

The MCP Client Connector (Camunda, open source, 8.8/8.9). Camunda's connector for letting an AI agent discover and call tools on MCP servers - stdio servers run as OS processes, or remote servers over Streamable HTTP / HTTP SSE - modelled as an ad-hoc sub-process, with the tool set shown in the published figure (Documentation, Memory, Time Conversions) and a human confirmation gate in front of the filesystem tool.

## Observations (description only, no interpretation)

- **AI activity - function:** discover and call MCP tools on behalf of an agent; the figure's tool set is documentation lookup, memory, time conversion and filesystem access.
- **AI activity - element type:** an adHocSubProcess 'AI Agent' (the agent container, violet glyph) whose interior holds serviceTasks bound to this connector's MCP client template, plus a nested event sub-process for the confirmation path.
- **AI activity - models named:** none - the connector is the tool-calling half; the model is supplied by whatever agent template hosts it (cf. n=228, the blueprint that uses it).
- **Authority - downstream:** the agent chooses which tool to call, and the tool result returns into the chat; the flow then asks the user 'User satisfied?' and loops back to the agent on 'no - we follow up'.
- **Authority - control (human):** the nested 'MCP with user confirmation' sub-process - gateway 'Needs confirmation?' then userTask 'Ask for confirmation' then gateway 'Execution allowed?' with the terminal path 'MCP execution not allowed' - i.e. the filesystem write only happens with consent.
- **Authority - control (governance):** the page's 'Filter and govern tool access' feature, plus stdio servers managed by the connector runtime and the option to 'Call MCP operations without an agent'.
- **Data reachable by the agent:** whatever the MCP servers expose - here a memory store, documentation and the filesystem (gated by the confirmation task).
- **Human role:** approves or denies the gated tool call, and decides via 'User satisfied?' whether the agent keeps working.

## Notes for the researcher

The connector view of the same pattern recorded at n=228: there the blueprint, here the tool task template itself, with the human-approval path modelled *inside* the agent container as an event sub-process - the clearest 'approval before a tool executes' structure in this source. Note the listing publishes the complete process, not just a template panel, and that the page claims tool-access filtering and governance as features, which is what makes the gated filesystem task readable as a governed agent rather than an open one.
