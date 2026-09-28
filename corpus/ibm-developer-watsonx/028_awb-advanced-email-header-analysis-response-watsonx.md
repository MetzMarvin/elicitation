---
n: 1228
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Analyze and respond to email headers with watsonx Orchestrate and watsonx.ai - the 'Workflow diagram' figure (header checks, an AI summarization step and three triage decisions)"
url: https://developer.ibm.com/articles/awb-advanced-email-header-analysis-response-watsonx/
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "The page's only figure (its alt text is 'Workflow diagram') is drawn as a process: a 'Validate user in IAM' actor feeding the activity box 'Upload & Parse Email Header', then a dashed container labelled 'watsonx.orchestrate' holding the check boxes ('Sender IP Address Blacklist Check', 'Sender Email Domain Reputation Check', 'SPF/DKIM/DMARC Check', 'Sender Email Domain Creation Date Check', 'Sender Email Domain Category', 'Subject Analysis', 'Check IP Exist in ReferenceSet'), then the AI step 'Summarize findings using watsonx.ai', then three decision questions in plain boxes ('Is email Legitimate?', 'Is email SPAM?', 'Is email Malicious?') fanning out by arrows to the outcome notes ('Notify the User the mail as legitimate / Update the case for the corresponding email in UI as legitimate', 'Move the mail to Spam mailbox - Analyse the behaviour of similar mails', 'Actions to be taken:- Case creation in analyst UI - Quarantine the email'). In BPMN a dashed rounded container is how an expanded sub-process is drawn, but the decisions are plain boxes rather than gateway diamonds. Is it a BPMN 2.0 model drawn in the vendor's house style (so it belongs in the corpus), or a slide-style workflow illustration that E1-not-bpmn excludes?"
needs_visual_check: false
bpmn_evidence: "png (tiled on SHEET_SWEEP1106, row 1 col 3; viewed full size on SHEET_ZS1301). the page's only figure. It was fetched from its native asset URL and viewed at 1200x820 on SHEET_ZS1301; the labels above were read off it at that size."
bpmn_evidence_quote: "Workflow diagram"
ai_evidence: "AI elements are inside the drawn figure: one of its stages is named 'Summarize findings using watsonx.ai', and the container the checks sit in is labelled 'watsonx.orchestrate'. The page's premise is verbatim 'Email remains a primary vector for various cyberthreats, including phishing, spoofing, and spam.' That is why the row is UNCERTAIN rather than excluded: the AI step is a stage of the drawn process, but the notation is a slide-style workflow diagram whose decisions are plain boxes rather than BPMN gateway diamonds."
ai_evidence_quote: "Workflow diagram"
artefacts:
  screenshot: 028_1228X_Screenshot_202024-10-28_20at_2011-31-45_E2_80_AFAM.png
  assets: [028_1228X_Screenshot_202024-10-28_20at_2011-31-45_E2_80_AFAM.png]
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

`https://developer.ibm.com/articles/awb-advanced-email-header-analysis-response-watsonx/` (api, ledger row n=1228), figure `figs/1228X_Screenshot_202024-10-28_20at_2011-31-45_E2_80_AFAM`.

## What the figure shows



## Why the row is UNCERTAIN

png (tiled on SHEET_SWEEP1106, row 1 col 3; viewed full size on SHEET_ZS1301). the page's only figure. It was fetched from its native asset URL and viewed at 1200x820 on SHEET_ZS1301; the labels above were read off it at that size.

## AI evidence (why this is not an E2 exclusion)

AI elements are inside the drawn figure: one of its stages is named 'Summarize findings using watsonx.ai', and the container the checks sit in is labelled 'watsonx.orchestrate'. The page's premise is verbatim "Email remains a primary vector for various cyberthreats, including phishing, spoofing, and spam." That is why the row is UNCERTAIN rather than excluded: the AI step is a stage of the drawn process, but the notation is a slide-style workflow diagram whose decisions are plain boxes rather than BPMN gateway diamonds.

## Notes for the researcher

- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
