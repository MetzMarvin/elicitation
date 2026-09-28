---
n: 187
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Credit Card Onboarding Process
url: https://marketplace.camunda.com/apps/616063/credit-card-onboarding-process
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: The page claims an AI-bound element inside this blueprint - 'Camunda IDP can extract the application form data ... harnessing AI models for smart data extraction' - while the published canvas shows no extraction task at all: the three automation tasks of the credit-check chain carry generic service-task and decision-table glyphs, and the diagram is cut off at its bottom pool ('Bank System Data'), whose contents are not published. Is a page claim about an IDP element that the artefact does not show enough to record this listing as AI-bound, or is the visible model decisive (in which case this is E2-no-ai-element)? Related: the crop family n=080, n=120, n=142.
needs_visual_check: true
bpmn_evidence: A published BPMN collaboration diagram: pools 'Customer', 'Credit Card processing' (laned 'Credit Card processing') and 'Bank System Data' - read natively: 'Credit Card Request Start' -> 'Check Credit Score' -> 'Verify Data for Fraud Check' -> 'Validate e-KYC through link' -> 'Set Credit Limit Based on Credit Score' -> 'Branch Manager(BM) Approval' -> gateway 'BM Approval?' ('Approve' -> 'Dispatch Card to Customer' -> 'Notify User for Card Dispatch' -> 'Credit Card Request Completed'; 'Reject' -> 'BM Reject'), with three event sub-processes ('Card Request Rejected - Low CIBIL Score', '- Fraud', '-Timeout'), a 'After 48 hrs' timer and an expanded event sub-process 'Card Request Rejection' ('Send Card Rejection Notification' -> 'Update System for Card Rejection'). No .bpmn is downloadable, and the published canvas is cut off at the bottom: the 'Bank System Data' pool's contents are not shown.
bpmn_evidence_quote: "Validate e-KYC through link"
ai_evidence: The page places an AI-bound element inside this blueprint: 'Intelligent document extraction - Camunda IDP can extract the application form data uploaded by customers or staff harnessing AI models for smart data extraction', and the following feature states that 'The blueprint contains implementation using business rules, SLAs, automated task executions, and smooth KYC through Zoom meeting integration'. No AI element is visible in the published canvas: the tasks that would carry document extraction ('Check Credit Score', 'Verify Data for Fraud Check', 'Validate e-KYC through link') show generic task glyphs in the crop - a gear for the service tasks, a decision-table glyph for the credit-limit task and a user glyph for the branch-manager approval - not the violet AI glyph.
ai_evidence_quote: "Camunda IDP can extract the application form data uploaded by customers or staff harnessing AI models for smart data extraction"
artefacts:
  screenshot: 187_credit-card-onboarding-process.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: marginal
capture_width_px: 856
capture_method: curl of the listing's own asset (d3bql97l1ytoxn.cloudfront.net, app_resources/616063/overview/img4679196815199859127-2x.png, 856x437) plus a 3x crop of the left-hand task row; the image read natively at full size, the crop to compare the task glyphs
---

## What the page shows

Credit Card Onboarding Process (Camunda Services GmbH, blueprint). A credit-card application journey: credit-score check, fraud-data verification, e-KYC through a link, credit-limit setting, branch-manager approval, card dispatch and notification, with rejection paths for score, fraud and timeout.

## Observations (description only, no interpretation)

- **AI activity - function:** claimed, not shown - the page attributes application-form data extraction to Camunda IDP with AI models; no extraction element appears in the published model.
- **AI activity - element type:** none visible. The candidate tasks carry generic glyphs in the crop (gear = automated service task; grid = decision table; person = user task).
- **Authority - downstream:** not published; the visible flow routes on the branch manager's decision and on score/fraud/timeout events.
- **Authority - data:** not shown - no data objects are drawn, and the canvas is cut off before the 'Bank System Data' pool's contents.
- **Authority - control:** the gateway 'BM Approval?' and the event sub-process triggers (low score, fraud, timeout).
- **Authority - control (human):** 'Branch Manager(BM) Approval' is a user task, and the 'BM Reject' path is its negative branch.
- **Input provenance:** the customer's application and uploaded form data, per the page; the document itself is not drawn.
- **Guards present:** the approval gateway, a 48-hour timer, and three rejection event sub-processes with a notification-and-update path.
- **Prompt / model detail visible:** none - no model, prompt or confidence threshold appears on the page or in the diagram.

## Notes for the researcher

Two reasons to hand this to the researcher rather than decide silently: the page places an AI extraction element inside the blueprint ('The blueprint contains implementation using ...'), and the published canvas is demonstrably incomplete - the bottom pool is cut off in both the 2x asset (856x437) and the overview asset (550x281), and no .bpmn is downloadable to read the rest. The crop is why the second capture is a 3x crop of the task row: it is the evidence that the visible automation tasks carry generic glyphs, not the violet AI glyph. Related crop-family rulings: n=080, n=120, n=142.
