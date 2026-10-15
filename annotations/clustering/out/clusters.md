# Candidate clusters (proposal, k = 6)

Chains: 91 from 79 annotatable artefacts; 18 artefacts not annotatable (stay in the denominator).
Average-linkage Gower distance, cut at 0.446. Mean silhouette 0.343.
Pattern status needs >= 3 distinct artefacts (method, minimum-instance rule); this is a proposal for the researcher, not the classification step.

Silhouette by k: 2: 0.20, 3: 0.27, 4: 0.26, 5: 0.30, 6: 0.34, 7: 0.32, 8: 0.31, 9: 0.30, 10: 0.29, 11: 0.28, 12: 0.31, 13: 0.31, 14: 0.30, 15: 0.30, 16: 0.29, 17: 0.29, 18: 0.27, 19: 0.26, 20: 0.26, 21: 0.26, 22: 0.27, 23: 0.27, 24: 0.28, 25: 0.29

## Cluster 1: 1 chains, 1 artefacts, 1 sources (below threshold)

Mean within-cluster distance 0.000.
Shared (>= 2/3): structure=agent-loop (1/1); autonomy=decides (1/1); op classify (1/1); op plan-act (1/1); writer=unknown (1/1); shape=closed-label (1/1); sink control-flow/ungated (1/1); ungated calls=0 (1/1); mutates=unknown (1/1); guard validation (1/1)
Sources: aletyx 1
Sensitive data (descriptor only): unknown 1

- `aletyx/001/C1`: agent inside an ad-hoc sub-process for a loan investigation, choosing which assessment / verification step runs next and producing a recommendation

## Cluster 2: 27 chains, 27 artefacts, 5 sources (candidate pattern)

Mean within-cluster distance 0.274.
Shared (>= 2/3): structure=agent-loop (27/27); autonomy=acts (26/27); op generate (19/27); op decide (21/27); op plan-act (27/27); writer=outsider-writable (24/27); shape=free-text (22/27); sink control-flow/ungated (19/27); sink external-recipient/ungated (18/27); sink internal-system/ungated (18/27); no guards (19/27)
Sources: camunda-docs-blog 12, camunda-marketplace 10, flows-for-apex 2, uipath-marketplace 2, quantumbpm 1
Sensitive data (descriptor only): customer-pii 20, business-records 16, unknown 9, knowledge-base 6, internal-docs 2

- `camunda-docs-blog/002/C1`: message delivery agent: a script task builds the prompt, an AI agent task decides whether tools are needed and the ad-hoc tool sub-process runs its choice (Slack message, email, or a human 'get more info' task), looping back to the agent until no more tools are needed
- `camunda-docs-blog/012/C1`: tax-submission fraud check: an AI task rates fraud likelihood, a script task turns that into the tasks to run, and an ad-hoc sub-process runs the selected ones (AI-generated email inquiry then send email, a human 'call on external advisor' task with a fraud-detected gateway, a throw-fraud path); a second AI task re-rates fraud likelihood and a 'decision made?' gateway either ends the process or loops back to the first AI task; a fraud escalation ends the process separately
- `camunda-docs-blog/013/C1`: lost-baggage claim: a passenger report starts an AI agent (ad-hoc sub-process captioned 'leverages any LLM to decide the next best action') that picks among querying a baggage tracking database, messaging the last known airport, sending a care-products voucher, asking the passenger for more information, and organising baggage delivery then informing the passenger; afterwards a 'compensation claim?' gateway routes to a human 'process compensation' task or ends; 'low confidence' and a 48h timer on the agent route to a human 'manual processing' task
- `camunda-docs-blog/019/C1`: Invoice dispute: after a rejected invoice and sender notification, an AI agent looks up account details, contacts a sales rep, cancels or recreates the invoice, and shows findings to a clerk.
- `camunda-docs-blog/021/C1`: claim handling: an AI agent asks the insurer for missing information, consolidates the claim and evaluates it against policy rules; documentation and an insurer notification follow, with an escalation path to a human.
- `camunda-docs-blog/024/C1`: flight disruption rebooking: an AI agent queries external flight and hotel MCP servers, then requests a rebooking commit that a human must approve before a travel summary is returned
- `camunda-docs-blog/067/C1`: loan AI agent whose tools are emailing the customer and awaiting a reply, a rule check, asking a loan specialist, querying a knowledge base, and an RPA object/QR-code/email sequence
- `camunda-docs-blog/075/C1`: Customer-support email: an AI agent on past conversations picks tools to reply to the customer, query the knowledge base, calculate loan repayment or ask a human expert, then saves the conversation.
- `camunda-docs-blog/077/C1`: insurance upsell: an AI agent task loops over a tool sub-process to consult an expert, call the policy holder, check rules, email recommendations, generate an umbrella offer email and trigger policy underwriting
- `camunda-docs-blog/086/C1`: Mortgage chat: a broker agent calls two remote A2A agents, rule-based risk scores, a conversation store and CRM lookups; a judge agent's confidence ends the chat or routes to a manual process.
- `camunda-docs-blog/121/C1`: Travel upsell: on a customer booking, an AI task enriches context, then an AI agent analyses the trip, checks risk, generates an offer that is sent after a rule check and activated on acceptance.
- `camunda-docs-blog/122/C1`: KYC screening: an AI agent picks sanctions, identity, risk-score and n8n-MCP address/employment checks, may ask a human for more information, then submits a screening result or escalates.
- `camunda-marketplace/005/C1`: Call-quality audit: an AI agent analyses a recorded call transcript and drives an ad-hoc sub-process of AI report and email drafting, a human review and an email notification to the agent.
- `camunda-marketplace/006/C1`: Customer-support email: an AI agent with past conversations emails the customer, queries the knowledge base or hands to a specialist; an AI judge then routes to auto-reply or human handling.
- `camunda-marketplace/008/C1`: Retail return: AI fraud check gates eligibility, AI visual inspection results are pushed to systems, then an AI-driven ad-hoc sub-process picks exchange, refund, cleaning or refurbish fragments.
- `camunda-marketplace/023/C1`: Logistics order from inbound email: three agents in sequence extract and check order data, plan the shipment with the customer, then book it with the carrier and update the ERP.
- `camunda-marketplace/024/C1`: Ticket support: an OpenAI task summarises a new ticket, then an AI agent picks tools to question engineers, search the knowledge base, summarise and post a solution comment.
- `camunda-marketplace/165/C1`: multi-channel customer messaging: an agent detects the customer's intent, forwards the message to business agents and replies to the customer on a chosen channel
- `camunda-marketplace/188/C1`: Security incident triage: LLM calls generate a simulated alert, plan which investigation tools an ad-hoc sub-process runs, classify the threat and GDPR relevance, and write report texts for human review.
- `camunda-marketplace/228/C1`: Generic chat: an AI agent answers a user's request by choosing MCP tools (memory, filesystem, remote wiki, time) and a script tool, looping on user feedback until satisfied.
- `camunda-marketplace/252/C1`: Leave request: an AI agent checks the time-off balance or requests a doctor's note, then either approves automatically or escalates to supervisor and manager review.
- `camunda-marketplace/255/C1`: Tax fraud check: an LLM picks which ad-hoc activities run (email inquiry, human advisor, fraud flag), an LLM drafts the inquiry email, and a second LLM check accepts the result or loops back.
- `flows-for-apex/002/C1`: Lost-luggage agent: an AI-driven ad-hoc sub-process selects lookup, voucher, rebooking and delivery tools, or escalates / declares the bag lost.
- `flows-for-apex/003/C1`: Lost-baggage recovery: an LLM-controlled ad-hoc sub-process (Control Mode AI) locates the bag, rebooks it, arranges delivery, issues vouchers or declares it lost.
- `quantumbpm/001/C1`: AI classifies an incoming support ticket; a rule table routes it to a human or to an agent that uses lookup, search and drafting tools before an automated reply is sent.
- `uipath-marketplace/001/C1`: An agent reads the latest inbox email, categorises it into a mail folder and moves it there.
- `uipath-marketplace/002/C1`: An agent describes each attachment of the newest email in a mail folder, using an LLM file-analysis tool.

## Cluster 3: 15 chains, 15 artefacts, 9 sources (candidate pattern)

Mean within-cluster distance 0.346.
Shared (>= 2/3): structure=fixed-sequence (15/15); autonomy=decides (13/15); op classify (11/15); op generate (10/15); shape=free-text (11/15); sink control-flow/ungated (12/15); sink internal-system/ungated (11/15); ungated calls=1-2 (10/15)
Sources: atamya 2, camunda-docs-blog 2, camunda-marketplace 2, flowable 2, flows-for-apex 2, frends-docs 2, bizagi 1, quantumbpm 1, uipath-maestro-docs 1
Sensitive data (descriptor only): customer-pii 9, business-records 5, unknown 4, knowledge-base 1

- `atamya/010/C1`: product-content enrichment: three parallel AI tasks derive highlights, derive keywords and summarise a description; results are saved, then machine-translated into two languages, then released by a human and activated
- `atamya/011/C1`: product release: on product creation, an automatic categorisation service task and a DeepL machine-translation service task run in parallel with a human marketing task; after a data-quality gateway the product is activated, a datasheet generated and the product synced to the online shop
- `bizagi/001/C1`: ticket handling: after a support agent creates a ticket, AI tasks classify it, prioritise it and produce a preliminary analysis for a human analyst; after the analyst's analysis and resolution, an AI task updates the knowledge base
- `camunda-docs-blog/008/C1`: loan application: after rule-based risk scoring and a KYC sub-process, an AI routing task assigns low / medium / high risk; low and high branches run automatically (accept or reject email plus issue-policy or reject-application service task), the medium branch has a second AI task summarise the results for a human investigator, whose risk assessment then routes to the low or high branch; a collapsed sentiment-analysis sub-process follows on both outcomes
- `camunda-docs-blog/016/C1`: vendor application evaluation: AI extracts application data, a rule table screens products, humans review; AI writes a website description or a rejection email, sent automatically on rule-based rejection
- `camunda-marketplace/064/C2`: Supplier invoice processing: document extraction feeds ERP posting, then an AI three-way match whose result, via a tolerance rule, auto-approves, escalates, disputes or rejects.
- `camunda-marketplace/067/C1`: Out-of-spec lot handling: AI parses a physician email, then decides the disposition that selects conversion, discard, recollection, logging or escalation activities and downstream system updates.
- `flowable/001/C1`: AI detects the intents of an inbound customer email; an inclusive gateway routes each intent to an AI extraction of structured data into process variables.
- `flowable/166/C1`: Inbound customer email: AI recognises intent, scores sentiment and extracts intent-specific data; results route to automatic processing or human handling.
- `flows-for-apex/001/C1`: LLM labels a case for fraud likelihood to drive an inclusive gateway; on the email label a second LLM drafts an information request sent automatically.
- `flows-for-apex/004/C1`: Tax-fraud screening: AI labels taxpayer data to route an inclusive gateway; on the email branch a second AI drafts a clarification email sent to the taxpayer automatically.
- `frends-docs/001/C1`: Invoice exception handling: AI verifies the invoice and routes to auto-accept, reject or human review, then AI drafts a rejection or exception brief.
- `frends-docs/002/C1`: invoice exception handling: an AI task verifies the case and sets the route; AI tasks write a rejection brief or an exception brief for human review.
- `quantumbpm/002/C1`: support triage: an AI task classifies the customer request and sets the route; on the simple path an AI task drafts the reply, which is sent automatically.
- `uipath-maestro-docs/070/C1`: Agents validate a new CRM contact, research the company and summarise the contact in parallel, then score the lead; gateways route to opportunity creation or nurturing.

## Cluster 4: 7 chains, 6 artefacts, 3 sources (candidate pattern)

Mean within-cluster distance 0.296.
Shared (>= 2/3): structure=single-call (6/7); autonomy=suggests (7/7); op generate (6/7); shape=free-text (7/7); no guards (7/7)
Sources: ibm-bamoe 3, camunda-docs-blog 2, uipath-marketplace 2
Sensitive data (descriptor only): customer-pii 6, unknown 1, internal-docs 1, business-records 1

- `camunda-docs-blog/003/C1`: claim adjuster flow: an AI task drafts a short email to the adjuster from policyholder details, which an email service task then sends; a Slack notification runs in parallel
- `camunda-docs-blog/017/C1`: insurance claim adjuster flow: an AI task composes an email telling the adjuster a claimant awaits an estimate, sent automatically, before the adjuster's estimate task
- `ibm-bamoe/004/C1`: Gen AI task drafts an offer letter from candidate, position, salary and bonus variables; the letter is later sent to the candidate after interviews.
- `ibm-bamoe/005/C1`: Gen AI task summarises the submitted claim documents after data validation, ahead of a DMN complexity decision.
- `ibm-bamoe/005/C2`: Langflow-backed agent task researches and investigates complex claims before settlement calculation.
- `uipath-marketplace/003/C1`: An agent turns a meeting transcript into minutes, decisions, risks and action items, which are automatically created as tracker tickets.
- `uipath-marketplace/007/C1`: When no preferred slot is free, an agent offers the patient alternatives or adds them to a waitlist; an accepted alternative is booked and confirmed.

## Cluster 5: 13 chains, 12 artefacts, 6 sources (candidate pattern)

Mean within-cluster distance 0.276.
Shared (>= 2/3): structure=single-call (12/13); autonomy=suggests (11/13); shape=structured (11/13); sink internal-human/gated (10/13); ungated calls=0 (9/13); guard human-review (13/13)
Sources: firestart 7, uipath-marketplace 2, bizagi 1, bonitasoft 1, camunda-docs-blog 1, uipath-maestro-docs 1
Sensitive data (descriptor only): business-records 7, customer-pii 4, unknown 3, internal-docs 1

- `bizagi/002/C1`: expense reporting: an employee uploads receipt files, then an AI Worker bound to the employee's submit task extracts the details and pre-fills the form fields; the submitted report goes through a human analyst policy review and an optional manager approval before notification
- `bonitasoft/012/C1`: customer onboarding / identity check: an automated identity-verification task (AI per page prose: compares submitted identity documents against official databases) precedes a gateway that routes to standard or enhanced due diligence; background check and data integration follow automatically, with a human review loop and a human approval before account creation
- `camunda-docs-blog/047/C1`: financial risk check: DMN risk rules run on submitted financial details, an AI task summarises the results, and medium-risk cases show the summary to a human investigator who decides accept or reject
- `firestart/001/C1`: AI reads data from an inbound invoice; a rule-based 3-way match checks it, then a human approves before ERP posting and archiving.
- `firestart/003/C1`: AI agent reads details from receipts an employee uploaded via form; a payroll human reviews before payout or notifying the employee.
- `firestart/006/C1`: client onboarding: an AI agent checks the client's entered data and rates risk before automated document creation, lawyer review, client signature and filing
- `firestart/007/C1`: Inbound customer inquiry is classified and data points extracted by two AI agent tasks; a clerk checks the data before backend processing or a request to the customer.
- `firestart/012/C1`: quote preparation: an AI agent classifies an emailed or web-form customer request and extracts requested items and quantities; humans confirm before the quote is generated and sent.
- `firestart/014/C1`: contract approval: an AI agent checks a submitted document before two reviewers and management sign digitally; then automated filing and audit log.
- `firestart/015/C1`: AI agent checks a submitted controlled document and extracts its data before human review and approval.
- `uipath-maestro-docs/192/C1`: After a rejected invoice is emailed to the vendor, an agent investigates and resolves the vendor's dispute before the invoice returns to human approval.
- `uipath-marketplace/004/C3`: An agent estimates the claim payout for the officer's final decision.
- `uipath-marketplace/004/C4`: An agent checks whether reinsurance treaty thresholds apply, for the officer's final decision.

## Cluster 6: 28 chains, 22 artefacts, 9 sources (candidate pattern)

Mean within-cluster distance 0.302.
Shared (>= 2/3): structure=single-call (28/28); autonomy=decides (22/28); op classify (23/28); shape=structured (19/28); sink control-flow/ungated (22/28); no guards (23/28)
Sources: uipath-marketplace 10, camunda-marketplace 5, firestart 4, camunda-docs-blog 2, trisotech 2, uipath-maestro-docs 2, frends-docs 1, newgen 1, quantumbpm 1
Sensitive data (descriptor only): customer-pii 16, business-records 12, unknown 4, none 2, knowledge-base 1

- `camunda-docs-blog/001/C1`: song requests for an event: an invited person submits a song via a web form; an AI task judges whether it fits the event type (yes / no / maybe) and the gateway routes to an acceptance or rejection notification, or on 'maybe' to a lyrics lookup and human review
- `camunda-docs-blog/007/C1`: customer inquiry routing: a customer enters an inquiry, an AI task determines the department (other / sales / technical / legal), a gateway routes it to the matching team's work task; the team can resolve, send it back through the AI with feedback, or reroute to a different team
- `camunda-marketplace/016/C1`: customer inquiry routing: an OpenAI task classifies the inquiry (or team feedback on retry) into a department label that a gateway uses to pick the handling team
- `camunda-marketplace/022/C1`: Meeting scheduling: after a client email arrives and upcoming meetings are listed, an AI agent task picks the best time, and a Zoom meeting is created automatically.
- `camunda-marketplace/064/C1`: Procure-to-pay intake: an AI task classifies the submitted purchase request after tenant configuration is loaded, before the approval stage.
- `camunda-marketplace/112/C1`: customer inquiry routing: an Azure OpenAI task classifies the inquiry (or team feedback on retry) into a department label that a gateway uses to pick the handling team
- `camunda-marketplace/136/C1`: Motor claim fast-track: an AI-enhanced validation scores the claim; confidence >= 0.85 auto-approves it and it flows on to settlement, payment and customer notification.
- `firestart/002/C1`: AI agent extracts data from a received supplier quote; approval rules then route to automatic approval or human approval before the order is placed and sent to the ERP.
- `firestart/008/C1`: complaint intake: an AI task categorises, prioritises and extracts data from an emailed or form-submitted complaint before automated system processing and a notification.
- `firestart/011/C1`: Supplier onboarding: an AI agent checks a registering supplier's data, documents and certificates (alternative to manual review) before automated CRM creation and buyer notification.
- `firestart/013/C1`: event registration: for an unknown company, an AI agent task checks the registrant's company data; valid data is created in the CRM and the participant registered automatically.
- `frends-docs/004/C1`: AI classifies an HTTP-submitted support ticket; a gateway routes on its category to raising an issue or request, notifying a lead, or alerting support.
- `newgen/037/C1`: Credit card intake: an AI rule engine evaluates applications from web, mobile, chatbot and email channels and routes them to bot processing.
- `quantumbpm/002/C2`: invoice pipeline: an AI task classifies the extracted, validated invoice as valid or invalid; valid ones are approved and recorded automatically.
- `trisotech/001/C1`: LLM scans a patient's journal entry against a high-risk word list for suicidal ideation; its detection feeds triage rules that route to self-help, specialist or ER.
- `trisotech/027/C1`: An AI performer on a user task scores the quality of an input appraisal; the score routes to approval/rejection directly or via a decision table to human review.
- `uipath-maestro-docs/097/C1`: Agent resolves invoice-to-order mismatches; its resolved/rejected decision routes to human approval or to an automated rejection email to the supplier.
- `uipath-maestro-docs/133/C1`: Agent compares retrieved invoice against purchase order (2-way matching); full match updates financial systems automatically, discrepancies go to manual review.
- `uipath-marketplace/004/C1`: An agent validates a claim against policy terms and limits; its verdict denies the claim or sends it on to the assessments.
- `uipath-marketplace/004/C2`: An agent scores fraud risk; high risk routes the claim to an investigator, low or medium goes straight to the officer review.
- `uipath-marketplace/005/C1`: An agent validates medical coding before submission; valid claims go automatically to the clearinghouse and the payer, invalid ones go to coder correction.
- `uipath-marketplace/005/C2`: An agent checks the claim's attachments, clinical notes and required fields; complete claims go on to automatic submission, missing data raises an error to staff.
- `uipath-marketplace/005/C3`: After a payer denial, an agent parses the rejection reason and puts the claim on a staff worklist.
- `uipath-marketplace/006/C1`: An agent validates the policy behind a reported loss; an inactive policy rejects the claim, an active one starts the parallel evaluations.
- `uipath-marketplace/006/C2`: An agent validates coverage of the reported loss; an excluded peril rejects the claim.
- `uipath-marketplace/006/C3`: An agent screens the loss notice for fraud; a suspicion routes the claim to an investigator, otherwise it goes to adjuster assignment.
- `uipath-marketplace/006/C4`: An agent enriches the loss intake data ahead of adjuster assignment and claim record creation.
- `uipath-marketplace/007/C2`: An agent verifies insurance eligibility; ineligible requests are cancelled, eligible ones get an automatic confirmation.

## Not annotatable

bonitasoft/013, camunda-docs-blog/006, camunda-docs-blog/009, camunda-docs-blog/035, camunda-docs-blog/119, camunda-marketplace/231, cib-seven/443, firestart/009, firestart/010, firestart/016, firestart/017, flowable/169, flows-for-apex/007, flows-for-apex/008, flows-for-apex/009, frends-docs/010, uipath-maestro-docs/188, uipath-maestro-docs/191
