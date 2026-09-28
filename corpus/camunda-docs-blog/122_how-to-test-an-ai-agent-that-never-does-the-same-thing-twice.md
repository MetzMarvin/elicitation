---
n: 1433
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: "How to Test an AI Agent That Never Does the Same Thing Twice"
url: https://camunda.com/blog/2026/08/how-to-test-an-ai-agent-that-never-does-the-same-thing-twice/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "the visual pass reads the captured figure as class 'other-diagram': KYC onboarding diagram; Extract/Validate Customer Info"
bpmn_evidence_quote: "Diagram testing the process around the agent with no model"
ai_evidence: "no AI/LLM element is bound to a process element on this page; the judgement rests on the figure and the page text: 'Testing an AI agent means testing the process around it, which is deterministic and free, the model's behavior, which is neither, and whether it stays'"
ai_evidence_quote: "Testing an AI agent means testing the process around it, which is deterministic and free, the model's behavior, which is neither, and whether it stays"
artefacts:
  screenshot: 122_how-to-test-an-ai-agent-that-never-does-the-same-thing-twice.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: marginal
capture_width_px: 897
capture_method: figure downloaded at w=1400 from the asset URL the saved page names (cdn.sanity.io), fetched 2026-09-26
---

## What the page shows

The post is Camunda's own write-up of "How to Test an AI Agent That Never Does the Same Thing Twice".
The line the record quotes on the AI element is: "Agentic Orchestration , Engineering Excellence"

The captured figure is the page's 897x590 asset with alt text "Diagram testing the process around the agent with no model". The contact-sheet pass over the same asset read it as class "other-diagram" with ai_visible=unclear, in its own words: KYC onboarding diagram; Extract/Validate Customer Info

## Observations (description only, no interpretation)

- **AI activity - function:** not visible on the page - the post names no AI/LLM activity
- **AI activity - element type:** the captured figure is what the contact-sheet pass read as class "other-diagram" (ai_visible=unclear), in its words: KYC onboarding diagram; Extract/Validate Customer Info
- **Authority - downstream:** the page: "the process - advance a virtual clock to check that an unanswered review reroutes when the SLA expires or evaluate the routing decision table directly."
- **Authority - data:** the page: "Does its output land on the variables that downstream routing, escalation, and error handling read?"
- **Authority - control:** the page: "likes, instructions that forbid escalating to compliance on a risk signal alone, an error boundary for its own failures, and a reporting tool that hands"
- **Input provenance:** the page: "A customer applies, a screening agent gathers what it needs and forms a recommendation, a decision table routes the case by risk and approval authority,"
- **Guards present:** the page: "nobody is doing the agent's job, leaving the test framework free to do it instead: pretend the agent chose the identity check with this argument."
- **Prompt / model detail visible:** the page: "judge call, and deterministic once you fix the embedding model, which makes them the better fit when the phrasing can vary but the meaning shouldn't."

## Notes for the researcher

**This item is UNCERTAIN and needs a human ruling.** Open question: Does any element of the BPMN diagram on this page call an AI/LLM service? The page text mentions AI but never binds it to a process element.

The AI call here rests on the material above. 

Capture: the page's 897x590 asset, downloaded at w=1400 and stored as 122_how-to-test-an-ai-agent-that-never-does-the-same-thing-twice.png; the contact-sheet reading of the same asset is class other-diagram / ai_visible unclear. Figure choice: alt 'Diagram testing the process around the agent with ' + sheet note 'KYC onboarding diagram; Extract/Validate Customer Info'.
