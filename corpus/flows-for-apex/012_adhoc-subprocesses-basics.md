---
n: 329
source: flows-for-apex
source_name: Flows for APEX (FlowQuest; flowsforapex.org docs, flowquest.net, GitHub)
source_type: vendor docs
title: Adhoc Sub Processes: Basics and Manual Runtime
url: https://flowquest.net/adhoc-subprocesses-basics/
accessed: 2026-09-24
verdict: UNCERTAIN
needs_human_ruling: true
question: "The page's BPMN ad-hoc sub-process shows Control Mode 'Manual' and ordinary user tasks, but its runtime screenshot shows a 'Manually Invoke AI' button, an 'AI Decisions' panel and activity descriptions referring to an 'AI wake cycle' - is the runtime artefact of the manual-mode AHSP an AI-in-process artefact to collect, or is the AI out of scope because the model itself is Manual?"
needs_visual_check: false
bpmn_evidence: BPMN ad-hoc sub-process diagram in the modeler (expanded ad-hoc sub-process, ad-hoc marker, boundary events) with its properties panel open; second artefact is the runtime APEX app for the same process
bpmn_evidence_quote: "EXPANDED AD HOC SUB PROCESS / Luggage Finder Workbench"
ai_evidence: the runtime screenshot carries a "Manually Invoke AI" button, an "AI Decisions" panel and activity text describing an "AI wake cycle"; the BPMN model itself is Control Mode "Manual"
ai_evidence_quote: "Manually Invoke AI"
artefacts:
  screenshot: 012_261-manual-ahsp-definition.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 2186
capture_method: curl -L on both asset srcs read from the page DOM; a second asset, 012_261-manual-ahsp-definition.png (1846x951), is the modeler view of the same process with its properties panel
---

## What the page shows

The "basics and manual runtime" half of the ad-hoc sub-process documentation, and the page
that the AI agentic page cross-references. Its BPMN diagram is an expanded ad-hoc
sub-process named "Luggage Finder Workbench" (ID `Activity_lost_ahsp`) inside a larger "bag
reported missing" -> "bag returned" process, with six inner activities: "check airline luggage
system", "rebook onward flights", "check airport luggage systems", "schedule local delivery",
"issue toilets voucher", "declare luggage lost". Its properties panel prints the decisive
field: **Control Mode "Manual"**. The second artefact is the runtime APEX application for
the same case: the "Airport_Lost_Baggage" app's Case Manager showing case 662 (Emily
Thompson, bag tag BA123456) with four startable activities - "check airline luggage system",
"check airport luggage systems", "declare luggage lost", "request human assistance" - an
activity log, and two controls in the right-hand panel: a **"Manually Invoke AI"** button and
below it an **"AI Decisions"** region. The activity descriptions on this screen refer to the
AI runtime: "do not call it repeatedly in the same AI wake cycle when the prior result shows
no material change", and "Request human assistance when automated processes cannot resolve
the case".

## Observations (description only, no interpretation)

- **AI activity - function:** on the runtime screen, an operator can invoke AI manually for
  the case ("Manually Invoke AI"); the case records AI decisions in a dedicated panel. The
  activity text constrains the AI's behaviour ("do not call it repeatedly in the same AI wake
  cycle when the prior result shows no material change").
- **AI activity - element type:** not visible in BPMN terms on this page. The BPMN diagram is
  an ad-hoc sub-process whose Control Mode is **Manual**; the AI surfaces only in the runtime
  application UI for the same process. The source's own words position this page as the
  non-AI half: "For AI -powered and agentic Adhoc Sub Processes, see Adding AI and Agentic
  Adhoc".
- **Authority - downstream:** the startable activities the process can perform: "check airline
  luggage system", "check airport luggage systems", "rebook onward flights", "schedule local
  delivery", "issue toilets voucher", "declare luggage lost"; plus an explicit "request human
  assistance" activity.
- **Authority - data:** the completion condition is a process variable expression -
  "F4A$bag_status = 'DELIVERED'"; the starting-activities expression is "Activity_ck_airline".
  The runtime log shows results written per activity ("Toilettes voucher issued with code:
  VOUCHER-20260415091259", "Deep airport search for bag BA123456 at LHR: Not found in airport
  systems ( Attempt 2)").
- **Authority - control:** the ad-hoc sub-process is entered from "Email acknowledgement sent
  to passenger", exits to "deliver bag to passenger" / "email report to passenger" (bag
  returned) or through non-interrupting boundary events to "send claim link to passenger" ->
  "process claim".
- **Input provenance:** the passenger's bag report (the case), and the airline baggage systems
  the activities query.
- **Guards present:** a "request human assistance" activity ("Request human assistance when
  automated processes cannot resolve the case or when passenger requires special handling");
  a timer boundary event on the sub-process; a case-level "Advance Demo Time" control. The
  runtime screen also exposes a "Manually Invoke AI" control, i.e. an explicit human trigger
  for the AI step.
- **Prompt / model detail visible:** no prompt text, provider or model name on this page; the
  only model reference is the runtime's "AI Decisions" panel. The completion condition quoted
  above is configuration, not a prompt.

## Notes for the researcher

This is the page the agentic page (record 003) sends readers to, and the pair is the source's
own manual/AI contrast: this one documents Control Mode "Manual", record 003 documents Control
Mode "AI" with provider anthropic and model claude-sonnet-4-5. The two AHSP diagrams are
**not** the same image (different files, 1846x951 vs 1755x962, different SHA-256; this one
shows "Luggage Finder Workbench" with Control Mode Manual, record 003's shows the same process
name with Control Mode AI and an AI Objective field). The judgement call this record asks for
is whether the runtime screen's "Manually Invoke AI" / "AI Decisions" surfaces are an
AI-in-process artefact to collect even though the model on the same page is Manual.
