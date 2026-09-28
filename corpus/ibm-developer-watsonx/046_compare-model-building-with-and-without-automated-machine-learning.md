---
n: 1119
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Build machine learning models with and without AutoML"
url: https://developer.ibm.com/articles/compare-model-building-with-and-without-automated-machine-learning/
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: "The figure draws AutoAI's work as chevron stage bands whose stages are activities in order - 'Provide data in a CSV file', 'Prepare data', 'Select model type', 'Generate and rank model pipelines', 'Save and deploy a model' - with sub-labels under each: is a chevron stage band of ordered AI/ML activities a process artefact for the corpus?"
needs_visual_check: false
bpmn_evidence: "The stages are verb-phrase activities, they are ordered, and the artefact they describe is an AI service doing the work - which is the corpus's question almost verbatim. What made me exclude it was the notation: a chevron band is an infographic convention, not a model, and my recode names it as such. Naming the notation is a call I can make, but a researcher may still want the figure in the corpus because of what it orders, so the row is recorded as UNCERTAIN rather than left as an exclusion."
bpmn_evidence_quote: "Machine learning overview"
ai_evidence: "AI performs the drawn stages: the bands are AutoAI's own pipeline ('Generate and rank model pipelines', with hyper-parameter optimization and algorithm selection under the stages), the page's AI vocabulary is 'AI|Bob|machine learning|predictive', and the page's premise - its own heading - is verbatim 'Machine learning overview'. The row is UNCERTAIN on notation and ordering, never on the presence of an AI element."
ai_evidence_quote: "Machine learning overview"
artefacts:
  screenshot: 046_1119X_AutoAI-ml-process.png
  assets: [046_1119X_AutoAI-ml-process.png]
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

`https://developer.ibm.com/articles/compare-model-building-with-and-without-automated-machine-learning/` (ledger row n=1119), figure `figs/1119X_AutoAI-ml-process.png`.

## What the figure shows

the page's process-shaped figures are chevron stage bands: 'AutoAI - Provide data in a CSV file, Prepare data, Select model type, Generate and rank model pipelines, Save and deploy a model' with sub-labels beneath each stage (feature type detection, missing values imputation, feature encoding and scaling, selection of the best algorithm, hyper-parameter optimization), and 'Machine learning overview - Define your project goals, Prepare the data, Choose a tool, Train your model, Deploy your model'. The page's other figures are two cartoon data scientists (Bob, Lauren) and a comparison table.

## Why the row is UNCERTAIN and not an E1 exclusion

The stages are verb-phrase activities, they are ordered, and the artefact they describe is an AI service doing the work - which is the corpus's question almost verbatim. What made me exclude it was the notation: a chevron band is an infographic convention, not a model, and my recode names it as such. Naming the notation is a call I can make, but a researcher may still want the figure in the corpus because of what it orders, so the row is recorded as UNCERTAIN rather than left as an exclusion.

## AI evidence (why this is not an E2 exclusion)

AI performs the drawn stages: the bands are AutoAI's own pipeline ('Generate and rank model pipelines', with hyper-parameter optimization and algorithm selection under the stages), the page's AI vocabulary is 'AI|Bob|machine learning|predictive', and the page's premise - its own heading - is verbatim "Machine learning overview". The row is UNCERTAIN on notation and ordering, never on the presence of an AI element.

## Notes for the researcher

- This row was first coded `E0-no-artefact` with `judgment: false` by the census pass, then recoded `E1-not-bpmn` with `judgment: true` (a drawn non-BPMN diagram is a notation call: CLAUDE.md sec 3, prompts/02b), and then flipped to `UNCERTAIN` by the self-audit that `prompts/02_source-census.md` step 3 asks for over the judgment rows. The ledger keeps all three rows for this `n`; the `supersedes_row` row is the one that counts (tools/audit.py: the last row for an `n` wins).
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
