---
n: 546
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Optimize a microservices workflow application architecture with the Camunda Workflow Engine — Figure 6 'Workflow definition in Camunda Modeler': a BPMN 2.0 payment-retrieval process with parallel gateways and service tasks"
url: https://developer.ibm.com/articles/optimize-microservices-architecture-with-camunda/
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "The page's Figure 6 is a BPMN 2.0 model — a lane named 'Payment Retrieval', a start event 'Payment Retrieval Requested', two parallel gateways (diamonds with a + marker), three service tasks drawn with the BPMN gear icon ('Check Credit Card', 'Check Item Info', 'Charge Credit Card') and a terminate end event with a thick ring ('Payment Received') — and it is the second decisively BPMN artefact in this source. But the page contains no AI, LLM or agent mention anywhere (its figures are a legacy ISO-5807 flowchart, a legacy sequence diagram and this Camunda model), so the artefact holds no AI element inside the process and E2-no-ai-element cannot be applied as written: E2 requires quoting the AI mention being dismissed, and there is none to quote. Does the researcher want this non-AI BPMN model recorded in the corpus (it is the source's only example of a BPMN model beside the anchor tutorial's), excluded under E2 with the absence of any AI mention noted, or excluded under another code?"
needs_visual_check: false
bpmn_evidence: "decisive and visible in the figure itself: a pool/lane frame labelled 'Payment Retrieval' running down the left edge; a start event circle labelled 'Payment Retrieval Requested'; two gateway diamonds each carrying a + marker (the BPMN parallel gateway marker), one forking to 'Check Credit Card' and 'Check Item Info' and one joining them; three tasks drawn with the BPMN service-task gear icon ('Check Credit Card', 'Check Item Info', 'Charge Credit Card'); and a terminate end event drawn as a thick-ringed circle labelled 'Payment Received'. The page's own caption is 'Figure 6. Workflow definition in Camunda Modeler', and Camunda Modeler is a BPMN 2.0 modeller whose native format is BPMN 2.0."
bpmn_evidence_quote: "Figure 6. Workflow definition in Camunda Modeler"
ai_evidence: "none anywhere on the page: the article is about replacing a legacy workflow implementation with the Camunda engine, and no AI, LLM, agent, model or assistant is named or drawn. The page's own text mentions only BPMN, business processes and DMN (the page's content API record lists exactly the tokens 'bpmn', 'business process', 'dmn'), and its other two figures are the legacy ISO-5807 flowchart (Figure 1, 'Sample payment workflow') and the legacy UML sequence diagram (Figure 3, 'Original workflow sequence diagram'). So the artefact is BPMN 2.0 but carries no AI element inside the process."
ai_evidence_quote: "Optimize a microservices workflow application architecture with the Camunda Workflow Engine"
artefacts:
  screenshot: 003_bpmn-payment-retrieval-camunda-modeler.png
  assets: [003_bpmn-payment-retrieval-camunda-modeler.png, 003_legacy-iso5807-payment-flowchart.png]
  bpmn_xml: []
  archive: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 2092
capture_method: "figures fetched at their native asset URLs on developer.ibm.com (the article's figures/camunda-workflow-definition.png and figures/payment-workflow.png), viewed at full size on 2026-09-25"
judgment: true
---

## What the artefact is

Figure 6 of the article, captioned "Workflow definition in Camunda Modeler" — a BPMN 2.0 model
of a payment-retrieval process, 2 092 x 806 px, captured as
`003_bpmn-payment-retrieval-camunda-modeler.png`. The page is an *article* (not a tutorial):
"Optimize a microservices workflow application architecture with the Camunda Workflow Engine",
12 125 characters, seven embedded figures.

## Observations (description only, no interpretation)

- Model structure: `startEvent` *Payment Retrieval Requested* → **parallel gateway** (fork) →
  `serviceTask` *Check Credit Card* and `serviceTask` *Check Item Info* → **parallel gateway**
  (join) → `serviceTask` *Charge Credit Card* → **terminate end event** *Payment Received*.
- All of it sits inside a single **lane** labelled *Payment Retrieval* (the lane frame is drawn
  down the left edge of the figure).
- Element-by-element evidence for the notation: the start event is a thin-ringed circle; both
  gateway diamonds carry the `+` marker (BPMN parallel gateway, i.e. AND-split and AND-join);
  the three tasks carry the BPMN **service-task** gear glyph in their top-left corner; the end
  event is a thick-ringed circle (terminate).
- **No AI/LLM/agent element of any kind** in the model, and no AI mention anywhere in the page
  text.
- The same page publishes the *legacy* versions of the same process beside it: Figure 1,
  "Sample payment workflow", drawn as an ISO-5807 flowchart (stadium terminators *Payment Start*
  / *Payment End*, plain rectangles, two Yes/No decision diamonds *Check OK*), captured as
  `003_legacy-iso5807-payment-flowchart.png`; and Figure 3, "Original workflow sequence
  diagram", drawn as a UML sequence diagram. This is the source's one page that puts a
  non-BPMN process drawing and its BPMN replacement side by side.

## Notes for the researcher

- This is the **strongest BPMN artefact in the source after the anchor tutorial** and the only
  one that is a *model* rather than a tutorial step: the notation is unambiguous (lane, parallel
  gateways, service tasks, terminate end event) and it is drawn by a BPMN-native modeller.
- It is `UNCERTAIN` rather than `INCLUDE` for one reason only: the artefact contains no AI
  element inside the process, and the page has no AI mention to dismiss, so `E2-no-ai-element`
  cannot be applied as its own rule requires. The ruling decides between recording it (which
  gives the corpus a clean non-AI BPMN contrast case) and excluding it.
- The legacy pair on the same page (ISO-5807 flowchart, UML sequence diagram) is excluded
  separately on the page's ledger row as `E1-not-bpmn`; they are captured here only because they
  are the same page's artefact set and they document the before/after of the notation.
