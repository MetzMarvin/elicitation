---
n: 336
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: "Orchestrating Intelligence: Accelerating Decisions with Camunda Intelligent Document Processing"
url: https://camunda.com/blog/2025/08/orchestrating-intelligence-accelerating-decisions-camunda-intelligent-document-processing/
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: "The three 'Extract ...' tasks are Camunda IDP extraction tasks, which the page describes as LLM/prompt-driven, but the figure shows only an unresolvable element-template icon - no template name, connector name or prompt binding is legible. Are these IDP extraction tasks to be counted as AI elements inside this BPMN sub-process on the strength of the page prose, or is an AI-named label or binding required in the figure?"
needs_visual_check: true
bpmn_evidence: "the visual pass reads the captured figure as class 'screenshot': Operate view; 'Submit Bid'/'Review Bid' sub-process and variables; the page names BPMN itself: 'What if you need to verify someone’s identity or review figures in supporting documents for a loan?'"
bpmn_evidence_quote: "What if you need to verify someone’s identity or review figures in supporting documents for a loan?"
ai_evidence: "the page binds AI to a process element (ad-hoc sub-process): 'Camunda’s agentic orchestration model brings even greater flexibility into how you can take advantage of IDP in your business processes.'; the contact-sheet pass reads the captured figure as ai_visible=no"
ai_evidence_quote: "Camunda’s agentic orchestration model brings even greater flexibility into how you can take advantage of IDP in your business processes."
artefacts:
  screenshot: 070_orchestrating-intelligence-accelerating-decisions-camunda-intelligent-.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1124
capture_method: figure downloaded at w=1400 from the asset URL the saved page names (cdn.sanity.io), fetched 2026-09-26
---

## What the page shows

The post is Camunda's own write-up of "Orchestrating Intelligence: Accelerating Decisions with Camunda Intelligent Document Processing".
The line the record quotes on the AI element is: "Camunda’s agentic orchestration model brings even greater flexibility into how you can take advantage of IDP in your business processes."

The captured figure is the page's 1124x917 asset with alt text "example BPMN sub-process in Camunda Operate showing process variables extracted with IDP". The contact-sheet pass over the same asset read it as class "screenshot" with ai_visible=no, in its own words: Operate view; "Submit Bid"/"Review Bid" sub-process and variables

## Observations (description only, no interpretation)

- **AI activity - function:** the page's own words bind the AI to the process: "Camunda’s agentic orchestration model brings even greater flexibility into how you can take advantage of IDP in your business processes." - the AI-bearing element it names is ad-hoc sub-process; elsewhere: "Ad-hoc sub-processes for dynamic document task composition" (ad-hoc sub-process)
- **AI activity - element type:** the captured figure is what the contact-sheet pass read as class "screenshot" (ai_visible=no), in its words: Operate view; "Submit Bid"/"Review Bid" sub-process and variables
- **Authority - downstream:** the page: "As detailed below, each IDP connector extracts the pertinent data from the documents provided and assigns them to the correct process variable."
- **Authority - data:** the page: "native IDP classifies incoming documents, extracts the fields and the data you care about with machine-learning precision, and hands clean data to the next task"
- **Authority - control:** not visible on the page - no gateway, threshold or routing rule is named
- **Input provenance:** the page: "Financial services : An excellent use of intelligent document processing is automating onboarding in financial services along with Know Your Customer (KYC) documentation."
- **Guards present:** the page: "What if you need to verify someone’s identity or review figures in supporting documents for a loan?"
- **Prompt / model detail visible:** not visible on the page - no model name, prompt text or parameter is printed

## Notes for the researcher

The AI call here rests on the page's own words, not on a reading of the figure. 

Capture: the page's 1124x917 asset, downloaded at w=1400 and stored as 070_orchestrating-intelligence-accelerating-decisions-camunda-intelligent-.png; the contact-sheet reading of the same asset is class screenshot / ai_visible no. Figure choice: alt 'example BPMN sub-process in Camunda Operate showin' + sheet note 'Operate view; "Submit Bid"/"Review Bid" sub-process and vari'.
