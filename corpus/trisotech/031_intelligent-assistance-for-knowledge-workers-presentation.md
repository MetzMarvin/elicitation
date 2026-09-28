# Intelligent Assistance for Knowledge Workers — INCLUDE (trisotech)

url: https://www.trisotech.com/intelligent-assistance-for-knowledge-workers-presentation/
accessed: 2026-09-25
title: Intelligent Assistance for Knowledge Workers (presentation deck, 57 slides)
record: 031

bpmn_evidence:
  Slide 47 ("NLP Situational Lifting - Process in BPMN") is a BPMN 2.0 model, viewed at full size
  (2048x1152): the start event "Start NLP Situational Lifting", the three tasks "NLP Detection",
  "Concept Lifting" and "Semantic Lifting" (each carrying the collapsed sub-process marker), the end
  event "NLP Situational Lifting End", and the data objects "Paragraph", "Entities", "Sentences",
  "Differentiated Entities", "Situational Business Events" and "Situational Business Objects" with
  their data associations. The slide's own title names the notation and the process.

ai_evidence:
  The AI work is modelled as the tasks of the process: "NLP Detection", "Concept Lifting" and
  "Semantic Lifting" are the NLP pipeline steps, and the deck states the AI techniques and models
  behind them - "The key AI techniques for NLP are: Optical Character Recognition … Entity
  Extraction …", and "Both the Intelligent Agent and the NLP Situational Lifting presented herein
  were implemented using Low Code language FEEL and BPM+ Models". Other slides name the pre-trained
  services used (Google Natural Language, Amazon Comprehend, Microsoft LUIS) and the intelligent
  agent that calls them.

screenshot: 031_intelligent-assistance-nlp-situational-lifting-bpmn.png
capture_quality: legible

note for the researcher:
  The AI step is identified by the task names (NLP/concept/semantic lifting) plus the deck's own
  statement that the pipeline was implemented with BPM+ models and FEEL, rather than by a vendor
  badge drawn on the task - unlike records 027 and 026, where the performer badge is visible. A
  reviewer who requires a visible AI marker on the shape may prefer to reclassify this one as
  UNCERTAIN; the underlying fact (an NLP pipeline published as a BPMN model) is the same either way.
