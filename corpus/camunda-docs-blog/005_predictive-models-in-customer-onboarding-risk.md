---
n: 98
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: Predictive Models in Customer Onboarding Risk
url: https://camunda.com/blog/2024/06/predictive-models-in-customer-onboarding-risk/
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: "The AI binding rests on the small element-template icon in the top-left corner of the task 'Verify Risk' (clearly a different icon from the 'R' icon on 'Check Credit Score'): at native 1400 px I cannot resolve whether that icon is the Hugging Face/ML connector template. Is any AI/ML template name, connector binding or properties-panel binding visible anywhere in this figure, or must the AI element be taken from the page prose alone?"
needs_visual_check: true
bpmn_evidence: the captured figure is a rendered BPMN process diagram, read at full width - start event "Submit Application", rectangular tasks ("Check Credit Score", "Verify Risk", "Review Manually", "Notify cannot provide loan", "Generate loan documents", "Send paperwork to start onboarding"), diamond gateways carrying an X marker labelled "Credit Risk Value?" and "Approve or Reject", sequence flows labelled "red", "yellow", "green", "Approved" and "Rejected", and the end events "Loan rejected" and "Loan accepted"
bpmn_evidence_quote: "In this example, a REST Connector returns the credit score for the applicant along with the DTI ratio based on the credit information obtained."
ai_evidence: the page states that a machine learning model is invoked as part of the process by the Hugging Face Connector - "a machine learning model runs using our Hugging Face Connector that will take the following inputs:" - and in the captured diagram that step is the task "Verify Risk", which carries its own connector icon and sits directly before the gateway "Credit Risk Value?" whose red/yellow/green flows branch on the model's output
ai_evidence_quote: a machine learning model runs using our Hugging Face Connector that will take the following inputs:
artefacts:
  screenshot: 005_predictive-models-in-customer-onboarding-risk.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1400
capture_method: chrome-devtools-mcp page fetch; the figure's cdn.sanity.io URL decoded out of the page's /_next/image proxy, downloaded at w=1400
---

## What the page shows

The post describes customer-onboarding risk assessment with AI and ML, and the figure
captured here is the process it walks through. Read at full width it is a BPMN diagram: the
start event "Submit Application" into the purple task "Check Credit Score" (marked with an
"R" icon), then the blue task "Verify Risk", then the exclusive gateway "Credit Risk Value?"
which forks into three colour-coded flows - "red" straight to a join gateway, "yellow" into
the task "Review Manually" and then the gateway "Approve or Reject", and "green" to the join
gateway below. The red branch leaves through the task "Notify cannot provide loan" to the end
event "Loan rejected"; the green branch runs through "Generate loan documents" and "Send
paperwork to start onboarding" to the end event "Loan accepted".

The AI element sits on the "Verify Risk" task. The page says of it that "a machine learning
model runs using our Hugging Face Connector that will take the following inputs:", and adds
that "the Hugging Face model can run a Python program that uses the scikit-learn package" and
that "The model can estimate the probability of each risk class for the applicant." In the
diagram the task carrying the connector's own icon is "Verify Risk", positioned exactly where
the page's narrative puts the model call, immediately before the risk-value branch.

## Observations (description only, no interpretation)

- **AI activity - function:** the page says a machine learning model runs inside the process
  and returns a risk estimate - "The model can estimate the probability of each risk class
  for the applicant", with a second framing under "Detection of anomalies : With machine
  learning models trained on historical fraud data, you can analyze various patterns in the
  data provided by prospective customers".
- **AI activity - element type:** a BPMN task whose implementation is a connector call; the
  page speaks of "the output of this BPMN component", and in the captured figure the model
  step is the task "Verify Risk", drawn with a small brown face icon in its top-left corner,
  distinct from the "R" icon on the neighbouring REST-backed "Check Credit Score" task.
- **Authority - downstream:** the exclusive gateway "Credit Risk Value?" with its "red",
  "yellow" and "green" outgoing flows - red to "Notify cannot provide loan" (end event "Loan
  rejected"), yellow to "Review Manually" and the gateway "Approve or Reject", green to
  "Generate loan documents" and "Send paperwork to start onboarding" (end event "Loan
  accepted").
- **Authority - data:** the page names the data a connector returns earlier in the process -
  "a REST Connector returns the credit score for the applicant along with the DTI ratio based
  on the credit information obtained" - but the list of inputs to the model itself is
  introduced by a colon on the page ("that will take the following inputs:") and is not
  carried in the brief; no variable names are printed in the captured figure.
- **Authority - control:** the gateway "Credit Risk Value?" that consumes the model output,
  the task "Review Manually" on the middle ("yellow") branch, and the following gateway
  "Approve or Reject".
- **Input provenance:** the application data submitted at process start ("Submit Application"
  in the captured figure); the page describes the models as analysing "the data provided by
  prospective customers".
- **Guards present:** a human review branch is drawn - the "yellow" medium-risk flow enters
  the task "Review Manually" before the gateway "Approve or Reject"; the page does not
  describe that step in the brief.
- **Prompt / model detail visible:** no prompt text and no model name are printed; the
  implementation detail the page does give is that "the Hugging Face model can run a Python
  program that uses the scikit-learn package. Using the LogisticRegression and predict
  functions, the model can predict the probability of the risk class for the applicant."

## Notes for the researcher

Both figures on this page have empty alt text, so the BPMN evidence rests on reading the
captured image itself; the first figure is the one captured. The page's model-input list
(the sentence ends with a colon) is not present in the brief's page text, so the inputs are
deliberately left unstated here - anyone re-checking should read the page for that list. The
source asset on cdn.sanity.io is 1024x333 and was downloaded at w=1400 (1400x455 file on
disk), which is an upscale of an already small asset.
