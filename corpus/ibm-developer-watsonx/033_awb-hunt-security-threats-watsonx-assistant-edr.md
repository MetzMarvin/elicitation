---
n: 1449
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Threat discovery with watsonx Assistant and IBM QRadar EDR - the 'EDRHunt chatbot workflow' figure (four product panels joined by gerund-labelled hand-off arrows)"
url: https://developer.ibm.com/articles/awb-hunt-security-threats-watsonx-assistant-edr/
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "The page's EDRHunt figure draws an ordered hand-off between four participants - a Watson Assistant panel, then an IBM Cloud Code Engine panel, then an IBM QRadar EDR panel, then back to Watson Assistant - with the arrows labelled by what each step does ('Parsing the intent', 'Deriving and fetching IOC details', 'Retrieving info from QRadar...', 'Predicting the threat intelligence...', 'Providing the threat intelligence back to the user'), and the AI work (predicting threat intelligence) sits inside one of those steps. The page itself introduces it as a workflow ('Following is a typical workflow for using AI Discover'). But the panels are UI mock-ups joined by gerund-labelled arrows, with no BPMN events, task types, gateways, pools or lanes. Is this a BPMN 2.0 model in the vendor's house style (so it belongs in the corpus), or a proprietary panel-and-arrow illustration that E1-not-bpmn excludes?"
needs_visual_check: false
bpmn_evidence: "png (tiled on SHEET_SWEEP30002; viewed full size). the page's only drawn figure: four stacked product panels (watsonx Assistant, IBM Cloud Code Engine, IBM QRadar EDR, watsonx Assistant) joined by arrows whose labels are gerunds describing the exchanged work - 'Parsing the intent', 'Deriving and fetching IOC details', 'Retrieving info from QRadar and validating the IOCs', 'Predicting the threat intelligence using QRadar EDR and watsonx Assistant', 'Providing the threat intelligence back to the user'. The prose narrates the same order step by step."
bpmn_evidence_quote: "Following is a typical workflow for using AI Discover: The user provides a threat advisory URL to watsonx Assistant."
ai_evidence: "AI elements are inside the drawn figure: two of the four panels are the AI participants themselves (watsonx Assistant twice, IBM QRadar EDR once) and one of the labelled steps is the AI's inference, 'Predicting the threat intelligence using QRadar EDR and watsonx Assistant'; the page introduces the figure verbatim: 'Following is a typical workflow for using AI Discover: The user provides a threat advisory URL to watsonx Assistant.' That is why the row is UNCERTAIN rather than excluded: the AI agents are the participants of an ordered, labelled workflow, but the drawing is a stack of product panels joined by gerund-annotated arrows - no BPMN events, task types, gateways, pools or lanes are visible - so I cannot show the notation is BPMN 2.0 rather than a house-style illustration of it."
ai_evidence_quote: "Following is a typical workflow for using AI Discover: The user provides a threat advisory URL to watsonx Assistant."
artefacts:
  screenshot: 033_1449X_EDRSummary_20Workflow.png
  assets: [033_1449X_EDRSummary_20Workflow.png]
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

`https://developer.ibm.com/articles/awb-hunt-security-threats-watsonx-assistant-edr/` (api, ledger row n=1449), figure `figs/1449X_EDRSummary_20Workflow`.

## What the figure shows



## Why the row is UNCERTAIN

png (tiled on SHEET_SWEEP30002; viewed full size). the page's only drawn figure: four stacked product panels (watsonx Assistant, IBM Cloud Code Engine, IBM QRadar EDR, watsonx Assistant) joined by arrows whose labels are gerunds describing the exchanged work - 'Parsing the intent', 'Deriving and fetching IOC details', 'Retrieving info from QRadar and validating the IOCs', 'Predicting the threat intelligence using QRadar EDR and watsonx Assistant', 'Providing the threat intelligence back to the user'. The prose narrates the same order step by step.

## AI evidence (why this is not an E2 exclusion)

AI elements are inside the drawn figure: two of the four panels are the AI participants themselves (watsonx Assistant twice, IBM QRadar EDR once) and one of the labelled steps is the AI's inference, 'Predicting the threat intelligence using QRadar EDR and watsonx Assistant'; the page introduces the figure verbatim: "Following is a typical workflow for using AI Discover: The user provides a threat advisory URL to watsonx Assistant." That is why the row is UNCERTAIN rather than excluded: the AI agents are the participants of an ordered, labelled workflow, but the drawing is a stack of product panels joined by gerund-annotated arrows - no BPMN events, task types, gateways, pools or lanes are visible - so I cannot show the notation is BPMN 2.0 rather than a house-style illustration of it.

## Notes for the researcher

- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
