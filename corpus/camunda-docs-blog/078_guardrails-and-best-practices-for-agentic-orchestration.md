---
n: 400
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: "Guardrails and Best Practices for Agentic Orchestration"
url: https://camunda.com/blog/2026/01/guardrails-and-best-practices-for-agentic-orchestration/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "the visual pass reads the captured figure as class 'bpmn': large BPMN; purple ad-hoc sub-process; labels unreadable; the page names BPMN itself: 'Process orchestration. Process orchestration is the coordination of systems, people, and decisions across an end-to-end workflow using a standard like'"
bpmn_evidence_quote: "Process orchestration. Process orchestration is the coordination of systems, people, and decisions across an end-to-end workflow using a standard like BPMN."
ai_evidence: "the page binds AI to a process element (AI-bound task, Anthropic/Claude): 'Your AI agents should not be the main orchestrator in processes; they should be participants in a greater orchestration, blending deterministic and dynamic steps into'; the contact-sheet pass reads the captured figure as ai_visible=unclear"
ai_evidence_quote: "Your AI agents should not be the main orchestrator in processes; they should be participants in a greater orchestration, blending deterministic and dynamic steps into"
artefacts:
  screenshot: 078_guardrails-and-best-practices-for-agentic-orchestration.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: poor
capture_width_px: 620
capture_method: figure downloaded at w=1400 from the asset URL the saved page names (cdn.sanity.io), fetched 2026-09-26
---

## What the page shows

The post is Camunda's own write-up of "Guardrails and Best Practices for Agentic Orchestration".
It opens on its subject directly: "As your organization embraces AI, it is of the utmost importance that you are using best practices and the proper guardrails so that your orchestrated processes."
The line the record quotes on the AI element is: "Your AI agents should not be the main orchestrator in processes; they should be participants in a greater orchestration, blending deterministic and dynamic steps into one executable model."

The captured figure is the page's 620x157 asset with alt text "Image3". The contact-sheet pass over the same asset read it as class "bpmn" with ai_visible=unclear, in its own words: large BPMN; purple ad-hoc sub-process; labels unreadable

## Observations (description only, no interpretation)

- **AI activity - function:** the page's own words bind the AI to the process: "Your AI agents should not be the main orchestrator in processes; they should be participants in a greater orchestration, blending deterministic and dynamic steps into" - the AI-bearing element it names is AI-bound task; elsewhere: "Model your process and the agent scope before selecting the LLM to use in that model ." (Anthropic/Claude)
- **AI activity - element type:** the captured figure is what the contact-sheet pass read as class "bpmn" (ai_visible=unclear), in its words: large BPMN; purple ad-hoc sub-process; labels unreadable
- **Authority - downstream:** the page: "You also want to consider agent response formats so that they can be properly utilized by downstream components."
- **Authority - data:** the page: "Sub-processes inside the agent’s scope can gather potentially helpful data, historical cases, and documents, while the agent plans its next action."
- **Authority - control:** the page: "Camunda, BPMN maps the flow, Decision Model and Notation (DMN) sets decision guardrails, connectors govern tool calls, and humans step in at the right gateways."
- **Input provenance:** the page: "The goal: Extract and summarize key points from complex customer documents."
- **Guards present:** the page: "Agentic orchestration refers to the specific coordinations of AI agents, tools, and handoffs including constraints like escalations, timers, and human approvals."
- **Prompt / model detail visible:** the page: "The goal of the system prompt and the agent are separate."

## Notes for the researcher

The AI call here rests on the page's own words, not on a reading of the figure. 

Capture: the page's 620x157 asset, downloaded at w=1400 and stored as 078_guardrails-and-best-practices-for-agentic-orchestration.png; the contact-sheet reading of the same asset is class bpmn / ai_visible unclear. Figure choice: alt 'Image3' + sheet note 'large BPMN; purple ad-hoc sub-process; labels unreadable'.
