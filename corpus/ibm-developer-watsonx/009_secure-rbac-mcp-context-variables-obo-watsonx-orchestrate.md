---
n: 773
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Implement secure RBAC for MCP server access using context variables and On-Behalf-Of (OBO) flow in watsonx Orchestrate - the 'RBAC_Architecture' figure"
url: https://developer.ibm.com/tutorials/secure-rbac-mcp-context-variables-obo-watsonx-orchestrate/
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "The page's 'RBAC_Architecture' figure is a participant-and-message-flow drawing: agent, tool and server boxes joined by numbered message flows, two of which carry decision conditions ('4.1 If User Role = General User', '4.11 If User Role = Manager') and two more the outcomes ('4.13 Access tools', '4.2 Access tools applicable for user with general access'). Its structure is that of a BPMN collaboration (pools as participants, numbered message flows, conditions on the flows) but the notation is the vendor's own - no events, no BPMN task types, no gateways or pools drawn as BPMN pools. Is it a BPMN 2.0 model in house style, so the corpus records it, or a non-BPMN process drawing that E1-not-bpmn excludes?"
needs_visual_check: false
bpmn_evidence: "png, zoomed to full size (contact sheet SHEET_VIEW06, row 4 col 5). an 'AI Platform' diagram: a user on the left, 'Secure WXO Embedded Chat', an 'HR Main agent', a 'watsonx Orchestrate' band containing 'Tools' (RBAC Plugin tool, mcp_tools_server with get_office_locations / get_leave_balance / get_holidays, and a second mcp_tools_server with get_employee_salary / get_team_summary_dashboard), a General Agent, a Manager Agent, an LLM 'GPT OSS 120B (via Groq)' node and an 'IBM Code Engine / MCP Server' box on the right. The connectors carry a numbered, ordered sequence with conditional branches: '1. User Query', '2. Pass user_profile as context variable', '3. Pre-invoke plugin', '4. Access/No Access to manager agent', '4.1 If User Role = General User', '4.2 Access tools applicable for user with general access', '4.11 If User Role = Manager', '4.12 Access manager specific tools', '4.13 Access tools', '5. Return the response', '6. Display the response in chat'. I hesitated here and the rules say hesitation resolves to UNCERTAIN, not to a code: the boxes are participants (agents, servers, tools) rather than activity boxes, but the numbered flows carry decision conditions, so the figure may be a BPMN collaboration-with-message-flows drawn in the vendor's house style rather than a mere architecture view."
bpmn_evidence_quote: "RBAC_Architecture"
ai_evidence: "AI elements are inside the drawn figure: an 'HR Main agent', 'General Agent' and 'Manager Agent' node, an LLM node ('GPT OSS 120B (via Groq)') and two MCP tool servers with their tools, and the page's own framing is verbatim 'This increasing autonomy creates an important responsibility: Enterprises must give each AI agent the correct level of access.' UNCERTAIN because the figure's conditional, numbered flows ('4.1 If User Role = General User', '4.11 If User Role = Manager') read as process steps while its boxes are agents and servers."
ai_evidence_quote: "RBAC_Architecture"
artefacts:
  screenshot: 009_773_image1.png
  assets: [009_773_image1.png]
  bpmn_xml: []
  archive: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: "the figure fetched from its native asset URL on developer.ibm.com and viewed at full size on 2026-09-25"
judgment: true
---

## What the artefact is

`https://developer.ibm.com/tutorials/secure-rbac-mcp-context-variables-obo-watsonx-orchestrate/` (api, ledger row n=773), figure `figs/773_image1`.

## What the figure shows



## Why the row is UNCERTAIN

png, zoomed to full size (contact sheet SHEET_VIEW06, row 4 col 5). an 'AI Platform' diagram: a user on the left, 'Secure WXO Embedded Chat', an 'HR Main agent', a 'watsonx Orchestrate' band containing 'Tools' (RBAC Plugin tool, mcp_tools_server with get_office_locations / get_leave_balance / get_holidays, and a second mcp_tools_server with get_employee_salary / get_team_summary_dashboard), a General Agent, a Manager Agent, an LLM 'GPT OSS 120B (via Groq)' node and an 'IBM Code Engine / MCP Server' box on the right. The connectors carry a numbered, ordered sequence with conditional branches: '1. User Query', '2. Pass user_profile as context variable', '3. Pre-invoke plugin', '4. Access/No Access to manager agent', '4.1 If User Role = General User', '4.2 Access tools applicable for user with general access', '4.11 If User Role = Manager', '4.12 Access manager specific tools', '4.13 Access tools', '5. Return the response', '6. Display the response in chat'. I hesitated here and the rules say hesitation resolves to UNCERTAIN, not to a code: the boxes are participants (agents, servers, tools) rather than activity boxes, but the numbered flows carry decision conditions, so the figure may be a BPMN collaboration-with-message-flows drawn in the vendor's house style rather than a mere architecture view.

## AI evidence (why this is not an E2 exclusion)

AI elements are inside the drawn figure: an 'HR Main agent', 'General Agent' and 'Manager Agent' node, an LLM node ('GPT OSS 120B (via Groq)') and two MCP tool servers with their tools, and the page's own framing is verbatim "This increasing autonomy creates an important responsibility: Enterprises must give each AI agent the correct level of access." UNCERTAIN because the figure's conditional, numbered flows ('4.1 If User Role = General User', '4.11 If User Role = Manager') read as process steps while its boxes are agents and servers.

## Notes for the researcher

- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
