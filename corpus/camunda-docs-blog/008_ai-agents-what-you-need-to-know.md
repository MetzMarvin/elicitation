---
n: 131
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: Artificial Intelligence (AI) Agents: What You Need to Know
url: https://camunda.com/blog/2024/08/ai-agents-what-you-need-to-know/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: the captured figure is a BPMN diagram, read at full width - start event "Loan Application Received", the tasks "Run Risk Rules", "Intelligent Routing (AI)", "Summarize Results", "Show Investigator Details", "Send Accept Email", "Issue Policy", "Send Reject Email" and "Reject Application", exclusive gateways with X markers labelled "Verified identity?", "Potential Risk?" and "Risk Assessment", labelled flows ("yes", "no", "Low Risk", "Medium Risk", "High Risk", "Low", "High", "Risk Assessment"), two collapsed sub-process boxes "KYC" and "Sentiment Analysis" with collapse markers, and the end events "Application Accepted" and "Application Rejected"
bpmn_evidence_quote: "Intelligent-routing-ai-camunda"
ai_evidence: the captured figure contains a task named "Intelligent Routing (AI)" and three further tasks ("Summarize Results", "Issue Policy", "Reject Application") drawn with the same rosette-shaped connector icon, but the page's own text never binds an AI element to a process element - its only process-adjacent AI reference is a link titled "Accessing Machine Learning Models with Camunda’s Hugging Face Connector for Business Improvement" - so whether this artefact carries an AI/LLM element is left to the researcher
ai_evidence_quote: An AI agent is a software program that autonomously gathers data and carries out tasks using this information
artefacts:
  screenshot: 008_ai-agents-what-you-need-to-know.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1400
capture_method: chrome-devtools-mcp page fetch; the figure's cdn.sanity.io URL decoded out of the page's /_next/image proxy, downloaded at w=1400
---

## What the page shows

The post is an explainer on AI agents - "An AI agent is a software program that autonomously
gathers data and carries out tasks using this information, independently or on behalf of
another system or person" - with sections on what agents are, what they can do, and how to
design one ("Determine the goal of the agent", "Determine how the AI agent will obtain
information to accomplish this goal"). Its text names use cases such as reviewing scans in
healthcare and returning a credit score, but it never walks through a process model and never
says which element in a diagram is AI-bound.

The captured figure is the second of the page's two BPMN diagrams (alt
"Intelligent-routing-ai-camunda"), a loan-application process: start event "Loan Application
Received" into "Run Risk Rules", then the collapsed sub-process "KYC", the gateway "Verified
identity?" (with a long "no" path running underneath the whole diagram), then the task
"Intelligent Routing (AI)" and the gateway "Potential Risk?" forking into "Low Risk", "Medium
Risk" and "High Risk". The low branch runs through "Send Accept Email" / "Issue Policy"; the
medium branch through "Summarize Results" and the human task "Show Investigator Details" to
the "Risk Assessment" gateway; the high branch through "Send Reject Email" / "Reject
Application". Both branches end in the collapsed "Sentiment Analysis" sub-process and the end
events "Application Accepted" (green) and "Application Rejected" (red).

## Observations (description only, no interpretation)

- **AI activity - function:** the page describes what AI agents do in general - they "gather
  data and carry out tasks", "take inputs, make decisions, and then take actions to meet the
  goals outlined for the agent" - but never states what function, if any, the AI element in
  the captured diagram performs.
- **AI activity - element type:** not stated on the page. The captured figure shows a task
  labelled "Intelligent Routing (AI)" carrying a rosette-shaped connector icon in its
  top-left corner, and the same icon on "Summarize Results", "Issue Policy" and "Reject
  Application"; no page text identifies those icons or bindings.
- **Authority - downstream:** the flows out of "Intelligent Routing (AI)" as drawn in the
  captured figure - the gateway "Potential Risk?" with "Low Risk", "Medium Risk" and "High
  Risk" branches leading to "Send Accept Email" / "Issue Policy", to "Summarize Results" and
  "Show Investigator Details", and to "Send Reject Email" / "Reject Application".
- **Authority - data:** not visible on the page - the figure prints no variables or data
  objects, and the page's text describes agent inputs only in the abstract ("input from
  various sources and media types including images, scanned documents, electronic documents,
  audio, etc.").
- **Authority - control:** the gateways drawn in the captured figure ("Verified identity?",
  "Potential Risk?", "Risk Assessment" with its "Low"/"High" flows) and the human task "Show
  Investigator Details"; the page does not describe any of them.
- **Input provenance:** not visible on the page - the start event reads "Loan Application
  Received" but nothing on the page says what the agent consumes.
- **Guards present:** not visible on the page - the captured figure shows the human task
  "Show Investigator Details" between the medium-risk routing and the "Risk Assessment"
  gateway, but the page's text does not discuss guards, review or confirmation.
- **Prompt / model detail visible:** not visible on the page - no model name, prompt text or
  parameter appears anywhere in the brief.

## Notes for the researcher

Flagged UNCERTAIN per the ruling, and there is a discrepancy worth the researcher's eye: the
visual pass recorded "labels unreadable" for this cell, but the captured file is legible and
the diagram contains a task literally named "Intelligent Routing (AI)", plus a repeated
connector icon on three further tasks. The page text, however, is silent about both diagrams
- it is an AI-agent explainer whose figures are not discussed - so the AI-to-element binding
is asserted by the diagram's own label rather than by the prose. The page's only
process-adjacent AI reference in the brief is a link title, "Accessing Machine Learning Models
with Camunda’s Hugging Face Connector for Business Improvement", which by itself names no
element. The other BPMN figure on the page ("Kyc-bpmn-camunda") was not captured; the ruling
question asks about both. The source asset is 1200x401 and the download is a w=1400 upscale
(1400x468 on disk).
