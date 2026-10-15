---
n: 7
source: uipath-marketplace
source_name: UiPath Studio Web template gallery (Maestro BPMN solutions)
source_type: vendor marketplace
title: "Patient Appointment Scheduling"
url: https://cloud.uipath.com/masterthesismetz/studio_/templates
accessed: 2026-10-11
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "Exported .bpmn 2.0 XML (bpmn:definitions with uipath namespace, bpmn:process, bpmndi diagram interchange) from the solution created via 'Create in Local Workspace'."
bpmn_evidence_quote: "bpmn:process id='Process_1'"
ai_evidence: "Two service tasks with Orchestrator.StartAgentJob: 'Offer Alternatives / Add to Waitlist Agent', 'Verify Insurance Eligibility Agent'."
ai_evidence_quote: "Offer Alternatives / Add to Waitlist Agent"
artefacts:
  screenshot: null
  archive: "Patient Appointment Scheduling/"
  bpmn_xml: 007_patient-appointment-scheduling.bpmn
duplicate_of: null
access: free-account
capture_source: bpmn-xml
capture_quality: legible
capture_width_px: null
capture_method: researcher exported the solution from the Studio Web template gallery ('Create in Local Workspace'); .bpmn copied from the solution folder
---

## What the page shows

Gallery card (Templates tab, filter 'Maestro BPMN', search 'AI'), verbatim:

> "An agentic process built with Maestro, modeled using BPMN to manage scheduling requests, provider availability checks, insurance eligibility, waitlist handling, and confirmations."

Card footer: "Created by UiPath", "Used in 11 automations", type "Solution".

Message start 'Patient Appointment Request Received', user task 'Capture Patient Preferences', 'Check Provider Availability', alternatives agent with patient response wait, parallel 'Reserve Appointment Slot' and 'Verify Insurance Eligibility Agent', 'Eligibility Result', confirmation generation and sending.

## Observations (description only, no interpretation)

- **AI activity - function:** Two service tasks with Orchestrator.StartAgentJob: 'Offer Alternatives / Add to Waitlist Agent', 'Verify Insurance Eligibility Agent'.
- **AI activity - element type:** Service tasks with implementation Orchestrator.StartAgentJob, no agent bound.
- **Authority - downstream:** Not visible on the page: agents have no bound tools.
- **Authority - data:** not visible on the page
- **Authority - control:** Alternatives agent -> event-based gateway 'Patient Response' (message 'Patient Accepts Alternative' or timer). Eligibility agent -> join -> gateway 'Eligibility Result' (Not Eligible -> cancel; Eligible -> 'Generate Appointment Confirmation', 'Send Confirmation to Patient').
- **Input provenance:** Message start 'Patient Appointment Request Received' and user task 'Capture Patient Preferences'.
- **Guards present:** Timer boundary 'Eligibility Check Delayed' on the eligibility agent -> end 'Escalated: Eligibility SLA Breach'.
- **Prompt / model detail visible:** not visible on the page

## Notes for the researcher

Researcher pre-vetted this template (2026-10-11). Full solution export kept in `Patient Appointment Scheduling/`. Industry template: agent tasks are placeholders with no agent bound. Downloaded first by the researcher.
