---
n: 426
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: "Scale Agentic Automation with A2A, MCP, and Enhanced Connectors with Camunda 8.9-alpha2"
url: https://camunda.com/blog/2026/01/a2a-mcp-and-enhanced-connectors-with-camunda-8-9-alpha2/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "the visual pass reads the captured figure as class 'bpmn': 'A2A Client' polling, blocking and webhook tasks; the page names BPMN itself: 'With our new A2A connectors, Camunda offers a reliable and observable way for a primary agent to delegate to a'"
bpmn_evidence_quote: "With our new A2A connectors, Camunda offers a reliable and observable way for a primary agent to delegate to a specialist , wait for the"
ai_evidence: "the page binds AI to a process element (Amazon AI service, MCP/A2A connector): 'Camunda has included A2A connectors in our 8.9-alpha2 release, updating our capabilities for clean multi-agent handoffs.'; the contact-sheet pass reads the captured figure as ai_visible=yes"
ai_evidence_quote: "Camunda has included A2A connectors in our 8.9-alpha2 release, updating our capabilities for clean multi-agent handoffs."
artefacts:
  screenshot: 082_a2a-mcp-and-enhanced-connectors-with-camunda-8-9-alpha2.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: marginal
capture_width_px: 529
capture_method: figure downloaded at w=1400 from the asset URL the saved page names (cdn.sanity.io), fetched 2026-09-26
---

## What the page shows

The post is Camunda's own write-up of "Scale Agentic Automation with A2A, MCP, and Enhanced Connectors with Camunda 8.9-alpha2".
The line the record quotes on the AI element is: "Camunda has included A2A connectors in our 8.9-alpha2 release, updating our capabilities for clean multi-agent handoffs."

The captured figure is the page's 529x388 asset with alt text "Image1". The contact-sheet pass over the same asset read it as class "bpmn" with ai_visible=yes, in its own words: "A2A Client" polling, blocking and webhook tasks

## Observations (description only, no interpretation)

- **AI activity - function:** the page's own words bind the AI to the process: "Camunda has included A2A connectors in our 8.9-alpha2 release, updating our capabilities for clean multi-agent handoffs." - the AI-bearing element it names is MCP/A2A connector; elsewhere: "Welcoming A2A connectors to Camunda" (MCP/A2A connector)
- **AI activity - element type:** the captured figure is what the contact-sheet pass read as class "bpmn" (ai_visible=yes), in its words: "A2A Client" polling, blocking and webhook tasks
- **Authority - downstream:** the page: "For example, an agent built with LangChain can hand off to another agent on CrewAI and still have the proper context, input, and outputs."
- **Authority - data:** the page: "A2A also uses a standardized protocol: HTTPS/S and JSON for data exchange and state updates."
- **Authority - control:** the page: "With this pattern, poll intervals and overall timeouts live in the BPMN model, so the process—not the agent—owns service levels."
- **Input provenance:** the page: "each other directly as well as agents that request specific tasks from a set of tools—essentially, providing our customers with the best of both worlds."
- **Guards present:** the page: "(or specialist agent) calls the webhook endpoint when the AI task completes or when a notable event occurs (eg, partial results, human-in-the-loop needed, final outcome)."
- **Prompt / model detail visible:** not visible on the page - no model name, prompt text or parameter is printed

## Notes for the researcher

The AI call here rests on the page's own words, not on a reading of the figure. 

Capture: the page's 529x388 asset, downloaded at w=1400 and stored as 082_a2a-mcp-and-enhanced-connectors-with-camunda-8-9-alpha2.png; the contact-sheet reading of the same asset is class bpmn / ai_visible yes. Figure choice: alt 'Image1' + sheet note '"A2A Client" polling, blocking and webhook tasks'.
