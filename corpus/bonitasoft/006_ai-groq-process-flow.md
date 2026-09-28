---
n: 0
url: https://documentation.ofelia.com/bonita/latest/process/ai-groq-connector
source: bonitasoft
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: >-
  The page's "Use cases" section describes a process in which "As the user fills fields, a
  service task calls Groq for instant validation and suggestions", i.e. an AI connector attached
  to a BPMN activity as its implementation - but the page publishes no diagram, no image and no
  .bpmn/.proc file of that process (prose only). Does a text-only process-flow narrative that
  binds a service task to an AI connector contribute an artefact to the corpus in its own right,
  or is it binding evidence for the connector and therefore not a corpus item?
bpmn_evidence: >-
  None published on this page: no diagram, no figure that names one, and no `.bpmn`/`.proc`
  link (checked in the page source). The process appears only as the numbered list under
  "Process flow", i.e. as prose.
ai_evidence: >-
  The AI element is the connector as the implementation of a BPMN service task, here inside a
  human task's form flow. Quoted from the page's "Use cases" section: "As the user fills fields,
  a service task calls Groq for instant validation and suggestions". The section's own framing
  is "to provide sub-second AI assistance in user-facing tasks".
artefacts:
  - no artefact on the page (prose only); the capture is the page's own "Use cases" section
  - screenshot: 006_ai-groq-process-flow.png
capture_quality: legible
capture_width_px: 1884
---

## What the page shows

The Groq AI connector page of the Bonita 2026.2 documentation. Its "Use cases" section is headed
"Real-time form assistance" and introduces it as "Use the Ask operation with Groq's ultra-fast
inference to provide sub-second AI assistance in user-facing tasks. This is ideal for live form
validation, auto-completion suggestions, or contextual help within human tasks." The
"Process flow:" list is

> A user opens a human task form with complex data entry requirements
> As the user fills fields, a service task calls Groq for instant validation and suggestions
> The AI response is returned in under 500ms, providing a seamless user experience
> The validated data is submitted and the process continues

## Observations

- Here the AI step sits *inside* the process's human-task interaction: a BPMN user task's form
  and a service task calling the Ask operation behind it. The delegated binding is the same as
  on the other AI connector pages, but it is tied to a form rather than to a document.
- No figure of any kind is published on the page.

## Notes for the researcher

Captured from the same page render as record 001. Sibling pages are records 001-009.
