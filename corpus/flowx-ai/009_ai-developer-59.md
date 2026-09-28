---
n: 009
record: 009
url: https://docs.flowx.ai/5.9/ai-platform/pre-built-agents/ai-developer
source: flowx-ai
surface: docs:flowx-ai:5.9
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: Does the corpus require BPMN 2.0 notation, or does a process this source publishes as a Mermaid graph whose endpoints are BPMN event circles (([Start]) and ([END])) and whose middle is a drawn subgraph of AI task boxes (Classify Document, Summarize, Identify process, Extract Prompt, Generate Business rule) count as a BPMN process with an AI element inside it?
page_publishes: mermaid-process
capture_quality: legible
quotes: the page's own words. Markdown emphasis and code markers are rendered away and long quotations are elided with "..."; text in single quotes is quoted from a label read in the page's own rendered diagram.
screenshot: 009_ai-developer-59.png
artefacts:
  - screenshot: 009_ai-developer-59.png
bpmn_evidence: |
  The page's "How it works" section publishes the AI Developer's architecture as a Mermaid `graph TD`
  diagram (the page's own fenced source, read verbatim):
    "graph TD; Start([Start]):::primary subgraph Document_intelligence [Document intelligence]
    Classify_Document[Classify Document]:::secondary Summarize[Summarize]:::secondary
    Identify_process[Identify process]:::secondary Extract_Prompt[Extract Prompt]:::secondary end
    Generate_Business_rule[Generate Business rule]:::secondary END([END]):::primary Start -->
    Document_intelligence; Document_intelligence --> Generate_Business_rule; Generate_Business_rule --> END"
  Rendered in the browser on 2026-09-25 the diagram is a live Mermaid `<svg class="flowchart">`, whose
  `<g class="cluster">` carries the label `Document intelligence` and whose `<g class="node ...">`
  elements are `Start`, `Classify Document`, `Summarize`, `Identify process`, `Extract Prompt`,
  `Generate Business rule` and `END` - read from the DOM, not from the picture. The two endpoints are
  drawn in BPMN event notation (the event circles `([Start])` and `([END])`) and the whole thing is a
  directed flow with one contained group. No `.bpmn` file, no BPMN XML and no modeller canvas is
  published on this page, and the page's own prose does not call the diagram BPMN.
ai_evidence: |
  The AI element is inside the diagram: the subgraph's nodes are AI task names - 'Classify Document',
  'Summarize', 'Identify process', 'Extract Prompt' - followed by 'Generate Business rule'. The page's
  prose describes them as an LLM pipeline: "The AI Developer architecture integrates large language
  models with the FlowX.AI Platform to convert natural language to code." The page's other artefact is
  the AI Developer's own product UI (its configuration panels), classified separately on the census's
  contact sheets. So this page publishes a process diagram with start/end events and four to five LLM
  tasks inside it - an AI element inside a BPMN process (INCLUDE) or an AI pipeline drawn with
  BPMN-shaped endpoints (EXCLUDE), depending on the corpus's notation rule.
note: |
  Read from the page's own published markdown twin
  (https://docs.flowx.ai/5.9/ai-platform/pre-built-agents/ai-developer.md), from the page as displayed
  in the browser (2026-09-25) and from the rendered diagram's DOM (see bpmn_evidence). The capture next to this record is a text render of the page's own fenced diagram source and of the sentences that name it, because the page publishes its process as Mermaid rather than as a diagram image (the same convention records 001 and 004 use). This row is UNCERTAIN, not an
  exclusion, because the notation is neither decisively BPMN (no `.bpmn` XML, no modeller canvas, plain
  rectangles for the tasks) nor decisively not-BPMN (BPMN event circles at both ends, one
  sub-process-shaped group): naming the notation here is a judgement call for the researcher.
  This is the 5.9 twin of record 008 (n=95, 4.7.x); its diagram differs in the subgraph label
  ("Document intelligence" against "DI Platform process"), so the two are separate items, not
  duplicates.
