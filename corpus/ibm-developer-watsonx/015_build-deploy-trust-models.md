---
n: 1744
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Build, deploy, and trust models (Learning Path: Get started with Watson Studio) - the 'Steps to model workflow' figure"
url: https://developer.ibm.com/learningpaths/get-started-watson-studio/build-deploy-trust-models/
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "The page's model-overflow.png is titled by its own alt text 'Steps to model workflow' and its three panels hold the ordered activities of an MLOps life cycle (Build: create a project, add and prepare data, build an experiment or flow ...; Deploy: organize assets, deploy and score models, monitor ...; Trust: evaluate for bias or drift, retrain, update ...). The panels are joined by no connectors - no arrows, no events, no gateways. Does the corpus record this stage-panel figure as a process artefact, or does E0-no-artefact exclude it because no flow is drawn?"
needs_visual_check: false
bpmn_evidence: "png, the page's own model-overflow.png fetched and viewed at full size (contact sheet SHEET_VIEW08, row 1 col 4). three stacked panels on a white ground, each with a solid blue header bar - 'Build', 'Deploy', 'Trust' - and a bulleted list of activities inside: Build ('Create a project for organizing assets', 'Add and prepare data', 'Build an experiment or flow', 'View your data in a dashboard'), Deploy ('Organize your assets in a deployment space', 'Deploy and score models and functions', 'Monitor deployments in a dashboard'), Trust ('Evaluate your deployments for bias or drift', 'Retrain when certain thresholds are met', 'Update your deployments to maintain accuracy'). The panels hold ordered activities and the page's own alt text calls the figure 'Steps to model workflow', but the three panels are joined by no connectors at all. Hesitation resolves to UNCERTAIN."
bpmn_evidence_quote: "Steps to model workflow"
ai_evidence: "the page's subject is AI model life-cycle management and the figure's 'Trust' panel names the AI-specific activities ('Evaluate your deployments for bias or drift', 'Retrain when certain thresholds are met'), so AI work sits inside the stage panels. The page states verbatim 'Typically, there are several techniques that can be applied, and some techniques have specific requirements regarding the data that is available.' UNCERTAIN because the three panels hold ordered activities but are joined by no connectors."
ai_evidence_quote: "Steps to model workflow"
artefacts:
  screenshot: 015_1744X_model-overflow.png
  assets: [015_1744X_model-overflow.png]
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

`https://developer.ibm.com/learningpaths/get-started-watson-studio/build-deploy-trust-models/` (html, ledger row n=1744), figure `figs/1744X_model-overflow`.

## What the figure shows



## Why the row is UNCERTAIN

png, the page's own model-overflow.png fetched and viewed at full size (contact sheet SHEET_VIEW08, row 1 col 4). three stacked panels on a white ground, each with a solid blue header bar - 'Build', 'Deploy', 'Trust' - and a bulleted list of activities inside: Build ('Create a project for organizing assets', 'Add and prepare data', 'Build an experiment or flow', 'View your data in a dashboard'), Deploy ('Organize your assets in a deployment space', 'Deploy and score models and functions', 'Monitor deployments in a dashboard'), Trust ('Evaluate your deployments for bias or drift', 'Retrain when certain thresholds are met', 'Update your deployments to maintain accuracy'). The panels hold ordered activities and the page's own alt text calls the figure 'Steps to model workflow', but the three panels are joined by no connectors at all. Hesitation resolves to UNCERTAIN.

## AI evidence (why this is not an E2 exclusion)

the page's subject is AI model life-cycle management and the figure's 'Trust' panel names the AI-specific activities ('Evaluate your deployments for bias or drift', 'Retrain when certain thresholds are met'), so AI work sits inside the stage panels. The page states verbatim "Typically, there are several techniques that can be applied, and some techniques have specific requirements regarding the data that is available." UNCERTAIN because the three panels hold ordered activities but are joined by no connectors.

## Notes for the researcher

- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
