---
n: 1405
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: Where AI Really Creates Value and Where It Doesn't | Camunda
url: https://camunda.com/blog/2026/09/where-ai-really-creates-value-and-where-it-doesnt/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: the captured figure is a BPMN process model - a start event with a message glyph "send a claim", rounded-rectangle tasks ("extract data", "find a customer data"), two nested sub-process containers (the outer one labelled "Process claim (AI agent)" with the purple star badge and the ad-hoc tilde at its bottom edge, the inner one labelled "Ask insurer for missing information" containing its own start event, a task "Send clarification request", a message catch event "Wait for insurer reply" and an end event "Reply received"), an escalation-style boundary event attached to the outer container's bottom edge, an exclusive gateway with an X marker between the container and the tasks that follow, an end event "claim processed" and a loop back from the user task "consider the claim" to the gateway
bpmn_evidence_quote: "Pic.3- Four mechanisms in one process, each one handles its own part of the decision."
ai_evidence: the process's own container is labelled "Process claim (AI agent)" and holds the steps "Consolidate claim into unified system" and "Evaluate claim against policy rules" plus the nested sub-process "Ask insurer for missing information"; the page states the design intent - "Need to sort a document into a category? Use an LLM. Need to figure out what a request is about? Use an LLM." and "If needed, an AI agent asks follow-up questions and pulls all the information together." - and names AI Agent as one of the mechanisms a process step can be assigned to
ai_evidence_quote: "Its job is to pick the best-fitting mechanism for each step of a process: DMN, API, Connector, User Task, or AI Agent."
artefacts:
  screenshot: 021_where-ai-really-creates-value-and-where-it-doesnt.png
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

The post argues that orchestration should not "use AI as often as possible" but pick "for
every step of a process, whichever mechanism creates the most value for the business", and
its first figure (alt "Process using multiple mechanisms", captioned "Pic.3- Four mechanisms
in one process, each one handles its own part of the decision.") is the claim process it
argues from. The model runs from the start event "send a claim" through "extract data"
(extraction-connector glyph) and "find a customer data" (REST glyph) into the large
container labelled "Process claim (AI agent)", which carries a purple four-pointed-star
badge at its top-left corner and the ad-hoc tilde at its bottom edge.

Inside the container sit the nested sub-process "Ask insurer for missing information" (its
own start event, the task "Send clarification request", the message catch event "Wait for
insurer reply" and the end event "Reply received") and the two tasks "Consolidate claim into
unified system" (gear glyph) and "Evaluate claim against policy rules" (DMN table glyph). A
boundary event on the container's bottom edge leads to the user task "consider the claim"
(person glyph), which flows back into the exclusive gateway that follows the container; from
there the process continues through "Create claim documentation" and "notify insurer about
decision" to the end event "claim processed".

## Observations (description only, no interpretation)

- **AI activity - function:** the page's statements about what the AI step does are "Need to
  sort a document into a category? Use an LLM. Need to figure out what a request is about?
  Use an LLM." and "If needed, an AI agent asks follow-up questions and pulls all the
  information together."; the container's own label is "Process claim (AI agent)".
- **AI activity - element type:** a BPMN sub-process container labelled "Process claim (AI
  agent)" - purple star badge, ad-hoc tilde at its bottom edge - holding an inner sub-process
  and two tasks; the page frames this as choosing one mechanism per step ("DMN, API,
  Connector, User Task, or AI Agent") rather than as a task type.
- **Authority - downstream:** the steps visible inside the agent container - "Ask insurer for
  missing information" (with "Send clarification request" and "Wait for insurer reply"),
  "Consolidate claim into unified system", "Evaluate claim against policy rules"; downstream
  of the container the process runs "Create claim documentation" and "notify insurer about
  decision", and the page states "The customer is notified of the claim decision."
- **Authority - data:** `not visible on the page` (the figure prints labels only; no
  variables or data objects appear in the brief or in the image).
- **Authority - control:** the exclusive gateway with the X marker that sits immediately
  after the agent container and receives both the container's own flow and the flow returning
  from the user task "consider the claim"; the boundary event on the container's bottom edge
  is what opens that human path. The page states the goal as "keeping the whole decision
  logic clear and under control".
- **Input provenance:** the claim arrives at the start event "send a claim" and is passed
  through "extract data" and "find a customer data" before it reaches the agent container;
  the page does not say what the extracted document is.
- **Guards present:** the user task "consider the claim" (person glyph) reached through the
  boundary event on the agent container, and the exclusive gateway that joins the two paths
  before any notification; the page does not name a filter, prompt guard or audit log.
- **Prompt / model detail visible:** `not visible on the page` - no model name, prompt text
  or tool definition is printed. The page discusses prompt ownership only as an operational
  cost: "Someone now needs to manage prompts, check answer quality, track model versions,
  build monitoring, run regression tests, keep things observable, and meet security and
  compliance requirements."

## Notes for the researcher

The captured figure's tasks carry connector glyphs (extraction, REST, gear, DMN table) and
one user task; the only visible marker of the AI element is the container's own label,
"Process claim (AI agent)", together with the purple star badge and the ad-hoc tilde - no
task-level AI icon appears anywhere in the figure. Labels are readable at 1400 px (verified
by enlarging the container and its contents). Two further page statements frame the diagram:
"That's exactly why AI isn't a competitor to, say, DMN, and it isn't a replacement for an
API. It's just one more tool for the architect." and "Orchestration ties all these mechanisms
together into one process that can be managed and governed." The post's second figure (alt
"The building blocks of orchestration: APIs, Scripts, Connectors, Human tasks, DMN, AI") is a
non-BPMN block diagram and is not captured.
