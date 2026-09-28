---
n: 233
source: loyjoy
source_name: LoyJoy (technical documentation, BPMN 2.0 reference)
source_type: vendor documentation
title: Build an Agent / How to Build an AI Agent
url: https://docs.loyjoy.com/guides/building/
accessed: 2026-09-24
verdict: UNCERTAIN
needs_visual_check: false
needs_human_ruling: true
question: "The guide's message-configuration figure (alt and title 'AI helps') shows the properties panel of a message module inside the process editor; its toolbar carries a GPT-style swirl icon (circled in the figure) beside the link, smiley and variable icons. The figure demonstrates an AI text-assist affordance attached to a process module, but no AI module is drawn as a step of the process itself, and the surrounding prose does not name that control. Is an AI text-assist control on a module's properties panel an AI/LLM element inside the process (so this row is an artefact), or only an editor convenience outside the process model (so this row is E2-no-ai-element)? The other figures on the page (editor canvases with '#1 Email'/'#2 Snapshot', the Process-bricks palette, new-experience menus) carry no AI label at all."
bpmn_evidence: "a crop of the LoyJoy process editor's message-module properties panel: the heading 'Welcoming recurrent customers' with a clock icon, the text field 'Glad you're back' (highlighted), the language label 'en', and the panel toolbar with a circled pencil icon, a GPT-style swirl icon, a link icon, a smiley icon and a '$' variable icon; beside it the image-upload box reading '1200 x 630 px / 500 KB'. The page's other figures are editor canvases: start event -> module '#1 Email' -> module '#2 Snapshot' -> end event, a '#1 Questionnaire' single-module canvas, and the 'Modules' palette with its 'control flow'/'events'/'essential' sections"
bpmn_evidence_quote: "Add bricks to editor"
ai_evidence: "the figure's own alt and title text is 'AI helps' and it points at the GPT-style swirl icon in the message panel's toolbar; the page is titled 'How to Build an AI Agent'. The AI element is therefore an editor affordance attached to a message module, not a module placed in the drawn process: no GPT/AI module appears in any of the page's canvases"
ai_evidence_quote: "AI helps"
artefacts:
  screenshot: corpus/loyjoy/006_building-guide-ai-helps-message-panel.png
  archive: ledgers/loyjoy.raw/html_rest/083.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1038
capture_method: curl of the page's figure asset https://docs.loyjoy.com/assets/images/gpt-*.png (1038 x 276 native, alt/title "AI helps"), archived in ledgers/loyjoy.raw/rest_imgs/083_13__gpt-*.png and copied to corpus/loyjoy/. Page HTML archived to ledgers/loyjoy.raw/html_rest/083.html
---

## What the page shows

`/guides/building/` is the 20-figure builder guide for LoyJoy agents (h1 "How to Build an AI
Agent"). It contains editor canvases, palette figures, menus - and one figure whose alt/title is
literally **"AI helps"**, reproduced here.

**What the captured figure shows:** the properties panel of a **message module** inside the process
editor - heading "Welcoming recurrent customers" with a clock icon, the message text field
("Glad you're back", highlighted), the language chip "en", and the panel's toolbar: a circled
pencil icon, a **GPT-style swirl icon**, a link icon, a smiley icon and a "$" variable icon. Beside
the panel sits the image-upload box ("1200 x 630 px / 500 KB").

**Why this row is UNCERTAIN rather than E2.** The AI affordance is *visible* (a GPT-marked control
in a module's panel) and the figure is *titled* "AI helps", but it is not an AI element drawn as a
step of the process: the page's canvases ("#1 Email" -> "#2 Snapshot", "#1 Questionnaire",
"Process bricks") contain no GPT/AI module. Whether a text-assist control on a module panel counts
as an AI element *inside the process* is a judgement call, and rule 3 forbids E2 for ambiguous
cases, so the row is recorded with a record and a question.

## Observations (description only, no interpretation)

- **AI activity - function:** if counted, generating or rewriting the module's message text from the
  text field ("Glad you're back").
- **AI activity - element type:** a toolbar control of the message module's properties panel; no
  module box and no event.
- **Authority - downstream:** the message text reaches the end user.
- **Authority - data:** not visible.
- **Authority - control:** the panel is a property of a module that sits in the process; the process
  structure itself (gateways, branches) is unaffected.
- **Input provenance:** the text typed in the module's message field.
- **Guards present:** none.
- **Prompt / model detail visible:** none - no model name, no prompt field.

## Notes for the researcher

- The figure is a native 1038 x 276 crop; the labels are legible at that size.
- The page's canvases were inspected one by one (21 raster assets under
  `ledgers/loyjoy.raw/rest_imgs/083_*`): none contains an AI-named module; the only AI-marked pixel
  content on the page is this message-panel control.
