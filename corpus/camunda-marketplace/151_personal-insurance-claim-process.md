---
n: 151
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Personal Insurance Claim Process
url: https://marketplace.camunda.com/apps/450145/personal-insurance-claim-process
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: The listing publishes a BPMN collaboration whose AI element is an external black-box participant named 'Gen AI Tool' (confirmed in the .bpmn, alongside the tasks 'Analyze receipt' and 'Identify damage in photo', whose implementations the file does not show), while the listing's own text never mentions AI. Does an external AI participant - or an unbound task whose job type suggests document and photo analysis - count as an AI element inside the process for this corpus, or should the corpus require a visible AI binding (in which case this artefact is E2-no-ai-element)? Both the capture and the .bpmn are in the corpus.
needs_visual_check: false
bpmn_evidence: BPMN collaboration published as the overview asset and as a downloadable .bpmn (process 'Insurance: Personal Property Claim Processing'). Read from the XML: the collaboration has four participants - 'Insurance', 'Customer', 'Insurance IT and CRM systems' and 'Gen AI Tool', the last one a black box with no process reference - and the insurance process holds 'Analyze receipt', 'Identify damage in photo', the sub-process 'Automatic Claim Approval Process' (with the business rule task 'Validate automatic claim business rules'), the user task 'Adjudicate' and the payment and notification tasks.
bpmn_evidence_quote: "Gen AI Tool"
ai_evidence: The .bpmn names the AI participant outright - participant 'Gen AI Tool', which carries no process reference, i.e. the collaboration's black box - and the process contains the tasks 'Analyze receipt' and 'Identify damage in photo', whose implementations are not visible in the file (both are plain Zeebe job types). The listing's own copy contains no AI term at all: its features are 'Faster Claim Processing', 'Enhanced Accuracy', 'Fraud Prevention', 'Improved Customer Experience' and 'Flexibility'.
ai_evidence_quote: "Gen AI Tool"
artefacts:
  screenshot: 151_personal-insurance-claim-process.png
  archive: null
  bpmn_xml: 151_personal-insurance-claim-process.bpmn
duplicate_of: null
access: public
capture_source: bpmn-xml
capture_quality: legible
capture_width_px: 1100
capture_method: curl of the listing's own overview asset (d3bql97l1ytoxn.cloudfront.net, app_resources/450145/overview/img1398435858740523721-2x.png, 1100x592) and of the .bpmn behind the listing's Modeler import link (raw.githubusercontent.com/camunda/camunda-platform-tutorials/main/solutions/insurance-personal-claim-handling/insurance-personal-property-damage-claim-handling.bpmn); the image read natively at full size, plus a 4x zoom crop of the 'Gen AI Tool' participant (fig2), the XML read directly
---

## What the page shows

The Personal Insurance Claim Process (blueprint, partner). The listing publishes the claim handling collaboration - customer, insurance, the insurer's IT/CRM systems and a 'Gen AI Tool' participant - as an image and as the runnable .bpmn: receipt and photo analysis, an automatic claim approval sub-process with its business rules, human adjudication with approved/declined branches, payment and customer notification.

## Observations (description only, no interpretation)

- **AI activity - function:** not visible - 'Gen AI Tool' is a black-box participant; the file says nothing about what is asked of it or where its messages go.
- **AI activity - element type:** an external participant (black-box pool, `participant name="Gen AI Tool"` with no processRef) plus two unbound service tasks ('Analyze receipt', 'Identify damage in photo').
- **Authority - downstream:** the message flows from the participant into the claim process; decisions inside the process run through the gateway after the 'Adjudicate' user task with its 'approved' and 'declined' branches.
- **Authority - data:** claim, policy and customer data ('Get customer and policy data'), the receipt and the damage photo; no data objects are drawn.
- **Authority - control:** the gateway after 'Adjudicate', the business rule task 'Validate automatic claim business rules' inside the automatic approval sub-process, and the payment trigger.
- **Authority - control (human):** the user task 'Adjudicate' - in the drawn flow a human decides the claim - plus the escalation to adjudication that the automatic path falls back to.
- **Input provenance:** the customer's notice of loss with a receipt and a damage photo.
- **Guards present:** the automatic approval path is gated by a business rule task, and anything it does not approve reaches human adjudication; nothing AI-specific is drawn or declared.
- **Prompt / model detail visible:** none - no model, provider or prompt appears in the .bpmn or on the page.

## Notes for the researcher

Correction to the batch-6 record, which rested on the figure alone: the .bpmn confirms the 'Gen AI Tool' participant exists in the published model (no processRef - a black box) and shows two further tasks whose implementation the file does not reveal. The verdict stays UNCERTAIN, but the question is now answerable from the artefact rather than from a screenshot, and it is the same boundary question the corpus needs settled: does the AI have to be a bound activity inside the process, or does a named AI participant count?
