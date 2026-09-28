---
n: 720
source: flowable
source_name: Flowable (enterprise documentation, vendor blog/marketing site, training site)
title: Flowable Inspect User Guide | Flowable Enterprise Documentation
url: https://documentation.flowable.com/latest/user/inspect/index.html
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "Does a BPMN diagram on this page contain an AI/LLM element inside the process? The page shows an Agent Service Process BPMN diagram (Get Weather - Review Weather) whose instance invoked the agent E2E Weather Agent, and a CMMN Classify documents case with an AI Agent plan item, but no AI binding is visible in the BPMN diagram itself."
needs_visual_check: false
bpmn_evidence: figure captions, alt text or OCR labels naming BPMN constructs: The Flowable Inspect panel docked in Flowable Work | inspect-panel-387064b10a725cb14a8ab515679520d9.png; The execution tree, diagram and variable list in the Inspect tab | inspect-execution-tree-b9c08681b2e00c97d4943805bb3; 13 execution tree | 13-inspect-execution-navigates-a2d43052af63b450454; 13 diagram view | 13-inspect-enlarge-diagram-8a89a369df2c99943ec0ea9
bpmn_evidence_quote: "Flowable Inspect allows users to debug case, process and task instances by providing additional information about activities, timer jobs, variables and so on."
ai_evidence: not established inside the process. The AI the page does show is an instance view: the Agent Service Process BPMN diagram (Get Weather - Review Weather) whose instance invoked the agent 'E2E Weather Agent', plus a CMMN 'Classify documents' case carrying an 'AI Agent' plan item. No AI binding is visible in the BPMN diagram itself, so whether any task in it is AI-bound is the question in the frontmatter. The census line here was an OCR dump of a Work case screen whose labels name no AI element - false, corrected 2026-09-26.
ai_evidence_quote: "E2E Weather Agent" (the agent named in the instance view, as recorded in the sighted observations below)
artefacts:
  screenshot: 144_documentation-flowable-com-latest-user-inspect-index-html.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 3200
capture_method: urllib download of https://documentation.flowable.com/latest/assets/images/inspect-panel-387064b10a725cb14a8ab515679520d9.png (asset published by the page); labels inside read with RapidOCR, this session cannot receive image content
---

## Why this row is UNCERTAIN

The page publishes figures and mentions AI, but the figure that would decide the
verdict could not be certified from the evidence this session can read (the DOM, the
page text, and OCR labels). Per CLAUDE.md section 5 an unresolved figure is UNCERTAIN
with needs_visual_check, never an exclusion.

## Observations (description only, no interpretation)

- **Figures on the page:** The Flowable Inspect panel docked in Flowable Work | inspect-panel-387064b10a725cb14a8ab515679520d9.png; The execution tree, diagram and variable list in the Inspect tab | inspect-execution-tree-b9c08681b2e00c97d4943805bb3; 13 execution tree | 13-inspect-execution-navigates-a2d43052af63b450454; 13 diagram view | 13-inspect-enlarge-diagram-8a89a369df2c99943ec0ea9
- **OCR labels of the captured figure:** 7Flowable | Search | WORK | For me | Created by me | Open | Create New | Claim CLM-4477 / Classify documents | Sort by: Default | Home page | Classify documents | Claim CLM-4477 | Created: 07/10/202614:15 | Assignee: | Task | FA
- **Page text quote:** Flowable Inspect allows users to debug case, process and task instances by providing additional information about activities, timer jobs, variables and so on.
- **Captured asset:** https://documentation.flowable.com/latest/assets/images/inspect-panel-387064b10a725cb14a8ab515679520d9.png (3200x1900)

## Sighted observations (visual pass elicitation-aa, shard s5, 2026-09-25)

Looked at the diagram-bearing figures natively, not from a contact sheet:
`13-inspect-diagram-navigates-*.png`, `13-inspect-diagram-sub-process-model-*.png`,
`inspect-execution-tree-*.png` (1.6x native crop), `inspect-agent-instances-*.png`,
plus a 9-tile 900 px triage sheet over the other diagram-named captures.

- **BPMN 2.0 present, no AI element visible.** `Inspect Demo Process` = start event -
  user task "Enter request" (with boundary events) - "Handle claim details" -
  service task "Send notification" - end event, plus user task "Handle timeout".
  `Inspect Sub Process` = start event - user task "Complete details" - end event.
  `Agent Service Process` = start event - service task "Get Weather" - user task
  "Review Weather" - end event. None of the visible task labels names an AI element.
- **CMMN 1.1 on the page.** `inspect-execution-tree-*.png` shows the `Classify documents`
  case in CMMN notation: folder-shaped "Case plan model", cut-corner stages `Intake` and
  `Payout`, sentry diamonds straddling the stage borders, and a plan item labelled
  **"AI Agent"** (robot icon) inside the `Payout` stage, next to "Payout failed".
- **Why UNCERTAIN rather than E2.** The same `Agent Service Process` instance
  (PRC-7eb66a0c-…) lists agent instance "E2E Weather Agent" (key `e2eWeatherAgent`) in the
  Agent instances panel, so an element of that BPMN process is very plausibly AI-bound,
  but no figure on the page exposes a task property, binding or properties panel. Per
  CLAUDE.md an element that might be AI-bound but is not visible is UNCERTAIN, never E2.

## What to check

Whether the captured figure (or another figure on the page) is a BPMN 2.0 process
diagram and whether an AI/LLM element sits inside that process.
