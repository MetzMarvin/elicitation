---
n: 1392
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: "Key Principles in Designing Agents for Production – Part III"
url: https://camunda.com/blog/2026/06/key-principles-in-designing-agents-for-production-part-3/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "the visual pass reads the captured figure as class 'bpmn': small box/flow diagram on page; labels unreadable; the page names BPMN itself: \"When building an Agent in Camunda, you might conflate the idea that an agent tool = a BPMN task.\""
bpmn_evidence_quote: "When building an Agent in Camunda, you might conflate the idea that an agent tool = a BPMN task."
ai_evidence: "the page binds AI to a process element (call to an LLM): \"Once a tool finishes being executed, the process engine wraps up and passes the value of the \"toolCallResult\" variable to the LLM.\"; the contact-sheet pass reads the captured figure as ai_visible=unclear"
ai_evidence_quote: "Once a tool finishes being executed, the process engine wraps up and passes the value of the \"toolCallResult\" variable to the LLM."
artefacts:
  screenshot: 119_key-principles-in-designing-agents-for-production-part-3.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: poor
capture_width_px: 903
capture_method: figure downloaded at w=1400 from the asset URL the saved page names (cdn.sanity.io), fetched 2026-09-26
---

## What the page shows

The post is Camunda's own write-up of "Key Principles in Designing Agents for Production – Part III".
The line the record quotes on the AI element is: "Once a tool finishes being executed, the process engine wraps up and passes the value of the "toolCallResult" variable to the LLM."

The captured figure is the page's 903x923 asset with alt text "Overview of tool options available within a Camunda agent's ad hoc subprocess". The contact-sheet pass over the same asset read it as class "bpmn" with ai_visible=unclear, in its own words: small box/flow diagram on page; labels unreadable

## Observations (description only, no interpretation)

- **AI activity - function:** the page's own words bind the AI to the process: "Once a tool finishes being executed, the process engine wraps up and passes the value of the "toolCallResult" variable to the LLM." - the AI-bearing element it names is call to an LLM
- **AI activity - element type:** the captured figure is what the contact-sheet pass read as class "bpmn" (ai_visible=unclear), in its words: small box/flow diagram on page; labels unreadable
- **Authority - downstream:** the page: "tool in order to send a communication to the client," or depending on the requirements could also include prerequisites: "Use this tool in order to"
- **Authority - data:** the page: "has either found some data from the user prompt or as the output of another tool and is recontextualizing it as input for this tool."
- **Authority - control:** the page: "series I'll talk in more detail about patterns that can help safeguard data and add guardrails to your agent for a safer feeling when deploying."
- **Input provenance:** the page: "status change to the customer," while the tool set available could have one that says, "Use this tool in order to send an email to"
- **Guards present:** the page: "This check means you can define specific instructions about formatting either in natural language or by giving a required JSON schema that needs to be"
- **Prompt / model detail visible:** the page: "an addition to the system prompt, but instead of defining concepts at a high level, it's a low-level natural language description of what the tool"

## Notes for the researcher

The AI call here rests on the page's own words, not on a reading of the figure. 

Capture: the page's 903x923 asset, downloaded at w=1400 and stored as 119_key-principles-in-designing-agents-for-production-part-3.png; the contact-sheet reading of the same asset is class bpmn / ai_visible unclear. Figure choice: alt 'Overview of tool options available within a Camund' + sheet note 'small box/flow diagram on page; labels unreadable'.
