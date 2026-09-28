# Unleashing Innovation: HL7 AI Challenge Winners Transforming Healthcare with Standards-Based AI (webinar recording) — UNCERTAIN (trisotech)

url: https://www.trisotech.com/hl7-ai-challenge-winners/
accessed: 2026-09-25
title: Unleashing Innovation: HL7 AI Challenge Winners Transforming Healthcare with Standards-Based AI (webinar recording)
record: 017

bpmn_evidence:
  The recording was watched end to end this session (109 canvas frames on a 32 s grid over the
  3482 s runtime; every frame the capture flagged as a screen change was viewed as contact sheets,
  and each drawing that mattered was then read at full frame or zoomed).
  The webinar is a three-team showcase of the inaugural HL7 AI Challenge, and two of the three
  segments publish BPMN 2.0 models, none of them as a downloadable file.
  (1) The Quantek Systems "dynaMap AI" segment (slides 12-14 of its deck, "Inference Based
  Workflow Engine for Clinical or Business Processes") shows a diagram the slide itself captions
  "BPMN" (captured at 017_hl7-ai-challenge-winners-dynamap-bpmn-detail.png, read at 2.6x): start
  event -> user task "Import/Contour" with the person marker -> exclusive gateway (the X diamond,
  labelled "Patient Has Situation Cardiac Implanted Device?") -> "Yes" branch -> user task
  "Contour CIED" with the person marker -> a second exclusive gateway -> onward. Slides 13 and 14
  ("Passive Inference" / "Active Inference", captured at
  017_hl7-ai-challenge-winners-dynamap-bpmn-agent.png) draw the whole process: the dashed pool
  containers "Pre Planning" / "Treatment Planning" / "Follow Up", the start event, the tasks
  "Import/Contour", "Contour CIED", "Fusion Request", "Contour Rounds", "MD Conferencing",
  "Treatment Planning", "Create Plan", "MD/Plan Approval", "Plan Rounds", "Fusion Rounds" and
  "Plan Finalization", the exclusive gateways labelled "Patient Has Situation Cardiac Implanted
  Device?", "Does the Patient Have Previous Fractionation History?", "Has Additional Images or
  Data been acquired?", "Is the patient a Candidate for Proton Therapy?", "Has Fusion been
  acquired?" and the end events.
  (2) The Trisotech segment is a live demonstration, not a slide: the vendor's own modeller
  (acr.trisotech.com) shows the DMN decision-requirement diagram "Anemia Severity WHO Criteria"
  with its decision table, then the BPMN process named in the modeller's tab bar (the "TKA Initial
  (STP)" model, read at 2.2x), and then a "Patient View" application. That process is
  start event "Evaluate for TKA Initial" -> the business-rule tasks "Contraindications to TKA" and
  "Criteria for severe knee arthropathy" (each with the modeller's decision-table and
  protected-information markers) -> the exclusive gateways "Contraindications to surgery?" and
  "Meets criteria?" -> the end events, with the data objects "Height in meters", "Weight in kg",
  "Experimental or investigational procedure?", "Any active infection?", "Articular injection",
  "Pain level", "Pain frequency" and "Knee function". No AI element is drawn on it.

ai_evidence:
  "A clinical workflow engine using active inference to guide patient-specific decisions."
  The page also carries the Trisotech segment's own framing: "Trisotech demonstrates how
  deterministic BPM+ models, HL7 integration patterns, and explicit decision logic create AI agents
  that remain explainable, governable and clinically trustworthy."
  Inside the drawings, the AI content sits at the edge of the process rather than as a task on it.
  On slide 12 the BPMN gateway's condition is resolved semantically: the slide's "Expression
  Builder" holds the expression "Patient | Situation | equals | History of cardiac pacemaker in..."
  and the SPARQL query "ASK WHERE { ?patient <http://snomed.info/sct/243796009>
  <http://snomed.info/sct/161692001>. }" under the caption "RDF Triples", fed by the FHIR panel
  (Source 1 Diagnosis / Source 2 Flag / Source 3 Document -> the coded finding "Cardiac pacemaker in
  situ (finding) SCTID: 441509002"). On slide 14 an orange bar labelled "Agent" points down into
  the start event "Import/Contour", the agent loop is spelled out under the model ("Fetch Data" /
  "Wait" / "Ask" / "Trade Off Actions" / "Reduce Uncertainty" / "Move Forward", slide 13: "Learn" /
  "Predict" / "No Actions" / "Optimization" / "Schedules" / "Resources"), and a run of tasks is
  tinted orange. The tasks themselves are drawn as ordinary user tasks with the person marker:
  no service task, no connector label, no badge inside the model names an AI or agent performer,
  which is the hesitation behind this row.

question for the researcher (needs_human_ruling):
  Two BPMN models are published in this recording, and neither draws an AI element inside the
  process: the Trisotech "TKA Initial (STP)" model has only DMN-bound business-rule tasks, and the
  Quantek "dynaMap AI" model (whose slide captions the drawing "BPMN") is driven from outside by a
  labelled "Agent" bar and resolves its gateway condition with a SPARQL/RDF inference over coded
  FHIR data. Does an AI-branded workflow engine's BPMN process count as carrying an AI element when
  the intelligence is the inference behind a gateway condition and an agent annotated onto the
  model, rather than a task typed as an AI task? This source's ledger already rules the paired
  slide deck of this same talk UNCERTAIN on the same construct (record 036), and I could not
  resolve it from the recording either, which is why this row is UNCERTAIN rather than INCLUDE or
  E2. Related: if the dynaMap slides also appear in that deck, the researcher may want to treat the
  two publications as one artefact - I have left both rows standing, since that is a reconciliation
  question and not mine to settle.

screenshot: 017_hl7-ai-challenge-winners-dynamap-bpmn-agent.png,
  017_hl7-ai-challenge-winners-dynamap-bpmn-detail.png,
  017_hl7-ai-challenge-winners-poster-frame.png
capture_quality: legible

note for the researcher:
  Not ruled E3 against the paired deck (record 036): the deck publishes the talks' slides, the
  recording publishes the slides plus the live Trisotech demonstration (the modeller at
  acr.trisotech.com, the "Anemia Severity WHO Criteria" DRD with its decision table, the TKA
  Initial (STP) process in edit state with its markers, and the "Patient View" app), which is the
  same medium relationship this source already treats as two publications (records 005/027,
  015/029).
