---
n: 190
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: AI Process Analysis & Optimization Agent
url: https://marketplace.camunda.com/apps/784361/ai-process-analysis-optimization-agent
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: The page describes an AI agent that continuously analyses process execution data and can 'trigger improvement workflows, propose configuration changes, or escalate insights', but the listing publishes no artefact of it: it is marked 'Listing Only', there is no .bpmn and no screenshot of the agent, and its only process image is a Modeler capture of a different, non-AI banking-routing process (whose versions panel merely lists an agent version). Is a described-but-unpublished AI agent blueprint enough to record this listing, or is it E0-no-artefact? Same question as the Ollama connector (n=058), the GCP Document AI connector (n=116), the Taktile agent (n=166) and this batch's n=185.
needs_visual_check: true
bpmn_evidence: No BPMN artefact of the described agent published. The catalogue marks the entry 'Listing Only'; there is no .bpmn link and the screenshots list is empty. The listing's only process image is a Camunda Modeler capture of a different model - project '1-BankingSupportAgent > Human Banking Support', canvas 'Human Banking Support (Main process)': 'inquiry received' -> userTask 'Distribute assembly' -> gateway -> 'Accounting' / 'Legal' / 'Loan' / 'Others' -> gateway -> end - whose versions panel lists 'Partially Automated Banking Support Agent' (request review) and 'Fully Manual Support Process' (approved). Its only other image is the 'mpmx' wordmark, and its only demonstration resource is a YouTube demo, not opened.
bpmn_evidence_quote: "Listing Only"
ai_evidence: The page describes the agent and its reach in detail: 'This blueprint demonstrates how AI agents can continuously analyze, evaluate, and optimize business processes orchestrated in Camunda. The AI agent monitors process execution data, evaluates performance metrics, identifies bottlenecks, detects anomalies, and generates optimization recommendations. It can trigger improvement workflows, propose configuration changes, or escalate insights to process owners.' Features: 'AI-generated recommendations', 'Closed-loop orchestration', 'Governed human oversight'.
ai_evidence_quote: "The AI agent monitors process execution data, evaluates performance metrics, identifies bottlenecks"
artefacts:
  screenshot: 190_ai-process-analysis-optimization-agent.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1100
capture_method: curl of the listing's own assets (d3bql97l1ytoxn.cloudfront.net, app_resources/784361/overview/img4282525478786844390-2x.png, 1100x540, and img5921016034060292796-2x.png, the 'mpmx' wordmark); native read at full size - a Camunda Modeler capture with the versions panel open
---

## What the page shows

AI Process Analysis & Optimization Agent (mpmx.ai, 'Listing Only'). Described as a governed agent loop over process execution data: it monitors, detects bottlenecks and anomalies, recommends optimisations, and can open improvement workflows with human-in-the-loop validation.

## Observations (description only, no interpretation)

- **AI activity - function:** described as process mining plus recommendation - analysing execution data, detecting deviations, generating optimisation recommendations and triggering improvement workflows.
- **AI activity - element type:** not published. The listing's only process image shows an unrelated routing model ('Distribute assembly' to four departments), so no AI-bound element can be inspected.
- **Authority - downstream:** described as being able to trigger improvement workflows and propose configuration changes, with 'Governed human oversight' for 'advisory and semi-autonomous modes'.
- **Authority - data:** described as process execution data and performance indicators; nothing is published.
- **Authority - control:** described as 'Closed-loop orchestration'; not shown.
- **Authority - control (human):** claimed as a feature ('Governed human oversight', 'human-in-the-loop validation for all optimization actions'), not shown.
- **Input provenance:** process execution data of Camunda-orchestrated processes.
- **Guards present:** claimed as 'full auditability' and advisory/semi-autonomous modes; nothing published.
- **Prompt / model detail visible:** none - no model, provider, prompt or threshold appears on the page.

## Notes for the researcher

artefact inside a video; not opened per operator instruction 2026-09-26. Worth flagging for the researcher: the one published process image is *not* the agent - it is a Camunda Modeler view of a human support-routing process, and the only trace of the agent in it is a version row in the side panel ('Partially Automated Banking Support Agent'). Recorded UNCERTAIN rather than E0 because the page describes the agent's workings inside the process in its own words (the n=116/n=058 pattern).
