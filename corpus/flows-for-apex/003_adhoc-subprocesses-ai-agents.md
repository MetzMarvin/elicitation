---
n: 328
source: flows-for-apex
source_name: Flows for APEX (FlowQuest; flowsforapex.org docs, flowquest.net, GitHub)
source_type: vendor blog
title: Adhoc Sub Processes with AI Agents
url: https://flowquest.net/adhoc-subprocesses-ai-agents/
accessed: 2026-09-24
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: figure image (261-autonomous-ahsp-definition.png, 1755x962) showing the BPMN diagram beside the modeller's expanded ad-hoc sub-process properties panel
bpmn_evidence_quote: "EXPANDED ADHOC SUB PROCESS / Lost Luggage Agent"
ai_evidence: Control Mode is set to "AI" on the ad-hoc sub-process, with AI Interface, AI Service, AI Provider "anthropic", AI Model "claude-sonnet-4-5" and a full AI Objective prompt
ai_evidence_quote: "Control Mode AI"
artefacts:
  screenshot: 003_261-autonomous-ahsp-definition.png
  archive: 003_adhoc-subprocesses-ai-agents.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1755
capture_method: curl -L on https://flowquest.net/assets/images/261-autonomous-ahsp-definition.png, src read from the page DOM
---

## What the page shows

The same baggage-recovery diagram as record 002, captured with the modeller's properties panel
open beside it. The panel is headed "EXPANDED ADHOC SUB PROCESS / Lost Luggage Agent" and gives
Name "Lost Luggage Agent", ID "Activity_lost_ahsp", Subject "Autonomous Luggage Agent - Case
:F4A$BUSINESS_REF - :F4A$PAXNAME, :F4A$ORIGIN-:F4A$DESTINATION" and **Control Mode "AI"**. The
AI section reads: AI Interface "UC_AI", AI Service "UC_AI_SERVICE", AI Provider "anthropic", AI
Model "claude-sonnet-4-5", followed by the AI Objective prompt beginning "You are managing a
delayed long-haul baggage recovery case." The page text states: "or APEX 26.1 adds
recommendation, hybrid, and autonomous AI control modes to Adhoc Sub Processes."

## Observations (description only, no interpretation)

- **AI activity - function:** drives the ad-hoc sub-process. The AI Objective states a "Business
  state model" (MISSING, LOCATED, TRANSPORT_BOOKED, EN_ROUTE, ARRIVED, DELIVERY_SCHEDULED,
  DELIVERED) and a seven-step "Decision sequence": "1. Search and confirm physical location.
  2. Book onward transport when the bag is LOCATED. 3. Wait while the bag is TRANSPORT_BOOKED
  until it departs. 4. Wait while the bag is EN_ROUTE. 5. Arrange local delivery once the bag is
  ARRIVED. 6. Wait while the bag is DELIVERY_SCHEDULED until courier dispatch. 7. Complete only
  when the bag is DELIVERED or the model completion condition is satisfied."
- **AI activity - element type:** an ad-hoc sub-process with Control Mode set to "AI" - the model
  chooses which contained activity to run and when to complete. The page distinguishes three
  modes: "recommendation, hybrid, and autonomous AI control modes".
- **Authority - downstream:** the contained activities it may invoke are the diagram's tasks:
  "check airline luggage system", "check airport luggage systems", "issue toiletries voucher",
  "rebook luggage to destination", "get local delivery details from customer", "arrange local
  delivery", "request human assistance", "declare luggage lost".
- **Authority - data:** "Process Variables To Submit: [bag_tag, bag_status, bag_location,
  bag_info, delivery_committed, case_resolved, demo_offset_hours]" (Array of Strings).
- **Authority - control:** completion is governed by a "Completion Condition" whose "Condition
  Type" is "Expression"; the panel exposes control limits "Review Interval Seconds: 10", "Turns
  Per Session: 4", "Max Total Turns: 20". Boundary markers lead to "Escalate for Human
  Assistance" or to "send claim link to passenger" -> "process claim".
- **Input provenance:** the variables listed under "Process Variables To Submit", plus the
  Subject line's case identifiers (:F4A$BUSINESS_REF, :F4A$PAXNAME, :F4A$ORIGIN,
  :F4A$DESTINATION) - instance data, not an external document.
- **Guards present:** the prompt's own operating rules are visible verbatim, e.g. "Only book
  onward transport once the bag is physically LOCATED." and "Only arrange local delivery once
  the bag has ARRIVED at the destination airport."; the loop is bounded by "Turns Per Session 4"
  and "Max Total Turns 20"; the process retains "get local delivery details from customer" and
  "request human assistance" as human steps, plus an "Escalate for Human Assistance" path.
- **Prompt / model detail visible:** AI Provider "anthropic" (the field's example text is
  "anthropic, openai"), AI Model "claude-sonnet-4-5" (example text "q, claude-sonnet-4-5"), AI
  Interface "UC_AI", AI Service "UC_AI_SERVICE", and the full AI Objective prompt quoted above.

## Notes for the researcher

This and record 002 show the same process; this capture is the more valuable one because the
properties panel exposes the binding (provider, model, prompt, turn limits) that the diagram
alone hides. The page also publishes `261-ahsp-recommendation-app.png` (alt "Recommendation
Mode"), saved here as `003_261-ahsp-recommendation-app.png`: an application screenshot of the
recommendation-mode UI, not a BPMN diagram, kept only as supporting evidence.
