---
n: 5
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Agentic AI Assisted Quality Audit Process
url: https://marketplace.camunda.com/apps/519046/agentic-ai-assisted-quality-audit-process
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: Camunda Web Modeler canvas published as the listing's overview asset; no .bpmn downloadable. Read natively: start event, exclusive gateway ('Audit Completed?'), an ad-hoc sub-process (tilde marker), an error boundary event ('Manual Task if any ERROR'), and free-text annotations.
bpmn_evidence_quote: "Audit Completed?"
ai_evidence: Four elements carry the OpenAI connector glyph (confirmed on a 12x icon crop of each task): the service task 'Audit Agent' and, inside the ad-hoc sub-process, 'Draft Email to be sent' (twice) and 'Quality report Generation'. The two user tasks ('Manual Review', 'Manual Task if any ERROR') carry the person glyph and 'Send Notification CSR via an email.' carries the email glyph. The annotations name the AI work: 'LLM trained on historical data', 'All calls are now AI audited.', 'Audit Completed either by AI or Human'; the page's own details line reads 'AI-powered call analysis'.
ai_evidence_quote: "All calls are now AI audited."
artefacts:
  screenshot: 005_agentic-ai-quality-audit.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own overview asset (d3bql97l1ytoxn.cloudfront.net), native read at 2200x1100
---

## What the page shows

A call-quality audit process. A recorded call arrives with its transcript ('Recorded Call Data And Provide Transcript' annotation) into the service task 'Audit Agent', which is annotated 'Sentimental Analysis' and 'LLM trained on historical data'. Next 'Create List of Tasks', then an ad-hoc sub-process holding the audit work: 'Quality report Generation', 'Manual Review' (a user task / human step), another 'Draft Email to be sent', and 'Send Notification CSR via an email.'. A boundary error event drops the call to the user task 'Manual Task if any ERROR'. An exclusive gateway labelled 'Audit Completed?' closes the process.

## Observations (description only, no interpretation)

- **AI activity - function:** the page says the solution 'audits 100% of calls, faster and smarter'; the diagram annotates the AI step as 'Sentimental Analysis' and 'LLM trained on historical data', and the closing annotation says 'All calls are now AI audited.'
- **AI activity - element type:** ordinary `serviceTask`s bound to the OpenAI connector (the OpenAI glyph sits at each task's top-left), plus one `adHocSubProcess` that groups the AI drafting and the human review.
- **Authority - downstream:** inside the sub-process the AI output is consumed by a human step ('Manual Review', annotated 'Auditor verified that the required DLP followed by the CSR for the call') and by 'Send Notification CSR via an email.'; on error, by 'Manual Task if any ERROR'.
- **Authority - data:** not visible on the page (no data objects, no variable panel in the captured asset).
- **Authority - control:** the exclusive gateway 'Audit Completed?' and the error boundary event; the annotation 'Human Task get created when: 1. any issues (minor or critical) 2. call performance is <70 3. if the call sentiment' names the escalation rule.
- **Input provenance:** the recorded call and its transcript (annotation 'Recorded Call Data And Provide Transcript').
- **Guards present:** a human review step ('Manual Review'), an error path to 'Manual Task if any ERROR', and the annotation 'Consider Auditor bandwidth, categorize: know Which group to send the call to.'
- **Prompt / model detail visible:** the annotation names an LLM trained on historical data; no model name, prompt text or tool definition is visible.

## Notes for the researcher

The listing also links 'Watch Demo' (youtu.be/RKN7U9JNt4M) and a Cognizant glossary page; the diagram itself is only available as this asset image.
