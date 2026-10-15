---
n: 4
source: uipath-marketplace
source_name: UiPath Studio Web template gallery (Maestro BPMN solutions)
source_type: vendor marketplace
title: "Insurance Claims Adjudication & Settlement"
url: https://cloud.uipath.com/masterthesismetz/studio_/templates
accessed: 2026-10-11
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "Exported .bpmn 2.0 XML (bpmn:definitions with uipath namespace, bpmn:process, bpmndi diagram interchange) from the solution created via 'Create in Local Workspace'."
bpmn_evidence_quote: "bpmn:process id='Process_1'"
ai_evidence: "Four service tasks with Orchestrator.StartAgentJob and tag caseTaskType=agent: 'Validate Claim Against Policy Terms & Limits Agent', 'Fraud Scoring Agent (patterns, history, anomalies)', 'Estimate Claim Payout Agent (rules engine + adjuster input)', 'Check Reinsurance Applicability Agent (treaty thresholds)'."
ai_evidence_quote: "Fraud Scoring Agent (patterns, history, anomalies)"
artefacts:
  screenshot: null
  archive: "Insurance Claims Adjudication & Settlement/"
  bpmn_xml: 004_insurance-claims-adjudication-and-settlement.bpmn
duplicate_of: null
access: free-account
capture_source: bpmn-xml
capture_quality: legible
capture_width_px: null
capture_method: researcher exported the solution from the Studio Web template gallery ('Create in Local Workspace'); .bpmn copied from the solution folder
---

## What the page shows

Gallery card (Templates tab, filter 'Maestro BPMN', search 'AI'), verbatim:

> "An agentic process built with Maestro, modeled using BPMN to coordinate policy validation, fraud scoring, payout estimation, reinsurance checks, and settlement issuance."

Card footer: "Created by UiPath", "Used in 21 automations", type "Solution".

Message start 'Claim Ready for Adjudication', agent validation, gateway 'Coverage Valid?', parallel fraud scoring / payout estimation / reinsurance check, user task 'Claims Officer Review & Final Decision', full or partial settlement payment with payment-confirmation waits.

## Observations (description only, no interpretation)

- **AI activity - function:** Four service tasks with Orchestrator.StartAgentJob and tag caseTaskType=agent: 'Validate Claim Against Policy Terms & Limits Agent', 'Fraud Scoring Agent (patterns, history, anomalies)', 'Estimate Claim Payout Agent (rules engine + adjuster input)', 'Check Reinsurance Applicability Agent (treaty thresholds)'.
- **AI activity - element type:** Service tasks with implementation Orchestrator.StartAgentJob, no agent bound (no agent project in the solution, output 'sampleOutput').
- **Authority - downstream:** Not visible on the page: agents have no bound tools.
- **Authority - data:** not visible on the page
- **Authority - control:** 'Coverage Valid?' after validation agent; 'Fraud Risk?' (High -> user task 'Fraud Investigator Review'); all branches join before user task 'Claims Officer Review & Final Decision', which precedes payments.
- **Input provenance:** Message start event 'Claim Ready for Adjudication'; data mappings not modelled.
- **Guards present:** User tasks 'Fraud Investigator Review' (High risk) and 'Claims Officer Review & Final Decision' before payment; timer SLA boundaries escalate.
- **Prompt / model detail visible:** not visible on the page

## Notes for the researcher

Researcher pre-vetted this template (2026-10-11). Full solution export kept in `Insurance Claims Adjudication & Settlement/`. Industry template: agent tasks are placeholders with no agent bound (a blank scaffold whose tasks are AI-bound by type).
