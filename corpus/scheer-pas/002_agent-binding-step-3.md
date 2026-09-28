---
n: 0
url: https://doc.scheer-pas.com/academy/latest/step-3-integrating-the-agent-to-the-process
source: scheer-pas
accessed: 2026-09-24
verdict: UNCERTAIN
needs_human_ruling: true
question: >-
  This page is where an AI agent becomes part of a process: the agent's `execute` operation is
  dragged into the execution model of the BPMN service task "Analyze customer request" and wired
  to the REST adapter and the agent alias. The diagrams published to show it are xUML
  execution-model diagrams (proprietary notation) and Designer screenshots, not BPMN 2.0
  diagrams. Does this page contribute an artefact to the corpus in its own right (a
  process model with an AI element), or is it the *binding evidence* for record 001 and
  therefore not an independent corpus item?
bpmn_evidence: >-
  The page opens the existing BPMN process and its BPMN tab is visible in two of its figures
  (fig 3 and fig 5), showing the same Insurance_Case_Process model as record 001 - start event
  "Start insurance case auto-processing", user task "Enter insurance request", service task
  "Analyze customer request" (highlighted), user task "Show case information", terminate end
  event - drawn in the Designer's BPMN editor.
ai_evidence: >-
  The page states the binding verbatim: "You created the CaseAgent to execute process step
  Analyze customer request ." and "You want to execute the AI agent during this process step, so
  drag & drop the agent's execute operation to the execution model". The AI element inside the
  process is the `execute` operation of the AI agent, dropped into the task's execution model,
  applied the REST adapter extension and selected the AI agent alias.
artefacts:
  - screenshot: 002_agent-binding-step-3_fig1.png
  - screenshot: 002_agent-binding-step-3_fig2.png
capture_quality: legible
capture_width_px: 1388
---

## What the page shows

`Step 3: Integrating the Agent to the Process` is the step of the AI tutorial in which the
previously built and tested AI agent is attached to the process from record 001. The page's
sequence:

> Open the Insurance_Case_Process . You created the CaseAgent to execute process step
> Analyze customer request . Therefore, you will now add the agent in this step of the process.

> Click Analyze customer request to open its execution model:

> You want to execute the AI agent during this process step, so drag & drop the agent's execute
> operation to the execution model:

then the REST extension ("Since the AI agent's execute operation is a REST call, you need to
apply the REST extension to the operation"), the agent alias selection, the persisted variables
that carry the agent's payload

> add the two necessary variables for the input ( request: CaseRequest ) and the output
> ( caseData: AgentResponse ) of the AI agent

and the platform authentication:

> When using an AI agent operation in a model, you need to authenticate with the PAS platform.
> To do so, you need to set the necessary request options to the execute REST call ... by using
> the PAS platform standard operation getAuthorizationOptions

Fig 1 (captured) is the page's own `open_execution_model.png`: the Designer with the BPMN tab on
top (the Insurance_Case_Process, "Analyze customer request" boxed in orange) and, below it, the
task's **execution model** - the proprietary xUML notation with the `Persisted` / `Local` data
bands, a black start dot and the empty flow. Fig 2 (captured) is the page's
`drop_execute_operation.png`: the same execution model with the agent's `execute` operation now
dropped into it, with the orange callout marking where it landed.

The page's remaining figures (`add_extension_to_operation`, `select_rest_extension`,
`select_agent_alias`, `rest_pins`, `add_persisted_variables`, `input_and_output_connected`,
`drop_authorization_options`, `add_local_variable_request_options`,
`finished_execution_diagram`) are further Designer screenshots of that same execution model,
its attributes panels and the Implementation tree; two of them (`finished_execution_diagram`,
`add_local_variable_request_options`) also show the BPMN tab of the process alongside.

## Observations

- The notation of the artefact this page *documents* is xUML / Designer execution model
  (proprietary: rounded boxes inside `Persisted` / `Local` bands, black start dot, dashed
  connectors, `⊞ ⊡` diagram toolbar) - **not** BPMN 2.0. The BPMN model itself appears here only
  as the editor's second tab, i.e. as the same diagram already recorded as 001.
- What this page adds to the corpus is the **binding**: the mechanism by which the BPMN service
  task "Analyze customer request" becomes an AI step - a default `execute` operation per AI agent
  (see record 003), dropped into the task's execution model, extended with the REST adapter and
  pointed at an AI agent alias, authenticated via `getAuthorizationOptions`.
- Hence the front-matter question: independent corpus item, or binding evidence for 001.

## Notes for the researcher

The assignment for this source anticipated exactly this shape ("That is `UNCERTAIN` with the
binding quoted, never `E2`"): the AI element is present and documented, but it is not a BPMN
element. Both captured figures are byte copies of the page's own attachments
(`open_execution_model.png`, `drop_execute_operation.png`), so the pair (BPMN level + execution
model level) can be read side by side.
