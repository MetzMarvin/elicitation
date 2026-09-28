---
n: 839
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Preparing data for fine-tuning LLMs for contract analysis using Data Prep Kit (DPK) - the 'Process of fine tuning an LLM' figure"
url: https://developer.ibm.com/tutorials/dpk-fine-tuning-llms/
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "The page's image1.png is an arrow chain carrying a dataset into a 'Base LLM', then a 'Fine tuned LLM', then 'Summarization', under the band labels 'Pre-training' and 'Fine-tuning', and the page's own alt text calls it the 'Process of fine tuning an LLM'. Its boxes are model artefacts rather than activities (an architecture/data-flow reading), but the phase labels and the alt text present it as a process. Does the corpus record this as a process artefact, or does E0-no-artefact exclude it as a component/data-flow view?"
needs_visual_check: false
bpmn_evidence: "png, the page's own image1.png fetched and viewed at full size (contact sheet SHEET_VIEW07, row 2 col 4). an arrow chain on a white ground: a dataset icon feeding a grey 'Base LLM' box, then a 'Fine tuned LLM' box, then a 'Summarization' box, with a 'User' node at the right and band labels above and below reading 'Pre-training', 'Fine-tuning', 'Large dataset (websites, books, academic papers, etc.)' and 'Domain specific dataset'. The chain mixes artefact boxes (Base LLM, Fine tuned LLM) with an activity box (Summarization) and phase labels, so the figure can be read either as a model-transformation pipeline (architecture) or as the ordered process of fine-tuning an LLM - which is what the page's own alt text calls it. I hesitated; hesitation resolves to UNCERTAIN."
bpmn_evidence_quote: "Process of fine tuning an LLM"
ai_evidence: "AI elements are inside the drawn figure: a 'Base LLM' box, a 'Fine tuned LLM' box and a 'Summarization' box, under the phase labels 'Pre-training' and 'Fine-tuning', and the page's own alt text calls the figure the 'Process of fine tuning an LLM'. The page states verbatim 'Fine-tuning LLMs involves taking pre-trained models and training them on smaller, domain-specific data sets to enhance their performance.' UNCERTAIN because the chain mixes model artefacts with an activity box."
ai_evidence_quote: "Process of fine tuning an LLM"
artefacts:
  screenshot: 012_839X_image1.png
  assets: [012_839X_image1.png]
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

`https://developer.ibm.com/tutorials/dpk-fine-tuning-llms/` (api, ledger row n=839), figure `figs/839X_image1`.

## What the figure shows



## Why the row is UNCERTAIN

png, the page's own image1.png fetched and viewed at full size (contact sheet SHEET_VIEW07, row 2 col 4). an arrow chain on a white ground: a dataset icon feeding a grey 'Base LLM' box, then a 'Fine tuned LLM' box, then a 'Summarization' box, with a 'User' node at the right and band labels above and below reading 'Pre-training', 'Fine-tuning', 'Large dataset (websites, books, academic papers, etc.)' and 'Domain specific dataset'. The chain mixes artefact boxes (Base LLM, Fine tuned LLM) with an activity box (Summarization) and phase labels, so the figure can be read either as a model-transformation pipeline (architecture) or as the ordered process of fine-tuning an LLM - which is what the page's own alt text calls it. I hesitated; hesitation resolves to UNCERTAIN.

## AI evidence (why this is not an E2 exclusion)

AI elements are inside the drawn figure: a 'Base LLM' box, a 'Fine tuned LLM' box and a 'Summarization' box, under the phase labels 'Pre-training' and 'Fine-tuning', and the page's own alt text calls the figure the 'Process of fine tuning an LLM'. The page states verbatim "Fine-tuning LLMs involves taking pre-trained models and training them on smaller, domain-specific data sets to enhance their performance." UNCERTAIN because the chain mixes model artefacts with an activity box.

## Notes for the researcher

- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
