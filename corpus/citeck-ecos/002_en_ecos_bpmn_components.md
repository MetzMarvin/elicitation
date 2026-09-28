---
n: 368
source: citeck-ecos
source_name: Citeck ECOS (citeck-ecos.readthedocs.io documentation + Citeck/ecos-demo-app)
source_type: vendor documentation page (BPMN component catalogue)
title: Citeck BPMN Components
url: https://citeck-ecos.readthedocs.io/en/latest/settings_kb/processes/ecos_bpmn/editor/ecos_bpmn_components.html
accessed: 2026-09-24
verdict: UNCERTAIN
needs_human_ruling: true
question: "The page draws every BPMN component as a single element thumbnail, and one of them is the AI Task (a task shape with the AI star badge). Is a one-element legend of the notation an artefact for the corpus, or does the corpus require the element inside a process (start event, flow, end)? I recorded it as UNCERTAIN rather than excluding it, because no sanctioned exclusion code fits: the figures are BPMN 2.0 notation (not E1) and one of them is the AI element itself (not E2)."
needs_visual_check: false
bpmn_evidence: "fourteen thumbnails, each one BPMN 2.0 element as drawn in the platform's editor: task shapes for User task / Script task / Send task / Service task / Set status task / AI Task / Business rule task, a thick-bordered Call activity, gateway diamonds (exclusive, parallel, event-based), the sequence-flow arrows, a sub-process and event circles"
bpmn_evidence_quote: "Each component corresponds to a specific BPMN 2.0 element type and has settings specific to the Citeck platform."
ai_evidence: "the AI element is one of the catalogued components and its thumbnail is the same star-badged task shape the downloadable AI processes use"
ai_evidence_quote: "Tasks - perform actions in the process: user input, script execution, sending notifications, calling services, setting status, AI processing, applying business rules, and calling child processes."
artefacts:
  screenshot: 002_ai_task.png
  assets: [002_set_status_task.png, 002_subprocess.png, 002_events.png]
  archive: 002_en_ecos_bpmn_components.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: poor
capture_width_px: 140
capture_method: curl of the Sphinx _images/ assets at their native URLs
---
## What the page shows

The page is the catalogue of the editor's components. Its fourteen figures are not
diagrams: each is a single element of the notation, drawn alone on a white ground - the
task shapes (`user_task.png`, `script_task.png`, `notification_task.png`,
`service_task.png`, `set_status_task.png`, **`ai_task.png`**, `business_rule_task.png`),
a thick-bordered call activity, four gateway diamonds, the three sequence-flow arrows, a
sub-process, an event gallery (start, boundary, end circles with their markers) and a
pool/lane bar. The AI Task thumbnail is a rounded rectangle carrying the four-point star
badge in its top-left corner, i.e. the same element the two downloadable AI processes
carry as `<bpmn:task ecos:taskType="aiTask">`.

The page's prose says the figure is also the navigation ("Click the image to navigate to
the corresponding section") and names the two AI process examples as sections of their
own ("AI Task", "Comparing Contract Versions", "Automatic Text Generation in a Commercial
Proposal").

## Observations (description only, no interpretation)

- **AI activity - function:** the catalogue lists AI as one of the task categories
  ("setting status, AI processing, applying business rules").
- **AI activity - element type:** a task shape with a star badge - a notation element of
  the editor, listed between "Set status task" and "Business rule task".
- **Authority - downstream / data / control:** not shown on this page - the thumbnails
  carry no connectors, no pools and no configuration.
- **Input provenance:** not shown.
- **Guards present:** none shown.
- **Prompt / model detail visible:** none - the element's own settings live on the
  AI Task page (record 001).

## Notes for the researcher

- This is the element-legend case: the AI element is drawn, but not inside a process. The
  researcher decides whether that counts; the two process-level artefacts with the same
  element are recorded at 001, and the AI Task reference page is row 348.
- Capture: the thumbnails are 129-199 px wide, so `capture_quality: poor` by the 1400 px
  bar; the element shape and its star badge are legible, the file names are the page's own.
