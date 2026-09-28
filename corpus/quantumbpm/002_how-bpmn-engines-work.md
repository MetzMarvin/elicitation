---
n: 13
source: quantumbpm
source_name: QuantumBPM (quantumbpm.com - BPMN/DMN engine vendor: blog, docs, product pages)
source_type: vendor blog post (BPMN engine explainer) with BPMN process figures
title: "How a BPMN Engine Works, and What You Can Build With One"
url: https://quantumbpm.com/blog/how-bpmn-engines-work
accessed: 2026-09-24
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "the post's pattern catalogue is a set of drawn BPMN processes (figures whose alt text names the notation's elements: start event, end event, service tasks, a parallel gateway, a timer wait, boundary events), and the page's prose names the model elements it is discussing"
bpmn_evidence_quote: "A two step BPMN process: start event, Get Customer Data, Send Welcome Email, end event"
ai_evidence: "two of the drawn processes contain AI steps: an AI classification step followed by a gateway that routes simple cases to an AI-generated response and hard ones to human review, and an invoice pipeline whose extraction/validation steps are followed by an AI classification and the same human-review gateway"
ai_evidence_quote: "Support process where an AI analyzes a request, then a gateway routes simple cases to an AI generated response and complex ones to human review"
artefacts:
  screenshot: 002_ai-support-triage.png
  assets: [002_invoice-processing.png, 002_how-bpmn-engines-work.page.html]
  bpmn_xml: []
  archive: 002_how-bpmn-engines-work.page.html
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1578
capture_method: curl of the two AI-named figures at their native URLs (1578x458 and 1720x462 px) and of the rendered page
---
## What the page shows

The post (Jakub Krištof, 5 September 2026, 16 min read) explains how a BPMN engine runs a
process and then lists "seven patterns worth knowing", each illustrated with a modelled
process. The first pattern is "AI-powered processes", whose two figures are the AI artefact
here; both are captured in the corpus.

* `ai-support-triage` (1578x458) - alt: "Support process where an AI analyzes a request, then
  a gateway routes simple cases to an AI generated response and complex ones to human
  review".
* `invoice-processing` (1720x462) - alt: "Invoice pipeline: get invoice, extract data,
  validate, AI classification, then a gateway to human review or approval and ...".

The section's prose, verbatim: "AI is a good example of something you can use inside a
business process without making the AI responsible for the entire workflow. Consider a
customer support process: The AI worker could classify the request, extract relevant
information, summarize the conversation, or draft a suggested response. The BPMN process
stays responsible for the overall flow. It can define that simple requests are handled
automatically while complex ones require a human to review the result." and, under the
vendor's own heading for what the product does, "In QuantumBPM An AI step is an ordinary
service task, so the model stays deterministic and replayable even though the model call is
not. Every prompt, response, and routing decision is recorded in the instance history for
audit."

The other nine figures of the page are non-AI BPMN material: a two-step welcome-email
process, a token-movement animation, a parallel-gateway run panel, a payment-retry timer
process, a long-running onboarding process, an order-orchestration process, a subscription
lifecycle with timers, and the saga pair (forward order process and the same process with
compensation boundary events). The page's three code blocks are JSON variable payloads
(`{"customerId": 123}`, a customer record, and `{"customerId": 123, "invoiceReady": true,
"shipmentReady": true}`), not model XML.

## Observations (description only, no interpretation)

- **AI activity - function:** classification of the incoming request in the support process,
  and classification inside the invoice pipeline; the AI's output feeds a gateway in both.
- **AI activity - element type:** the figures are drawn in BPMN notation and the visual check
  (see Notes) read both of them out element by element, confirming what the alt text said:
  in `002_ai-support-triage.png` the AI steps are a `service task` "AI analyzes request" after
  the user task "Receive customer request", and a `service task` "AI Generates Response" on
  the gateway's "Simple" branch; in `002_invoice-processing.png` the AI step is the
  `service task` "AI Classification" after "Validate Invoice", with a gateway routing
  "Invalid" cases to the user task "Human Review" and "Valid" cases to "Approve". The
  section's own rule is "An AI step is an ordinary service task".
- **Authority - control:** in both processes the routing decision is a gateway downstream of
  the AI step, and the AI step itself does not decide the flow.
- **Authority - human in the loop:** both drawings end their AI branch at a human review or
  approval path when the case is not simple.
- **Guards present:** the page describes retries and error paths in the following section
  (payment retry with timer wait), but the two AI drawings are not described as carrying a
  model-level guard; nothing in the page fixes a confidence threshold here (contrast record
  001, where the DMN table does).
- **Prompt / model detail visible:** none; the page names no model, provider or prompt for
  either process.
- **Cross-reference:** the page links the anchor post ("We covered the full pattern,
  including ad-hoc sub-processes for reasoning loops, in Orchestrating AI agents with
  BPMN"), which is record 001 - the two pages are two views of the same vendor pattern, not
  duplicates of one diagram.

## Notes for the researcher

- **Visual check done** (visual check by orchestrator elicitation-5a, 2026-09-25): this
  session could not render images, so the two figures were read by the orchestrator, who
  reports both as legible BPMN diagrams with the AI steps drawn as service tasks; the
  read-out is in the Observations above. `needs_visual_check` is therefore false.
- No model XML is downloadable for these two processes; the decisive `.bpmn` channel of this
  source is record 001's files. If the reviewer wants XML for the drawn AI steps, the figures
  are the only evidence and the task labels above come from the visual read.
- The page is included rather than excluded because a wrongly excluded item is invisible to
  the method's exhaustiveness claim, and because the AI element here is *inside* the drawn
  process (not a diagram about AI, and not AI used to draw the diagram).
