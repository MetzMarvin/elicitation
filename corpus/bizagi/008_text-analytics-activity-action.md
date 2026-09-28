---
n: 209
source: bizagi
source_name: Bizagi (vendor documentation, help.bizagi.com)
source_type: vendor docs
title: Text Analytics Connector Example
url: https://help.bizagi.com/platform/en/text_analytics_example.htm
accessed: 2026-09-24
verdict: UNCERTAIN
needs_human_ruling: true
question: "Microsoft Text Analytics actions are bound as Activity Actions (On Enter) of a process activity; is a cloud AI service invoked at activity level in scope?"
needs_visual_check: false
bpmn_evidence: process described in prose (customer-review handling); the figures are the connector Activity actions dialog and its data mapping
bpmn_evidence_quote: "MicrosoftTextAnalytics - Detect Language"
ai_evidence: page text + the vendor figure
ai_evidence_quote: "After the area receives a new review, it's analyzed using the Text Analytics connector provided by Microsoft Cognitive Services."
artefacts:
  screenshot: 008_textanalytics05.png
  archive: 008_text_analytics_example.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: poor
capture_width_px: 902
capture_method: curl of the vendor's own .png asset at its native URL (help.bizagi.com documentation image)
---

## What the page shows

The `Text Analytics Connector Example` page, in the `Artificial Intelligence Connectors`
branch. It opens with a process description ("Suppose the following process is how
customer reviews are handled in your company's Customer Satisfaction area...") and its
figures are the connector's Activity actions dialog (`On Enter`: `MicrosoftTextAnalytics -
Detect Language`, `Set detected language`) and the input/output mapping tree.

## Observations (description only, no interpretation)

- **AI activity - function:** "After the area receives a new review, it's analyzed using
  the Text Analytics connector provided by Microsoft Cognitive Services."
- **AI activity - element type:** not a BPMN element - Activity Actions on a process
  activity: `MicrosoftTextAnalytics - Detect Language` and a following
  `Set detected language` action, configured on `On Enter`.
- **Authority - downstream:** the detected language is set into a variable
  (`Set detected language`) and then used by the following sentiment action.
- **Authority - data:** the mapping figure shows the connector outputs
  (`detectedLanguage`, `confidenceScore`, `statistics`, `errors`) feeding Bizagi data
  (`BizagiData` tree with `DetectedLanguage`, `ConfidenceScore`, `Document`, `Sentiment`).
- **Authority - control:** not visible on the page.
- **Input provenance:** a customer review text held in the case.
- **Guards present:** none observed.
- **Prompt / model detail visible:** no model or prompt; this is a pre-built cloud
  service call.

## Notes for the researcher

- The page's own `Process Model` figure was not located among its images; the two figures
  captured are the AI-binding evidence. Flagged `needs_human_ruling` because the AI is
  invoked at activity level rather than as a BPMN element.
- Capture 902 px wide, `capture_quality: poor` by rule; dialog labels are legible.
