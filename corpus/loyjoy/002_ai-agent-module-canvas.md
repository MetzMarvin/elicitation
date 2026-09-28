---
n: 12
source: loyjoy
source_name: LoyJoy (technical documentation, BPMN 2.0 reference)
source_type: vendor documentation
title: AI Agent
url: https://docs.loyjoy.com/bpmn/subprocesses/ai_agent/
accessed: 2026-09-24
verdict: INCLUDE
needs_visual_check: false
needs_human_ruling: false
bpmn_evidence: "a LoyJoy process-editor screenshot of a complete little process: message start event (envelope in a circle) -> module box '#2 AI Agent' (carrying a green '1' annotation badge) -> module box '#3 Add variables', selected, with a sequence flow arrow -> end event (plain circle). The properties panel beside it is the editor's 'Enter target / Enter source' panel. The page sits in the docs' 'BPMN 2.0 Reference / BPMN Modules' section; LoyJoy's process modules are the elements its BPMN process editor draws (no .bpmn XML published)"
bpmn_evidence_quote: "Start by adding the \"AI Agent\" module to your process."
ai_evidence: "the module box '#2 AI Agent' is a step inside the drawn process, sitting between the message start event and the end event; the page describes it as the component that lets 'an AI ... understand user intent and use a set of tools to respond' and that 'replaces the older AI Gateway, AI Knowledge, AI Prompt, AI Smalltalk and AI Recommender modules'"
ai_evidence_quote: "The AI Agent module is LoyJoy's new component for building AI-driven conversational experiences."
artefacts:
  screenshot: corpus/loyjoy/002_ai-agent-module-canvas.png
  archive: ledgers/loyjoy.raw/html/012.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1210
capture_method: chrome-devtools-mcp, in-page fetch() of the figure asset https://docs.loyjoy.com/assets/images/question_count-*.png (1210 x 730 native); saved via base64 to corpus/loyjoy/002_ai-agent-module-canvas.png. Page HTML archived with curl to ledgers/loyjoy.raw/html/012.html
---

## What the page shows

`/bpmn/subprocesses/ai_agent/` is the reference page for LoyJoy's current AI module. It is
39,987 characters of body text and carries **one** figure, `question_count.png`
(1210 x 730 native) — a process-editor screenshot reproduced as
`002_ai-agent-module-canvas.png`.

**The AI-in-BPMN artefact, element by element** (read off the capture):

- a **message start event** — envelope in a circle, with the editor's small "+" affordance
  beneath it;
- a module box **"#2 AI Agent"**, carrying a green "1" annotation badge;
- a sequence flow (arrow) down to a module box **"#3 Add variables"**, drawn selected
  (blue outline, variable icon);
- a sequence flow down to an **end event** (plain circle);
- the editor's right-hand properties panel, shown for the "#3 Add variables" step
  ("Enter target": Process variable `question`, Variable scope `process-specific`;
  "Enter source": `Fun` = `increment`, `question_count`, value `1`).

The canvas is the LoyJoy process editor; the AI element is a **module inside the drawn
process**, not a separate diagram, a roadmap item or a documentation aid.

**Page prose on the AI element**, verbatim: "The AI Agent module is LoyJoy's new component
for building AI-driven conversational experiences. It allows an AI to understand user intent
and use a set of tools to respond to requests and complete tasks. The agent can operate
iteratively, meaning it can call multiple tools in sequence (e.g., search a knowledge base,
then read a full document, then search the web) before formulating a final answer for the
user. This module replaces the older AI Gateway, AI Knowledge, AI Prompt, AI Smalltalk and
AI Recommender modules."

The same page documents the module's tool configuration (unique names, descriptions, usage
logic, "we recommend keeping the number below 30"), a custom-instruction prompt field, and a
settings popover with "Show/hide AI label", an editable "AI label text and URL", and "AI
agent status messages". That is the richest account of an AI element's *configuration*
found on this source.

## Observations (description only, no interpretation)

- **AI activity - function:** understand user intent, call tools iteratively, formulate a
  final answer for the user (page prose), plus optional voice settings for phone agents.
- **AI activity - element type:** one module box ("AI Agent") inside the process; the tools
  it may call are configured in a sub-panel, not drawn as separate process elements.
- **Authority - downstream:** tools can include "searching knowledge or running a process";
  the page names Knowledge Search and Web Search tools as examples, no fixed tool list.
- **Authority - data:** a knowledge base is named as a possible tool and described as being
  called multiple times per question; no data source is drawn in the figure.
- **Authority - control:** the page provides usage-logic instructions ("Only use the
  'Discount' tool if the user is a registered customer and mentions 'coupon'") written in a
  Custom Instruction, i.e. prompt-level, not process-level, control.
- **Input provenance:** user message (the process starts at the message start event).
- **Guards present:** none drawn; the page mentions an AI-answer label ("AI-generated") that
  can be shown to end users.
- **Prompt / model detail visible:** custom instructions field described; no model name on
  the page; no prompt template text.

## Notes for the researcher

- The single figure is a crop of the module plus its canvas neighbourhood, not the whole
  process, and it is dominated by the properties panel (the "AI Agent" box occupies the left
  third). Capture is the native asset at 1210 x 730 and is recorded as `legible`.
- The page's own statement that this module "replaces the older AI Gateway, AI Knowledge, AI
  Prompt, AI Smalltalk and AI Recommender modules" is why the legacy AI module pages
  (`ai_knowledge`, `ai_prompt`, `ai_recommender`, `ai_smalltalk`, `ai_knowledge_followup`)
  are in this source's frontier and are judged separately in the ledger; there is **no**
  separate `/bpmn/subprocesses/ai_gateway/` URL in the sitemap.
- Raw evidence for the excluded rows of this source lives in `ledgers/loyjoy.raw/`.
