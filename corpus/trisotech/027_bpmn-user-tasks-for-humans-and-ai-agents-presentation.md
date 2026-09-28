# BPMN User Tasks for Humans and AI Agents — INCLUDE (trisotech)

url: https://www.trisotech.com/bpmn-user-tasks-for-humans-and-ai-agents-presentation/
accessed: 2026-09-25
title: BPMN User Tasks for Humans and AI Agents (presentation deck, 25 slides, Tom Debevoise / Denis Gagné)
record: 027

bpmn_evidence:
  Slide 20 ("DEMO 4: Dynamic supervision") is a BPMN 2.0 process model, viewed at full size
  (2048x1152): a start event, the user task "Evaluate Appraisal Quality" drawn as a rounded
  rectangle, the business-rule task "Determine Next Available Actions" (table marker), the user
  tasks "Manual Review" and "Senior Review", exclusive gateways on the review path, the end events
  "Appraisal Approved", "Request more comparables" and "Appraisal Rejected", and the data objects
  "House Appraisal", "Appraisal Quality", "Next Available Actions" and "Next Action" attached by
  dotted data associations.
  Slide 23 ("DEMO 5: Unsupervised Autonomous AI Performer") is the same notation applied to the same
  appraisal process, again viewed at full size.
  The deck's own text names the notation: "patterns for orchestrating work across both human and AI
  performers" (slide 2) and the demo slides are titled "Dynamic supervision" / "Unsupervised
  Autonomous AI Performer".

ai_evidence:
  The AI element is drawn inside the BPMN model: in both slides the user task "Evaluate Appraisal
  Quality" carries a blue performer badge under the task labelled "AI Reviewer" (slide 20's sibling
  tasks "Manual Review" and "Senior Review" carry the same badge style with "Collateral R…" and
  "Senior Colla…"), i.e. the performer of the task is an AI agent rather than a person.
  Slide 23's own bullets state the binding: "Context provided to the AI Performer: Task Description,
  Data Input(s), Output format dictated by Data Output(s)".
  This is the same "AI as a performer" construct that Trisotech documents in prose elsewhere
  (see record 026), here actually drawn on the task in the deck.

screenshot: 027_bpmn-user-tasks-for-humans-and-ai-agents-demo4-dynamic-supervision.png,
  027_bpmn-user-tasks-for-humans-and-ai-agents-demo5-ai-performer.png
capture_quality: legible

note for the researcher:
  Two captures of the same process under two supervision regimes (human-supervised vs unsupervised).
  The video page for this same talk is recorded separately as record 005 (UNCERTAIN, poster frame);
  the artefacts are different (a poster frame there, the model slides here), so this is not an E3
  duplicate. The deck is hosted on the page as a deck; the page's own per-slide text is what makes
  the demo slides locatable without watching the video.
