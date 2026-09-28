---
n: 516
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Creating cloud-native applications: 12-factor applications - the 'Processes diagram' figure (ellipse processes over cylinder data stores)"
url: https://developer.ibm.com/articles/creating-a-12-factor-application-with-open-liberty/
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "The page's 'Processes diagram' draws four ellipses ('Process A' .. 'Process D') joined by arrows (three of them double-headed) with three of them sitting on database cylinders. On a 12-factor page a 'process' is an application process run as a stateless share-nothing instance backed by services, so the figure would be a component picture (ellipses = app processes, cylinders = backing services) and E0-no-artefact excludes it; read the other way it is a data-flow diagram (ellipses = processes, cylinders = data stores) and it is a process artefact the corpus records. Which reading governs, and does the artefact enter the corpus?"
needs_visual_check: false
bpmn_evidence: "png, the page's own figure fetched at full size and viewed as the first tile of SHEET_Z0401; the page's own alt text for it is 'Processes diagram'. a drawing in the data-flow convention: four black ellipses labelled 'Process A', 'Process B', 'Process C' and 'Process D', joined to each other by red arrows three of which are double-headed (Process A exchanges with B, with C and with D), and each of Processes B, C and D sitting on a database cylinder. The page's own alt text calls it a 'Processes diagram'. The page is the source's 12-factor article, where a 'process' is an application process executed as a stateless share-nothing instance backed by services, which would make the ellipses components and the cylinders their backing services; read the other way, the ellipses are business processes and the cylinders data stores, which would make the figure a data-flow diagram. I could not settle the reading from the figure or the alt text, and hesitation resolves to UNCERTAIN."
bpmn_evidence_quote: "Processes diagram"
ai_evidence: "the page carries no AI, LLM or agent element at all - it is the source's 12-factor cloud-native article, and the figure's only content is the four ellipses and their database cylinders - so no AI element sits inside the drawn figure. UNCERTAIN for the reading question in the header above, not for an AI element: on a 12-factor page a 'process' is an application process, which would make the ellipses components."
ai_evidence_quote: "Processes diagram"
artefacts:
  screenshot: 020_516_image06.png
  assets: [020_516_image06.png]
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

`https://developer.ibm.com/articles/creating-a-12-factor-application-with-open-liberty/` (api, ledger row n=516), figure `figs/516_image06`.

## What the figure shows



## Why the row is UNCERTAIN

png, the page's own figure fetched at full size and viewed as the first tile of SHEET_Z0401; the page's own alt text for it is 'Processes diagram'. a drawing in the data-flow convention: four black ellipses labelled 'Process A', 'Process B', 'Process C' and 'Process D', joined to each other by red arrows three of which are double-headed (Process A exchanges with B, with C and with D), and each of Processes B, C and D sitting on a database cylinder. The page's own alt text calls it a 'Processes diagram'. The page is the source's 12-factor article, where a 'process' is an application process executed as a stateless share-nothing instance backed by services, which would make the ellipses components and the cylinders their backing services; read the other way, the ellipses are business processes and the cylinders data stores, which would make the figure a data-flow diagram. I could not settle the reading from the figure or the alt text, and hesitation resolves to UNCERTAIN.

## AI evidence (why this is not an E2 exclusion)

the page carries no AI, LLM or agent element at all - it is the source's 12-factor cloud-native article, and the figure's only content is the four ellipses and their database cylinders - so no AI element sits inside the drawn figure. UNCERTAIN for the reading question in the header above, not for an AI element: on a 12-factor page a 'process' is an application process, which would make the ellipses components.

## Notes for the researcher

- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
