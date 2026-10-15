---
n: 5
source: uipath-marketplace
source_name: UiPath Studio Web template gallery (Maestro BPMN solutions)
source_type: vendor marketplace
title: "Claim Submission & Status (Provider to Payer)"
url: https://cloud.uipath.com/masterthesismetz/studio_/templates
accessed: 2026-10-11
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "Exported .bpmn 2.0 XML (bpmn:definitions with uipath namespace, bpmn:process, bpmndi diagram interchange) from the solution created via 'Create in Local Workspace'."
bpmn_evidence_quote: "bpmn:process id='Process_1'"
ai_evidence: "Three service tasks with Orchestrator.StartAgentJob: 'Validate Coding & Modifiers Agent (ICD, CPT, DRG)', 'Check Completeness Agent (attachments, clinical notes, required fields)', 'Rejection Reason Parsing & Worklisting Agent'."
ai_evidence_quote: "Rejection Reason Parsing & Worklisting Agent"
artefacts:
  screenshot: null
  archive: "Claim Submission & Status (Provider to Payer)/"
  bpmn_xml: 005_claim-submission-and-status-provider-to-payer.bpmn
duplicate_of: null
access: free-account
capture_source: bpmn-xml
capture_quality: legible
capture_width_px: null
capture_method: researcher exported the solution from the Studio Web template gallery ('Create in Local Workspace'); .bpmn copied from the solution folder
---

## What the page shows

Gallery card (Templates tab, filter 'Maestro BPMN', search 'AI'), verbatim:

> "An agentic process built with Maestro, modeled using BPMN to manage claim validation, eligibility checks, clearinghouse submission, payer acknowledgments, and status tracking."

Card footer: "Created by UiPath", "Used in 13 automations", type "Solution".

Message start 'Claim Ready for Submission', parallel pre-submission validations (coding agent, eligibility service task, completeness agent), 'Submit Claim to Clearinghouse (837 EDI)', 'Transmit Claim to Payer', payer response handling with 'Rejection Reason Parsing & Worklisting Agent'.

## Observations (description only, no interpretation)

- **AI activity - function:** Three service tasks with Orchestrator.StartAgentJob: 'Validate Coding & Modifiers Agent (ICD, CPT, DRG)', 'Check Completeness Agent (attachments, clinical notes, required fields)', 'Rejection Reason Parsing & Worklisting Agent'.
- **AI activity - element type:** Service tasks with implementation Orchestrator.StartAgentJob, no agent bound.
- **Authority - downstream:** Not visible on the page: agents have no bound tools.
- **Authority - data:** not visible on the page
- **Authority - control:** 'Coding Valid?' (Invalid -> user task 'Coder Correction'); completeness agent error boundary 'Missing Data' -> user task 'Staff Correction'; merge -> automated clearinghouse submission and payer transmission; denial parsing agent -> end 'Claim Rejected: Payer Denial'.
- **Input provenance:** Message start 'Claim Ready for Submission'; payer denial message ('Payer Denied Claim') feeds the parsing agent; data mappings not modelled.
- **Guards present:** Error boundary to human 'Staff Correction'; 'Coder Correction' on invalid coding.
- **Prompt / model detail visible:** not visible on the page

## Notes for the researcher

Researcher pre-vetted this template (2026-10-11). Full solution export kept in `Claim Submission & Status (Provider to Payer)/`. Industry template: agent tasks are placeholders with no agent bound.
