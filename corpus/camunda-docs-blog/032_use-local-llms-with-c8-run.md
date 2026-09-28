---
n: 445
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: "Bringing Local LLMs to Camunda 8: Orchestrating AI Agents with Camunda Run"
url: https://camunda.com/blog/2026/01/use-local-llms-with-c8-run/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "the visual pass reads the captured figure as class 'screenshot': Operate; 'AI Agent' ad-hoc sub-process; agent/toolCallResults variables; the page names BPMN itself: 'A BPMN process modeled with an agentic feedback loop (using the AI Agent connector.'"
bpmn_evidence_quote: "A BPMN process modeled with an agentic feedback loop (using the AI Agent connector."
ai_evidence: "the page binds AI to a process element (AI Agent connector, AI Agent sub-process, ad-hoc sub-process, call to an LLM): 'Camunda 8’s new AI Agent connector makes it easy to integrate large language models (LLMs) into your process workflows.'; the contact-sheet pass reads the captured figure as ai_visible=yes"
ai_evidence_quote: "Camunda 8’s new AI Agent connector makes it easy to integrate large language models (LLMs) into your process workflows."
artefacts:
  screenshot: 032_use-local-llms-with-c8-run.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: marginal
capture_width_px: 623
capture_method: figure downloaded at w=1400 from the asset URL the saved page names (cdn.sanity.io), fetched 2026-09-26
---

## What the page shows

The post is Camunda's own write-up of "Bringing Local LLMs to Camunda 8: Orchestrating AI Agents with Camunda Run".
The line the record quotes on the AI element is: "Camunda 8’s new AI Agent connector makes it easy to integrate large language models (LLMs) into your process workflows."

The captured figure is the page's 623x602 asset with alt text "Image5". The contact-sheet pass over the same asset read it as class "screenshot" with ai_visible=yes, in its own words: Operate; "AI Agent" ad-hoc sub-process; agent/toolCallResults variables

## Observations (description only, no interpretation)

- **AI activity - function:** the page's own words bind the AI to the process: "Camunda 8’s new AI Agent connector makes it easy to integrate large language models (LLMs) into your process workflows." - the AI-bearing element it names is AI Agent connector; elsewhere: "A BPMN process modeled with an agentic feedback loop (using the AI Agent connector." (AI Agent connector)
- **AI activity - element type:** the captured figure is what the contact-sheet pass read as class "screenshot" (ai_visible=yes), in its words: Operate; "AI Agent" ad-hoc sub-process; agent/toolCallResults variables
- **Authority - downstream:** the page: "One of the tasks should have a description similar to Sends an email to the specified user ."
- **Authority - data:** the page: "In a production-ready process, the user prompt would likely be set as a variable and built from a previous set of inputs."
- **Authority - control:** not visible on the page - no gateway, threshold or routing rule is named
- **Input provenance:** the page: "If you downloaded the Starter Package from the Developer Portal, Camunda Modeler was included in the zip file."
- **Guards present:** not visible on the page - no human review, threshold or validation step is named
- **Prompt / model detail visible:** the page: "In the Model provider section, select OpenAI Compatible from the Provider dropdown."

## Notes for the researcher

The AI call here rests on the page's own words, not on a reading of the figure. 

Capture: the page's 623x602 asset, downloaded at w=1400 and stored as 032_use-local-llms-with-c8-run.png; the contact-sheet reading of the same asset is class screenshot / ai_visible yes. Figure choice: forced by gen_overrides.json: figure 1 is the post's title card; figure 2 is the Operate instance view with the AI Agent container.
