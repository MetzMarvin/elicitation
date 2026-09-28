---
n: 0
url: https://documentation.ofelia.com/bonita/latest/process/ai-anthropic-connector
source: bonitasoft
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: >-
  This page is the docs-side instance of the class the assignment calls delegated binding: its
  "Use cases" section describes a process in which "A service task uses the Ask connector with
  the document attached", i.e. an AI connector attached to a BPMN activity as its
  implementation - but the page publishes no diagram, no image and no .bpmn/.proc file of that
  process (prose only). Does a text-only process-flow narrative that binds a service task to an
  AI connector contribute an artefact to the corpus in its own right (a process with an AI
  element), or is it binding evidence for the connector and therefore not a corpus item, like
  the scheer-pas record 002 question?
bpmn_evidence: >-
  None published on this page: the page carries no diagram, no figure that names one, and no
  `.bpmn`/`.proc` link (checked in the page source). The process appears only as the numbered
  list under "Process flow", i.e. as prose.
ai_evidence: >-
  The AI element is the connector as the implementation of a BPMN service task. Quoted from the
  page's "Use cases" section: "2. A service task uses the Ask connector with the document
  attached". Step 3 names the model ("Claude analyzes both text and visual elements (stamps,
  signatures, formatting)") and step 4 the binding's result ("The structured result is stored
  for downstream verification"). The "Operations" section lists the connector's operations -
  Ask, Classify, Extract - which is the vocabulary a Bonita connector binds to a task.
artefacts:
  - no artefact on the page (prose only); the capture is the page's own "Use cases" section
  - screenshot: 001_ai-anthropic-process-flow.png
capture_quality: legible
capture_width_px: 1884
---

## What the page shows

The Anthropic connector page of the Bonita 2026.2 documentation (breadcrumb "Bonita / Processes
/ Connectors / Bonita official connectors / AI / Anthropic"). Its sections are *Getting started*,
*Connection configuration*, *Available models*, *Operations* (Ask, Classify, Extract), *Use
cases*, *Configuration tips* and *Source code*. The captured region is the "Use cases" section:
the heading "Document analysis with vision", the sentence "Use Claude's native vision support to
analyze scanned documents, photos of forms, or image-based PDFs with visual elements like
signatures, stamps, or handwritten notes.", and the numbered "Process flow:" list

> 1. A scanned identity document is uploaded to the process
> 2. A service task uses the Ask connector with the document attached
> 3. Claude analyzes both text and visual elements (stamps, signatures, formatting)
> 4. The structured result is stored for downstream verification

The left sidebar of the capture shows the sibling pages of the same "AI" section - OpenAI,
Anthropic (highlighted), Cohere, DeepSeek, Gemini, Groq, Mistral, Azure AI Foundry, Ollama - all
of which are records 001-009 of this source.

## Observations

- The page documents a **binding**, not a diagram: a service task in a Bonita process whose
  implementation is the Ask operation of the Anthropic connector. That is the delegated-binding
  class the assignment puts in scope, and it is stated in the vendor's own words.
- The page publishes **no figure at all** - no screenshot of a process, no BPMN diagram, no
  `.bpmn` or `.proc` file - so nothing on the page is itself an artefact of the corpus's shape.
- Record 010 is the same connector one step further: a `.proc` file that really does carry a
  service task bound to `definitionId="anthropic-ask"`.

## Notes for the researcher

The assignment for this source anticipated this shape ("a plain task whose surrounding text binds
it to an AI connector is `UNCERTAIN` with the binding quoted, never `E2`"). The capture is a
screenshot of the page's own render, so the quoted list and the page's wording can be checked
against it directly.
