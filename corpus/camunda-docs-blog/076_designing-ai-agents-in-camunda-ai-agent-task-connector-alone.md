---
n: 381
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: "Designing AI Agents in Camunda: The AI Agent Task Connector Standing Alone"
url: https://camunda.com/blog/2025/11/designing-ai-agents-in-camunda-ai-agent-task-connector-alone/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "the visual pass reads the captured figure as class 'bpmn': 'Summarize Results', 'Review Upsell AI Agent Results' tasks; the page names BPMN itself: 'In the following excerpt from a BPMN model, we have used a single AI Agent Task connector to summarize results'"
bpmn_evidence_quote: "In the following excerpt from a BPMN model, we have used a single AI Agent Task connector to summarize results from something then using that"
ai_evidence: "the page binds AI to a process element (AI Agent Task, Anthropic/Claude): 'Designing AI Agents in Camunda: The AI Agent Task Connector Standing Alone'; the contact-sheet pass reads the captured figure as ai_visible=yes"
ai_evidence_quote: "Designing AI Agents in Camunda: The AI Agent Task Connector Standing Alone"
artefacts:
  screenshot: 076_designing-ai-agents-in-camunda-ai-agent-task-connector-alone.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: marginal
capture_width_px: 252
capture_method: figure downloaded at w=1400 from the asset URL the saved page names (cdn.sanity.io), fetched 2026-09-26
---

## What the page shows

The post is Camunda's own write-up of "Designing AI Agents in Camunda: The AI Agent Task Connector Standing Alone".
It opens on its subject directly: "In this post, we’ll learn about the first of three key patterns for designing AI agents in Camunda."
The line the record quotes on the AI element is: "Designing AI Agents in Camunda: The AI Agent Task Connector Standing Alone"

The captured figure is the page's 252x108 asset with alt text "Summary-for-human-task-camunda". The contact-sheet pass over the same asset read it as class "bpmn" with ai_visible=yes, in its own words: "Summarize Results", "Review Upsell AI Agent Results" tasks

## Observations (description only, no interpretation)

- **AI activity - function:** the page's own words bind the AI to the process: "Designing AI Agents in Camunda: The AI Agent Task Connector Standing Alone" - the AI-bearing element it names is AI Agent Task; elsewhere: "Designing AI Agents in Camunda: The AI Agent Task Connector Standing Alone" (AI Agent Task)
- **AI activity - element type:** the captured figure is what the contact-sheet pass read as class "bpmn" (ai_visible=yes), in its words: "Summarize Results", "Review Upsell AI Agent Results" tasks
- **Authority - downstream:** the page: "data, policy checks, retrieval, or follow‑on actions; such as looking up a customer, asking a human expert, comparing policy rules, or creating a support ticket."
- **Authority - data:** the page: "the LLM that they are to summarize the results that were taken from a previous agent that are stored in the process variable string(agent.content.conversation.messages) ."
- **Authority - control:** not visible on the page - no gateway, threshold or routing rule is named
- **Input provenance:** the page: "This short summary is used to make the call to see if any previous conversations were held with this customer in the past."
- **Guards present:** not visible on the page - no human review, threshold or validation step is named
- **Prompt / model detail visible:** the page: "The user prompt is a variable from a previous task, recsForUpsell which could be lengthy content."

## Notes for the researcher

The AI call here rests on the page's own words, not on a reading of the figure. 

Capture: the page's 252x108 asset, downloaded at w=1400 and stored as 076_designing-ai-agents-in-camunda-ai-agent-task-connector-alone.png; the contact-sheet reading of the same asset is class bpmn / ai_visible yes. Figure choice: alt 'Summary-for-human-task-camunda' + sheet note '"Summarize Results", "Review Upsell AI Agent Results" tasks'.
