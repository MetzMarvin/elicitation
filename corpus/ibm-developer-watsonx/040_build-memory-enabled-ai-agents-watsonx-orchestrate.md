---
n: 404
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Build memory-enabled AI agents in watsonx Orchestrate"
url: https://developer.ibm.com/tutorials/build-memory-enabled-ai-agents-watsonx-orchestrate/
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: "The figure is captioned an architecture diagram but draws the numbered interaction of a watsonx Orchestrate 'Main Agent' whose sub-agents and reasoning steps (Disambiguation, Reasoning, Tool calling) hand work to MCP tools and back: an ordered agent interaction with numbered steps - process artefact or architecture?"
needs_visual_check: false
bpmn_evidence: "On re-opening the figure for this audit what I see is an ordered interaction: the Main Agent's sub-agent boxes and the numbered steps that carry work between the user panel, the agent and the tools. My first-pass note read the same boxes as the components of a platform architecture, and both readings are defensible on the drawing itself, so the row cannot stay an exclusion - agent routing drawn as numbered steps is precisely the shape prompts/02b tells the self-audit to surface."
bpmn_evidence_quote: "AI agents should provide personalized, context-aware experiences instead of treating every interaction as a new conversation."
ai_evidence: "AI is the actor of the drawn interaction, not a topic beside it: the boxes are a 'Main Agent' with its sub-agents and an MCP tool surface inside a watsonx Orchestrate panel, and the page's AI vocabulary is 'AI|agentic|watsonx Orchestrate' over the tutorial 'Build memory-enabled AI agents in watsonx Orchestrate'. The page's premise is verbatim 'AI agents should provide personalized, context-aware experiences instead of treating every interaction as a new conversation.' So the row is UNCERTAIN, never E2."
ai_evidence_quote: "AI agents should provide personalized, context-aware experiences instead of treating every interaction as a new conversation."
artefacts:
  screenshot: 040_404_image1.png
  assets: [040_404_image1.png]
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

`https://developer.ibm.com/tutorials/build-memory-enabled-ai-agents-watsonx-orchestrate/` (ledger row n=404), figure `figs/404_image1.png`.

## What the figure shows

an architecture: a user panel and an AI Platform panel holding watsonx Orchestrate, a 'Main Agent' with agent boxes (.x, Disambiguation, Reasoning, Tool calling), MCP and tools boxes; alt text 'Architecture diagram showing the watsonx...'.

## Why the row is UNCERTAIN and not an E1 exclusion

On re-opening the figure for this audit what I see is an ordered interaction: the Main Agent's sub-agent boxes and the numbered steps that carry work between the user panel, the agent and the tools. My first-pass note read the same boxes as the components of a platform architecture, and both readings are defensible on the drawing itself, so the row cannot stay an exclusion - agent routing drawn as numbered steps is precisely the shape prompts/02b tells the self-audit to surface.

## AI evidence (why this is not an E2 exclusion)

AI is the actor of the drawn interaction, not a topic beside it: the boxes are a 'Main Agent' with its sub-agents and an MCP tool surface inside a watsonx Orchestrate panel, and the page's AI vocabulary is 'AI|agentic|watsonx Orchestrate' over the tutorial 'Build memory-enabled AI agents in watsonx Orchestrate'. The page's premise is verbatim "AI agents should provide personalized, context-aware experiences instead of treating every interaction as a new conversation." So the row is UNCERTAIN, never E2.

## Notes for the researcher

- This row was first coded `E0-no-artefact` with `judgment: false` by the census pass, then recoded `E1-not-bpmn` with `judgment: true` (a drawn non-BPMN diagram is a notation call: CLAUDE.md sec 3, prompts/02b), and then flipped to `UNCERTAIN` by the self-audit that `prompts/02_source-census.md` step 3 asks for over the judgment rows. The ledger keeps all three rows for this `n`; the `supersedes_row` row is the one that counts (tools/audit.py: the last row for an `n` wins).
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
