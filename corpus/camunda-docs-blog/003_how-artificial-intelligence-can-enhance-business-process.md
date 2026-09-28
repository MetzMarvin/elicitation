---
n: 9
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: How Artificial Intelligence can Enhance Your Business Process
url: https://camunda.com/blog/2024/02/how-artificial-intelligence-can-enhance-business-process/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: the captured figure is the Camunda Modeler canvas the page's BPMN sentence refers to, read at full width - a pool with the lane "Claim Adjuster", the start event "Start Adjuster Flow", the task "Generate Adjuster Document", the task "Generate Adjuster Email Content", two diamond gateways carrying an X marker, and the tasks "Notify Adjuster Email" and "Notify Adjuster Slack"; the properties panel on the right is headed "OPENAI CONNECTOR" over an element template, and the bottom drawer's breadcrumb reads "Bpmn:ServiceTask / Prompt"
bpmn_evidence_quote: "Using this Connector within your process models allows you to incorporate AI into any business process."
ai_evidence: the BPMN service task "Generate Adjuster Email Content" is bound to the OpenAI Connector element template - the properties panel shows Authentication (OpenAI API key fx = secrets.OPENAI_KEY), Operation "Chat", Model "GPT-3.5-turbo" and a Prompt field holding a FEEL expression, i.e. the task's implementation is the LLM call itself
ai_evidence_quote: In the simple BPMN example below, you can see a service task that accesses an AI engine to read a customer request
artefacts:
  screenshot: 003_how-artificial-intelligence-can-enhance-business-process.png
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

The post is a general argument that AI helps business process work, and in its middle it
names the mechanism it means: "Camunda provides out of the box Connectors, including one for
Open AI . Using this Connector within your process models allows you to incorporate AI into
any business process." The figure captured here is the model that sentence sits next to: an
open Camunda Modeler with a pool containing the lane "Claim Adjuster", a "Start Adjuster
Flow" start event into "Generate Adjuster Document", the gateway fork to "Generate Adjuster
Email Content" and "Notify Adjuster Slack", a second gateway, and the outgoing "Notify
Adjuster Email".

The AI element is the task "Generate Adjuster Email Content": it carries the OpenAI logo on
the canvas and is selected, so the right-hand properties panel shows its connector
configuration - Authentication (OpenAI API key `fx`, `secrets.OPENAI_KEY`; Organization
`fx`), Payload with Operation "Chat" and Model "GPT-3.5-turbo", empty System message and
Chat history fields, and a bottom drawer headed "Bpmn:ServiceTask / Prompt" holding the FEEL
prompt expression.

## Observations (description only, no interpretation)

- **AI activity - function:** the page says the task reads a business input and classifies
  it - "you can see a service task that accesses an AI engine to read a customer request and
  make a determination as to the nature of that request so it is properly routed"; the same
  connector is also described as generating text: "the OpenAI Connector is being used to
  generate a targeted and specific email to a customer providing a status update."
- **AI activity - element type:** a BPMN service task whose implementation is an element
  template - the panel header reads "OPENAI CONNECTOR / Generate Adjuster Email Content" and
  the drawer breadcrumb reads "Bpmn:ServiceTask / Prompt", so the AI binding is a task
  implementation binding, not a new node type.
- **Authority - downstream:** the captured figure shows the AI task's output flowing through
  a gateway to the notification tasks "Notify Adjuster Email" and "Notify Adjuster Slack";
  the page describes the outcome as the request being "properly routed".
- **Authority - data:** the prompt expression reads the process variables
  `policyholderName`, `policyholderPhone` and a third beginning `policyholderEma` (cut off at
  the right edge of the drawer); authentication reads `secrets.OPENAI_KEY`; no output
  variable name is shown.
- **Authority - control:** the two diamond gateways with X markers drawn between the tasks
  in the captured figure; the selection state shows the model is still being edited
  ("Problems 6", "Zeebe 8.3").
- **Input provenance:** the customer/policyholder's own details arriving as process
  variables (`policyholderName`, `policyholderPhone`, ...), consistent with the page's
  "incoming customer requests" framing.
- **Guards present:** not visible on the page - the captured figure shows only the AI task,
  gateways and notification tasks; no review or confirmation step is drawn or named on the
  page.
- **Prompt / model detail visible:** yes - Model "GPT-3.5-turbo"; Operation "Chat";
  System message (empty, `fx`); Chat history (empty, `fx`, helper text "Optional chat
  history, or examples of the desired model behaviour"); and the user prompt as a FEEL
  expression: "Prepare a short email to Camundanzia Adjuster saying that the vehicle owner "
  concatenated with `policyholderName`, `policyholderPhone` and a third variable beginning
  `policyholderEma`. The OpenAI API key field holds `secrets.OPENAI_KEY`.

## Notes for the researcher

The captured asset is a Modeler screenshot rather than a rendered diagram, and the AI
evidence in it is unusually complete for a blog: the connector's element-template panel is
open on exactly the AI-bound task, so model name, operation, credential secret and prompt
template are all readable in the same image. The source asset on cdn.sanity.io is 1190x702;
requesting w=1400 upscales it to the 1400x826 file that landed on disk. The page has six
figures in all; only the connector figure (alt "Connectors-ai") carries the AI-bound task,
and the two "Process-optimization-ai" / "Interpreting-data-ai" cells are bar-chart style
illustrations rather than process diagrams.
