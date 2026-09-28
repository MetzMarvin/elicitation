---
n: 0
url: https://github.com/bonitasoft/bonita-connector-ai/blob/main/bonita-connector-ai-azure/src/test/resources/AzureOpenAIDemo-1.0.proc
source: bonitasoft
accessed: 2026-09-25
verdict: INCLUDE
needs_human_ruling: false
question: >-
  ANSWERED (elicitation-5a, 2026-09-25): the census protocol puts this artefact class
  deliberately in scope - "diagrams where the AI element is only visible as a task
  *property* or implementation binding, not as a distinct BPMN element type" - so the
  verdict is INCLUDE and the question is closed. It is kept here as the record of what was
  asked before the ruling. It read: like record 010, this is a Bonita `.proc` process in
  which a BPMN service task "Ask Azure" carries the Azure OpenAI connector
  (`definitionId="azure-ask"`), and unlike 010 it also contains a user task "Review
  Results" after the AI step, i.e. the human-in-the-loop shape the connector documentation
  describes in prose.
bpmn_evidence: >-
  The file is BPMN 2.0 XML in Bonita's `.proc` serialisation, so the BPMN evidence is decisive:
  `<process:MainProcess xmi:id="_AzDemoMp01" name="AzureOpenAIDemo" bonitaModelVersion="9">`,
  the pool `process:Pool name="Azure OpenAI Demo"`, the lane `process:Lane name="Employee lane"`
  with `process:Actor name="Employee"`, the start event "Start", the service task "Ask Azure",
  the user task `process:UserTask name="Review Results"`, and the end event "End".
ai_evidence: >-
  The AI element is inside the process: the connector `process:Connector xmi:id="_AzDemoConn01"
  name="Azure Ask" definitionId="azure-ask" event="ON_ENTER"` is attached to the service task
  "Ask Azure", and the task is followed by a user task in which a human reviews the model's
  output before the process ends.
artefacts:
  - screenshot: 011_azure-openai-demo-proc.png
  - file: ledgers/bonitasoft.raw/AzureOpenAIDemo-1.0.proc
capture_quality: legible
capture_width_px: 1884
---

## What the file shows

`AzureOpenAIDemo-1.0.proc` sits under
`bonita-connector-ai-azure/src/test/resources/` in the repository
`github.com/bonitasoft/bonita-connector-ai`, the Azure sibling of record 010's Anthropic module.
Read as XML it is

- `process:MainProcess name="AzureOpenAIDemo" bonitaModelVersion="9"`,
- a pool "Azure OpenAI Demo" with one lane "Employee lane" acting as the actor "Employee",
- a start event "Start",
- a service task "Ask Azure" carrying the connector "Azure Ask"
  (`definitionId="azure-ask"`, `event="ON_ENTER"`),
- a user task "Review Results", i.e. a human step *after* the model call,
- and the end event "End".

## Observations

- This is the two-step shape the connector pages describe in prose (AI service task, then human
  review) realised as actual BPMN elements: a `process:ServiceTask` bound to an AI connector and
  a downstream `process:UserTask`.
- **The human review after the AI step is what the protocol asks not to abstract away.** The
  protocol lists as deliberately in scope "diagrams with an AI element *and* a guard, human review
  or filter in front of it (the mitigating element is exactly what must not be abstracted away
  later)", and "Review Results" is exactly that element: the process does not hand the connector's
  output straight to the next automated step, it routes it to a person first.
- It is shipped as a *test resource* of the vendor's public connector repository. That is not a
  ground for doubt - shared rules §4 bans "internal template / boilerplate listing" as a reason to
  hold an artefact back - and the repository is inside this source's enumerated population.
- The capture is a render of the file's own header through the lane, start event, service task
  and user task.

## Notes for the researcher

Record 010 is the Anthropic twin of this file, from the same repository; both were ruled INCLUDE by
the orchestrator on 2026-09-25 (delegated binding is deliberately in scope). Together 010/011 are the
code-side counterpart of the connector documentation pages 001-009, and they are the only two
artefacts in this source where the AI element is *inside* the process as a binding on a task the
diagram shows.
