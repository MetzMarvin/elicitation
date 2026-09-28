---
n: 002
record: 002
url: https://docs.flowx.ai/5.9/docs/building-blocks/process/passing-data-between-nodes
source: flowx-ai
surface: docs:flowx-ai:5.9
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: The artefact is an ASCII box-and-arrow diagram of a BPMN process with "AI agent" as one of its four node kinds (and the page binds that node to a Service Task with the agent integration). Is an ASCII sketch a collectable process artefact, or does the criterion require BPMN 2.0 notation?
page_publishes: ascii-process
capture_quality: legible
quotes: the page's own words. Markdown emphasis and code markers are rendered away and long quotations are elided with "..."; text in single quotes is quoted from another named source (the site's own glossary, or a label read in this page's figure).
screenshot: 002_passing-data-between-nodes.png
artefacts:
  - screenshot: 002_passing-data-between-nodes.png
bpmn_evidence: |
  The page publishes the process as an ASCII box-and-arrow sketch whose boxes are BPMN/process element
  names, under the heading "The mental model" - a shared store read from and written to by four node
  kinds:
         Process variables (shared store)
                ^                ^                ^              ^
                | output         | output         | output       | read
          | Subprocess|    | Workflow  |    | AI agent  |  | User task |
  and the sentence above it names the same set as nodes of a BPMN process: "Inside a BPMN process, every
  node, including subprocess, integration workflow, AI agent, business rule, and user task, reads from
  and writes to a shared store of process variables". The page also names the BPMN nodes that do the
  waiting: "place a Receive Message Task after the Send Message Task that triggers the workflow", and
  "Any node after the Receive Message Task, including gateway, business rule, and user task, can read the
  result key". No figure and no .bpmn model: the artefact is the ASCII sketch.
ai_evidence: |
  "AI agent" is one of the four node kinds in that sketch, and the page's own pattern table binds it to a
  BPMN node type: "Call an AI agent (extraction, decision, generation) | Service Task with the agent
  integration | Mapped back to process variables in the action's output mapping". A Note repeats it:
  "For AI agents: the integration is typically wired on a Service Task, and the agent's response is
  mapped back to process variables in the action's output mapping. No separate Receive Message Ta...".
  The same page files "AI ops" under the workflow-call row: "Call an integration workflow (REST, DB, AI
  ops) and capture the result".
note: |
  Read from the page's own published markdown twin (https://docs.flowx.ai/5.9/docs/building-blocks/process/passing-data-between-nodes.md), and - where a Mintlify component renders differently from the twin - from the page as displayed in the browser, on 2026-09-25; nothing on this page was paraphrased. The capture next to this record is a text render of the page's own diagram/prose, because the page publishes its process as ascii-process rather than as a diagram image. The page publishes no BPMN-notation diagram: it carries no figure at all. The evidence above is quoted verbatim from that page.
