---
n: 299
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: "Guide to Adding a Tool for an AI Agent"
url: https://camunda.com/blog/2025/05/guide-to-adding-tool-ai-agent/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "the visual pass reads the captured figure as class 'bpmn': 'AI Task Agent' task; 'Create Prompt'; empty Tools Pool; the page names BPMN itself: 'AI Agents and BPMN open up an exciting world of agentic orchestration , empowering AI to act with greater autonomy'"
bpmn_evidence_quote: "AI Agents and BPMN open up an exciting world of agentic orchestration , empowering AI to act with greater autonomy while also preserving auditability and"
ai_evidence: "the page binds AI to a process element (AI Task Agent, ad-hoc sub-process): 'AI Agents and BPMN open up an exciting world of agentic orchestration , empowering AI to act with greater autonomy while also preserving auditability and'; the contact-sheet pass reads the captured figure as ai_visible=yes"
ai_evidence_quote: "AI Agents and BPMN open up an exciting world of agentic orchestration , empowering AI to act with greater autonomy while also preserving auditability and"
artefacts:
  screenshot: 064_guide-to-adding-tool-ai-agent.png
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

The post is Camunda's own write-up of "Guide to Adding a Tool for an AI Agent".
It opens on its subject directly: "In this guide we’re going to add a task to the empty sub-process."
The line the record quotes on the AI element is: "AI Agents and BPMN open up an exciting world of agentic orchestration , empowering AI to act with greater autonomy while also preserving auditability and control."

The captured figure is the page's 1200x491 asset with alt text "Ad-hoc-sub-process". The contact-sheet pass over the same asset read it as class "bpmn" with ai_visible=yes, in its own words: "AI Task Agent" task; "Create Prompt"; empty Tools Pool

## Observations (description only, no interpretation)

- **AI activity - function:** the page's own words bind the AI to the process: "AI Agents and BPMN open up an exciting world of agentic orchestration , empowering AI to act with greater autonomy while also preserving auditability and" - the AI-bearing element it names is ad-hoc sub-process; elsewhere: "The AI Task Agent is the brain, able to understand the context and the goal and then to use the tools at its disposal to" (AI Task Agent)
- **AI activity - element type:** the captured figure is what the contact-sheet pass read as class "bpmn" (ai_visible=yes), in its words: "AI Task Agent" task; "Create Prompt"; empty Tools Pool
- **Authority - downstream:** the page: "how we map the response from the tool back into the process instance, which means that the Task Agent will be aware of the result"
- **Authority - data:** the page: "Process variable name It’s important that this variable name matches the output expected by the sub-process."
- **Authority - control:** not visible on the page - no gateway, threshold or routing rule is named
- **Input provenance:** the page: "In this case, we want it to read the answer from the human expert it’s going to consult."
- **Guards present:** not visible on the page - no human review, threshold or validation step is named
- **Prompt / model detail visible:** not visible on the page - no model name, prompt text or parameter is printed

## Notes for the researcher

The AI call here rests on the page's own words, not on a reading of the figure. 

Capture: the page's 1200x491 asset, downloaded at w=1400 and stored as 064_guide-to-adding-tool-ai-agent.png; the contact-sheet reading of the same asset is class bpmn / ai_visible yes. Figure choice: alt 'Ad-hoc-sub-process' + sheet note '"AI Task Agent" task; "Create Prompt"; empty Tools Pool'.
