---
n: 78
record: 002
url: https://www.ibm.com/docs/en/ibamoe/9.5.x?topic=workflows-authoring-bpmn
source: ibm-bamoe
surface: docs:ibamoe-9.5.x
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: >
  The page documents the BPMN editor and its palette, and the palette's AI group (Gen AI Task, AI
  Agent Task) is documented here as an editor feature; the page's own figures show the editor, a
  decision task, property panels and the ad-hoc sub-process, and one of them (task-element-menu.png,
  the capture) shows the element-append menu with the AI task type among the choices - but no figure
  on the page shows a completed process in which an AI node sits with its binding. Does a page whose
  BPMN diagrams contain no AI element, but which documents the AI node types as palette furniture
  and shows them in the element menu, count as a corpus item (INCLUDE), or is it E2-no-ai-element
  because no BPMN diagram on the page contains the element?
bpmn_evidence: |
  The page ("Authoring Workflows with BPMN") is the documentation of the BPMN editor itself. All
  twelve of its figures are BPMN-editor artefacts: bpmn-editor-main-page.png (the editor with a
  process on the canvas), decision-task.png and decision-in-workflow-props.png (a DMN decision task
  used inside a workflow), bpmn-process-props-panel.png, bpmn-props-mngmnt.png, bpmn-process-vars.png,
  task-element-menu.png, adhoc-proc-props.png, adhoc-sub-proc.png, adhoc-auto-st.png,
  adhoc-milestone.png, correlations-bmpn-dialog.png. The figures are the editor, the palette and the
  property panels; the only figure that shows a diagram with a process in it is the editor main page.
ai_evidence: |
  The AI element appears here as a palette entry, in the page's own words about the editor's custom
  tasks: "Custom Tasks ( Keyboard Shortcuts ) -> to display custom tasks that have been integrated
  into the editor (e.g., AI and flexible process tasks as ...". The AI group is documented as part of
  the editor's shape set, not as an element placed in a published process.
artefacts:
  - screenshot: 002_ibm-bamoe-docs-authoring-workflows-task-menu.png
  - file: ledgers/_bamoe.raw/workflow__task-element-menu.png
  - file: ledgers/_bamoe/sh_workflow_authoring-workflows.png
capture_quality: legible
capture_width_px: 829
---

## What the file shows

The documentation topic "Authoring Workflows with BPMN" (parent: *Developing stateful Workflows*),
the reference page for the BAMOE Canvas BPMN editor: how to open a workflow, the editor layout, the
task element menu, the process properties panel, process variables, ad-hoc sub-processes
(ad-hoc sub-process, automatic start, milestone) and correlations.

The capture is `task-element-menu.png` (829x870): a "New Task" shape on the canvas with its append
button circled in red, and the menu it opens - eight circular icons, being (1) task, (2) user task,
(3) business-rule/DMN task, (4) service task, (5) script task, (6) embedded sub-process, (7) the AI
task (the sparkle icon), and the milestone flag. So the figure does show that the editor offers an
AI task type from the element menu; it does not show such a node placed in a finished process.

## Observations

- The page is the *manual* of the notation as BAMOE implements it, and it is the only docs topic
  that shows the editor's element menu. The AI sparkle in that menu is the same glyph the Gen AI
  Task node carries in records 001, 004, 005 and 007.
- The page's AI mention is a parenthetical inside the Custom Tasks note; the rest of the page is
  notation mechanics (gateways, ad-hoc sub-processes, variables, correlations) with no AI content.
- Both this page and the "Using Gen AI tasks in Workflows" topic (record 001) document the AI palette
  group, but only the latter shows the node placed on a canvas.

## Notes for the researcher

- I did not resolve this one to INCLUDE or to E2, because both readings are defensible and the
  difference matters for the corpus: treating palette documentation as a corpus item enlarges the
  corpus with editor manuals; treating it as E2 discards a page that demonstrably contains the AI
  node type in the editor's own UI. The capture is attached so the call can be made by eye.
- If the ruling is INCLUDE, this is a *weak* item by the standard of the other records: no process on
  the page contains an AI element. If the ruling is E2, note that the page is the strongest
  documentation evidence in this source that the AI node is a first-class editor feature, which is
  why it was surfaced rather than dropped.
