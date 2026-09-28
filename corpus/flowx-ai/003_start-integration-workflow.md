---
n: 003
record: 003
url: https://docs.flowx.ai/5.9/docs/building-blocks/actions/start-integration-workflow
source: flowx-ai
surface: docs:flowx-ai:5.9
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: This page publishes no artefact at all - no figure, no diagram - and its AI-in-BPMN evidence is prose and a table ("available on Send Message Task, Task, and User Task nodes within BPMN processes"; "Execute AI operations (extraction, generation)"). Is a documented binding of an AI action to named BPMN node types collectable without a diagram?
page_publishes: prose-binding
capture_quality: legible
quotes: the page's own words. Markdown emphasis and code markers are rendered away and long quotations are elided with "..."; text in single quotes is quoted from another named source (the site's own glossary, or a label read in this page's figure).
screenshot: 003_start-integration-workflow.png
artefacts:
  - screenshot: 003_start-integration-workflow.png
bpmn_evidence: |
  No figure and no diagram on the page: the binding is published as prose and as a table. The Info box
  names the BPMN node types the action sits on: "The Start Integration Workflow action is available on
  Send Message Task, Task, and User Task nodes within BPMN processes." The Steps describe the node-level
  mechanics: "The input data mapped in the action configuration is sent as start variables to the
  workflow", "The BPMN process continues to the next node after the workflow completes", and the Warning
  "The process waits for the workflow to complete before continuing. To receive output data, you must add
  a Receive Message Task node after the Send Message Task that triggers the workflow."
  What is missing is a published process artefact: nothing on this page shows a process diagram.
ai_evidence: |
  The action is the documented route by which AI work reaches a BPMN node. The "When to use" table lists
  "Execute AI operations (extraction, generation) | Start Integration Workflow", and the workflow is
  described as "executing its configured nodes (REST calls, data transformations, AI operations,
  etc.)". Its sibling page in this source states the agent case outright ("Call an AI agent ... | Service
  Task with the agent integration"), and this page is the action that page links to.
note: |
  Read from the page's own published markdown twin (https://docs.flowx.ai/5.9/docs/building-blocks/actions/start-integration-workflow.md), and - where a Mintlify component renders differently from the twin - from the page as displayed in the browser, on 2026-09-25; nothing on this page was paraphrased. The capture next to this record is a text render of the page's own diagram/prose, because the page publishes its process as prose-binding rather than as a diagram image. The page publishes no BPMN-notation diagram: it carries no figure at all. The evidence above is quoted verbatim from that page.
