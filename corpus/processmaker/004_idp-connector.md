---
n: 486
record: 004
url: https://docs.processmaker.com/docs/idp-connector
source: processmaker
surface: docs:processmaker
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: An AI/ML-bound connector documented as a process modelling object (pool containment, boundary events, sequence flows, loop modes), with its object shape shown but no process diagram, and with its AI nature stated only on the package page of the same docs set - INCLUDE, or E2?
bpmn_evidence: |
  The IDP connector is one of the Process Modeler's connector objects. Document images 5 and 7 are its
  shape as the Modeler draws it: a rounded BPMN activity rectangle on the dotted canvas grid with an
  icon and the label "Intelligent Document Processing". Image 9 is its Configuration/Name panel
  ("Configuration / Name: Intelligent Document Proc..." with the usual "Enter the name of this element"
  hint), image 10 its Variable Name panel ("Variable Name - Variable containing the file to be sent"),
  and images 11-20 its remaining configuration panels and the IDP Admin screens it delegates document
  handling to. The prose is unambiguous that this is an object in a diagram: "Add an IDP connector from
  one of the following locations in Process Modeler"; "If your process has a Pool object, the IDP object
  cannot be placed outside of the Pool"; and it lists the boundary events the object supports. As with
  records 001-003, no image on the page shows a process diagram in which the connector sits.
ai_evidence: |
  Not on this page. This page calls the object "ProcessMaker IDP is ProcessMaker's intelligent document
  processing (IDP) solution" and never uses the word AI. The AI statement lives on another page of the
  same source, `apidocs/idp-package` (recorded in this ledger at row 119), which says: "ProcessMaker IDP
  is technology that uses Artificial Intelligence (AI) and Machine Learning (ML) algorithms to extract
  information and insights from unstructured data sources such as documents, images, and videos." The
  census reads the two pages together because they document the same element; the ambiguity is that the
  artefact page itself never says what the extraction runs on.
artefacts:
  - screenshot: 004_idp-connector.png
  - file: ledgers/processmaker.raw/figures/docs__idp-connector/001_c953ba37-820e-4b4f-b1df-e364c51de365.png
  - file: ledgers/processmaker.raw/figures/docs__idp-connector/003_35af9b62-08a4-43f3-a287-5de5a41de512.png
  - file: ledgers/processmaker.raw/figures/sh_idp.png
capture_quality: legible
capture_width_px: 1712
---

## What the page is

`docs/idp-connector`, a child of DESIGNER > Connectors. It documents the connector that sends an
uploaded document to a ProcessMaker IDP instance and writes the extracted fields back into the process.

## What the capture shows

- images 5 and 7 - **the artefact**: the IDP object's shape, a rounded BPMN activity rectangle labelled
  "Intelligent Document Processing" on the Modeler's dotted canvas grid.
- image 9 - the Configuration panel with the element's Name.
- image 10 - the Variable Name panel ("Variable containing the file to be sent").
- images 11 and 12 - the IDP Admin sign-out screen and its navigation ("Global Settings / Entity
  Management"), i.e. the external system the connector hands the document to.

## Why this is UNCERTAIN and not E2

CLAUDE.md section 3 makes an element whose implementation "might be AI-bound but is not visible" an
UNCERTAIN verdict rather than E2. Here the element *is* AI-bound - the vendor says so on the package
page - but the statement is not on the artefact page, and the process diagram that would show the
connector in place is not published. Ruling E2 would silently drop the source's clearest AI-bound
process element from the corpus.

## Observations

- The mechanical AI screen missed this page and `smart-extract` for the same reason: both are AI
  elements documented without the word AI. The extended lexicon run over the same text is what caught
  them, which is why the method notes that the token census alone would have under-collected here.
- The companion item `idp-settings` (row 487) is E0: it documents the IDP server settings, with no
  process artefact anywhere on the page.
