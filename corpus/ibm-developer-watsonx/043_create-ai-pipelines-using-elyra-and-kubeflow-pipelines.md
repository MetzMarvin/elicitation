---
n: 521
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Create AI pipelines using Elyra and Kubeflow Pipelines"
url: https://developer.ibm.com/articles/create-ai-pipelines-using-elyra-and-kubeflow-pipelines/
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: "The figure is captioned 'Diagram of a pipeline example' and draws load_data.csv branching into 'Part 1 - Data Clean...', which then branches into 'Part 2 - Data Ana...' and 'Part 3 - Time Seri...': numbered, ordered stages with a split - is a pipeline DAG with numbered stages a process artefact for the corpus?"
needs_visual_check: false
bpmn_evidence: "The stages are numbered ('Part 1', 'Part 2', 'Part 3'), they are ordered by directed edges, and the drawing contains a genuine split where one stage feeds two successors - the one structural feature of this figure that a BPMN reader will recognise immediately. The counter-reading is mine from the first pass: the figure is the authored pipeline of an Elyra/Kubeflow notebook, i.e. an executable data graph rather than a process performed by anyone. Both readings survive the drawing, and the page's BPMN vocabulary even contains 'canvas' and 'sub-process'."
bpmn_evidence_quote: "Data scientists frequently use Jupyter Notebooks to do their work."
ai_evidence: "AI is the pipeline's purpose and its content: the page is a tutorial for building AI pipelines ('Create AI pipelines using Elyra and Kubeflow Pipelines', AI vocabulary 'AI|machine learning') and the stages it chains are the data preparation and time-series analysis steps that feed a model. So the row is UNCERTAIN rather than an E2 exclusion - the AI is inside the chain of stages the figure draws."
ai_evidence_quote: "Data scientists frequently use Jupyter Notebooks to do their work."
artefacts:
  screenshot: 043_521_basic_pipeline.png
  assets: [043_521_basic_pipeline.png]
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

`https://developer.ibm.com/articles/create-ai-pipelines-using-elyra-and-kubeflow-pipelines/` (ledger row n=521), figure `figs/521_basic_pipeline.png`.

## What the figure shows

a small hand-drawn-style pipeline DAG: a 'load_data.csv' box branching into 'Part 1 - Data Clean...', which branches into 'Part 2 - Data Ana...' and 'Part 3 - Time Seri...'; alt text 'Diagram of a pipeline example'. A data pipeline DAG, not a process.

## Why the row is UNCERTAIN and not an E1 exclusion

The stages are numbered ('Part 1', 'Part 2', 'Part 3'), they are ordered by directed edges, and the drawing contains a genuine split where one stage feeds two successors - the one structural feature of this figure that a BPMN reader will recognise immediately. The counter-reading is mine from the first pass: the figure is the authored pipeline of an Elyra/Kubeflow notebook, i.e. an executable data graph rather than a process performed by anyone. Both readings survive the drawing, and the page's BPMN vocabulary even contains 'canvas' and 'sub-process'.

## AI evidence (why this is not an E2 exclusion)

AI is the pipeline's purpose and its content: the page is a tutorial for building AI pipelines ('Create AI pipelines using Elyra and Kubeflow Pipelines', AI vocabulary 'AI|machine learning') and the stages it chains are the data preparation and time-series analysis steps that feed a model. So the row is UNCERTAIN rather than an E2 exclusion - the AI is inside the chain of stages the figure draws.

## Notes for the researcher

- This row was first coded `E0-no-artefact` with `judgment: false` by the census pass, then recoded `E1-not-bpmn` with `judgment: true` (a drawn non-BPMN diagram is a notation call: CLAUDE.md sec 3, prompts/02b), and then flipped to `UNCERTAIN` by the self-audit that `prompts/02_source-census.md` step 3 asks for over the judgment rows. The ledger keeps all three rows for this `n`; the `supersedes_row` row is the one that counts (tools/audit.py: the last row for an `n` wins).
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
