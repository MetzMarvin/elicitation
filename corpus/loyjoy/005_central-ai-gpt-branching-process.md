---
n: 235
source: loyjoy
source_name: LoyJoy (technical documentation, BPMN 2.0 reference)
source_type: vendor documentation
title: Centralized AI Handling
url: https://docs.loyjoy.com/guides/central_ai/
accessed: 2026-09-24
verdict: INCLUDE
needs_visual_check: false
needs_human_ruling: false
bpmn_evidence: "a LoyJoy process-editor figure: message start event (circle) -> module box '#1 Simple message' -> module box '#2 GPT gateway' (carrying a green '1' annotation badge) -> exclusive gateway (diamond with X) whose outgoing sequence flows are labelled 'Branch 1', 'Branch 2' and 'Branch 3' -> module boxes '#3 GPT Knowledge', '#5 GPT Follow-up question', '#7 GPT Smalltalk'; '#3 GPT Knowledge' flows on to '#4 Questionnaire' (with an email icon), '#5' to '#6 Automatic jump' -> end event, and '#4'/'#7' rejoin at a second exclusive gateway -> end event; a second fragment shows a message start event -> '#8 Automatic jump' -> end event. The page's own image metadata names it 'Central AI Agent Configuration in LoyJoy Backend'"
bpmn_evidence_quote: "add a Message start module as usual, but instead of adding the AI modules"
ai_evidence: "four GPT modules sit inside the depicted process: '#2 GPT gateway' immediately after the start event, and '#3 GPT Knowledge', '#5 GPT Follow-up question' and '#7 GPT Smalltalk' on the three gateway branches. The page documents the pattern: the central agent 'handles the generative AI for several or all your agents'"
ai_evidence_quote: "LoyJoy allows you to use one central AI agent that handles the generative AI for several or all your agents in LoyJoy."
artefacts:
  screenshot: corpus/loyjoy/005_central-ai-gpt-branching-process.png
  archive: ledgers/loyjoy.raw/html_rest/085.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 912
capture_method: chrome-devtools-mcp/curl, the page's figure asset https://docs.loyjoy.com/assets/images/central_ai-*.png (alt "Central AI Agent", title "Central AI Agent Configuration in LoyJoy Backend"), downloaded to ledgers/loyjoy.raw/rest_imgs/ and copied to corpus/loyjoy/. Page HTML archived to ledgers/loyjoy.raw/html_rest/085.html
---

## What the page shows

`/guides/central_ai/` is the guide for running one central AI agent for several LoyJoy agents. Its
figure `central_ai-*.png` (915 x 1455 native, alt "Central AI Agent") is the strongest single
AI-in-process artefact found outside the `/bpmn/` section.

**The AI-in-BPMN artefact, element by element** (read off the capture):

- a **start event** (plain circle) -> module box **"#1 Simple message"**;
- module box **"#2 GPT gateway"** with a green "1" badge - the AI element directly in the flow;
- an **exclusive gateway** (X diamond) with the outgoing flows labelled **"Branch 1"**, **"Branch 2"**,
  **"Branch 3"**;
- the three branches feed **"#3 GPT Knowledge"**, **"#5 GPT Follow-up question"** and
  **"#7 GPT Smalltalk"**;
- **"#3"** continues to **"#4 Questionnaire"**; **"#5"** to **"#6 Automatic jump"** -> end event;
  **"#4"** and **"#7"** rejoin at a second exclusive gateway -> end event;
- a separate fragment below: **message start event -> "#8 Automatic jump" -> end event**.

The page is a *guide*, not a module reference page, and the figure is the published diagram of the
pattern (no editor chrome). The modules are drawn in the same notation the `/bpmn/` reference pages
use ("#N" module boxes, round events, X-diamond gateways).

## Observations (description only, no interpretation)

- **AI activity - function:** the GPT gateway classifies the user's message into one of the three
  branches; each branch module then answers (knowledge lookup, follow-up question, smalltalk).
- **AI activity - element type:** four module boxes inside the process; one of them (the GPT gateway)
  is directly adjacent to an exclusive gateway.
- **Authority - downstream:** the branches continue into further modules (questionnaire, automatic
  jump); the central-agent pattern means other agents jump into this agent's AI configuration.
- **Authority - data:** not visible on the page.
- **Authority - control:** the exclusive gateway and the "Branch 1/2/3" labels are the control
  structure; the branching decision itself is taken by the GPT gateway module.
- **Input provenance:** the start event (a chat message).
- **Guards present:** none drawn.
- **Prompt / model detail visible:** none on this page (the guide documents configuration elsewhere).

## Notes for the researcher

- Found by the secondary sweep of the docs host, i.e. it lies **outside** the `/bpmn/` section that
  the first 150 rows cover - this is exactly the kind of row the exhaustiveness claim depends on.
- The page's second figure (`other_agent-*.png`, 574 x 1020, alt "Other Agent") shows a two-module
  canvas fragment; both figures are archived in `ledgers/loyjoy.raw/rest_imgs/`.
- The page text does not contain the string "GPT gateway": the module names are read from the figure
  itself, which is legible at native resolution.
