---
n: 0
source: creatio
source_name: Creatio Academy (academy.creatio.com), version 10 - development guide / Freedom UI / Creatio.ai examples
source_type: vendor product documentation
title: Handle system-level data using Creatio.ai in the business process
url: https://academy.creatio.com/guides/dev/development-on-creatio-platform/platform-customization/freedom-ui/creatio-ai/examples/creatio-ai-in-script-task
accessed: 2026-09-24
verdict: INCLUDE
bpmn_evidence: "Three figures are the process model itself, all captioned in the page's own prose as the diagram of the process: 'The diagram of the \"Summarize contact information\" business process will be as follows.' (after the Read data element, after the Sub-agent element and after the auto-generated page). Each is a BPMN fragment drawn in the Creatio process designer: a green start event, rounded-corner tasks with element icons, directional sequence flows and an orange terminate end event. The page then walks through building exactly that model in the designer: 'place the Sub-agent element between the Read data system action and Terminate page element in the working area of the Process Designer.'"
bpmn_evidence_quote: "The diagram of the \"Summarize contact information\" business process will be as follows."
ai_evidence: "One task of the diagram is the AI element: 'Title Run the AI Sub-agent Which sub-agent to call? Contact summary'. The Sub-agent it calls is a Creatio.ai agent created earlier on the same page ('As a result , Creatio will add the \"Contact summary\" AI Sub-agent to the Creatio.ai sub-agents section.'), and the process consumes its output in later elements ('the outcome of the Creatio.ai work')."
ai_evidence_quote: "Title Run the AI Sub-agent Which sub-agent to call? Contact summary"
artefacts:
  screenshot: 004_handle-system-level-data-creatio-ai_fig1.png
  screenshot_2: 004_handle-system-level-data-creatio-ai_fig2.png
  archive: null
  bpmn_xml: null
capture_source: figure-as-published
capture_quality: legible
capture_width_px: 700
capture_method: "the page's own three process-diagram figures, downloaded from the Academy CDN (d3a7ykdi65m4cy.cloudfront.net) and kept unmodified; a third capture (004_..._fig3.png) is the finished diagram after the auto-generated page element was added"
duplicate_of: null
access: public
---

## What the page shows

The worked example "Handle system-level data using Creatio.ai in the business process" (dev guide,
Freedom UI, Creatio.ai examples). It builds a business process that hands a step to a Creatio.ai
Sub-agent and then pages the result to the user:

> "The "Summarize contact information" business process generates the "Retrieve the summarized contact
> information" page and handles the retrieved data using Creatio.ai."

The page publishes the process model three times, each time as the result of the step just described:

- **fig1** - after "Add a Read data element": start event → task **Read contact information**
  (read-data icon) → terminate end event.
- **fig2** - after "4. Implement running the AI Sub-agent / Add a Sub-agent element": start event →
  **Read contact information** → task **Run the AI Sub-agent** (Creatio.ai "ai" icon) → terminate end
  event.
- **fig3** - after "5. Implement a separate page to display the outcome of the Creatio.ai work": the
  same model with the auto-generated page task **Retrieve the summarized contact information** added
  before the terminate event.

The AI element's binding is on the page: "Fill out the element properties . Property Property value
**Title Run the AI Sub-agent Which sub-agent to call? Contact summary**", and the Sub-agent itself was
created in step 1 ("Creatio will add the "Contact summary" AI Sub-agent to the Creatio.ai sub-agents
section"). The result handling is explicit too: the process writes the Sub-agent's output, status and
error message into three parameters (`Outcome of the Creatio.ai work`, `Status of the Creatio.ai
execution`, `Error message`) that the auto-generated page displays.

## Observations (description only, no interpretation)

- **AI activity - function:** summarise a contact's data (full name, birth date, job title, business
  phone) - the Sub-agent's prompt and formula are set up on the page ("Add the formula: "Birth date: " +
  [#Read contact information...]").
- **AI activity - element type:** a **Sub-agent element** of the process designer, drawn as a BPMN task
  labelled "Run the AI Sub-agent" inside the process model. This is the same element family as the
  "Call Creatio.ai" element (corpus record 002), but here the element is visible *inside a published
  process model*, which is why this page is a corpus item and record 002 is a ruling.
- **AI activity - model binding:** to a Sub-agent named "Contact summary" configured in the Creatio.ai
  sub-agents section; the process binds it as a task property.
- **Authority - downstream:** the three result parameters are written with the Sub-agent's output,
  execution status and error message; the auto-generated page displays them.
- **Authority - control:** the process decides when the Sub-agent runs (placed between the Read data
  element and the terminate event).
- **Guards present:** none described - no threshold, no human confirmation of the Sub-agent's answer
  before it is stored. The `Status of the Creatio.ai execution` and `Error message` parameters are the
  only handling of failure the page names.
- **Input provenance:** the contact record read by the preceding Read data element (the tenant's own
  data), passed to the vendor's Sub-agent.
- **Availability:** no gate named on the page.

## How it was found

This row began as UNCERTAIN: the caption classifier could not settle the notation of the page's 21
figures because the page uses no figure captions (the figures are identified only by file name and by
the prose sentence that introduces them). The visual pass over the figures resolved it - three of them
are named `..._in_process_diagram.png` and are the process model - so the row was superseded to
INCLUDE and this record written (`ledgers/_creatio_correct.py`, capture sheet
`ledgers/_creatio/candidates2.png`).
