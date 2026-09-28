---
n: 231
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Hospital Integration Blueprint
url: https://marketplace.camunda.com/apps/778691/hospital-integration-blueprint
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: A published canvas of the discharge-to-claim flow: start event 'Patient Discharge Initiated' -> gateway -> six tasks, of which 'Validate Discharge Information (AI-Powered)', 'Prepare Claim Data (AI-Powered)', 'Submit Insurance Claim (AI-Powered)', 'Analyze Nursing Requirements', 'Intelligent Nurse Assignment (AI-Powered)' and 'Update Patient Records' all carry the violet AI glyph, plus 'Review Claim Rejection' (grey glyph) -> gateways 'Claim Approved?' and the merge/approval gateways -> 'Process Payment' -> end event 'Process Complete'; the nursing branch ('Analyze Nursing Requirements' -> 'Intelligent Nurse Assignment (AI-Powered)') rejoins the same end. The second published image shows the wider healthcare workflow with further violet-marked tasks.
bpmn_evidence_quote: "Validate Discharge Information (AI-Powered)"
ai_evidence: Six violet AI-glyph tasks in one published process, several of them literally named '(AI-Powered)'. The page's own feature list confirms the bindings and names the provider: 'AI-Powered Patient Discharge to Claim Processing :: ... using AWS Bedrock (Mistral 7B) ... uses dynamically generated AI prompts with full healthcare context including ICD-10 codes, CPT codes, and DRG classifications.', with further AI sub-solutions described - 'Emergency Department Workflow with Intelligent Triage' (AI-powered symptom analysis and triage scoring), 'Agentic AI Prior Authorization' (an autonomous agent system with goal-oriented planning, self-directed execution and confidence-based decision-making), 'AI-Optimized Nurse Scheduling' (Bedrock over historical staffing data, acuity levels and skills) and 'Real-Time Resource Management' with AI-driven conflict resolution.
ai_evidence_quote: "uses dynamically generated AI prompts with full healthcare context including ICD-10 codes, CPT codes, and DRG classifications."
artefacts:
  screenshot: 231_hospital-integration-blueprint.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: listing-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own assets (d3bql97l1ytoxn.cloudfront.net, app_resources/783475/overview/img8014398170544023832-2x.png, 1100x231, and a 1500x372 screenshot of the wider workflow), both read natively at full size
---

## What the page shows

The Hospital Integration Blueprint (Camunda, solution accelerator, 'Listing Only', categories 'Agentic Solutions', 'AI Services', 'Healthcare'). A hospital workflow suite: AI-powered patient discharge and claim processing, emergency-department triage, agentic prior authorization, AI-optimised nurse scheduling and AI-assisted resource management.

## Observations (description only, no interpretation)

- **AI activity - function:** validate discharge information, prepare claim data, submit the insurance claim, analyse nursing requirements, assign nurses, and update patient records - plus, per the page, triage scoring, prior-authorization screening, shift-schedule generation and resource-conflict resolution.
- **AI activity - element type:** serviceTasks carrying the violet AI element glyph (the canvas names six); the human/administrative steps ('Review Claim Rejection', approval gateways) are separate.
- **AI activity - models named:** AWS Bedrock (Mistral 7B) in the page's feature text; the page also describes 'dynamically generated AI prompts with full healthcare context including ICD-10 codes, CPT codes, and DRG classifications'.
- **Authority - downstream:** each AI task is followed by a gateway or an approval - claim data preparation precedes submission, the approval gateways decide payment versus 'Review Claim Rejection', and the nurse-assignment result rejoins the main flow at 'Process Complete'.
- **Authority - control:** the 'Claim Approved?' gateway and the merge/approval gateways, plus the human review of rejections; for the prior-authorization sub-solution the page lists 'confidence-based decision-making'.
- **Data reachable by the model:** clinical and claims context - discharge data, ICD-10/CPT/DRG codes, claim data, nurse skills and historical staffing data (per the feature list).
- **Human role:** claim-rejection review and the approval gateways; nursing and prior-authorization steps are described as autonomous or AI-optimised.
- **Scope note:** the listing is tagged 'Listing Only' and publishes no .bpmn, so the evidence is the two canvases plus the feature prose.

## Notes for the researcher

The largest AI footprint in this batch: six violet-marked tasks inside a single published process, several named '(AI-Powered)', in a clinical setting where the AI touches claims data and staff assignment. Two things the researcher may want to weigh: the page claims a whole suite of AI sub-solutions (triage, prior authorization, scheduling) while the published canvas covers the discharge-to-claim flow plus part of nursing, and the listing is 'Listing Only' with no .bpmn to grep. This is also the batch's only healthcare listing, and the only one naming a specific hosted model (Bedrock / Mistral 7B) in prose while leaving the model field itself unpublished.
