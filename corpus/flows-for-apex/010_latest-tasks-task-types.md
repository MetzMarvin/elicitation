---
n: 17
source: flows-for-apex
source_name: Flows for APEX (FlowQuest; flowsforapex.org docs, flowquest.net, GitHub)
source_type: vendor docs
title: BPMN Tasks
url: https://flowsforapex.org/latest/tasks/
accessed: 2026-09-24
verdict: UNCERTAIN
needs_human_ruling: true
question: "The page states that service tasks can be used for 'Calling Generative AI Services via APEX AI', but its only artefact is a 890px-wide task-type strip image (taskTypes22.2.png, from v22.2) that predates the AI task type. I cannot read every label on it at native resolution: does the vendor's canonical task-type diagram show the AI Service Task, and should this page be collected as an AI-in-process artefact?"
needs_visual_check: true
bpmn_evidence: one figure image, /assets/images/taskTypes22.2.png, alt "task types", title "Task types" (890x103 - the filename dates it to v22.2, before the AI task type existed)
bpmn_evidence_quote: "alt=\"task types\" title=\"Task types\""
ai_evidence: page prose names AI as a service-task binding, but no AI element is visible in the page's only diagram
ai_evidence_quote: "Calling Generative AI Services via APEX AI."
artefacts:
  screenshot: 010_latest-tasks-task-types.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: poor
capture_width_px: 890
capture_method: curl -L on /assets/images/taskTypes22.2.png, src read from the page DOM
---

## What the page shows

The vendor's reference page for BPMN task types. It lists the task types a Flows for APEX
developer can use and, for service tasks, states: "Currently BPMN service tasks can be used to
call the following services: Calling Generative AI Services via APEX AI. 🆕 ... Sending Mail
defined declaratively in your process model ... Running a PL/SQL script to call any other
s..." It also states that a business rule task can be used "to call AI / ML services inside
your Oracle database". Its only diagram is the task-type strip `taskTypes22.2.png`.

## Observations (description only, no interpretation)

- **AI activity - function:** the page states that a service task can call "Generative AI
  Services via APEX AI" (marked 🆕) and points to "More Info" for it; the diagram itself is a
  strip of task types and carries no visible AI marker at the resolution available.
- **AI activity - element type:** described in prose as a service task binding ("Calling
  Generative AI Services via APEX AI"); the corresponding task type is documented on its own
  page (record 001).
- **Authority - downstream:** not visible on the page.
- **Authority - data:** not visible on the page.
- **Authority - control:** not visible on the page.
- **Input provenance:** not visible on the page.
- **Guards present:** none observed.
- **Prompt / model detail visible:** none. The page's other AI mention - "presentation
  requirements are specified in a simple JSON definition, optionally with AI assistance" - refers
  to generating APEX user-task forms, not to an element inside a process, and was not treated as
  the artefact evidence.

## Notes for the researcher

`capture_quality: poor` is a hard limit of the source, not of the capture: the native asset is
890x103 px, so no larger capture exists. This is the docs surface for the `serviceTask` scaffold
whose model file is record 005 (Tutorial 4a), and it is the page a reader lands on when looking
for what a service task can be bound to. Verdict UNCERTAIN because the AI/non-AI question here
turns on labels I could not resolve in the image, and the shared rules forbid an E2 where the AI
mention is ambiguous or a visual check failed.
