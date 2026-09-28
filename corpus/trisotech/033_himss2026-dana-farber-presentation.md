# HIMSS26 Dana-Farber presentation — UNCERTAIN (trisotech)

url: https://www.trisotech.com/himss2026-dana-farber-presentation/
accessed: 2026-09-25
title: How Dana-Farber Enables Earlier Cancer Symptom Intervention at Scale (HIMSS26 deck, 19 slides)
record: 033

bpmn_evidence:
  Slide 5 ("Using BPMN to model shareable preemptive symptom management pathways") is a BPMN 2.0
  model, viewed at full size (2048x1152): a start event, the tasks "Extract Active Care Plan",
  "Extract Care Plan Information", "Diagram Care Plan Fake DB", "Generate CDS Card Details",
  "Generate Service Request", "Generate Information CDS Card" and the branch task "Generate No
  Information CDS Card" (each carrying its marker - service/script task icons and a padlock on the
  generated outputs), the two exclusive gateways "Has an active Care Plan?" and "Existing regimen
  information?", the two end events "No Information" and "Provided information", and the data objects
  "CarePlan", "Active Care Plan", "PatientPractitioner", "Care Plan", "MRN", "NPI", "Protocol",
  "Card Detail", "Service Request" and "CDS Card" with their data associations. The slide title
  names the notation; the model is drawn on a Dana-Farber "Pathways" grid.

ai_evidence:
  The deck claims AI agents inside these pathways in prose, but the published model carries no AI
  element: no AI performer badge and no AI task is visible anywhere in slide 5.
  Slide 17 states the claim ("AI agents act as performers within orchestrated pathways, analyzing
  symptom severity and routing escalations to the right nurse navigator in real time", with the tag
  "Agent as Performer"), and slide 18 calls the pathways "AI-augmented".
  The second capture is slide 17, the slide that makes the claim, so the researcher can compare claim
  and diagram side by side.

screenshot: 033_himss2026-dana-farber-bpmn-preemptive-pathway.png,
  033_himss2026-dana-farber-agent-as-performer-claim.png
capture_quality: legible

note for the researcher:
  needs_human_ruling. This is the cleanest instance of the method question the source keeps raising:
  the vendor asserts "AI agents act as performers within orchestrated pathways" and tags a slide
  "Agent as Performer", while the BPMN diagram it publishes for those same pathways shows an
  ordinary decision/data pipeline with no AI performer bound to any task. Either the deck's own
  claim counts as evidence of an AI element inside the process, or a visible element in the diagram
  is required - the ruling will also settle records 035 and 036.
