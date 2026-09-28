---
n: 165
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: AI Communication Agent
url: https://marketplace.camunda.com/apps/808027/ai-communication-agent
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: Five .bpmn files published (reached through the listing's own Modeler import links): 1-communication-agent, 2-message-intake, 3-message-outbound, 4-business-agent-calculator and 5-business-agent-translator. Read from the XML: 1-communication-agent runs start event 'Customer message received' -> ad-hoc sub-process 'Communication Agent' -> sendTasks 'Forward to "Calculator Agent"' and 'Forward to "Translator Agent"' -> callActivity 'Reply to customer' -> end 'Session ended'; 2-message-intake fans three channels (email, SMS, chat) into the script task 'Run AI firewall' -> gateway 'Is message safe?' -> the business rule task 'Find customer context' -> gateway 'Customer found?' -> end 'Propagate message to communication agent'; the published overview asset is a building-block illustration (labelled 'Building Block'), not a BPMN canvas.
bpmn_evidence_quote: "Customer message received"
ai_evidence: Decisive, from the process files: the ad-hoc sub-processes 'Communication Agent', 'Translator Agent' and the service task 'Solve math problem' are bound to Camunda's agentic-AI templates (`io.camunda.connectors.agenticai.aiagent.jobworker.v1` and `io.camunda.connectors.agenticai.aiagent.v1`), and the intake process contains the script task 'Run AI firewall' feeding the gateway 'Is message safe?' with the end events 'AI firewall failed' and 'Message rejected by AI firewall'. The page's own copy states the mechanism: 'Uses LLM reasoning to interpret customer intent and dynamically route requests to the appropriate business service'.
ai_evidence_quote: "Uses LLM reasoning to interpret customer intent and dynamically route requests to the appropriate business service"
artefacts:
  screenshot: 165_ai-communication-agent.png
  archive: null
  bpmn_xml: 165_ai-communication-agent.bpmn
duplicate_of: null
access: public
capture_source: bpmn-xml
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own asset (d3bql97l1ytoxn.cloudfront.net, app_resources/808027/overview/img15306768265583167352-2x.png, 1100x604) and of the .bpmn files reached through the listing's own Modeler import links; the image read natively at full size, the XML read directly
---

## What the page shows

The AI Communication Agent (Camunda Services GmbH, blueprint/pattern). The listing publishes five processes that together form a multi-channel AI engagement layer: an intake process with an AI firewall, a communication agent that routes a customer message to business agents, an outbound process, and two business agents (a calculator and a translator).

## Observations (description only, no interpretation)

- **AI activity - function:** LLM intent detection and routing of customer messages, plus two business agents (calculator, translator) and an AI firewall that screens incoming messages.
- **AI activity - element type:** two ad-hoc sub-processes ('Communication Agent', 'Translator Agent') and one service task ('Solve math problem') bound to Camunda's agentic-AI templates, plus the script task 'Run AI firewall' with its safe/unsafe gateway; the published overview image is a vendor building-block illustration rather than a BPMN canvas.
- **Authority - downstream:** the message's routing to the correct business service, the reply back through the customer's channel ('Reply to customer' call activity, outbound send tasks) and, on the intake side, the rejection path.
- **Authority - data:** message context extracted per channel by script tasks ('Extract message context from SMS / Email / message / chat') before the firewall and the intent routing.
- **Authority - control:** the intake gateways 'Message context complete?', 'Is message safe?' and 'Customer found?', and the routing decision inside the communication agent.
- **Authority - control (human):** none visible in the published processes - the firewall, the intent routing and both business agents run without a user task.
- **Input provenance:** customer messages from email, SMS and chat starts events, plus 'Generic message from customer received'.
- **Guards present:** the AI firewall with its 'Message rejected by AI firewall' / 'AI firewall failed' exits, and the customer-context and completeness gateways.
- **Prompt / model detail visible:** none - the XML names the agent templates but no model or prompt; the page says the pattern works with any LLM Camunda supports ('OpenAI, Azure OpenAI, Ollama, and beyond').

## Notes for the researcher

The largest agentic artefact in this batch by far: five processes, two agent containers, an AI firewall with its own rejection path and no human step anywhere. Note for the corpus that the published overview image is a building-block illustration and that the BPMN evidence sits entirely in the downloadable process files, which the listing's own Modeler import links expose.
