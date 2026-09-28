---
n: 77
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Embeddings Vector Database Connector
url: https://marketplace.camunda.com/apps/522490/embeddings-vector-database-connector
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: BPMN diagram published as the listing's overview asset (Camunda Web Modeler canvas with the element-template glyphs, free-text annotations and a large expanded sub-process); no .bpmn downloadable. Read natively: start event 'Conversation Received', exclusive gateways, message throw/catch events, a large sub-process labelled 'Tools available to AI agent', and end events 'Case closed' and 'Conversation handled by human'.
bpmn_evidence_quote: "Tools available to AI agent"
ai_evidence: Violet four-pointed-star element-template glyphs (Camunda's agentic-AI template) sit on 'Agent as a Judge', on the memory tasks 'Fetch past conversations from customer' and 'Save customer interaction in long term memory', and on 'Query knowledge base' and 'Save answer in knowledge base' inside the tools sub-process; a further instance appears in the pink 'Human controlled request' path. The page states the connector 'works seamlessly with the AI Agent connector to provide RAG capabilities' and is for 'long-term conversational memory, Retrieval-Augmented Generation (RAG), and semantic search'.
ai_evidence_quote: "The Vector Database connector works seamlessly with the AI Agent connector to provide RAG capabilities"
artefacts:
  screenshot: 077_embeddings-vector-database-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own overview asset (d3bql97l1ytoxn.cloudfront.net, overview/img12724063186157673844-2x.png, 1100x443); native read at full size
---

## What the page shows

Camunda's own Embeddings Vector Database connector listing (8.8, Camunda Connectors Bundle). The page describes bidirectional access to vector stores (Elasticsearch, OpenSearch) so that processes and AI agents can write embeddings and retrieve relevant chunks at runtime. Its published diagram is the AI email-support blueprint: a conversation is received, past conversations are fetched from long-term memory, the request is handled ('Handle customer request'), a 'User solved?' gateway routes to an AI 'Agent as a Judge' with 'needs review' / 'needs human review' paths, the knowledge base is read and written, and a human specialist can take over ('Ask loan specialist', 'Handle request' in the 'Human controlled request' path).

## Observations (description only, no interpretation)

- **AI activity - function:** memory retrieval for an agent, knowledge-base question answering, and judging the agent's answer ('Agent as a Judge').
- **AI activity - element type:** tasks carrying the violet AI-agent element-template glyph, including inside the expanded sub-process 'Tools available to AI agent'; the vector-store operations are the tasks named after long-term memory and the knowledge base.
- **Authority - downstream:** the email reply path ('Ask customer via email', 'Customer responded'), the knowledge base, and the human path 'Finalize case manually' / 'Handle request' in the 'Human controlled request' sub-process.
- **Authority - data:** the vector store (write on 'Save customer interaction in long term memory', 'Save answer in knowledge base'; read on 'Fetch past conversations from customer', 'Query knowledge base').
- **Authority - control:** the 'User solved?' gateway, the 'Agent as a Judge' review split ('needs review' / 'needs human review'), and the human sub-process; annotations read 'Can be integrated into ad hoc subprocess with 8.8', 'Use long term memory...' and 'Store long term memory in the long term memory'.
- **Input provenance:** the inbound conversation ('Conversation Received') and the customer's email answers.
- **Guards present:** the judging agent, the 'needs human review' branch, the human-controlled request path, and 'Final answer to customer and close support' as the terminal AI path.
- **Prompt / model detail visible:** none visible in the diagram; the page links the vector-database connector documentation.

## Notes for the researcher

The published diagram is the same blueprint whose .bpmn this census read at n=006 (Camunda's AI Email Support Agent: 'Handle customer request', 'Agent as a Judge', 'Ask loan specialist'), but it is a different published artefact - a different image (1100x443 against n=006's 1100x353, ~13% of resampled pixels differing) on a different listing - so it is recorded on its own rather than as an E3-duplicate of n=006; the researcher may still want to reconcile the two. It is the clearest example in this source of the vector-database connector's own AI-agent usage.
