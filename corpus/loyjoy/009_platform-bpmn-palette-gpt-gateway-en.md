---
n: 276
source: loyjoy
source_name: LoyJoy (marketing site, product pages)
source_type: vendor marketing page
title: BPMN 2.0 Process Automation (English)
url: https://www.loyjoy.com/en/platform/bpmn/
accessed: 2026-09-24
verdict: UNCERTAIN
needs_visual_check: false
needs_human_ruling: true
question: "Same question as the German twin (/de/platform/bpmn/, corpus/loyjoy/008_...): the editor screenshot's 'Modules' palette lists 'GPT gateway' while the process drawn on the canvas contains no AI module. Is a GPT module visible in the editor palette, but not placed in the depicted process, an AI element inside the artefact, or does the artefact contain no AI element (E2-no-ai-element)?"
bpmn_evidence: "a marketing screenshot of the LoyJoy process editor: the 'Modules' palette with the sections 'control flow' (Loop, Gateway, Decision gateway, 'GPT gateway'), 'events' and 'essential', and on the canvas a process in the editor's notation - start event, module boxes ('#1 ...', '#2 Decision gateway', '#3 Simple message', '#4 Product gallery'), exclusive gateways, end event - with the English annotations 'No-code approach through BPMN 2.0 modelling.', 'Continuous development of the BPMN process modules.' and 'Simply remove or add modules using drag & drop.'"
bpmn_evidence_quote: "LoyJoy is based on the BPMN 2.0 modeling standard"
ai_evidence: "the palette tile 'GPT gateway' (diamond icon carrying the GPT swirl) is the only AI-marked content of the screenshot; the canvas shows no AI module. The page's prose AI claim is about the platform: 'LoyJoy seamlessly connects BPMN 2.0 process automation with agentic AI.' - which the figure does not depict"
ai_evidence_quote: "LoyJoy seamlessly connects BPMN 2.0 process automation with agentic AI."
artefacts:
  screenshot: corpus/loyjoy/009_platform-bpmn-palette-gpt-gateway-en.png
  archive: ledgers/loyjoy.marketing/737.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1024
capture_method: curl of the page's figure asset https://www.loyjoy.com/_astro/bpmn_en.CttUSZB9_ZpLfDt.webp (1024 x 600 native), converted to PNG with PIL; palette region re-examined at 4x zoom (ledgers/loyjoy.raw/mont3/pal2.jpg, where 'GPT gateway' is legible). Page HTML archived to ledgers/loyjoy.marketing/737.html
---

## What the page shows

The English twin of `/de/platform/bpmn/`. Its figure is the same editor screenshot in an English
annotated render: palette section "control flow" with Loop, Gateway, Decision gateway and
**"GPT gateway"**, the canvas with a process that contains no AI module, and three English
annotations pointing at BPMN 2.0 modelling and the module palette.

**Verified at 4x zoom** (`ledgers/loyjoy.raw/mont3/pal2.jpg`): the tile reads "GPT gateway" beneath
the section label "control flow", with the GPT swirl icon on the diamond - so the module name is
not an inference from the file name or the URL.

**Why UNCERTAIN:** identical to `corpus/loyjoy/008_platform-bpmn-palette-gpt-gateway-de.md` - the
GPT element is in the palette, not in the drawn process.

## Observations (description only, no interpretation)

- **AI activity - function:** if counted, an AI gateway module offered by the editor palette.
- **AI activity - element type:** a palette tile ("GPT gateway"); nothing placed on the canvas.
- **Authority - downstream / data / control:** not visible in the figure; the page prose names
  knowledge-based advice and process permissions.
- **Input provenance:** not visible.
- **Guards present:** none.
- **Prompt / model detail visible:** none.

## Notes for the researcher

- The `bpmn_en` and `bpmn_de` files are different renders (different content hashes) of the same
  editor state, so both rows exist; if the researcher rules the palette entry irrelevant, both fall
  together.
- The English platform landing page (`/en/platform/`) is a separate row (`E3-duplicate` of the
  German landing page, identical canvas assets) and is unaffected by this question.
