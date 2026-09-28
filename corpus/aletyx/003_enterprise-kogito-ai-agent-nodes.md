---
n: 199
source: aletyx
source_name: Aletyx (Kogito AI add-ons, aletyx.ai)
title: "Enterprise Kogito - a BPMN process-instance monitor whose prose names AI Agent nodes that the drawn diagram does not contain"
url: https://aletyx.ai/enterprise-kogito/
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: >-
  The page asserts that AI Agent nodes sit inside the process ("AI Agent nodes handle ad-hoc
  intelligent tasks inside workflows.", "AI Agent nodes for intelligent tasks inside the
  process.", "Direct LLM invocation nodes call language models as workflow steps."), but the
  only BPMN figure it draws - the Aletyx process-instance monitor - shows no AI-labelled element.
  Is that page an artefact to record, or is the assertion a product claim that stays
  E2-no-ai-element?
needs_visual_check: false
bpmn_evidence: "a BPMN 2.0 process drawing rendered inside the Aletyx Dev Console 'Process Instances' view: a start event, a 'Test task' and an 'Approval' script/task node, an exclusive gateway, a 'Get salary' service task, a 'Generate base offer' node, a 'Generate Offer' sub-process (collapsed, with a + marker), a yellow-highlighted 'HR Interview' user task in the timeline, an 'Applicant Verify' node and 'Log Offer', ending in red end events; the neighbouring panels are a Timeline, a Details/Variables inspector and a node-trigger panel"
bpmn_evidence_quote: "AI Agent nodes handle ad-hoc intelligent tasks inside workflows."
ai_evidence: "the AI element is asserted in prose only. The page's own process drawing contains no AI-labelled node, no AI task type and no LLM marker - every label in the diagram is an ordinary BPMN task name (Test task, Approval, Get salary, Generate Offer, HR Interview, Log Offer). The AI Agent node the prose describes is therefore a product/roadmap claim about what the platform can do, not an element visible inside any diagram on this page"
ai_evidence_quote: "AI Agent nodes for intelligent tasks inside the process."
artefacts:
  screenshot: 003_enterprise-kogito-process-instance-monitor.png
  assets: [003_enterprise-kogito-process-instance-monitor.png]
  bpmn_xml: []
  archive: null
duplicate_of: null
access: public
capture_source: page-figure
capture_quality: legible
capture_width_px: 1001
capture_method: "the page figure aa3243de_Dark-20Mode-20Screen-20Recreation.D0tcFtk6_Z2lAt6q.webp (11038 B) downloaded from aletyx.ai and converted to PNG on 2026-09-25; the page's other figures are an AI-chip icon, an approval-workflows icon and the Kogito logo"
judgment: true
---

## What the artefact is

`https://aletyx.ai/enterprise-kogito/`, the vendor's "Enterprise Kogito" product page,
figure `aa3243de_Dark-20Mode-20Screen-20Recreation.D0tcFtk6_Z2lAt6q.webp` (11 038 B,
1001 x 429). It is a screenshot of the Aletyx Dev Console in its **Process Instances** view
(left nav: Process Instances / Jobs / Tasks), so it is a live BPMN render rather than a
marketing illustration.

## Observations (description only, no interpretation)

- Diagram, left to right: a start event (grey circle); "Test task"; an "Approval" node;
  an exclusive gateway (diamond); a "Get salary" service task and a "Generate base offer"
  node; a collapsed sub-process "Generate Offer" with a `+` expander and "Generate Offer"
  inner label; a second exclusive gateway; "Applicant Verify" and "Log Offer" nodes;
  "Complete Interview"; two red end events.
- "HR Interview" is drawn as a yellow-highlighted node - the token's current position -
  and appears in the Timeline panel with the subtitle "Human Task".
- Right-hand panels: Timeline (Start, New Hiring, Split, Generate base offer, Log Offer,
  HR Interview), Details (Name "Hiring", State "Active"), Variables (`$id=16`,
  `$offer="30K"`, `$job="SDE3"`, `$category="Senior Software Engineer"`,
  `$candidateData=[ ]`) and a node-trigger panel ("Select a node from the process nodes list
  and click Trigger to launch it.").
- The page's other figures on this URL: `af53cdec_ai-chip` (icon), `33562515_approval-workflows`
  (icon), `4cafe0c3_kogito-logo` (logo). None is a process drawing.

## Notes for the researcher

The mismatch this row exists for: the page's prose promises "AI Agent nodes ... inside the
process" and "Direct LLM invocation as a native workflow step", but the one process it draws
is AI-free - its tasks are Test task, Approval, Get salary, Generate Offer, HR Interview,
Applicant Verify, Log Offer. The same prose pattern recurs on `/intelligent-process-automation/`
(record 004) and on `/aletyx-vs-bamoe-vs-apache-kie/` and `/enterprise-kie-server/`; the only
place in this source where the AI node is actually *drawn* is the vendor's GitHub repository
(`examples/quarkus/src/main/resources/process.bpmn`, record 001), where it appears as a
`drools:taskName="AletyxAI"` task named "Aletyx Intelligence" inside an ad-hoc sub-process.

The page's other AI mentions were not excluded as marketing: marketing material is the
evidence base for this step. This row is `UNCERTAIN` only because the ruling question above
is not mine to answer.
