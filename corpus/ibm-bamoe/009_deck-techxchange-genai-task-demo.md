---
n: 135
record: 009
url: https://community.ibm.com/HigherLogic/System/DownloadDocumentFile.ashx?DocumentFileKey=48e39a74-897d-4027-879e-16d3ee789a0e&forceDialog=0
source: ibm-bamoe
surface: community:ibm.com
accessed: 2026-09-25
verdict: INCLUDE
needs_human_ruling: false
question:
bpmn_evidence: |
  Page 12 of the deck, under the section the agenda calls "AI Demos - BAMOE Gen AI Task for BPMN -
  BAMOE MCP Server", is a BAMOE Canvas screen: the project header reads "Workflow | GenAI Task
  demo", the editor's shape palette stands on the left, and on the dotted canvas a complete
  three-element BPMN process is drawn - a start event, one task, and an end event, joined by
  sequence flows. The task is labelled "Generate some content". The slide's own text, from the
  deck's text layer, is "BAMOE Gen AI Task for BPMN" and the canvas footer reads "Example project:
  process-saga-quarkus".
ai_evidence: |
  The single task in the process carries the AI sparkle of the Gen AI Task in its top-left corner, so
  the AI element is the only activity in the process. The deck's release-highlights pages state the
  capability in words: "Generative AI task, to incorporate LLM invocation within a workflow" and
  "MCP Server, to publish BAMOE applications as tools for agents to use" (page 16, release theme
  "AI", version 9.3.0), with page 17 adding "AI Agent task, to delegate work to an autonomous agent".
artefacts:
  - screenshot: 009_ibm-bamoe-deck-tx-genai-task-demo.png
  - file: ledgers/_bamoe_comm/techxchange_2025.pdf
  - file: ledgers/_bamoe_comm/tx_hi_12-12.png
  - file: ledgers/_bamoe_comm/tx_hi_10-10.png
  - file: ledgers/_bamoe_comm/sheet_deck_tx.png
capture_quality: legible
capture_width_px: 3467
---

## What the file shows

A 20-page IBM TechXchange 2025 session deck (session 3058, "Business Automation in the hybrid cloud
with IBM BAMOE", Phil Simpson and Tiago Bento). Page 12 is the Gen AI Task demo:

- Project header "Workflow | **GenAI Task demo**", editor toolbar and palette, dotted canvas.
- The process: start event → **"Generate some content"** (the AI sparkle in its corner) → end event.
- Canvas footer "Example project: **process-saga-quarkus**"; slide header "02-2025 Roadmap Update".

Page 10, on the same deck, is the 9.2.0 "Process Automation" slide with **two** BPMN diagrams and no
AI element in either:

- the hiring process in its pre-AI form - start → "New Hiring" → gateway → **"Generate base Offer"**
  → **"Log Offer"** → "HR Interview" (timer) → "IT Interview" (timer) → gateway → "Send Offer to
  Candidate" → end, with "Send notification HR Interview avoided" and "Application denied" branches
  and the flow label "Candidate doesn't meet requirements" (caption "Example project:
  jbpm-compact-architecture-example");
- the saga order process - "reserve stock" / "process payment" / "schedule shipping" / "Order
  Success" with compensation boundary events, the cancel tasks and a "Handle Error" sub-process
  (caption "Example project: process-saga-quarkus").

## Observations

- Page 12 is the minimal case of the phenomenon this census is after: a BPMN process whose *only*
  activity is the AI task, wired between a start and an end event. There is no ambiguity about where
  the AI sits - it is the process.
- **Page 10 is the corpus's cleanest negative.** It is a full BPMN 2.0 diagram (events, exclusive
  gateways, timer boundary events, compensation, a sub-process) with no AI element, and it holds the
  same hiring process that row 119 (record 004) later shows with the Gen AI task "Create Offer"
  carrying the watsonx/granite binding. The pair 9.2.0-page-10 → 9.3.0-record-004 is the
  before/after of an AI node entering an existing process; record 007 is the intermediate state in
  which the node has been dropped on the canvas but not yet wired in.
- Pages 16-17 give the vendor's own framing of the AI work in text ("Generative AI task, to
  incorporate LLM invocation within a workflow"; "AI Agent task, to delegate work to an autonomous
  agent"), which is useful for the thesis's vocabulary even though those pages carry no diagram.

## Notes for the researcher

- The deck's page 10 is *not* a separate row: the deck is one enumerated item, and its diagrams are
  described here. If you want the pre-AI hiring diagram as a corpus item in its own right (it is a
  good negative control for "BPMN without AI"), it can be lifted from
  `ledgers/_bamoe_comm/tx_hi_10-10.png`, which is kept alongside this record's capture.
- The deck's download URL is the community platform's attachment endpoint and was verified to
  resolve (HTTP 302 → higherlogicdownload.s3.amazonaws.com/IMWUC/<key>_file.pdf); the page that
  published the link was not preserved in this session's captures, so the referring page is not
  claimed here.
