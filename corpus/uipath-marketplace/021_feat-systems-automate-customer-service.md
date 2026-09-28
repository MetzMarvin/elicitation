---
n: 1870
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: "Automate Customer Service"
url: https://marketplace.uipath.com/listings/automate-customer-service
accessed: 2026-09-28
verdict: UNCERTAIN
needs_human_ruling: true
question: "The listing names 'BPMN.IO' among its technologies and promises 'Configurable process and decision points' with ML query classification, but shows no process diagram (only marketing slides). Is an unpublished BPMN model behind the product in scope, or is this an exclusion (no artefact)?"
needs_visual_check: false
bpmn_evidence: no diagram in the five listing images (marketing slides); the page lists 'BPMN.IO' among technologies; slide text 'Configurable process and decision points'
bpmn_evidence_quote: "BPMN.IO"
ai_evidence: slides 'AI / Machine Learning - Classification: Trained ML model for 70 different query types and achieved 60-70% accuracy' and 'Text Analytics: Sentiment analysis to calculate emotions'; page prose on Communications Mining and intent/sentiment analysis
ai_evidence_quote: "function and make it future-ready. Additional Information Dependencies UiPath Communication Mining for classifying incoming communications like email, social media, etc. concerning intent and sentiment"
artefacts:
  screenshot: 021_feat-systems-automate-customer-service.png
  archive: 021_feat-systems-automate-customer-service.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1682
capture_method: python urllib GET of the original marketplace-cdn.uipath.com asset (cdn-cgi resize wrapper stripped); 1682 px is the native size
---

## What the page shows

A partner solution by Feat Systems Inc. for automating customer service query handling. The five images are marketing slides: 'Blue Sky Thinking' (New Support Channels, AI / Machine Learning 'Query identification and prioritization', Process Optimization, Automation around 'Improved Customer Satisfaction'), 'AI / Machine Learning' (captured here), 'Automation', 'Process Optimization' ('Configurable process and decision points', 'Minimize human interventions', 'Query classification, prioritization, assignment', 'Reclassification and hand offs') and 'New Support Channels' (Web Form, Chatbot). The listing text names 'BPMN.IO' next to Java, JavaScript and Node.js.

## Observations (description only, no interpretation)

- **AI activity - function:** 'Trained ML model for 70 different query types and achieved 60-70% accuracy'; 'Sentiment analysis to calculate emotions'; 'Query identification and prioritization'
- **AI activity - element type:** not visible on the page (no diagram)
- **Authority - downstream:** 'Query classification, prioritization, assignment'; 'Reclassification and hand offs' (slide text)
- **Authority - data:** not visible on the page
- **Authority - control:** 'Configurable process and decision points' (slide text)
- **Input provenance:** customer queries via 'Chatbot and web form for the self service' and incoming communications
- **Guards present:** not visible on the page
- **Prompt / model detail visible:** none

## Notes for the researcher

The BPMN evidence is a technology name only; no model is published on the listing. Recorded as UNCERTAIN because the page ties ML classification to configurable process decision points in a BPMN.IO-based product.
