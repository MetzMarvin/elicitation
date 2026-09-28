---
n: 208
source: atamya
source_name: Atamya (www.atamya.com - Agentic PIM with an embedded bpmn.io / Flowable BPMN engine)
source_type: vendor product page
title: ATAMYA homepage (start page)
url: https://www.atamya.com/de/
accessed: 2026-09-24
verdict: UNCERTAIN
needs_human_ruling: true
question: "The homepage USP card 'Workflows' shows a BPMN-shaped model whose tasks carry no text at all - only ATAMYA's element icons - and two of those tasks carry the robot-face glyph the site uses elsewhere for AI agents. Does an unlabelled, icon-only AI-agent task inside a BPMN model count as an AI element in the process, or is the card too generic to be an artefact?"
needs_visual_check: true
bpmn_evidence: "image: the homepage USP card 'website-homepage-usp-workflows.png' - a white canvas holding a BPMN model drawn with BPMN element shapes: a start event circle with the start marker, two exclusive-gateway diamonds carrying the X marker, two parallel-gateway diamonds carrying the + marker, six rounded-rectangle tasks on sequence-flow arrows and a plain end-event circle"
bpmn_evidence_quote: "Mit KI im Kern orchestrieren intelligente Agenten Ihre Workflows über den gesamten Produktdatenprozess hinweg"
ai_evidence: "page text + the robot-face task glyphs in the same figure"
ai_evidence_quote: "Mit KI im Kern orchestrieren intelligente Agenten Ihre Workflows"
artefacts:
  screenshot: 001_website-homepage-usp-workflows.png
  assets: []
  archive: 001_de.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: poor
capture_width_px: 640
capture_method: curl of the vendor's own wp-content/uploads asset at its native URL
---
## What the page shows

The German start page carries one workflow figure, `website-homepage-usp-workflows.png`
(640 x 437, the same file is served on the English start page), on a USP card headed
"Workflows". Inside a white canvas sits a BPMN model: start event, an exclusive gateway,
a parallel gateway, two tasks carrying a robot-face glyph (teal), two tasks carrying a
pencil and a person glyph (yellow), a second exclusive gateway, a further exclusive
gateway, three tasks carrying a document / gear / moon glyph, and an end event. Nothing
in the figure is labelled; the card's copy is the slogan text quoted above.

## Observations (description only, no interpretation)

- **AI activity - function:** not visible in the figure; the page copy claims AI agents
  orchestrate the workflow ("Mit KI im Kern orchestrieren intelligente Agenten Ihre
  Workflows").
- **AI activity - element type:** the two robot-face tasks are drawn as BPMN tasks, but
  with no label, so the element type they stand for is not readable from the diagram.
- **Authority - downstream / data / control:** not visible. The control flow is visible
  (X and + gateways, sequence flows) but carries no conditions.
- **Input provenance:** not visible.
- **Guards present:** not visible.
- **Prompt / model detail visible:** not visible in the figure. Elsewhere the site names
  the LLMs it integrates ("Integrieren Sie Ihre gewohnten KI-Systeme wie Claude, OpenAI
  oder Gemini").

## Notes for the researcher

- This is the weakest of the twelve atamya candidates and the reason it is UNCERTAIN, not
  INCLUDE: the notation is unambiguous BPMN, the AI element is unambiguous only if the
  robot-face glyph is read as ATAMYA's AI-agent icon, which the site does elsewhere
  (compare record 003, where the same glyph sits under the words "AI Agents").
- Capture: the vendor's own asset at its native 640 px - well under the 1400 px bar, so
  `capture_quality: poor` by rule; the shapes are legible but the icons are 20 px.
