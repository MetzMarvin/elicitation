---
n: 0
url: https://documentation.ofelia.com/bonita/latest/process/ai-cohere-connector
source: bonitasoft
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: >-
  The page's "Use cases" section describes a process in which "A service task attaches relevant
  policy documents and uses the Ask connector", i.e. an AI connector attached to a BPMN
  activity as its implementation - but the page publishes no diagram, no image and no
  .bpmn/.proc file of that process (prose only). Does a text-only process-flow narrative that
  binds a service task to an AI connector contribute an artefact to the corpus in its own right,
  or is it binding evidence for the connector and therefore not a corpus item?
bpmn_evidence: >-
  None published on this page: no diagram, no figure that names one, and no `.bpmn`/`.proc`
  link (checked in the page source). The process appears only as the numbered list under
  "Process flow", i.e. as prose.
ai_evidence: >-
  The AI element is the connector as the implementation of a BPMN service task. Quoted from the
  page's "Use cases" section: "A service task attaches relevant policy documents and uses the
  Ask connector". The next step is the model's answer with citations ("Cohere generates an
  answer with citations referencing specific document sections"), i.e. the RAG binding the
  operation documents.
artefacts:
  - no artefact on the page (prose only); the capture is the page's own "Use cases" section
  - screenshot: 003_ai-cohere-process-flow.png
capture_quality: legible
capture_width_px: 1884
---

## What the page shows

The Cohere AI connector page of the Bonita 2026.2 documentation. Its "Use cases" section is
headed "Compliance question answering with citations" and introduces it as "Use the Ask
operation with Cohere's RAG capabilities to answer compliance questions grounded in actual
policy documents. The model provides citations referencing specific sections, making answers
auditable and verifiable." The "Process flow:" list is

> A compliance officer submits a question about internal policies
> A service task attaches relevant policy documents and uses the Ask connector
> Cohere generates an answer with citations referencing specific document sections
> The answer and citations are stored as BDM objects for audit purposes

## Observations

- Same shape as the other eight AI connector pages: a process described in prose, one BPMN
  **service task** bound to the connector, and no figure at all on the page.
- The RAG pattern here (documents attached, answer with citations, stored as BDM objects) is
  the same pattern the docs portal documents elsewhere with diagrams; on this page it exists
  only as the numbered list.

## Notes for the researcher

Captured from the same page render as record 001. Sibling pages are records 001-009.
