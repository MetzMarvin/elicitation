# Enterprise AI in 2026: From Experimentation to Operational Value (webinar recording) — UNCERTAIN (trisotech)

url: https://www.trisotech.com/enterprise-ai-in-2026/
accessed: 2026-09-25
title: Enterprise AI in 2026: From Experimentation to Operational Value (webinar recording)
record: 014

bpmn_evidence:
  The artefact is inside the recording, and the recording was watched end to end this session
  (107 canvas frames on an 18 s grid over the 1920 s runtime; all 34 frames the capture flagged as
  screen changes were viewed as two contact sheets, and the one frame that shows a modeller was
  zoomed 2.5x and 4x).
  That frame (t = 252 s, captured at 014_enterprise-ai-in-2026-fannie-mae-process-bpmn.png) is a
  shared Windows desktop carrying a browser tab strip reading "appliance repair near me", "ACR
  Digital Enterprise Suite" and "Fannie Mae Selling Guide Onli...", and a URL bar reading
  "acr.trisotech.com/modeler/bpmmnmodeler/#" - i.e. the vendor's own BPMM modeller, in the tenant of
  the co-presenter (the page names the speaker as "Tom DeBevoise, ACR").
  The model open in it, named in the modeller's own tab bar as "Fannie Mae Multiphase Process"
  (with a "Process Breakdown" artefact at the top left), is BPMN 2.0: green-bordered task
  rectangles carrying the modeller's overflow marker - "Credit Score Requirements", "Borrowers
  DTI", "Standard DU Eligibility Requirements", "Standard Manual Underwriting Eligibility
  Requirements", "Manual Underwriting", "Inadmissible Income", "Monthly Housing expense",
  "Monthly Income" - diamond exclusive gateways labelled "Insufficient Credit Score", "Loan
  processing", "Desktop Underwriter", "Unqualified for DU", "Prequalification", "Unqualified for
  Manual Underwriting" and "Income from employment?", a thick-bordered end event labelled "Not
  acceptable credit score", data objects ("credit score", "Borrowers DTI", "Standard Eligibility
  Requirements DU") attached by dotted data associations, and bracket-shaped text annotations citing
  the underwriting source ("B3-1.1-01, General Requirements for Credit Scores"; "12 CFR
  1026.43(c)(2)(vi) Monthly debt-to-income ratio").
  This is the live-demo section of the talk ("LIVE DEMO - AI inside orchestrated control" is on
  screen at t = 72 s and t = 306 s). The recording's other material is not BPMN: Gmail and Google
  Sheets windows being driven by the copilot (t = 90-234 s, t = 270-288 s), the vendor's case
  application ("KW Case Status", "Criticality: 0.0", "Sentiment: 0.3", "Search all conversations"),
  and the architecture drawings "AI Operating Inside a Case" (KWCP Case File), "KWCP architecture:
  neuro-symbolic & assistant layers", "Enterprise systems automate the visible 20 percent" (an
  iceberg infographic) and "The Enterprise failure pattern".
  The page itself publishes only the video's poster frame; its paired deck at
  /enterprise-ai-in-2026-presentation/ is judged separately and is E1-not-bpmn, so this process
  model is published nowhere else in the source.

ai_evidence:
  "Why explicit models are essential when combining symbolic and sub-symbolic AI, and how they
  provide the stability AI systems need in production."
  Read carefully, that sentence puts the models *under* the AI as its control structure, and the
  recording is consistent with it: the AI of the demo is the copilot driving Gmail and Google
  Sheets and the case application, and the BPMN model is the orchestration it works inside. No AI
  marker is drawn inside the process in the one frame of the modeller this recording publishes: no
  AI task, no AI performer badge under any of the legible tasks, no AI-named task.

question for the researcher (needs_human_ruling):
  A recording whose live demo is titled "AI inside orchestrated control" shows a BPMN 2.0 process
  ("Fannie Mae Multiphase Process", mortgage underwriting) in the vendor's modeller, with the AI
  copilot demonstrably operating outside the diagram (Gmail, Sheets, the case app), and the page
  says the models are what give AI "the stability AI systems need in production". The process is
  legible at 2.5x and carries no AI element, but the model is shown at 63% zoom in one 18 s sample
  of a live modeller, so neither the whole canvas nor the element implementations are visible.
  Does a BPMN process that is framed as the control structure an AI operates within - with no AI
  element drawn on it - belong in the corpus, or is this E2-no-ai-element because the AI sits
  outside the process?
  Either way the artefact itself is not in doubt (record 030's PMML task shows this source does draw
  AI-bound tasks when a model has them); what is unresolved is whether this process's tasks are
  AI-bound below the diagram.

screenshot: 014_enterprise-ai-in-2026-fannie-mae-process-bpmn.png,
  014_enterprise-ai-in-2026-poster-frame.png
capture_quality: marginal
