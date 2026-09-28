---
n: 292
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: "Intelligent by Design: A Step-by-Step Guide to AI Task Agents in Camunda"
url: https://camunda.com/blog/2025/05/step-by-step-guide-ai-task-agents-camunda/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "captured figure 2 (page alt \"Sub-process\", 1200x526 source): a screenshot of the Camunda Web Modeler canvas (header \"Modeler > Home > AI Agent Tutorial JJ > AI Agent Tutorial > Message Delivery Service\", tabs \"Design | Implement | Play\", \"Autosaved at 15:57:40\") showing a BPMN process whose elements are labelled start event \"Message needs to be sent\", the task \"Create Prompt\", the task \"AI Task Agent\" and the end event \"Message delivered\"; the BPMN element palette is visible on the left (start and end event circles, gateway diamonds, task rectangles, the expanded sub-process entry) with the palette entry \"Create expanded sub-process\" outlined in red and a red callout repeating that label"
bpmn_evidence_quote: "Sub-process"
ai_evidence: the canvas contains a task labelled "AI Task Agent" sitting between "Create Prompt" and the end event "Message delivered"; the page describes the agent as built from the BPMN ad-hoc sub-process construct and names this model as its example
ai_evidence_quote: "At the core of this approach is our use of the BPMN ad-hoc sub-process construct, which allows for tasks to be executed in any order"
artefacts:
  screenshot: 015_step-by-step-guide-ai-task-agents-camunda.png
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

The post is a step-by-step tutorial for building an AI Task Agent, and its example model is
a message delivery service: "Our example model for this process is the Message Delivery
Service as shown below." The captured figure 2 is a live Web Modeler screenshot of that
process in its first state - the start event "Message needs to be sent", the task "Create
Prompt", the task "AI Task Agent" and the end event "Message delivered" - with the palette
entry "Create expanded sub-process" outlined in red and pointed at by a red callout, i.e.
the figure is the step in which the modeller is told to create the container the agent will
live in.

The page's explanation of what that container does is printed in the same section: "The
tasks that can be performed are located in the ah-hoc sub-process and are:", followed by
the list beginning "Request additional information (Ask an Expert) with a User Task and
corresponding form."

## Observations (description only, no interpretation)

- **AI activity - function:** the post's framing is that the ad-hoc sub-process is where
  LLM-driven choice happens - the page calls it the agent's decision workspace, "a flexible
  execution container where large language models (LLMs) can assess available actions"; in
  the captured figure the agent appears only as the task "AI Task Agent", with no tool
  tasks drawn around it yet.
- **AI activity - element type:** a named BPMN task, "AI Task Agent", on the ordinary
  sequence flow of the process; the page's construct for it is the ad-hoc sub-process -
  "At the core of this approach is our use of the BPMN ad-hoc sub-process construct, which
  allows for tasks to be executed in any order".
- **Authority - downstream:** `not visible on the page` in this figure (the container is
  not yet drawn); the page lists the tasks that will live in the ad-hoc sub-process,
  including "Request additional information (Ask an Expert) with a User Task and
  corresponding form."
- **Authority - data:** `not visible on the page` (the canvas shows labels only; the page
  section describing this step names no variables for the agent task).
- **Authority - control:** the sequence flow of the outer process - "Message needs to be
  sent" -> "Create Prompt" -> "AI Task Agent" -> "Message delivered" - which places the
  agent task under the process's own start and end events.
- **Input provenance:** the task labelled "Create Prompt" immediately precedes the agent
  task, so the prompt is prepared in the process itself; the page does not say in this
  section what the message content is.
- **Guards present:** `not visible on the page` in this figure; the page describes the
  wider model as deterministic process logic wrapped around the agent's container.
- **Prompt / model detail visible:** `not visible on the page` (the figure shows the model
  canvas, not the task properties; the page names the AI Agent Outbound connector and the
  Embeddings Vector Database Outbound connector elsewhere but prints no prompt text or model
  id in this section).

## Notes for the researcher

Two things about this capture. First, the red highlight in the figure is on the *palette
entry* "Create expanded sub-process", not on a process element, so the figure documents a
modelling step rather than a finished agent container; the ad-hoc sub-process is named in
the page text and in the post's prose, but it is not visible in this particular image.
Second, the alt text is only "Sub-process"; the ruling chose it over figure 1 (alt
"Sub-process-2"), which shows the same process with the container already drawn. Since the
captured figure does contain an AI-bound BPMN task ("AI Task Agent") and is part of the
process the page documents, the INCLUDE verdict stands; `needs_visual_check` stays true
because a reader may want to see the container itself, which sits in the post's other
figures. The downloaded file is 1400x614 although the source asset is 1200x526.
