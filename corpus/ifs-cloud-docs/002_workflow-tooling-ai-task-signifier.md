---
n: 16
source: ifs-cloud-docs
source_name: IFS Cloud (technical documentation, Business Process Automation)
source_type: vendor documentation
title: Workflow Tooling - Technical Documentation For IFS Cloud
url: https://docs.ifs.com/techdocs/26r1/040_tailoring/500_business_process_automation/040_workflow_tooling/
accessed: 2026-09-24
verdict: UNCERTAIN
needs_human_ruling: true
question: "The figure ai_signifier_cascade.png shows a BPMN fragment (start event -> service task 'Regulatory Body' -> end event) whose task carries a projection-action list naming 'DemoAiWF [AI]' and 'DemoNonAiWF', and the page's legend says the IFS AI Task Signifier marks 'that an IFS AI Task exists in the Workflow triggered by a Projection action'. Is that AI marker an AI element inside the depicted process (the AI task sits in the triggered workflow, not in this diagram) - i.e. collect it as AI-in-BPMN - or is the AI one hop outside the diagram?"
needs_visual_check: false
bpmn_evidence: "a BPMN process fragment rendered in the IFS Workflow designer: start event -> service task 'Regulatory Body' (gear icon, i.e. a Camunda-class service task) -> end event with sequence flows, plus an attached projection-action popover; the same page shows the designer canvas with service tasks, a properties panel and a signifier tooltip (tourbleshoot_cascade.png, 1487 x 692). No .bpmn XML is exposed for these figures; the page's two downloadable models are zipped (see Notes)"
bpmn_evidence_quote: "provides the ability to model BPMN graphical flow charts"
ai_evidence: "the IFS AI Task Signifier: an '[AI]' tag on the projection-action-triggered workflow 'DemoAiWF' listed against a service task in the BPMN fragment, contrasted with 'DemoNonAiWF' on the same task; plus the page's signifier legend and the management screen's 'IFS AI section'"
ai_evidence_quote: "The IFS AI Task Signifier is used to indicate that an IFS AI Task exists in the Workflow triggered by a Projection action."
artefacts:
  screenshot: corpus/ifs-cloud-docs/002_workflow-tooling-ai-task-signifier.png
  archive: corpus/ifs-cloud-docs/002_workflow-tooling.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: marginal
capture_width_px: 327
capture_method: chrome-devtools-mcp, in-page fetch() of the figure assets images/ai_signifier_cascade.png (327 x 273), images/tourbleshoot_cascade.png (1487 x 692) and images/workflow_management_ai_section.png (1624 x 740); page HTML archived by in-page fetch() of the document URL
---

## What the page shows

`040_workflow_tooling/` is the Workflow Tooling reference page: the Workflow management
screens, the Workflow designer, troubleshooting and observation tooling, deployment, and
the ACP installer. 44,793 characters of body text, ~125 image requests. Release `26r1`.

**The AI-in-BPMN artefact.** The troubleshooting icon legend carries the AI signifier. The
figure `ai_signifier_cascade.png` (327 x 273 px native, `alt` empty) is a **BPMN process
fragment**: a start event (circle) — sequence flow → a service task labelled
"Regulatory Body" (rounded rectangle with the gear icon, i.e. the designer's service-task
shape) — sequence flow → an end event (thick circle). Attached under the task is a
signifier icon and a popover titled "Configured BPA(s) on Projection" whose rows are
"DemoAiWF [AI]" (highlighted), "[After]", "DemoNonAiWF", "[After]". The `[AI]` marker is
what the page's legend names, verbatim: "The IFS AI Task Signifier is used to indicate that
an IFS AI Task exists in the Workflow triggered by a Projection action. This can also be
triggered by a cascade, in which case the icon is displayed as 'E'."

The same page's larger designer figures show the same view class: `tourbleshoot_cascade.png`
(1487 px) is the designer canvas with a start event → three service tasks ("add variable",
"Set Values", "Insert RB", gear icons) → end event, a signifier 'E' under the end event, the
popover "Pending Cascade BPA(s) / LogEnrichedValues [After]", and the right-hand properties
panel (Id "enrichment", "Executable" checked). That figure carries **no** AI marker; together
the two figures show that the signifier family distinguishes AI-triggered ('AI' tag) from
cascade ('E').

**The page's second AI passage** is the management screen's AI section, before the figure
`workflow_management_ai_section.png` (1624 px): "The highlighted IFS AI section below is
displayed when a deployed (Active) Workflow includes IFS AI Task(s). This section lists all
independent AI use cases associated with the Task(s), with each use case representing a
distinct functionality. Refer the IFS AI Task page for more information." That figure is a
UI panel, not a diagram.

**The page's projection walkthrough**, verbatim: "Upload the diagram testProjectionAction.bpmn
and deploy. Set up a projection action for uploaded bpmn as below. Now, whenever you click
the Lock/Unlock command in the Workflow version page, the testProjectionAction Workflow will
run and create (if not exist) a Regulatory Body record with RegulatoryBodyCode PRACT."
A second section, "Initiating Workflows from a Projection Delegate", says "Upload
testProjectionActionCascade.bpmn and deploy."

## Observations (description only, no interpretation)

- **AI activity - function:** not described on this page; it defers, verbatim: "Refer the
  IFS AI Task page for more information."
- **AI activity - element type:** an "IFS AI Task" that "exists in the Workflow triggered by
  a Projection action" (legend), surfaced in the designer by a signifier icon and an `[AI]`
  tag in the projection-action list; the AI task itself is not drawn in the figure.
- **Authority - downstream:** the marker is attached to the task's projection-action
  configuration; no tool list, model name or sub-process is visible on the page.
- **Authority - data:** not visible on the page.
- **Authority - control:** the page relates the AI task to Projection actions and to
  cascades ("This can also be triggered by a cascade"); no gateway or human control step is
  shown in the fragment.
- **Input provenance:** not visible on the page.
- **Guards present:** none observed; the AI section on the management screen is described as
  informational.
- **Prompt / model detail visible:** none on this page.

## Notes for the researcher

- **This row was rewritten during the self-audit.** The earlier version was a bare
  `UNCERTAIN` whose question asked whether *any* figure here shows a BPMN diagram with an AI
  element; the figures were then read, and the answer is that `ai_signifier_cascade.png`
  does: it is a BPMN fragment whose service task carries the `[AI]` projection marker. The
  remaining doubt is only whether that marker counts as an AI element *inside* the depicted
  process, since the AI task lives in the workflow the projection action triggers. Hence
  `needs_human_ruling`, not `needs_visual_check`.
- **The two downloadable models behind this page's walkthrough were fetched and read.**
  `resources/testProjectionAction.zip` and `resources/testProjectionActionCascade.zip` are
  zips, not bare `.bpmn` (the docs' bot protection rejects a plain `curl` of them; they were
  fetched in-page). Contents: `testProjectionAction.bpmn` (one process, 4 `serviceTask` all
  `camunda:class="com.ifsworld.fnd.bpa.IfsProjectionDelegate"`, 2 `exclusiveGateway`, start
  and end events) and `testProjectionActionCascade.bpmn` (one process, 2 `serviceTask`,
  1 `IfsProjectionDelegate` named "Read Bpa Test Entity Set", start and end events).
  **Neither contains any AI/LLM/agent element**, so they are evidence for excluding the
  *models* while the signifier figure remains the artefact. Kept as
  `ledgers/ifs-cloud-docs.raw/testProjectionAction.bpmn` and
  `ledgers/ifs-cloud-docs.raw/testProjectionActionCascade.bpmn`, declared in the ledger row
  via `raw_evidence_files`.
- Captures stored alongside this record:
  `002_workflow-tooling-ai-task-signifier.png` (327 x 273, the decisive figure — the AI
  marker; native resolution is below the 1400 px rule and cannot be improved, but the
  popover text reads legibly at native size, which is why this file is the record's
  `screenshot`);
  `002_workflow-tooling-cascade-designer.png` (1487 x 692, the designer canvas and
  properties panel, showing the 'E' cascade signifier variant, no AI marker);
  `002_workflow-tooling-ai-section.png` (1624 x 740, the management screen's AI section).
- `archive`: the page HTML (838,046 chars) was saved from the rendered document via in-page
  `fetch()`, so the figures and the walkthrough survive vendor edits.
- The record file was renamed from `002_workflow-tooling-ai-section.md` to
  `002_workflow-tooling-ai-task-signifier.md` during the rewrite; the `NNN` number is
  unchanged.
