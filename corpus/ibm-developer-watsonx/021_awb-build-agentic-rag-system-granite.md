---
n: 931
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Build an agentic RAG system with IBM Granite - the 'Multi-agent RAG architecture' figure (a High Level Planner feeding a numbered Execution Loop of four agents)"
url: https://developer.ibm.com/tutorials/awb-build-agentic-rag-system-granite/
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "The page's first figure is a multi-agent RAG pipeline: a 'High Level Planner' feeding a dashed 'Execution Loop' that numbers its steps ('1. Research Assistant Agent', '2. Summarizer Agent', '3. Critic Agent', '4. Reflection Agent'), with a loop back to step 1, a 'Tool Call' path down to an 'Executor' and 'Output from all steps' running to a 'Report Generator' - ordered, numbered activity steps joined by arrows. Its boxes are AI agents, so it can be read as an architecture (the page's own alt texts call its two figures 'Multi-agent RAG architecture' and 'Architecture diagram ...'); its numbered connectors order the work, so it can be read as a process. Should this figure enter the corpus, and if so under which reading?"
needs_visual_check: false
bpmn_evidence: "png, the page's own figure at full size (SHEET_Z0701, fourth tile; contact sheet SHEET_GAP0701, row 3 col 6). a 'High Level Planner' box feeding a dashed 'Execution Loop' boundary that holds four numbered steps - '1. Research Assistant Agent', '2. Summarizer Agent', '3. Critic Agent', '4. Reflection Agent' - with a looping arrow back to step 1, a 'Tool Call' path down to an 'Executor' box, and 'Output from all steps' running to a 'Report Generator'. The page's other figure is an architecture diagram of the same agents ('Open WebUI, AG2 Python agent, document search tool, web search tool, and Ollama serving IBM Granite 3.2')."
bpmn_evidence_quote: "Artificial intelligence (AI) agents are generative AI (gen AI) systems or programs capable of autonomously designing and executing task workflows using available tools."
ai_evidence: "AI elements are inside the drawn figure and the page is explicit that the agentic system is generative AI: the execution loop is worked by a 'Research Assistant Agent', a 'Summarizer Agent', a 'Critic Agent' and a 'Reflection Agent' (an earlier step in the same flow instructs the reader to 'create a new agent'), and the page states its premise verbatim: 'Artificial intelligence (AI) agents are generative AI (gen AI) systems or programs capable of autonomously designing and executing task workflows using available tools.' That is why the row is UNCERTAIN rather than excluded: the AI work is inside the drawn pipeline, but the notation the pipeline is drawn in is a vendor house style, and the page's own alt text calls it an 'architecture'."
ai_evidence_quote: "Artificial intelligence (AI) agents are generative AI (gen AI) systems or programs capable of autonomously designing and executing task workflows using available tools."
artefacts:
  screenshot: 021_931_Screenshot_202024-12-16_20at_208-52-26_E2_80_AFPM.png
  assets: [021_931_Screenshot_202024-12-16_20at_208-52-26_E2_80_AFPM.png]
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

`https://developer.ibm.com/tutorials/awb-build-agentic-rag-system-granite/` (api, ledger row n=931), figure `figs/931_Screenshot_202024-12-16_20at_208-52-26_E2_80_AFPM`.

## What the figure shows



## Why the row is UNCERTAIN

png, the page's own figure at full size (SHEET_Z0701, fourth tile; contact sheet SHEET_GAP0701, row 3 col 6). a 'High Level Planner' box feeding a dashed 'Execution Loop' boundary that holds four numbered steps - '1. Research Assistant Agent', '2. Summarizer Agent', '3. Critic Agent', '4. Reflection Agent' - with a looping arrow back to step 1, a 'Tool Call' path down to an 'Executor' box, and 'Output from all steps' running to a 'Report Generator'. The page's other figure is an architecture diagram of the same agents ('Open WebUI, AG2 Python agent, document search tool, web search tool, and Ollama serving IBM Granite 3.2').

## AI evidence (why this is not an E2 exclusion)

AI elements are inside the drawn figure and the page is explicit that the agentic system is generative AI: the execution loop is worked by a 'Research Assistant Agent', a 'Summarizer Agent', a 'Critic Agent' and a 'Reflection Agent' (an earlier step in the same flow instructs the reader to 'create a new agent'), and the page states its premise verbatim: "Artificial intelligence (AI) agents are generative AI (gen AI) systems or programs capable of autonomously designing and executing task workflows using available tools." That is why the row is UNCERTAIN rather than excluded: the AI work is inside the drawn pipeline, but the notation the pipeline is drawn in is a vendor house style, and the page's own alt text calls it an 'architecture'.

## Notes for the researcher

- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
