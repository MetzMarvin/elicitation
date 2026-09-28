---
n: 360
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: "Build an AI Process Agent with Camunda: Orchestrating People, Tools, and LLMs"
url: https://camunda.com/blog/2025/10/build-ai-agent-camunda-orchestrating-people-tools-llms/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "the visual pass reads the captured figure as class 'bpmn': start-to-end only; palette tooltip 'expanded sub-process'; the page names BPMN itself: 'Create a new BPMN diagram and name it “Tech Helper Agent” with an ID of process_techHelperAgent .'"
bpmn_evidence_quote: "Create a new BPMN diagram and name it “Tech Helper Agent” with an ID of process_techHelperAgent ."
ai_evidence: "the page binds AI to a process element (AI-bound task, Anthropic/Claude, ad-hoc sub-process): 'This example demonstrates how to integrate Camunda’s AI features into a Camunda process using AWS Bedrock and Claude Sonnet.'; the contact-sheet pass reads the captured figure as ai_visible=no"
ai_evidence_quote: "This example demonstrates how to integrate Camunda’s AI features into a Camunda process using AWS Bedrock and Claude Sonnet."
artefacts:
  screenshot: 073_build-ai-agent-camunda-orchestrating-people-tools-llms.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: marginal
capture_width_px: 869
capture_method: figure downloaded at w=1400 from the asset URL the saved page names (cdn.sanity.io), fetched 2026-09-26
---

## What the page shows

The post is Camunda's own write-up of "Build an AI Process Agent with Camunda: Orchestrating People, Tools, and LLMs".
It opens on its subject directly: "In this blog, we’ll explore how to create an AI process agent using Camunda that brings together the intelligence of an LLM, the structure of a business process, and the"
The line the record quotes on the AI element is: "This example demonstrates how to integrate Camunda’s AI features into a Camunda process using AWS Bedrock and Claude Sonnet."

The captured figure is the page's 869x292 asset with alt text "Sub-process". The contact-sheet pass over the same asset read it as class "bpmn" with ai_visible=no, in its own words: start-to-end only; palette tooltip "expanded sub-process"

## Observations (description only, no interpretation)

- **AI activity - function:** the page's own words bind the AI to the process: "This example demonstrates how to integrate Camunda’s AI features into a Camunda process using AWS Bedrock and Claude Sonnet." - the AI-bearing element it names is Anthropic/Claude; elsewhere: "It is important to note that the box in the center, the ad-hoc sub-process, is our AI process agent that connects to the LLM and" (ad-hoc sub-process)
- **AI activity - element type:** the captured figure is what the contact-sheet pass read as class "bpmn" (ai_visible=no), in its words: start-to-end only; palette tooltip "expanded sub-process"
- **Authority - downstream:** the page: "Now in this situation, we need the agent to create some data and then display it to the user in a formatted manner."
- **Authority - data:** the page: "fromAi(toolCall.resultOfQuery, "This is the result of the query made by the user, format this in markdown") This function tells the agent to create a variable"
- **Authority - control:** not visible on the page - no gateway, threshold or routing rule is named
- **Input provenance:** the page: "need to add a form to the start event so that the AI process agent will know what query it has received so that it"
- **Guards present:** the page: "end, you’ll see how simple it can be to connect a REST endpoint, orchestrate an LLM, and even incorporate human decision-making into the same flow."
- **Prompt / model detail visible:** the page: "We will leave the System Prompt with the default for now and move to the User Prompt."

## Notes for the researcher

The AI call here rests on the page's own words, not on a reading of the figure. 

Capture: the page's 869x292 asset, downloaded at w=1400 and stored as 073_build-ai-agent-camunda-orchestrating-people-tools-llms.png; the contact-sheet reading of the same asset is class bpmn / ai_visible no. Figure choice: alt 'Sub-process' + sheet note 'start-to-end only; palette tooltip "expanded sub-process"'.
