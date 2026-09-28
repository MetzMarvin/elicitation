---
n: 227
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: Why AI Agents Need Orchestration
url: https://camunda.com/blog/2025/02/why-ai-agents-needs-orchestration/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "captured figure 2 (page alt \"Screenshot\", 1024x471 source): a BPMN collaboration the page uses for its support-ticket scenario - a \"Front end Application\" pool on top and an \"Orchestration Engine\" pool below, containing the task \"Question has come in\" (start), the two tasks \"Decide on Best Agent - LLM\" and \"Decide on Best Agent - Gemini\", a parallel gateway, \"Review Consensus\", an event-based gateway with three labelled branches (\"Generic Question\", \"Camunda Specific Question\", \"No trustworthy response possible\") into \"Ask ChatGPT\" and \"Camunda Kapa ia Instance\", the end event \"No ideal agent for this query\", then \"Generate response\", the exclusive gateway \"How trusted is the response\" with flows \"Very\" and \"Not very\", \"Send response\", the tasks \"Get Ticket information\" and \"Post response to ticket\", the end event \"Ticket updated\", and a \"Ticketing System\" pool at the bottom; the page also names BPMN in prose"
bpmn_evidence_quote: "Building this with an orchestrator like Camunda that uses BPMN would be pretty easy."
ai_evidence: the captured figure shows two tasks that carry the OpenAI connector icon - "Ask ChatGPT" and "Generate response" - and a third LLM branch reached through the flow labelled "Camunda Specific Question"; the page's own justification for AI inside the process is the ad-hoc sub-process sentence, but no ad-hoc sub-process container is visible in the captured figure, so whether the page's "AI agent" is bound to a process element remains unresolved
ai_evidence_quote: "BPMN has a construct called an ad-hoc subprocess in which a small part of the process decision-making can be handed over to a human"
artefacts:
  screenshot: 011_why-ai-agents-needs-orchestration.png
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

The post argues that AI agents cannot be trusted with consequential action until an
orchestrator decides when and why they are called, and illustrates the argument with a
support-ticket scenario: a customer question enters through a "Front end Application"
pool, an "Orchestration Engine" pool decides which agent is best suited, queries either
"Ask ChatGPT" (flow "Generic Question") or "Camunda Kapa ia Instance" (flow "Camunda
Specific Question"), reviews the answers in "Review Consensus", and only when the response
is trusted ("Very") goes on to "Get Ticket information" and "Post response to ticket"
against the "Ticketing System" pool. The captured figure 2 is that model; its labels are
readable at the downloaded width.

The page's AI sentences are about how an agent's freedom should be bounded, not about a
particular model bound into the diagram: "BPMN has a construct called an ad-hoc subprocess
in which a small part of the process decision-making can be handed over to a human or
agent."

## Observations (description only, no interpretation)

- **AI activity - function:** the page frames the agent as the thing that makes the choice
  of answer and whose reasoning is not visible - "The biggest reason to distrust AI agents
  is that, in most cases, you'll never be able to get a good answer to why a result was
  given"; the tasks it shows doing that are "Ask ChatGPT" and "Generate response".
- **AI activity - element type:** not resolvable from the page - the text's AI mechanism is
  an ad-hoc sub-process ("BPMN has a construct called an ad-hoc subprocess in which a small
  part of the process decision-making can be handed over to a human or agent"), whereas the
  captured figure shows ordinary rounded-rectangle tasks ("Ask ChatGPT", "Generate
  response", "Decide on Best Agent - LLM", "Decide on Best Agent - Gemini") and no ad-hoc
  sub-process container.
- **Authority - downstream:** the branch labelled "Very" leads to "Get Ticket information"
  and "Post response to ticket", which the page describes as "accessing the ticketing
  system to find the relevant ticket and then updating the ticket with a trustworthy
  answer"; the "Not very" branch leads to "Send response".
- **Authority - data:** `not visible on the page` (the figure prints labels only; no
  variables or data objects appear in it).
- **Authority - control:** the parallel gateway after the two "Decide on Best Agent" tasks,
  the event-based gateway that fans out to the three answer sources, and the exclusive
  gateway "How trusted is the response" whose "Very" / "Not very" flows gate the ticket
  update.
- **Input provenance:** the ticket text itself - the start of the model is "Question has
  come in", and the page's scenario is a Camunda customer's support ticket about "getting
  the first element in an array".
- **Guards present:** the trust gateway "How trusted is the response" and the review step
  "Review Consensus"; the page also says a human is needed to look over an agent's chain of
  thought.
- **Prompt / model detail visible:** `not visible on the page` - the figure names no model,
  prompt or parameter; the page mentions Gemini and ChatGPT only as tools the author uses
  in his own work.

## Notes for the researcher

Unresolved by design: the rulings verdict for this post is UNCERTAIN and I did not change
it, but the captured figure does contain LLM-bound tasks ("Ask ChatGPT", "Generate
response", each carrying the OpenAI connector icon) and a second LLM branch reached via the
flow labelled "Camunda Specific Question". What the figure does *not* show is the ad-hoc
sub-process the page names as the AI construct, which is the hesitation the question
records. The figure's own alt text is only "Screenshot" - it does not name BPMN - so the
BPMN reading rests on the image itself (pools, tasks, parallel and event-based gateways,
labelled flows, end events) plus the page's prose mention of BPMN. The downloaded file is
1400x644 although the source asset is 1024x471 (the CDN upscaled it); labels are readable.

One label in the figure is only partly legible: the third answer source reads "Camunda Kapa
ia Instance" (an internal name I could not resolve with certainty), so it is not quoted as
evidence anywhere above.
