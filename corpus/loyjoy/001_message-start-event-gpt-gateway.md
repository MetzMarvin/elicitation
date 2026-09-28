---
n: 7
source: loyjoy
source_name: LoyJoy (technical documentation, BPMN 2.0 reference)
source_type: vendor documentation
title: Message Start Event
url: https://docs.loyjoy.com/bpmn/events/startEvent_message/
accessed: 2026-09-24
verdict: INCLUDE
needs_visual_check: false
needs_human_ruling: false
bpmn_evidence: "a LoyJoy process-editor screenshot: a message start event (envelope icon in a circle) -> module box '#3 GPT gateway' -> an exclusive gateway (diamond with X) whose outgoing sequence flows are labelled 'Branch 1', 'Branch 2', 'Branch 3' -> three further module boxes '#4 GPT Knowledge', '#6 GPT Follow up question', '#8 GPT Smalltalk'; an attached properties panel reads 'Message start' with the trigger text and a Yes/No control. The page sits in the docs' 'BPMN 2.0 Reference / BPMN 2.0 Events' section and the editor is the BPMN process editor LoyJoy documents as its modelling surface (no .bpmn XML and no bpmn-js canvas on the public docs)"
bpmn_evidence_quote: "The message start event is a type of start event that is triggered by the receipt of a message."
ai_evidence: "four AI modules named inside the depicted process: '#3 GPT gateway' directly after the start event, then an exclusive gateway fanning out to '#4 GPT Knowledge', '#6 GPT Follow up question' and '#8 GPT Smalltalk'; the page prose states the AI Agent module follows this event"
ai_evidence_quote: "The message start event is typically followed by an AI Agent module that processes the user's message and generates a response."
artefacts:
  screenshot: corpus/loyjoy/001_message-start-event-gpt-gateway.png
  archive: ledgers/loyjoy.raw/html/007.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: marginal
capture_width_px: 940
capture_method: chrome-devtools-mcp, in-page fetch() of the figure asset https://docs.loyjoy.com/assets/images/icon-*.png (940 x 367 native, no larger version published); saved via base64 to corpus/loyjoy/001_message-start-event-gpt-gateway.png (PNG, first frame equivalent). Page HTML archived with curl to ledgers/loyjoy.raw/html/007.html
---

## What the page shows

`/bpmn/events/startEvent_message/` is the reference page for the message start event in the
"BPMN 2.0 Reference / BPMN 2.0 Events" section of the LoyJoy docs. Its single figure is a
**process-editor screenshot of a GPT-branching process** (see
`001_message-start-event-gpt-gateway.png`).

**The AI-in-BPMN artefact, element by element** (read off the capture):

- a **message start event** — the envelope-in-a-circle event shape, shown magnified by a
  callout in the figure;
- a module box **"#3 GPT gateway"** immediately after it;
- an **exclusive gateway** (diamond marked with an X) whose three outgoing sequence flows
  are labelled **"Branch 1"**, **"Branch 2"**, **"Branch 3"**;
- three module boxes fed by those branches: **"#4 GPT Knowledge"**,
  **"#6 GPT Follow up question"**, **"#8 GPT Smalltalk"**;
- the editor's right-hand properties panel for the selected element, titled
  **"Message start"**, reading "When a new message is entered to the chat footer, this event
  is triggered." with the control "Prevent the current process execution from being saved"
  (Yes / No).

The canvas is the LoyJoy process editor (visible editor chrome: the process breadcrumb
"/ GPT Process", the Process / Branding / Publish / Texts / Assets tabs, "Show chat",
"Preview", the tenant "Katharina" sidebar). No `.bpmn` XML and no rendered `bpmn-js`
canvas is published for this figure.

**Page prose on the AI element**, verbatim: "The message start event is typically followed
by an AI Agent module that processes the user's message and generates a response." The same
page's closing line points at the branching that the figure draws. The four `GPT …` module
names in the figure match the AI-module family the docs describe elsewhere
(`/bpmn/subprocesses/ai_agent/` states that the AI Agent module "replaces the older AI
Gateway, AI Knowledge, AI Prompt, AI Smalltalk and AI Recommender modules").

## Observations (description only, no interpretation)

- **AI activity - function:** not stated on this page; the figure shows four AI-named modules
  chained after the start event, one of them the gateway that fans out to the other three.
- **AI activity - element type:** module boxes inside the process model ("GPT gateway",
  "GPT Knowledge", "GPT Follow up question", "GPT Smalltalk"); the AI Agent module the
  prose names is not itself drawn in this figure.
- **Authority - downstream:** not visible on the page.
- **Authority - data:** the knowledge modules imply a knowledge source, but none is shown.
- **Authority - control:** the exclusive gateway ("Branch 1/2/3") is the only control
  element drawn between the AI modules; no human task is shown.
- **Input provenance:** the start event is a user message from the chat footer ("When a new
  message is entered to the chat footer, this event is triggered.").
- **Guards present:** none observed in the figure.
- **Prompt / model detail visible:** none (no model name, no prompt template).

## Notes for the researcher

- **This is the strongest artefact found on the source**: the AI elements are modules *inside*
  the depicted process, one of them feeding a real BPMN exclusive gateway with three guarded
  branches. The capture is the native figure asset (940 x 367); the figure is a magnifier
  callout crop, so the canvas is only partially visible and the capture is recorded as
  `marginal`. The labels quoted above are legible at native size.
- The page has exactly one image; there is no larger version of it on the docs host.
- `archive` holds the page HTML fetched with `curl` (the docs host serves it without a bot
  challenge), so the figure URL and the prose survive vendor edits.
- Raw evidence files for this source (all downloaded assets, the per-page inventory and the
  classifier reports) live in `ledgers/loyjoy.raw/`.
