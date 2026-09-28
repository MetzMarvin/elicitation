---
n: 0
url: https://documentation.ofelia.com/bonita/latest/process/ai-mistral-connector
source: bonitasoft
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: >-
  The page's "Use cases" section describes a process in which "A service task uses the Extract
  connector to parse the document", i.e. an AI connector attached to a BPMN activity as its
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
  page's "Use cases" section: "A service task uses the Extract connector to parse the document".
  The page's framing is a data-residency one ("Mistral's European infrastructure ensures data
  never leaves EU jurisdiction"), and the last step names the BPMN data store ("Extracted data
  is stored in the Bonita BDM for downstream processing").
artefacts:
  - no artefact on the page (prose only); the capture is the page's own "Use cases" section
  - screenshot: 007_ai-mistral-process-flow.png
capture_quality: legible
capture_width_px: 1884
---

## What the page shows

The Mistral AI connector page of the Bonita 2026.2 documentation. Its "Use cases" section is
headed "GDPR-compliant text processing" and introduces it as "Process personal data documents
while keeping all data within the EU. Mistral's European infrastructure ensures data never
leaves EU jurisdiction." The "Process flow:" list is

> An HR document containing employee personal data is uploaded
> A service task uses the Extract connector to parse the document
> All processing occurs on Mistral's EU servers
> Extracted data is stored in the Bonita BDM for downstream processing

## Observations

- The delegated-binding shape again: a BPMN **service task** whose implementation is the
  Mistral Extract operation, with the output bound to a BDM business object.
- No figure, no screenshot and no `.bpmn`/`.proc` file is published on the page.

## Notes for the researcher

Captured from the same page render as record 001. Sibling pages are records 001-009. The same
connector vendor also publishes a separate OCR connector repository
(bonitasoft/bonita-connector-mistral-ocr), which is a row of the repository group.
