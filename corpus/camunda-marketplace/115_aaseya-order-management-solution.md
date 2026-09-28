---
n: 115
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Aaseya Order Management Solution
url: https://marketplace.camunda.com/apps/440239/aaseya-order-management-solution
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: The model contains the service task 'Voice Assistant Check' (element-template glyph visible, implementation not visible anywhere on the page), and a voice assistant is plausibly AI-bound - but the listing's own content names no AI, LLM, model or AI service at all and its catalogue tags are 'Human Task orchestration', not an AI category. Is 'Voice Assistant Check' an AI element of this process, or an ordinary telephony/IVR integration task (which would make the listing E2-no-ai-element)?
needs_visual_check: false
bpmn_evidence: BPMN diagram published as the listing's overview asset; no .bpmn downloadable. Read natively: a three-pool collaboration - 'Customer', 'Order is Planned (IMS)' and 'Network Provider'. Customer pool: 'Order updated' -> 'Notify customer' / 'Reenter Order Data' / 'Send reminder notification' -> end 'Order Updated' / 'Reminder sent'. IMS pool: start 'Order received' -> 'Service Availability Check' -> gateway 'Data complete?' -> 'Credit service check' -> gateway 'Approve order?' -> 'Voice Assistant Check' -> 'Create billing cycle', with a rejection branch to 'Send rejection notification' -> end 'Order rejected' and, in the Network Provider pool, gateway 'Resource required?' -> 'Service Order Review' -> 'Resource installation' -> back to 'Notify order completion' -> end 'Order completed'. Tasks carry element-template glyphs at their top-left.
bpmn_evidence_quote: "Voice Assistant Check"
ai_evidence: No AI element is demonstrable and none is claimed: the listing's own content contains no AI, LLM, model or AI-service term at all - it describes telecom order management ('AOMS automates processes, enhances real-time visibility, and improves the customer experience') - and its catalogue tags are 'Human Task orchestration', 'Blueprints', 'Solution Accelerators'. The single candidate is the service task 'Voice Assistant Check', which carries an element-template glyph but whose implementation is not visible in the published diagram or anywhere on the page.
ai_evidence_quote: "AOMS automates processes, enhances real-time visibility, and improves the customer experience"
artefacts:
  screenshot: 115_aaseya-order-management-solution.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1100
capture_method: curl of the listing's own overview asset (d3bql97l1ytoxn.cloudfront.net, overview/img5346305550680538212-2x.png, 1100x417); native read at full size
---

## What the page shows

Aaseya's Order Management Solution for telecom (Partner, 'Human Task orchestration'). The page describes customer self-service ordering for prepaid, postpaid and fiber services, with approval, rejection and network-provider fulfilment; its published diagram is the three-pool collaboration that implements that flow.

## Observations (description only, no interpretation)

- **AI activity - function:** unknown - the candidate is 'Voice Assistant Check', a service task on the approval path.
- **AI activity - element type:** drawn as an ordinary `serviceTask` with an element-template glyph; no AI-agent element, no ad-hoc container and no AI-specific label.
- **Authority - downstream:** 'Create billing cycle', then the network-provider branch 'Resource installation' and 'Notify order completion'.
- **Authority - data:** the order data entered by the customer, revised through 'Reenter Order Data'; no data objects are drawn.
- **Authority - control:** the gateways 'Data complete?', 'Approve order?' and 'Resource required?'; the approval gateway is the process's main control.
- **Authority - control (human):** the customer pool's tasks ('Notify customer', 'Reenter Order Data') and the order approver named in the page's features ('The order approver evaluates service requests from customers and either approves or rejects them').
- **Input provenance:** customer-entered service order data.
- **Guards present:** availability, credit and voice-assistant checks in sequence before the order is approved; reminder notifications on non-completion.
- **Prompt / model detail visible:** none - no model, prompt or AI connector is named anywhere on the page.

## Notes for the researcher

Recorded as UNCERTAIN on CLAUDE.md's rule that an element whose implementation 'might be AI-bound but is not visible' is never E2. 'Voice Assistant Check' is the only element in the process whose name points at a technology that is plausibly AI; everything else (credit check, availability check, billing cycle) reads as an ordinary system integration. The researcher can settle it from the captured figure and the quoted page copy.
