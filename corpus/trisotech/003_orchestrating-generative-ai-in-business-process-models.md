# Orchestrating Generative AI in Business Process Models — INCLUDE (trisotech)

url: https://www.trisotech.com/orchestrating-generative-ai-in-business-process-models/
accessed: 2026-09-25
title: Orchestrating Generative AI in Business Process Models (blog, Dr. John Svirbely)
record: 003

bpmn_evidence:
  Figure 1 (1004x1464, viewed at full size) is a BPMN 2.0 fragment, and the page calls it one: "In
  Figure 1 there is a portion of a BPMN model for the diagnosis of anemia." The drawing shows a
  sequence flow entering a task "WHO Anemia Grades" whose top-left corner carries the DMN
  business-rule-table marker plus a padlock badge, then a sequence flow to a second task "Generate
  Explanation"; seven data objects (Preferred Language, Language Level, Anemia Severity, Anemia
  Severity Note, Age in Years, Sex Status, "Hemoglobin in g.per dL") attached by dotted data
  associations with data-input/data-output arrowheads. Read from the drawing itself: the site
  publishes no .bpmn/.dmn/.cmmn XML anywhere (negative check across all 768 saved content pages).

ai_evidence:
  Inside the process: the task "Generate Explanation" carries the OpenAI/ChatGPT swirl marker in its
  top-left corner — the same mark the source uses on its "OpenAI Connector" page — i.e. an LLM task
  bound into the process flow, downstream of the DMN decision task, not an AI mention in prose only.
  Page prose: "The problem of translation can be approached by taking the outputs of the decision
  and sending them as inputs to Generative AI (in this case OpenAI, indicated by the icon in the top
  left corner), along with the patient's preferred language and education level."
  and "A business process model can access Generative AI simply by adding a connector to a task,
  which is done by a simple drag and drop."
  and "Orchestration of Generative AI can make it less of a black box."

screenshot: 003_orchestrating-generative-ai-figure1-bpmn-chatgpt-task.png
capture_quality: legible

researcher notes:
  * figure 1 is the page's only figure (the other own-region images are the post header and the
    author portrait).
  * the page's own region carries AI terms: Generative AI, OpenAI, black box.
  * nothing was changed in any vendor tool; the figure was read from the saved page HTML.
