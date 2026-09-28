---
n: 41
source: creatio
source_name: Creatio Academy (academy.creatio.com), version 10 - AI tools / Predictive models
source_type: vendor product documentation
title: Implement prediction models
url: https://academy.creatio.com/guides/no-code-customization/ai-tools/predictive-models/implement-prediction-models
accessed: 2026-09-24
verdict: INCLUDE
bpmn_evidence: "Fig. 1 ('An ML model implementation process') is a BPMN process drawn in the Creatio process designer: a start event labelled 'Account added', one task labelled 'Predict account category' carrying the prediction icon, an end event, and two sequence flows joining them. The page then walks through building exactly that diagram - 'Create a new business process from the process library and add ...' - so the model is the page's own worked example, not an illustration of the notation."
bpmn_evidence_quote: "Create a new business process from the process library and add"
ai_evidence: "The task in the diagram is the Predict data process element, i.e. a trained machine learning model invoked inside the process. The page states the element's role ('set up the actual data prediction in a business process using the Predict data process element') and the worked example is an ML lookup-value prediction: predict the account category whenever a new account with an empty Category field is saved. Fig. 3 is the element's setup area, where the trained model is selected in the 'Machine learning model' list."
ai_evidence_quote: "set up the actual data prediction in a business process using the Predict data process element"
artefacts:
  screenshot: 001_implement-prediction-models.png
  screenshot_2: null
  archive: null
  bpmn_xml: null
capture_source: figure-as-published
capture_quality: legible
capture_width_px: 492
capture_method: "the page's own figure, downloaded from the Academy CDN (d3a7ykdi65m4cy.cloudfront.net) and kept unmodified; it is the whole artefact (the process fragment), so no browser screenshot was needed"
duplicate_of: null
access: public
---

## What the page shows

One of the few AI-bearing diagrams in the whole source. The Academy's "Implement prediction models" page
explains how a trained prediction model is put to work *inside a business process*, and its Fig. 1 is the
process itself:

- a start event, labelled **Account added**;
- one task, labelled **Predict account category**, carrying the prediction (head-and-gear) icon;
- an end event;
- sequence flows between them.

The prose fixes what the task is: "Once your prediction model is created, you can set up the actual data
prediction in a business process using the **Predict data process element**. This will give you complete
control over what records are predicted and when." The worked example is a lookup-value prediction: "Set up
a prediction of the account category whenever a new account with an empty Category field is saved (Fig. 1)."
Fig. 3 is the element's setup area, where the model is chosen in the *Machine learning model* list.

## Observations (description only, no interpretation)

- **AI activity - function:** a trained ML model predicts a field value for a record (here: the account
  category) at a defined point in the process.
- **AI activity - element type:** the *Predict data* process element, drawn as an ordinary BPMN task in the
  process designer. This is the strongest in-process AI element in the source: it is a task in the model,
  not a form control or a panel.
- **AI activity - model binding:** the element binds to a prediction model created and trained outside the
  process ("Prediction models have to be trained before they can be used in the business process", on the
  sibling element-reference page); the page's example model is a lookup-value prediction model for the
  Account category field.
- **Authority - downstream:** the predicted value is written to the record; the page gives no review step
  for the prediction on this page.
- **Authority - control:** the process controls when the prediction runs - the author places the task and
  chooses which records are predicted.
- **Guards present:** none on this page beyond the requirement that the model be trained; no confidence
  threshold or human confirmation appears in the diagram or the text.
- **Input provenance:** the vendor's own model, trained in the tenant on the tenant's data.
- **Availability:** no gating named on this page.

## How it was found

The page sits in the AI tools / Predictive models section of the no-code-customization guide tree, which is
in scope for this source. It is the only page in scope that (a) carries AI/ML vocabulary in its article
text and (b) publishes a BPMN process model in which the AI element is visible as an element of the model -
the neighbouring pages of the same section publish model mini-pages and parameter tabs only.
