---
n: 114
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Automate Batch Predictions
url: https://marketplace.camunda.com/apps/451491/automate-batch-predictions
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: BPMN diagram published as the listing's overview asset; no .bpmn downloadable. Read natively: start event -> 'Upload file to GCS' -> 'Create JSONL file' -> 'Upload JSONL file to GCS' -> 'Create a batch prediction' -> 'Get Job State' -> exclusive gateway 'Is Job complete?' -> Yes -> 'Get Output URI' -> end event 'Batch Prediction Completed'; No -> 'Inform Prediction Failure' -> end event 'Batch Prediction Failed'. Each task carries an element-template glyph at its top-left.
bpmn_evidence_quote: "Create a batch prediction"
ai_evidence: The AI element is the task 'Create a batch prediction', which submits a job to Google Cloud Vertex AI against a pre-deployed model; 'Get Job State' and 'Get Output URI' are the Vertex AI job operations around it. The page says the blueprint uses 'a pre-deployed machine learning model for outcome predictions' and that it 'leverages pre-deployed AI models to deliver reliable and accurate predictions'. The AI here is classic ML batch inference, not a generative model, and no AI-agent element is used.
ai_evidence_quote: "This blueprint leverages pre-deployed AI models to deliver reliable and accurate predictions"
artefacts:
  screenshot: 114_automate-batch-predictions.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1100
capture_method: curl of the listing's own overview asset (d3bql97l1ytoxn.cloudfront.net, overview/img6358912466808948414-2x.png, 1100x178); native read at full size - a wide, short strip of the whole process
---

## What the page shows

Acheron's 'Automate Batch Predictions' blueprint (Partner, 'Automated predictions with Vertex AI'). The page describes an end-to-end automated pipeline that uploads a data file, converts it to JSONL, runs a Vertex AI batch prediction with a pre-deployed model, polls the job and retrieves the output; its published diagram is that pipeline from start to both terminal states.

## Observations (description only, no interpretation)

- **AI activity - function:** run a batch prediction job against a pre-deployed Vertex AI model and retrieve the output URI.
- **AI activity - element type:** an ordinary `serviceTask` ('Create a batch prediction') plus two job-state tasks; no AI-agent or ad-hoc element is used.
- **Authority - downstream:** 'Get Job State', the 'Is Job complete?' gateway and 'Get Output URI' consume the job; the failure branch ends in 'Inform Prediction Failure'.
- **Authority - data:** the uploaded data file and its JSONL conversion in Google Cloud Storage; the prediction result arrives as an output URI.
- **Authority - control:** one exclusive gateway on job completion with an explicit failure end state - the only control in the model.
- **Authority - control (human):** none - the page states 'The entire process is fully automated, from job initiation through to the retrieval of prediction results'.
- **Input provenance:** a file uploaded by the process itself ('Upload file to GCS'), converted to JSONL before submission.
- **Guards present:** the completion check and the failure notification; no confidence threshold, validation or human review anywhere in the model.
- **Prompt / model detail visible:** the model is not identified in the diagram; the page calls it a 'pre-deployed machine learning model'.

## Notes for the researcher

Recorded as INCLUDE because the process's central task is a call to an AI service (Vertex AI batch prediction), the same basis as the ABBYY Vantage record in this batch - but the researcher should note that this is ML batch inference rather than an LLM element, and that the page describes the pipeline as fully automated with no human checkpoint. The listing also publishes a 'Watch Demo' video, but a diagram is published as an image, so the operator's video rule does not apply.
