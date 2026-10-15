# Crisp patterns per PATTERN-SPEC.md

91 chains from 79 annotatable workflows; 97 workflows in the denominator (18 not annotatable). Pattern = complete profile with >= 3 workflows.

| Level | Profiles | Patterns (lower / upper) | Chains undetermined | Covered of 97 (lower / upper) | Covered of 79 (lower / upper) | Largest pattern (workflows) |
|---|---|---|---|---|---|---|
| posture | 34 | 5 / 11 | 27 | 25 (26%) / 43 (44%) | 32% / 54% | 9 |
| coarse | 32 | 5 / 12 | 27 | 28 (29%) / 49 (51%) | 35% / 62% | 9 |
| medium | 53 | 3 / 3 | 28 | 9 (9%) / 11 (11%) | 11% / 14% | 3 |
| fine | 54 | 1 / 1 | 30 | 3 (3%) / 3 (3%) | 4% / 4% | 3 |

## Posture

Slots: structure, autonomy, writer, shape, outward-ungated, mutates, human-review. Profiles: 34; of these with 1 workflow: 21.

### P1: 9 workflows lower / 9 upper, PATTERN

structure=agent; autonomy=acts; writer=outsider; shape=free-text; outward-ungated=yes; mutates=some; human-review=no

Sources: camunda-docs-blog 6, camunda-marketplace 2, quantumbpm 1

- variable structure: agent-loop 9
- variable operations: {classify-or-decide, generate-or-summarise, plan-act} 6, {classify-or-decide, extract, generate-or-summarise, plan-act} 2, {classify-or-decide, plan-act} 1
- variable shape: free-text 9
- variable internal ungated audiences: {control-flow, internal-human, internal-system} 3, {control-flow, internal-system} 3, {internal-human, internal-system} 2, {control-flow} 1
- variable mutates: internal-records 6, external-systems 3
- variable other guards: {} 7, {error-path-to-human} 2
- variable sensitive (descriptor): {business-records, customer-pii, unknown} 2, {business-records, customer-pii, knowledge-base} 2, {business-records, customer-pii} 2, {customer-pii, unknown} 1, {customer-pii, knowledge-base, unknown} 1, {business-records, knowledge-base} 1

- `camunda-docs-blog/013/C1`: lost-baggage claim: a passenger report starts an AI agent (ad-hoc sub-process captioned 'leverages any LLM to decide the next best action') that picks among querying a baggage tracking database, messaging the last known airport, sending a care-products voucher, asking the passenger for more information, and organising baggage delivery then informing the passenger; afterwards a 'compensation claim?' gateway routes to a human 'process compensation' task or ends; 'low confidence' and a 48h timer on the agent route to a human 'manual processing' task
- `camunda-docs-blog/021/C1`: claim handling: an AI agent asks the insurer for missing information, consolidates the claim and evaluates it against policy rules; documentation and an insurer notification follow, with an escalation path to a human.
- `camunda-docs-blog/067/C1`: loan AI agent whose tools are emailing the customer and awaiting a reply, a rule check, asking a loan specialist, querying a knowledge base, and an RPA object/QR-code/email sequence
- `camunda-docs-blog/075/C1`: Customer-support email: an AI agent on past conversations picks tools to reply to the customer, query the knowledge base, calculate loan repayment or ask a human expert, then saves the conversation.
- `camunda-docs-blog/077/C1`: insurance upsell: an AI agent task loops over a tool sub-process to consult an expert, call the policy holder, check rules, email recommendations, generate an umbrella offer email and trigger policy underwriting
- `camunda-docs-blog/121/C1`: Travel upsell: on a customer booking, an AI task enriches context, then an AI agent analyses the trip, checks risk, generates an offer that is sent after a rule check and activated on acceptance.
- `camunda-marketplace/006/C1`: Customer-support email: an AI agent with past conversations emails the customer, queries the knowledge base or hands to a specialist; an AI judge then routes to auto-reply or human handling.
- `camunda-marketplace/023/C1`: Logistics order from inbound email: three agents in sequence extract and check order data, plan the shipment with the customer, then book it with the carrier and update the ERP.
- `quantumbpm/001/C1`: AI classifies an incoming support ticket; a rule table routes it to a human or to an agent that uses lookup, search and drafting tools before an automated reply is sent.

### P2: 7 workflows lower / 10 upper, PATTERN

structure=non-agent; autonomy=decides; writer=outsider; shape=bounded; outward-ungated=no; mutates=none; human-review=no

Sources: camunda-marketplace 2, uipath-marketplace 2, camunda-docs-blog 1, flowable 1, trisotech 1

- variable structure: single-call 8, fixed-sequence 1
- variable operations: {classify-or-decide} 8, {classify-or-decide, extract} 1
- variable shape: structured 6, closed-label 3
- variable internal ungated audiences: {control-flow} 7, {control-flow, internal-system} 1, {control-flow, internal-human} 1
- variable mutates: none 9
- variable other guards: {} 9
- variable sensitive (descriptor): {customer-pii} 3, {none} 2, {business-records, customer-pii} 2, {unknown} 1, {customer-pii, knowledge-base} 1

- `camunda-docs-blog/007/C1`: customer inquiry routing: a customer enters an inquiry, an AI task determines the department (other / sales / technical / legal), a gateway routes it to the matching team's work task; the team can resolve, send it back through the AI with feedback, or reroute to a different team
- `camunda-marketplace/016/C1`: customer inquiry routing: an OpenAI task classifies the inquiry (or team feedback on retry) into a department label that a gateway uses to pick the handling team
- `camunda-marketplace/112/C1`: customer inquiry routing: an Azure OpenAI task classifies the inquiry (or team feedback on retry) into a department label that a gateway uses to pick the handling team
- `flowable/001/C1`: AI detects the intents of an inbound customer email; an inclusive gateway routes each intent to an AI extraction of structured data into process variables.
- `trisotech/001/C1`: LLM scans a patient's journal entry against a high-risk word list for suicidal ideation; its detection feeds triage rules that route to self-help, specialist or ER.
- `uipath-marketplace/006/C1`: An agent validates the policy behind a reported loss; an inactive policy rejects the claim, an active one starts the parallel evaluations.
- `uipath-marketplace/006/C2`: An agent validates coverage of the reported loss; an excluded peril rejects the claim.
- `uipath-marketplace/006/C3`: An agent screens the loss notice for fraud; a suspicion routes the claim to an investigator, otherwise it goes to adjuster assignment.
- `uipath-marketplace/007/C2`: An agent verifies insurance eligibility; ineligible requests are cancelled, eligible ones get an automatic confirmation.
- (upper only) `flowable/166/C1`
- (upper only) `newgen/037/C1`
- (upper only) `trisotech/027/C1`

### P3: 3 workflows lower / 4 upper, PATTERN

structure=agent; autonomy=acts; writer=outsider; shape=free-text; outward-ungated=yes; mutates=none; human-review=no

Sources: camunda-marketplace 2, camunda-docs-blog 1

- variable structure: agent-loop 3
- variable operations: {classify-or-decide, generate-or-summarise, plan-act} 3
- variable shape: free-text 3
- variable internal ungated audiences: {control-flow, internal-human} 1, {internal-system} 1, {control-flow} 1
- variable mutates: none 3
- variable other guards: {} 3
- variable sensitive (descriptor): {customer-pii} 2, {customer-pii, unknown} 1

- `camunda-docs-blog/012/C1`: tax-submission fraud check: an AI task rates fraud likelihood, a script task turns that into the tasks to run, and an ad-hoc sub-process runs the selected ones (AI-generated email inquiry then send email, a human 'call on external advisor' task with a fraud-detected gateway, a throw-fraud path); a second AI task re-rates fraud likelihood and a 'decision made?' gateway either ends the process or loops back to the first AI task; a fraud escalation ends the process separately
- `camunda-marketplace/165/C1`: multi-channel customer messaging: an agent detects the customer's intent, forwards the message to business agents and replies to the customer on a chosen channel
- `camunda-marketplace/255/C1`: Tax fraud check: an LLM picks which ad-hoc activities run (email inquiry, human advisor, fraud flag), an LLM drafts the inquiry email, and a second LLM check accepts the result or loops back.
- (upper only) `camunda-docs-blog/002/C1`

### P4: 3 workflows lower / 3 upper, PATTERN

structure=non-agent; autonomy=decides; writer=outsider; shape=bounded; outward-ungated=yes; mutates=some; human-review=no

Sources: camunda-marketplace 2, firestart 1

- variable structure: fixed-sequence 2, single-call 1
- variable operations: {classify-or-decide, extract} 2, {extract} 1
- variable shape: structured 3
- variable internal ungated audiences: {control-flow, internal-system} 1, {control-flow, internal-human, internal-system} 1, {control-flow} 1
- variable mutates: external-systems 2, internal-records 1
- variable other guards: {} 2, {error-path-to-human, validation} 1
- variable sensitive (descriptor): {business-records} 2, {business-records, customer-pii} 1

- `camunda-marketplace/064/C2`: Supplier invoice processing: document extraction feeds ERP posting, then an AI three-way match whose result, via a tolerance rule, auto-approves, escalates, disputes or rejects.
- `camunda-marketplace/067/C1`: Out-of-spec lot handling: AI parses a physician email, then decides the disposition that selects conversion, discard, recollection, logging or escalation activities and downstream system updates.
- `firestart/002/C1`: AI agent extracts data from a received supplier quote; approval rules then route to automatic approval or human approval before the order is placed and sent to the ERP.

### P5: 3 workflows lower / 3 upper, PATTERN

structure=non-agent; autonomy=decides; writer=outsider; shape=free-text; outward-ungated=yes; mutates=none; human-review=no

Sources: flows-for-apex 2, quantumbpm 1

- variable structure: fixed-sequence 3
- variable operations: {classify-or-decide, generate-or-summarise} 3
- variable shape: free-text 3
- variable internal ungated audiences: {control-flow} 3
- variable mutates: none 3
- variable other guards: {} 3
- variable sensitive (descriptor): {customer-pii} 3

- `flows-for-apex/001/C1`: LLM labels a case for fraud likelihood to drive an inclusive gateway; on the email label a second LLM drafts an information request sent automatically.
- `flows-for-apex/004/C1`: Tax-fraud screening: AI labels taxpayer data to route an inclusive gateway; on the email branch a second AI drafts a clarification email sent to the taxpayer automatically.
- `quantumbpm/002/C1`: support triage: an AI task classifies the customer request and sets the route; on the simple path an AI task drafts the reply, which is sent automatically.

### P6: 2 workflows lower / 7 upper, pattern only in upper bound

structure=non-agent; autonomy=decides; writer=outsider; shape=bounded; outward-ungated=no; mutates=some; human-review=no

Sources: camunda-marketplace 1, firestart 1

- variable structure: single-call 2
- variable operations: {classify-or-decide} 2
- variable shape: structured 1, closed-label 1
- variable internal ungated audiences: {control-flow, internal-human, internal-system} 1, {control-flow, internal-system} 1
- variable mutates: external-systems 1, internal-records 1
- variable other guards: {} 2
- variable sensitive (descriptor): {business-records, customer-pii} 1, {customer-pii} 1

- `camunda-marketplace/136/C1`: Motor claim fast-track: an AI-enhanced validation scores the claim; confidence >= 0.85 auto-approves it and it flows on to settlement, payment and customer notification.
- `firestart/013/C1`: event registration: for an unknown company, an AI agent task checks the registrant's company data; valid data is created in the CRM and the participant registered automatically.
- (upper only) `flowable/166/C1`
- (upper only) `frends-docs/004/C1`
- (upper only) `newgen/037/C1`
- (upper only) `quantumbpm/002/C2`
- (upper only) `uipath-marketplace/005/C1`
- (upper only) `uipath-marketplace/005/C2`

### P7: 2 workflows lower / 4 upper, pattern only in upper bound (single source: template reuse?)

structure=non-agent; autonomy=suggests; writer=insider; shape=bounded; outward-ungated=no; mutates=none; human-review=yes

Sources: firestart 2

- variable structure: single-call 2
- variable operations: {extract} 1, {classify-or-decide, extract} 1
- variable shape: structured 2
- variable internal ungated audiences: {} 2
- variable mutates: none 2
- variable other guards: {} 2
- variable sensitive (descriptor): {business-records} 1, {internal-docs} 1

- `firestart/003/C1`: AI agent reads details from receipts an employee uploaded via form; a payroll human reviews before payout or notifying the employee.
- `firestart/015/C1`: AI agent checks a submitted controlled document and extracts its data before human review and approval.
- (upper only) `firestart/014/C1`
- (upper only) `uipath-marketplace/004/C3`
- (upper only) `uipath-marketplace/004/C4`

### P8: 2 workflows lower / 3 upper, pattern only in upper bound

structure=agent; autonomy=acts; writer=outsider; shape=free-text; outward-ungated=no; mutates=some; human-review=no

Sources: uipath-marketplace 1, camunda-docs-blog 1

- variable structure: agent-loop 2
- variable operations: {generate-or-summarise, plan-act} 1, {classify-or-decide, plan-act} 1
- variable shape: free-text 2
- variable internal ungated audiences: {internal-human, internal-system} 1, {internal-system} 1
- variable mutates: internal-records 2
- variable other guards: {} 2
- variable sensitive (descriptor): {business-records, unknown} 1, {business-records} 1

- `camunda-docs-blog/019/C1`: Invoice dispute: after a rejected invoice and sender notification, an AI agent looks up account details, contacts a sales rep, cancels or recreates the invoice, and shows findings to a clerk.
- `uipath-marketplace/001/C1`: An agent reads the latest inbox email, categorises it into a mail folder and moves it there.
- (upper only) `camunda-marketplace/024/C1`

### P9: 2 workflows lower / 3 upper, pattern only in upper bound

structure=non-agent; autonomy=suggests; writer=outsider; shape=bounded; outward-ungated=no; mutates=some; human-review=no

Sources: firestart 1, uipath-marketplace 1

- variable structure: single-call 2
- variable operations: {classify-or-decide} 1, {classify-or-decide, extract} 1
- variable shape: structured 2
- variable internal ungated audiences: {internal-human, internal-system} 1, {internal-human} 1
- variable mutates: internal-records 2
- variable other guards: {} 2
- variable sensitive (descriptor): {business-records} 1, {customer-pii} 1

- `firestart/011/C1`: Supplier onboarding: an AI agent checks a registering supplier's data, documents and certificates (alternative to manual review) before automated CRM creation and buyer notification.
- `uipath-marketplace/005/C3`: After a payer denial, an agent parses the rejection reason and puts the claim on a staff worklist.
- (upper only) `uipath-marketplace/006/C4`

### P10: 1 workflows lower / 4 upper, pattern only in upper bound (single source: template reuse?)

structure=non-agent; autonomy=decides; writer=system; shape=bounded; outward-ungated=no; mutates=some; human-review=no

Sources: uipath-maestro-docs 1

- variable structure: single-call 1
- variable operations: {classify-or-decide, extract} 1
- variable shape: structured 1
- variable internal ungated audiences: {control-flow, internal-human, internal-system} 1
- variable mutates: internal-records 1
- variable other guards: {} 1
- variable sensitive (descriptor): {business-records} 1

- `uipath-maestro-docs/133/C1`: Agent compares retrieved invoice against purchase order (2-way matching); full match updates financial systems automatically, discrepancies go to manual review.
- (upper only) `frends-docs/004/C1`
- (upper only) `quantumbpm/002/C2`
- (upper only) `uipath-marketplace/005/C1`
- (upper only) `uipath-marketplace/005/C2`

### P11: 1 workflows lower / 3 upper, pattern only in upper bound (single source: template reuse?)

structure=non-agent; autonomy=suggests; writer=outsider; shape=bounded; outward-ungated=no; mutates=none; human-review=yes

Sources: firestart 1

- variable structure: single-call 1
- variable operations: {extract} 1
- variable shape: structured 1
- variable internal ungated audiences: {internal-human, internal-system} 1
- variable mutates: none 1
- variable other guards: {validation} 1
- variable sensitive (descriptor): {business-records} 1

- `firestart/001/C1`: AI reads data from an inbound invoice; a rule-based 3-way match checks it, then a human approves before ERP posting and archiving.
- (upper only) `firestart/014/C1`
- (upper only) `uipath-marketplace/004/C3`
- (upper only) `uipath-marketplace/004/C4`

Residue at posture (lower bound): 54 annotatable workflows in no pattern.

aletyx/001, atamya/010, atamya/011, bizagi/001, bizagi/002, bonitasoft/012, camunda-docs-blog/001, camunda-docs-blog/002, camunda-docs-blog/003, camunda-docs-blog/008, camunda-docs-blog/016, camunda-docs-blog/017, camunda-docs-blog/019, camunda-docs-blog/024, camunda-docs-blog/047, camunda-docs-blog/086, camunda-docs-blog/122, camunda-marketplace/005, camunda-marketplace/008, camunda-marketplace/022, camunda-marketplace/024, camunda-marketplace/136, camunda-marketplace/188, camunda-marketplace/228, camunda-marketplace/252, firestart/001, firestart/003, firestart/006, firestart/007, firestart/008, firestart/011, firestart/012, firestart/013, firestart/014, firestart/015, flowable/166, flows-for-apex/002, flows-for-apex/003, frends-docs/001, frends-docs/002, frends-docs/004, ibm-bamoe/004, ibm-bamoe/005, newgen/037, trisotech/027, uipath-maestro-docs/070, uipath-maestro-docs/097, uipath-maestro-docs/133, uipath-maestro-docs/192, uipath-marketplace/001, uipath-marketplace/002, uipath-marketplace/003, uipath-marketplace/004, uipath-marketplace/005

## Coarse

Slots: structure, autonomy, writer, shape, outward-ungated, mutates, human-review. Profiles: 32; of these with 1 workflow: 20.

### C1: 9 workflows lower / 9 upper, PATTERN

structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes; mutates=some; human-review=no

Sources: camunda-docs-blog 6, camunda-marketplace 2, quantumbpm 1

- `camunda-docs-blog/013/C1`: lost-baggage claim: a passenger report starts an AI agent (ad-hoc sub-process captioned 'leverages any LLM to decide the next best action') that picks among querying a baggage tracking database, messaging the last known airport, sending a care-products voucher, asking the passenger for more information, and organising baggage delivery then informing the passenger; afterwards a 'compensation claim?' gateway routes to a human 'process compensation' task or ends; 'low confidence' and a 48h timer on the agent route to a human 'manual processing' task
- `camunda-docs-blog/021/C1`: claim handling: an AI agent asks the insurer for missing information, consolidates the claim and evaluates it against policy rules; documentation and an insurer notification follow, with an escalation path to a human.
- `camunda-docs-blog/067/C1`: loan AI agent whose tools are emailing the customer and awaiting a reply, a rule check, asking a loan specialist, querying a knowledge base, and an RPA object/QR-code/email sequence
- `camunda-docs-blog/075/C1`: Customer-support email: an AI agent on past conversations picks tools to reply to the customer, query the knowledge base, calculate loan repayment or ask a human expert, then saves the conversation.
- `camunda-docs-blog/077/C1`: insurance upsell: an AI agent task loops over a tool sub-process to consult an expert, call the policy holder, check rules, email recommendations, generate an umbrella offer email and trigger policy underwriting
- `camunda-docs-blog/121/C1`: Travel upsell: on a customer booking, an AI task enriches context, then an AI agent analyses the trip, checks risk, generates an offer that is sent after a rule check and activated on acceptance.
- `camunda-marketplace/006/C1`: Customer-support email: an AI agent with past conversations emails the customer, queries the knowledge base or hands to a specialist; an AI judge then routes to auto-reply or human handling.
- `camunda-marketplace/023/C1`: Logistics order from inbound email: three agents in sequence extract and check order data, plan the shipment with the customer, then book it with the carrier and update the ERP.
- `quantumbpm/001/C1`: AI classifies an incoming support ticket; a rule table routes it to a human or to an agent that uses lookup, search and drafting tools before an automated reply is sent.

### C2: 7 workflows lower / 10 upper, PATTERN

structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=no; mutates=none; human-review=no

Sources: camunda-marketplace 2, uipath-marketplace 2, camunda-docs-blog 1, flowable 1, trisotech 1

- `camunda-docs-blog/007/C1`: customer inquiry routing: a customer enters an inquiry, an AI task determines the department (other / sales / technical / legal), a gateway routes it to the matching team's work task; the team can resolve, send it back through the AI with feedback, or reroute to a different team
- `camunda-marketplace/016/C1`: customer inquiry routing: an OpenAI task classifies the inquiry (or team feedback on retry) into a department label that a gateway uses to pick the handling team
- `camunda-marketplace/112/C1`: customer inquiry routing: an Azure OpenAI task classifies the inquiry (or team feedback on retry) into a department label that a gateway uses to pick the handling team
- `flowable/001/C1`: AI detects the intents of an inbound customer email; an inclusive gateway routes each intent to an AI extraction of structured data into process variables.
- `trisotech/001/C1`: LLM scans a patient's journal entry against a high-risk word list for suicidal ideation; its detection feeds triage rules that route to self-help, specialist or ER.
- `uipath-marketplace/006/C1`: An agent validates the policy behind a reported loss; an inactive policy rejects the claim, an active one starts the parallel evaluations.
- `uipath-marketplace/006/C2`: An agent validates coverage of the reported loss; an excluded peril rejects the claim.
- `uipath-marketplace/006/C3`: An agent screens the loss notice for fraud; a suspicion routes the claim to an investigator, otherwise it goes to adjuster assignment.
- `uipath-marketplace/007/C2`: An agent verifies insurance eligibility; ineligible requests are cancelled, eligible ones get an automatic confirmation.
- (upper only) `flowable/166/C1`
- (upper only) `newgen/037/C1`
- (upper only) `trisotech/027/C1`

### C3: 5 workflows lower / 5 upper, PATTERN

structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=yes; mutates=some; human-review=no

Sources: camunda-marketplace 3, firestart 2

- `camunda-marketplace/022/C1`: Meeting scheduling: after a client email arrives and upcoming meetings are listed, an AI agent task picks the best time, and a Zoom meeting is created automatically.
- `camunda-marketplace/064/C2`: Supplier invoice processing: document extraction feeds ERP posting, then an AI three-way match whose result, via a tolerance rule, auto-approves, escalates, disputes or rejects.
- `camunda-marketplace/067/C1`: Out-of-spec lot handling: AI parses a physician email, then decides the disposition that selects conversion, discard, recollection, logging or escalation activities and downstream system updates.
- `firestart/002/C1`: AI agent extracts data from a received supplier quote; approval rules then route to automatic approval or human approval before the order is placed and sent to the ERP.
- `firestart/008/C1`: complaint intake: an AI task categorises, prioritises and extracts data from an emailed or form-submitted complaint before automated system processing and a notification.

### C4: 4 workflows lower / 5 upper, PATTERN

structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes; mutates=none; human-review=no

Sources: camunda-docs-blog 2, camunda-marketplace 2

- `camunda-docs-blog/012/C1`: tax-submission fraud check: an AI task rates fraud likelihood, a script task turns that into the tasks to run, and an ad-hoc sub-process runs the selected ones (AI-generated email inquiry then send email, a human 'call on external advisor' task with a fraud-detected gateway, a throw-fraud path); a second AI task re-rates fraud likelihood and a 'decision made?' gateway either ends the process or loops back to the first AI task; a fraud escalation ends the process separately
- `camunda-docs-blog/086/C1`: Mortgage chat: a broker agent calls two remote A2A agents, rule-based risk scores, a conversation store and CRM lookups; a judge agent's confidence ends the chat or routes to a manual process.
- `camunda-marketplace/165/C1`: multi-channel customer messaging: an agent detects the customer's intent, forwards the message to business agents and replies to the customer on a chosen channel
- `camunda-marketplace/255/C1`: Tax fraud check: an LLM picks which ad-hoc activities run (email inquiry, human advisor, fraud flag), an LLM drafts the inquiry email, and a second LLM check accepts the result or loops back.
- (upper only) `camunda-docs-blog/002/C1`

### C5: 3 workflows lower / 3 upper, PATTERN

structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes; mutates=none; human-review=no

Sources: flows-for-apex 2, quantumbpm 1

- `flows-for-apex/001/C1`: LLM labels a case for fraud likelihood to drive an inclusive gateway; on the email label a second LLM drafts an information request sent automatically.
- `flows-for-apex/004/C1`: Tax-fraud screening: AI labels taxpayer data to route an inclusive gateway; on the email branch a second AI drafts a clarification email sent to the taxpayer automatically.
- `quantumbpm/002/C1`: support triage: an AI task classifies the customer request and sets the route; on the simple path an AI task drafts the reply, which is sent automatically.

### C6: 2 workflows lower / 7 upper, pattern only in upper bound

structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=no; mutates=some; human-review=no

Sources: camunda-marketplace 1, firestart 1

- `camunda-marketplace/136/C1`: Motor claim fast-track: an AI-enhanced validation scores the claim; confidence >= 0.85 auto-approves it and it flows on to settlement, payment and customer notification.
- `firestart/013/C1`: event registration: for an unknown company, an AI agent task checks the registrant's company data; valid data is created in the CRM and the participant registered automatically.
- (upper only) `flowable/166/C1`
- (upper only) `frends-docs/004/C1`
- (upper only) `newgen/037/C1`
- (upper only) `quantumbpm/002/C2`
- (upper only) `uipath-marketplace/005/C1`
- (upper only) `uipath-marketplace/005/C2`

### C7: 2 workflows lower / 4 upper, pattern only in upper bound (single source: template reuse?)

structure=non-agent; autonomy=suggests; writer=not-outsider; shape=not-free-text; outward-ungated=no; mutates=none; human-review=yes

Sources: firestart 2

- `firestart/003/C1`: AI agent reads details from receipts an employee uploaded via form; a payroll human reviews before payout or notifying the employee.
- `firestart/015/C1`: AI agent checks a submitted controlled document and extracts its data before human review and approval.
- (upper only) `firestart/014/C1`
- (upper only) `uipath-marketplace/004/C3`
- (upper only) `uipath-marketplace/004/C4`

### C8: 2 workflows lower / 3 upper, pattern only in upper bound

structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=no; mutates=some; human-review=no

Sources: uipath-marketplace 1, camunda-docs-blog 1

- `camunda-docs-blog/019/C1`: Invoice dispute: after a rejected invoice and sender notification, an AI agent looks up account details, contacts a sales rep, cancels or recreates the invoice, and shows findings to a clerk.
- `uipath-marketplace/001/C1`: An agent reads the latest inbox email, categorises it into a mail folder and moves it there.
- (upper only) `camunda-marketplace/024/C1`

### C9: 2 workflows lower / 3 upper, pattern only in upper bound

structure=agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=no; mutates=some; human-review=no

Sources: camunda-docs-blog 1, flows-for-apex 1

- `camunda-docs-blog/122/C1`: KYC screening: an AI agent picks sanctions, identity, risk-score and n8n-MCP address/employment checks, may ask a human for more information, then submits a screening result or escalates.
- `flows-for-apex/003/C1`: Lost-baggage recovery: an LLM-controlled ad-hoc sub-process (Control Mode AI) locates the bag, rebooks it, arranges delivery, issues vouchers or declares it lost.
- (upper only) `aletyx/001/C1`

### C10: 2 workflows lower / 3 upper, pattern only in upper bound

structure=non-agent; autonomy=suggests; writer=outsider; shape=not-free-text; outward-ungated=no; mutates=some; human-review=no

Sources: firestart 1, uipath-marketplace 1

- `firestart/011/C1`: Supplier onboarding: an AI agent checks a registering supplier's data, documents and certificates (alternative to manual review) before automated CRM creation and buyer notification.
- `uipath-marketplace/005/C3`: After a payer denial, an agent parses the rejection reason and puts the claim on a staff worklist.
- (upper only) `uipath-marketplace/006/C4`

### C11: 1 workflows lower / 4 upper, pattern only in upper bound (single source: template reuse?)

structure=non-agent; autonomy=decides-or-acts; writer=not-outsider; shape=not-free-text; outward-ungated=no; mutates=some; human-review=no

Sources: uipath-maestro-docs 1

- `uipath-maestro-docs/133/C1`: Agent compares retrieved invoice against purchase order (2-way matching); full match updates financial systems automatically, discrepancies go to manual review.
- (upper only) `frends-docs/004/C1`
- (upper only) `quantumbpm/002/C2`
- (upper only) `uipath-marketplace/005/C1`
- (upper only) `uipath-marketplace/005/C2`

### C12: 1 workflows lower / 3 upper, pattern only in upper bound (single source: template reuse?)

structure=non-agent; autonomy=suggests; writer=outsider; shape=not-free-text; outward-ungated=no; mutates=none; human-review=yes

Sources: firestart 1

- `firestart/001/C1`: AI reads data from an inbound invoice; a rule-based 3-way match checks it, then a human approves before ERP posting and archiving.
- (upper only) `firestart/014/C1`
- (upper only) `uipath-marketplace/004/C3`
- (upper only) `uipath-marketplace/004/C4`

Residue at coarse (lower bound): 51 annotatable workflows in no pattern.

## Medium

Slots: structure, operations, autonomy, writer, shape, ungated-reach, mutates, guards. Profiles: 53; of these with 1 workflow: 47.

### M1: 3 workflows lower / 4 upper, PATTERN

structure=single-call; operations={classify-or-decide}; autonomy=decides; writer=outsider; shape=closed-label; ungated-reach={control-flow}; mutates=none; guards=none

Sources: camunda-marketplace 2, camunda-docs-blog 1

- `camunda-docs-blog/007/C1`: customer inquiry routing: a customer enters an inquiry, an AI task determines the department (other / sales / technical / legal), a gateway routes it to the matching team's work task; the team can resolve, send it back through the AI with feedback, or reroute to a different team
- `camunda-marketplace/016/C1`: customer inquiry routing: an OpenAI task classifies the inquiry (or team feedback on retry) into a department label that a gateway uses to pick the handling team
- `camunda-marketplace/112/C1`: customer inquiry routing: an Azure OpenAI task classifies the inquiry (or team feedback on retry) into a department label that a gateway uses to pick the handling team
- (upper only) `newgen/037/C1`

### M2: 3 workflows lower / 4 upper, PATTERN

structure=single-call; operations={classify-or-decide}; autonomy=decides; writer=outsider; shape=structured; ungated-reach={control-flow}; mutates=none; guards=none

Sources: uipath-marketplace 2, trisotech 1

- `trisotech/001/C1`: LLM scans a patient's journal entry against a high-risk word list for suicidal ideation; its detection feeds triage rules that route to self-help, specialist or ER.
- `uipath-marketplace/006/C1`: An agent validates the policy behind a reported loss; an inactive policy rejects the claim, an active one starts the parallel evaluations.
- `uipath-marketplace/006/C2`: An agent validates coverage of the reported loss; an excluded peril rejects the claim.
- `uipath-marketplace/007/C2`: An agent verifies insurance eligibility; ineligible requests are cancelled, eligible ones get an automatic confirmation.
- (upper only) `trisotech/027/C1`

### M3: 3 workflows lower / 3 upper, PATTERN

structure=fixed-sequence; operations={classify-or-decide, generate-or-summarise}; autonomy=decides; writer=outsider; shape=free-text; ungated-reach={control-flow, external-recipient}; mutates=none; guards=none

Sources: flows-for-apex 2, quantumbpm 1

- `flows-for-apex/001/C1`: LLM labels a case for fraud likelihood to drive an inclusive gateway; on the email label a second LLM drafts an information request sent automatically.
- `flows-for-apex/004/C1`: Tax-fraud screening: AI labels taxpayer data to route an inclusive gateway; on the email branch a second AI drafts a clarification email sent to the taxpayer automatically.
- `quantumbpm/002/C1`: support triage: an AI task classifies the customer request and sets the route; on the simple path an AI task drafts the reply, which is sent automatically.

Residue at medium (lower bound): 70 annotatable workflows in no pattern.

aletyx/001, atamya/010, atamya/011, bizagi/001, bizagi/002, bonitasoft/012, camunda-docs-blog/001, camunda-docs-blog/002, camunda-docs-blog/003, camunda-docs-blog/008, camunda-docs-blog/012, camunda-docs-blog/013, camunda-docs-blog/016, camunda-docs-blog/017, camunda-docs-blog/019, camunda-docs-blog/021, camunda-docs-blog/024, camunda-docs-blog/047, camunda-docs-blog/067, camunda-docs-blog/075, camunda-docs-blog/077, camunda-docs-blog/086, camunda-docs-blog/121, camunda-docs-blog/122, camunda-marketplace/005, camunda-marketplace/006, camunda-marketplace/008, camunda-marketplace/022, camunda-marketplace/023, camunda-marketplace/024, camunda-marketplace/064, camunda-marketplace/067, camunda-marketplace/136, camunda-marketplace/165, camunda-marketplace/188, camunda-marketplace/228, camunda-marketplace/252, camunda-marketplace/255, firestart/001, firestart/002, firestart/003, firestart/006, firestart/007, firestart/008, firestart/011, firestart/012, firestart/013, firestart/014, firestart/015, flowable/001, flowable/166, flows-for-apex/002, flows-for-apex/003, frends-docs/001, frends-docs/002, frends-docs/004, ibm-bamoe/004, ibm-bamoe/005, newgen/037, quantumbpm/001, trisotech/027, uipath-maestro-docs/070, uipath-maestro-docs/097, uipath-maestro-docs/133, uipath-maestro-docs/192, uipath-marketplace/001, uipath-marketplace/002, uipath-marketplace/003, uipath-marketplace/004, uipath-marketplace/005

## Fine

Slots: structure, operations, autonomy, writer, shape, sinks, mutates, guards. Profiles: 54; of these with 1 workflow: 49.

### F1: 3 workflows lower / 3 upper, PATTERN

structure=single-call; operations={classify}; autonomy=decides; writer=outsider; shape=closed-label; sinks={control-flow/ungated}; mutates=none; guards={}

Sources: camunda-marketplace 2, camunda-docs-blog 1

- `camunda-docs-blog/007/C1`: customer inquiry routing: a customer enters an inquiry, an AI task determines the department (other / sales / technical / legal), a gateway routes it to the matching team's work task; the team can resolve, send it back through the AI with feedback, or reroute to a different team
- `camunda-marketplace/016/C1`: customer inquiry routing: an OpenAI task classifies the inquiry (or team feedback on retry) into a department label that a gateway uses to pick the handling team
- `camunda-marketplace/112/C1`: customer inquiry routing: an Azure OpenAI task classifies the inquiry (or team feedback on retry) into a department label that a gateway uses to pick the handling team

Residue at fine (lower bound): 76 annotatable workflows in no pattern.

## Not annotatable (in the denominator, never covered)

bonitasoft/013, camunda-docs-blog/006, camunda-docs-blog/009, camunda-docs-blog/035, camunda-docs-blog/119, camunda-marketplace/231, cib-seven/443, firestart/009, firestart/010, firestart/016, firestart/017, flowable/169, flows-for-apex/007, flows-for-apex/008, flows-for-apex/009, frends-docs/010, uipath-maestro-docs/188, uipath-maestro-docs/191
