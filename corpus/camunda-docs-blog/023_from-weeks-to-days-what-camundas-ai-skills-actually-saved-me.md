---
n: 1413
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: From Weeks to Days: What Camunda's AI Skills Actually Saved Me | Camunda
url: https://camunda.com/blog/2026/08/from-weeks-to-days-what-camundas-ai-skills-actually-saved-me/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: the captured figure is a BPMN model - a start event "Policy Change Request Submitted", rounded-rectangle tasks, message and timer intermediate events ("Policy Change" message into "Short Wait" timer), boundary events on tasks ("Policy Not Found", "Invalid / Indelgible", "Invalid DL Escalation", "SLA Violation"), exclusive and parallel gateways with X and plus markers and labelled flows ("Changes Made?", "Who takes control?" with "agent" / "human", "Upsell or Complete?" with "Complete" / "Should Upsell"), one large container labelled "Policy Change Agent" carrying the purple star badge and the ad-hoc tilde at its bottom edge, two dashed/dotted sub-frames inside it ("Policy Changes", "Asking an Expert") and a dotted escalation frame outside it ("Human control required"), and end events ("No Policy Found", "Policy Updated", "Upsell Completed", "Policy Updated by Human", "Exit for Invalid DL", "Exit for SLA Violation")
bpmn_evidence_quote: "BPMN is the open standard for modeling a business process as a diagram."
ai_evidence: the process contains a BPMN ad-hoc sub-process - the container labelled "Policy Change Agent" (purple star badge, tilde at its bottom edge) - whose steps are named as agents ("Validate / Add a Driver AI Agent", "Underwrite / Rate AI Agent"), and further agent-labelled tasks sit outside it ("Parse AI Agent Metrics", "Upsell Products Agent"); the page states both the container's role and the escalation design - "The process itself took shape in Modeler exactly the way I described it: submit a change, route by risk, land on a review step before anything's applied. The agent can call a human gate tool when it needs expert input before proceeding."
ai_evidence_quote: "I needed to build an end-to-end full Policy Change for automobile insurance process with AI agents."
artefacts:
  screenshot: 023_from-weeks-to-days-what-camundas-ai-skills-actually-saved-me.png
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

The post is a first-hand account of building an automobile-insurance policy change process
with Camunda's AI Skills driving a coding assistant, and its second figure (alt "The
resulting policy change process") is the process that came out of it. The model starts at
"Policy Change Request Submitted" into "Policy Validation" (which carries a REST glyph and a
"Policy Not Found" boundary event leading to "Email Customer Policy Not Found" and the end
event "No Policy Found"), then "Display Policy Change Request", "Email Application Received"
(a "Policy Change" message and a "Short Wait" timer feed into it), "Pre-checks before full
data capture" (with the "Invalid / Indelgible" boundary event), "Preliminary Risk Score",
"Prepare Change Prompt".

The centre of the model is the large purple container "Policy Change Agent" - purple star
badge at its top-left corner, ad-hoc tilde at its bottom edge - holding the dashed frame
"Policy Changes" with "Validate / Add a Driver AI Agent" and "Update Policy", the tasks
"Determine Upselling Opportunities", "Summarize Changes", "Underwrite / Rate AI Agent", the
dotted frame "Capture Duplicate Requests" with "Update Conversation", and the dashed frame
"Asking an Expert" with the human task "Ask an Expert", the gateway "Who takes control?"
("agent" into the "Expert Asked" event, "human" into the "Human Control" escalation event).
After the container the flow runs through "Parse AI Agent Metrics", "Changes Made?", "Bind
Policy", "Email Policy Update Complete" and "Upsell or Complete?" into "Upsell Products
Agent" (end event "Upsell Completed") or directly to the end event "Policy Updated"; the
"No" branch of "Changes Made?" runs through "AI Evaluation of Case Handling" and the human
task "Review AI Handling of Change". A dotted "Human control required" frame outside the
container holds "Handle Policy Change Exception" and ends at "Policy Updated by Human", and
two further boundary events, "Invalid DL Escalation" and "SLA Violation", lead to "Invalid
DL Escalation" / "Supervisor Escalation" with "Back to AI?" or "Exit for SLA Violation".

## Observations (description only, no interpretation)

- **AI activity - function:** the page describes the work the agents do as "Flagging an
  expert (human-in-the-loop) when unsure of steps to take" and "Based on the changes, binds
  the policy and tracks to a second AI agent to build a path for upselling new offerings";
  the figure names the agent steps themselves ("Validate / Add a Driver AI Agent",
  "Underwrite / Rate AI Agent", "Parse AI Agent Metrics", "Upsell Products Agent").
- **AI activity - element type:** one BPMN ad-hoc sub-process configured as an agent - the
  container "Policy Change Agent" (purple star, ad-hoc tilde) holding its task set - plus
  individual agent-bound tasks outside it; the page describes the whole model as "The process
  itself took shape in Modeler exactly the way I described it: submit a change, route by
  risk, land on a review step before anything's applied."
- **Authority - downstream:** the steps inside the container ("Validate / Add a Driver AI
  Agent", "Update Policy", "Determine Upselling Opportunities", "Summarize Changes",
  "Underwrite / Rate AI Agent", "Ask an Expert", "Update Conversation") and, after it, "Bind
  Policy", "Email Policy Update Complete" and "Upsell Products Agent"; the page adds that the
  process "binds the policy and tracks to a second AI agent to build a path for upselling new
  offerings".
- **Authority - data:** `not visible on the page` for the AI element (the figure prints
  labels only, and no variable the agent writes is named). The page does name the inputs of
  the routing decision - "By taking in risk scores, motor vehicle lookup results,
  comprehensive loss underwriting exchange results, and additional criteria, a decision risk
  is determined using business rules."
- **Authority - control:** the gateways "Changes Made?", "Who takes control?" ("agent" /
  "human"), "Upsell or Complete?" ("Complete" / "Should Upsell"), the human tasks "Ask an
  Expert", "Review AI Handling of Change" and "Handle Policy Change Exception", and the
  escalation boundary events "Invalid DL Escalation" and "SLA Violation" leading to the
  "Supervisor Escalation" step with its "Back to AI?" and "Exit for SLA Violation" flows.
- **Input provenance:** the start event "Policy Change Request Submitted" and, on a separate
  path, the message event "Generic message from customer received" into "Extract message
  context from message"; the page summarises the entry as "submit a change, route by risk,
  land on a review step before anything's applied".
- **Guards present:** the human task "Ask an Expert" behind the "Who takes control?" gateway
  (the page calls this "Flagging an expert (human-in-the-loop) when unsure of steps to take"
  and "The agent can call a human gate tool when it needs expert input before proceeding.
  That's orchestration from the inside."), the "Human Control" escalation event, the "Human
  control required" frame with "Handle Policy Change Exception", and the review task "Review
  AI Handling of Change" after "AI Evaluation of Case Handling".
- **Prompt / model detail visible:** no model id and no prompt text are printed; the figure
  contains a step named "Prepare Change Prompt", which is the closest the artefact comes to
  prompt content. The page names the coding assistant, not the in-process model: "I took
  advantage of Camunda's AI Skills with Claude Code and it completely changed the experience."

## Notes for the researcher

The captured figure is the post's own process diagram, and its agent elements are readable at
1400 px after enlarging (the "Policy Change Agent" container with its purple star and tilde,
the "... AI Agent" task names, the "Who takes control?" gateway with its agent / human
flows). Two other figures on the page - "AI Agent Tool Optimize dashboard showing tool calls
made by agents" and "AI Agent Token Metrics with Optimize" - are Optimize dashboards over the
same process and would carry the tool-call evidence; the rulings file names the process
figure, so only that one is captured. The page also shows "A DMN decision table for deciding
on risk" and an HTML portal screenshot.
