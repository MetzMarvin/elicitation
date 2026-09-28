---
n: 1393
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: "Key Principles in Designing Agents for Production – Part IV"
url: https://camunda.com/blog/2026/06/key-principles-in-designing-agents-for-production-part-4/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "the visual pass reads the captured figure as class 'bpmn': pink/purple task boxes with arrows; the page names BPMN itself: 'Learn how to protect your Camunda agents in production with BPMN-based guardrails, tool gatekeeping, agent success evaluation, and timing restrictions.'"
bpmn_evidence_quote: "Learn how to protect your Camunda agents in production with BPMN-based guardrails, tool gatekeeping, agent success evaluation, and timing restrictions."
ai_evidence: "the page binds AI to a process element (call to an LLM): 'You can take advantage of this when it comes to protecting important systems from weird LLM behavior while still technically giving the LLM the ability'; the contact-sheet pass reads the captured figure as ai_visible=unclear"
ai_evidence_quote: "You can take advantage of this when it comes to protecting important systems from weird LLM behavior while still technically giving the LLM the ability"
artefacts:
  screenshot: 120_key-principles-in-designing-agents-for-production-part-4.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1120
capture_method: figure downloaded at w=1400 from the asset URL the saved page names (cdn.sanity.io), fetched 2026-09-26
---

## What the page shows

The post is Camunda's own write-up of "Key Principles in Designing Agents for Production – Part IV".
The line the record quotes on the AI element is: "You can take advantage of this when it comes to protecting important systems from weird LLM behavior while still technically giving the LLM the ability to use such tools."

The captured figure is the page's 1120x586 asset with alt text "Tool gatekeeping pattern: human task placed before an action task within a tool flow". The contact-sheet pass over the same asset read it as class "bpmn" with ai_visible=unclear, in its own words: pink/purple task boxes with arrows

## Observations (description only, no interpretation)

- **AI activity - function:** the page's own words bind the AI to the process: "You can take advantage of this when it comes to protecting important systems from weird LLM behavior while still technically giving the LLM the ability" - the AI-bearing element it names is call to an LLM
- **AI activity - element type:** the captured figure is what the contact-sheet pass read as class "bpmn" (ai_visible=unclear), in its words: pink/purple task boxes with arrows
- **Authority - downstream:** the page: "Sure, it might be able to update a customer record when needed, but what are the consequences of it making an update when it shouldn't?"
- **Authority - data:** the page: "to have the judge result in either "optimal," "suboptimal," or "acceptable." Acceptable executions can just end—there's nothing to learn from them and nothing to fix."
- **Authority - control:** the page: "One great way of doing that is by letting it trigger an event that cancels itself, like an escalation event."
- **Input provenance:** the page: "non-interrupting events, you can trigger an agent to update its context if it's dealing with stale data, or perhaps the job it's working on is"
- **Guards present:** not visible on the page - no human review, threshold or validation step is named
- **Prompt / model detail visible:** not visible on the page - no model name, prompt text or parameter is printed

## Notes for the researcher

The AI call here rests on the page's own words, not on a reading of the figure. 

Capture: the page's 1120x586 asset, downloaded at w=1400 and stored as 120_key-principles-in-designing-agents-for-production-part-4.png; the contact-sheet reading of the same asset is class bpmn / ai_visible unclear. Figure choice: alt 'Tool gatekeeping pattern: human task placed before' + sheet note 'pink/purple task boxes with arrows'.
