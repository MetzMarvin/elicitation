---
n: 225
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: AI Firewall Agent
url: https://marketplace.camunda.com/apps/808028/ai-firewall-agent
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: Two downloadable BPMN files. (1) 'safeguard-agent': startEvent 'Prompt received' -> serviceTask 'Safeguard user prompt' (bound to io.camunda.connectors.agenticai.aiagent.v1, task type io.camunda.agenticai:aiagent:1) -> exclusiveGateways 'User prompt within size limit?', 'Confidence level sufficient?', 'Output conforms to JSON schema?', 'Limit of tries reached?' -> scriptTask 'Refine system prompt' and scriptTask 'Retain history of results' -> boundaryEvent 'Error within agent task occurred' -> intermediateThrowEvents 'User prompt too large', 'Agent output malformed', 'AI Agent task failed', 'Limit of tries exceeded' -> endEvent 'Return safeguard result', with escalations 'primary AI failed', 'safeguard_bad-agent-output', 'safeguard_task-agent-failed', 'safeguard_max-iterations-reached'. (2) 'Safeguard Agent Usage Example': startEvent 'Process started' -> callActivity 'Run AI Firewall on user prompt' -> endEvent 'Process ended', with separate escalation-catching paths that each 'Create an incident'. The published figure shows the same block as a 'Building Block' slide: green checks 'Threat classification', 'Prompt sanitization / size check', 'Confidence score', start event 'Safeguard User Prompt', ends 'Safe prompt' and 'Unsafe prompt'.
bpmn_evidence_quote: "Safeguard user prompt"
ai_evidence: The guard itself is an AI agent: the task 'Safeguard user prompt' is bound to Camunda's agentic AI agent template (io.camunda.agenticai:aiagent:1), and the page says 'Safeguard AI-powered processes from unsafe prompts', 'Classify threats before they reach AI tasks', 'Classify threats before they reach AI tasks :: The agent classifies injection, jailbreak, harmful intent, policy evasion, sensitive data, privacy, obfuscation, and tool manipulation threats', with 'Retry automatically on low-confidence decisions' (confidence threshold, prompt refinement and automatic retry) and 'Connect to any supported AI provider :: Works with any LLM supported by Camunda: OpenAI, Azure OpenAI, Ollama, and beyond.' The page also states it 'Includes an automated test suite that validates prompt classification against a real LLM, covering block, warn, and allow scenarios out of the box.'
ai_evidence_quote: "Safeguard AI-powered processes from unsafe prompts"
artefacts:
  screenshot: 225_ai-firewall-agent.png
  archive: null
  bpmn_xml: 225_ai-firewall-agent.bpmn
duplicate_of: null
access: public
capture_source: bpmn-xml
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own assets - the published 'Building Block' figure (d3bql97l1ytoxn.cloudfront.net, app_resources/..., img7761992142663287634-2x.png, 1100x604) read natively at full size - plus both .bpmn files reached through the listing's own resource links, read directly
---

## What the page shows

The AI Firewall Agent (Camunda, open source, pattern/blueprint, 8.8/8.9). An agentic guard task that classifies an incoming prompt as safe or unsafe, sanitises or blocks it, scores its own confidence, retries with a refined prompt when confidence is low, and raises an incident (via callActivity) when it fails.

## Observations (description only, no interpretation)

- **AI activity - function:** classify the user prompt against threat categories (injection, jailbreak, harmful intent, policy evasion, sensitive data, privacy, obfuscation, tool manipulation), return a sanitised prompt plus a confidence score, and retry on low confidence.
- **AI activity - element type:** a serviceTask bound to the Camunda agentic AI agent element template (io.camunda.connectors.agenticai.aiagent.v1 / io.camunda.agenticai:aiagent:1) - an AI Agent element, not a plain connector call.
- **AI activity - models named:** none in the files; the page says any LLM supported by Camunda (OpenAI, Azure OpenAI, Ollama, 'and beyond').
- **Authority - downstream:** the agent's verdict is the branch: the usage-example callActivity returns a result, and each escalation path (prompt too large, agent output malformed, agent task failed, retries exceeded, bad agent output) leads to 'Create an incident'.
- **Authority - control (in-process):** four exclusive gateways test the agent's output - size limit, confidence level, JSON-schema conformance, try limit - and scriptTasks 'Refine system prompt' (re-prompt) and 'Retain history of results' (memory) feed the retry loop; escalations are modelled as BPMN escalation events, not just error codes.
- **Guardrails named:** the threat taxonomy, the confidence threshold with bounded retries, prompt sanitisation that preserves legitimate intent, a size limit, and a test suite covering block/warn/allow scenarios against a real LLM.
- **Data reachable by the model:** the user prompt (and, from 'Retain history of results' / 'Refine system prompt', the conversation's own history and system prompt).
- **Human role:** none in the files; the guard is fully automatic and reports failures as incidents.

## Notes for the researcher

An AI agent whose *job* is to police other AI tasks - a guardrail pattern rather than a business process, and the only listing in this batch where the AI element's own reliability machinery (confidence gateway, refine-and-retry loop, schema check, bounded tries) is modelled explicitly in BPMN. The published figure is a 'Building Block' slide rather than a canvas, so the two .bpmn files carry the record (the standing .bpmn-first rule, cf. n=136, n=188).
