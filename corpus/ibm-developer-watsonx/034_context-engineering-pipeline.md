---
n: 261
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Build context-aware AI agents with IBM BeeAI"
url: https://developer.ibm.com/articles/context-engineering-pipeline/
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: "The page's own alt text calls its figure an eight-stage context diagram, and the page is about context engineering for AI agents, but the stages are drawn inside mobile-app screens in the vendor's house style: does an eight-stage LLM-context stage diagram count as a BPMN-shaped process artefact for the corpus, or is it an in-app illustration of the pipeline's stages?"
needs_visual_check: false
bpmn_evidence: "I cannot show the figure is not a process. Its alt text asserts ordered stages ('Diagram showing the eight-stage context ...') and the page's subject is the LLM context pipeline those stages belong to, so a reader who takes the alt text at its word sees an ordered stage sequence with an LLM element, drawn in a style that is neither BPMN 2.0 nor a convention I can name with certainty."
bpmn_evidence_quote: "Prompt engineering helped with what to say to the model."
ai_evidence: "AI is inside the artefact's subject rather than merely alongside it: the figure's stages are the context-handling steps of an LLM agent, and the page's own AI vocabulary is 'AI|LLM|LLMs|NLP|agentic|machine learning|watsonx.ai' over a tutorial titled 'Build context-aware AI agents with IBM BeeAI'. So the row is UNCERTAIN rather than an E2 exclusion: nothing here rests on the absence of an AI element."
ai_evidence_quote: "Prompt engineering helped with what to say to the model."
artefacts:
  screenshot: 034_261_context-flow-stages.png
  assets: [034_261_context-flow-stages.png]
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

`https://developer.ibm.com/articles/context-engineering-pipeline/` (ledger row n=261), figure `figs/261_context-flow-stages.png`.

## What the figure shows

three mobile-app screenshots, each with a small embedded diagram and chat text; alt text 'Diagram showing the eight-stage context ...'. The images are app screens, not a drawn process.

## Why the row is UNCERTAIN and not an E1 exclusion

I cannot show the figure is not a process. Its alt text asserts ordered stages ('Diagram showing the eight-stage context ...') and the page's subject is the LLM context pipeline those stages belong to, so a reader who takes the alt text at its word sees an ordered stage sequence with an LLM element, drawn in a style that is neither BPMN 2.0 nor a convention I can name with certainty.

## AI evidence (why this is not an E2 exclusion)

AI is inside the artefact's subject rather than merely alongside it: the figure's stages are the context-handling steps of an LLM agent, and the page's own AI vocabulary is 'AI|LLM|LLMs|NLP|agentic|machine learning|watsonx.ai' over a tutorial titled 'Build context-aware AI agents with IBM BeeAI'. So the row is UNCERTAIN rather than an E2 exclusion: nothing here rests on the absence of an AI element.

## Notes for the researcher

- This row was first coded `E0-no-artefact` with `judgment: false` by the census pass, then recoded `E1-not-bpmn` with `judgment: true` (a drawn non-BPMN diagram is a notation call: CLAUDE.md sec 3, prompts/02b), and then flipped to `UNCERTAIN` by the self-audit that `prompts/02_source-census.md` step 3 asks for over the judgment rows. The ledger keeps all three rows for this `n`; the `supersedes_row` row is the one that counts (tools/audit.py: the last row for an `n` wins).
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
