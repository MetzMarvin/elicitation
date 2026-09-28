---
n: 206
source: aletyx
source_name: Aletyx (Kogito AI add-ons, aletyx.ai)
title: "Intelligent Process Automation - a BPMN hiring process drawn in full, with the page's AI Agent Node named only in prose"
url: https://aletyx.ai/intelligent-process-automation/
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: >-
  The page asserts an AI Agent node inside the process ("AI Agent Node integrates LLMs directly
  into your process flow.", "AI Agent nodes allow LLMs to safely execute intelligent tasks
  directly within your process flow."), but the only BPMN figure it draws (the hiring process)
  shows no AI-labelled element. Artefact, or product claim that stays E2-no-ai-element?
needs_visual_check: false
bpmn_evidence: "a complete BPMN 2.0 process diagram for a hiring process: a green start event, 'New Hiring', 'Create Offer', 'HR Interview' and 'IT Interview' (the latter two drawn with the person icon of a user task and carrying yellow boundary timer events), 'Send notification HR Interview avoided', 'Send Offer to Candidate', 'Application denied', two diverging exclusive gateways drawn as orange X-diamonds, and two red end events"
bpmn_evidence_quote: "AI Agent Node integrates LLMs directly into your process flow."
ai_evidence: "asserted in prose only. The drawn process contains no AI-labelled node: its boxes are New Hiring, Create Offer, HR Interview, IT Interview, Send notification HR Interview avoided, Send Offer to Candidate and Application denied - ordinary BPMN service and user tasks. The page's AI Agent Node claim, and its companion claim that 'AI Agent nodes allow direct LLM invocation', describe platform capability rather than an element the diagram shows"
ai_evidence_quote: "AI Agent nodes allow LLMs to safely execute intelligent tasks directly within your process flow."
artefacts:
  screenshot: 004_intelligent-process-automation.png
  assets: [004_intelligent-process-automation.png]
  bpmn_xml: []
  archive: null
duplicate_of: null
access: public
capture_source: page-figure
capture_quality: legible
capture_width_px: 1448
capture_method: "the page figure 49ed8131_aletyx-product-process-automation-v2.CaM5TiYC_ZygHUl.webp (34546 B) downloaded from aletyx.ai and converted to PNG on 2026-09-25; the page's other figures are a code listing, the KIE logo and a video thumbnail"
judgment: true
---

## What the artefact is

`https://aletyx.ai/intelligent-process-automation/`, the vendor's "Intelligent Process
Automation" product page, figure `49ed8131_aletyx-product-process-automation-v2.CaM5TiYC_ZygHUl.webp`
(34 546 B, 1448 x 1086). It is a clean, uncluttered BPMN 2.0 render on a dark dotted canvas
(the vendor's own product illustration, not a screenshot of an editor).

## Observations (description only, no interpretation)

- Main path: green start event -> "New Hiring" -> exclusive gateway (orange X-diamond) ->
  "Create Offer" -> "HR Interview" (user task, person icon; yellow boundary timer) ->
  "IT Interview" (user task, person icon; yellow boundary timer) -> exclusive gateway ->
  "Send Offer to Candidate" -> red end event.
- Exception path: the first gateway also flows down and across to the final gateway; both
  interview timers flow into a common gateway that triggers "Send notification HR Interview
  avoided", which flows into the final gateway, whose other branch is "Application denied"
  -> red end event.
- Every box carries either the "script/service" glyph (a small scroll) or the user-task
  person icon. There is no AI badge, no bot icon and no LLM-labelled node anywhere in the
  diagram; the only colour coding is the orange of the gateways and the green/red of the
  start and end events.
- The page's other figures on this URL: `db6340ba_code-image` (a code listing),
  `7c58a5bb_kie-logo` (logo), `ae32711f_video-thumbnail` (video thumbnail). None is a model.

## Notes for the researcher

Same pattern as record 003, in a cleaner drawing: the prose places an "AI Agent Node" inside
"your process flow", the picture shows a hiring process whose every element is an ordinary
BPMN task. `/enterprise-kogito/` (record 003) and `/aletyx-vs-bamoe-vs-apache-kie/` and
`/enterprise-kie-server/` carry the same claim in different words.

The only diagram in this source in which the AI node is actually drawn is the vendor's GitHub
example (record 001): `examples/quarkus/src/main/resources/process.bpmn`, a task with
`drools:taskName="AletyxAI"` named "Aletyx Intelligence" sitting inside an ad-hoc sub-process
with the three human tasks it drives.

The page's remaining AI mentions (the hero line "Aletyx orchestrates your IT systems, people,
and AI agents.", "accountable AI", "generative AI") were not excluded as marketing material;
marketing material is the evidence base here. This row is `UNCERTAIN` only because the ruling
question above is not mine to answer.
