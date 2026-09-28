---
n: 159
source: creatio
source_name: Creatio Academy (academy.creatio.com), version 10 - process elements reference / system actions
source_type: vendor product documentation
title: Predict data process element
url: https://academy.creatio.com/guides/no-code-customization/bpm-tools/process-elements-reference/system-actions/predict-data-process-element
accessed: 2026-09-24
verdict: UNCERTAIN
needs_human_ruling: true
question: "This page documents the 'Predict data' element - the element that places a trained machine learning model INSIDE a business process ('uses trained machine learning (ML) models to predict data for records as part of a business process'). Its single figure is the element's setup area (Fig. 1 'Setting up parameters of the Predict data element'), not a process model. Same boundary question as record 002 (Call Creatio.ai): does an AI element placed inside a process count as an artefact when only its parameter panel is published, with the process model itself appearing on a neighbouring page (record 001, where the same element is drawn as the task 'Predict account category')?"
bpmn_evidence: "NONE on this page: the page publishes exactly one figure and it is the element's parameter panel - 'Fig. 1 Setting up parameters of the Predict data element' - showing the Machine learning model list, the prediction type and the record to predict. No process diagram, no process designer canvas. (The element itself is drawn inside a BPMN process on the sibling AI-tools page, corpus record 001.)"
bpmn_evidence_quote: "Fig. 1 Setting up parameters of the Predict data element"
ai_evidence: "The element is the AI element: 'The Predict data process element uses trained machine learning (ML) models to predict data for records as part of a business process. Specify a previsouly created ML model to predict data and select records for prediction.' The page also names the precondition that binds the element to a trained model: 'Prediction models have to be trained before they can be used in the business process.'"
ai_evidence_quote: "uses trained machine learning (ML) models to predict data for records as part of a business process"
artefacts:
  screenshot: 003_predict-data-process-element.png
  screenshot_2: null
  archive: null
  bpmn_xml: null
capture_source: figure-as-published
capture_quality: legible
capture_width_px: 343
capture_method: "the page's own single figure, downloaded from the Academy CDN and kept unmodified"
duplicate_of: null
access: public
---

## What the page shows

The element-reference page for **Predict data**, the element that carries a trained ML model into a
process:

> "The Predict data process element uses trained machine learning (ML) models to predict data for records
> as part of a business process. Specify a previsouly created ML model to predict data and select records
> for prediction."

It adds the precondition - "Prediction models have to be trained before they can be used in the business
process. If the model is not trained, it ..." - and then documents the element's setup: the *Machine
learning model* list, the prediction type, and which record to predict. The single figure is that setup
panel.

## Observations (description only, no interpretation)

- **AI activity - function:** predicts data for records using a trained ML model, at the point in the
  process where the element is placed.
- **AI activity - element type:** a *system action* element of the process designer (a task type in the
  process model).
- **AI activity - model binding:** explicit and visible in the figure - the element selects a previously
  created ML model from a list; the model is trained outside the process.
- **Authority - downstream:** the predicted value is written to the record for the elements that follow.
- **Authority - control:** the process (the element's position and its record filter) decides what is
  predicted and when.
- **Guards present:** the page names no confidence threshold and no review step; the only guard is the
  trained-model precondition.
- **Input provenance:** the customer's own model, trained on the tenant's data.
- **Availability:** no gate named on the page.

## Notes for the researcher

This page and record 002 raise the same boundary question in a stronger form, because the page's first
sentence states the element's position *inside* the process ("as part of a business process") while the
published figure is the element's parameter panel. The same element is drawn as a BPMN task - "Predict
account category", with the prediction icon - on the AI-tools page recorded as corpus record 001, so the
two records describe the same element from opposite sides: one shows it in the model, this one shows how it
is bound to a model.
