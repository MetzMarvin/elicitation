---
n: 0
url: https://documentation.ofelia.com/bonita/latest/process/ai-openai-connector
source: bonitasoft
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: >-
  The page's "Use cases" section describes a process in which "A service task uses the Ask
  connector to generate an email draft", i.e. an AI connector attached to a BPMN activity as its
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
  page's "Use cases" section: "A service task uses the Ask connector to generate an email
  draft". The steps around it are BPMN tasks too - "A human task presents the draft for agent
  review and editing" and "The email is sent via an email connector" - and the configuration
  block names the model (`"chatModelName": "gpt-4o"`) and the system prompt.
artefacts:
  - no artefact on the page (prose only); the capture is the page's own "Use cases" section
  - screenshot: 009_ai-openai-process-flow.png
capture_quality: legible
capture_width_px: 1884
---

## What the page shows

The OpenAI connector page of the Bonita 2026.2 documentation. Its "Use cases" section is headed
"Generate customer email responses" and introduces it as "Use the Ask operation to generate
professional email drafts based on customer support cases." The "Process flow:" list is

> A support ticket is created with customer information and issue description
> A service task uses the Ask connector to generate an email draft
> A human task presents the draft for agent review and editing
> The email is sent via an email connector

followed by the "Configuration:" block (`"apiKey": "${AI_API_KEY}"`, `"chatModelName":
"gpt-4o"`, a `systemPrompt` naming a professional customer service representative).

## Observations

- The clearest of the nine of the "AI as one step in a human process" shape: an AI service task
  between a form/start and a human review task, with the human able to edit the model's output.
- Still no figure on the page: the flow is prose plus a JSON configuration block.

## Notes for the researcher

Captured from the same page render as record 001, so the wording can be checked against the
screenshot. Sibling pages are records 001-009; records 010 and 011 are the `.proc` demo files
that bind the Anthropic and Azure connectors to a real service task.
