# AI-Driven Healthcare Orchestration (VHA) — UNCERTAIN (trisotech)

url: https://www.trisotech.com/ai-driven-healthcare-orchestration-presentation/
accessed: 2026-09-25
title: AI-Driven Healthcare Orchestration: Insight from the Veteran Health Administration (HIMSS25 deck, 26 slides)
record: 032

bpmn_evidence:
  Slide 19 ("The Next Generation Digital Health Teams") draws a process model inside a monitor
  mock-up, viewed at full size (2048x1152): a start event, then the tasks "Listen for new data"
  (gear/service marker), "Aggregate risk factor data" (gear/service marker), "CDS risk calculation"
  (decision-table marker) and "Provider 1 determines risk level" (person marker, plus a small round
  badge at the task's top-right corner), an exclusive gateway with the outgoing branches "Probable"
  (to an end event) and "Possible", a feedback path labelled "Unlikely" returning to "Aggregate risk
  factor data", and a data object "CDS recommendation" attached by a dotted data association.
  The task shapes, the gateway and the data association are drawn in the same Trisotech BPMN style
  as the other decks in this source (compare records 027 and 030).

ai_evidence:
  The slide claims AI inside the orchestration in prose: "AI supporting Providers in areas of
  cognitive weakness - Listening for new data - Harmonizing data - Near real time risk calculation",
  and the deck's title is "AI-Driven Healthcare Orchestration". An AI robot is drawn standing above
  the process beside a clinician.
  The uncertainty: the robot is an illustration *above* the flow, and the small round badge on
  "Provider 1 determines risk level" is too small in this frame to resolve - it could be the AI
  performer badge used elsewhere by this vendor, or an ordinary task marker. No AI element is
  unambiguously bound to a task in the published frame.

screenshot: 032_ai-driven-healthcare-orchestration-digital-health-team-process.png
capture_quality: marginal

note for the researcher:
  needs_visual_check. The process itself is legible; what is not resolvable at this resolution is the
  badge on the "Provider 1 determines risk level" task and whether the robot illustration is meant to
  bind to a task. If the badge is the AI performer marker, this is an INCLUDE with the same construct
  as record 027; if it is not, the AI sits outside the model and this is closer to E2.
