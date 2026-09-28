---
n: 1067
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Automate Scope 3 emissions reporting with Envizi Assist and watsonx - the 'AI NLP - Account Styles Allocations' figure"
url: https://developer.ibm.com/tutorials/awb-envizi-assist-scope3/
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "The page's 'AI NLP - Account Styles Allocations' figure draws an ordered pipeline - Financial Transaction Descriptions, then an AI NLP model, then 'Use USES10 Commodity Classes', then Envizi Account Style Allocation (S3 Category 1 Only), then Scope 3 Emissions Reporting - with the AI NLP model inside the drawn flow, but no BPMN events, no BPMN task types and no pool semantics. Is it a BPMN 2.0 model drawn in the vendor's house style (so it belongs in the corpus), or a proprietary pipeline illustration that E1-not-bpmn excludes?"
needs_visual_check: false
bpmn_evidence: "png (tiled on SHEET_SWEEP0903, row 1 col 4; viewed full size on SHEET_ZG0901). the page's other drawn figure is 'GHG-Scope3' (a circular infographic of 'Scope 1 direct', 'Scope 2 indirect' and 'Scope 3 indirect' over an 'Upstream activities / Reporting company / Downstream activities' bar); the remaining 22 figures are Envizi AI-assist console screenshots and template spreadsheets."
bpmn_evidence_quote: "AI NLP - Account Styles Allocations"
ai_evidence: "AI elements are inside the drawn figure: its second box is an 'AI NLP model' that classifies free-text 'Financial Transaction Descriptions', and the pipeline it sits in ends at an 'Envizi Account Style Allocation (S3 Category 1 Only)' box feeding 'Scope 3 Emissions Reporting'. So the AI is not merely mentioned on the page, it is a node the drawn flow passes through. The page's premise is verbatim 'The increasing demand for regulatory compliance has led organizations to disclose Greenhouse Gas (GHG) emissions, specifically Scope 3.' That is why the row is UNCERTAIN rather than excluded: the AI model is inside the drawn pipeline, but the notation the pipeline is drawn in is a vendor house style with no BPMN event, task or gateway types visible."
ai_evidence_quote: "AI NLP - Account Styles Allocations"
artefacts:
  screenshot: 024_1067X_AI-Assist-architecture.png
  assets: [024_1067X_AI-Assist-architecture.png]
  bpmn_xml: []
  archive: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: "the figure fetched from its native asset URL on developer.ibm.com and viewed at full size on 2026-09-25"
judgment: true
---

## What the artefact is

`https://developer.ibm.com/tutorials/awb-envizi-assist-scope3/` (api, ledger row n=1067), figure `figs/1067X_AI-Assist-architecture`.

## What the figure shows



## Why the row is UNCERTAIN

png (tiled on SHEET_SWEEP0903, row 1 col 4; viewed full size on SHEET_ZG0901). the page's other drawn figure is 'GHG-Scope3' (a circular infographic of 'Scope 1 direct', 'Scope 2 indirect' and 'Scope 3 indirect' over an 'Upstream activities / Reporting company / Downstream activities' bar); the remaining 22 figures are Envizi AI-assist console screenshots and template spreadsheets.

## AI evidence (why this is not an E2 exclusion)

AI elements are inside the drawn figure: its second box is an 'AI NLP model' that classifies free-text 'Financial Transaction Descriptions', and the pipeline it sits in ends at an 'Envizi Account Style Allocation (S3 Category 1 Only)' box feeding 'Scope 3 Emissions Reporting'. So the AI is not merely mentioned on the page, it is a node the drawn flow passes through. The page's premise is verbatim "The increasing demand for regulatory compliance has led organizations to disclose Greenhouse Gas (GHG) emissions, specifically Scope 3." That is why the row is UNCERTAIN rather than excluded: the AI model is inside the drawn pipeline, but the notation the pipeline is drawn in is a vendor house style with no BPMN event, task or gateway types visible.

## Notes for the researcher

- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
