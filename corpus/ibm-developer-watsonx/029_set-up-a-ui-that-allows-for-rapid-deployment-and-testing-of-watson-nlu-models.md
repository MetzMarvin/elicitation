---
n: 1275
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Set up a UI for rapid deployment and testing of Watson Natural Language Understanding models - the 'NLU.png' interaction figure (a numbered USER -> APPLICATION -> Watson NLU service round trip)"
url: https://developer.ibm.com/tutorials/set-up-a-ui-that-allows-for-rapid-deployment-and-testing-of-watson-nlu-models/
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "The page's interaction figure ('NLU.png', alt text 'Architecture') draws an ordered, numbered interaction - USER icon -(1)-> APPLICATION icon -(2)-> 'Natural Language Understanding Service' -(4)-> back to APPLICATION -(5)-> '{JSON}' result box, with a cloud and a boundary rectangle - and the AI service (the Watson NLU model) is one of the nodes in it. But the nodes are product icons and actors, not activity rectangles, and the order is carried by circled numbers rather than by labelled sequence flows: is this an AI-bearing process artefact drawn in the vendor's house style (so it belongs in the corpus), or a context/interaction diagram that is not a process model at all?"
needs_visual_check: false
bpmn_evidence: "png (tiled on the sweep sheet for gaps 252:276, figs/SHEET_SWEEP25201-25205; viewed full size on 2026-09-26). the drawn figure is the only one on the page: a cloud icon above a boundary rectangle that contains the gold 'APPLICATION' gear icon and the dark-blue 'Natural Language Understanding Service' chat icon; the gold 'USER' person icon sits outside at the left and a '{JSON}' box outside at the right; five circled numbers label the connectors (1 user->application, 2 application->NLU, 3 application->NLU, 4 NLU->application, 5 application->JSON). The page's other figures are console captures (NLUApp, NLU_credentials)."
bpmn_evidence_quote: "The application requests the latest model from the IBM Watson Natural Language Understanding Service"
ai_evidence: "AI elements are inside the drawn figure: one of its nodes is the 'Natural Language Understanding Service', the model-backed IBM Watson NLU service, and the numbered connectors 2 and 3 are the application's requests to it - the page says of them verbatim 'The application requests the latest model from the IBM Watson Natural Language Understanding Service.' That is why the row is UNCERTAIN rather than excluded: the AI service is a node of the drawn, ordered interaction, but the notation is a vendor house style of product icons and circled step numbers rather than BPMN tasks, events or gateways."
ai_evidence_quote: "The application requests the latest model from the IBM Watson Natural Language Understanding Service"
artefacts:
  screenshot: 029_1275X_NLU.png
  assets: [029_1275X_NLU.png]
  bpmn_xml: []
  archive: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: "the figure fetched from its native asset URL on developer.ibm.com and viewed at full size on 2026-09-25"
judgment: true
---

## What the artefact is

`https://developer.ibm.com/tutorials/set-up-a-ui-that-allows-for-rapid-deployment-and-testing-of-watson-nlu-models/` (api, ledger row n=1275), figure `figs/1275X_NLU`.

## What the figure shows



## Why the row is UNCERTAIN

png (tiled on the sweep sheet for gaps 252:276, figs/SHEET_SWEEP25201-25205; viewed full size on 2026-09-26). the drawn figure is the only one on the page: a cloud icon above a boundary rectangle that contains the gold 'APPLICATION' gear icon and the dark-blue 'Natural Language Understanding Service' chat icon; the gold 'USER' person icon sits outside at the left and a '{JSON}' box outside at the right; five circled numbers label the connectors (1 user->application, 2 application->NLU, 3 application->NLU, 4 NLU->application, 5 application->JSON). The page's other figures are console captures (NLUApp, NLU_credentials).

## AI evidence (why this is not an E2 exclusion)

AI elements are inside the drawn figure: one of its nodes is the 'Natural Language Understanding Service', the model-backed IBM Watson NLU service, and the numbered connectors 2 and 3 are the application's requests to it - the page says of them verbatim "The application requests the latest model from the IBM Watson Natural Language Understanding Service." That is why the row is UNCERTAIN rather than excluded: the AI service is a node of the drawn, ordered interaction, but the notation is a vendor house style of product icons and circled step numbers rather than BPMN tasks, events or gateways.

## Notes for the researcher

- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
