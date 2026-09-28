---
n: 296
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Optimize RAG performance with intelligent chunking strategies"
url: https://developer.ibm.com/articles/awb-enhancing-rag-performance-chunking-strategies/
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: "The figure is a flow of boxes with 'Turn' labels and 'Generate' steps over a database cylinder on a RAG-optimisation page: is an ordered, LLM-bearing generation flow drawn as boxes and arrows a process artefact, or the architecture of the query's own processing?"
needs_visual_check: false
bpmn_evidence: "My first reading was architecture - the boxes are the machinery of one query - but the page draws it as an ordered flow with labelled turns and 'Generate' steps and uses it to explain a sequence of operations, so I cannot rule the process reading out. The drawing carries neither BPMN types nor events, and it also carries no element that would let me say a BPMN reader is wrong to see a flow in it."
bpmn_evidence_quote: "Retrieval-augmented generation (RAG) enhances large language model (LLM) responses by incorporating external knowledge sources, improving accuracy and relevance."
ai_evidence: "AI is inside the drawn flow: the figure sits on a page about chunking strategies for retrieval-augmented generation, the page's AI vocabulary is 'AI|LLM|LLMs|NLP|machine learning|watsonx.ai', and the flow's own stages are the LLM's input assembly ('Generate' over the retrieved-chunk store). The page's premise is verbatim 'Retrieval-augmented generation (RAG) enhances large language model (LLM) responses by incorporating external knowledge sources, improving accuracy and relevance.' No E2 exclusion would be honest here."
ai_evidence_quote: "Retrieval-augmented generation (RAG) enhances large language model (LLM) responses by incorporating external knowledge sources, improving accuracy and relevance."
artefacts:
  screenshot: 036_296_RAG_20performace.png
  assets: [036_296_RAG_20performace.png]
  bpmn_xml: []
  archive: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: "the figure fetched from its native asset URL on developer.ibm.com and viewed at full size on 2026-09-25, re-opened in the self-audit montage on 2026-09-26"
judgment: true
---

## What the artefact is

`https://developer.ibm.com/articles/awb-enhancing-rag-performance-chunking-strategies/` (ledger row n=296), figure `figs/296_RAG_20performace.png`.

## What the figure shows

a flow of boxes with 'Turn' labels, arrows and 'Generate' steps over a database cylinder; alt text 'Diagram showing how contextual compressi...'. Stages of one query's processing, no activities, events or decisions.

## Why the row is UNCERTAIN and not an E1 exclusion

My first reading was architecture - the boxes are the machinery of one query - but the page draws it as an ordered flow with labelled turns and 'Generate' steps and uses it to explain a sequence of operations, so I cannot rule the process reading out. The drawing carries neither BPMN types nor events, and it also carries no element that would let me say a BPMN reader is wrong to see a flow in it.

## AI evidence (why this is not an E2 exclusion)

AI is inside the drawn flow: the figure sits on a page about chunking strategies for retrieval-augmented generation, the page's AI vocabulary is 'AI|LLM|LLMs|NLP|machine learning|watsonx.ai', and the flow's own stages are the LLM's input assembly ('Generate' over the retrieved-chunk store). The page's premise is verbatim "Retrieval-augmented generation (RAG) enhances large language model (LLM) responses by incorporating external knowledge sources, improving accuracy and relevance." No E2 exclusion would be honest here.

## Notes for the researcher

- This row was first coded `E0-no-artefact` with `judgment: false` by the census pass, then recoded `E1-not-bpmn` with `judgment: true` (a drawn non-BPMN diagram is a notation call: CLAUDE.md sec 3, prompts/02b), and then flipped to `UNCERTAIN` by the self-audit that `prompts/02_source-census.md` step 3 asks for over the judgment rows. The ledger keeps all three rows for this `n`; the `supersedes_row` row is the one that counts (tools/audit.py: the last row for an `n` wins).
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
