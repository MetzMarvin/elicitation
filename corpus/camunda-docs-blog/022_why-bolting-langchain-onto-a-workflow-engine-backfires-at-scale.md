---
n: 1410
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: Why Bolting LangChain onto a Workflow Engine Backfires at Scale | Camunda
url: https://camunda.com/blog/2026/07/why-bolting-langchain-onto-a-workflow-engine-backfires-at-scale/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: the captured figure is a BPMN model - a start event "Loan request received", rounded-rectangle tasks, exclusive gateways with X markers and labelled flows ("Fraud Risk Acceptable?", "Who keeps control?" with "agent" / "specialist", "Save answer to Knowledge base" with "yes" / "no"), a large container labelled "Loan Offer Preparation Agent" carrying the purple star badge and the ad-hoc tilde at its bottom edge, intermediate events ("Specialist answered", "Human control required"), a dotted escalation frame, end events ("Application Rejected (Fraud)", "Case solved", "Case resolution applied by human", "Human control required", "Case resolved by human"), and an orange frame labelled "Outer Orchestration" around the deterministic part with blue frames labelled "Inner Orchestration" inside the agent
bpmn_evidence_quote: "Inner and outer orchestration in a loan origination process. The orange frame shows outer orchestration: BPMN coordinates the end-to-end journey."
ai_evidence: the agent is a BPMN ad-hoc sub-process - the container labelled "Loan Offer Preparation Agent" (purple star badge, tilde at its bottom edge) - whose inner boxes are the LLM's tools, and two further tasks carry agent badges ("Fraud Agent", "Agent as a Judge"); the page states the mechanics directly: "The agent is the ad-hoc subprocess (the purple star). It's the reasoning space." and "The activities inside the subprocess become the agent's tools: each one is a real BPMN activity with a name and a description that the LLM uses to decide which tool to call."
ai_evidence_quote: "A loan support agent in Camunda Modeler. The ad-hoc subprocess (purple star) is the agent's reasoning space."
artefacts:
  screenshot: 022_why-bolting-langchain-onto-a-workflow-engine-backfires-at-scale.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1400
capture_method: chrome-devtools-mcp page fetch; the figure's cdn.sanity.io URL decoded out of the page's /_next/image proxy, downloaded at w=1400
---

## What the page shows

The post argues that putting an agent framework (LangChain) between a workflow engine and
the LLM is the wrong place for orchestration, and introduces "outer orchestration" (BPMN
coordinating the end-to-end journey) and "inner orchestration" (BPMN defining the operating
procedures between an agent's reasoning and its tools). The captured figure (alt "Inner and
outer orchestration in a loan origination process...") is the loan origination model it
argues from: the orange "Outer Orchestration" frame holds the start event "Loan request
received", the task "Fraud Agent", the gateway "Fraud Risk Acceptable?" (the "no" branch
going to "Auto-Reject (Fraud Risk)" and the end event "Application Rejected (Fraud)"), and
after the agent container the task "Agent as a Judge", a gateway with the flows "solved with
confidence", "needs review" and "needs human resolution", the task "Finalize case manually",
and the end events "Case solved" and "Case resolution applied by human".

The centre container is labelled "Loan Offer Preparation Agent", carries the purple star
badge at its top-left corner and the ad-hoc tilde at its bottom edge, and holds the tool
tasks "Load available home loan products", "Load available consumer loan products",
"Calculate loan repayments and assess affordability", "Core Banking Tools (Via MCP)", "Risk
Assessment", "Consumer Loan Application", "Query knowledge base" and "Set up customer
meeting". Inside the container two blue frames are labelled "Inner Orchestration": one holds
"Ask loan specialist", the gateway "Who keeps control?" ("agent" / "specialist"), the gateway
"Save answer to Knowledge base" ("yes" / "no"), "Save answer in knowledge base" and the
"Specialist answered" and "Human control required" events; the other holds "Review proposed
customer message", "Message customer" and "Wait for customer message". A dotted frame,
"Escalated to human control", holds "Human control required" into "Handle customer request"
and "Case resolved by human".

## Observations (description only, no interpretation)

- **AI activity - function:** the page describes the division of labour as "Inside the
  subprocess, the LLM reasons over these tools and decides what to invoke and in what order.
  Outside it, the process is deterministic. The agent reasons, the tools act, and the process
  orchestrates both.", and "The agent is the ad-hoc subprocess (the purple star). It's the
  reasoning space."
- **AI activity - element type:** a BPMN ad-hoc sub-process configured as an AI agent - the
  page says "The agent is a BPMN ad-hoc subprocess , a standard BPMN construct that contains
  activities which can be executed in any order, repeated, or skipped, rather than in a
  predefined sequence." and "The activities inside the subprocess become the agent's tools:
  each one is a real BPMN activity with a name and a description that the LLM uses to decide
  which tool to call." Two tasks outside the container, "Fraud Agent" and "Agent as a Judge",
  also carry agent badges in the figure.
- **Authority - downstream:** the tools the page names are "preconfigured BPMN activities the
  agent can invoke, such as asking the customer, querying a knowledge base, consulting a loan
  specialist, loading available products, calculating repayments and affordability" (the
  brief's copy of the sentence is cut off after the words "as its own s", so the last tool in
  the list is not recoverable from it); the figure's own tool labels are "Load available home
  loan products", "Load available consumer loan products", "Calculate loan repayments and
  assess affordability", "Core Banking Tools (Via MCP)", "Risk Assessment", "Consumer Loan
  Application", "Query knowledge base", "Set up customer meeting", "Ask loan specialist",
  "Review proposed customer message", "Message customer" and "Wait for customer message".
- **Authority - data:** `not visible on the page` (the figure prints labels only; no
  variables or data objects appear in the brief or in the image).
- **Authority - control:** the page states "Every tool invocation flows through explicit
  orchestration, so you can enforce guardrails, inject human review when needed, or adjust
  autonomy levels"; in the figure the control points are the gateway "Who keeps control?"
  ("agent" / "specialist"), the gateway "Save answer to Knowledge base" ("yes" / "no"), the
  "Human control required" events, the "Escalated to human control" frame with "Handle
  customer request", and the "Agent as a Judge" gateway whose "needs review" flow goes to the
  human task "Finalize case manually".
- **Input provenance:** the model starts at "Loan request received"; the page frames the outer
  layer as "BPMN coordinates the end-to-end business journey, from initial request to final
  outcome, across enterprise systems, agents, and people". The figure does not show how the
  loan data reaches the agent's tools.
- **Guards present:** the "Who keeps control?" gateway with its "specialist" branch to the
  "Human control required" escalation, the "Escalated to human control" frame ("Human control
  required" into "Handle customer request"), and the human task "Finalize case manually" on
  the "needs review" branch; the page also says the system prompt is inspectable ("The system
  prompt is plain text, visible right in the modeler. Nothing hidden behind the scenes.").
- **Prompt / model detail visible:** `not visible on the page` - no model id and no prompt
  text appear in the brief or in the captured figure (the figure is the model canvas, not the
  modeler's properties panel). The page asserts that the system prompt is visible in the
  modeler, and one tool label names a protocol: "Core Banking Tools (Via MCP)".

## Notes for the researcher

The captured figure is `021`-style canvas art, not a Modeler screenshot: it is a BPMN model
drawn in Camunda's illustration style with an orange "Outer Orchestration" frame and blue
"Inner Orchestration" frames added on top. The rulings' `ai_evidence_quote` is the alt text
of this post's *second* figure ("A loan support agent in Camunda Modeler. The ad-hoc
subprocess (purple star) is the agent's reasoning space."), which is the Modeler screenshot
showing the same agent and its properties panel; the same sentence also appears in the
brief's list of page lines that the AI judgement rested on, so it is on the page, but it
describes figure 2 rather than the captured figure 1. Figure 2 is the one that would show
the system prompt; it was not captured because the rulings file names figure 1. Agent
identity in the captured figure is readable (verified by enlarging: the purple star badge on
the "Loan Offer Preparation Agent" container, on "Agent as a Judge" and a purple badge on
"Fraud Agent"), and all task and gateway labels are legible at 1400 px.
