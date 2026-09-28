---
n: 521
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: "Why BPMN (Still) Matters—Especially in the Age of AI"
url: https://camunda.com/blog/2026/04/why-bpmn-still-matters-especially-in-the-age-of-ai/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "the visual pass reads the captured figure as class 'bpmn': loan process; 'Credit Check', 'Risk Assessment', 'Loan Disbursement'; the page names BPMN itself: 'Why BPMN (Still) Matters—Especially in the Age of AI'"
bpmn_evidence_quote: "Why BPMN (Still) Matters—Especially in the Age of AI"
ai_evidence: "the page binds AI to a process element (Anthropic/Claude, call to an LLM): 'In practice, agentic orchestration is not just “call an LLM from one step in a process.” It’s the ability to combine two kinds of automation'; the contact-sheet pass reads the captured figure as ai_visible=no"
ai_evidence_quote: "In practice, agentic orchestration is not just “call an LLM from one step in a process.” It’s the ability to combine two kinds of automation"
artefacts:
  screenshot: 088_why-bpmn-still-matters-especially-in-the-age-of-ai.png
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

The post is Camunda's own write-up of "Why BPMN (Still) Matters—Especially in the Age of AI".
It opens on its subject directly: "So what does agentic orchestration look like beyond the buzzword?"
The line the record quotes on the AI element is: "In practice, agentic orchestration is not just “call an LLM from one step in a process.” It’s the ability to combine two kinds of automation in one coherent system:"

The captured figure is the page's 1024x228 asset with no alt text. The contact-sheet pass over the same asset read it as class "bpmn" with ai_visible=no, in its own words: loan process; "Credit Check", "Risk Assessment", "Loan Disbursement"

## Observations (description only, no interpretation)

- **AI activity - function:** the page's own words bind the AI to the process: "In practice, agentic orchestration is not just “call an LLM from one step in a process.” It’s the ability to combine two kinds of automation" - the AI-bearing element it names is call to an LLM; elsewhere: "This isn’t theoretical. Daniel, our CTO, built a full AI agent orchestration in under an hour using Claude and Camunda , from natural language description" (Anthropic/Claude)
- **AI activity - element type:** the captured figure is what the contact-sheet pass read as class "bpmn" (ai_visible=no), in its words: loan process; "Credit Check", "Risk Assessment", "Loan Disbursement"
- **Authority - downstream:** the page: "It converses with the customer, understands their needs, proposes loan options, answers questions, and decides when to trigger the formal application."
- **Authority - data:** the page: "work is fuzzy and variable, and you want deterministic control where work is very structured (and can be automated very efficiently) or must be reliable,"
- **Authority - control:** the page: "see and control what’s happening: which instances are stuck at the fraud check, retry failed credit bureau calls, reassign loans when a specialist is unavailable."
- **Input provenance:** the page: "And when the agent decides the customer is ready to apply for a specific loan, it triggers the structured loan application subprocess ."
- **Guards present:** the page: "to message the customer , BPMN can route the draft through human review before it’s sent or skip that step based on a confidence score."
- **Prompt / model detail visible:** not visible on the page - no model name, prompt text or parameter is printed

## Notes for the researcher

The AI call here rests on the page's own words, not on a reading of the figure. 

Capture: the page's 1024x228 asset, downloaded at w=1400 and stored as 088_why-bpmn-still-matters-especially-in-the-age-of-ai.png; the contact-sheet reading of the same asset is class bpmn / ai_visible no. Figure choice: alt '(none)' + sheet note 'loan process; "Credit Check", "Risk Assessment", "Loan Disbu'.
