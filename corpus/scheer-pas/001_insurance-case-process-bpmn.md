---
n: 0
url: https://doc.scheer-pas.com/academy/latest/preparations-ai-tutorial-1
source: scheer-pas
accessed: 2026-09-24
verdict: INCLUDE
needs_human_ruling: false
ruling: >-
  The delegated-binding question this record first raised (UNCERTAIN, 2026-09-24) is settled by the
  census protocol, which puts this artefact class deliberately in scope: "diagrams where the AI
  element is only visible as a task *property* or implementation binding, not as a distinct BPMN
  element type" (prompts/02_source-census.md, "Deliberately in scope"). The binding is not inferred:
  the vendor publishes it on a sibling page of the same tutorial (record 002, "Step 3: Integrating
  the Agent to the Process"), where the agent's `execute` operation is dragged into the execution
  model of the BPMN service task "Analyze customer request", and again on record 003. Superseding
  ledger row for n=68, see ledgers/_scheer_correct_001.py.
bpmn_evidence: >-
  The page publishes the process as a BPMN 2.0 model drawn in the Scheer PAS Designer: a start
  event, two user tasks and one service task, an exclusive gateway-free linear flow and a
  terminate end event, labelled "Start insurance case auto-processing" / "Enter insurance
  request" / "Analyze customer request" / "Show case information" / "End Event". The page's own
  element list names the artefact: a process "Insurance_Case_Process" in the folder Process.
ai_evidence: >-
  The AI element inside the process is the service task "Analyze customer request": the page's
  own process-step table binds that task to the AI agent, and the tutorial adds an "AI agent
  that processes unstructured data and displays it in a form" to exactly this deployed process.
  The AI binding itself is not drawn in the BPMN notation - it lives in the xUML execution model
  behind the task (see record 002 and 003).
artefacts:
  - screenshot: 001_insurance-case-process-bpmn_fig1.png
  - screenshot: 001_insurance-case-process-bpmn_fig2.png
capture_quality: legible
capture_width_px: 1365
---

## What the page shows

`Preparations AI Tutorial 1` is the first page of Scheer PAS's AI tutorial. It hands the reader a
**service template** (`AIAgent_Tutorial_StartService`) and tells them to open its process:

> In folder Process : a process Insurance_Case_Process

The page then tabulates the process's three steps. The middle row is the AI-bound one:

> Analyze customer request | The AI agent, that you are going to create during this tutorial,
> will process the insurance request into insurance case information.

and the model itself is published as a figure (fig 1), drawn in the Designer's process editor
(BPMN 2.0: a green start event "Start insurance case auto-processing", a person-iconed user task
"Enter insurance request", a gear-iconed service task "Analyze customer request", a user task
"Show case information", a red terminate end event labelled "End Event", and the editor chrome
`Assets` tree, `Properties` / `Validation` panels).

Fig 2 is the same model captured inside the running Designer with the tutorial's two annotations
laid over it:

> During our AI tutorial, you will extend the deployed process by adding an AI agent that
> processes unstructured data and displays it in a form.

> Please note: PAS AI tutorials can only be run on a Kubernetes system. To execute a PAS AI
> tutorial, you need an API key from OpenAI or Mistral.

and a callout on the AI-bound step:

> You will add the "CaseAgent" to this process step. The agent processes the insurance request
> into insurance case information.

## Observations

- The diagram is **genuine BPMN 2.0**: event circles (start = thin ring, end = thick red ring
  with the inner dot = terminate end event), rounded tasks with type icons (person = user task,
  gear = service task), labelled sequence flows, no proprietary step tiles.
  Not the Campaign-Designer-style notation seen elsewhere.
- **The AI element is delegated, not drawn.** In the notation the AI step is an ordinary service
  task. What makes it AI is the execution model behind it: sibling pages of the same tutorial
  ("Step 3: Integrating the Agent to the Process", record 002) and the Designer guide page
  "Using an AI Agent in an xUML Service" (record 003) document the agent's default operation
  `execute` being dragged into the task's execution model and wired to the REST adapter and the
  AI agent alias.
- So the artefact exists, and its AI element exists, but the two are published on **different
  pages in two different notations**: the process part as BPMN here, the AI binding as an xUML
  activity/execution diagram there.

## Notes for the researcher

Per the source's assignment, a diagram whose AI element is bound through the xUML execution model
is recorded with the binding quoted, never as `E2-no-ai-element` - the AI element is *not absent*,
it is *not visible at BPMN level*. That ruling question resolved to `INCLUDE`: the census protocol
lists this artefact class under "Deliberately in scope" (see the front matter `ruling`), and the
binding is published by the vendor rather than inferred from this page. Both figures are captured
here so the collection can be checked against the evidence rather than against this description.
Record 002 keeps its own open question (is the binding step an artefact in its own right or the
binding evidence for this record?), which is a genuine researcher call.
