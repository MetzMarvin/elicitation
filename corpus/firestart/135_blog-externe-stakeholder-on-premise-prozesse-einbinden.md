---
n: 326
source: firestart
source_name: FireStart (vendor site, firestart.com)
source_type: vendor site (marketing, docs, blog)
class: firestart-inline-flow
title: Externe Stakeholder in On-Premise-Prozesse einbinden: Lieferanten, Bewerber und Kunden ohne VPN andocken
url: https://www.firestart.com/blog/externe-stakeholder-on-premise-prozesse-einbinden
accessed: 2026-09-27
verdict: UNCERTAIN
needs_human_ruling: true
question: CLASS firestart-inline-flow, sub-case: stacked zones (rounded boxes + dashed connectors + an icon) that read as an architecture illustration rather than a linear flow, no AI in the graphic and none in the page's own text (the only AI string is site chrome): BPMN-like process artefact (collect) or marketing illustration (E1)? And with no AI element visible at all, does the row meet criterion C1 or is it E2?
needs_visual_check: false
bpmn_evidence: the route serves a hand-authored <svg> process graphic: 8 rounded-corner rectangle(s) carrying step labels, joined by 3 connector(s) (viewBox 0 0 320 390); no event circle, no gateway diamond, no pool or lane, and no modeller markup anywhere on the page - 0 elements with a djs-*/bpmn-* class, 0 data-element-id, no <bpmn:process>; the route carries 2 such graphics in total
bpmn_evidence_quote: "Externe Person | Azure-Komponente | als Brücke | Internes Netzwerk | Interner Prozess"
ai_evidence: no AI in the graphic and none in the page's own solution text; the only AI string on the page is site chrome - the navigation entry "KI Workflows"
ai_evidence_quote: "KI Workflows"
artefacts:
  screenshot: 135_blog-externe-stakeholder-on-premise-prozesse-einbinden.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: inline-svg-render
capture_quality: legible
capture_width_px: 399
capture_method: the route's own inline <svg> serialised with its computed fill/stroke/font and drawn onto a white canvas in the browser that served it (chrome-devtools-mcp, own tab); the markup as served is beside this record as .svg
---

## What the page shows

The page carries two inline-SVG figures that illustrate the article's two ways of carrying a
request across the network boundary. They are drawn as stacked zones rather than as a task
sequence: the first names "Externe Person", then "Azure-Komponente" / "als Brücke", then
"Internes Netzwerk" with "Interner Prozess" inside it; the second replaces the middle zone with
"FireStart" / "Cloud-Formular". The drawing is not BPMN: rounded rectangles, dashed connectors
and an icon, with no event, gateway, pool or lane. The article's own summary reads: "Dieser
Beitrag vergleicht zwei Wege über die Unternehmensgrenze: eine Azure-basierte Anbindung und den
FireStart-Hybridansatz."

## Observations (description only, no interpretation)

- **AI activity - function:** not visible in the graphic and not named in the page's own text
- **AI activity - element type:** not visible on the artefact
- **Authority - downstream:** not visible on the page.
- **Authority - data:** not visible on the page.
- **Authority - control:** not visible on the page.
- **Input provenance:** not visible on the page.
- **Guards present:** none observed.
- **Prompt / model detail visible:** not visible on the page.

## Notes for the researcher

class member: nothing in the graphic and nothing in the page text marks an AI element; the AI string on the page is site chrome, which is why this row was not coded E2 - the class ruling and criterion C1 are the researcher's calls here.
This route serves 2 such graphics; the second and its markup are beside this record as `_fig2.png` / `_fig2.svg`. Both read as zone/architecture illustrations rather than as linear task flows - if the class ruling is to collect the linear flows only, the researcher may want to code this route E1.
Ruling applied 2026-09-27: this row was `E1-not-bpmn` and is superseded - the operator moved the whole `firestart-inline-flow` class to UNCERTAIN because rounded boxes plus arrows can be read as BPMN tasks and sequence flows (CLAUDE.md section 3: an ambiguous notation is UNCERTAIN, never E1).
