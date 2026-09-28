---
n: 0
url: https://doc.scheer-pas.com/designer/latest/using-an-ai-agent-in-an-xuml-service
source: scheer-pas
accessed: 2026-09-24
verdict: UNCERTAIN
needs_human_ruling: true
question: >-
  This is the reference page for embedding an AI agent in a service: it states that each AI
  agent gets a default `execute` operation which the modeller drags into "execution and activity
  diagrams", and its figures show that operation inside a Designer execution model - a
  proprietary notation, not BPMN 2.0. Does the corpus take this page as an AI-enabled process
  artefact (an AI agent as a first-class element of a process model), or only as the notation
  reference for the binding documented in records 001 and 002?
bpmn_evidence: >-
  The page presupposes the BPMN process but publishes no BPMN model of its own: its figures are
  Designer execution/activity diagrams (the AI agent's `execute` operation dropped into the
  model) plus the Implementation tree listing `Agents > CaseAgent > CaseAgentInterface > execute
  (in: CaseRequest, out: AgentResponse)`. The word used for the model it targets is the service's
  process ("you can embedd it in your xUML process"), not a BPMN diagram.
ai_evidence: >-
  The AI element is an operation of the process model itself: "for each AI agent a default
  operation execute is created" and "Now, you can use the execute operation in execution and
  activity diagrams. Simply drag & drop the operation on the diagram pane". The page also fixes
  the agent's interface at model level: input and output "must be of a complex type", the
  template classes being `CaseRequest` in and `AgentResponse` out.
artefacts:
  - screenshot: 003_using-an-ai-agent-in-an-xuml-service_fig1.png
capture_quality: legible
capture_width_px: 1387
---

## What the page shows

`Using an AI Agent in an xUML Service` is the Designer guide's reference page for the binding that
records 001 and 002 exercise in the tutorial. Verbatim:

> Once you have created and tested your AI agent, you can embedd it in your xUML process. As
> explained in detail on Creating an AI Agent , for each AI agent a default operation execute is
> created

> Now, you can use the execute operation in execution and activity diagrams. Simply drag & drop
> the operation on the diagram pane

> Since the AI agent's execute operation is a REST call, you need to apply the REST extension to
> the operation. Go to the operations's attributes, select the REST Adapter extension and the
> corresponding AI agent alias

> Within activity diagrams, this extension is already applied automatically.

> Mandatory Usage of "getAuthorizationOptions" - When using the AI agent operation in a model,
> you need to authenticate with the PAS platform.

Captured fig 1 is the page's `drag_execute_to_execution_model.png`: the Designer with the BPMN
process tab on top (the Insurance_Case_Process of record 001, small) and the execution model
below, with the orange arrow that marks dragging the `execute` operation into the model.

The page's other figures (`execute_operation`, `execute_rest_extension`,
`get_authorization_options`, `request_options`) are: the Implementation tree showing the AI agent
package with its `CaseAgent` / `CaseAgentInterface` / `execute` (in: `CaseRequest`, out:
`AgentResponse`) operation; the same execution model with the REST extension applied; the
Implementation tree under `Base Types > PAS_Platform > Auth > AuthService` with
`setAuthorizationOptions` highlighted; and the execution model's `request_options` local variable
wired to the `getAuthorizationOptions` operation.

## Observations

- **AI agent as a process element.** Here the AI agent is not a form, a script or an external
  system call bolted on: the agent is created as a package in the service's Implementation, gets
  an `execute` operation with typed input/output, and that operation is then a first-class
  element the modeller drags into the process's model. That is as close to an "AI element inside
  the process" as this source gets.
- **But the diagram that shows it is not BPMN.** The notation of every figure on this page is the
  Designer's execution model / activity diagram (proprietary). No BPMN 2.0 diagram is published
  on this page.
- The page's own terminology is worth noting for the method: Scheer PAS separates the *BPMN
  process* (what the business sees) from the *execution model* (what runs). The AI element lives
  strictly on the execution-model side, which is why this source cannot yield a BPMN diagram with
  a *visible* AI element.

## Notes for the researcher

This is the third and last artefact page of the source; together with 001 (BPMN level) and 002
(the tutorial's binding step) it completes the delegated-binding story. If the ruling on record
001 is "delegated binding counts", then this page is the notation reference for it; if the ruling
is "the AI element must be drawn in the BPMN", then no page of this source qualifies and the
answer for scheer-pas is "no AI-enabled BPMN artefact", which is a result about the source's
tooling design, not a collection gap.
