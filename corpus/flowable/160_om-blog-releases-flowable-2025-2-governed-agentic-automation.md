---
n: 772
source: flowable
source_name: Flowable (enterprise documentation, vendor blog/marketing site, training site)
title: Flowable 2025.2: Governed Agentic Automation & AI Studio
url: https://www.flowable.com/blog/releases/flowable-2025-2-governed-agentic-automation
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "Does any figure here show a BPMN process containing an AI/LLM element? The only BPMN 2.0 diagram on the page (Flowable Design, 'Customer onboarding': start event - user task 'Customer Verification' - user task 'Approval' - end event) has no AI element inside the process, and the AI on the page is the AI Assistant that authored that step plus a separate 'Liability check agent' model, so an AI-bound task inside a BPMN process is not visible."
needs_visual_check: false
bpmn_evidence: figure captions, alt text or OCR labels naming BPMN constructs: thumbnail 6. A2A agent | thumbnail_6._A2A_agent.png; thumbnail 8. Agentforce config | thumbnail_8._Agentforce_config.png; thumbnail 7. Tool config | thumbnail_7._Tool_config.png; thumbnail 2. Customer id variable usage before | thumbnail_2._Customer_id_variable_usage_before.png
bpmn_evidence_quote: "Your AI takes a huge step away from generating suggestions to executing decisions under human oversight."
ai_evidence: labels inside the figure name an AI element: Flowable | Workspaces | Models | Search | Overview | Customeronboarding | Generateddefault | Editing | DESIGN | Liability check agent | AlAssistant | Liability check agent (liabilityCheckAgent) | Capabilities | Capabilities | Agent type* | Operations
ai_evidence_quote: "Flowable | Workspaces | Models | Search | Overview | Customeronboarding | Generateddefault | Editing | DESIGN | Liability check agent | AlAssistant | Liability check agent (liabilityCheckAgent) | Capa"
artefacts:
  screenshot: 160_om-blog-releases-flowable-2025-2-governed-agentic-automation.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1920
capture_method: urllib download of https://images.ctfassets.net/chja9v5uur3u/4S9DgNb8C5yXvYo0e2If8C/4fe34c487ea803e97decb7d2a7dfb0e7/thumbnail_6._A2A_agent.png?fm=webp&q=75&bg=rgb%3Affffff&w=1920 (asset published by the page); labels inside read with RapidOCR, this session cannot receive image content
---

## Why this row is UNCERTAIN

The page publishes figures and mentions AI, but the figure that would decide the
verdict could not be certified from the evidence this session can read (the DOM, the
page text, and OCR labels). Per CLAUDE.md section 5 an unresolved figure is UNCERTAIN
with needs_visual_check, never an exclusion.

## Observations (description only, no interpretation)

- **Figures on the page:** thumbnail 6. A2A agent | thumbnail_6._A2A_agent.png; thumbnail 8. Agentforce config | thumbnail_8._Agentforce_config.png; thumbnail 7. Tool config | thumbnail_7._Tool_config.png; thumbnail 2. Customer id variable usage before | thumbnail_2._Customer_id_variable_usage_before.png
- **OCR labels of the captured figure:** Flowable | Workspaces | Models | Search | Overview | Customeronboarding | Generateddefault | Editing | DESIGN | Liability check agent | AlAssistant | Liability check agent (liabilityCheckAgent) | Capabilities | Capabilities | Agent type* | Operations
- **Page text quote:** Your AI takes a huge step away from generating suggestions to executing decisions under human oversight.
- **Captured asset:** https://images.ctfassets.net/chja9v5uur3u/4S9DgNb8C5yXvYo0e2If8C/4fe34c487ea803e97decb7d2a7dfb0e7/thumbnail_6._A2A_agent.png?fm=webp&q=75&bg=rgb%3Affffff&w=1920 (1920x1158)

## Sighted observations (visual pass elicitation-aa, shard s5, 2026-09-25)

Looked at all eleven content figures of the page natively (Contentful assets fetched
at 2000 px; site-wide CTA/stock/related-post images skipped by name). The census
capture for this n is `thumbnail_6._A2A_agent.png`, an agent-configuration form.

- **The page's only BPMN 2.0 diagram: no AI element inside the process.**
  `thumbnail_1._Add_verification_step_after.png` is the Flowable Design modeller on model
  "Customer onboarding": start event circle - user task **"Customer Verification"**
  (person icon) - user task **"Approval"** (person icon) - end event circle, with the
  palette listing Start event / User task / Subprocess / Call activity / Service task /
  Exclusive gateway. The right-hand panel is the **AI Assistant**, prompt "Add customer
  verification step before approval", reply "Added a customer verification step before the
  approval step by inserting a new form task and updating the sequence flows accordingly.",
  change summary "1 element repositioned / 1 element added - Customer Verification". The
  AI here **authored/edited** the model (outside the process), which per the worker brief
  is not an AI element inside the process.
- **AI elsewhere on the page, outside any drawn process.** `thumbnail_6._A2A_agent.png`
  (the census capture) and `thumbnail_8._Agentforce_config.png` are the agent-model editor
  for "Liability check agent (liabilityCheckAgent)": Agent type dropdown with Utility /
  Document / Knowledge / Orchestrator / External / A2A agent, and Agentforce fields
  (Salesforce URL, Agent ID, OAuth2 Registration Key). `thumbnail_7._Tool_config.png`
  lists tool `accountHistory - getAccountHistory` with an "Add tool" menu offering
  **Service** and **AI agent**. `thumbnail_5` is the Admin "Dashboard - Agents" with
  agent-invocation and agent-token-usage charts (agent names `issueAgent`,
  `sensitiveDataRemover`, `flowableKnowledgeBaseSearchAgent`, ...). `thumbnail_4` is the
  "Agents timeline" waterfall (Sensitive Data Remover, Knowledge Base Search, Issue agent;
  User Message / LLM call / Agent Response, token counts, JSON result). `thumbnail_2`
  before/after are the Design model list plus an AI Assistant answer about variable
  `customerId`. `thumbnail_9` and `thumbnail_10` are Flowable Work UI screens (a
  credit-request form and a task form) with no diagram.
- **Why UNCERTAIN rather than E2 (or E1).** BPMN 2.0 is genuinely present and the drawn
  diagram has no AI element, but the same Design app on the page couples a BPMN process
  to an agent model: the modeller tab bar carries a second, never-rendered model tab
  ("Account history"), and the page states "This release brings AI agents deeper into your
  processes". An AI/LLM service task bound inside a BPMN process therefore cannot be ruled
  out from the figures, so per CLAUDE.md ("an element's implementation might be AI-bound
  but is not visible" -> UNCERTAIN, never E2) the verdict stays UNCERTAIN.

## What to check

Whether the captured figure (or another figure on the page) is a BPMN 2.0 process
diagram and whether an AI/LLM element sits inside that process.
