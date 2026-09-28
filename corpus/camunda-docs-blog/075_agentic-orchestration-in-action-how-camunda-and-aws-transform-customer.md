---
n: 375
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: "Agentic Orchestration in Action: How Camunda and AWS Transform Customer Support"
url: https://camunda.com/blog/2025/10/agentic-orchestration-in-action-how-camunda-and-aws-transform-customer-support/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "the visual pass reads the captured figure as class 'bpmn': 'AI Agent' task; lanes Amazon Bedrock, SES, Lambda; the page names BPMN itself: 'Email Intake and Triggering – The customer’s message arrives via Amazon SES, which triggers a Camunda process instance.'"
bpmn_evidence_quote: "Email Intake and Triggering – The customer’s message arrives via Amazon SES, which triggers a Camunda process instance."
ai_evidence: "the page binds AI to a process element (AI Agent connector, Amazon AI service, ad-hoc sub-process): 'We are in a new era of automation , and customer expectations for accurate and seamless service have never been greater.'; the contact-sheet pass reads the captured figure as ai_visible=yes"
ai_evidence_quote: "We are in a new era of automation , and customer expectations for accurate and seamless service have never been greater."
artefacts:
  screenshot: 075_agentic-orchestration-in-action-how-camunda-and-aws-transform-customer.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1000
capture_method: figure downloaded at w=1400 from the asset URL the saved page names (cdn.sanity.io), fetched 2026-09-26
---

## What the page shows

The post is Camunda's own write-up of "Agentic Orchestration in Action: How Camunda and AWS Transform Customer Support".
It opens on its subject directly: "This post is designed as a companion post, which tackles the same example but explains more what happens inside Camunda’s orchestration layer—how Camunda structures, governs, and operationalizes these AWS components"
The line the record quotes on the AI element is: "We are in a new era of automation , and customer expectations for accurate and seamless service have never been greater."

The captured figure is the page's 1000x578 asset with no alt text. The contact-sheet pass over the same asset read it as class "bpmn" with ai_visible=yes, in its own words: "AI Agent" task; lanes Amazon Bedrock, SES, Lambda

## Observations (description only, no interpretation)

- **AI activity - function:** the page's own words bind the AI to the process: "We are in a new era of automation , and customer expectations for accurate and seamless service have never been greater." - the AI-bearing element it names is Amazon AI service; elsewhere: "Understanding and Intent Extraction – Using Amazon Bedrock, am AI agent is embedded via Camunda’s AI Agent connector , which helps set boundaries around which" (AI Agent connector)
- **AI activity - element type:** the captured figure is what the contact-sheet pass read as class "bpmn" (ai_visible=yes), in its words: "AI Agent" task; lanes Amazon Bedrock, SES, Lambda
- **Authority - downstream:** the page: "Email Intake and Triggering – The customer’s message arrives via Amazon SES, which triggers a Camunda process instance."
- **Authority - data:** the page: "Their input is then captured as part of the process data and, through Camunda’s orchestration, fed back into OpenSearch—continuously refining the agent’s knowledge base."
- **Authority - control:** the page: "Retry logic and circuit breakers – Process variables control the number of permitted retries, timeout thresholds, and fallback paths when an AWS call fails or"
- **Input provenance:** the page: "In this example of a customer interaction, a customer sends an email asking something like: “What’s my remaining loan balance and payoff schedule?”"
- **Guards present:** the page: "Confidence-based branching – Camunda gateways can inspect metadata returned by Bedrock (e.g., confidence scores) and dynamically route execution to either continue automation or escalate to"
- **Prompt / model detail visible:** the page: "For AWS, Amazon OpenSearch Service acts as the agent’s long-term memory, storing semantic embeddings that allow the system to recall relevant documents or past interactions."

## Notes for the researcher

The AI call here rests on the page's own words, not on a reading of the figure. 

Capture: the page's 1000x578 asset, downloaded at w=1400 and stored as 075_agentic-orchestration-in-action-how-camunda-and-aws-transform-customer.png; the contact-sheet reading of the same asset is class bpmn / ai_visible yes. Figure choice: alt '(none)' + sheet note '"AI Agent" task; lanes Amazon Bedrock, SES, Lambda'.
