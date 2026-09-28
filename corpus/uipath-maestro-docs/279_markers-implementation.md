---
n: 279
source: uipath-maestro-docs
source_name: UiPath Maestro user guide (docs.uipath.com)
source_type: vendor documentation
title: Multi-instance markers
url: https://docs.uipath.com/maestro/automation-suite/2.2510/user-guide/markers-implementation
accessed: 2026-09-25
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "BPMN task cards with markers (element toolbar with 'Select markers', a marker on a task, a subprocess marker, an example multi-instance task), i.e. BPMN 2.0 element diagrams."
bpmn_evidence_quote: "Use markers to configure the execution of a certain task type to create multiple executions of that task by iterating over a List variable"
ai_evidence: "The page instructs the reader to bind the multi-instance BPMN service task to an agent: 'Action: Start and wait for agent Agent: your invoice validation agent'."
ai_evidence_quote: "Action: Start and wait for agent Agent: your invoice validation agent"
artefacts:
  screenshot: 279_maestro-example-multi-instance-615354-e425af28.png, 279_subprocess-marker-cf45c755.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: page asset at its native URL (dev-assets.cms.uipath.com, .webp converted to .png) or the page's own downloadable model file
capture_quality: marginal
capture_width_px: 720
capture_method: plain GET of the figure asset listed on the page (ledgers/uipath-maestro-docs.raw/img/)
---

## What the page shows

Verbatim from the page:

> "Multi-instance markers link Configure multi-instance markers to iterate a task over a List variable, producing multiple parallel or sequential executions within a Maestro process."

## Judgement

The 2.2510 revision of the multi-instance markers page. Its own figures are the marker diagrams (markers, marker on a task, subprocess marker, example multi instance) rather than the Cloud revision's agent-bound properties-panel capture, but it carries the same implementation step in its prose, so the agent-bound BPMN task is documented on this line too. Recorded separately rather than folded into the Cloud row because the figures differ; the two pages are revisions of one topic and the researcher may want to merge them.

## Artefact reading (native resolution unless stated)

- **BPMN:** BPMN task cards with markers (element toolbar with "Select markers", a marker on a task, a subprocess marker, an example multi-instance task), i.e. BPMN 2.0 element diagrams.
- **AI element:** The page instructs the reader to bind the multi-instance BPMN service task to an agent: "Action: Start and wait for agent Agent: your invoice validation agent".

- `279_maestro-example-multi-instance-615354-e425af28.png` - the multi-instance example diagram on the 2.2510 page
- `279_subprocess-marker-cf45c755.png` - the subprocess marker diagram

## Notes for the researcher

Figure alt text on the page (verbatim): 'markers' | 'marker on a task' | 'subprocess marker' | 'example multi instance'
