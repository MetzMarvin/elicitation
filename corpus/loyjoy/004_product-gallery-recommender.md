---
n: 102
source: loyjoy
source_name: LoyJoy (technical documentation, BPMN 2.0 reference)
source_type: vendor documentation
title: Products Module (Product gallery) - "Using the Recommender"
url: https://docs.loyjoy.com/bpmn/subprocesses/products/
accessed: 2026-09-24
verdict: UNCERTAIN
needs_visual_check: false
needs_human_ruling: true
question: "The Product gallery module's settings panel inside the editor canvas offers a 'Recommender' feature with the three options Off / Filter / Smart, and the same page documents Smart as deterministic tag matching ('products are sorted based on the number of matching tags'). LoyJoy separately publishes a deprecated 'AI Recommender' module whose page says it 'takes a user message and generates an appropriate product recommendation ... using SQL queries'. Is the Product gallery 'Recommender' the AI Recommender (i.e. an AI element inside the depicted process, so this row is an artefact), or the deterministic tag filter described on this page (so this row is E2-no-ai-element)? The word 'Recommender' is a visible label of a process element, so I could not resolve it without an ambiguity call."
bpmn_evidence: "a LoyJoy process-editor screenshot: start event -> module box '#1 Decision gateway' -> exclusive gateway with sequence flows labelled 'Red' and 'Blue' -> two module boxes '#2 Tag' and '#3 Tag' -> a second gateway -> module box '#4 Product gallery' (drawn selected) -> end event. The right-hand properties panel is the Product gallery module's settings ('Select image orientation': Landscape / Portrait / Square; product rows 'red' and 'blue'; 'Add product'). Figure asset 'Recommender_2.gif' (672 x 398 native, animated; frame 0 captured)"
bpmn_evidence_quote: "When creating your chatflow, add relevant tags to it using the Tag Module."
ai_evidence: "the settings panel inside the process editor is headed 'Recommender' and contains the mode buttons Off / Filter / Smart (Off selected, with the caption 'Display all available products' beneath it); the page prose calls it 'a powerful tool that helps you provide the most relevant products to your customers'. Whether that feature is AI-backed is not stated on this page - see the question above; LoyJoy's own AI-module page lists a deprecated 'AI Recommender' module among the modules the AI Agent replaces"
ai_evidence_quote: "The recommender feature is a powerful tool that helps you provide the most relevant products to your customers."
artefacts:
  screenshot: corpus/loyjoy/004_product-gallery-recommender.png
  archive: ledgers/loyjoy.raw/html/102.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 672
capture_method: chrome-devtools-mcp, in-page fetch() of the figure asset https://docs.loyjoy.com/assets/images/Recommender_2-*.gif (672 x 398 native, animated GIF); frame 0 decoded with PIL and saved as corpus/loyjoy/004_product-gallery-recommender.png. Page HTML archived with curl to ledgers/loyjoy.raw/html/102.html
---

## What the page shows

`/bpmn/subprocesses/products/` is the reference page for the Product gallery module (4,301
characters of body text; 10 images, of which the animated `Recommender_1.gif` and
`Recommender_2.gif` show the editor). The captured frame is `Recommender_2.gif` frame 0.

**The artefact, element by element** (read off the capture):

- start event (circle) -> module box **"#1 Decision gateway"**;
- an **exclusive gateway** (X diamond) whose outgoing flows are labelled **"Red"** and
  **"Blue"**;
- two module boxes **"#2 Tag"** and **"#3 Tag"** on those branches;
- a second gateway and a module box **"#4 Product gallery"**, drawn selected (blue outline);
- an end event (circle);
- the properties panel for "#4 Product gallery": "Select image orientation" (Landscape
  1200x630, Portrait 1080x1920, Square 1080x1080), product rows `red` / `blue` with
  "Add product", then a section headed **"Recommender"** containing the mode buttons
  **Off** (selected) / **Filter** / **Smart**, the caption "Display all available products"
  and "Max. number of products to display" = 12.

**The ambiguity, stated plainly.** The panel heading "Recommender" is a label of a process
element (a setting of the "#4 Product gallery" module that sits inside the drawn process),
so if it names an AI capability it is an AI element *inside* the process. But this page
documents the feature deterministically: "3. Smart With the 'Smart' option, products are
sorted based on the number of matching tags. Products with more matching tags are displayed
first, offering a personalized shopping agent." No AI/LLM/GPT wording appears anywhere on
the page or in its images. At the same time LoyJoy publishes a *deprecated* module
`/bpmn/subprocesses/ai_recommender/`: "This module takes a user message and generates an
appropriate product recommendation based on it. To make this recommendation, it searches the
product database using SQL queries."

Per the shared rules (an ambiguous AI mention resolves to `UNCERTAIN`, never to
`E2-no-ai-element`), this row is recorded as `UNCERTAIN` with a record and capture.

## Observations (description only, no interpretation)

- **AI activity - function:** if the "Recommender" is the AI Recommender, the function is
  generating a product recommendation from a user message by generating SQL; if it is the
  tag recommender, the function is deterministic tag matching and ordering.
- **AI activity - element type:** a settings section of the "#4 Product gallery" module
  inside the canvas; no separate AI element is drawn.
- **Authority - downstream:** the module displays products to the end user; the panel exposes
  "Max. number of products to display" (12).
- **Authority - data:** the product database and the tags assigned in the "#2/#3 Tag" modules;
  the panel has no model or knowledge-source field.
- **Authority - control:** the "#1 Decision gateway" and the two Tag branches are the control
  structure; the ranking itself is a module setting, not a gateway.
- **Input provenance:** tags set earlier in the chatflow (page prose), products from the
  product database.
- **Guards present:** none drawn.
- **Prompt / model detail visible:** none - no model name, no prompt field, on the page or in
  any of its 10 images.

## Notes for the researcher

- The capture is frame 0 of an animated GIF; later frames walk through the same panel, which
  is why the still frame is the useful evidence. Native width 672 px, labels legible.
- Two further images on the same page (`Recommender_1.gif`, `products__intro.gif`) show the
  same canvas and the module palette; they carry no additional AI label.
- Related rows in this source: `/bpmn/subprocesses/ai_recommender/` (deprecated AI Recommender
  module, no figure at all -> E0), `/bpmn/subprocesses/product_feed_tag_recommender/` (Tag
  recommender guide, canvas with Tag modules, no AI label -> E2), `/bpmn/subprocesses/tag/`
  (Tag module, canvas, prose about "product recommendations" -> E2).
