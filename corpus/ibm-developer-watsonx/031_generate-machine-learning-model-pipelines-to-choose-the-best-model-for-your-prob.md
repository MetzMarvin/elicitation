---
n: 1381
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Generate machine learning model pipelines with AutoAI - the 'Pipeline comparison' / 'Progress map' views, which draw each generated pipeline as an ordered node-link graph"
url: https://developer.ibm.com/tutorials/generate-machine-learning-model-pipelines-to-choose-the-best-model-for-your-problem-autoai/
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "The page's 'Pipeline comparison' figure draws each generated pipeline as an ordered node-link graph - 'Read dataset' -> 'Split holdout data' -> 'Read training data' -> 'Preprocessing' -> 'Model selection' -> 'XGB Classifier' / 'Snap Random Forest Classifier' -> 'Hyperparameter optimization' -> 'Feature engineering' -> 'Hyperparameter optimization', with the eight pipelines labelled P1 to P8 - so AI model nodes (the classifiers and the hyperparameter-optimization stages) sit inside a drawn, ordered process. The drawing is the tool's own progress map, not a modeller canvas, so it is neither an authored flow definition (like the Node-RED / DataStage / SPSS Modeler canvases excluded elsewhere in this census as E1) nor a BPMN 2.0 model: is an AutoAI-generated pipeline progress map within the artefact criteria (a process model in a proprietary notation, hence a corpus item), or a tool-generated progress visualisation that E1-not-bpmn excludes?"
needs_visual_check: false
bpmn_evidence: "png (tiled on the sweep sheet for gaps 276:300, figs/SHEET_SWEEP27601-27606 and 27604; viewed at full size on figs/SHEET_SHEET_ZS190101). the drawn figure appears in three successive console captures - 'Relationship map 1', 'Hovering over map', 'Progress map' and 'Pipeline comparison' (autoai-09, -10, -11, -13) - and in each of the last two the eight candidate pipelines are drawn as node-link graphs: the shared prefix 'Read dataset' -> 'Split holdout data' -> 'Read training data' -> 'Preprocessing' -> 'Model selection', then per-pipeline branches through 'XGB Classifier' or 'Snap Random Forest Classifier' to 'Feature engineering' and 'Hyperparameter optimization' nodes labelled P1-P8, beside a radial 'Relationship map' score chart and the 'Pipeline leaderboard' table (Pipeline 1-8, XGB Classifier / Snap Random Forest Classifier, accuracy 0.742-0.763, enhancements HPO-1, FE, HPO-2, build time). The page's other 43 figures are Watson Studio, Cloud Object Storage and Watson Machine Learning console captures of the same click-through."
bpmn_evidence_quote: "It automatically prepares your data for modeling, chooses the best algorithm for your problem, and creates pipelines for the trained models"
ai_evidence: "AI elements are inside the drawn figure: the graph's nodes are AI model-building stages - 'XGB Classifier' and 'Snap Random Forest Classifier' selection, 'Feature engineering' and two 'Hyperparameter optimization' stages per pipeline, with the eight pipelines labelled P1 to P8 - and the page describes the process verbatim: 'It automatically prepares your data for modeling, chooses the best algorithm for your problem, and creates pipelines for the trained models.' That is why the row is UNCERTAIN rather than excluded: the AI pipeline is drawn as an ordered, connected graph of named stages, but the drawing is the AutoAI service's own progress map of pipelines it generated, so it is neither an authored flow definition (the Node-RED, DataStage, Pentaho and SPSS Modeler canvases excluded elsewhere in this census) nor a BPMN 2.0 model."
ai_evidence_quote: "It automatically prepares your data for modeling, chooses the best algorithm for your problem, and creates pipelines for the trained models"
artefacts:
  screenshot: 031_1381X_autoai-13.png
  assets: [031_1381X_autoai-13.png]
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

`https://developer.ibm.com/tutorials/generate-machine-learning-model-pipelines-to-choose-the-best-model-for-your-problem-autoai/` (api, ledger row n=1381), figure `figs/1381X_autoai-13`.

## What the figure shows



## Why the row is UNCERTAIN

png (tiled on the sweep sheet for gaps 276:300, figs/SHEET_SWEEP27601-27606 and 27604; viewed at full size on figs/SHEET_SHEET_ZS190101). the drawn figure appears in three successive console captures - 'Relationship map 1', 'Hovering over map', 'Progress map' and 'Pipeline comparison' (autoai-09, -10, -11, -13) - and in each of the last two the eight candidate pipelines are drawn as node-link graphs: the shared prefix 'Read dataset' -> 'Split holdout data' -> 'Read training data' -> 'Preprocessing' -> 'Model selection', then per-pipeline branches through 'XGB Classifier' or 'Snap Random Forest Classifier' to 'Feature engineering' and 'Hyperparameter optimization' nodes labelled P1-P8, beside a radial 'Relationship map' score chart and the 'Pipeline leaderboard' table (Pipeline 1-8, XGB Classifier / Snap Random Forest Classifier, accuracy 0.742-0.763, enhancements HPO-1, FE, HPO-2, build time). The page's other 43 figures are Watson Studio, Cloud Object Storage and Watson Machine Learning console captures of the same click-through.

## AI evidence (why this is not an E2 exclusion)

AI elements are inside the drawn figure: the graph's nodes are AI model-building stages - 'XGB Classifier' and 'Snap Random Forest Classifier' selection, 'Feature engineering' and two 'Hyperparameter optimization' stages per pipeline, with the eight pipelines labelled P1 to P8 - and the page describes the process verbatim: "It automatically prepares your data for modeling, chooses the best algorithm for your problem, and creates pipelines for the trained models." That is why the row is UNCERTAIN rather than excluded: the AI pipeline is drawn as an ordered, connected graph of named stages, but the drawing is the AutoAI service's own progress map of pipelines it generated, so it is neither an authored flow definition (the Node-RED, DataStage, Pentaho and SPSS Modeler canvases excluded elsewhere in this census) nor a BPMN 2.0 model.

## Notes for the researcher

- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
