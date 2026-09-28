---
n: 270
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: Camunda Releases Agentic Orchestration for the Enterprise
url: https://camunda.com/blog/2025/04/camunda-87-agentic-orchestration-for-enterprise/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "captured figure 2 (page alt \"Ai-agent-ad-hoc-sub-process-camunda\", 1448x735 source): a BPMN process headed by a magenta container titled \"AI-Agent\" with the subtitle \"The BPMN ad-hoc subprocess leverages any LLM to decide the next best action\", itself labelled \"Baggage Loss Agent\" and holding the tasks \"Query baggage tracking database\", \"Inquire with last known airport\" (into the message catch event \"Airport responded\"), \"Send voucher for personal care products\", \"Request more information from passenger\" (into \"Passenger responded\"), \"Organize baggage delivery\" (into \"Inform passenger about delivery\"); outside it are the start event \"Passenger reports lost baggage\", the boundary events \"Passenger requests status\", \"Low Confidence\" and the timer \"48h\", the tasks \"Notify passenger about status\" and \"Manual Processing\" (a user task), the exclusive gateway \"Compensation claim?\" with \"Yes\" / \"No\", the user task \"Process compensation\", and the ad-hoc marker \"~\" at the bottom edge of the container"
bpmn_evidence_quote: "Ai-agent-ad-hoc-sub-process-camunda"
ai_evidence: the AI element is the BPMN ad-hoc sub-process itself - the figure's container is captioned "AI-Agent" / "The BPMN ad-hoc subprocess leverages any LLM to decide the next best action", and the page states the release debuts agents powered by BPMN ad-hoc sub-processes
ai_evidence_quote: "We’re excited to announce the general availability of new agentic process orchestration capabilities to model, deploy and manage AI agents"
artefacts:
  screenshot: 013_camunda-87-agentic-orchestration-for-enterprise.png
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

The post announces the 8.7 release and its agentic orchestration capability, and its
central figure is a luggage claim at an airline: "Passenger reports lost baggage" starts the
process, an "AI-Agent" container labelled "Baggage Loss Agent" holds the agent's available
actions, and the outcome forks at the gateway "Compensation claim?" into the user task
"Process compensation" or straight to the end event. The container is drawn in the vendor's
AI colour with the caption "The BPMN ad-hoc subprocess leverages any LLM to decide the next
best action", and two of its tasks ("Query baggage tracking database", "Organize baggage
delivery") are outlined to mark them, while the messaging tasks carry an envelope icon.

Around the container the model carries the boundary events "Passenger requests status",
"Low Confidence" and a "48h" timer, and the page describes the release in terms of the same
construct: "The introduction of ad-hoc sub-processes to Camunda (released in 8.7) allows
tasks to be activated dynamically, removing requirements for modeling task sequence, task
order or task completion; this is all handled in runtime by the ad-hoc sub-process logic."

## Observations (description only, no interpretation)

- **AI activity - function:** deciding the next action at runtime - the figure's own
  caption is "The BPMN ad-hoc subprocess leverages any LLM to decide the next best action";
  the page adds that the ad-hoc sub-process removes "requirements for modeling task
  sequence, task order or task completion".
- **AI activity - element type:** a BPMN ad-hoc sub-process used as the agent's container -
  the page: "Build your first AI agent leveraging BPMN ad-hoc sub-processes with this
  step-by-step guide."; the figure names the container "Baggage Loss Agent" under the
  heading "AI-Agent" and prints the ad-hoc marker "~" at its bottom edge.
- **Authority - downstream:** the tasks the agent can run, as printed in the container:
  "Query baggage tracking database", "Inquire with last known airport", "Send voucher for
  personal care products", "Request more information from passenger", "Organize baggage
  delivery", "Inform passenger about delivery".
- **Authority - data:** `not visible on the page` (the figure prints labels only; the page
  names no variables or data objects for this model).
- **Authority - control:** the exclusive gateway "Compensation claim?" with its "Yes" /
  "No" flows, the user task "Process compensation", the user task "Manual Processing"
  reached from the "Low Confidence" and "48h" boundary events through a gateway, and the
  human-facing "Notify passenger about status" task.
- **Input provenance:** the passenger's lost-baggage report at the start event "Passenger
  reports lost baggage", and the answers returned to the container's message catch events
  "Airport responded" and "Passenger responded".
- **Guards present:** the boundary error event "Low Confidence" and the boundary timer
  "48h", both routing through a gateway to the "Manual Processing" user task; the page
  frames the release as letting customers "implement as much or as little AI as you want
  within guardrails".
- **Prompt / model detail visible:** `not visible on the page` - no model id, prompt text or
  parameter is printed; both the page and the figure speak generically of "any LLM".

## Notes for the researcher

The figure is a vendor marketing render rather than a Modeller screenshot - the "AI-Agent"
container is drawn as a magenta card over the process - but its contents are drawn in
ordinary BPMN notation with the ad-hoc tilde marker at the container's bottom edge, so the
artefact is a BPMN diagram with a highlighted region. The downloaded file is 1400x711
although the source asset is 1448x735. The post also carries a GIF of "Camunda Copilot"
generating a travel-planner model (figure 1, alt "trip-planner-bpmn-copilot-camunda") and
an IDP invoice figure, neither captured here. Icons inside the container were checked by
zooming: the two outlined tasks carry a gray gear-like icon and the messaging tasks an
envelope icon; the figure does not print what those icons bind to.
