---
n: 424
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: "UiPath – Cognizant® Automation Center Connector"
url: https://marketplace.uipath.com/listings/uipath-cognizant-hivecenter-connector
accessed: 2026-09-28
verdict: UNCERTAIN
needs_human_ruling: true
question: "Informal box-flow sketch (no BPMN shapes) of ticket handling in which an 'SME triggers the recommended Resolution and Diagnostic actions' in a platform whose prose names a virtual agent and machine learning. Is the recommendation AI-bound, and does the sketch count as a BPMN diagram?"
needs_visual_check: false
bpmn_evidence: single listing image: coloured-box flow User creates a ticket in the ITSM ticketing tool -> Cognizant AutomationCenter pulls the ticket -> SME triggers the recommended Resolution and Diagnostic actions -> Automation Engine triggers UiPath workflow -> API call posts output -> status updated to ticketing tool; no BPMN shapes
bpmn_evidence_quote: "An application connector workflow that helps to connect UiPath & Cognizant® Automation Center through web API’s"
ai_evidence: box 'SME triggers the recommended Resolution and Diagnostic actions'; prose: platform 'engages a virtual agent' and includes machine learning and predictive analytics; source of the recommendation not stated in the diagram
ai_evidence_quote: "The I&O Automation Platform engages a virtual agent that can understand and execute actions"
artefacts:
  screenshot: 030_cognizant-automation-center-connector.png
  archive: 030_cognizant-automation-center-connector.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 614
capture_method: python urllib GET of the original marketplace-cdn.uipath.com asset (cdn-cgi resize wrapper stripped); 614 px is the native size
---

## What the page shows

A Cognizant connector between UiPath and Cognizant Automation Center. The listing image is a flow of coloured boxes: 'User creates a ticket in the ITSM ticketing tool' -> 'Cognizant AutomationCenter pulls the ticket details from ITSM and creates a Cognizant Automation Center activity' -> 'SME triggers the recommended Resolution and Diagnostic actions in Cognizant Automation Center' -> 'The triggered action passes the details in Cognizant Automation Center's Automation Engine' -> 'Cognizant AutomationCenter Automation Engine triggers the execution of required predefined workflow in the UiPath tool' -> 'After the completion of workflow execution in UiPath, an API call is made' -> a highlighted frame 'UiPath - Cognizant Automation Center Connector' (API call posts output and status; activity attributes updated) -> 'Cognizant Automation Center updates the completion/closure status to the ticketing tool'.

## Observations (description only, no interpretation)

- **AI activity - function:** not visible in the diagram; the actions an SME triggers are called 'recommended' (recommender not named)
- **AI activity - element type:** no AI-labelled element; possible AI source behind 'recommended Resolution and Diagnostic actions'
- **Authority - downstream:** UiPath workflow executed; closure status written to the ticketing tool
- **Authority - data:** activity attributes and status updated in Cognizant Automation Center and ITSM
- **Authority - control:** the SME chooses to trigger the recommended actions
- **Input provenance:** ITSM ticket details
- **Guards present:** SME triggers the actions (human step before execution)
- **Prompt / model detail visible:** none

## Notes for the researcher

Native asset legible. Hesitation: AI presence inside the process rests on the word 'recommended' plus platform prose (virtual agent, machine learning, predictive analytics).
