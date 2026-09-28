---
n: 0
url: https://documentation.ofelia.com/bonita/latest/process/ai-azure-connector
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
  page's "Use cases" section: "A service task uses the Extract connector to parse the
  document". The step that follows is a BPMN element too - "A human task presents the extracted
  data for manager approval" - which is what makes the AI step one node of a process rather than
  a standalone call.
artefacts:
  - no artefact on the page (prose only); the capture is the page's own "Use cases" section
  - screenshot: 002_ai-azure-process-flow.png
capture_quality: legible
capture_width_px: 1884
---

## What the page shows

The Azure AI Foundry connector page of the Bonita 2026.2 documentation. Its "Use cases" section
is headed "Enterprise document processing" and introduces it as "Process internal HR and finance
documents using Azure AI within your corporate network, leveraging Azure AD authentication and
VNet integration for maximum security." The "Process flow:" list is

> An expense report is submitted through a Bonita form
> A service task uses the Extract connector to parse the document
> The data is validated against company policies via business rules
> A human task presents the extracted data for manager approval

followed by the "Configuration:" block with `"apiKey": "${AZURE_OPENAI_API_KEY}"` and the
`url`, i.e. the connector's own parameters.

## Observations

- Four steps, three of them BPMN elements named in the page's own words: a form-driven start, a
  **service task** whose implementation is the Extract connector, a business-rule validation and
  a **human task** for approval. That is a process with an AI element in it, described but not
  drawn.
- As with the other eight AI connector pages, the page publishes no figure of any kind - the
  artefact the corpus wants would have to be reconstructed from the prose, which is exactly the
  question the record asks.

## Notes for the researcher

Captured from the same page render as record 001, so the wording can be checked against the
screenshot. The sibling pages are records 001-009.
