# Novel Coronavirus (COVID-19) presentation — UNCERTAIN (trisotech)

url: https://www.trisotech.com/novel-coronavirus-covid-19-presentation/
accessed: 2026-09-25
title: COVID-19 Decision Automation (presentation deck, 18 slides)
record: 034

bpmn_evidence:
  Slide 11 ("COVID Decision Automation") publishes a BPMN 2.0 process, viewed at full size
  (2048x1152): a start event ("Patient under restrictions"), the business-rule task "Signs of acute
  respiratory infection?" (decision-table marker), the exclusive gateway "Symptomatic?" with the
  outgoing flows "Yes, acute", "Yes, subacute or chronic" and "No" to three end events, and the data
  objects "Do you have a Fever?", "What is your temperature in degrees Centigrade?", "Do you have a
  Cough?", "Did the symptoms start in the past week?" and "Is there evidence of an acute respiratory
  infection?" with their data associations. Beside it the slide shows the corresponding DMN decision
  requirements diagram.

ai_evidence:
  The deck's "Predictive" perspective is stated on the same slide: "Prediction PMML: Predictive Model
  Markup Language A standard from the Data Mining Group System acts based on the PMML Prediction",
  drawn as its own schematic next to the process and the DMN model. "Machine Learning" is also named
  in the deck's API-container architecture slide.
  The uncertainty: the BPMN process itself carries no AI element - its automation is the DMN
  business-rule task - so the predictive model (if it counts as an AI element) sits beside the
  process rather than inside it.

screenshot: 034_novel-coronavirus-covid-19-bpmn-decision-automation.png
capture_quality: legible

note for the researcher:
  needs_visual_check and needs_human_ruling. Two questions for the same diagram: whether a PMML
  predictive model counts as an AI element at all for this study, and if so whether it counts when it
  is drawn as its own schematic rather than bound to a task. The process is otherwise a textbook
  decision-automation pattern (BPMN routing over a DMN decision), useful as the non-AI baseline
  against which this source's AI-bound tasks can be compared.
