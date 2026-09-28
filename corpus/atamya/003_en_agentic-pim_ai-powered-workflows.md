---
n: 242
source: atamya
source_name: Atamya (www.atamya.com - Agentic PIM with an embedded bpmn.io / Flowable BPMN engine)
source_type: vendor product page
title: AI-Powered Workflows (agentic PIM)
url: https://www.atamya.com/en/agentic-pim/ai-powered-workflows/
accessed: 2026-09-24
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "page claim plus five figures, one of which draws a five-step chain of AI tasks between event circles ('Generate Content', 'Extract Attributes', 'Enrich Content', 'Translate Content', 'AI Decisions')"
bpmn_evidence_quote: "It's a BPMN service task - just like 'Active Object,' 'Edit Attribute Value,' or 'Synch with Shopware.' It has inputs, outputs, as well as conditions before and after."
ai_evidence: "page text binding AI to the process: 'In ATAMYA, however, it operates directly from within the process itself - as a native service task, orchestrated by a full-fledged BPMN engine.'"
ai_evidence_quote: "In ATAMYA, however, it operates directly from within the process itself - as a native service task, orchestrated by a full-fledged BPMN engine."
artefacts:
  screenshot: 003_1_website-agentic-pim-diagram-workflow-AI-tasks-en.png
  assets: [003_2_website-agentic-pim-diagram-workflow-hero-en.png]
  archive: 003_en_agentic-pim_ai-powered-workflows.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: poor
capture_width_px: 1281
capture_method: curl of the vendor's own wp-content/uploads asset at its native URL
---
## What the page shows

The page is a product page for AI in the process and shows five figures:
`website-agentic-pim-diagram-workflow-hero-en.png` (a stylised BPMN render with gateway
diamonds and icon tasks), `...-workflow-AI-tasks-en.png` (five yellow icon tasks -
Generate Content, Extract Attributes, Enrich Content, Translate Content, AI Decisions -
strung between a start and an end circle, each with a one-line description),
`...-diagram-AI-based-decisions-en.png`, `...-diagram-expression-language-en.png` (the
prompt editor: chips Attribute / Variable / Logic / Context, the prompt
"Create the product description with:" and the tokens {Product Name} {Brand Tone}
{LengthxWidthxHeight} {Language}, with the caption "AI Service Task - Prompt meets live
data from your PIM") and `...-diagram-human-in-the-loop-en.png`.

## Observations (description only, no interpretation)

- **AI activity - function:** generation (content), extraction (attributes), enrichment,
  translation and decisions - the five functions named on the AI-tasks figure.
- **AI activity - element type:** the page states the element type explicitly and
  repeatedly: "An AI service task in ATAMYA functions differently. It's a BPMN service
  task - just like 'Active Object,' 'Edit Attribute Value,' or 'Synch with Shopware.' It
  has inputs, outputs, as well as conditions before and after."
- **Authority - downstream:** "As soon as a new product is created, a first AI task
  generates the product description" - the AI runs downstream of a data event.
- **Authority - data:** inputs and outputs are declared on the element ("It has inputs,
  outputs"); the expression-language figure shows the prompt tokens filled from PIM data.
- **Authority - control:** "conditions before and after" (quoted above); the
  human-in-the-loop figure is the page's own answer to control.
- **Input provenance:** PIM attributes, bound into the prompt as tokens
  ({Product Name}, {Brand Tone}, {Language}).
- **Guards present:** the page advertises provider fallbacks ("Retries, Timeouts,
  Fallback-Pfade greifen automatisch" on the German twin of the page) and "human-in-the-loop".
- **Prompt / model detail visible:** yes - the expression-language figure shows the prompt
  skeleton and the bound attributes; the page also states translation can be bound to DeepL
  ("Dedicated translation tasks, optionally with DeepL for maximum quality").

## Notes for the researcher

- The English page has its own German twin (`de/agentic-pim/ai-powered-workflows/`), which
  carries the same claims with German figures and its own record (008) - the two figure
  sets are different files, so neither page is an E3 duplicate of the other.
- Capture: vendor assets, 1281 x 875 (the AI-tasks chain) - under the 1400 px bar,
  `capture_quality: poor` by rule; all labels legible.
