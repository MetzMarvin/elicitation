---
n: 001
record: 001
url: https://docs.flowx.ai/5.9/ai-platform/tutorials/document-processing
source: flowx-ai
surface: docs:flowx-ai:5.9
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: Does the corpus require BPMN 2.0 notation, or does a process this source publishes as a Mermaid flowchart whose node labels are BPMN element names (User Task, Send/Receive Message Task, Exclusive Gateway, End Event) with the AI steps bound into it as workflow calls count as a BPMN process with an AI element inside it?
page_publishes: mermaid-process
capture_quality: legible
quotes: the page's own words. Markdown emphasis and code markers are rendered away and long quotations are elided with "..."; text in single quotes is quoted from another named source (the site's own glossary, or a label read in this page's figure).
screenshot: 001_document-processing.png
artefacts:
  - screenshot: 001_document-processing.png
bpmn_evidence: |
  The process itself is published twice on this page: as a Mermaid flowchart whose node labels are BPMN
  element names, and as prose steps that name the nodes.
    "```mermaid theme={"dark"} flowchart TD A["User uploads documents"] --> B["User Task<br/>(file
    upload UI)"] B --> C["Send / Receive Message Task"] C -. "Workflow: classifyAndExtract<br/>(per
    document)" .-> C C --> D["Send / Receive Message Task"] D -. ..."
  The prose in Step 4, "Build the BPMN process", names the same nodes and adds: "Add a Receive Message
  Task node to capture the extraction output. In the node's Data Stream, set the Key Name to
  extraction.classifiedDocs", "Add a Service Task with a Business Rule action (JavaScript)", "Add an
  Exclusive Gateway after the business rule", "Add an End Event after the summary is received". Step 5
  ties the UI to the BPMN task: "A User Task's UI lives on the node - a standalone UI Flow cannot be
  attached to a BPMN task."
  The page's three figures are node-configuration panels (dp-01 Document Extraction node configuration,
  dp-02 Extract Data from File, dp-03 File Upload response key). No Process Designer canvas figure. The
  process is therefore rendered as Mermaid, not in BPMN 2.0 notation.
ai_evidence: |
  The AI elements are the workflow calls wired into the process's Send/Receive Message Task pairs. The
  page's own workflow table names them: "classifyAndExtract | Document Understanding + Document
  Extraction | Classify document type, then extract fields using type-specific prompts",
  "reconcileData | Text Understanding | Compare extracted fields against application data",
  "generateSummary | Text Generation | Produce a human-re...". The BPMN step keeps the same binding:
  "the two Send/Receive pairs that call classifyAndExtract and reconcileData collapse into one pair that
  calls verifyDocuments per document", and the business rule is there to "supplement the AI
  reconciliation ... to catch issues the LLM might miss".
note: |
  Read from the page's own published markdown twin (https://docs.flowx.ai/5.9/ai-platform/tutorials/document-processing.md), and - where a Mintlify component renders differently from the twin - from the page as displayed in the browser, on 2026-09-25; nothing on this page was paraphrased. The capture next to this record is a text render of the page's own diagram/prose, because the page publishes its process as mermaid-process rather than as a diagram image. The page publishes no BPMN-notation diagram: its 3 figures are node-configuration panels, not a process diagram. The evidence above is quoted verbatim from that page.
