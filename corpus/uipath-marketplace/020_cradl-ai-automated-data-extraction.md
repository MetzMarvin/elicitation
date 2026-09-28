---
n: 1797
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: "Cradl AI - Automated Data Extraction"
url: https://marketplace.uipath.com/listings/cradl-ai-automated-data-extraction-demo
accessed: 2026-09-28
verdict: UNCERTAIN
needs_human_ruling: true
question: "Informal icon-and-arrow process sketch (no BPMN shapes, events or gateways) in which an 'AI Model' output is routed on 'Certain' / 'Uncertain' to straight-through JSON or a 'Human validation' step. Does it count as a BPMN diagram?"
needs_visual_check: false
bpmn_evidence: single listing image: process sketch UiPath -> invoice.pdf -> AI Model -> 'Certain' / 'Uncertain' branches -> invoice.json / 'Human validation' -> UiPath, inside a 'CRADL-AI' frame; no BPMN shapes
bpmn_evidence_quote: "Boost UiPath with Cradl AI: State of the art document parsing powered by the latest within machine learning."
ai_evidence: node 'AI Model' whose output branches on 'Certain' / 'Uncertain'; prose on ML document parsing
ai_evidence_quote: "Boost UiPath with Cradl AI: State of the art document parsing powered by the latest within machine learning."
artefacts:
  screenshot: 020_cradl-ai-automated-data-extraction.png
  archive: 020_cradl-ai-automated-data-extraction.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 4050
capture_method: python urllib GET of the original marketplace-cdn.uipath.com asset (cdn-cgi resize wrapper stripped); 4050 px is the native size
---

## What the page shows

A Cradl AI document-extraction solution for UiPath. The single listing image shows: 'UiPath' -> 'invoice.pdf' -> 'AI Model' -> a green branch labelled 'Certain' straight to 'invoice.json' -> 'UiPath', and a branch labelled 'Uncertain' down to 'Human validation - Human-in-the-loop user interface' (with a stock photo of a person at a screen), which then joins to 'invoice.json'. All of it sits in a frame titled 'CRADL-AI'.

## Observations (description only, no interpretation)

- **AI activity - function:** 'AI Model' extracts data from 'invoice.pdf' to 'invoice.json'
- **AI activity - element type:** a labelled card 'AI Model' in an informal flow
- **Authority - downstream:** 'invoice.json' returned to 'UiPath'
- **Authority - data:** 'invoice.json'
- **Authority - control:** branch labels 'Certain' (straight through) / 'Uncertain' (to human validation) on the AI model's output
- **Input provenance:** 'invoice.pdf' handed over by 'UiPath'
- **Guards present:** 'Human validation - Human-in-the-loop user interface' on the 'Uncertain' branch
- **Prompt / model detail visible:** none

## Notes for the researcher

Native asset 4050 px wide, fully legible.
