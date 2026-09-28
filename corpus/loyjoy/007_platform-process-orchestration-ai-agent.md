---
n: 273
source: loyjoy
source_name: LoyJoy (marketing site, product pages)
source_type: vendor marketing page
title: LoyJoy Platform (German landing page)
url: https://www.loyjoy.com/de/platform/
accessed: 2026-09-24
verdict: INCLUDE
needs_visual_check: false
needs_human_ruling: false
bpmn_evidence: "a marketing figure of a process in the LoyJoy editor's notation: a start event (circle with a globe icon on a white card) -> module box '#1 AI Agent' (green '1' annotation badge) -> exclusive gateway (diamond with X) whose outgoing flows are labelled 'Branch 1', 'Branch 2', 'Branch 3' -> module boxes '#2 GPT Knowledge', '#3 GPT follow-up question', '#4 GPT Smalltalk' -> module box '#4 Automatic jump' -> end event (plain circle). The same page's second canvas figure ('no-code-bpmn') shows start event -> module '#1 Welcoming' -> the editor cursor dragging module '#2 AI Agent' into the flow -> exclusive gateway"
bpmn_evidence_quote: "Eine no-code BPMN-Engine modelliert Dialoge und Prozesse mit Regeln, Routing, Experimenten und Analytics."
ai_evidence: "the module boxes '#1 AI Agent', '#2 GPT Knowledge', '#3 GPT follow-up question' and '#4 GPT Smalltalk' are steps inside the drawn process, and the second figure shows '#2 AI Agent' being placed into the flow; the page prose describes exactly that: the business team builds AI Agents visually"
ai_evidence_quote: "Ihre Fachabteilung baut AI Agents visuell oder im Dialog mit ihrem KI-Assistenten."
artefacts:
  screenshot: corpus/loyjoy/007_platform-process-orchestration-ai-agent.png
  archive: ledgers/loyjoy.marketing/314.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1167
capture_method: curl of the page's figure asset https://www.loyjoy.com/_astro/process-orchestration.CgbVPyh5_aqxij.webp (1167 x 976 native), converted to PNG with PIL; the page's other canvas asset no-code-bpmn.Be3QCK8a_9QMdK.webp is archived beside it in ledgers/loyjoy.raw/mkt_imgs/. Page HTML archived to ledgers/loyjoy.marketing/314.html
---

## What the page shows

The German platform landing page carries 33 figure assets, of which two are process canvases. The
captured one (`process-orchestration`) is the clearest AI-in-process artefact on the marketing host.

**The AI-in-BPMN artefact, element by element** (read off the capture):

- a **start event** (circle with a globe glyph) at the top;
- module box **"#1 AI Agent"** with a green "1" badge, directly after the start event;
- an **exclusive gateway** (X diamond) with three outgoing flows labelled **"Branch 1"**,
  **"Branch 2"**, **"Branch 3"**;
- the branches feed **"#2 GPT Knowledge"**, **"#3 GPT follow-up question"** and
  **"#4 GPT Smalltalk"**;
- a module box **"#4 Automatic jump"** and an **end event** below;
- the figure is composited over a photograph of a person at a laptop (marketing hero treatment).

The second canvas figure on the same page (`no-code-bpmn`) shows **"#1 Welcoming"** with the editor
cursor dragging **"#2 AI Agent"** into the flow, ending in an exclusive gateway.

## Observations (description only, no interpretation)

- **AI activity - function:** the AI Agent handles the request; the three gateway branches route to
  knowledge lookup, a follow-up question or smalltalk - the same pattern the docs' `/guides/central_ai/`
  page documents (`corpus/loyjoy/005_central-ai-gpt-branching-process.md`).
- **AI activity - element type:** module boxes inside the process ("AI Agent", "GPT Knowledge",
  "GPT follow-up question", "GPT Smalltalk"), one of them the first step after the start event.
- **Authority - downstream:** an automatic jump and the end event; the marketing page's other figures
  advertise the surrounding platform (knowledge, integrations, live-chat handover).
- **Authority - data:** the page names the knowledge layer ("ai-agent-knowledge" figure card) and the
  model choice (a chat LLM on LoyJoy hardware, Enterprise choice of GPT/Claude/own LLM).
- **Authority - control:** the exclusive gateway with the three named branches.
- **Input provenance:** the start event (a customer message).
- **Guards present:** none drawn.
- **Prompt / model detail visible:** the page's AI-model figure (`ai_model_de`) shows a settings
  dropdown, not the process.

## Notes for the researcher

- **Outside the docs host.** This row comes from the documented secondary sweep of the marketing site
  (see the ledger header note); it is not part of the `/bpmn/` census.
- The English twin `/en/platform/` publishes the *same two canvas files* (identical content hashes)
  and is recorded as `E3-duplicate` in the ledger.
- 33 page assets were inspected by contact sheet and zooms; the remaining AI-named cards
  (`ai-agent`, `agentic-ai`, `ai-quality-check`, `ai-testing-automation`, `smart-product-advisor`)
  are UI/illustration cards, not process diagrams - except `process-orchestration` and `no-code-bpmn`.
