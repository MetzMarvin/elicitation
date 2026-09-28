---
n: 0
url: https://documentation.ofelia.com/bonita/latest/process/ai-gemini-connector
source: bonitasoft
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: >-
  The page's "Use cases" section describes a process in which "A service task uses the Extract
  connector to parse the invoice", i.e. an AI connector attached to a BPMN activity as its
  implementation - but the page publishes no diagram, no image and no .bpmn/.proc file of that
  process (prose only). Does a text-only process-flow narrative that binds a service task to an
  AI connector contribute an artefact to the corpus in its own right, or is it binding evidence
  for the connector and therefore not a corpus item?
bpmn_evidence: >-
  None published on this page: no diagram, no figure that names one, and no `.bpmn`/`.proc`
  link (checked in the page source). The process appears only as the numbered list under
  "Process flow", i.e. as prose.
ai_evidence: >-
  The AI element is the connector as the implementation of a BPMN service task. Quoted from the
  page's "Use cases" section: "A service task uses the Extract connector to parse the invoice".
  The step that follows names the data binding ("The JSON output is mapped to BDM variables
  (InvoiceData business object)") and the last one a human task ("A human task displays the
  extracted data for validation").
artefacts:
  - no artefact on the page (prose only); the capture is the page's own "Use cases" section
  - screenshot: 005_ai-gemini-process-flow.png
capture_quality: legible
capture_width_px: 1884
---

## What the page shows

The Gemini AI connector page of the Bonita 2026.2 documentation. Its "Use cases" section is
headed "Invoice data extraction" and introduces it as "Extract structured fields from PDF
invoices and populate BDM objects automatically. Gemini's fast processing makes it ideal for
high-volume invoice pipelines." The "Process flow:" list is

> An invoice document is uploaded or received via email
> A service task uses the Extract connector to parse the invoice
> The JSON output is mapped to BDM variables (InvoiceData business object)
> A human task displays the extracted data for validation

The section ends with the connector's configuration parameters (`apiKey`, `chatModelName`,
field names).

## Observations

- A four-step process with a BPMN **service task** whose implementation is the Gemini Extract
  operation and a human validation task after it - all in prose.
- The page publishes no figure: nothing on it is a diagram of the pipeline it describes.

## Notes for the researcher

Captured from the same page render as record 001. Sibling pages are records 001-009.
