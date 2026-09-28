---
n: 479
source: firestart
source_name: FireStart (vendor site, firestart.com)
source_type: vendor site (marketing, docs, blog)
class: firestart-inline-flow
title: Rechte-Missbrauch-Check (IAM) mit KI
url: https://www.firestart.com/use-cases/iam-missbrauch-ki
accessed: 2026-09-27
verdict: UNCERTAIN
needs_human_ruling: true
question: CLASS firestart-inline-flow: hand-drawn inline-SVG linear flow (rounded boxes + arrows, no events/gateways, no modeller markup), AI named only in the page's own solution prose and in no step label: BPMN-like process artefact (collect) or marketing illustration (E1)? And does a step the prose calls AI-bound count as an AI element when the graphic itself does not mark it?
needs_visual_check: false
bpmn_evidence: the route serves a hand-authored <svg> process graphic: 5 rounded-corner rectangle(s) carrying step labels, joined by 9 connector(s) (viewBox 0 0 900 200); no event circle, no gateway diamond, no pool or lane, and no modeller markup anywhere on the page - 0 elements with a djs-*/bpmn-* class, 0 data-element-id, no <bpmn:process>
bpmn_evidence_quote: "Zugriffsmuster übe... | Baseline lernen | Anomalie erkennen | Alert generieren | Human-Entscheidung"
ai_evidence: no step label names the AI; the page's own solution text does: "Rechte-Missbrauch-Check (IAM) mit KI"
ai_evidence_quote: "Rechte-Missbrauch-Check (IAM) mit KI"
artefacts:
  screenshot: 178_use-cases-iam-missbrauch-ki.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: inline-svg-render
capture_quality: legible
capture_width_px: 791
capture_method: the route's own inline <svg> serialised with its computed fill/stroke/font and drawn onto a white canvas in the browser that served it (chrome-devtools-mcp, own tab); the markup as served is beside this record as .svg
---

## What the page shows

A single inline-SVG graphic reads as a process: "Zugriffsmuster übe..." -> "Baseline lernen" -> "Anomalie erkennen" -> "Alert generieren" -> "Human-Entscheidung". It uses no BPMN notation - the boxes are rounded rectangles with a plain text label each, the connectors are plain arrow-headed lines, and there is no event, gateway, pool or lane. The page presents it under its own process walk-through and repeats the sequence in prose: "Rechnungsfreigabe Zahlungsläufe prüfen & freigeben Budgetfreigaben / Kostenstellen-Freigaben Bestellanforderungs- und Freigabeprozess Spesenabrechnung".

## Observations (description only, no interpretation)

- **AI activity - function:** not marked in the graphic; the page text says: "Rechte-Missbrauch-Check (IAM) mit KI"
- **AI activity - element type:** not visible on the artefact
- **Authority - downstream:** not visible on the page.
- **Authority - data:** not visible on the page.
- **Authority - control:** not visible on the page.
- **Input provenance:** not visible on the page.
- **Guards present:** none observed.
- **Prompt / model detail visible:** not visible on the page.

## Notes for the researcher

class member: the graphic carries no AI marker; the AI step is named only in the page's solution prose, so whether the artefact itself holds an AI element is unresolved.
The markup as the page served it is archived beside this record as `.svg`, and the render is the graphic itself on a white background, so the notation can be judged from the file rather than from prose.
Ruling applied 2026-09-27: this row was `E1-not-bpmn` and is superseded - the operator moved the whole `firestart-inline-flow` class to UNCERTAIN because rounded boxes plus arrows can be read as BPMN tasks and sequence flows (CLAUDE.md section 3: an ambiguous notation is UNCERTAIN, never E1).
