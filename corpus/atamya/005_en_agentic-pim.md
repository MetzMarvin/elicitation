---
n: 246
source: atamya
source_name: Atamya (www.atamya.com - Agentic PIM with an embedded bpmn.io / Flowable BPMN engine)
source_type: vendor product page
title: Agentic PIM (overview page)
url: https://www.atamya.com/en/agentic-pim/
accessed: 2026-09-24
verdict: UNCERTAIN
needs_human_ruling: true
question: "Two of the page's five feature figures are stylised BPMN-derived renders - yellow task rectangles, an exclusive-gateway diamond, sequence-flow arrows - that carry explicit AI work ('Generate Description', 'Translate with: DeepL') but are not drawn as a real BPMN model and carry no events. Is a stylised render that keeps the BPMN element semantics an artefact for this corpus?"
needs_visual_check: false
bpmn_evidence: "image: 'website-agentic-pim-graphic-content-creation-en.png' and '...-graphic-multilingual-en.png' - yellow task rectangles joined by sequence-flow arrows with an exclusive-gateway diamond between them"
bpmn_evidence_quote: "The management is carried out via a BPMN-based workflow engine."
ai_evidence: "the task labels inside the figures ('Generate Description', 'Translate German', 'Translate with: DeepL')"
ai_evidence_quote: "The management is carried out via a BPMN-based workflow engine."
artefacts:
  screenshot: 005_1_website-agentic-pim-graphic-content-creation-en.png
  assets: [005_2_website-agentic-pim-graphic-multilingual-en.png]
  archive: 005_en_agentic-pim.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: poor
capture_width_px: 640
capture_method: curl of the vendor's own wp-content/uploads asset at its native URL
---
## What the page shows

The overview page stacks five AI-feature figures. Two of them are process-shaped:
`...-graphic-content-creation-en.png` (Generate Description -> Save Description -> and then
an exclusive-gateway diamond with three outgoing branches: Derive Keywords, Create Short
Description, Create Informal Description; a UI screenshot of the feature sits below) and
`...-graphic-multilingual-en.png` (Generate Description -> exclusive-gateway diamond ->
Translate German -> Proofread German in one branch and Translate French -> Proofread French
in the other; a UI card shows the language pair and the picker "Translate with: DeepL /
Other AI"). The page also carries the AI-feature list figure, the smart-import UI figure,
the data-quality figure and an LLM architecture figure.

## Observations (description only, no interpretation)

- **AI activity - function:** description generation and translation/proofreading, both
  named in the figures themselves.
- **AI activity - element type:** not drawn - the figures use task rectangles and one
  gateway diamond, but there are no BPMN events and the render drops the element markers the
  site's real models carry; the UI card names the binding ("Translate with: DeepL").
- **Authority - downstream:** not visible.
- **Authority - data:** the UI card below the multilingual figure shows the attribute
  ("Beschreibung") and the language pair.
- **Authority - control:** the content-creation figure's gateway splits one generated
  description into three derived outputs - the only control element drawn.
- **Input provenance:** a task labelled "Generate Description" precedes the gateway, so the
  branch consumes generated content.
- **Guards present:** not visible.
- **Prompt / model detail visible:** no prompt; the model choice is named as a picker
  ("DeepL / Other AI").

## Notes for the researcher

- This is the Q1 question of this source: the notation is BPMN-derived but redrawn for
  marketing, and the page's own claim ("The management is carried out via a BPMN-based
  workflow engine") is about the engine, not about the picture. The German twin
  (`de/agentic-pim/`, record 006) is a different set of files.
- Capture: vendor assets, native 640 x 437 - well under the 1400 px bar,
  `capture_quality: poor`.
