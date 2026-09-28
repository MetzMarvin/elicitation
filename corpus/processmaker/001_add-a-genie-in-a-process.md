---
n: 283
record: 001
url: https://docs.processmaker.com/docs/add-a-genie-in-a-process
source: processmaker
surface: docs:processmaker
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: An AI node type whose own BPMN shape, configuration and loop/boundary-event semantics are published, but with no process diagram containing it - is that a corpus item (INCLUDE, the same "node type only" class recorded for IBM BAMOE as records 006/007), or does the artefact criterion require a diagram in which the AI element sits inside a process?
bpmn_evidence: |
  The page publishes a modelling object, not a diagram. The decisive images are the object's own shape
  (document images 3 and 4): a rounded BPMN activity rectangle sitting on the Process Modeler's dotted
  canvas grid, carrying the Genie-lamp icon in its top-left corner and the word "FlowGenie" as its
  label - the same rounded-rectangle shape the Modeler draws for every task-type object. Image 7 is the
  object's Configuration panel ("Configuration / FlowGenie Studio / Genie Name: Summarize Article /
  Select the Genie: Article summary"). Images 8-12 are the panels that are only meaningful for a node
  placed in a diagram: Loop Activity and Loop Mode ("No Loop Mode", "Loop", "Multi-instance (Parallel)",
  "Multi-instance (Sequential)"), Request Variable Array and Node Identifier. The prose gives the
  object full BPMN activity semantics: it is added "from one of the following locations in Process
  Modeler" (Object Panel, Object Bar, right-click context menu), it obeys Pool containment ("If your
  process has a Pool object, the FlowGenie object cannot be placed outside of the Pool"), and it
  supports boundary events and sequence flows.
  What is missing is a figure of a process: no image on the page shows a Process Modeler canvas with
  the Genie node placed among tasks, gateways and events. The claim "this source publishes a BPMN
  process containing an AI node" therefore rests on the object's shape and prose, not on a diagram.
ai_evidence: |
  The AI element is the node itself and the page names it as such: the FlowGenie object is bound to a
  Genie, and a Genie is the unit ProcessMaker's FlowGenie Studio builds and manages ("Select the Genie:
  Article summary"). The worked example names a concrete binding: Genie Name "Summarize Article",
  Genie "Article summary", and its output mapped to a Request variable. The DESIGNER section index
  describes the family as "generate AI-powered tasks by simply entering a description", and the
  FlowGenie section index describes adding "a Genie to a process using a modeling object in the
  Modeler". So the element inside the process is a call to a configured AI agent, invoked as a task in
  the flow.
artefacts:
  - screenshot: 001_add-a-genie-in-a-process.png
  - file: ledgers/processmaker.raw/figures/docs__add-a-genie-in-a-process/001_image_130_.png
  - file: ledgers/processmaker.raw/figures/docs__add-a-genie-in-a-process/003_image_134_.png
  - file: ledgers/processmaker.raw/figures/sh_genie2.png
capture_quality: legible
capture_width_px: 1712
---

## What the page is

`docs/add-a-genie-in-a-process`, a child of DESIGNER > FlowGenie in the ProcessMaker Platform
documentation. It documents the FlowGenie modelling object: where it can be added, how it is
configured with a Genie, and how it behaves inside a process.

## What the capture shows

Three images, laid out at the document positions they occupy:

- image 3 (and its duplicate at image 4) - **the artefact**: the FlowGenie object's own shape, a
  rounded BPMN activity rectangle with the Genie-lamp icon, drawn on the Modeler's dotted canvas grid.
- image 7 - the Configuration panel: "Genie Name: Summarize Article", "Select the Genie: Article
  summary".
- the remaining images on the page are the object's Loop Activity / Loop Mode panels, the Node
  Identifier panel and two Object Panel "+" tiles.

## Why this is UNCERTAIN and not E2

The exclusion code `E2-no-ai-element` requires a BPMN artefact that demonstrably contains no AI
element. Here the element is plainly AI-bound, but the page never shows it inside a process model, so
the census cannot demonstrate from this source a *diagram* in which an AI node occupies a place in a
flow. CLAUDE.md section 3 resolves exactly this doubt in favour of collection: the row is recorded in
full, with the question left for the researcher.

## Observations

- If the researcher accepts "an AI node type published with its own BPMN shape and configuration" as
  an artefact, this is an INCLUDE and the same class as the IBM BAMOE Gen AI Task records. If the
  criterion requires the AI element to be visible inside a process diagram, this page is E2 and the
  source's AI-node evidence rests on `ai-asset-generation` instead.
- The Genie is bound by name at design time ("Summarize Article"), so the AI behaviour is
  parameterised in the model, not implied.
