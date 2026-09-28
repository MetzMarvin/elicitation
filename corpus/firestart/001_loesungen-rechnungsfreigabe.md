---
n: 116
source: firestart
source_name: FireStart (vendor site, firestart.com)
source_type: vendor site (marketing, docs, blog)
title: Rechnungsfreigabe automatisieren
url: https://www.firestart.com/loesungen/rechnungsfreigabe
accessed: 2026-09-27
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: raster export of a BPMN 2.0 process diagram served by the page (task rectangles with type glyphs, diamond gateways, event circles)
bpmn_evidence_quote: "Rechnungsfreigabe Prozessdiagramm"
ai_evidence: a task whose marker is the literal word "OCR/KI", with the invoice document attached as a data object
ai_evidence_quote: "OCR und KI lesen Rechnungsdaten, Positionen und Lieferant aus."
artefacts:
  screenshot: 001_loesungen-rechnungsfreigabe.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: marginal
capture_width_px: 406
capture_method: the process export as the page serves it, downloaded once and re-encoded to png
---

## What the page shows

The diagram depicts invoice approval: capture, OCR/KI read-out, 3-way match, approval matrix, ERP posting. The page carries one process export, whose alt text reads "Rechnungsfreigabe Prozessdiagramm".
The page states: "OCR und KI lesen Rechnungsdaten, Positionen und Lieferant aus."

## Observations (description only, no interpretation)

- **AI activity - function:** "OCR und KI lesen Rechnungsdaten, Positionen und Lieferant aus."
- **AI activity - element type:** a task whose marker is the literal word "OCR/KI", with the invoice document attached as a data object
- **Authority - downstream:** not visible on the page.
- **Authority - data:** not visible on the page.
- **Authority - control:** not visible on the page.
- **Input provenance:** not visible on the page.
- **Guards present:** none observed
- **Prompt / model detail visible:** not visible on the page

## Notes for the researcher

BPMN 2.0 process export with an AI-bound task inside the process
the export is served only at 406 px wide, so the task labels are small at native size
