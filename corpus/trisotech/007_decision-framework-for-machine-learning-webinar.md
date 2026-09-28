# A Decision Framework for Machine Learning (webinar recording) — UNCERTAIN (trisotech)

url: https://www.trisotech.com/decision-framework-for-machine-learning-webinar/
accessed: 2026-09-25
title: A Decision Framework for Machine Learning (webinar recording)
record: 007

bpmn_evidence:
  The artefact is inside the recording, and the recording was watched end to end this session
  (110 canvas frames on a 31 s grid over the 3407 s runtime; all 39 screen-change frames viewed at
  full size, and the one BPMN slide zoomed 3x in two halves to read every label and marker).
  The BPMN artefact is the slide "BPMN: Permissible Use Framework": a pool of lanes (the lane bands
  reading Data / Monitoring / Compliance / Usage, with the vertical lane labels Validate / Monitor /
  Compliance / Use / Monitoring on the left), the start event "Start ML Process" -> the user task
  "Model Access and Data Collection" -> the business-rule task "Producing Classes", the user task
  "Create Models" -> the business-rule task "Generate Analytics" -> the business-rule task "Generate
  Explanation" -> the user task "Deploy Model" -> the end event "End ML Process", the user task
  "Contractual Usage" -> exclusive gateway (Pass) -> user task "Data Usage" -> exclusive gateway
  (Pass/Fail), the user task "Model Usage" -> exclusive gateway, and the user task "Monitor and
  Evaluate Business Outcomes"; plus the data store "Explanations and Analytics" and the data objects
  Data and Business at the top.
  Every task marker in that model is a standard BPMN marker: a person for the user tasks, a table
  for the business-rule tasks, and a call-activity marker on "Deploy Model". The vendor's own marker
  for an ML-bound task - the PMML / Predictive Model task marker, which it does draw elsewhere in
  this source (record 030) - does not appear anywhere in this model.
  The recording's other diagrams are not BPMN: "DMN Implementation" and "Boundary Rules" are DMN
  decision-requirements graphs (oval input data, rectangular decisions, the decision "Ripper
  Predictive Model" with Attribute1/2/3 and Test Data), "ML + MO + DD = AI", "Data vs Decision
  Scientist" and "Usage Stage" are box/architecture illustrations, and the rest are bullet slides.

ai_evidence:
  "This framework will be enabled through the use of BPMN and DMN – a process for permissible use, decisions to ensure proper use of data and models, and explainable AI embodied in decisions."
  Read carefully, the page's own sentence places the AI in the *decisions* ("explainable AI embodied
  in decisions"), which is the DMN half of the framework, and the recording is consistent with that:
  the ML content is the DMN decision "Ripper Predictive Model" and the explanation techniques
  discussed in prose and slides (LIME + Ripper, algorithmic bias, AI ethics, "A.I. = ML + Model
  Orchestration + Decision Design"). Nothing in the BPMN process is labelled as an AI task, and no
  AI performer badge is drawn on any task in it.

question for the researcher (needs_human_ruling):
  A BPMN process whose own task names are "Create Models", "Generate Analytics", "Generate
  Explanation", "Deploy Model" and "Monitor and Evaluate Business Outcomes", inside a talk whose
  subject is enabling machine learning, but drawn entirely with human (person), business-rule
  (table) and call-activity markers and with no AI marker anywhere: does the framing of the process
  around ML models make it an AI-in-BPMN artefact, or is this E2-no-ai-element because no AI element
  is drawn inside the process (the AI sitting in the DMN decisions the page names, and in the slides)?
  The element implementations are not visible, which is why this row is UNCERTAIN rather than E2.

screenshot: 007_decision-framework-for-machine-learning-webinar-poster-frame.png
capture_quality: null
