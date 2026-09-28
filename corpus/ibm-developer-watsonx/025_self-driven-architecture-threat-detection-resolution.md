---
n: 1109
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Self-driven architecture: threat detection and resolution - the five-step threat-resolution pipeline figure"
url: https://developer.ibm.com/articles/self-driven-architecture-threat-detection-resolution/
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "The page's threat-resolution figure draws an ordered process - Ingest Security Events, then Threat Detection (AI / Rules), then Threat Prioritization (Context, Risk), then Decision Engine, then Automated Response, with a feedback arrow from Automated Response back to Threat Detection - and one of its steps is explicitly an AI step, 'Threat Detection (AI / Rules)'. But no BPMN events, task types, gateways or pool semantics are visible. Is it a BPMN 2.0 model drawn in the vendor's house style (so it belongs in the corpus), or a proprietary box-and-arrow illustration that E1-not-bpmn excludes?"
needs_visual_check: false
bpmn_evidence: "png (tiled on SHEET_SWEEP1001, row 1 col 6; viewed full size on SHEET_ZS1001). the page's only other figure is a JSON/code listing (image2.png). The drawn figure is a blue-banded pipeline: Ingest Security Events, Threat Detection (AI / Rules), Threat Prioritization (Context, Risk), Decision Engine, Automated Response, with a return path from Automated Response to Threat Detection."
bpmn_evidence_quote: "Cloud threats are growing faster than traditional security operations can handle."
ai_evidence: "AI elements are inside the drawn figure: one of its five steps is named 'Threat Detection (AI / Rules)' and the page's argument is that this detection step is what the automation replaces human triage with. The page's premise is verbatim 'Cloud threats are growing faster than traditional security operations can handle.' That is why the row is UNCERTAIN rather than excluded: the AI step is inside the drawn process and the arrows order the steps (including a feedback arrow from Automated Response back to Threat Detection), but the notation is a vendor box-and-arrow band with no BPMN events, task types, gateways or pools."
ai_evidence_quote: "Cloud threats are growing faster than traditional security operations can handle."
artefacts:
  screenshot: 025_1109X_image1.png
  assets: [025_1109X_image1.png]
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

`https://developer.ibm.com/articles/self-driven-architecture-threat-detection-resolution/` (api, ledger row n=1109), figure `figs/1109X_image1`.

## What the figure shows



## Why the row is UNCERTAIN

png (tiled on SHEET_SWEEP1001, row 1 col 6; viewed full size on SHEET_ZS1001). the page's only other figure is a JSON/code listing (image2.png). The drawn figure is a blue-banded pipeline: Ingest Security Events, Threat Detection (AI / Rules), Threat Prioritization (Context, Risk), Decision Engine, Automated Response, with a return path from Automated Response to Threat Detection.

## AI evidence (why this is not an E2 exclusion)

AI elements are inside the drawn figure: one of its five steps is named 'Threat Detection (AI / Rules)' and the page's argument is that this detection step is what the automation replaces human triage with. The page's premise is verbatim "Cloud threats are growing faster than traditional security operations can handle." That is why the row is UNCERTAIN rather than excluded: the AI step is inside the drawn process and the arrows order the steps (including a feedback arrow from Automated Response back to Threat Detection), but the notation is a vendor box-and-arrow band with no BPMN events, task types, gateways or pools.

## Notes for the researcher

- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
