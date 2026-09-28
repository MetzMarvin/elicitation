---
n: 14
source: quantumbpm
source_name: QuantumBPM (quantumbpm.com - BPMN/DMN engine vendor: blog, docs, product pages)
source_type: vendor blog post with downloadable BPMN 2.0 process and DMN 1.5 decision files
title: "Orchestrating AI Agents with BPMN: Durable, Auditable Agentic Workflows"
url: https://quantumbpm.com/blog/orchestrating-ai-agents-with-bpmn
accessed: 2026-09-24
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "the post publishes its process as a downloadable BPMN 2.0 file (bpmn:definitions with the OMG BPMN 20100524 MODEL namespace, a full bpmn:process plus bpmndi diagram), captured byte-exact in the corpus"
bpmn_evidence_quote: "<bpmn:adHocSubProcess id=\"AdHoc_resolve\" name=\"Resolve\"> ... <bpmn:completionCondition xsi:type=\"bpmn:tFormalExpression\">resolved = true</bpmn:completionCondition>"
ai_evidence: "the AI is a task inside the process: an agent-bound service task type (agent-plan) sits in an ad-hoc sub-process that the engine repeats until the completion condition holds, and a DMN decision table converts the agent's own confidence score into the routing condition of the exclusive gateway, so the process decides whether the agent may answer autonomously or a human must review"
ai_evidence_quote: "<bpmn:serviceTask id=\"Task_agent_plan\" name=\"Agent: plan &amp; act\"> <quantum:taskDefinition type=\"agent-plan\" retries=\"3\" />"
artefacts:
  screenshot: 001_agent-support-process.png
  assets: [001_orchestrating-ai-agents-with-bpmn.page.html]
  bpmn_xml: [001_support-agent.bpmn, 001_support-agent-routing.dmn]
  archive: 001_orchestrating-ai-agents-with-bpmn.page.html
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1540
capture_method: curl of /assets/files/support-agent.bpmn and /assets/files/support-agent-routing.dmn at their native URLs, plus the modeler screenshot the post embeds for this process
---
## What the page shows

The post (Richard Bízik, 13 June 2026) argues that an agentic workflow becomes governable
when it is given a process to live inside, and it publishes the worked example as two
downloadable files, both fetched verbatim and kept in the corpus:

* `support-agent.bpmn` - `bpmn:definitions` (OMG BPMN 20100524 MODEL namespace, exporter
  "QuantumBPMN Modeler") with one executable process `support-agent` name="Support Agent":
  * `bpmn:startEvent` "Ticket arrives" -> `bpmn:serviceTask` "Classify ticket"
    (`quantum:taskDefinition type="classify-ticket" retries="3"`, output mapping
    `{category, urgency, confidence: agentConfidence}` -> `classification`)
  * -> `bpmn:businessRuleTask` "Route Support Ticket"
    (`quantum:calledDecision decisionId="route-support-ticket" resultVariable="routing"
    bindingType="latest"`)
  * -> `bpmn:exclusiveGateway` "Auto-resolvable?" default="Flow_human"; the `Flow_auto`
    sequence flow carries `routing = "AUTO"`
  * auto branch: `bpmn:adHocSubProcess` "Resolve" with
    `<quantum:adHoc activeElementsCollection="[&quot;Task_agent_plan&quot;]" />` and
    `bpmn:completionCondition` `resolved = true`, containing `bpmn:serviceTask`
    "Agent: plan & act" (`quantum:taskDefinition type="agent-plan" retries="3"`) which flows
    into "Validate &amp; record resolution" (`finalize-resolution`), alongside three other
    service tasks "Look up order", "Search knowledge base", "Draft reply"
  * human branch: `bpmn:userTask` "Review &amp; approve"
    (`quantum:assignmentDefinition candidateGroups="support"`) with an interrupting
    `bpmn:boundaryEvent` "SLA breached" carrying `bpmn:timeDuration` `PT8H` -> `bpmn:endEvent`
    "Escalated"
  * both branches converge on `bpmn:serviceTask` "Send reply" -> `bpmn:endEvent` "Done"
  * 13 shapes and 10 edges in the `bpmndi` diagram, all with `quantum:connectionHandles`.
* `support-agent-routing.dmn` - DMN 1.5 `definitions` (namespace
  `https://www.omg.org/spec/DMN/20230324/MODEL/`) holding one `decision` id
  `route-support-ticket` name "Route Support Ticket" with a `decisionTable hitPolicy="FIRST"`
  over three inputs (category, urgency, agentConfidence) and one output (routing). Its rule
  order is: `"high"` urgency -> `"HUMAN"`; `"billing"` -> `"HUMAN"`; `agentConfidence < 0.7`
  -> `"HUMAN"`; `"password_reset", "order_status", "shipping"` with confidence `>= 0.7` ->
  `"AUTO"`; fallback -> `"HUMAN"`. The file's own leading comment says it "Turns the
  classifier agent's fuzzy output (category, urgency, confidence) into a deterministic
  routing decision the BPMN exclusive gateway branches on".

The post's own figure for this process is the modeler screenshot captured as
`001_agent-support-process.png` (1540x721), alt "The support-automation process modelled in
the QuantumBPM modeler". The page's other three figures are modeler UI captures of the DMN
FEEL editor, the replay slider and the instance history, not further process diagrams.

## Observations (description only, no interpretation)

- **AI activity - element type:** an ordinary `bpmn:serviceTask` whose engine binding is
  `quantum:taskDefinition type="agent-plan"`; the post's own sentence from the anchor text
  the census quotes: "A single agent step is a service task. A reasoning loop is an ad-hoc
  sub-process."
- **AI activity - function:** the task is the agent's plan-and-act step; the sibling tasks it
  can call are lookups ("Look up order", "Search knowledge base", "Draft reply"), and
  "Validate &amp; record resolution" turns the draft into a recorded resolution.
- **Loop/iteration:** the `adHocSubProcess` re-runs the tasks listed in
  `activeElementsCollection` until `resolved = true`; `activeElementsCollection` names only
  `Task_agent_plan`, so the agent step is the one the engine repeats.
- **Authority - control:** the `routing` variable that gates the gateway comes from the DMN
  decision, not from code, and `bindingType="latest"` binds the newest stored decision
  version; the gateway's default flow is the human path, so an unmatched result falls back to
  review.
- **Authority - human in the loop:** the non-auto branch is a `bpmn:userTask` with candidate
  group `support`, and an interrupting timer boundary of `PT8H` ("SLA breached") leads to a
  separate "Escalated" end event.
- **Guards present:** `retries="3"` on every service task including the agent task; the DMN
  confidence threshold `>= 0.7`; the SLA timer; and the human review branch.
- **Data flow:** explicit `quantum:ioMapping` on each task - the classifier writes
  `classification`, the agent task reads `subject`, `body` and `classification`, the DMN
  inputs are fed from `classification.category`, `classification.urgency` and
  `classification.confidence`, and the ad-hoc sub-process outputs
  `{reply: draft, recorded: recorded}` as `resolution`.
- **Prompt / model detail visible:** the process file names no model or provider; the page's
  TypeScript listing shows a `Worker` with `handle(...)` handlers, and the agent's internals
  are inside the external worker, not in the model.
- **Auditability claim (page prose):** "Every prompt, response, and routing decision is
  recorded in the instance history for audit" - the page's claim, not something the file
  shows.

## Notes for the researcher

- Strongest evidence in this source: a complete, downloadable BPMN 2.0 file plus the
  matching DMN decision file, both byte-exact in the corpus, so the AI element can be read
  without inspecting any image. The screenshot is included for convenience only
  (`capture_quality: legible` by the 1400 px bar, 1540 px wide).
- Two files, one artefact: the process and its guardrail decision are recorded together
  because the decision exists only to route this process (its `calledDecision` is bound from
  `Task_route`), and the DMN file's comment says so.
- The page also links the same two files a second time (the download block appears twice), so
  no duplicate row was opened for them; the ledger row for the page covers both links.
- `needs_visual_check` is false here only because the `.bpmn` file is decisive; the reviewer
  who wants the drawn picture should look at `001_agent-support-process.png`.
