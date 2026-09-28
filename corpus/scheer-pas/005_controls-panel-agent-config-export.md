---
n: 0
url: https://doc.scheer-pas.com/designer/latest/controls-panel
source: scheer-pas
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: >-
  The Controls panel page states that the service export contains the configuration of "each AI
  agent included in this service", and "AI agents are available only on systems with Kubernetes
  setup" - i.e. it presupposes services that contain AI agents. Its one diagram shows the BPMN
  process `JanesFirstBPMN` (a start event, user task, gateway, service task, end event) with no AI
  element in it and the Explorer's `Implementation` node collapsed. Does a service of this kind
  carry the AI agent as an element of its BPMN process (as in the tutorial's
  Insurance_Case_Process, records 001-003), so that this page documents an AI-enabled process
  artefact? Or is the agent here only a service asset whose configuration the export happens to
  include? A reading of the page, and of the export documentation behind it, is needed.
bpmn_evidence: >-
  Fig 1 (captured) publishes BPMN 2.0 notation inside a Designer screenshot: the process asset is
  named `JanesFirstBPMN` in the Explorer under `Process` (its icon is the BPMN model icon), and the
  canvas shows a start event (thin green circle), the user task "James First User Task" (rounded
  box with the person marker), the gateway "James Gateway" (diamond with an X), the service task
  "James First Service Task" (rounded box with the gear marker) and the end event (thick red
  circle), joined by the labelled flows "James Relation_1", "James Relation_2". The validation
  area below names the same elements: "The activity diagram 'James_FirstService_Task' does not do
  anything."
ai_evidence: >-
  The page's AI mention is about agents *in* the service whose export the Controls panel triggers:
  "the compiled agent configuration for each AI agent included in this service (one JSON file for
  each AI agent)" and "AI agents are available only on systems with Kubernetes setup. In a Docker
  ...". Nothing in the figure itself is AI-bound - the model drawn is the "James" example, and the
  Explorer's `Implementation` node (where `Agents` would sit, cf. record 004 fig 2) is collapsed,
  so whether this service contains an agent cannot be read off the figure.
artefacts:
  - screenshot: 005_controls-panel-agent-config-export_fig1.png
capture_quality: legible
capture_width_px: 1468
---

## What the page shows

`Controls Panel` is the reference page for the Designer's Controls panel - the run, test,
validate, deploy, log-analyzer, support-data and export buttons. Its seven figures are:

- **fig 1 (captured)** `controls_panel_default.png` (1468x782) - the panel over the Designer with
  `JanesFirstBPMN` open: the BPMN canvas on the left, the `Attributes` panel (`Name`,
  `JanesFirstBPMN`) on the right, and a validation message under the canvas.
- `controls_additional_menu.png` (337x502) - the panel's additional menu (Pro-Code, Compiler,
  Designer Service, Support Data, Apply CSS, Assets).
- `clear_compiler_cache_icon.png`, `open_log_analyzer_icon.png`, `open_menu_icon.png`,
  `open_test_application_icon.png`, `start_validation_icon.png` - single icons of the panel.

So the page publishes exactly one diagram, and it is BPMN 2.0 (fig 1).

## Observations

- The Controls panel's export function is what the AI sentence is about: the export bundle
  contains, per the page, "the compiled xUML service" and "the compiled agent configuration for
  each AI agent included in this service (one JSON file for each AI agent)". That is a statement
  about what a *service* may contain, not about an element inside the drawn process.
- The drawn process (`JanesFirstBPMN`, the Designer's "James" example also used on the
  troubleshooting and deploying pages) contains no AI element; the `Implementation` node is
  collapsed in the figure, so an agent asset, if present, is not visible.
- Under the corpus rules this is hesitation, not a ground for exclusion: the AI mention cannot be
  dismissed as "AI generating the diagram / roadmap / documentation" (E2), so the row goes to the
  researcher as `UNCERTAIN`.

## Notes for the researcher

The captured figure is a byte copy of the page's own attachment `controls_panel_default.png`; the
Explorer tree was additionally cropped and re-read at 3x (`ledgers/_scheer/aipp/_crop_controls_
panel_default.png`) to confirm the asset name and its BPMN icon. The page's other six figures were
looked at in the AI-page contact sheets (`ledgers/_scheer/ai_s128.png`) and are UI icons and
menus.
