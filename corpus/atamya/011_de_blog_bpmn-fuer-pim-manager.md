---
n: 440
source: atamya
source_name: Atamya (www.atamya.com - Agentic PIM with an embedded bpmn.io / Flowable BPMN engine)
source_type: vendor blog
title: BPMN fuer PIM-Manager (blog article)
url: https://www.atamya.com/de/blog/bpmn-fuer-pim-manager/
accessed: 2026-09-24
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "a dark BPMN 2.0 model figure (start event, exclusive and parallel gateways, service and user tasks) plus the article's own element-by-element description of it: 'eine automatische Kategorisierung (Service Task), der Start der DeepL-Uebersetzung (Service Task), und ein Marketing-Review (User Task)'"
bpmn_evidence_quote: "eine automatische Kategorisierung (Service Task), der Start der DeepL-Übersetzung (Service Task), und ein Marketing-Review (User Task), das dem entsprechenden Team zugewiesen wird."
ai_evidence: "the article names the AI service tasks of the figure: automatic categorization and the start of the DeepL translation, both marked Service Task"
ai_evidence_quote: "eine automatische Kategorisierung (Service Task), der Start der DeepL-Übersetzung (Service Task), und ein Marketing-Review (User Task)"
artefacts:
  screenshot: 011_1_blog-graphic-der-20-minuten-workflow.png
  assets: [011_2_blog-graphic-fuenf-bpmn-symbole.png]
  archive: 011_de_blog_bpmn-fuer-pim-manager.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1804
capture_method: curl of the vendor's own wp-content/uploads asset at its native URL
---
## What the page shows

Two figures. `blog-graphic-der-20-minuten-workflow.png` (1804 x 537) is a dark-styled BPMN
2.0 model: start event, exclusive gateway (marked with X) splitting into a standard and a
non-standard path, "Manuelle Vorabpruefung und Pflege" (orange, person glyph), a parallel
gateway, "Automatische Kategorisierung" (marked with the AI glyph), "DeepL-Uebersetzung
starten" (marked with the AI glyph), "Marketing-Pflege und Review" (orange, person glyph),
a second parallel gateway, an exclusive gateway, then "Objekt aktivieren", "Datenblatt
erstellen" and "Zum Online Shop synchronisieren", and an end event. The second figure
`blog-graphic-fuenf-bpmn-symbole.png` is a legend of five BPMN symbols (event, activity,
gateway, sequence flow, pool).

## Observations (description only, no interpretation)

- **AI activity - function:** automatic categorization and the start of a DeepL translation.
- **AI activity - element type:** both are named *Service Task* by the article text quoted
  above; the figure marks them with the vendor's AI glyph.
- **Authority - downstream:** the AI tasks sit between a parallel split and a parallel join,
  i.e. they run in parallel with a manual branch; the article contrasts the manual and the
  automated path.
- **Authority - data:** not visible; the article's "Vorher/Nachher" table (6 weeks -> 2
  days, 23 manual steps -> 3 manual input points) is the page's own before/after claim.
- **Authority - control:** X and + gateways with labelled paths ("Standard",
  "Nicht-Standard", "Dayly", "rejected", "approved") - the clearest control evidence in the
  whole atamya corpus.
- **Input provenance:** the process starts from a data event ("Objekt erstellt").
- **Guards present:** the article describes the user task "Marketing-Review" as the
  assignment of the process to a responsible team - a human check after automation.
- **Prompt / model detail visible:** no prompt; the service is named (DeepL).

## Notes for the researcher

- The strongest atamya artefact: the article documents its own diagram element by element, so
  the BPMN reading and the AI reading both rest on page text and not only on the picture.
- The English twin article (`en/blog/bpmn-for-pim-managers/`) carries the same description in
  English with its own English figure - recorded separately (012).
- Capture: vendor asset, 1804 px wide - above the 1400 px bar, `capture_quality: legible`.
