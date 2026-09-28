---
n: 162
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: UiPath Communication Mining Connector
url: https://marketplace.camunda.com/apps/446152/uipath-communication-mining-connector
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: BPMN diagram published as the listing's own asset (Camunda Web Modeler, canvas with the properties panel of the second task open); no .bpmn downloadable. Read natively: start event 'Classifying Started' -> serviceTask 'Classify email' -> serviceTask 'Populate Missing Categories' -> serviceTask 'Determine Email Type' -> exclusive gateway with the three branches 'Update' (-> 'Update Customer Details' -> end 'Customer Details Updated'), 'Complaint' (-> 'Review Complaint' -> end 'Complaint Reviewed') and 'Default' (-> 'Take Default Action' -> end 'Default Action Initiated').
bpmn_evidence_quote: "Classify email"
ai_evidence: The AI work is the process's first task, and the open properties panel shows what it is bound to: template 'UIPATH COMMS MINING CONNECTOR' / 'Classify email', operation 'Classify Email' ('The operation in UiPath to invoke'), with a 'Model Version' property ('123') and the UiPath instance and organisation fields. The page's own copy calls the task AI twice: 'Classify emails with UiPath AI' and 'Leverage UiPath's AI functionality to classify emails as part of your Camunda-based business processes'. The task carries the connector's element-template glyph on the canvas.
ai_evidence_quote: "Leverage UiPath's AI functionality to classify emails as part of your Camunda-based business processes"
artefacts:
  screenshot: 162_uipath-communication-mining-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own asset (d3bql97l1ytoxn.cloudfront.net, app_resources/446152/overview/img4032986012634941490-2x.png, 1100x507); native read at full size - a Camunda Web Modeler canvas with the task's properties panel open
---

## What the page shows

The UiPath Communication Mining Connector (Camunda Services GmbH, connector template). The listing publishes one model: an email-classification flow whose first task invokes the UiPath Communications Mining classification operation, after which the email is categorised, its missing categories are populated and its type determined before one of three branches is taken.

## Observations (description only, no interpretation)

- **AI activity - function:** classification of incoming emails by UiPath's Communications Mining service.
- **AI activity - element type:** an ordinary `serviceTask` labelled 'Classify email', bound to the vendor's connector template with a model version configured; no agent element and no ad-hoc container.
- **Authority - downstream:** everything downstream of the classification - 'Populate Missing Categories', 'Determine Email Type' and the three-way branching to customer-detail update, complaint review or default action.
- **Authority - data:** the panel shows the instance, organisation, tenant, project and dataset the classification is run against, and a 'Model Version' field; the branch variable is the email type.
- **Authority - control:** the exclusive gateway 'Determine Email Type' -> the update/complaint/default branches.
- **Authority - control (human):** the 'Complaint' branch ends in the user task 'Review Complaint' - the only human step, and it sits behind the classification rather than in front of it.
- **Input provenance:** the incoming email handed to the classification task.
- **Guards present:** the three-way branch; no confidence gate or approval on the classification itself.
- **Prompt / model detail visible:** the properties panel shows the operation and 'Model Version 123', but names no prompt; the field values are demo placeholders ('cloud.uipath.com', '{{secrets.UIPATH_DEMO}}').

## Notes for the researcher

One of the batch's clear connector-bound AI elements: the binding is visible in the published properties panel and the vendor's own copy names the capability as AI. The listing demonstrates the connector in a real routing context (three branches), unlike the minimal three-element connector models elsewhere in this source.
