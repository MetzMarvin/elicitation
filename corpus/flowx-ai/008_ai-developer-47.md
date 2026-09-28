---
n: 008
record: 008
url: https://docs.flowx.ai/4.7.x/docs/platform-deep-dive/ai-core/ai-developer
source: flowx-ai
surface: docs:flowx-ai:4.7.x
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: Does the corpus require BPMN 2.0 notation, or does a process this source publishes as a Mermaid graph whose endpoints are BPMN event circles (([Start]) and ([END])) and whose middle is a drawn subgraph of AI task boxes (Classify Document, Summarize, Identify process, Extract Prompt, Generate Business rule) count as a BPMN process with an AI element inside it?
page_publishes: mermaid-process
capture_quality: legible
quotes: the page's own words. Markdown emphasis and code markers are rendered away and long quotations are elided with "..."; text in single quotes is quoted from a label read in the page's own diagram.
screenshot: 008_ai-developer-47.png
artefacts:
  - screenshot: 008_ai-developer-47.png
bpmn_evidence: |
  The page's "Anatomy" section publishes the AI Developer's architecture as a Mermaid `graph TD` diagram
  (the page's own fenced source, read verbatim):
    "graph TD; Start([Start]):::primary subgraph DI_Platform_process [DI Platform process]
    Classify_Document[Classify Document]:::secondary Summarize[Summarize]:::secondary
    Identify_process[Identify process]:::secondary Extract_Prompt[Extract Prompt]:::secondary end
    Generate_Business_rule[Generate Business rule]:::secondary END([END]):::primary Start -->
    DI_Platform_process; DI_Platform_process --> Generate_Business_rule; Generate_Business_rule --> END"
  Two of its seven nodes are drawn in BPMN event notation - the circles `([Start])` and `([END])`, which
  is how a start event and an end event are written - and the flow is a directed sequence with a
  contained sub-process-shaped group. The remaining nodes are plain rectangles carrying AI task names.
  No `.bpmn` file, no BPMN XML and no modeller canvas is published anywhere on this page, and the page's
  own prose does not call the diagram BPMN.
ai_evidence: |
  The AI element is inside the diagram itself, not only in the prose: the subgraph nodes are AI task
  names - 'Classify Document', 'Summarize', 'Identify process', 'Extract Prompt' - and the step after
  the group is 'Generate Business rule'. The page's prose states what they are: "The AI Developer
  architecture integrates large language models with the FlowX.AI Platform to seamlessly convert
  natural language to code." and, of the generated rule, "Review and implement the generated code".
  So a process diagram with start/end events is published with four to five LLM tasks inside it - which
  is either an AI element inside a BPMN process (an INCLUDE) or an AI pipeline drawn with BPMN-shaped
  endpoints (an EXCLUDE), depending on the corpus's notation rule.
note: |
  Read from the page's own published markdown twin
  (https://docs.flowx.ai/4.7.x/docs/platform-deep-dive/ai-core/ai-developer.md) and from the rendered
  page in the browser (2026-09-25), where the diagram is a live Mermaid `<svg class="flowchart">` whose
  `<g class="cluster">` is `DI Platform process` and whose `<g class="node ...">` elements are the five
  task boxes named above - so the diagram is real, is rendered, and its labels are machine-readable.
  The capture next to this record is a text render of the page's own fenced diagram source and of the sentences that name it, because the page publishes its process as Mermaid rather than as a diagram image (the same convention records 001 and 004 use). This row is UNCERTAIN,
  not an exclusion, because the notation is neither decisively BPMN (no `.bpmn` XML, no modeller canvas,
  plain rectangles) nor decisively not-BPMN (the endpoints are BPMN event circles and the group is a
  sub-process shape): naming the notation here is a judgement call the researcher should make.
  The 5.9 twin of this page (n=464, record 009) publishes the same diagram with a different subgraph
  label ("Document intelligence" instead of "DI Platform process"); the two were kept as separate
  items, not deduped, because the diagrams differ.
