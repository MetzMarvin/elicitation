---
n: 1141
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Build an agentic RAG pipeline with CrewAI - the 'Agentic RAG system architecture' figure (four specialized agents in a CrewAI orchestration pipeline)"
url: https://developer.ibm.com/articles/agentic-rag-pipeline/
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "The page's only figure is drawn as an agent pipeline - a 'Products Retrievers' box and a 'Requirements Retriever' box at the left, a blue 'User' box, and a central orchestration region holding the agent cards 'Products Retrievers', 'Requirements Retriever', 'Question Generator', 'Answer Generator A', 'Answer Generator B' and 'Output / Consolidation' - with arrows between the parts carrying the labels 'subqueries', 'answers' and 'question'. The page's own alt text calls it an 'Agentic RAG system architecture showing four specialized agents - Products Retriever, Requirements Retriever, and two Answer Generators - connected through a CrewAI orchestration pipeline'. Is it a BPMN 2.0 model drawn in the vendor's house style (so it belongs in the corpus), or a proprietary agent-architecture illustration that E1-not-bpmn excludes?"
needs_visual_check: false
bpmn_evidence: "jpg (tiled on SHEET_ZS1101, row 1 col 1; viewed full size at 720x500 on SHEET_ZS1201). the page's only figure. Labels read off the figure at full size: left column 'LLM / Products Retrievers' and 'Requirements Retriever'; a blue rounded 'User' plate; the central rounded region contains the agent cards 'Products Retrievers', 'Requirements Retriever', 'Question Generator', 'Answer Generator A', 'Answer Generator B' and a 'Output / Consolidation' panel; the arrows between the parts are labelled 'subqueries', 'answers' and 'question', and one arrow leaves the figure to the right."
bpmn_evidence_quote: "Agentic RAG system architecture showing four specialized agents — Products Retriever, Requirements Retriever, and two Answer Generators — connected through a CrewAI orchestration pipeline"
ai_evidence: "AI elements are inside the drawn figure: its cards are named 'Products Retrievers', 'Requirements Retriever', 'Question Generator', 'Answer Generator A' and 'Answer Generator B' - the four specialized agents the page's own alt text counts - and the orchestration region they sit in is what that alt text calls a 'CrewAI orchestration pipeline'. The page's own alt text is verbatim 'Agentic RAG system architecture showing four specialized agents - Products Retriever, Requirements Retriever, and two Answer Generators - connected through a CrewAI orchestration pipeline', and the page's premise is verbatim 'Traditional RAG systems work in a linear pipeline: query encoding, vector similarity search, top-k document retrieval, and response generation.' That is why the row is UNCERTAIN rather than excluded: the AI agents are nodes the drawn flow passes through, but the notation is an architecture illustration of grouped agent cards, not BPMN 2.0."
ai_evidence_quote: "Agentic RAG system architecture showing four specialized agents — Products Retriever, Requirements Retriever, and two Answer Generators — connected through a CrewAI orchestration pipeline"
artefacts:
  screenshot: 026_1141X_agentic-rag-arch3.png
  assets: [026_1141X_agentic-rag-arch3.png]
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

`https://developer.ibm.com/articles/agentic-rag-pipeline/` (api, ledger row n=1141), figure `figs/1141X_agentic-rag-arch3`.

## What the figure shows



## Why the row is UNCERTAIN

jpg (tiled on SHEET_ZS1101, row 1 col 1; viewed full size at 720x500 on SHEET_ZS1201). the page's only figure. Labels read off the figure at full size: left column 'LLM / Products Retrievers' and 'Requirements Retriever'; a blue rounded 'User' plate; the central rounded region contains the agent cards 'Products Retrievers', 'Requirements Retriever', 'Question Generator', 'Answer Generator A', 'Answer Generator B' and a 'Output / Consolidation' panel; the arrows between the parts are labelled 'subqueries', 'answers' and 'question', and one arrow leaves the figure to the right.

## AI evidence (why this is not an E2 exclusion)

AI elements are inside the drawn figure: its cards are named 'Products Retrievers', 'Requirements Retriever', 'Question Generator', 'Answer Generator A' and 'Answer Generator B' - the four specialized agents the page's own alt text counts - and the orchestration region they sit in is what that alt text calls a 'CrewAI orchestration pipeline'. The page's own alt text is verbatim "Agentic RAG system architecture showing four specialized agents - Products Retriever, Requirements Retriever, and two Answer Generators - connected through a CrewAI orchestration pipeline", and the page's premise is verbatim "Traditional RAG systems work in a linear pipeline: query encoding, vector similarity search, top-k document retrieval, and response generation." That is why the row is UNCERTAIN rather than excluded: the AI agents are nodes the drawn flow passes through, but the notation is an architecture illustration of grouped agent cards, not BPMN 2.0.

## Notes for the researcher

- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
