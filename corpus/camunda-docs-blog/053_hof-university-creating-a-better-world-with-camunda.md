---
n: 136
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: "Hof University: Creating a Better World with Camunda"
url: https://camunda.com/blog/2024/09/hof-university-creating-a-better-world-with-camunda/
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: "This is one very wide, very faint composite BPMN figure (four stacked process fragments / a collapsed parent pool). At native width the task labels are a few grey pixels tall and completely illegible, so I cannot read whether any task, gateway or call activity inside the process names an AI/LLM step (the page's single AI mention is prose about 'latest technologies such as blockchain and AI' for a central data platform, not a drawn element). Needs a legible re-capture or the source BPMN to rule the AI element in or out."
needs_visual_check: true
bpmn_evidence: "the visual pass reads the captured figure as class 'bpmn': wide process with several tasks; the page names BPMN itself: 'The first thing they did was try to understand the process of creating new textiles.'"
bpmn_evidence_quote: "The first thing they did was try to understand the process of creating new textiles."
ai_evidence: "no AI/LLM element is bound to a process element on this page; the judgement rests on the figure and the page text: 'Brauch and Weigand knew the implementation of DPPs would affect every industry, with far-reaching implications for nearly all business processes.'"
ai_evidence_quote: "Brauch and Weigand knew the implementation of DPPs would affect every industry, with far-reaching implications for nearly all business processes."
artefacts:
  screenshot: 053_hof-university-creating-a-better-world-with-camunda.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: marginal
capture_width_px: 600
capture_method: figure downloaded at w=1400 from the asset URL the saved page names (cdn.sanity.io), fetched 2026-09-26
---

## What the page shows

The post is Camunda's own write-up of "Hof University: Creating a Better World with Camunda".
The line the record quotes on the AI element is: "Hof University: Creating a Better World with Camunda"

The captured figure is the page's 600x224 asset with alt text "A large BPMN shows how linear and siloed the textile process is". The contact-sheet pass over the same asset read it as class "bpmn" with ai_visible=no, in its own words: wide process with several tasks

## Observations (description only, no interpretation)

- **AI activity - function:** not visible on the page - the post names no AI/LLM activity
- **AI activity - element type:** the captured figure is what the contact-sheet pass read as class "bpmn" (ai_visible=no), in its words: wide process with several tasks
- **Authority - downstream:** the page: "also realized that to create a true end-to-end approach, they needed a central platform that can capture,exchange, and store data based on the latest technologies"
- **Authority - data:** the page: "collects and shares product data throughout the entire product lifecycle and has product data from the whole supply chain, including raw materials, extraction, and manufacturing"
- **Authority - control:** not visible on the page - no gateway, threshold or routing rule is named
- **Input provenance:** the page: "world would love to have greater visibility into their supply chain data to help customers and stakeholders make more informed, sustainable choices for the planet."
- **Guards present:** not visible on the page - no human review, threshold or validation step is named
- **Prompt / model detail visible:** not visible on the page - no model name, prompt text or parameter is printed

## Notes for the researcher

**This item is UNCERTAIN and needs a human ruling.** Open question: Does any element of the BPMN diagram on this page call an AI/LLM service? The page text mentions AI but never binds it to a process element.

The AI call here rests on the material above. 

Capture: the page's 600x224 asset, downloaded at w=1400 and stored as 053_hof-university-creating-a-better-world-with-camunda.png; the contact-sheet reading of the same asset is class bpmn / ai_visible no. Figure choice: alt 'A large BPMN shows how linear and siloed the texti' + sheet note 'wide process with several tasks'.
