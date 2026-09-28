---
n: 299
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Key strategies for enhancing RAG effectiveness"
url: https://developer.ibm.com/articles/awb-strategies-enhancing-rag-effectiveness/
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: "The figure draws a 'Start' box, two parallel 'AnnSearchRequest (text)' panels, a 'Rerank' panel that merges them, a 'Limit (final)' box and an 'End' box: start and end nodes plus a parallel split and a merge, in the vendor's own style, on a RAG-strategy page whose BPMN vocabulary includes 'gateway'. Does an LLM retrieval pipeline drawn with start, split, merge and end count as a BPMN-like artefact?"
needs_visual_check: false
bpmn_evidence: "This is the one recoded figure in the whole set that uses the vocabulary of process notation - Start and End as named nodes, and a fan-out that converges again - so my own note that 'the boxes are named after the API's own request and ranker objects' answers a question the figure does not ask. A researcher can reasonably read the drawing as a process whose steps are search operations, and I cannot name the notation it is drawn in, which under CLAUDE.md sec 3 makes the honest verdict UNCERTAIN rather than E1."
bpmn_evidence_quote: "Generation step: The relevant passages that are retrieved are fed into a large language model along with the original query to generate a response."
ai_evidence: "AI is the subject of the drawn sequence: the artefact is the multi-vector search step of a retrieval-augmented generation pipeline, and the page's AI vocabulary is 'AI|LLM|machine learning' with 'gateway' also present in its BPMN vocabulary. So this is not an E2 case - the sequence exists to serve an LLM, and the question for the researcher is its notation, not its AI content."
ai_evidence_quote: "Generation step: The relevant passages that are retrieved are fed into a large language model along with the original query to generate a response."
artefacts:
  screenshot: 037_299_image1.png
  assets: [037_299_image1.png]
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

`https://developer.ibm.com/articles/awb-strategies-enhancing-rag-effectiveness/` (ledger row n=299), figure `figs/299_image1.png`.

## What the figure shows

a 'Multi-Vector Search' pipeline of API objects: a 'Start' box over two parallel 'AnnSearchRequest (text)' panels (each holding 'Query Vector' and 'Limit 1'/'Limit 2' boxes), a 'Rerank' panel holding 'RRFRanker' and 'WeightedRanker', then 'Limit (final)' and 'End'. The boxes are named after the API's own request and ranker objects, so this is a pipeline of operations and parameters, not a process performed by actors. Alt text: 'Diagram showing Milvus multi-vector sear...'.

## Why the row is UNCERTAIN and not an E1 exclusion

This is the one recoded figure in the whole set that uses the vocabulary of process notation - Start and End as named nodes, and a fan-out that converges again - so my own note that 'the boxes are named after the API's own request and ranker objects' answers a question the figure does not ask. A researcher can reasonably read the drawing as a process whose steps are search operations, and I cannot name the notation it is drawn in, which under CLAUDE.md sec 3 makes the honest verdict UNCERTAIN rather than E1.

## AI evidence (why this is not an E2 exclusion)

AI is the subject of the drawn sequence: the artefact is the multi-vector search step of a retrieval-augmented generation pipeline, and the page's AI vocabulary is 'AI|LLM|machine learning' with 'gateway' also present in its BPMN vocabulary. So this is not an E2 case - the sequence exists to serve an LLM, and the question for the researcher is its notation, not its AI content.

## Notes for the researcher

- This row was first coded `E0-no-artefact` with `judgment: false` by the census pass, then recoded `E1-not-bpmn` with `judgment: true` (a drawn non-BPMN diagram is a notation call: CLAUDE.md sec 3, prompts/02b), and then flipped to `UNCERTAIN` by the self-audit that `prompts/02_source-census.md` step 3 asks for over the judgment rows. The ledger keeps all three rows for this `n`; the `supersedes_row` row is the one that counts (tools/audit.py: the last row for an `n` wins).
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
