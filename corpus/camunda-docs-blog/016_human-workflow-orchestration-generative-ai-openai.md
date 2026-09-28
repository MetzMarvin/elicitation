---
n: 1263
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: Facilitating Human Workflow Orchestration with Generative AI
url: https://camunda.com/blog/2023/05/human-workflow-orchestration-generative-ai-openai/
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: "The page states this Community Market vendor-evaluation process uses ChatGPT ('The process uses ChatGPT to extract important information from the text'), and the diagram's 'Extract information from vendor application' and 'Write personalized rejection email' tasks do carry small connector icons, but no label, template name or binding in the figure names the model. At native resolution I cannot resolve whether those icons are the OpenAI connector icon: is this AI binding to be accepted from the page prose plus the connector icon, or does it need a named AI element in the figure?"
needs_visual_check: true
bpmn_evidence: "captured figure 1 (page alt \"A BPMN diagram showing the evaluation process for the Community Market.\", 1200x474 source): a BPMN process with the start event \"Application received\", the tasks \"Extract information from vendor application\", \"Evaluate products\", \"Write description for website\", \"Write personalized rejection email\", \"Verify business address\", \"Notify applicant\" (used four times), the two user tasks \"Review vendor application\" and \"Review description\" and a third \"Review personalized rejection email\", the gateways \"Review application?\", \"Approve application?\", \"Rejected by?\" and two parallel gateways, the boundary timer \"every 14 days\" on \"Review vendor application\" with the branch to \"Notify team lead\" (end event \"Team lead notified\"), and the end events \"Application accepted\" and \"Application rejected\"; flows are labelled \"review\", \"rejected\", \"approved\", \"rejected by team\" and \"rejected automatically\""
bpmn_evidence_quote: "A BPMN diagram showing the evaluation process for the Community Market."
ai_evidence: three service tasks carry the OpenAI connector icon (the OpenAI mark, distinct from the person icon on the user tasks and the pin icon on "Verify business address") - "Extract information from vendor application", "Write description for website" and "Write personalized rejection email" - and the page names exactly those duties for ChatGPT
ai_evidence_quote: "The process uses ChatGPT to extract important information from the text such as the applicant's name, their email address, their business name and address"
artefacts:
  screenshot: 016_human-workflow-orchestration-generative-ai-openai.png
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

The post documents a hackathon example: a vendor evaluation process for a Community Market
in which generative AI drafts text and people decide. Its first figure is the model, and
the page's own account of it matches the labels: an application arrives and is evaluated, a
decision table rejects prohibited products ("There are certain types of products that are
not allowed at the market, such as alcohol, so the process uses a decision table to
automatically reject vendors that want to sell these products. ChatGPT writes a rejection
email based on the output of the decision table."), otherwise a team member reviews, and on
approval "the process uses ChatGPT to write a description for the Community Market website,
which a team member will review for accuracy."

In the captured figure the ChatGPT-bound tasks are visually distinct: "Extract information
from vendor application", "Write description for website" and "Write personalized rejection
email" each carry the OpenAI connector icon, while review steps carry a person icon,
"Verify business address" carries the Google Maps pin, and the notifications carry the
SendGrid mark. The rejection branch splits at the gateway "Rejected by?" into a human
review path ("rejected by team" -> "Review personalized rejection email") and an automatic
one ("rejected automatically" -> "Notify applicant").

## Observations (description only, no interpretation)

- **AI activity - function:** writing and extraction on the page's own account - "ChatGPT
  writes a rejection email based on the output of the decision table" and the process "uses
  ChatGPT to write a description for the Community Market website"; the figure also puts
  the OpenAI connector on "Extract information from vendor application", a task the page
  does not otherwise mention in the paragraphs quoted here.
- **AI activity - element type:** BPMN service tasks whose implementation is the OpenAI
  Connector - the page names the connector for the rejection email ("ChatGPT writes a
  rejection email based on the output of the decision table") and the figure marks the
  tasks with the connector's icon.
- **Authority - downstream:** the AI-generated text is consumed by human review and then by
  notification tasks - in the figure "Review description" and "Review personalized
  rejection email" both lead into "Notify applicant" tasks, and the page states that the
  process "leverages the OpenAI , Slack , Google Maps , and SendGrid Connectors".
- **Authority - data:** `not visible on the page` (no variables or data objects are printed
  in the figure, and the page names none for this process).
- **Authority - control:** the gateways "Review application?", "Approve application?" and
  "Rejected by?", the boundary timer "every 14 days" that diverts an undecided application
  to "Notify team lead", and the human tasks that must pass before anything is sent - the
  page: "a team member reviews the email and decides whether to approve or reject the
  application."
- **Input provenance:** the vendor's application - the start event is "Application received",
  and the page describes the process as handling an application by a vendor who wants to
  sell at the market.
- **Guards present:** human review of AI output before it leaves the process - the page
  states that BPMN "makes it easy to enforce the requirement that AI-generated text is
  reviewed and validated", and the figure shows "Review description" and
  "Review personalized rejection email" between the OpenAI tasks and the notification
  tasks. The page also warns about sending sensitive data to such a tool.
- **Prompt / model detail visible:** `not visible on the page` - no model name, prompt text
  or parameter is printed; the page names the OpenAI Connector, ChatGPT and the OpenAI
  Moderation API, and says the connector requires an API key, but shows no prompt.

## Notes for the researcher

This is the oldest post among my assignments (May 2023) and it is written around the
OpenAI Connector rather than around agents: the AI elements are plain connector tasks, not
ad-hoc sub-processes. The downloaded file is 1400x553 although the source asset is
1200x474. The figure's connector icons were verified by zooming; the icon on "Evaluate
products" is a table icon (not the OpenAI mark) and the OpenAI mark on "Extract information
from vendor application" was confirmed at 3x. The page also carries no second process
figure, so figure 1 is the whole artefact.
