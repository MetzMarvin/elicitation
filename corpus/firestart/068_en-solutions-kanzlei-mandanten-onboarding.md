---
n: 221
source: firestart
source_name: FireStart (vendor site, firestart.com)
source_type: vendor site (marketing, docs, blog)
class: firestart-inline-flow
title: Automate Client Onboarding & KYC/AML
url: https://www.firestart.com/en/solutions/kanzlei-mandanten-onboarding
accessed: 2026-09-27
verdict: UNCERTAIN
needs_human_ruling: true
question: CLASS firestart-inline-flow: hand-drawn inline-SVG linear flow (rounded boxes + arrows, no events/gateways, no modeller markup), no AI in the graphic and none in the page's own text - the only AI string on the page is site chrome (navigation/footer): BPMN-like process artefact (collect) or marketing illustration (E1)? And with no AI element visible at all, does the row meet criterion C1 or is it E2?
needs_visual_check: false
bpmn_evidence: the route serves a hand-authored <svg> process graphic: 4 rounded-corner rectangle(s) carrying step labels, joined by 7 connector(s) (viewBox 0 0 720 200); no event circle, no gateway diamond, no pool or lane, and no modeller markup anywhere on the page - 0 elements with a djs-*/bpmn-* class, 0 data-element-id, no <bpmn:process>
bpmn_evidence_quote: "Client request | Document check | KYC/AML check | Approval & setup"
ai_evidence: no AI in the graphic and none in the page's own solution text; the only AI string on the page is site chrome - the navigation entry "AI Workflows"
ai_evidence_quote: "AI Workflows"
artefacts:
  screenshot: 068_en-solutions-kanzlei-mandanten-onboarding.png
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

A single inline-SVG graphic reads as a process: "Client request" -> "Document check" -> "KYC/AML check" -> "Approval & setup". It uses no BPMN notation - the boxes are rounded rectangles with a plain text label each, the connectors are plain arrow-headed lines, and there is no event, gateway, pool or lane. The page presents it under its own process walk-through and repeats the sequence in prose: "Four-Eyes Principle Three-Way Match Audit & Compliance Processes Risk Approvals Document Control".

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
The markup as the page served it is archived beside this record as `.svg`, and the render is the graphic itself on a white background, so the notation can be judged from the file rather than from prose.
Ruling applied 2026-09-27: this row was `E1-not-bpmn` and is superseded - the operator moved the whole `firestart-inline-flow` class to UNCERTAIN because rounded boxes plus arrows can be read as BPMN tasks and sequence flows (CLAUDE.md section 3: an ambiguous notation is UNCERTAIN, never E1).
