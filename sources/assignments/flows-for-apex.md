---
source: flows-for-apex
source_name: Flows for APEX (FlowQuest; flowsforapex.org docs, flowquest.net, GitHub)
source_type: open-source vendor docs + blog + repo
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: YES
  C2_native_bpmn20: YES
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES (operator ruling 2026-09-24, general C4 rule)
access: public
population_type: enumerable
population_estimate: 15
effort: small
needs_logged_in_browser: false
status: DONE (Pass 2 census 2026-09-24, audit clean; 362 rows, 4 INCLUDE, 8 UNCERTAIN)
---

## Criteria evidence

- **C1/C2 YES**: https://flowsforapex.org/latest/ai-service-task/ (2026-09-24): "The Flows
  for APEX AI Service Task allows you to call Generative AI Services as a workflow step."
  Configuration: "Add a Service Task into your BPMN diagram… convert the task to a Service
  Task". Documented use cases: "Generate Process Routing / Recommended Course of Action",
  "Generate Document".
- **C3 YES**: open source.
- **C4 UNCLEAR**: an Oracle-APEX-community BPMN engine maintained by FlowQuest. See the
  general C4 rule.

## Promotion mode

A BPMN service task bound to an AI service (a labelled/configured task). The "process
routing" use case puts AI in charge of gateway decisions, which is noteworthy for the
taxonomy's exposure axis.

## Entry points

- The anchor docs page (pinned `latest`; resolve it to the version number and record it)
- "Flows for APEX 26.1: adaptive workflow and AI-driven BPMN…" (flowquest.net/posts/release26,
  not opened)
- `github.com/flowsforapex/apex-flowsforapex`: look for example `.bpmn` models using the AI
  Service Task
- (A LinkedIn release post exists; out of scope per Gate 1 ruling B4, vendor sources only.)

## Enumeration instructions

1. Docs: the AI Service Task page and its siblings, plus any "adaptive workflow" pages
   introduced in 26.1.
2. Repo: every `.bpmn` file. Decisive evidence is a service task configured with the AI
   type.
3. The flowquest.net posts index.

## Gate 1 / orchestrator notes (2026-09-24)

Version pinning: census `latest/*` (record the resolved version). From the archived doc
versions, include only paths that do not exist under `latest/`, and record the reduction in
the ledger header.

## RESUME

(empty)
