---
n: 105
record: 001
url: https://www.ibm.com/docs/en/ibamoe/9.5.x?topic=ai-using-gen-tasks-in-workflows
source: ibm-bamoe
surface: docs:ibamoe-9.5.x
accessed: 2026-09-25
verdict: INCLUDE
needs_human_ruling: false
question:
bpmn_evidence: |
  The decisive figure, genai-task-create.png (1077x692), is a crop of the BAMOE Canvas BPMN editor:
  the editor's shape palette on the left with its AI group expanded and "Gen AI Task" listed under
  it, and a Gen AI Task node - the rounded task shape carrying the AI sparkle - placed on the dotted
  process canvas. The page's own words for this figure are "Integrate AI into Workflows by dragging a
  Gen AI task directly into your BPMN process models". The remaining nine figures are the node's
  property panels in the same editor (AI provider, authentication, model selection, prompt, data
  mapping, and a worked example on the hiring process), i.e. the BPMN task's own configuration UI,
  not separate diagrams.
ai_evidence: |
  The AI element is the node itself, and the page names its bindings: AI Provider (watsonx, OpenAI
  or Ollama), Model (the worked example uses ibm/granite-3-2-8b-instruct), Temperature (0.2), Token
  Limit (240), a Prompt field, Data mapping, Preview, and a Test action. The example task
  ("Create Offer" in the hiring process) shows the generated offer letter in the Preview table.
  The page also documents the work-item-handler coordinate
  com.ibm.bamoe:bamoe-gen-ai-task-work-item-handler-quarkus for deployment.
artefacts:
  - screenshot: 001_ibm-bamoe-docs-genai-task-canvas.png
  - file: ledgers/_bamoe.raw/workflow__genai-task-create.png
  - file: ledgers/_bamoe/sheet_ai_extra.png
capture_quality: legible
capture_width_px: 1077
---

## What the file shows

IBM's BAMOE 9.5.x documentation topic "Using Gen AI tasks in Workflows", a child of the
*Integrating with AI* branch. Ten figures, all in the BAMOE Canvas BPMN editor:

- `genai-connect.png`, `genai-authenticate-watsonx.png`, `genai-connect-vscode.png` - provider
  connection and authentication dialogs.
- `genai-task-create.png` - **the artefact**: the canvas with the AI group in the palette and a
  Gen AI Task node placed on the process.
- `genai-task-props.png`, `genai-model-select.png`, `genai-prompt.png`, `genai-data-mapping.png` -
  the node's property panel: AI provider, model, prompt, data mapping.
- `genai-example-task-config.png`, `genai-example-prompt-result.png` - a worked example on the
  hiring process (the "Create Offer" task and the offer letter it produced).

## Observations

- The Gen AI Task is a **first-class BPMN node type of the editor**, not a binding buried in another
  task's properties. Its signal in the diagram is the shape itself: a task rectangle with the AI
  sparkle in its top-left corner. This is the contrast the assignment asked to record against
  UiPath, where the AI is invisible in the diagram.
- The node carries the ordinary BPMN task furniture alongside its AI settings: `Data mapping
  (in / out)`, `onEntry / onExit`, `Metadata`.
- The documentation names the providers it can be bound to (watsonx, OpenAI, Ollama) and a concrete
  model (`ibm/granite-3-2-8b-instruct`) with sampling settings - the AI element is explicit and
  parameterised in the page, not implied.

## Notes for the researcher

- `genai-task-create.png` is the single figure that puts the AI node and the canvas in the same
  frame; every other figure is a panel, so the *process-level* view of the AI element rests on this
  one crop. It is legible (1077x692) and is the record's capture. If you want a fuller process
  picture, the community rows 004 and 007 (records 004 and 007) show the same node inside complete
  processes.
- The docs page documents the Gen AI Task for both the Canvas and the VS Code extension
  (`genai-connect-vscode.png`); this record does not distinguish the two editors beyond that figure.
