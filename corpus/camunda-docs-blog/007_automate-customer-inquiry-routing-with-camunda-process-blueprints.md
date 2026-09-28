---
n: 130
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: Automate Customer Inquiry Routing with Camunda’s Process Blueprint and Azure OpenAI
url: https://camunda.com/blog/2024/08/automate-customer-inquiry-routing-with-camunda-process-blueprints/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: the captured figure is a BPMN workflow diagram, read at full width - start event "inquiry process started", the user task "Enter inquiry (customer)", the task "Determine routing (AI)", exclusive gateways with X markers labelled "route to which department?" and "inquiry response", the four user tasks "Work on inquiry (default)", "Work on inquiry (Sales team)", "Work on inquiry (Engineering team)" and "Work on inquiry (Legal team)" with the flows "other", "sales", "technical", "legal", the intermediate events "retry with feedback" and "route to different team", the flow "resolved" and the end event "inquiry resolved"
bpmn_evidence_quote: "This use case uses AI to determine the correct routing for a customer inquiry. You can see the BPMN for this process below."
ai_evidence: the BPMN task "Determine routing (AI)" is the AI step the page documents - "the first human task is providing a customer inquiry that will be routed using the results of the OpenAI Connector" - and the page names the implementation as the Azure OpenAI Connector whose "resulting expression ... will provide the route determined by OpenAI", feeding the "route to which department?" gateway
ai_evidence_quote: In Modeler, you see that the first human task is providing a customer inquiry that will be routed using the results of the OpenAI Connector.
artefacts:
  screenshot: 007_automate-customer-inquiry-routing-with-camunda-process-blueprints.png
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

The post walks through a Camunda blueprint called "Intelligent Routing with AI", and its own
BPMN figure is the captured one: "This use case uses AI to determine the correct routing for
a customer inquiry. You can see the BPMN for this process below." Read at full width the
diagram runs from the start event "inquiry process started" into the user task "Enter
inquiry (customer)", then the task "Determine routing (AI)", then an exclusive gateway, then
a second exclusive gateway labelled "route to which department?" whose flows "other",
"sales", "technical" and "legal" lead to the four user tasks "Work on inquiry (default)",
"Work on inquiry (Sales team)", "Work on inquiry (Engineering team)" and "Work on inquiry
(Legal team)". The branches merge into the gateway "inquiry response", which either reaches
the end event "inquiry resolved" via "resolved" or loops back through the intermediate
events "retry with feedback" and "route to different team" into the AI task.

The AI element is a first-class task in the model, named for what it does - "Determine
routing (AI)". The page supplies its implementation: "In this post, we'll use one of those
blueprints to showcase our new Azure OpenAI Connector", the prompt is entered as "If is
defined(feedback) then feedback else customer_inquiry", and the temperature is set to 1.

## Observations (description only, no interpretation)

- **AI activity - function:** the routing decision - "This use case uses AI to determine the
  correct routing for a customer inquiry"; the page describes the connector's output as "the
  resulting expression that will provide the route determined by OpenAI".
- **AI activity - element type:** a BPMN task labelled "Determine routing (AI)", drawn with a
  cog/service-task icon in its top-left corner; the implementation is the out-of-the-box
  Azure OpenAI Connector, i.e. a task with an AI connector binding rather than a new node
  type.
- **Authority - downstream:** the gateway "route to which department?" and its four outgoing
  flows "other", "sales", "technical", "legal" into the human tasks "Work on inquiry
  (default / Sales team / Engineering team / Legal team)"; the page frames the result as
  being used for routing: "the first human task is providing a customer inquiry that will be
  routed using the results of the OpenAI Connector".
- **Authority - data:** the form field "Customer message" is "stored in the process variable
  noted by customer_inquiry"; the second variable is `feedback` - "the prompt uses
  customer_inquiry if the feedback process variable is not yet defined"; the page's prompt
  expression is "If is defined(feedback) then feedback else customer_inquiry".
- **Authority - control:** the exclusive gateway that consumes the model's route, the four
  human "Work on inquiry (...)" tasks, and the two loop-back paths ("retry with feedback",
  "route to different team") that re-enter the AI task; the page adds "You can provide
  feedback and send this through OpenAI again, reroute to another department, or resolve the
  item."
- **Input provenance:** the customer's own message - "Most likely, this prompt would come
  from an SMS text message or an email, or this could also be our Contact Us page for asking
  questions on our website."
- **Guards present:** the outcome of the AI routing always lands on a human task ("Work on
  inquiry (...)"), and the loop-back flows force a re-run through the AI task with additional
  feedback; no separate approval or confirmation gate on the AI output is shown in the
  captured figure.
- **Prompt / model detail visible:** yes - the prompt expression "If is defined(feedback)
  then feedback else customer_inquiry" and the sampling setting: "You must also define a
  Temperature that controls the randomness of the model’s output. For this example, select a
  temperature of 1 , which is the midrange temperature." The credential prerequisite is
  stated ("you must have an API key for Azure OpenAI"); no deployment or model name is
  printed in the brief. The page's other figures include "Pop-up window showing System
  message and Chat history for the Payload" and "Properties form showing optional fields for
  the OpenAI outbound connector".

## Notes for the researcher

This is the strongest of the eight records in this batch on the input/parameter side: the
page prints the actual FEEL prompt expression, the process variables it reads and the
temperature setting. The captured asset is small on the CDN (622x273) and the w=1400
download is an upscale, but it is a clean line diagram and every label named above is
readable in the captured file. The figure captured is not one of the two "selected" cells -
it sits further down the page's figure list, which is why it is reached with `shotall`. The
page has 19 figures in total, several of which are Modeler UI screenshots (form JSON, the
connector's System message / Chat history pop-up, the sequence-flow form) that a second pass
could mine for further parameter detail.
