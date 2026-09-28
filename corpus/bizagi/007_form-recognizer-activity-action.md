---
n: 132
source: bizagi
source_name: Bizagi (vendor documentation, help.bizagi.com)
source_type: vendor docs
title: Executing Form Recognizer from an activity action (Temporarily unavailable)
url: https://help.bizagi.com/platform/en/form_recognizer_activity_action.htm
accessed: 2026-09-24
verdict: UNCERTAIN
needs_human_ruling: true
question: "Azure Form Recognizer is bound as an Activity Action of a BPMN task; the diagram itself shows only "Upload file" and "Display file" tasks. Does an AI connector bound at activity level count as an in-process AI element?"
needs_visual_check: false
bpmn_evidence: vendor figure: BPMN pool FormRecognizerTest, Lane 1, Upload file -> Display file, start and end events
bpmn_evidence_quote: "Upload file, Display file"
ai_evidence: page text + the vendor figure
ai_evidence_quote: "In this example you must create it in the Upload file task and On Exit."
artefacts:
  screenshot: 007_form_recognizer_execution_01.png
  archive: 007_form_recognizer_activity_action.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: poor
capture_width_px: 799
capture_method: curl of the vendor's own .png asset at its native URL (help.bizagi.com documentation image)
---

## What the page shows

A small BPMN process model used by the example: pool `FormRecognizerTest`, `Lane 1`,
start event -> user task `Upload file` -> user task `Display file` -> end event. The
page is in the `Artificial Intelligence Connectors` branch and walks through attaching
Azure Form Recognizer to that process.

## Observations (description only, no interpretation)

- **AI activity - function:** the connector extracts data from an uploaded document; the
  page's figures show the resulting form attributes (`Birth date`, `City of birth`,
  `First name`, `Last name`, `Middle initial`, `Occupation`, `Social security number`).
- **AI activity - element type:** not a BPMN element - an Activity Action on the task:
  "in this example you must create it in the Upload file task and On Exit".
- **Authority - downstream:** the extracted fields populate the next form (`Display file`).
- **Authority - data:** the attribute list above (from the second figure of the page).
- **Authority - control:** none; no gateway in the model.
- **Input provenance:** an uploaded file (the driver's-licence image used by the example).
- **Guards present:** none observed.
- **Prompt / model detail visible:** not visible on the page (a cloud service endpoint is
  configured on the separate Form Recognizer resource pages).

## Notes for the researcher

- The page also carries a notice: "The Bizagi team is actively working on updating the API
  version to restore functionality to the Form Recognizer connector" - a deprecation note
  on an AI connector.
- Capture 799 px wide, `capture_quality: poor` by rule; element labels are legible.
