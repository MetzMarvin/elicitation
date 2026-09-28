---
n: 14
source: loyjoy
source_name: LoyJoy (technical documentation, BPMN 2.0 reference)
source_type: vendor documentation
title: AI Knowledge
url: https://docs.loyjoy.com/bpmn/subprocesses/ai_knowledge/
accessed: 2026-09-24
verdict: INCLUDE
needs_visual_check: false
needs_human_ruling: false
bpmn_evidence: "a minimal LoyJoy process diagram: message start event (envelope in a circle) with the editor's '+' affordance, a sequence flow down into one module box labelled '#2 GPT Knowledge', a sequence flow out of it into an end event (plain circle). The page belongs to the docs' 'BPMN 2.0 Reference / BPMN Modules' section and the box is drawn as a process module of the kind LoyJoy's BPMN process editor renders; no .bpmn XML is published and the page has no bpmn-js canvas"
bpmn_evidence_quote: "This module is not deprecated, however limited to answering customer questions based on a static knowledge database"
ai_evidence: "the only element between the start and the end event is the module box '#2 GPT Knowledge' - an AI (GPT) module occupying the process step itself; the page describes it as implementing retrieval-augmented generation over a knowledge database"
ai_evidence_quote: "This implements the classical Retrieval Augmented Generation (RAG) approach."
artefacts:
  screenshot: corpus/loyjoy/003_ai-knowledge-gpt-flow.png
  archive: ledgers/loyjoy.raw/html/014.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: marginal
capture_width_px: 338
capture_method: chrome-devtools-mcp, in-page fetch() of the figure asset https://docs.loyjoy.com/assets/images/flow-*.png (338 x 390 native - this is the largest version published); saved via base64 to corpus/loyjoy/003_ai-knowledge-gpt-flow.png. Page HTML archived with curl to ledgers/loyjoy.raw/html/014.html
---

## What the page shows

`/bpmn/subprocesses/ai_knowledge/` is the reference page for the (still supported) GPT
knowledge module. It is 19,195 characters of body text and carries **one** figure, a small
diagram reproduced as `003_ai-knowledge-gpt-flow.png` (338 x 390 native).

**The AI-in-BPMN artefact, element by element** (read off the capture, which is legible at
native size despite being small):

- a **message start event** (envelope in a circle, with the editor's "+" affordance);
- a single module box **"#2 GPT Knowledge"**, into which the start event flows;
- a sequence flow out of it into an **end event** (plain circle).

Three elements, one of them an AI module: the process step itself *is* the GPT knowledge
call. The figure has no editor chrome (no toolbar, no properties panel), which is why it
reads as a bare process fragment rather than an editor screenshot — but the "+" affordance
is the LoyJoy editor's, and the module numbering ("#2") matches the editor's module labels.

**Page prose on the AI element**, verbatim: "This module is not deprecated, however limited
to answering customer questions based on a static knowledge database, which is queried once
per question. This implements the classical Retrieval Augmented Generation (RAG) approach."
The page then directs new use cases to the AI Agent module, "which is more powerful due to
its ability to call the knowledge database multiple times per question, and to call
additional tools such as web search, product search, and more."

## Observations (description only, no interpretation)

- **AI activity - function:** answer customer questions from a static knowledge database,
  queried once per question (RAG).
- **AI activity - element type:** one module box ("GPT Knowledge") occupying the process step
  between the start and end events.
- **Authority - downstream:** the module's answer is the output; no downstream tool or system
  is drawn.
- **Authority - data:** a knowledge database is named in prose and shown as the module's
  subject; the database itself is not drawn or linked on the page.
- **Authority - control:** none drawn — no gateway, no human review between question and
  answer.
- **Input provenance:** the message start event, i.e. a user message.
- **Guards present:** none in the figure; the page notes the module cannot resolve follow-up
  questions (that is what the separate AI Followup module is for).
- **Prompt / model detail visible:** none on the page; no model name, no prompt text.

## Notes for the researcher

- Capture is the native asset (338 x 390) — the docs publish no larger version of this
  figure, so it is recorded as `marginal`; the three element labels are nonetheless readable
  at native size, which is why the file is the record's `screenshot`.
- The page's own cross-reference to the AI Followup module (`ai_knowledge_followup`, which
  carries **no** figure) is the reason that page is a separate ledger row rather than a
  duplicate of this one.
- Raw evidence for this source lives in `ledgers/loyjoy.raw/`; the per-page image inventory
  and the six classifier reports are `ledgers/_lj_table.json` and
  `ledgers/loyjoy.raw/_cls_*.txt`.
