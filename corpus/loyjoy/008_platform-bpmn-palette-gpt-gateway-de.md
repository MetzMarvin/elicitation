---
n: 275
source: loyjoy
source_name: LoyJoy (marketing site, product pages)
source_type: vendor marketing page
title: BPMN 2.0 Prozessautomatisierung (German)
url: https://www.loyjoy.com/de/platform/bpmn/
accessed: 2026-09-24
verdict: UNCERTAIN
needs_visual_check: false
needs_human_ruling: true
question: "The page's figure is a screenshot of the LoyJoy BPMN editor: the canvas shows a process (start event, module boxes, exclusive gateways, end event) and the 'Modules' palette beside it lists the section 'control flow' with Loop, Gateway, Decision gateway and 'GPT gateway' (the last carrying the OpenAI-style swirl icon). No GPT module is placed inside the process drawn on the canvas. Is a GPT module that is visible in the editor's palette (i.e. available, AI-bound, and part of the artefact) an AI element inside the artefact, or does the artefact contain no AI element (E2-no-ai-element)? The same question applies to the English twin."
bpmn_evidence: "a marketing screenshot of the LoyJoy process editor: title bar 'LoyJoy / My Experience', the 'Modules' palette on the left with the section headings 'control flow' (Loop, Gateway, Decision gateway, 'GPT gateway'), 'events' (End, Wait, Message start, Timer start) and 'essential' (Add variables, Appointment scheduler, Automatic jump, Clipboard, Conversion, Create PDF, Decision jump, Email, External link, Goodbye), and on the canvas a process drawn in the editor's notation: start event, module boxes ('#1 ...', '#2 Decision gateway', '#3 Simple message', '#4 Product gallery'), exclusive gateways and an end event, with German annotations ('No-Code Ansatz durch BPMN 2.0 Modellierung.') drawn over it"
bpmn_evidence_quote: "LoyJoy basiert auf dem Modellierungsstandard BPMN 2.0"
ai_evidence: "the palette entry 'GPT gateway' with the GPT swirl icon is part of the depicted editor; the German annotation 'Kontinuierliche Weiterentwicklung der BPMN-Prozessmodule.' points at the palette. No GPT/AI module is placed in the process drawn on the canvas, and the page prose about AI is about the platform, not about the depicted model"
ai_evidence_quote: "BPMN 2.0 Prozessautomatisierung nahtlos mit agentischer KI"
artefacts:
  screenshot: corpus/loyjoy/008_platform-bpmn-palette-gpt-gateway-de.png
  archive: ledgers/loyjoy.marketing/317.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1024
capture_method: curl of the page's figure asset https://www.loyjoy.com/_astro/bpmn_de.CZTki966_Z1xvGuj.webp (1024 x 600 native), converted to PNG with PIL; the palette region was additionally re-examined at 4x zoom (ledgers/loyjoy.raw/mont3/pal.jpg, pal2.jpg). Page HTML archived to ledgers/loyjoy.marketing/317.html
---

## What the page shows

`/de/platform/bpmn/` is LoyJoy's German BPMN marketing page. Its single figure is a **screenshot of
the LoyJoy process editor** with the "Modules" palette open beside the canvas.

**What the capture shows** (read off the figure; palette labels verified at 4x zoom):

- the editor shell: title "LoyJoy", breadcrumb "My Experience", the Process/Branding/Language/
  Publish/Texts/Assets tabs;
- the **Modules palette**, section by section: **control flow** - Loop, Gateway, Decision gateway,
  **"GPT gateway"** (with the GPT swirl icon); **events** - End, Wait, Message start, Timer start;
  **essential** - Add variables, Appointment scheduler, Automatic jump, Clipboard, Conversion,
  Create PDF, Decision jump, Email, External link, Goodbye;
- the **canvas**: start event, module boxes ("#1 ...", "#2 Decision gateway", "#3 Simple message",
  "#4 Product gallery"), exclusive gateways, end event;
- German marketing annotations over the screenshot: "No-Code Ansatz durch BPMN 2.0 Modellierung.",
  "Kontinuierliche Weiterentwicklung der BPMN-Prozessmodule.", "Module einfach per Drag & Drop
  entfernen oder hinzufügen."

**Why UNCERTAIN.** The GPT element is on screen (a palette entry, and the palette is how the editor
offers AI modules), but the process that is *drawn* contains no AI module. A reader could argue
either way, and rule 3 forbids E2 for ambiguous cases.

## Observations (description only, no interpretation)

- **AI activity - function:** if the palette entry is counted, an AI gateway module available for
  insertion into the process.
- **AI activity - element type:** a palette tile labelled "GPT gateway" (diamond icon with the GPT
  swirl); nothing placed on the canvas.
- **Authority - downstream:** not visible.
- **Authority - data:** not visible.
- **Authority - control:** the canvas's exclusive gateways are the drawn control structure.
- **Input provenance:** not visible.
- **Guards present:** none.
- **Prompt / model detail visible:** none.

## Notes for the researcher

- The German and English pages do **not** share the figure file (`bpmn_de` vs `bpmn_en`, different
  hashes), so both are recorded - they are similar-but-different artefacts, not duplicates. The
  editor UI inside both is English; only the marketing annotations differ.
- The palette region is the only place a GPT module is visible; the earlier 4x zoom is archived at
  `ledgers/loyjoy.raw/mont3/pal2.jpg` so the researcher can re-check the label.
