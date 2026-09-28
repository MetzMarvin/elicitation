---
n: 87
source: flowable
source_name: Flowable (enterprise documentation, vendor blog/marketing site, training site)
title: Advanced Usage Patterns | Flowable Enterprise Documentation
url: https://documentation.flowable.com/latest/ai/ai-orchestrator-advanced/index.html
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: false
question: null
needs_visual_check: true
bpmn_evidence: not established from the page text; the page is about process/case modelling: To do so, the Trigger intent evaluation task can be used for that exact purpose.
bpmn_evidence_quote: "To do so, the Trigger intent evaluation task can be used for that exact purpose."
ai_evidence: labels inside the figure name an AI element: CasePlanModel-Al | Agent Model: | agent v4(agentV4) | Variable mapping type: | Blocked | Variable mappings tothe AlAgent: | 1configured
ai_evidence_quote: "CasePlanModel-Al | Agent Model: | agent v4(agentV4) | Variable mapping type: | Blocked | Variable mappings tothe AlAgent: | 1configured"
artefacts:
  screenshot: 019_n-flowable-com-latest-ai-ai-orchestrator-advanced-index-html.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: marginal
capture_width_px: 438
capture_method: urllib download of https://documentation.flowable.com/latest/assets/images/variable-mapping-d0bc30624552bc31c81c2f8a9ffee2b8.png (asset published by the page); labels inside read with RapidOCR, this session cannot receive image content
---

## Why this row is UNCERTAIN

The page publishes figures and mentions AI, but the figure that would decide the
verdict could not be certified from the evidence this session can read (the DOM, the
page text, and OCR labels). Per CLAUDE.md section 5 an unresolved figure is UNCERTAIN
with needs_visual_check, never an exclusion.

## Observations (description only, no interpretation)

- **Figures on the page:** Orchestrator agent variable mapping | variable-mapping-d0bc30624552bc31c81c2f8a9ffee2b8.
- **OCR labels of the captured figure:** CasePlanModel-Al | Agent Model: | agent v4(agentV4) | Variable mapping type: | Blocked | Variable mappings tothe AlAgent: | 1configured
- **Page text quote:** To do so, the Trigger intent evaluation task can be used for that exact purpose.
- **Captured asset:** https://documentation.flowable.com/latest/assets/images/variable-mapping-d0bc30624552bc31c81c2f8a9ffee2b8.png (438x249)

## What to check

Whether the captured figure (or another figure on the page) is a BPMN 2.0 process
diagram and whether an AI/LLM element sits inside that process.
