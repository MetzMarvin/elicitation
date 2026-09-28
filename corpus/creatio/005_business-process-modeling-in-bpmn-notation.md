---
n: 1657
source: creatio
source_name: Creatio (creatio.com marketing site) - Business Process Modeling in BPMN Notation
source_type: vendor product marketing page
title: Business Process Modeling in BPMN Notation
url: https://www.creatio.com/page/bpmn
accessed: 2026-09-24
verdict: UNCERTAIN
needs_human_ruling: true
question: "The vendor's BPMN showcase page publishes eight full BPMN process diagrams drawn in the Creatio process designer (purchase request, event participation planning, business trip request, recruitment, employee onboarding, termination of employment, converting lead to sale, closing a sale), and none of them contains an AI element. Separately it publishes five figures that are the designer's element palettes: 'User Actions', 'System Actions in Creatio', 'Start events', 'Logical operators', 'Subprocesses'. The 'System Actions' palette figure lists 'Predict data' - the machine-learning element that the same source documents as putting a prediction model into a process (corpus records 001 and 003). Does a figure that publishes the designer's palette (the set of elements a process can be built from) count as an AI element bound into a process, so that this page is corpus material with the palette figure as the capture? Or does the artefact requirement ('AI element inside the process') exclude it, because none of the eight published process diagrams uses that element and the palette is a UI list rather than a process model - which would make this row E2-no-ai-element? I recorded UNCERTAIN rather than excluding because the element is inside the product's process designer and the palette is what the designer inserts into a process, and under the shared rules a wrong exclusion is unrecoverable (rules 1, 2 and 3)."
bpmn_evidence: "Eight of the page's figures are complete BPMN 2.0 process diagrams, drawn in the Creatio process designer and published at 1080-1286 px wide. Viewed directly: a start event circle, rounded-corner tasks carrying the designer's element icons, white diamonds as exclusive/inclusive gateways with 'Yes'/'No'-labelled outgoing flows, a 'Rejected' flow looping back to an earlier gateway, a red-bordered terminate end event, and lanes in 'Event participation planning' and 'Termination of employment' (e.g. the lane 'Determine marketing materials for stand'). The page states its own notation standard: 'BPMN notation elements look the same in any program.' Each diagram is introduced by the page's own stage list, e.g. 'Business process stages: Purchase order receipt Cost clarification, approval of head department, director approval (if needed)'."
bpmn_evidence_quote: "BPMN notation elements look the same in any program."
ai_evidence: "No AI element appears inside any of the eight published process diagrams: their tasks are the designer's user actions and system actions (Perform task, User dialog, Auto-generated page, Send email, Approval, Read data, Modify data, Formula, Call web service). The AI-bound element is named only in the palette figure 'System Actions in Creatio', which lists 'Predict data' - the ML element recorded for this source in corpus records 001 and 003 - among Read data, Add data, Modify data, Delete data, Formula, Change access rights, Call web service, Script task, Connect process to object and User task. The page's only AI/LLM token in its text is 'Intelligent' inside an award line: 'Creatio has been included in the Gartner Magic Quadrant for Intelligent Business Process Management Suites (2019)', which refers to the analyst category, not to a process element."
ai_evidence_quote: "Creatio has been included in the Gartner Magic Quadrant for Intelligent Business Process Management Suites (2019)"
artefacts:
  screenshot: 005_business-process-modeling-in-bpmn-notation_fig1.png
  screenshot_2: 005_business-process-modeling-in-bpmn-notation_fig2.png
  archive: null
  bpmn_xml: null
capture_source: figure-as-published
capture_quality: legible
capture_width_px: 1186
capture_method: "the page's own published figures, downloaded from www.creatio.com (/page/sites/landings/files/2019-12/) and kept unmodified: fig1 is the 'System Actions in Creatio' palette figure (385x787) whose list contains 'Predict data'; fig2 is the BPMN process diagram 'Purchase request for internal use' (1186x900); fig3 is the BPMN process diagram 'Event participation planning' (814x618), which shows lanes"
duplicate_of: null
access: public
---

## What the page shows

The vendor's landing page for BPMN, on the marketing site rather than in the Academy. It explains the
notation, publishes the process designer's element palettes, and then shows eight business processes
modelled in it. The page's own framing:

> "BPMN notation elements look the same in any program. They can differ only in the color of the shapes,
> but the shapes themselves and even the thickness of their contours are universal. In the notation itself
> the shapes are all black and white."

The eight process diagrams (each with the page's own "Business process stages" list) are: Purchase request
for internal use, Event participation planning, Business trip request, Recruitment, Employee onboarding,
Termination of employment, Converting lead to sale, Closing a sale. All eight were looked at (two contact
sheets: `ledgers/_creatio/crm_bpmn_sheet.png`, `ledgers/_creatio/crm_sheet2.png`); they are the Creatio
process designer's canvas - BPMN tasks, gateways, events, flows and lanes.

The five palette figures are labelled by the page itself: "User Actions", "System Actions in Creatio",
"Start events", "Logical operators", "Subprocesses" (the last showing "Sub-process" and "Event
sub-process"). The System Actions figure is the one that carries the AI-bound element name:

```
Read data · Add data · Modify data · Delete data · Formula · Change access rights ·
Call web service · Predict data · Script task · Connect process to object · User task
```

## Observations (description only, no interpretation)

- **AI activity - function:** none performed by any published process diagram on this page. The only
  AI-bound element is *available*: "Predict data" in the designer's System Actions palette, the element
  that (per corpus records 001 and 003, same source) runs an ML prediction model inside a process.
- **AI activity - element type:** a *system action* palette entry, i.e. a node type that can be placed into
  a process; it is not placed in any of the eight diagrams this page publishes.
- **AI activity - model binding:** none visible - the palette figure names the element, not a model.
- **Authority - downstream / control:** not described on this page.
- **Guards present:** none.
- **Input provenance:** not described on this page.
- **Availability:** the page names no availability gate.

## Notes for the researcher

Two reasons this page is worth a ruling rather than a silent exclusion:

1. It is the vendor's *own* BPMN showcase, and it publishes eight BPMN process diagrams at full size -
   the largest set of published process models found anywhere in this source. Their common feature is
   that none of them is AI-enabled: the vendor's marketing for its BPMN tooling shows process
   automation, not AI-in-process.
2. Its only AI-bound content is one entry in a palette figure. Whether the palette figure counts is the
   same shape of boundary question as records 002/003 (an AI element documented without a process model
   in which it appears) and as oracle-oic record 032.

If the method requires the AI element to be drawn *inside* a published process model, this page is
`E2-no-ai-element` - the dismissed mention being the palette's "Predict data" (an element available in
the designer) and the award line's "Intelligent Business Process Management Suites" (an analyst category).
If the method counts a published palette of in-process element types, this page is corpus material and the
capture is `005_..._fig1.png`.
