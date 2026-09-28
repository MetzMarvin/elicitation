# Automated Guidelines for Healthcare Reimbursement, Series Part 2 — UNCERTAIN (trisotech)

url: https://www.trisotech.com/automated-guidelines-for-healthcare-reimbursement-series-part-2/
accessed: 2026-09-25
title: Automated Guidelines for Healthcare Reimbursement — Series Part 2 (presentation deck, 24 slides)
record: 035

bpmn_evidence:
  The series publishes BPMN 2.0 pathways for the reimbursement process (the preauthorization
  workflow pattern and the off-label request pathway, drawn in the same Trisotech BPMN style as the
  other decks in this source) whose business-rule tasks invoke the decision models of the slide set.
  Slide 22 ("Introducing AI") itself is a DMN decision requirements diagram, not BPMN: the decision
  "Is there established evidence of efficacy?" taking the green decision input "Efficacy Prediction
  Model", with the sub-decisions "What off label usage is planned?", "Are there published reports of
  well controlled studies in peer reviewed journals?" and "Standard Reference Compendia supporting
  request", shown beside a DMN decision table.

ai_evidence:
  Slide 22 is titled "Introducing AI" and its diagram carries the annotation "Predictive model of the
  Quality of Evidence based on Machine Learning of Clinical Trials" on the "Efficacy Prediction
  Model" input. That is an ML-backed decision input to a decision that the BPMN pathway invokes.
  The uncertainty: the AI element is visible in the DMN view, not in the BPMN diagram, so whether it
  sits "inside the process" depends on the same ruling the earlier DMN/BPMN operator note covers.

screenshot: 035_automated-guidelines-part-2-introducing-ai-ml-prediction.png
capture_quality: legible

note for the researcher:
  needs_human_ruling. Sits on the operator's earlier ruling that a DMN decision invoked from a BPMN
  business-rule task is judged on the BPMN diagram: here the invoked decision takes an ML prediction
  as one of its inputs, and the only slide that shows the ML step is a DMN diagram. Part 1 of this
  series is a separate page in the ledger. The annotation naming machine learning over clinical
  trials is the strongest AI claim in the series and is the reason this is UNCERTAIN rather than E2.
