---
n: 174
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Loan Origination and Processing
url: https://marketplace.camunda.com/apps/450143/loan-origination-and-processing
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: The published collaboration contains a black-box participant named 'Chatbot' that the process exchanges messages with ('Send offer to chatbot', 'Send rejection to chatbot', job type 'chatbot_message'), but nothing in the process file names AI, an LLM or a model, the page's own copy says only 'Orchestrate a chatbot-driven loan process', and the listing carries no AI category tag. Does a chatbot participant of unstated implementation count as an AI element inside the process - compare the 'Gen AI Tool' participant (n=151) and the 'Voice Assistant Check' task (n=115) - or is this artefact E2-no-ai-element? The capture and the .bpmn are both in the corpus.
needs_visual_check: false
bpmn_evidence: BPMN collaboration published as the overview asset and as a downloadable .bpmn (process 'Bank: Loan origination and processing', five participants). Read from the XML: the participants are 'Bank: Loan Origination and Processing', 'Customer', 'Chatbot', 'FICO agencies' and 'Bank IT systems' (the last three black boxes with no process reference); the bank process runs start 'Loan requested' -> 'Get credit score' -> 'Validate data and create ticket' -> sub-process 'Loan processing' -> gateway 'Loan results?' -> 'Send offer via mail' -> 'Customer response process' (with the receive task 'Customer accepts offer' and a reminder send task) -> 'Provide loan' -> 'Send confirmation mail' -> end 'loan request processed', with the decline paths ('loan declined manually', 'loan declined automatically', 'loan declined - timeout') and an event sub-process 'loan declined' holding 'Send rejection mail' and 'Record declined loan application'.
bpmn_evidence_quote: "Send offer to chatbot"
ai_evidence: No AI term appears anywhere in the published .bpmn: no modelerTemplate attribute, no AI-named element, no model or provider - only ordinary Zeebe job types (`chatbot_message`, `email_notification`, `getCreditScore`, `provideLoan`, `validate_data`, `recordDeclinedLoanApplication`). The only candidate is the black-box participant 'Chatbot', which the process reaches through the send tasks 'Send offer to chatbot' and 'Send rejection to chatbot'; the participant carries no process reference, so its implementation is not shown. The page's own copy names no AI technology either: 'Orchestrate a chatbot-driven loan process', and its features are 'Reduced Approval Time', 'Fewer Touchpoints', 'Improved Accuracy', 'Cost Savings' and 'Digital Self-Service'.
ai_evidence_quote: "Orchestrate a chatbot-driven loan process"
artefacts:
  screenshot: 174_loan-origination-and-processing.png
  archive: null
  bpmn_xml: 174_loan-origination-and-processing.bpmn
duplicate_of: null
access: public
capture_source: bpmn-xml
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own asset (d3bql97l1ytoxn.cloudfront.net, app_resources/450143/overview/img8893815648550006287-2x.png, 1100x628) and of the .bpmn reached through the listing's own Modeler import link; the image read natively at full size, the XML read directly
---

## What the page shows

The Loan Origination and Processing blueprint (Camunda Services GmbH, solution accelerator, tagged BPMN/DMN/Form). The listing publishes a full lending collaboration: credit-scoring and validation, rule-based loan calculation, an underwriting decision, customer response handling with reminders and timeouts, and a decline path.

## Observations (description only, no interpretation)

- **AI activity - function:** none named. The process talks to a 'Chatbot' participant as the customer channel and calculates loan results with a business rule task; no AI, LLM or model appears in the file.
- **AI activity - element type:** none bound - the chatbot-facing steps are `sendTask`s with the Zeebe job type 'chatbot_message'; the 'Chatbot' participant is a black box with no process reference.
- **Authority - downstream:** the offer, reminder and rejection messages sent to the chatbot and by mail, and the 'Provide loan' service task.
- **Authority - data:** the credit score (from 'Get credit score', via the 'FICO agencies' participant) and the loan results from the DMN decision.
- **Authority - control:** the gateways 'Loan results?' and 'Underwriting result?' plus the event sub-process 'loan declined' - the drawn decision structure sits entirely on rule and human decisions, not on the chatbot.
- **Authority - control (human):** the user task 'Underwrite loan' before the offer is sent - a human underwrites every approved case in the drawn flow.
- **Input provenance:** the loan request from the customer/chatbot channel, plus the credit score returned by the FICO participant.
- **Guards present:** underwriting, the loan-results gateways, the decline event sub-process and a customer-response timeout end event.
- **Prompt / model detail visible:** none - the file names no model, provider or prompt.

## Notes for the researcher

The artefact is strong (a complete five-participant collaboration with DMN and a human underwriting step) but the AI question is exactly the one n=151 raised: a chat-based participant whose implementation the artefact does not show, in a listing that never claims AI. Recorded UNCERTAIN so the chatbot-participant boundary is settled once by the researcher.
