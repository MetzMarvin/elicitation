---
n: 288
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: "Building Trustworthy AI Agents: How Camunda Aligns with Industry Best Practices"
url: https://camunda.com/blog/2025/05/ai-agent-design-patterns-in-camunda/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "captured figure 1 (page alt \"AI agent inserted into BPMN diagram for process visibility\", 624x320 source): a BPMN process in which a blue container titled \"AI Agent\" with the subtitle \"The BPMN ad-hoc subprocess leverages any LLM to decide the next best action\" is labelled \"Baggage Loss Agent\" and holds the tasks \"Query baggage tracking database\", \"Inquire with last known airport\" (into the message catch event \"Airport responded\"), \"Send voucher for personal care products\", \"Request more information from passenger\" (into \"Passenger responded\"), \"Organize baggage delivery\" (into \"Inform passenger about delivery\"); around it are the start event \"Passenger reports lost baggage\", the boundary events \"Passenger requests status\", \"Low Confidence\" and the \"48h\" timer, the tasks \"Notify passenger about status\" and \"Manual Processing\", the exclusive gateway \"Compensation claim?\" with \"Yes\" / \"No\", the user task \"Process compensation\", and the end events \"Passenger report (semi-)automatically processed\", \"Passenger notified about status\" and \"Passenger report manually processed\""
bpmn_evidence_quote: "By visualizing these handoffs in BPMN diagrams, stakeholders across technical and nontechnical domains can easily understand the agent responsibilities, audit workflows, and troubleshoot when necessary."
ai_evidence: the AI element is inside the model as a BPMN ad-hoc sub-process container captioned "AI Agent" / "The BPMN ad-hoc subprocess leverages any LLM to decide the next best action", while the page binds each agent to a discrete BPMN element
ai_evidence_quote: "Each agent’s task is represented as a discrete service task with well-defined inputs and expected outputs."
artefacts:
  screenshot: 014_ai-agent-design-patterns-in-camunda.png
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

The post compares Camunda's agent implementation with published OpenAI and Anthropic
guidance, and argues that agents should be narrowly scoped and coordinated by a central
orchestrator rather than delegating to one another. Its first figure is the same
baggage-loss claim process used in the 8.7 release material, here drawn with a blue "AI
Agent" container: the passenger reports a lost bag, the container named "Baggage Loss
Agent" holds the agent's possible actions (querying the tracking database, inquiring with
the last known airport, sending a voucher, requesting more information, organising
delivery), and the process continues at the gateway "Compensation claim?" either into the
user task "Process compensation" or to an end event; the boundary events "Low Confidence"
and "48h" route to the "Manual Processing" task.

The page's own binding of agent to process element is explicit: "Each agent's task is
represented as a discrete service task with well-defined inputs and expected outputs", and
it names three agents in an insurance example - "Camunda orchestrates a Document Extraction
agent to pull key fields, a Fraud Detection agent to assess risk, and a Claims Decision
agent to recommend next steps."

## Observations (description only, no interpretation)

- **AI activity - function:** the figure's caption states the function - "The BPMN ad-hoc
  subprocess leverages any LLM to decide the next best action"; the page describes the
  scope of each agent as a single task such as "information retrieval, natural language
  generation, decision support, or classification".
- **AI activity - element type:** both forms are named - the page says "Each agent's task
  is represented as a discrete service task with well-defined inputs and expected outputs",
  while the captured figure shows the agent as an ad-hoc sub-process container labelled
  "AI Agent" / "Baggage Loss Agent".
- **Authority - downstream:** the actions printed inside the container: "Query baggage
  tracking database", "Inquire with last known airport", "Send voucher for personal care
  products", "Request more information from passenger", "Organize baggage delivery",
  "Inform passenger about delivery".
- **Authority - data:** `not visible on the page` (no variables, data objects or records
  are printed in the figure, and the page names none for this model; it says only that
  every "data handoff is visually modeled and logged").
- **Authority - control:** the exclusive gateway "Compensation claim?", the user task
  "Process compensation", the end events "Passenger report (semi-)automatically processed"
  and "Passenger report manually processed", and the "Manual Processing" task reached from
  the "Low Confidence" and "48h" boundary events.
- **Input provenance:** the passenger's lost-baggage report (start event "Passenger reports
  lost baggage") and the responses caught at "Airport responded" and "Passenger responded".
- **Guards present:** the boundary error "Low Confidence" and boundary timer "48h" with
  their route to "Manual Processing"; the page also states that "BPMN error events and
  boundary timers allow processes to anticipate common failures (like timeouts or bad data)
  and take corrective actions, such as retrying, skipping, or escalating to a human
  operator"; the page also states that it supports centralised (manager) patterns, where a
  single orchestrator manages when, why, and how agents act.
- **Prompt / model detail visible:** `not visible on the page` - no model id, prompt text or
  parameter appears in the page or the figure; the figure says only "any LLM".

## Notes for the researcher

The figure is a vendor render (blue "AI Agent" card over the process) of the same
baggage-loss model that the 8.7 release post uses in magenta - the two files are not
identical, and only this post's figure 1 carries alt text binding the agent to the BPMN
diagram. The source asset is
small (624x320) and the downloaded file is an upscaled 1400x718; all element labels were
still readable and are quoted above, but a human may want to confirm the two smallest
strings ("Low Confidence" on the boundary error and the parenthetical in "(semi-)
automatically processed"). The post's second figure (alt "AI agents working together with
their separate tasks", 624x243) was not captured because the ruling named figure 1.
