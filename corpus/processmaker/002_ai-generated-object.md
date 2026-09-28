---
n: 292
record: 002
url: https://docs.processmaker.com/docs/all-in-one-ai-asset-generation
source: processmaker
surface: docs:processmaker
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: Design-time AI object - the "AI Generated object" is placed in the process model but becomes an ordinary Sub Process / Form Task / Script once the AI has generated the asset. Does it count as an AI element inside the process (INCLUDE), or is it E2-no-ai-element because the AI runs at design time and nothing AI-bound survives in the running process?
bpmn_evidence: |
  The page is titled "AI Generated Object" and documents a process object you place on the model. The
  decisive images are the object's own shape (document images 4 and 5, the same file twice): a rounded
  BPMN activity rectangle on the Process Modeler's dotted canvas grid carrying a robot-head icon. Image
  6 is the AI Assistant panel that configures it ("AI Assistant / Generate an Asset", with the cards
  "Sub Process From Text" and "Screen From Text"). The page's own instruction is "Place the AI Generated
  object onto your Process model like any other object", and the object is added from the Object Panel,
  the Object Bar or the context menu of the Process Modeler.
  The page also states what the object becomes: "After creating your AI-generated Process, the current
  AI Generated object becomes a Sub Process object that references the new Process you created using
  AI". As with record 001, no image on the page shows a process diagram in which this object sits.
ai_evidence: |
  The AI is named by the object itself and by the panel that drives it: "AI Assistant", "Generate an
  Asset", and the asset kinds it generates ("Sub Process From Text", "Screen From Text"). The page's
  guidance is about the AI Generator's behaviour ("When generating multiple assets, the AI Generator
  creates a consistent JSON data model across all assets in the process"; "If an asset already exists
  (for example, a Screen in the first task), the AI Generator does not create a duplicate").
  The AI acts at design time. What it leaves behind in the process is an ordinary Sub Process, Form
  Task or Script - the AI-bound state is temporary and is not what the running process calls.
artefacts:
  - screenshot: 002_ai-generated-object.png
  - file: ledgers/processmaker.raw/figures/docs__all-in-one-ai-asset-generation/001_32bb5e47-bfae-452f-aa1c-656f50f37731.png
  - file: ledgers/processmaker.raw/figures/docs__all-in-one-ai-asset-generation/003_e9f0b8b2-aca4-4943-8cf2-9832c7cb38de.png
  - file: ledgers/processmaker.raw/figures/sh_genie2.png
capture_quality: legible
capture_width_px: 1712
---

## What the page is

`docs/all-in-one-ai-asset-generation`, whose page title is "AI Generated Object" (the URL slug and the
title disagree; the census records the item under its title). A child of BUSINESS PROCESSES >
Processes > Modeling Objects, i.e. the same family as Form Task, Manual Task and Sub Process.

## What the capture shows

- images 4 and 5 - **the artefact**: the AI Generated object's shape, a rounded BPMN activity
  rectangle with a robot-head icon, on the Modeler's dotted canvas grid.
- image 6 - the AI Assistant panel: "Generate an Asset", with "Sub Process From Text" and "Screen
  From Text" cards.
- the page's other images are the AI Generator's asset-creation screenshots.

## Why this is UNCERTAIN and not E2

The assignment file for this source flags this page as a design-time trap: the AI generates the model,
so the exclusion `E2` applies "unless the generated process also contains a Genie node". No Genie node
appears anywhere on the page. On the other hand the object is *placed inside the process model* and is
drawn in BPMN notation there, and ProcessMaker's own documentation gives it the full modelling-object
treatment. CLAUDE.md section 3 is explicit that doubt about whether an element is AI-bound resolves to
UNCERTAIN and never to E2; the researcher's ruling decides between the two readings.

## Observations

- This page and record 001 are the two halves of the same question: ProcessMaker's AI-bound objects
  are documented as modelling objects with their own BPMN shapes, and in both cases the diagram that
  would settle the question is absent.
- The 2025–2026 release notes and the "Create a Process from Text" page (row 359) describe the same
  generator from the other end: generating a whole process from a description. Their verdict in this
  ledger is E2, because the artefact those pages publish is an ordinary process model.
