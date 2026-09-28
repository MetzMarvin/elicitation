---
n: 324
source: flows-for-apex
source_name: Flows for APEX (FlowQuest; flowsforapex.org docs, flowquest.net, GitHub)
source_type: vendor blog
title: Flows for APEX 26.1 Features (AI-Driven BPMN Agents)
url: https://flowquest.net/Flows4APEX261Features/
accessed: 2026-09-24
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: figure image (ahsp-261-autonomous-def.png, 1624x812) showing a BPMN diagram with a bordered ad-hoc sub-process, three grouped regions, boundary markers and named end events
bpmn_evidence_quote: "Move from recommendations to hybrid or fully autonomous BPMN-defined agents while keeping workflow behavior auditable and governed."
ai_evidence: the ad-hoc sub-process "Lost Luggage Agent" is the AI-controlled unit; the image's alt text is "AI-Driven BPMN Agents"
ai_evidence_quote: "AI-Driven BPMN Agents"
artefacts:
  screenshot: 002_ahsp-261-autonomous-def.png
  archive: 002_flows4apex261features.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1624
capture_method: curl -L on /assets/images/ahsp-261-autonomous-def.png, src read from the page DOM
---

## What the page shows

A baggage-recovery process. After the start event "bag reported missing", the task "Email
acknowledgement to passenger" leads into a large bordered **ad-hoc sub-process named "Lost
Luggage Agent"**, inside which three dashed regions group the available activities: "LOCATE"
("check airline luggage system", "check airport luggage systems", "issue toiletries voucher"),
"REBOOK" ("rebook luggage to destination") and "ARRANGE DELIVERY" ("get local delivery details
from customer" -> "arrange local delivery"). Two further activities sit outside the regions:
"request human assistance" and "declare luggage lost". After the sub-process, "deliver bag to
passenger" and "email report to passenger" lead to the end event "bag returned". Two side paths
leave through boundary markers: one to "Escalate for Human Assistance", and one through "send
claim link to passenger" -> "process claim" to the end event "claim paid".

## Observations (description only, no interpretation)

- **AI activity - function:** controls the ad-hoc sub-process. The page's own heading is
  "AI-Driven BPMN Agents" with the text "Move from recommendations to hybrid or fully autonomous
  BPMN-defined agents while keeping workflow behavior auditable and governed."
- **AI activity - element type:** the ad-hoc sub-process itself is the delegated unit ("Lost
  Luggage Agent"); the tasks inside it are the activities it may choose among. No AI-specific
  node type is drawn - the sub-process carries the delegation.
- **Authority - downstream:** the activities inside the sub-process, named exactly as printed:
  "check airline luggage system", "check airport luggage systems", "issue toiletries voucher",
  "rebook luggage to destination", "get local delivery details from customer", "arrange local
  delivery", "request human assistance", "declare luggage lost". Downstream of the sub-process:
  "deliver bag to passenger", "email report to passenger", and the claim line "send claim link to
  passenger" -> "process claim".
- **Authority - data:** not visible on the page.
- **Authority - control:** the completion markers at the sub-process boundary lead either to
  "Escalate for Human Assistance" or to "send claim link to passenger" / "process claim".
- **Input provenance:** not visible on the page; the start event is "bag reported missing".
- **Guards present:** a human-assistance path - the activity "request human assistance" inside the
  sub-process and the "Escalate for Human Assistance" task reachable from the boundary marker.
- **Prompt / model detail visible:** not visible on this image. The same artefact re-published on
  the "AI agents" page (record 003) shows the properties panel with provider, model and the full
  AI Objective prompt.

## Notes for the researcher

This page publishes five images; only `ahsp-261-autonomous-def.png` is a BPMN-with-AI artefact.
The other four are `ahsp-261-manual-def.png` (manual ad-hoc sub-process, no AI),
`async-task-261.png`, `261-dev-features.png`, and `261-ai-dev-bundle.png` (alt text "AI
Development Support Toolkit" - an illustration, not a BPMN diagram). The same image is
re-published on flowquest.net/releases (ledger row E3, duplicate_of this record).
