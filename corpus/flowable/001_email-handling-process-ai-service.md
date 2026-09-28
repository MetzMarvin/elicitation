---
n: 95
source: flowable
source_name: Flowable (enterprise documentation, vendor blog/marketing site, training site)
source_type: vendor docs
title: Create an AI Service
url: https://documentation.flowable.com/latest/ai/howto-ai-service/index.html
accessed: 2026-09-25
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: BPMN process model figure (process-model1-…png, 2116x800) plus prose naming the BPMN constructs the figure shows ("we start with a process model", "add a Service Registry Task", "a start event having a start form")
bpmn_evidence_quote: "In the process model, add a Service Registry Task and select our service definition and the Detect Intent operation."
ai_evidence: the process's service tasks are bound to a service definition whose Service type is "AI"; the tasks are named "Detect intents" and "Extract address", and the page gives their prompts
ai_evidence_quote: "create a new service definition and choose Service type to be AI"
artefacts:
  screenshot: 001_email-handling-process-ai-service.png
  archive: 001_email-handling-process-ai-service.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 2116
capture_method: curl -L on https://documentation.flowable.com/latest/assets/images/process-model1-eba8a6581fbc7e35255a697d7834d934.png, src read from the page DOM; labels first read with RapidOCR, then confirmed by sight in the visual pass (elicitation-aa, 2026-09-25)
---

## What the page shows

A step-by-step how-to ("Create an AI Service", marked "Outdated documentation page ... old version
of the documentation for Flowable 3.17") that builds an AI-backed service definition and then uses it
from a BPMN process. The figure `process-model1` is the process model the page names
"Email Handling Process": a start event with a start form, then service tasks wired to the AI service
operations, ending the flow. The page states the case is "from a financial institution, improving the
handling of customer inquiries through email."

## Observations (description only, no interpretation)

- **AI activity - function:** the process detects the customer's intent in an inbound email and
  extracts structured data from it. The page: "First, we examine the content within the email to
  detect the intent of the customer and if we have an intent we want to support automatically, we use
  a second AI operation to extract structured data from that unstructured email content." The intent
  operation returns an array: "As the content could have more than one intent ... we choose Array as
  the type to be able to get more than one intent".
- **AI activity - element type:** an ordinary BPMN `serviceTask` (Flowable's Service Registry Task)
  whose implementation is a *service definition of Service type "AI"* and one of its operations. This
  is the case the method puts in scope as "AI element visible only as a task property or
  implementation binding": nothing in the diagram's shape says "AI". Page: "Within Flowable Design
  and your example app, create a new service definition and choose Service type to be AI." and "In the
  process model, add a Service Registry Task and select our service definition and the Detect Intent
  operation."
- **Authority - downstream:** the process itself. The extracted variables are mapped from the
  operation output to process variables ("the Input and Output tabs will already list the necessary
  input parameters and available output parameters"). Verified at runtime in Flowable Inspect:
  "Executing the process and using Flowable Inspect, we can see the extracted values, and as expected,
  AI even filled in the missing gaps like the ZIP code and the country".
- **Authority - data:** output parameters of the AI operations - for `Detect intents` an Array named
  `intents` (mapped to process variable `customerIntents`); for `Extract address data` the fields
  Street / House Number / ZIP / City / Country mapped to `street`, `houseNumber`, `zip`, `city`,
  `country`.
- **Authority - control:** the page's later variant of this process (record 002) adds an inclusive
  gateway on the returned intents; in *this* figure the AI task output feeds the next task directly.
  The page explicitly keeps a human option open for later versions: "we could now extend the process
  model and create more details like a user task showing the extracted information and detected
  intents to manually check, if necessary".
- **Input provenance:** the process's start form, a multi-line text field carrying the customer's
  email body. Page: "we just use a form with a multi-line content field to provide the email content
  we want to process". The mapping binds the form variable to the operation input parameter
  `customerMessage` (figure `service-task1` labels: "Input parameters for Detect Intents / Map data to
  service operation input parameter / Customer message / $(customerMessage)").
- **Guards present:** none observed in this figure. The page notes the operator can map a missing
  value default ("Missing value ... Set default value ... unknown"). No approval or review step in
  the shipped model.
- **Prompt / model detail visible:** the page publishes the system messages of the AI service
  operations verbatim, e.g. for intent detection: "Act as a financial back officer handling customer
  inquiries through email. There are several use cases happening all the time and being supported
  automatically. Everything else is handled ..."; and for address extraction: "As a help desk
  employee you receive emails from customers that contain an address. If there is a partially found
  address only and you can't figure out the missing fields, return null for ...". A worked test case is
  given: input "I moved to a new location at Baslerstrasse 6o in Zurich." -> response
  `"intents":["address-change"]`, and the extraction response is shown field by field
  (`"zip": "8048"` after completion). No model provider or model name is printed on this page.

## Notes for the researcher

**Sighted confirmation (visual pass elicitation-aa, 2026-09-25).** The figure was looked at, not
merely OCR'd, and the verdict above is confirmed. Notation is BPMN 2.0 and is unambiguous: a pool
"Email handling process" containing a lane "System", a start event, two rounded-corner service tasks
and an end event, with sequence flows between them; on the second model a diamond gateway. It is not
CMMN (no cut-corner stages, no sentry diamonds), and no element carries an error boundary event that
could be mistaken for an AI marker.

The AI sits inside the process as the **implementation binding of the two service tasks**, which is
the case the method calls "AI element visible only as a task property or implementation binding":
nothing in the shape of "Detect intents" or "Extract address data" says AI, but the accompanying
`service-task1/2/3` panels show both tasks bound to operations of a service definition whose Service
type is AI - `Detect Intents` (input `${customerMessage}` mapped to "Customer message
(customerMessage, String)"; output `intents` (Array) mapped to process variable `customerIntents`)
and `Extract address data` (output fields street / houseNumber / zip / city / country).

Second model read off the figure: `Detect intents` feeds a gateway labelled "Intents?" whose outgoing
sequence flows are labelled *address-change*, *payment-instructions*, *account-balance or
new-account*, *block-credit-card or change-credit-card-limit* and *unknown*, each branch leading to
its own extraction service task, then a joining gateway and an end event. The gateway is fed by the AI
output, so the earlier OCR note that this figure is the plain linear flow understates it - the AI
output drives a conditional split; on this figure it still does not drive the flow directly.

Earlier method note, retained for audit: the census could not receive image content, so the labels
were first obtained from RapidOCR over the native-resolution asset. OCR of this figure returned both
diagram content ("Email handling process", "Detect intents", "Extract address", "data", "Start event")
and the modeler's element palette ("User task", "Subprocess", "Call activity", "Case task", "Exclusive
gateway", "Timer boundary event"), which is expected for a Flowable Design canvas screenshot with its
palette open. The palette entries are modeler UI, not process elements.

(Orchestrator note 2026-09-25: the second model on this page, the "Intents?" inclusive-gateway
variant, is captured as `001_email-handling-process-inclusive-gateway.png`. It was formerly a
separate record 002 for the same ledger row n=95. Duplicate records 002/023/064 were moved to
`ledgers/flowable.raw/orphans/`.)
