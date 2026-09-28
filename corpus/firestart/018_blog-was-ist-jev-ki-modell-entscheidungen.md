---
n: 324
source: firestart
source_name: FireStart (vendor site, firestart.com)
source_type: vendor site (marketing, docs, blog)
title: Was ist Jev? Das KI-Modell, das entscheidet, statt zu schreiben
url: https://www.firestart.com/blog/was-ist-jev-ki-modell-entscheidungen
accessed: 2026-09-27
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: raster export of a BPMN 2.0 process diagram served by the page (task rectangles with type glyphs, diamond gateways, event circles)
bpmn_evidence_quote: "FireStart-Workflow: OCR liest eingehende Nachrichten, Jev klassifiziert und validiert sie, ein Gateway steuert den weiteren Prozessweg."
ai_evidence: the activity that classifies and validates is bound to the Jev model; the page says the routing gateway is steered by it
ai_evidence_quote: "Jev ist ein KI-Modell des US-Startups TypeSafe AI, das keinen Text erzeugt, sondern Entscheidungen trifft."
artefacts:
  screenshot: 018_blog-was-ist-jev-ki-modell-entscheidungen.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 2888
capture_method: the process export as the page serves it, downloaded once and re-encoded to png
---

## What the page shows

The diagram depicts incoming mail: OCR read-out, model classification, gateway routing. The page carries one process export, whose alt text reads "FireStart-Workflow: OCR liest eingehende Nachrichten, Jev klassifiziert und validiert sie, ein Gateway steuert den weiteren Prozessweg.".
The page states: "Was ist Jev? Das KI-Modell, das entscheidet, statt zu schreiben Welches Problem löst Jev? Mehrere Fragen zum selben Kontext beantwortet Jev parallel. Eine zusätzliche Frage macht die Anfrage laut TypeSafe kaum langsamer."

## Observations (description only, no interpretation)

- **AI activity - function:** "Jev ist ein KI-Modell des US-Startups TypeSafe AI, das keinen Text erzeugt, sondern Entscheidungen trifft."
- **AI activity - element type:** the activity that classifies and validates is bound to the Jev model; the page says the routing gateway is steered by it
- **Authority - downstream:** not visible on the page.
- **Authority - data:** not visible on the page.
- **Authority - control:** not visible on the page.
- **Input provenance:** not visible on the page.
- **Guards present:** the page names the limits of the model: it returns answer probabilities, gives no reason, and "Jev behandelt den übergebenen Text nicht als feindlich"; the page adds that a process should compute deadline arithmetic itself rather than ask the model
- **Prompt / model detail visible:** the page names the model and the integration (see the notes below)

## Notes for the researcher

BPMN 2.0 process export with an AI-bound task inside the process

