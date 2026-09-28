---
n: 107
record: 003
url: https://www.ibm.com/docs/en/ibamoe/9.5.x?topic=ia-using-ai-agent-tasks-in-workflows-tech-preview
source: ibm-bamoe
surface: docs:ibamoe-9.5.x
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: >
  The page documents BAMOE's second AI node type (the AI Agent task, Langflow-backed) and its nine
  figures are the node's dialogs and property panels inside the BPMN editor - Langflow account,
  agent selection, the {{aiAgentInput}} input, data mapping, Test Agent - so the figures carry BPMN
  task furniture (Data mapping, onEntry/onExit) but none of them shows the process diagram the node
  sits in. Is a node's property panel, published in the editor's own documentation, a process
  artefact for this census (INCLUDE), or is the page E0-no-artefact because no diagram is published
  on it?
bpmn_evidence: |
  The page's figures are all crops of the BAMOE Canvas BPMN editor with the AI Agent task selected:
  langflow-connect.png, authenticate-langflow.png, langflow-connect-vscode.png (provider sign-in),
  langflow-task-props.png (the node's property panel - the capture), selecting-agent.png,
  aiAgentInput.png, edit-input-field.png (the input variable), langflow-data-mapping.png,
  test-the-agent.png. They show BPMN task properties (Langflow Account, Agent, Input, Data mapping,
  onEntry / onExit) but no figure shows the process the node belongs to, so no pool, lane, sequence
  flow or gateway is visible anywhere on the page.
ai_evidence: |
  "The AI Agent task in the BPMN Editor, powered by Langflow, allows you ..." - the page's own
  opening sentence. The node is bound to a Langflow account and an agent, its input is the process
  variable `{{aiAgentInput}}`, and it can be tested from the panel (Test Agent) and logged
  (Agent Execution Log). Providers named on the page include Langflow, watsonx, OpenAI and Ollama;
  the node's work-item-handler dependencies (com.ibm.bamoe:bamoe-ai-agent-task-work-item-handler-*)
  are documented alongside the Gen AI task's.
artefacts:
  - screenshot: 003_ibm-bamoe-docs-ai-agent-task-props.png
  - file: ledgers/_bamoe.raw/workflow__langflow-task-props.png
  - file: ledgers/_bamoe/sheet_aiagent.png
capture_quality: marginal
capture_width_px: 952
---

## What the file shows

The BAMOE 9.5.x documentation topic "Using AI Agent tasks in Workflows (Tech Preview)" (child of
*Integrating with AI*), documenting the Langflow-backed AI Agent task - the second AI node type, next
to the Gen AI task of record 001. Nine figures, all of them the node's own dialogs or property panels
in the BAMOE Canvas BPMN editor.

The capture, `langflow-task-props.png` (952x388), is the node's property panel with the Langflow
Account field empty: "Langflow Account *", "Agent *", plus the panel's BPMN sections.

## Observations

- This is the node with the robot glyph (the AI Agent Task entry in the palette) rather than the
  sparkle of the Gen AI task; both are visible side by side in the community capture of record 006.
- The AI binding is *external*: the node delegates to an agent defined in Langflow, addressed by an
  account and an agent name, with the process variable `{{aiAgentInput}}` as its input. That is a
  different pattern from the Gen AI task in record 001, which binds to a model with a prompt.
- Because the figures are panels, the page gives no evidence about how the node is laid out inside a
  process - a gap that records 005, 006, 007 and 008 fill from published captures.

## Notes for the researcher

- I did not resolve this to INCLUDE or E0: an INCLUDE would rest on the panel being the node's
  artefact (the page *is* the documentation of a BPMN node type), an E0 on the absence of any
  diagram. The capture is attached so the call can be made by eye.
- Capture quality is marked `marginal` rather than `legible` only because `langflow-task-props.png`
  is a narrow 952x388 crop of a panel with an empty account field; the text is readable, the
  process context is not present in it.
- The same node appears with a filled panel in record 008 (page 29 of the 9.3.1 webinar deck) and
  as a placed node in record 006 (the animation on the community post), which is where the
  process-level evidence lives.
