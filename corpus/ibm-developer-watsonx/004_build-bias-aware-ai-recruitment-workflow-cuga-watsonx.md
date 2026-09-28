---
n: 35
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Create a bias-aware AI recruitment workflow with CUGA - the 'CUGA HR Screening Architecture' figure: a five-agent screening pipeline with a human review gate"
url: https://developer.ibm.com/tutorials/build-bias-aware-ai-recruitment-workflow-cuga-watsonx/
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "The figure 'CUGA HR Screening' is drawn as a process: Input and Output panels, an Orchestrator that fans out to five numbered agent steps in sequence (Resume Parser, Bias Guard, Job Matcher, Shortlist, Email Draft) joined by solid arrows, a red decision diamond 'Human Review' with the labelled branch 'Approved', a second panel of five numbered policy layers wired in with dashed lines, and a legend of three arrow types ('Data Flow', 'Policy Enforcement', 'Output Distribution'). It has no BPMN events, no BPMN task types, no gateways beyond the diamond and no pool/lane with BPMN semantics, and the page's own alt text calls it an 'Architecture'. Is this a BPMN 2.0 model drawn in the vendor's house style (so it belongs in the corpus), or a proprietary vendor illustration that E1-not-bpmn excludes?"
needs_visual_check: false
bpmn_evidence: "png (zoomed at full size). agent pipeline with a decision diamond and a labelled branch; sequence solid arrows, policy enforcement dashed; page calls it an Architecture."
bpmn_evidence_quote: "CUGA HR Screening Architecture"
ai_evidence: "the page is an AI tutorial and its AI content surrounds the figure: the process it draws is a pipeline of five AI agents (a CV-screening agent, a bias-detection agent, an explainability agent and so on) with a human-review gate, and the page states its AI premise verbatim: 'Organizations are increasingly using AI to screen resumes, rank candidates, and accelerate recruitment.' That is why the row is UNCERTAIN rather than excluded: the AI is inside the drawn pipeline, but the notation the pipeline is drawn in is not BPMN 2.0."
ai_evidence_quote: "CUGA HR Screening Architecture"
artefacts:
  screenshot: 004_35_CUGA_HR_Screening.png
  assets: [004_35_CUGA_HR_Screening.png]
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

`https://developer.ibm.com/tutorials/build-bias-aware-ai-recruitment-workflow-cuga-watsonx/` (api, ledger row n=35), figure `figs/35_CUGA_HR_Screening`.

## What the figure shows



## Why the row is UNCERTAIN

png (zoomed at full size). agent pipeline with a decision diamond and a labelled branch; sequence solid arrows, policy enforcement dashed; page calls it an Architecture.

## AI evidence (why this is not an E2 exclusion)

the page is an AI tutorial and its AI content surrounds the figure: the process it draws is a pipeline of five AI agents (a CV-screening agent, a bias-detection agent, an explainability agent and so on) with a human-review gate, and the page states its AI premise verbatim: "Organizations are increasingly using AI to screen resumes, rank candidates, and accelerate recruitment." That is why the row is UNCERTAIN rather than excluded: the AI is inside the drawn pipeline, but the notation the pipeline is drawn in is not BPMN 2.0.

## Notes for the researcher

- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
