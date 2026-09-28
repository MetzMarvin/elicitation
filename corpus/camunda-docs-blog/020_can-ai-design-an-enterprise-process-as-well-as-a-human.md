---
n: 1399
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: Can AI Design an Enterprise Process as Well as a Human? | Camunda
url: https://camunda.com/blog/2026/08/can-ai-design-an-enterprise-process-as-well-as-a-human/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: the captured figure is a BPMN process model - a message start event "Travel event detected", rounded-rectangle tasks, exclusive gateways with X markers and labelled flows ("Eligible for offer?", "High risk score?", "Offers ready", "Compliance pass?", "Customer accepted?"), an event-based gateway with "Customer response received" and "Response window elapsed", end events ("Travel pack activated", "Cancelled - customer declined", "Cancelled by reviewer", "Cancelled - not eligible", "Cancelled - compliance failed", "Cancelled - no response in time"), and one sub-process container labelled "AI agent: build travel offer" carrying the ad-hoc tilde marker
bpmn_evidence_quote: "the skill returned a finished BPMN diagram right in the chat"
ai_evidence: the process contains a sub-process container explicitly labelled "AI agent: build travel offer" (ad-hoc tilde at its bottom edge) holding the tool steps "Check risk and account limits", "Generate offer" and "Predict acceptance likelihood"; the page states the design principle behind it - "the agent reasons inside an ad-hoc sub-process, while everything around it stays deterministic" - and names the internal steps and their LLM calls when describing the escalation branch
ai_evidence_quote: "Both are built on the same principle: the agent reasons inside an ad-hoc sub-process, while everything around it stays deterministic and controlled"
artefacts:
  screenshot: 020_resulted-bpmn-by-ai.png
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

The post reports an experiment in which the author gave Camunda's open-source AI skills two
processes he had designed by hand and compared the results, then argues that the quality of
the outcome "depends much more on how well the AI agent is designed". The captured figure
(alt "Resulted BPMN by AI") is the model the skill produced for the travel scenario - "A
customer is about to travel. The AI agent analyzes the trip and prepares a personalized
offer while ensuring it complies with business rules."

The model runs from the start event "Travel event detected" through "Identify customer",
"Enrich trip context" and "Check offer eligibility" into the sub-process container labelled
"AI agent: build travel offer", which holds "Check risk and account limits", "Generate
offer" and "Predict acceptance likelihood" (each carrying a gear glyph) and is marked with
the ad-hoc tilde at its bottom edge. From the container the flow continues through "High
risk score?" (a "High risk" branch into the user task "Review high risk offer", itself
followed by the gateway with "Reviewer decision" / "Create manually" / "Cancel"), "Offers
ready", "Run compliance check", "Compliance pass?", "Send offer to customer" and an
event-based gateway ("Wait for customer response", "Customer response received" / "Response
window elapsed"), then "Customer accepted?" into "Activate travel pack" and the end event
"Travel pack activated".

## Observations (description only, no interpretation)

- **AI activity - function:** the page's scenario line says "AI agent analyzes the trip,
  predicts acceptance, and generates the best offer."; the container's own tool steps are
  printed as "Check risk and account limits", "Generate offer" and "Predict acceptance
  likelihood".
- **AI activity - element type:** a BPMN sub-process container labelled "AI agent: build
  travel offer" with the ad-hoc tilde marker, i.e. an ad-hoc sub-process; the page states
  the principle as "the agent reasons inside an ad-hoc sub-process, while everything around
  it stays deterministic and controlled".
- **Authority - downstream:** the page names the agent's internal steps and their LLM calls
  when describing the escalation design - "If risk becomes obvious as early as the 'Check
  risk and limits' step, there's no point burning two more LLM calls on 'Generate Offer' and
  'Predict Acceptance'". The figure's own tool labels inside the container are the three
  named tasks.
- **Authority - data:** `not visible on the page` (the figure prints labels only; no
  variables or data objects appear in the brief or in the image).
- **Authority - control:** the page describes the gateway after the agent - "The skill
  instead placed a plain exclusive gateway after the agent finishes—meaning the agent runs
  through all its steps first, and only then does a separate check to see whether the risk
  score came back high."; in the figure those are the gateways "High risk score?", "Offers
  ready", "Compliance pass?" and "Customer accepted?", plus the human task "Review high risk
  offer" on the "High risk" branch.
- **Input provenance:** the page gives the scenario - "A customer is about to travel. The AI
  agent analyzes the trip and prepares a personalized offer while ensuring it complies with
  business rules."; in the figure the trip data reaches the agent through "Identify
  customer", "Enrich trip context" and "Check offer eligibility" after the "Travel event
  detected" start event.
- **Guards present:** the human task "Review high risk offer" (with the reviewer's
  "Create manually" / "Cancel" outcomes) on the high-risk branch, and the compliance check
  step "Run compliance check" with the gateway "Compliance pass?"; the page also describes
  the alternative guard the author would have preferred - "the agent can signal 'I need a
  human' at any point during its run, without waiting for all internal steps to finish".
- **Prompt / model detail visible:** `not visible on the page` for the in-process agent - no
  model id, system prompt or tool definition is printed. The page does name the design-time
  assistant and its model family: "I used Camunda's published open-source AI Skills with
  Claude", "I took Camunda's open-source AI skills, compatible with Claude Code, the Claude
  desktop app, Cursor, GitHub Copilot, and other AI agents", and "I ran Claude from the
  command line, locally on my machine, instead of the usual chat interface."

## Notes for the researcher

The rulings' `capture:` line offers two alt texts, "Resulted BPMN by AI" or "BPMN diagram
generated by AI". The captured file is the first of these
(`020_resulted-bpmn-by-ai.png`, alt "Resulted BPMN by AI"), because it is the one that
carries the AI element visibly: its container is labelled "AI agent: build travel offer" and
carries the ad-hoc tilde, whereas the other candidate (alt "BPMN diagram generated by AI",
which shows the shipment-delay process with an "Investigate delay" container) has no AI
label anywhere on the diagram. Both were downloaded and compared; the second was deleted so
that only the recorded artefact remains.

Every task in the captured figure except the human step carries the same gear glyph, and no
task carries an AI connector icon, so the only visible marker of the AI element is the
container's label and the ad-hoc tilde. Label legibility is good at 1400 px (verified by
enlarging the container). `needs_visual_check` stays true because whether the container is
itself the agent or merely holds the agent's steps is a reading of its label, not something
the page states in the figure's terms.
