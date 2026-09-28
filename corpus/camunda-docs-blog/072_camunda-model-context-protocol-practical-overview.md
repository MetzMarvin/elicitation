---
n: 348
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: "Camunda and the Model Context Protocol: A Practical Overview"
url: https://camunda.com/blog/2025/09/camunda-model-context-protocol-practical-overview/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "the visual pass reads the captured figure as class 'bpmn': pool 'AI Agent'; ad-hoc 'Engage Lost Agent'; LLM caption; the page names BPMN itself: 'Before we jump into Camunda’s support of MCP, it is important to understand how Camunda implements AI agents.'"
bpmn_evidence_quote: "Before we jump into Camunda’s support of MCP, it is important to understand how Camunda implements AI agents."
ai_evidence: "the page binds AI to a process element (AI Agent Task, AI Agent connector, AI Task Agent, AI-bound task, Anthropic/Claude, MCP/A2A connector, ad-hoc sub-process): 'Before we jump into Camunda’s support of MCP, it is important to understand how Camunda implements AI agents.'; the contact-sheet pass reads the captured figure as ai_visible=yes"
ai_evidence_quote: "Before we jump into Camunda’s support of MCP, it is important to understand how Camunda implements AI agents."
artefacts:
  screenshot: 072_camunda-model-context-protocol-practical-overview.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1200
capture_method: figure downloaded at w=1400 from the asset URL the saved page names (cdn.sanity.io), fetched 2026-09-26
---

## What the page shows

The post is Camunda's own write-up of "Camunda and the Model Context Protocol: A Practical Overview".
The line the record quotes on the AI element is: "Before we jump into Camunda’s support of MCP, it is important to understand how Camunda implements AI agents."

The captured figure is the page's 1200x615 asset with alt text "BPMN diagram of an ad-hoc sub-process in Camunda representing an AI Agent". The contact-sheet pass over the same asset read it as class "bpmn" with ai_visible=yes, in its own words: pool "AI Agent"; ad-hoc "Engage Lost Agent"; LLM caption

## Observations (description only, no interpretation)

- **AI activity - function:** the page's own words bind the AI to the process: "Before we jump into Camunda’s support of MCP, it is important to understand how Camunda implements AI agents." - the AI-bearing element it names is ad-hoc sub-process; elsewhere: "The following process diagram depicts an example of how this can be modeled in BPMN with Camunda." (ad-hoc sub-process)
- **AI activity - element type:** the captured figure is what the contact-sheet pass read as class "bpmn" (ai_visible=yes), in its words: pool "AI Agent"; ad-hoc "Engage Lost Agent"; LLM caption
- **Authority - downstream:** the page: "To start this exercise, we will create the required forms first so that we can simply link them when we create the BPMN model."
- **Authority - data:** the page: "Agent provides the proper inputs to this tool, so you will need to create two input variables to match those used in the previous FEEL"
- **Authority - control:** the page: "a start event, followed by an exclusive gateway, connected to a task, another exclusive gateway, another task and then an end event as shown below."
- **Input provenance:** the page: "our standard AI agent which provides information about the incoming request (incoming from a starting form) and makes suggestions on how to resolve the request."
- **Guards present:** the page: "You need to validate documents, receipts, confirm policies are in effect, check deductibles and inclusions, and interface with several other systems to detect possible fraud."
- **Prompt / model detail visible:** the page: "that you have access to the following: an AWS region, an AWS access key for AWS Bedrock, and an AWS secret key for AWS Bedrock."

## Notes for the researcher

The AI call here rests on the page's own words, not on a reading of the figure. 

Capture: the page's 1200x615 asset, downloaded at w=1400 and stored as 072_camunda-model-context-protocol-practical-overview.png; the contact-sheet reading of the same asset is class bpmn / ai_visible yes. Figure choice: alt 'BPMN diagram of an ad-hoc sub-process in Camunda r' + sheet note 'pool "AI Agent"; ad-hoc "Engage Lost Agent"; LLM caption'.
