# Knowledge Worker Copilot in the Loop: AI-Powered Contract Workflows (webinar recording) — UNCERTAIN (trisotech)

url: https://www.trisotech.com/knowledge-worker-copilot-in-the-loop/
accessed: 2026-09-25
title: Knowledge Worker Copilot in the Loop: AI-Powered Contract Workflows (webinar recording)
record: 019

bpmn_evidence:
  The recording was watched end to end this session (110 canvas frames on a 26 s grid over the
  2852 s runtime; all 74 frames the capture flagged as screen changes were viewed as four contact
  sheets, and the process diagram was then read at 2.2x and its tasks at 7-8x).
  The talk is Tom DeBevoise's and Denis Gagné's "Knowledge Worker CoPilot — AI and BPM+" webinar,
  with an outline "Set the Context / Explain the problem we are trying to solve / Explain how we
  tackle that problem / Examples and Demo / Conclusion".
  One slide publishes a BPMN 2.0 process model, "KW CoPilot in Action (Notional)" (t = 1820 s,
  captured at 019_knowledge-worker-copilot-in-the-loop-bpmn-notional-process.png and read at 2.2x
  in raw/video/knowledge-worker-copilot-in-the-loop/z_diagram.png). It is drawn in the vendor's own
  modeller idiom: a pool/lane band labelled "KW CoPilot Case" holding the task "Contract Sentiment
  Extraction" (fed by the data object "Contract" through a [create] association, and producing the
  data objects "Contract Terms and Conditions", "Contract Deliverables", "Contract Contacts" and
  "Contract Calendar"), then a sub-process / group "Manage Contract" with the tasks "Manage
  Stakeholder Communication", "Store Terms and Conditions to read", "Manage Contract Calendar",
  "Schedule Deliverable", "Request Deliverable Review", "Request Deliverable Approval" and "Forward
  Deliverable", the exclusive gateways "Extraction Completed?", "Review Required?", "Approval
  Required?" and "Deliverable Completed?", the timer intermediate event "Contract Milestone"
  (with [update] / [create] / [occur] data associations), a nested group "Complete Accountable
  Deliverables", and the end events "Contract Terminated" and "Contract Fulfilled".
  The rest of the recording is not BPMN: the deck slides on knowledge work, the "KW CoPilot
  leverages Neuro-Symbolic AI" slides, the case/workflow prose slides, and the demonstration, which
  is the product itself (a "KW Copilot" web application: the case dashboard "Real Estate Case
  2025" with its Terms & Conditions and their red/green statuses, Google Drive folders of
  submitted artifacts, the knowledge worker's Gmail inbox, the Google Calendar for August 2025, the
  document "Termite Prevention and Control Methods" being read, and the "Ask KW Copilot" chat), not
  a modeller screen and not a model.

ai_evidence:
  "orchestrates BPM+ workflows and AI reasoning to automate follow-ups, surface real-time insights,
  and keep legal, compliance, and sourcing teams perfectly aligned"
  Inside the process, the AI content is the performer rather than a task type: the pool the whole
  model sits in is named "KW CoPilot Case", every task in it carries a small performer badge at its
  top-left corner, and the talk's own slides state the construct ("Our Solution: KW CoPilot — KW
  Copilot - Augmented intelligence ... The KW Copilot is an intelligent Digital Assistant that
  interacts with knowledge workers to assist them with tasks"; "KW CoPilot leverages Neuro-Symbolic
  AI - The KW Copilot combines the adaptability of Generative AI with deterministic BPM+ models -
  BPM+ Models are deterministic visual models readable by both Humans and Machines - DMN (Decision
  Model and Notation) / CMMN (Case Management Model and Notation) / BPMN (Business Process Model
  and Notation)"; "The KW CoPilot captures events, documents, and stakeholder roles" / "The KW
  CoPilot contextualizes the case workflows and Generative AI reasoning"), and one task name is an
  AI operation ("Contract Sentiment Extraction"). The badge itself could not be resolved at the
  video's 1280x720 resolution even at 8x (z_task_sentiment.png, z_task_compare.png): it is a small
  dark glyph that may be the vendor's AI/agent performer marker or an ordinary task marker, and the
  same badge sits on every task in the model, which is why this row is UNCERTAIN rather than
  INCLUDE. The demonstration's own screens are the copilot application, not a process model.

question for the researcher (needs_human_ruling):
  This recording publishes a real BPMN 2.0 model - "KW CoPilot in Action (Notional)", a pool named
  "KW Copilot Case" with the task "Contract Sentiment Extraction", eight further tasks, four
  exclusive gateways, timer and data-object associations and two end events - and the talk frames
  the model as the AI copilot's own case workflow ("The KW Copilot is an intelligent Digital
  Assistant that interacts with knowledge workers to assist them with tasks"; "orchestrates BPM+
  workflows and AI reasoning"). Every task in it carries an identical small performer badge whose
  glyph I could not read at the published 1280x720 resolution. If that badge is the vendor's
  AI/agent performer marker, the AI element is drawn inside the process and this row is INCLUDE; if
  it is an ordinary user-task marker, the row is E2-no-ai-element, which is how this ledger already
  rules the sibling talk's contract-workflow diagrams (row 202: "the published BPMN process
  diagrams of the contract workflows do not carry an AI element inside the process") and the paired
  deck of this talk (row 431, E1-not-bpmn). A researcher who can open the model, or a higher
  resolution copy of the recording, could settle it in one look; I could not.

screenshot: 019_knowledge-worker-copilot-in-the-loop-bpmn-notional-process.png,
  019_knowledge-worker-copilot-in-the-loop-poster-frame.png
capture_quality: marginal

note for the researcher:
  The diagram is captioned "(Notional)" by the vendors themselves, and it is a slide picture, not a
  downloadable model - no .bpmn file, no live modeller screen anywhere in the recording. I did not
  rule E3 against the paired deck (row 431): that row records no artefact.
