---
n: 320
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: "Xebia - Email Sentiment Analysis"
url: https://marketplace.uipath.com/listings/feedback-workflow-system
accessed: 2026-09-28
verdict: UNCERTAIN
needs_human_ruling: true
question: "Informal coloured-box flow sketch (no BPMN shapes, events or gateways) in which a 'Machine Learning Model' (sentiment result + probability) drives the branch to 'Thank You Mail' or 'Feedback Mail'. Does it count as a BPMN diagram?"
needs_visual_check: false
bpmn_evidence: single listing image: box-and-arrow flow feedback@company.com -> Email Automation -> Email Body Extraction -> Machine Learning Model (Sentiment Analysis Result, Probability) -> Processing of Result -> Thank You Mail / Feedback Mail; Analysis of All Email; rounded boxes, no BPMN shapes
bpmn_evidence_quote: "Reads Email from Outlook Copies the Data from the Email Body as a string to the Python Library (Machine Learning Model)."
ai_evidence: box 'Machine Learning Model' with 'Sentiment Analysis Result' and 'Probability'; prose: model returns True/False (positive/negative) and the bot acts on it
ai_evidence_quote: "Machine Learning Model gives the solution in the form of True and False (Whether the mail is positive or negative in nature.)"
artefacts:
  screenshot: 025_xebia-email-sentiment-analysis.png
  archive: 025_xebia-email-sentiment-analysis.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1280
capture_method: python urllib GET of the original marketplace-cdn.uipath.com asset (cdn-cgi resize wrapper stripped); 1280 px is the native size
---

## What the page shows

A Xebia solution for sentiment analysis of feedback emails. The listing image (under the heading 'Solution') shows: 'feedback@company.com' -> 'Email Automation (Bot read Email form client)' -> 'Email Body Extraction' -> a yellow frame 'Machine Learning Model' containing 'Sentiment Analysis Result' and 'Probability'; 'Sentiment Analysis Result' -> 'Processing of Result', which splits to 'Thank You Mail' and 'Feedback Mail'; 'Probability' -> 'Analysis of All Email'. Prose: a positive result triggers a thank-you mail; a negative one an apology mail plus escalation to the assigned authority. The page also embeds 1 YouTube video(s), not opened (operator no-media rule 2026-09-26).

## Observations (description only, no interpretation)

- **AI activity - function:** sentiment classification of the email body ("positive or negative in nature")
- **AI activity - element type:** a labelled box 'Machine Learning Model' in an informal flow
- **Authority - downstream:** 'Thank You Mail' / 'Feedback Mail' to the customer; per prose, negative case also highlighted "to the assigned authority"
- **Authority - data:** 'Analysis of All Email' fed by 'Probability'
- **Authority - control:** 'Processing of Result' branches on the model's sentiment result
- **Input provenance:** email body extracted by the bot from 'feedback@company.com'
- **Guards present:** none visible in the diagram; prose: negative case is highlighted to the assigned authority
- **Prompt / model detail visible:** none

## Notes for the researcher

Native asset fully legible. The page also embeds one YouTube video, left unplayed and unfetched (operator no-media rule).
