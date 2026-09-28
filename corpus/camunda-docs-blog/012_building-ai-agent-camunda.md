---
n: 248
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: Building Your First AI Agent in Camunda
url: https://camunda.com/blog/2025/02/building-ai-agent-camunda/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "captured figure 1 (page alt \"A BPMN model of an AI agent in an ad-hob sub-process using Camunda.\", 2053x815 animated GIF, 116 frames): a BPMN model with the start event \"Enter Details of Tax\", the tasks \"Decide on Likelihood of Fraud\", \"Decide Tasks to do\", \"Generate Email Inquiry\", \"Send Email\", \"Call on External Advisor\", a gateway labelled \"Is Fraud detected?\" with the \"No\" branch to the end event \"No Fraud!\" and the \"Yes\" branch into \"Throw Fraud\", a throw-event feeding a second \"Decide on Likelihood of Fraud\", the exclusive gateway \"Decision Made?\" with a \"No\" flow looping back to the first gateway and a \"Yes\" flow to the end event \"No Fraud Detected\", and the end event \"Fraud is detected\"; the expanded container that holds \"Generate Email Inquiry\", \"Send Email\", \"Call on External Advisor\" and \"Throw Fraud\" carries the tilde marker of an ad-hoc sub-process at its bottom edge"
bpmn_evidence_quote: "A BPMN model of an AI agent in an ad-hob sub-process using Camunda."
ai_evidence: the page binds the AI to the process explicitly - the OpenAI bot decides which tasks to run, and those tasks are the contents of the ad-hoc sub-process; in the captured figure the tasks "Decide on Likelihood of Fraud" and "Generate Email Inquiry" carry the OpenAI connector icon, and the task "Decide Tasks to do" sits immediately before the ad-hoc sub-process container whose members are the candidate tasks
ai_evidence_quote: "An OpenAI bot checks the data provided for any indication of fraud"
artefacts:
  screenshot: 012_building-ai-agent-camunda.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1400
capture_method: chrome-devtools-mcp page fetch; the figure's cdn.sanity.io URL decoded out of the page's /_next/image proxy, downloaded at w=1400; the published animation is kept beside the still as 012_building-ai-agent-camunda.gif (116 frames, first frame identical to the still)
---

## What the page shows

The guide builds a first AI agent and uses a fraud-detection process for tax-form
submissions as its example - "Our example model for this process is a fraud detection
process when submitting tax forms." The captured figure 1 is that model as an animated GIF
of the Web Modeler canvas (116 frames; the frames I read show the finished model): the tax
details enter at "Enter Details of Tax", "Decide on Likelihood of Fraud" and "Decide Tasks
to do" hand over to an expanded container holding the task list ("Generate Email Inquiry" ->
"Send Email", "Call on External Advisor", and a "Fraud Detected" -> "Throw Fraud" path
guarded by the gateway "Is Fraud detected?"), after which a second "Decide on Likelihood of
Fraud" and the exclusive gateway "Decision Made?" either loop back or finish at "No Fraud
Detected" / "Fraud is detected".

The container in the figure carries the tilde ad-hoc sub-process marker, and the page's
description of the pattern is that "the ad-hoc subprocess serves as a container where the
exact sequence and occurrence of tasks are not pre-defined but rather determined at
runtime".

## Observations (description only, no interpretation)

- **AI activity - function:** the AI bot inspects the submitted data and chooses the work -
  "An OpenAI bot checks the data provided for any indication of fraud. The AI bot will
  determine which tasks, from a list of tasks, to perform for this set of criteria."; the
  page also lists that AI agents "Make autonomous decisions about task execution".
- **AI activity - element type:** an AI agent implemented as a BPMN ad-hoc sub-process -
  "An AI agent is an automation within Camunda that leverages ad-hoc subprocesses to
  perform one or more tasks with non-deterministic behavior."; in the captured figure the
  container holds the tasks "Generate Email Inquiry", "Send Email", "Call on External
  Advisor" and "Throw Fraud".
- **Authority - downstream:** the tasks inside the ad-hoc sub-process, as printed in the
  figure: "Generate Email Inquiry", "Send Email", "Call on External Advisor" and the throw
  event "Throw Fraud"; the page names SendGrid and OpenAI connectors as the ones used in
  this model.
- **Authority - data:** `not visible on the page` (the figure shows labels only; no
  variables or data objects are printed, and the page text does not name the process
  variables either).
- **Authority - control:** the gateways "Is Fraud detected?" (inside the container, with
  "Yes" / "No") and "Decision Made?" (outside it, with a "No" flow looping back to the
  first gateway), plus the second "Decide on Likelihood of Fraud" task after the throw
  event.
- **Input provenance:** a tax-return form filled in by a user - "The process begins when a
  form is filled in by a user who wants to submit information for their tax return."
- **Guards present:** the ad-hoc sub-process is itself the constraint (the page: the
  approach "provides the AI agent some freedom, with constraints"); the model also carries
  the "Call on External Advisor" task and the "Decision Made?" gateway, both inside the
  process that wraps the container.
- **Prompt / model detail visible:** `not visible on the page` - the page names the OpenAI
  connector and a connector secret placeholder `{{secrets.yourSecretHere}}`, but prints no
  model id, prompt text or parameter; the figure prints no prompt either.

## Notes for the researcher

The page itself notes it was written against Camunda 8.7 functionality. Because the
captured artefact is a 116-frame GIF, what a reader sees depends on when the animation
stops: I read frame 1 (the finished model, with the mouse cursor visible), plus mid and
final frames of the same file, and they show the completed model rather than an empty
canvas. The downloaded file is 1400x556 although the source asset is 2053x815. The figure
was captured with the ruling's chosen figure 1; the page also carries a second model figure
(alt "Model-fraudfound") that I did not capture. The "AI agent" binding is visible in the
figure only through the ad-hoc sub-process container and the connector icons on "Decide on
Likelihood of Fraud" and "Generate Email Inquiry"; the OpenAI icon identity was checked by
zooming the frame, and the task "Decide Tasks to do" carries a different icon.
