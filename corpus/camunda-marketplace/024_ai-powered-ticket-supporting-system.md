---
n: 24
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: AI-Powered Ticket Supporting System
url: https://marketplace.camunda.com/apps/613092/ai-powered-ticket-supporting-system
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: Camunda Web Modeler canvas published as a listing asset; no .bpmn downloadable. Read natively: start event 'Ticket Created', two exclusive gateways (one labelled 'Action Needed?'), an ad-hoc sub-process (tilde marker), an end event 'Ticket closed'.
bpmn_evidence_quote: "Action Needed?"
ai_evidence: The service task 'Work on the ticket' carries the violet four-pointed-star AI-agent glyph; four tasks carry the OpenAI connector glyph ('Summarize the ticket content' in the main flow, and inside the ad-hoc sub-process 'Give a set of questions', 'Pick the most relevant ticket', 'Summarize the ticket content'). The page's own features list reads 'AI-powered ticket summaries', 'AI-driven knowledge retrieval', 'Human-AI collaboration'.
ai_evidence_quote: "AI-powered ticket summaries"
artefacts:
  screenshot: 024_ai-powered-ticket-supporting-system.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own overview asset; native read at 1100x511
---

## What the page shows

An AI ticket-support process. A ticket is created, the service task 'Summarize the ticket content' summarises it (OpenAI glyph), a gateway decides whether the AI can act: 'Work on the ticket' (AI-agent glyph) then 'Action Needed?'. If not needed, a human engineer closes it ('L3 engineer to close the ticket') and the outcome is stored in the knowledge base. If needed, an ad-hoc sub-process runs the AI-and-human loop: post a question in Clickup, the engineer posts answers, the agent reads the comment, checks and picks from the knowledge base, summarises, posts the solution as a comment, and the engineer reviews it.

## Observations (description only, no interpretation)

- **AI activity - function:** the page says the system 'summarizes and validates tickets, retrieves relevant knowledge, and enriches the database with every resolved issue'.
- **AI activity - element type:** OpenAI-bound `serviceTask`s plus one AI-agent `serviceTask` ('Work on the ticket'), grouped in an `adHocSubProcess`.
- **Authority - downstream:** 'Store in the knowledge base', 'Post the question in Clickup', 'Post the solution as comment' - the AI writes to a knowledge base and a ticketing tool.
- **Authority - data:** the knowledge base (read and write), the ticket record.
- **Authority - control:** the two exclusive gateways ('Action Needed?') and the human decisions 'Engineer to post the answers', 'Engineer to work on the ticket', 'Engineer to review the comment', 'L3 engineer to close the ticket'.
- **Input provenance:** the ticket content.
- **Guards present:** four human steps inside the loop, including 'Engineer to review the comment' after the agent posts its solution.
- **Prompt / model detail visible:** not visible on the page.

## Notes for the researcher

By Acheron ('Listing Only' partner accelerator); the page links a demo video and a GitHub blueprint repo (Acheron-Camunda/Camunda-MS-AI-Agent-Blueprint), which would carry the .bpmn, but the listing itself publishes only the diagram asset.
