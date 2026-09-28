---
n: 398
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: "Migrate Your Agentic Processes Without Disruption Using Process Instance Migration"
url: https://camunda.com/blog/2026/01/migrate-your-agentic-processes-without-disruption-using-process-instance-migration/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "the visual pass reads the captured figure as class 'screenshot': version comparison dialog with two process diagrams; the page names BPMN itself: 'We worked with our team and determined that the best (and simplest) approach would be to add a human step'"
bpmn_evidence_quote: "We worked with our team and determined that the best (and simplest) approach would be to add a human step as an additional guardrail in"
ai_evidence: "the page binds AI to a process element (AI-bound task, ad-hoc sub-process, call to an LLM): 'Since we are a bit new to adding AI into our processes at Horse & Hawk Habitat, we wanted to add a check to see'; the contact-sheet pass reads the captured figure as ai_visible=no"
ai_evidence_quote: "Since we are a bit new to adding AI into our processes at Horse & Hawk Habitat, we wanted to add a check to see"
artefacts:
  screenshot: 031_migrate-your-agentic-processes-without-disruption-using-process-instan.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1024
capture_method: figure downloaded at w=1400 from the asset URL the saved page names (cdn.sanity.io), fetched 2026-09-26
---

## What the page shows

The post is Camunda's own write-up of "Migrate Your Agentic Processes Without Disruption Using Process Instance Migration".
The line the record quotes on the AI element is: "Since we are a bit new to adding AI into our processes at Horse & Hawk Habitat, we wanted to add a check to see how the prompt looked."

The captured figure is the page's 1024x559 asset with alt text "Diagram showing versioned process definitions with multiple versions and process instances". The contact-sheet pass over the same asset read it as class "screenshot" with ai_visible=no, in its own words: version comparison dialog with two process diagrams

## Observations (description only, no interpretation)

- **AI activity - function:** the page's own words bind the AI to the process: "Since we are a bit new to adding AI into our processes at Horse & Hawk Habitat, we wanted to add a check to see" - the AI-bearing element it names is call to an LLM; elsewhere: "Ad-hoc subprocesses that allows agents to dynamically select tasks at runtime" (ad-hoc sub-process)
- **AI activity - element type:** the captured figure is what the contact-sheet pass read as class "screenshot" (ai_visible=no), in its words: version comparison dialog with two process diagrams
- **Authority - downstream:** the page: "communication to HR, but the suggestion to send an email doesn’t have a mechanism to take that input and feed it back to the process."
- **Authority - data:** the page: "Carefully handle the state of variables."
- **Authority - control:** the page: "Common migration scenarios include correcting logic errors, adding new compliance rules, and improving process efficiency."
- **Input provenance:** the page: "Since this message seems to be of a personal nature, it makes sense that the AI agent would send an email, and that is exactly"
- **Guards present:** the page: "our team and determined that the best (and simplest) approach would be to add a human step as an additional guardrail in our AI agent."
- **Prompt / model detail visible:** not visible on the page - no model name, prompt text or parameter is printed

## Notes for the researcher

**This item is UNCERTAIN and needs a human ruling.** Open question: Do the agentic versions of the order process on this page bind an AI element? The post speaks of a call to an LLM and of ad-hoc sub-processes, but the two versions shown in the capture contain no AI element.

The AI call here rests on the page's own words, not on a reading of the figure. 

Capture: the page's 1024x559 asset, downloaded at w=1400 and stored as 031_migrate-your-agentic-processes-without-disruption-using-process-instan.png; the contact-sheet reading of the same asset is class screenshot / ai_visible no. Figure choice: forced by gen_overrides.json: the Operate migration view of both process versions, read at 1400 px.
