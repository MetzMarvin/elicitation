---
n: 307
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: "Camunda Alpha Release for June 2025"
url: https://camunda.com/blog/2025/06/camunda-alpha-release-june-2025/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "the visual pass reads the captured figure as class 'bpmn': 'AI Agent Connector' task; 'Handle tools' ad-hoc sub-process; the page names BPMN itself: 'The AI Agent connector is designed for use with an ad-hoc sub-process in a feedback loop, providing automated user interaction'"
bpmn_evidence_quote: "The AI Agent connector is designed for use with an ad-hoc sub-process in a feedback loop, providing automated user interaction and tool discovery/selection."
ai_evidence: "the page binds AI to a process element (AI Agent connector, AI-bound task, ad-hoc sub-process): 'The AI Agent connector which was recently published on Camunda Marketplace is now officially included as part of this alpha release and directly available in'; the contact-sheet pass reads the captured figure as ai_visible=yes"
ai_evidence_quote: "The AI Agent connector which was recently published on Camunda Marketplace is now officially included as part of this alpha release and directly available in"
artefacts:
  screenshot: 066_camunda-alpha-release-june-2025.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1999
capture_method: figure downloaded at w=1400 from the asset URL the saved page names (cdn.sanity.io), fetched 2026-09-26
---

## What the page shows

The post is Camunda's own write-up of "Camunda Alpha Release for June 2025".
It opens on its subject directly: "This blog is organized using the following product house, with E2E Process Orchestration at the foundation and our product components represented by the building bricks."
The line the record quotes on the AI element is: "The AI Agent connector which was recently published on Camunda Marketplace is now officially included as part of this alpha release and directly available in Web Modeler."

The captured figure is the page's 1999x974 asset with alt text "Camunda-agentic-orchestration". The contact-sheet pass over the same asset read it as class "bpmn" with ai_visible=yes, in its own words: "AI Agent Connector" task; "Handle tools" ad-hoc sub-process

## Observations (description only, no interpretation)

- **AI activity - function:** the page's own words bind the AI to the process: "The AI Agent connector which was recently published on Camunda Marketplace is now officially included as part of this alpha release and directly available in" - the AI-bearing element it names is AI Agent connector; elsewhere: "The Vector Database connector , also published to Camunda Marketplace , allows embedding, storing, and retrieving Large Language Model (LLM) embeddings." (AI Agent connector)
- **AI activity - element type:** the captured figure is what the contact-sheet pass read as class "bpmn" (ai_visible=yes), in its words: "AI Agent Connector" task; "Handle tools" ad-hoc sub-process
- **Authority - downstream:** not visible on the page - the page does not say what the AI's output acts on
- **Authority - data:** the page: "With a continued focus on operationalizing AI, this section provides information about the continued support of agentic orchestration in our product components."
- **Authority - control:** the page: "By default, when a job is created, its retry count is determined based on the camunda:failedJobRetryTimeCycle expression defined in the BPMN model."
- **Input provenance:** the page: "A process application is now deployed as a single bundle of files."
- **Guards present:** the page: "While the Camunda 7 to Camunda 8 Migration Tools are still in alpha, you can already check out the project and give it a try!"
- **Prompt / model detail visible:** not visible on the page - no model name, prompt text or parameter is printed

## Notes for the researcher

The AI call here rests on the page's own words, not on a reading of the figure. 

Capture: the page's 1999x974 asset, downloaded at w=1400 and stored as 066_camunda-alpha-release-june-2025.png; the contact-sheet reading of the same asset is class bpmn / ai_visible yes. Figure choice: alt 'Camunda-agentic-orchestration' + sheet note '"AI Agent Connector" task; "Handle tools" ad-hoc sub-process'.
