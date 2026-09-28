---
n: 205
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: "Putting AI Prompt Engineering Into Practice"
url: https://camunda.com/blog/2024/12/putting-ai-prompt-engineering-into-practice-part-2/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "the visual pass reads the captured figure as class 'bpmn': sample process canvas; labels unreadable"
bpmn_evidence_quote: "Camunda sample process for AI travel agent"
ai_evidence: "no AI/LLM element is bound to a process element on this page; the judgement rests on the figure and the page text: 'Engineering Excellence , Process Orchestration'"
ai_evidence_quote: "Engineering Excellence , Process Orchestration"
artefacts:
  screenshot: 058_putting-ai-prompt-engineering-into-practice-part-2.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: poor
capture_width_px: 660
capture_method: figure downloaded at w=1400 from the asset URL the saved page names (cdn.sanity.io), fetched 2026-09-26
---

## What the page shows

The post is Camunda's own write-up of "Putting AI Prompt Engineering Into Practice".
The line the record quotes on the AI element is: "Engineering Excellence , Process Orchestration"

The captured figure is the page's 660x189 asset with alt text "Camunda sample process for AI travel agent". The contact-sheet pass over the same asset read it as class "bpmn" with ai_visible=unclear, in its own words: sample process canvas; labels unreadable

## Observations (description only, no interpretation)

- **AI activity - function:** not visible on the page - the post names no AI/LLM activity
- **AI activity - element type:** the captured figure is what the contact-sheet pass read as class "bpmn" (ai_visible=unclear), in its words: sample process canvas; labels unreadable
- **Authority - downstream:** the page: "AI requires detailed instructions to mimic humans and create the most relevant and high-quality output."
- **Authority - data:** the page: "There are other components that need to be considered in order to maximize results when integrating generative AI into your business operations."
- **Authority - control:** not visible on the page - no gateway, threshold or routing rule is named
- **Input provenance:** the page: "Copy I will provide you with an email that I receive and you will respond to that email."
- **Guards present:** the page: "simple example in the previous blog post shows a human interacting directly with a chatbot in a “conversation” reviewing results and fine tuning right away."
- **Prompt / model detail visible:** the page: "Temperature ."

## Notes for the researcher

**This item is UNCERTAIN and needs a human ruling.** Open question: Does any element of the BPMN diagram on this page call an AI/LLM service? The page text mentions AI but never binds it to a process element.

The AI call here rests on the material above. 

Capture: the page's 660x189 asset, downloaded at w=1400 and stored as 058_putting-ai-prompt-engineering-into-practice-part-2.png; the contact-sheet reading of the same asset is class bpmn / ai_visible unclear. Figure choice: alt 'Camunda sample process for AI travel agent' + sheet note 'sample process canvas; labels unreadable'.
