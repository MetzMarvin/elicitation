---
n: 6
source: uipath-marketplace
source_name: UiPath Studio Web template gallery (Maestro BPMN solutions)
source_type: vendor marketplace
title: "Insurance First Notice of Loss (FNOL)"
url: https://cloud.uipath.com/masterthesismetz/studio_/templates
accessed: 2026-10-11
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "Exported .bpmn 2.0 XML (bpmn:definitions with uipath namespace, bpmn:process, bpmndi diagram interchange) from the solution created via 'Create in Local Workspace'."
bpmn_evidence_quote: "bpmn:process id='Process_1'"
ai_evidence: "Four service tasks with Orchestrator.StartAgentJob: 'Validate Policy Agent', 'Coverage Validation Agent', 'Fraud Screening Agent', 'Loss Intake Data Enrichment Agent'."
ai_evidence_quote: "Loss Intake Data Enrichment Agent"
artefacts:
  screenshot: null
  archive: "Insurance First Notice of Loss (FNOL)/"
  bpmn_xml: 006_insurance-first-notice-of-loss-fnol.bpmn
duplicate_of: null
access: free-account
capture_source: bpmn-xml
capture_quality: legible
capture_width_px: null
capture_method: researcher exported the solution from the Studio Web template gallery ('Create in Local Workspace'); .bpmn copied from the solution folder
---

## What the page shows

Gallery card (Templates tab, filter 'Maestro BPMN', search 'AI'), verbatim:

> "An agentic process built with Maestro, modeled using BPMN to guide claim intake, coverage checks, fraud screening, claim record creation, and adjuster assignment."

Card footer: "Created by UiPath", "Used in 12 automations", type "Solution".

Message start 'Claim Notification Received (FNOL)', user task 'Collect Incident Details & Evidence', 'Validate Policy Agent', parallel coverage / fraud / enrichment agents, 'Evaluation Outcome', 'Fraud Investigator Review', 'Assign Claims Adjuster', claim record creation, acknowledgement to policyholder.

## Observations (description only, no interpretation)

- **AI activity - function:** Four service tasks with Orchestrator.StartAgentJob: 'Validate Policy Agent', 'Coverage Validation Agent', 'Fraud Screening Agent', 'Loss Intake Data Enrichment Agent'.
- **AI activity - element type:** Service tasks with implementation Orchestrator.StartAgentJob, no agent bound.
- **Authority - downstream:** Not visible on the page: agents have no bound tools.
- **Authority - data:** not visible on the page
- **Authority - control:** 'Policy Active?' after the policy agent; 'Evaluation Outcome' after the join (Coverage Excluded -> end; Fraud Suspicion -> 'Fraud Investigator Review'; else -> user task 'Assign Claims Adjuster'), then record creation and notifications.
- **Input provenance:** Message start 'Claim Notification Received (FNOL)' and user task 'Collect Incident Details & Evidence'.
- **Guards present:** User tasks 'Fraud Investigator Review' and 'Assign Claims Adjuster' before claim record creation; timer SLA boundaries escalate.
- **Prompt / model detail visible:** not visible on the page

## Notes for the researcher

Researcher pre-vetted this template (2026-10-11). Full solution export kept in `Insurance First Notice of Loss (FNOL)/`. Industry template: agent tasks are placeholders with no agent bound.
