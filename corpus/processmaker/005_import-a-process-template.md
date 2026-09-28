---
n: 490
record: 005
url: https://docs.processmaker.com/docs/import-a-process-template
source: processmaker
surface: docs:processmaker
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: The page says process templates carry IDP Connectors (AI/ML-bound, per apidocs/idp-package) that must be configured before use, and shows one template process (Expense Approval) without them. Is the pictured template process an AI-enabled artefact (INCLUDE), or is the page E2 because no AI-bound element is visible in the artefact?
bpmn_evidence: |
  The artefact on this page is image 2, the cover of the "Expense Approval" Process Template, and it is a
  full BPMN model: a pool named "Expense Approval" with two lanes, "Requester" and "Approver"; in the
  Requester lane a start event labelled "Expense slip capture" flowing to the task "Confirm expense
  approval" and on to the end event "Expense approved"; in the Approver lane the tasks "Process slip",
  "Review expense" and "Notify expense rejection", joined by two exclusive gateways whose conditions are
  written on the flows ("Auto approve?" with a "No" branch into "Review expense", "Approved?" with a
  "no" branch into "Notify expense rejection", and "Yes" branches from both gateways up to "Confirm
  expense approval"), ending at "Expense rejected". All of it is drawn on the Modeler's dotted canvas.
  Image 1 is the Template Gallery the template is chosen from ("Template Gallery", with its category
  list and template cards). Nothing else on the page is a diagram: the page's other images are inline
  icons, one per element type the page tells you to inspect in an imported template.
ai_evidence: |
  The AI-bound element is named in the prose, not shown in the diagram. Under the heading "IDP:
  Configure IDP Connectors in the Process Template" the page states that the template's IDP connectors
  "must be configured prior to use", and the checklist tells the reader to "Inspect the Process model
  for an IDP connector". IDP is AI/ML-bound by the vendor's own statement on `apidocs/idp-package`
  ("technology that uses Artificial Intelligence (AI) and Machine Learning (ML) algorithms to extract
  information"; that page is recorded at row 119 and the connector itself at record 004 / row 486).
  So: the page documents an AI-bound connector inside a process that is being imported, and the diagram
  it publishes does not make the connector out.
artefacts:
  - screenshot: 005_import-a-process-template.png
  - file: ledgers/processmaker.raw/figures/docs__import-a-process-template/cap_002_438aa0f5-55af-4ce1-8521-4daa345b14c0.png
  - file: ledgers/processmaker.raw/figures/sh_tpl.png
capture_quality: legible
capture_width_px: 1144
---

## What the page is

`docs/import-a-process-template`, a child of the Process Templates articles. It is a procedure: import
a template from the Template Gallery, then work through a checklist that asks the reader to inspect the
imported process model for each connector type the template may use (Script Tasks, Form Tasks, Manual
Tasks, Send Email, Actions By Email, Data Connector, Decision Task, DocuSign, **IDP**, PDF Generator,
Slack Notification).

## What the capture shows

- image 1 - the **Template Gallery**: categories (Accounting and Finance, Banking, Customer Success,
  Higher Education, Human Resources, Marketing and Sales, Operations) and template cards.
- image 2 - **the artefact**: the "Expense Approval" template cover, "Extract information from a
  scanned image of a payment slip and submit a request for approval of the expense.", with the
  template's process drawn below the description: the "Expense Approval" pool with its "Requester" and
  "Approver" lanes, the four tasks, the two "Auto approve?" / "Approved?" gateways and the three
  events.

## Why this is UNCERTAIN and not E2

The page does not show an AI element inside the pictured process, but it does document one inside a
process of this kind: the imported template carries IDP connectors, and IDP is AI/ML-bound per the
vendor. The AI-bound element is therefore neither in the artefact nor absent from the process; it is
named in the prose and invisible in the figure. CLAUDE.md section 3 sends that case to UNCERTAIN
("might be AI-bound but is not visible"), not to E2.

## Observations

- This row is the census's second route to the IDP element: record 004 captures it as a modelling
  object of the Modeler, this row captures it as a component that ships inside a distributable
  process template. If the researcher's criterion is "the AI element must be visible in the diagram",
  both rows turn on the same question and can be ruled together.
- The page's own advice to the reader is that the AI-bound connector is *not* self-evident in an
  imported model - which is itself a finding about how ProcessMaker presents AI elements: they are
  ordinary connector shapes, distinguishable from the rest only by their icon and name.
