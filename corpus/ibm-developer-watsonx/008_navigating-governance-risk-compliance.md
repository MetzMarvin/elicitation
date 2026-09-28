---
n: 543
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Navigating governance, risk management, and compliance in modern business - the 'vendor management lifecycle stages' figure"
url: https://developer.ibm.com/articles/navigating-governance-risk-compliance/
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "The page's Vendormanagement.png is named by its own alt text a 'vendor management lifecycle stages' figure and lists four ordered stages of a vendor-management life cycle (identify, classify, assess, mitigate/monitor/report), each with sub-bullets - but the stages are joined by no connectors, and the numbers are list markers rather than flow. Is a numbered stage list a process artefact the corpus records, or does E0-no-artefact exclude it because no flow is drawn?"
needs_visual_check: false
bpmn_evidence: "png, the page's own Vendormanagement.png fetched and viewed at full size (contact sheet SHEET_PROC101, row 2 col 3). a panel headed 'Vendor management lifecycle' holding four numbered entries with their sub-bullets: 'Identify vendors and third-party suppliers' (Accurate list, Onboarding or existing customer, nth-party risk), 'Classify vendors' (Critical vendors, PII data shared, critical engagements), 'Assess vendor compliance' (Regular assessment based on tier/classification, Ad-hoc assessment (event based)), 'Mitigate, monitor, and report' (Ongoing risk management, KPIs, reporting). The page's own alt text calls the figure 'vendor management lifecycle stages' and the entries are ordered activities - but the figure draws no connectors between them at all. Hesitation resolves to UNCERTAIN."
bpmn_evidence_quote: "vendor management lifecycle stages"
ai_evidence: "the page's AI content is about governing AI third parties rather than an AI element inside the figure: the life-cycle stages it lists (identify vendors, classify them, assess compliance, mitigate and report) are drawn for a risk-and-governance audience and the page says verbatim 'Corporate landscapes encompass a diverse array of industries including energy, manufacturing, cybersecurity, supply chain'. UNCERTAIN because the figure asserts a life cycle but draws no flow between its stages."
ai_evidence_quote: "vendor management lifecycle stages"
artefacts:
  screenshot: 008_543X_Vendormanagement.png
  assets: [008_543X_Vendormanagement.png]
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

`https://developer.ibm.com/articles/navigating-governance-risk-compliance/` (api, ledger row n=543), figure `figs/543X_Vendormanagement`.

## What the figure shows



## Why the row is UNCERTAIN

png, the page's own Vendormanagement.png fetched and viewed at full size (contact sheet SHEET_PROC101, row 2 col 3). a panel headed 'Vendor management lifecycle' holding four numbered entries with their sub-bullets: 'Identify vendors and third-party suppliers' (Accurate list, Onboarding or existing customer, nth-party risk), 'Classify vendors' (Critical vendors, PII data shared, critical engagements), 'Assess vendor compliance' (Regular assessment based on tier/classification, Ad-hoc assessment (event based)), 'Mitigate, monitor, and report' (Ongoing risk management, KPIs, reporting). The page's own alt text calls the figure 'vendor management lifecycle stages' and the entries are ordered activities - but the figure draws no connectors between them at all. Hesitation resolves to UNCERTAIN.

## AI evidence (why this is not an E2 exclusion)

the page's AI content is about governing AI third parties rather than an AI element inside the figure: the life-cycle stages it lists (identify vendors, classify them, assess compliance, mitigate and report) are drawn for a risk-and-governance audience and the page says verbatim "Corporate landscapes encompass a diverse array of industries including energy, manufacturing, cybersecurity, supply chain". UNCERTAIN because the figure asserts a life cycle but draws no flow between its stages.

## Notes for the researcher

- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
