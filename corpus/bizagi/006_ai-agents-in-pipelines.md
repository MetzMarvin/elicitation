---
n: 4
source: bizagi
source_name: Bizagi (vendor documentation, help.bizagi.com)
source_type: vendor docs
title: Execute AI Agents in Pipelines
url: https://help.bizagi.com/platform/en/ai-agents-in-pipelines.htm
accessed: 2026-09-24
verdict: UNCERTAIN
needs_human_ruling: true
question: "The AI Agent is added as a step inside a pipeline invoked from the process: is AI bound through a pipeline action (not a BPMN element) in scope?"
needs_visual_check: false
bpmn_evidence: vendor figure: BPMN pool/lane model behind the Activity actions dialog
bpmn_evidence_quote: "Activity actions (On Enter / On Exit)"
ai_evidence: page text + the vendor figure
ai_evidence_quote: "This enhancement increases the flexibility and power of pipelines, enabling you to incorporate AI-driven tasks throughout your workflows."
artefacts:
  screenshot: 006_aiagents21.png
  archive: 006_ai-agents-in-pipelines.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1919
capture_method: curl of the vendor's own .png asset at its native URL (help.bizagi.com documentation image)
---

## What the page shows

A Bizagi Studio canvas showing a process model (pool with lanes, start event, tasks and
gateway) with the `Activity actions` dialog open over it, divided into `On Enter` and
`On Exit` panels that hold action icons. The page text documents adding an AI Agent to a
pipeline.

## Observations (description only, no interpretation)

- **AI activity - function:** "This enhancement increases the flexibility and power of
  pipelines, enabling you to incorporate AI-driven tasks throughout your workflows." "This
  article shows you how to configure AI Agents within Pipelines in Bizagi, allowing you to
  seamlessly integrate AI into any pipeline step."
- **AI activity - element type:** not a BPMN element - the AI runs as a step inside a
  pipeline, and the pipeline is invoked from a task's Activity actions (the dialog shown).
- **Authority - downstream:** not visible in the figure.
- **Authority - data:** not visible on the page.
- **Authority - control:** not visible on the page.
- **Input provenance:** not visible on the page.
- **Guards present:** none observed.
- **Prompt / model detail visible:** not visible on this page.

## Notes for the researcher

- `needs_human_ruling` is set: AI invoked through a pipeline action rather than bound to
  a BPMN element.
- The dialog image shows empty `On Enter` / `On Exit` panels with action icons; the
  AI-specific icon is not resolvable at this size.
