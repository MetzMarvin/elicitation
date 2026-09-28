---
n: 648
record: 003
url: https://docs.processmaker.com/docs/smart-extract
source: processmaker
surface: docs:processmaker
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: Smart Extract is a process object configured with "a specific extraction model", stores its results in Request variables and is documented with Loop Activity semantics, but the page never states that the model is an AI/ML model. Is this an AI element inside the process (INCLUDE), or E2-no-ai-element?
bpmn_evidence: |
  Smart Extract is a connector object of the Process Modeler. Document images 3 and 5 are its shape as
  the Modeler draws it: a rounded BPMN activity rectangle on the dotted canvas grid, carrying a gear
  icon and the label "Smart Extract". Image 7 is its Configuration/Name panel ("Configuration / Name:
  Smart Extract"), image 8 its Variable Name panel ("Variable Name: file_upload - Variable containing
  the file to be sent", with the Loop Activity switch "Use Custom Array for Multi-Instance"), image 9
  its model selectors ("Select Model Type / Model", each a search dropdown) and images 10-14 its Loop
  Activity panels. The prose places the object in a process and at runtime: "It can be added to a
  process directly from the Process Modeler and configured with a specific extraction model"; "The
  results of the extraction are stored in Request variables and can be used in subsequent process
  steps". As with records 001 and 002, no image on the page shows a process diagram containing the
  object.
ai_evidence: |
  The AI is not spelled out. The page never uses the word AI or LLM for this object; what it says is
  that the object is "configured with a specific extraction model" and that the extraction is performed
  by that model. That is the ambiguity this row exists for: a document-data-extraction model selected
  from a list is, in 2026, an AI/ML model in every comparable vendor's documentation (and ProcessMaker's
  own IDP page, `apidocs/idp-package`, states the same family of technology is AI/ML), but this page
  does not say so. The census therefore cannot quote an AI statement from the page.
artefacts:
  - screenshot: 003_smart-extract.png
  - file: ledgers/processmaker.raw/figures/docs__smart-extract/003_Smart_Extract_Name.png
  - file: ledgers/processmaker.raw/figures/docs__smart-extract/004_Smart_Extract_-_Request_Variable.png
  - file: ledgers/processmaker.raw/figures/sh_smartextract.png
capture_quality: legible
capture_width_px: 1712
---

## What the page is

`docs/smart-extract`, page title "Smart Extract Connector", a child of DESIGNER > Connectors in the
ProcessMaker Platform documentation. It documents an object that reads an uploaded document and writes
extracted fields into Request variables.

## What the capture shows

- image 3 (repeated at image 5) - **the artefact**: the Smart Extract object's shape, a rounded BPMN
  activity rectangle with a gear icon on the Modeler's dotted canvas grid.
- image 7 - the Configuration/Name panel.
- image 8 - the Variable Name panel ("Variable containing the file to be sent") and the Loop Activity
  switch.
- image 9 - the "Select Model Type / Model" selectors, both empty dropdowns with the validation
  messages "Please select a model type" and "Please select a model".
- the remaining images are the object's Loop Activity panels and the page's Human-In-The-Loop screens.

## Why this is UNCERTAIN and not E2

The exclusion `E2-no-ai-element` would be a judgement that the object is *not* AI-bound. Nothing on the
page supports that claim; what the page leaves unsaid is whether the model is AI/ML. CLAUDE.md section
3: "If the AI mention is ambiguous, or an element's implementation might be AI-bound but is not
visible, the verdict is UNCERTAIN, never E2." The same rule covers this page in the other direction
too - the model itself is not visible, only the dropdown that selects it.

## Observations

- The mechanical AI screen did not fire on this page precisely because the page avoids the word AI;
  the extended lexicon run over the same text (intelligent document processing, semantic, model,
  recommendation) is what surfaced it for a human look.
- If the researcher rules this INCLUDE, then the sibling item `smart-extract-models` (row 649) stays
  E0: it documents only the validation records, with no process artefact on the page.
