---
n: 1340
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: "Claims Processing Automation in Insurance: A Complete Guide"
url: https://camunda.com/blog/2023/10/claims-processing-automation-insurance-complete-guide/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "captured figure 1 (page alt \"Auto-claim-adjuster-tasks-bpmn-camunda\", 961x372 source): a BPMN pool with the rotated lane label \"Claim Adjuster\" containing the start event \"Start Adjuster Flow\", the tasks \"Generate Adjuster Document\", \"Generate Adjuster Email Content\", \"Notify Adjuster Email\" and \"Notify Adjuster Slack\", two parallel gateways (one opening the fork, one closing it), the user task \"View Vehicle/Submit Estimate\" and the end event \"Adjuster Complete\"; the page confirms both the notation and the colour coding - \"This process, represented in Camunda Modeler , shows user tasks in yellow, subprocesses in blue and Connector tasks in green.\""
bpmn_evidence_quote: "This process, represented in Camunda Modeler , shows user tasks in yellow, subprocesses in blue and Connector tasks in green."
ai_evidence: the task "Generate Adjuster Email Content" carries the OpenAI connector icon and sits on the fork of the adjuster sub-process, which the page annotates as the place where the OpenAI Connector composes the claimant email
ai_evidence_quote: "Camunda provides an out-of-the-box OpenAI Connector which is used to compose an email to the adjuster"
artefacts:
  screenshot: 017_claims-processing-automation-insurance-complete-guide.png
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

The post walks through an automobile claims process and dissects it system by system; the
captured figure 1 is the detail view of the adjuster work, drawn as a BPMN pool labelled
"Claim Adjuster". Inside it, "Start Adjuster Flow" leads to "Generate Adjuster Document"
(the Google Drive connector, per the page: "an adjuster estimate form is generated using the
Camunda Google Drive Connector with variables from the process to provide the adjuster with
a template to use while performing the estimate"), then a parallel gateway forks into
"Generate Adjuster Email Content" - the OpenAI-bound task - and "Notify Adjuster Slack",
which the page describes as "a Slack message is made using an out-of-the-box Slack
Connector"; the fork closes into the user task "View Vehicle/Submit Estimate" and the end
event "Adjuster Complete".

The AI element is therefore one parallel branch inside the adjuster sub-process, and the
page places it there explicitly: "Camunda provides an out-of-the-box OpenAI Connector which
is used to compose an email to the adjuster the claimant is waiting for an estimate". The page's only other AI-adjacent statement
is the connector's own description; this is not an article about agents - the model is
deterministic apart from the AI-generated email text.

## Observations (description only, no interpretation)

- **AI activity - function:** composing the claimant email - "Camunda provides an
  out-of-the-box OpenAI Connector which is used to compose an email to the adjuster"; in the
  figure that is the task "Generate Adjuster Email Content", which then hands to "Notify
  Adjuster Email".
- **AI activity - element type:** a BPMN service task bound to a connector - the page says
  the model shows "Connector tasks in green", and the OpenAI-bound task in the figure is an
  ordinary task box on the sequence flow, marked by the OpenAI connector icon.
- **Authority - downstream:** the generated email content flows into "Notify Adjuster Email"
  (which carries the SendGrid mark in the figure) in parallel with "Notify Adjuster Slack",
  and both branches close before the human step "View Vehicle/Submit Estimate".
- **Authority - data:** `not visible on the page` (the figure prints labels only; the page
  says the adjuster estimate form is generated "with variables from the process" but names
  no variable).
- **Authority - control:** the two parallel gateways that fork and join the branches, and
  the user task "View Vehicle/Submit Estimate" - the page describes it as the point where
  "The adjuster accesses a form that provides a link to the adjuster estimate template
  created and provides a location to enter the final estimate figure and any specific
  comments using a human task."
- **Input provenance:** the adjuster estimate document generated in the preceding task from
  process variables, i.e. the Google Drive-created template; the page says the estimate
  detail is entered by the adjuster afterwards.
- **Guards present:** the human task at the end of the branch - the adjuster's form is where
  the final estimate figure and comments are entered - and the page notes that connectors
  can be saved as templates "so that the required fields are pre-populated"; no review step
  of the AI-composed email itself is shown in this figure.
- **Prompt / model detail visible:** `not visible on the page` - no model name, prompt text
  or parameter appears anywhere in the post; the only statement is the connector sentence
  quoted above.

## Notes for the researcher

The post is largely non-AI content - the page text contains only two AI/LLM term hits - so
this record captures a single AI connector task inside a deterministic claims process,
which is a different arrangement from the agent posts in this source. The ruling named
figure 1 (the adjuster sub-process detail); the post's other process figure (figure 2, alt
"Auto-claim-process-bpmn-diagram-basic", 1200x231) shows the whole claims process and was
not captured. The downloaded file is 1400x542 although the source asset is 961x372; all
labels are readable, including the lane label "Claim Adjuster" which is drawn rotated. The
OpenAI connector icon on "Generate Adjuster Email Content" was confirmed by inspection, as
was the Google Drive icon on "Generate Adjuster Document" and the Slack icon on "Notify
Adjuster Slack".
