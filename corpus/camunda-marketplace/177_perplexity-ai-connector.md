---
n: 177
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Perplexity AI Connector
url: https://marketplace.camunda.com/apps/632753/perplexity-ai-connector
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: BPMN diagram published as the listing's own assets (a Camunda Web Modeler canvas plus Operate instance views of the same process, 'New BPMN diagram', instance key 6755399441092369). Read natively: start event 'Registration Process Started' -> serviceTask 'Collect Location Details' -> userTask 'Approve the Location' -> gateway 'Approved?' -> 'Notify the user' on the yes-branch (end 'Registration successful') and end 'Registration unsuccessful' on the no-branch (the Operate view shows this last end event as reached).
bpmn_evidence_quote: "Collect Location Details"
ai_evidence: The AI call is the process's first service task, and the listing's own Operate view shows its output as a process variable: on the executed instance, 'Collect Location Details' holds the variable 'result' whose value is a Perplexity-generated answer with citations ('## Location of Delhi ... is located in north-central India[1][3]'). The page's own copy names the capability: 'Send prompts to Perplexity AI - Easily send natural language prompts to Perplexity AI directly from BPMN elements in Camunda', and 'Retrieve and use AI responses'.
ai_evidence_quote: "Send prompts to Perplexity AI"
artefacts:
  screenshot: 177_perplexity-ai-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own assets (d3bql97l1ytoxn.cloudfront.net, app_resources/632753/overview/img992245420848958327-2x.png 902x446 and screenshot/img6539867417407281274.png 902x405); native reads at full size - a Web Modeler canvas and an Operate instance view of the same process (the other two screenshots are the same Operate view at smaller size)
---

## What the page shows

The Perplexity AI Connector (Nagarro, connector template). The listing publishes a small approval process in which the first task queries Perplexity AI - the executed instance's answer about Delhi is shown in the Operate variables panel - after which a human approves the location and the customer is notified.

## Observations (description only, no interpretation)

- **AI activity - function:** a natural-language query to Perplexity AI whose answer is stored in a process variable.
- **AI activity - element type:** an ordinary `serviceTask` labelled 'Collect Location Details' carrying the connector's element-template glyph; no agent element and no ad-hoc container.
- **Authority - downstream:** the human approval task 'Approve the Location' and, through it, the notification and both end events - the AI output is subject to a human decision in the drawn flow.
- **Authority - data:** the process variable 'result' holding the AI's answered text (visible in the published Operate variables panel).
- **Authority - control:** the gateway 'Approved?' after the human task.
- **Authority - control (human):** the user task 'Approve the Location', which sits between the AI answer and any downstream action - a drawn human gate on the AI output.
- **Input provenance:** the prompt configured in the connector task; the instance shows no upstream data object.
- **Guards present:** the human approval before the branch; no confidence gate on the AI call itself.
- **Prompt / model detail visible:** the prompt text is not visible in the published views; the page names Perplexity AI and its API, and the Operate variable shows the answer with its citations.

## Notes for the researcher

Included because the AI element is inside the process and its effect is visible in the listing's own execution evidence: a service task whose runtime variable holds the model's cited answer, gated by a human approval step. Useful corpus example of an AI output that a drawn human task actually decides on.
