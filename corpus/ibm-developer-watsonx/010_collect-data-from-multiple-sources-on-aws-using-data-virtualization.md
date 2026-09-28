---
n: 774
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Gather real-time analytics with IBM Cloud Pak for Data on AWS Cloud - the page's 'flow.png' figure"
url: https://developer.ibm.com/tutorials/collect-data-from-multiple-sources-on-aws-using-data-virtualization/
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "The page's flow.png is a cloud architecture figure - boxes for AWS RDS / Aurora, Red Hat OpenShift on AWS, Cloud Pak for Data, Watson Studio, Data Virtualization, Cognos Dashboard Embedded and Db2, joined by arrows that carry numbered circles (1, 2, 1) marking the tutorial's ordered steps - and the page's own alt text names it a 'step flow'. Its boxes are products and services (an architecture view), but its numbered connectors order the steps of the task the tutorial performs. Is this a process artefact the corpus records, or an architecture diagram that E0-no-artefact excludes?"
needs_visual_check: false
bpmn_evidence: "png, the page's own flow.png fetched and viewed at full size (contact sheet SHEET_VIEW07, row 1 col 1). an AWS / IBM cloud diagram: 'AWS CLOUD' band with an 'AMAZON RDS' box holding 'AMAZON AURORA DB (MySQL)' and '(PostgreSQL)', and a 'RED HAT OPENSHIFT ON AWS (ROSA)' band holding 'CLOUD PAK FOR DATA 4.0', 'WATSON STUDIO', 'DATA VIRTUALIZATION', 'COGNOS DASHBOARD EMBEDDED' and 'IBM DB2'. The connectors carry numbered circles (1, 2, 1). The boxes are products and services, not activities - so by content this is a product architecture view - but the page's own alt text calls the figure a step flow and the connectors are numbered, i.e. the figure is used as the ordered interaction of the tutorial's steps. I hesitated between the two readings and the rules say hesitation resolves to UNCERTAIN."
bpmn_evidence_quote: "Image lays out diagram of step flow of above steps"
ai_evidence: "the page's AI content is the analytics stack the figure arranges (Watson Studio, Cloud Pak for Data, Cognos Dashboard Embedded) rather than an AI element drawn inside the flow: the boxes are AWS and IBM services. The page's premise is verbatim 'This is costly and prone to error when most manage an average of 400 unique data sources for business intelligence.' UNCERTAIN because the page's own alt text calls the figure a 'step flow' and its connectors are numbered, while its boxes are products."
ai_evidence_quote: "Image lays out diagram of step flow of above steps"
artefacts:
  screenshot: 010_774X_flow.png
  assets: [010_774X_flow.png]
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

`https://developer.ibm.com/tutorials/collect-data-from-multiple-sources-on-aws-using-data-virtualization/` (api, ledger row n=774), figure `figs/774X_flow`.

## What the figure shows



## Why the row is UNCERTAIN

png, the page's own flow.png fetched and viewed at full size (contact sheet SHEET_VIEW07, row 1 col 1). an AWS / IBM cloud diagram: 'AWS CLOUD' band with an 'AMAZON RDS' box holding 'AMAZON AURORA DB (MySQL)' and '(PostgreSQL)', and a 'RED HAT OPENSHIFT ON AWS (ROSA)' band holding 'CLOUD PAK FOR DATA 4.0', 'WATSON STUDIO', 'DATA VIRTUALIZATION', 'COGNOS DASHBOARD EMBEDDED' and 'IBM DB2'. The connectors carry numbered circles (1, 2, 1). The boxes are products and services, not activities - so by content this is a product architecture view - but the page's own alt text calls the figure a step flow and the connectors are numbered, i.e. the figure is used as the ordered interaction of the tutorial's steps. I hesitated between the two readings and the rules say hesitation resolves to UNCERTAIN.

## AI evidence (why this is not an E2 exclusion)

the page's AI content is the analytics stack the figure arranges (Watson Studio, Cloud Pak for Data, Cognos Dashboard Embedded) rather than an AI element drawn inside the flow: the boxes are AWS and IBM services. The page's premise is verbatim "This is costly and prone to error when most manage an average of 400 unique data sources for business intelligence." UNCERTAIN because the page's own alt text calls the figure a 'step flow' and its connectors are numbered, while its boxes are products.

## Notes for the researcher

- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
