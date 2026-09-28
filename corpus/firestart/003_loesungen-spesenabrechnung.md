---
n: 120
source: firestart
source_name: FireStart (vendor site, firestart.com)
source_type: vendor site (marketing, docs, blog)
title: Spesenabrechnung automatisieren
url: https://www.firestart.com/loesungen/spesenabrechnung
accessed: 2026-09-27
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: raster export of a BPMN 2.0 process diagram served by the page (task rectangles with type glyphs, diamond gateways, event circles)
bpmn_evidence_quote: "Spesenabrechnung Prozessdiagramm"
ai_evidence: an AI-bound task on the OCR read-out of the receipt
ai_evidence_quote: "Mitarbeitende erfassen Belege per Foto, OCR liest die Daten aus."
artefacts:
  screenshot: 003_loesungen-spesenabrechnung.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1200
capture_method: the process export as the page serves it, downloaded once and re-encoded to png
---

## What the page shows

The diagram depicts expense submission. The page carries one process export, whose alt text reads "Spesenabrechnung Prozessdiagramm".
The page states: "Mitarbeitende erfassen Belege per Foto, OCR liest die Daten aus. Ja. Mitarbeitende fotografieren Belege per App, die per OCR ausgelesen und automatisch zugeordnet werden. Per Foto mit automatischer OCR-Auslesung; manuelles Abtippen entfällt."

## Observations (description only, no interpretation)

- **AI activity - function:** "Mitarbeitende erfassen Belege per Foto, OCR liest die Daten aus."
- **AI activity - element type:** an AI-bound task on the OCR read-out of the receipt
- **Authority - downstream:** not visible on the page.
- **Authority - data:** not visible on the page.
- **Authority - control:** not visible on the page.
- **Input provenance:** not visible on the page.
- **Guards present:** none observed
- **Prompt / model detail visible:** not visible on the page

## Notes for the researcher

BPMN 2.0 process export with an AI-bound task inside the process

