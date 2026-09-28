---
n: 277
source: atamya
source_name: Atamya (www.atamya.com - Agentic PIM with an embedded bpmn.io / Flowable BPMN engine)
source_type: vendor product page
title: Agentic PIM (German overview page)
url: https://www.atamya.com/de/agentic-pim/
accessed: 2026-09-24
verdict: UNCERTAIN
needs_human_ruling: true
question: "Same question as record 005, on the German twin page: its content-creation and multilingual figures are stylised BPMN-derived renders (task rectangles, an exclusive-gateway diamond, sequence flows) with explicit AI work in the labels. Are they artefacts, given that they keep BPMN element semantics but are not BPMN drawings?"
needs_visual_check: false
bpmn_evidence: "image: 'website-agentic-pim-graphic-content-creation.png' and '...-graphic-multilingual.png' - yellow task rectangles, a gateway diamond, sequence-flow arrows"
bpmn_evidence_quote: "Die Steuerung erfolgt über eine BPMN-basierte Workflow-Engine."
ai_evidence: "the task labels inside the figures ('Beschreibung generieren', 'Uebersetzen', 'DeepL')"
ai_evidence_quote: "Die Steuerung erfolgt über eine BPMN-basierte Workflow-Engine."
artefacts:
  screenshot: 006_1_website-agentic-pim-graphic-content-creation.png
  assets: [006_2_website-agentic-pim-graphic-multilingual.png]
  archive: 006_de_agentic-pim.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: poor
capture_width_px: 640
capture_method: curl of the vendor's own wp-content/uploads asset at its native URL
---
## What the page shows

The German overview page carries the same five AI-feature figures as its English twin, in
German renders: content creation (description generation feeding an exclusive-gateway
diamond with three derived outputs), multilingual (translation into two languages with a
proofreading step each, and a picker naming DeepL), smart import, data quality and the LLM
architecture figure.

## Observations (description only, no interpretation)

- **AI activity - function:** content generation, translation and proofreading.
- **AI activity - element type:** not drawn; the figures carry no BPMN events and no element
  markers, only the gateway diamond that the site's stylised renders keep.
- **Authority - downstream / data / control:** the only control element is the gateway that
  fans one generated description out to three derived texts.
- **Input provenance:** generation precedes the gateway.
- **Guards present:** not visible.
- **Prompt / model detail visible:** a picker names the translation binding ("DeepL"); no
  prompt is shown.

## Notes for the researcher

- Paired with record 005: same content, different files, so neither page can be an E3
  duplicate of the other; both are the Q1 question of this source.
- Capture: vendor assets, native 640 x 437 - well under the 1400 px bar,
  `capture_quality: poor`.
