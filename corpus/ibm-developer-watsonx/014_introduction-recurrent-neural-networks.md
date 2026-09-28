---
n: 1649
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Introduction to recurrent neural networks (Learning Path: Supervised deep learning) - the 'Flowchart of the genetic algorithm process' figure"
url: https://developer.ibm.com/learningpaths/supervised-deep-learning/recurrent-neural-networks/introduction-recurrent-neural-networks/
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "The page's figure5.png is titled by its own alt text a 'Flowchart of the genetic algorithm process' and its four boxes carry the ordered steps of that algorithm - but the boxes are joined by no connectors whatsoever (no arrows, no decision diamonds, no terminators). Is a connector-less stack of ordered step boxes a process artefact the corpus records, or does E0-no-artefact exclude it because no flow is drawn?"
needs_visual_check: false
bpmn_evidence: "png, the page's own figure5.png fetched and viewed at full size (contact sheet SHEET_VIEW07, row 4 col 3). four white text boxes stacked on a black ground, each holding one step of a genetic algorithm: 'Create random population of candidate solutions', 'Test each candidate solution in the population and record its fitness', 'For each child in the new population, select two parents based upon their fitness', 'Combine each parent into a child, applying crossover and mutation operations per defined probabilities'. The page's own alt text calls the figure a 'Flowchart of the genetic algorithm process', but at full size the four boxes are joined by no connectors at all - no arrows, no decision shapes, no events. The page asserts a process artefact; I can name neither a flowchart notation nor a BPMN one in what is drawn, and hesitation resolves to UNCERTAIN."
bpmn_evidence_quote: "Flowchart of the genetic algorithm process"
ai_evidence: "the page's subject is AI (recurrent neural networks) and the figure steps through a genetic algorithm, i.e. the search process behind a learning method, but no AI element is drawn inside the four step boxes: they name only populations, solutions, parents and crossover. The page states verbatim 'Because RNNs include loops, they can store information while processing new input.' UNCERTAIN because the page calls the figure a flowchart while the boxes are joined by no connectors at all."
ai_evidence_quote: "Flowchart of the genetic algorithm process"
artefacts:
  screenshot: 014_1649X_figure5.png
  assets: [014_1649X_figure5.png]
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

`https://developer.ibm.com/learningpaths/supervised-deep-learning/recurrent-neural-networks/introduction-recurrent-neural-networks/` (html, ledger row n=1649), figure `figs/1649X_figure5`.

## What the figure shows



## Why the row is UNCERTAIN

png, the page's own figure5.png fetched and viewed at full size (contact sheet SHEET_VIEW07, row 4 col 3). four white text boxes stacked on a black ground, each holding one step of a genetic algorithm: 'Create random population of candidate solutions', 'Test each candidate solution in the population and record its fitness', 'For each child in the new population, select two parents based upon their fitness', 'Combine each parent into a child, applying crossover and mutation operations per defined probabilities'. The page's own alt text calls the figure a 'Flowchart of the genetic algorithm process', but at full size the four boxes are joined by no connectors at all - no arrows, no decision shapes, no events. The page asserts a process artefact; I can name neither a flowchart notation nor a BPMN one in what is drawn, and hesitation resolves to UNCERTAIN.

## AI evidence (why this is not an E2 exclusion)

the page's subject is AI (recurrent neural networks) and the figure steps through a genetic algorithm, i.e. the search process behind a learning method, but no AI element is drawn inside the four step boxes: they name only populations, solutions, parents and crossover. The page states verbatim "Because RNNs include loops, they can store information while processing new input." UNCERTAIN because the page calls the figure a flowchart while the boxes are joined by no connectors at all.

## Notes for the researcher

- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
