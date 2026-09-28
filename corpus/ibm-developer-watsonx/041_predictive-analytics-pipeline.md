---
n: 484
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "From data to prediction: Building a robust  predictive analytics pipeline"
url: https://developer.ibm.com/articles/predictive-analytics-pipeline/
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: "The figure draws an ordered chain of ML activities - Data Collection > Data Preprocessing & Cleaning > Exploratory Data Analysis > Feature Engineering > Principal Component Analysis > Feature Selection > Model Training > Model Evaluation > Prediction Output - grouped in three labelled bands: is a pipeline of activity-labelled stages in the vendor's house style a process artefact?"
needs_visual_check: false
bpmn_evidence: "Re-opening the figure in the audit shows what my first-pass note understated: the stages inside each band are chained by directed arrows, and the stage names are activities performed in order (collect, clean, analyse, engineer, train, evaluate), ending in an output. The band headings are what made me code it as a layered architecture; the arrows and the verb labels are what make a BPMN reader see a process. I cannot name a notation that settles it, so UNCERTAIN is the honest verdict, and the question is the one the researcher must answer."
bpmn_evidence_quote: "Predictive analytics has quickly become a cornerstone of modern applications- powering everything from customer churn forecasting to equipment failure detection."
ai_evidence: "AI is inside the drawn chain rather than mentioned beside it: the sequence ends in 'Model Training', 'Model Evaluation' and 'Prediction Output', i.e. the machine learning pipeline itself, and the page's AI vocabulary is 'machine learning|predictive' on an article titled 'From data to prediction: Building a robust predictive analytics pipeline' whose premise is verbatim 'Predictive analytics has quickly become a cornerstone of modern applications- powering everything from customer churn forecasting to equipment failure detection.'"
ai_evidence_quote: "Predictive analytics has quickly become a cornerstone of modern applications- powering everything from customer churn forecasting to equipment failure detection."
artefacts:
  screenshot: 041_484_predictive-analytics-pipeline-arch.png
  assets: [041_484_predictive-analytics-pipeline-arch.png]
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

`https://developer.ibm.com/articles/predictive-analytics-pipeline/` (ledger row n=484), figure `figs/484_predictive-analytics-pipeline-arch.png`.

## What the figure shows

a three-band pipeline architecture: Data Source Layer (Data Collection, Data Preprocessing & Cleaning), Analytics Layer (Exploratory Data Analysis, Feature Engineering, Prepare Data for Model, Feature Selection) and Models Layer (Model Training, Model Evaluation, Prediction Output); alt text 'Predictive analytics pipeline architectu...'. Bands of components with no connectors between them - an architecture, not a process.

## Why the row is UNCERTAIN and not an E1 exclusion

Re-opening the figure in the audit shows what my first-pass note understated: the stages inside each band are chained by directed arrows, and the stage names are activities performed in order (collect, clean, analyse, engineer, train, evaluate), ending in an output. The band headings are what made me code it as a layered architecture; the arrows and the verb labels are what make a BPMN reader see a process. I cannot name a notation that settles it, so UNCERTAIN is the honest verdict, and the question is the one the researcher must answer.

## AI evidence (why this is not an E2 exclusion)

AI is inside the drawn chain rather than mentioned beside it: the sequence ends in 'Model Training', 'Model Evaluation' and 'Prediction Output', i.e. the machine learning pipeline itself, and the page's AI vocabulary is 'machine learning|predictive' on an article titled 'From data to prediction: Building a robust predictive analytics pipeline' whose premise is verbatim "Predictive analytics has quickly become a cornerstone of modern applications- powering everything from customer churn forecasting to equipment failure detection."

## Notes for the researcher

- This row was first coded `E0-no-artefact` with `judgment: false` by the census pass, then recoded `E1-not-bpmn` with `judgment: true` (a drawn non-BPMN diagram is a notation call: CLAUDE.md sec 3, prompts/02b), and then flipped to `UNCERTAIN` by the self-audit that `prompts/02_source-census.md` step 3 asks for over the judgment rows. The ledger keeps all three rows for this `n`; the `supersedes_row` row is the one that counts (tools/audit.py: the last row for an `n` wins).
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
