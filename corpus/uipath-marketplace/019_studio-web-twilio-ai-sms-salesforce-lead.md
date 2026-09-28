---
n: 1733
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: "Send an SMS message via Twilio when a new Lead is created in Salesforce"
url: https://marketplace.uipath.com/listings/send-an-sms-message-via-twilio-when-a-new-lead-is-created-in-salesforce
accessed: 2026-09-28
verdict: UNCERTAIN
needs_human_ruling: true
question: "Studio Web workflow template (not a Maestro/BPMN template) not opened in Studio Web (operator ruling 2026-09-28: opening creates a tenant draft); the listing has no image. Is a Studio Web workflow in scope at all, and does its 'AI generated SMS' step count?"
needs_visual_check: true
bpmn_evidence: none on the listing (0 images, 0 video); Studio Web workflow template, not opened
bpmn_evidence_quote: "Send an AI generated SMS message via Twilio to a new Lead when it's created in Salesforce."
ai_evidence: listing prose describes an AI/ML step in the automated process
ai_evidence_quote: "Send an AI generated SMS message via Twilio to a new Lead when it's created in Salesforce."
artefacts:
  screenshot: 019_studio-web-twilio-ai-sms-salesforce-lead.png
  archive: 019_studio-web-twilio-ai-sms-salesforce-lead.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: fullpage-screenshot
capture_quality: legible
capture_width_px: 1500
capture_method: offline headless-Edge render of the archived listing HTML (scripts, styles and video iframes stripped, so no YouTube request); the listing has no image asset to download
---

## What the page shows

A Studio Web template: when a new Lead is created in Salesforce, send it an AI-generated SMS via Twilio (tags include 'openai', 'text generation'). The listing has no screenshots and no video; the template itself lives in Studio Web and was not opened (operator ruling 2026-09-28: opening creates a tenant draft).

## Observations (description only, no interpretation)

- **AI activity - function:** 'AI generated SMS message' (tags 'openai', 'text generation')
- **AI activity - element type:** not visible on the page (no diagram on the page)
- **Authority - downstream:** SMS via Twilio to the new Lead
- **Authority - data:** not visible on the page
- **Authority - control:** not visible on the page
- **Input provenance:** new Lead record created in Salesforce
- **Guards present:** not visible on the page
- **Prompt / model detail visible:** none

## Notes for the researcher

Studio Web workflow templates are UiPath low-code workflows; whether they are BPMN was not verifiable without opening the template, which the operator ruled out. The PNG is an offline render of the archived listing text.
