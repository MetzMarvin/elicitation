---
n: 1152
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Build an AI research agent for image analysis with IBM Granite - the 'multi-agent image research workflow' figure (Image Explainer -> Research Identifier -> Research Agents -> Report Generator)"
url: https://developer.ibm.com/tutorials/awb-build-ai-research-agent-image-analysis-granite/
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "The page's process figure is a drawio diagram drawn as a left-to-right chain of four stages, each naming the Granite model that works it - 'Image Explainer' on a 'Granite Vision Model', 'Research Identifier' on 'Granite 3.2 Instruct', stacked 'Research Agents' on 'Granite 3.2 2b', 'Report Generator' on 'Granite 3.2 Instruct' - with single-headed arrows between the stages, a 'watsonx' plate beneath the second stage and boxes for 'Image', 'Research Doc' and 'watsonx.ai'. The page's own alt text calls it a 'Diagram of the multi-agent image research workflow connecting Granite vision, item identifier, and parallel RAG crews'. Is it a BPMN 2.0 model drawn in the vendor's house style (so it belongs in the corpus), or a drawio workflow illustration that E1-not-bpmn excludes?"
needs_visual_check: false
bpmn_evidence: "png (tiled on SHEET_SWEEP1102, row 4 col 8; viewed full size at 720x500 on SHEET_ZS1201). the page's process figure; its other three figures are console screenshots of the running system (Open WebUI server logs showing the JSON research items, logs showing the parallel research agents, and the chat interface with the final synthesized report)."
bpmn_evidence_quote: "Diagram of the multi-agent image research workflow connecting Granite vision, item identifier, and parallel RAG crews"
ai_evidence: "AI elements are inside the drawn figure: each stage names the Granite model that works it - 'Image Explainer' on a 'Granite Vision Model', 'Research Identifier' on 'Granite 3.2 Instruct', the stacked 'Research Agents' on 'Granite 3.2 2b' and the 'Report Generator' on 'Granite 3.2 Instruct' - and a 'watsonx.ai' box sits at the foot of the chain. The page's own alt text is verbatim 'Diagram of the multi-agent image research workflow connecting Granite vision, item identifier, and parallel RAG crews', and the page says verbatim 'In this tutorial, you'll build an AI research agent that conducts in-depth research based on image analysis.' That is why the row is UNCERTAIN rather than excluded: the AI models are stages of the drawn workflow, but the notation is a drawio illustration, not BPMN 2.0."
ai_evidence_quote: "Diagram of the multi-agent image research workflow connecting Granite vision, item identifier, and parallel RAG crews"
artefacts:
  screenshot: 027_1152X_image-explainer-agent-drawio.png
  assets: [027_1152X_image-explainer-agent-drawio.png]
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

`https://developer.ibm.com/tutorials/awb-build-ai-research-agent-image-analysis-granite/` (api, ledger row n=1152), figure `figs/1152X_image-explainer-agent-drawio`.

## What the figure shows



## Why the row is UNCERTAIN

png (tiled on SHEET_SWEEP1102, row 4 col 8; viewed full size at 720x500 on SHEET_ZS1201). the page's process figure; its other three figures are console screenshots of the running system (Open WebUI server logs showing the JSON research items, logs showing the parallel research agents, and the chat interface with the final synthesized report).

## AI evidence (why this is not an E2 exclusion)

AI elements are inside the drawn figure: each stage names the Granite model that works it - 'Image Explainer' on a 'Granite Vision Model', 'Research Identifier' on 'Granite 3.2 Instruct', the stacked 'Research Agents' on 'Granite 3.2 2b' and the 'Report Generator' on 'Granite 3.2 Instruct' - and a 'watsonx.ai' box sits at the foot of the chain. The page's own alt text is verbatim "Diagram of the multi-agent image research workflow connecting Granite vision, item identifier, and parallel RAG crews", and the page says verbatim "In this tutorial, you'll build an AI research agent that conducts in-depth research based on image analysis." That is why the row is UNCERTAIN rather than excluded: the AI models are stages of the drawn workflow, but the notation is a drawio illustration, not BPMN 2.0.

## Notes for the researcher

- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
