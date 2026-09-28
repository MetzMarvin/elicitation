---
n: 0
url: https://documentation.ofelia.com/bonita/latest/process/ai-deepseek-connector
source: bonitasoft
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: >-
  The page's "Use cases" section describes a process in which "A service task uses the Ask
  connector to generate structured summaries", i.e. an AI connector attached to a BPMN activity
  as its implementation - but the page publishes no diagram, no image and no .bpmn/.proc file of
  that process (prose only). Does a text-only process-flow narrative that binds a service task
  to an AI connector contribute an artefact to the corpus in its own right, or is it binding
  evidence for the connector and therefore not a corpus item?
bpmn_evidence: >-
  None published on this page: no diagram, no figure that names one, and no `.bpmn`/`.proc`
  link (checked in the page source). The process appears only as the numbered list under
  "Process flow", i.e. as prose.
ai_evidence: >-
  The AI element is the connector as the implementation of a BPMN service task. Quoted from the
  page's "Use cases" section: "A service task uses the Ask connector to generate structured
  summaries". The step that follows - "A human task reviews flagged items that require
  attention" - puts a human BPMN task downstream of the AI step.
artefacts:
  - no artefact on the page (prose only); the capture is the page's own "Use cases" section
  - screenshot: 004_ai-deepseek-process-flow.png
capture_quality: legible
capture_width_px: 1884
---

## What the page shows

The DeepSeek AI connector page of the Bonita 2026.2 documentation. Its "Use cases" section is
headed "Cost-effective document summarization" and introduces it as "Use the Ask operation to
summarize large volumes of documents at a fraction of the cost of other providers. DeepSeek V3
delivers quality comparable to GPT-4o at 10-70x lower cost per token." The "Process flow:" list
is

> A batch of support tickets or reports is collected in the process
> A service task uses the Ask connector to generate structured summaries
> The summaries are stored as BDM objects for dashboards and reporting
> A human task reviews flagged items that require attention

## Observations

- The same delegated-binding shape as the other AI connector pages: one BPMN **service task**
  whose implementation is the Ask operation, with a human task downstream.
- No figure, no screenshot, no `.bpmn`/`.proc` file on the page: the process exists only as the
  numbered list.

## Notes for the researcher

Captured from the same page render as record 001. Sibling pages are records 001-009.
