---
n: 1610
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: "LLM Framework for UiPath Studio"
url: https://marketplace.uipath.com/listings/llm-framework-for-uipath-studio
accessed: 2026-09-28
verdict: UNCERTAIN
needs_human_ruling: true
question: "Informal box-and-icon process sketch (no BPMN shapes, events or gateways) of a queue-based transaction with an LLM 'Ask Agent' step, a prompt template and a human 'Review' in Action Center. Does it count as a BPMN diagram?"
needs_visual_check: false
bpmn_evidence: slide 'Quick Start Use Case - Transactional - Contracts Indemnification Review' with a box/icon flow (Orchestrator Contracts Queue -> Get Transaction -> Ingest Knowledge -> Ask Agent -> Answer -> Review -> Downstream Process); informal notation, not BPMN shapes; a small UiPath workflow thumbnail sits top-left
bpmn_evidence_quote: "Sample Implementation: Transaction Mode - Contracts Indemnification Review (Queues + LLM Framework)"
ai_evidence: flow nodes 'Ask Agent' and 'Ingest Knowledge' with a 'Prompt Template/Query' input; slide text on the LLM agent; config sheet names OpenAI/Anthropic LLM settings
ai_evidence_quote: "This template leverages custom Python API built on top of LangChain framework (standard framework for LLM app development)."
artefacts:
  screenshot: 012_llm-framework-for-uipath-studio.png
  archive: 012_llm-framework-for-uipath-studio.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: marginal
capture_width_px: 1273
capture_method: python urllib GET of the original marketplace-cdn.uipath.com asset (cdn-cgi resize wrapper stripped); 1273 px is the native size
---

## What the page shows

A Studio template ('LLM Framework for UiPath Studio') for LLM-powered automations. Its five images: a 'Solution Architecture' slide (Studio + LangChain, embeddings/vector storage, 'Goal Oriented LLM Agent with Thought Chain Output', Action Center 'Human in the Loop'), a conversational quick-start slide 'Chat With Your Data', the transactional quick-start slide 'Contracts Indemnification Review' (captured here), a 'Contextual LLM Interaction' infographic, and a configuration table. The transactional slide text reads: 'After the LLM agent is used to identify if an MSA document has one-sided or two-sided indemnification (with extracted excerpts from the contract) it will push to human for further review via the custom action center form.' The page also embeds 2 YouTube video(s), not opened (operator no-media rule 2026-09-26).

## Observations (description only, no interpretation)

- **AI activity - function:** 'Ask Agent' identifies 'if an MSA document has one-sided or two-sided indemnification (with extracted excerpts from the contract)' (slide text)
- **AI activity - element type:** a round icon node labelled 'Ask Agent' in an informal flow, fed by a 'Prompt Template/Query' box
- **Authority - downstream:** 'Answer' -> 'Review' (UiPath Action Center) -> 'Downstream Process'
- **Authority - data:** extracted excerpts from the contract; answer passed to review
- **Authority - control:** human 'Review' in Action Center after the agent's answer; 'Downstream Process' after review
- **Input provenance:** contracts from 'Contracts Queue' via 'Get Transaction'; 'Ingest Knowledge' of the contract document
- **Guards present:** 'it will push to human for further review via the custom action center form' (slide text); config rows 'ActionCenter_AlwaysValidate TRUE'
- **Prompt / model detail visible:** config table rows 'LLM_Model_Name' with value 'gpt-4-0613' and the description 'If provider is ANTHROPICCLAUDE, specify claude-2 here'; rows for OpenAI and Pinecone keys (values not reproduced here)

## Notes for the researcher

The configuration image published on the listing shows what look like real API key strings for OpenAI and Pinecone; they are deliberately not copied into this record. Two YouTube walkthrough videos are embedded, not opened. The 'Solution Architecture' slide also shows a UiPath process-template thumbnail too small to read.
