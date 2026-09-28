---
n: 157
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: NICE CXone Connector
url: https://marketplace.camunda.com/apps/797170/nice-cxone-connector
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: The published BPMN contains a task labelled 'Review AI Triage Decision', whose gateway then routes to an automated branch ('Auto-Resolvable' -> 'Send Auto-Resolution to Customer') or to a human-agent branch - but the AI that produced the triage decision is not drawn inside the process, the task's own implementation is not visible in the capture, and the page's prose names no AI technology at all. Does an element whose label references an AI decision count as an AI element inside the process, or must the corpus require an AI-bound element that the artefact itself shows (in which case this listing is E2-no-ai-element)? The capture is in the corpus.
needs_visual_check: false
bpmn_evidence: BPMN diagram published as the listing's own overview asset (Camunda Web Modeler, canvas with palette); no .bpmn downloadable. Read natively: start event -> 'Review AI Triage Decision' -> gateway with the branch 'Auto-Resolvable' (-> 'Send Auto-Resolution to Customer') and the branch 'Human Agent Needed' (-> 'Check CXone Agent Availability' -> 'Create CXone Work Item' -> the sub-process 'Await Resolution (SLA Monitored)' with the tasks 'Waiting Started', 'Wait for Customer Message', 'Resolution Received' and an SLA boundary timer escalating to 'Escalate - Notify Supervisor'); both branches converge at 'Pull Resolution & CSAF Data' -> gateway -> 'Update Case - Update Audit Trail' -> end 'Complaint Resolved & Closed'.
bpmn_evidence_quote: "Review AI Triage Decision"
ai_evidence: The only AI term in the artefact is the label of the process's second element - the task 'Review AI Triage Decision' - whose gateway then routes either to 'Auto-Resolvable' / 'Send Auto-Resolution to Customer' or to a human-agent branch. The AI that produced the triage decision is not drawn anywhere in the process, and the task's own implementation is not visible in the capture (it carries an unbound job, no element-template glyph legible at published size). The page's own copy contains no AI term at all: its features are 'Create work items and route to agents', 'Check agent availability for smart routing' and 'Manage your contact center end-to-end'.
ai_evidence_quote: "Review AI Triage Decision"
artefacts:
  screenshot: 157_nice-cxone-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own assets (d3bql97l1ytoxn.cloudfront.net, app_resources/797170/overview/img14535201668227252220-2x.png, 1100x403); native read at full size - a Camunda Web Modeler canvas
---

## What the page shows

The NICE CXone Connector (Camunda Services GmbH, outbound connector). The listing publishes one model as its overview asset: a contact-center flow that starts from a review of an AI triage decision, either auto-resolves the case or hands it to a CXone agent on a work item, waits for the resolution under a monitored SLA, and closes the case with an audit-trail update.

## Observations (description only, no interpretation)

- **AI activity - function:** none drawn. The process reviews an AI triage decision and can send an auto-resolution, but no AI task, model or service appears in the model.
- **AI activity - element type:** the label 'Review AI Triage Decision' on an ordinary task (no element-template glyph legible at published size, no agent element, no ad-hoc container); the AI system that produced the triage is outside the drawn process.
- **Authority - downstream:** the triage review gates both the automatic branch and the human-agent branch, so the AI decision reaches the customer either as an auto-resolution or as a work item for an agent.
- **Authority - data:** none drawn; the page's feature list mentions CXone queue data and reporting metrics, not triage data.
- **Authority - control:** the gateway immediately after the review (branch labels 'Auto-Resolvable' and 'Human Agent Needed').
- **Authority - control (human):** the 'Human Agent Needed' branch - 'Check CXone Agent Availability' -> 'Create CXone Work Item' -> 'Await Resolution (SLA Monitored)', with a boundary SLA timer escalating to 'Escalate - Notify Supervisor'.
- **Input provenance:** the incoming contact-center case; the AI triage decision is an input the process consumes rather than produces.
- **Guards present:** the two-way branch after the triage review and the SLA boundary timer with its escalation sub-process.
- **Prompt / model detail visible:** none - no model, provider or prompt appears anywhere in the published model, and the task carries no visible binding.

## Notes for the researcher

Kept UNCERTAIN because the classification, not the evidence, is in doubt: the element is legible and the flow is complete, but the AI sits outside the process (the listing is a connector for the contact-center platform, and the triage decision comes from it). This is the first artefact in this source whose AI reference is a human review of an upstream AI decision rather than an AI task inside the flow, so the boundary is worth one ruling rather than a silent decision.
