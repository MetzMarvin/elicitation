---
n: 0
url: https://documentation.ofelia.com/bonita/latest/process/ai-ollama-connector
source: bonitasoft
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: >-
  This page's "Use cases" section is about building the connector rather than running a
  process: "Developer configures a connector in Bonita Studio with Ollama", then "Prompts and
  JSON schemas are tested locally with instant feedback". The AI connector is still the
  implementation of a service task (the "Operations" section lists Ask, Classify and Extract),
  but the published flow is a development workflow rather than a business process. Does this
  page contribute an artefact to the corpus in its own right, or is it binding evidence for the
  connector (and is a Studio configuration flow a process at all)?
bpmn_evidence: >-
  None published on this page: no diagram, no figure that names one, and no `.bpmn`/`.proc`
  link (checked in the page source). The process appears only as the numbered list under
  "Process flow", i.e. as prose - and here that list describes a development workflow.
ai_evidence: >-
  The AI element is the connector as the implementation of a BPMN service task. Quoted from the
  page's "Use cases" section: "Developer configures a connector in Bonita Studio with Ollama",
  and the section's framing "Use Ollama during development and testing phases to iterate on AI
  prompts and configurations without incurring API costs".
artefacts:
  - no artefact on the page (prose only); the capture is the page's own "Use cases" section
  - screenshot: 008_ai-ollama-process-flow.png
capture_quality: legible
capture_width_px: 1884
---

## What the page shows

The Ollama connector page of the Bonita 2026.2 documentation. Its "Use cases" section is headed
"Development and testing" and introduces it as "Use Ollama during development and testing phases
to iterate on AI prompts and configurations without incurring API costs or sending sensitive
test data to external services." The "Process flow:" list is

> Developer configures a connector in Bonita Studio with Ollama
> Prompts and JSON schemas are tested locally with instant feedback
> Once validated, the connector configuration is switched to a cloud provider for production
> The same prompt and schema work across all providers

## Observations

- This is the one page of the nine whose "process flow" is a *development* flow: the steps are a
  developer's actions in Bonita Studio, not BPMN activities of a business process. Whether that
  counts as a process at all is part of the record's question.
- Like the other eight pages it publishes no figure, so nothing on the page is an artefact
  independently of the question above.

## Notes for the researcher

Captured from the same page render as record 001. Sibling pages are records 001-009; this is the
weakest of the nine, kept rather than dropped because the connector is still an AI binding that
a service task can carry.
