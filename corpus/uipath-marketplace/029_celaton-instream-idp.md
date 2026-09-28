---
n: 470
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: "inSTREAM™ - Intelligent Document Processing"
url: https://marketplace.uipath.com/listings/celaton-instream
accessed: 2026-09-28
verdict: UNCERTAIN
needs_human_ruling: true
question: "Informal hexagon-and-arrow process sketch (no BPMN shapes, events or gateways) with an AI step 'Understand Meaning Intent & Document Type' and a 'Human in the Loop' arc when confidence is low. Does it count as a BPMN diagram?"
needs_visual_check: false
bpmn_evidence: single listing image: marketing process sketch Inbound Documents Received -> Prepare Documents -> Understand Meaning Intent & Document Type -> Extract Data -> Validate, Verify & Enrich -> Deliver to Line of Business System / Action Triggered, with 'Human in the Loop' arc and RPA Bots icons; no BPMN shapes
bpmn_evidence_quote: "Intelligent automatic data recognition, classification, extraction, validation and enrichment"
ai_evidence: step 'Understand Meaning Intent & Document Type' (brain icon); 'Human in the Loop' caption: low-confidence exceptions referred to operators, platform learns from their decisions; prose on Machine Learning capabilities
ai_evidence_quote: "Celaton’s inSTREAM™ platform complements UiPath robots with Machine Learning capabilities"
artefacts:
  screenshot: 029_celaton-instream-idp.png
  archive: 029_celaton-instream-idp.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1655
capture_method: python urllib GET of the original marketplace-cdn.uipath.com asset (cdn-cgi resize wrapper stripped); 1655 px is the native size
---

## What the page shows

A Celaton partner solution (inSTREAM) for intelligent document processing. The listing image shows a left-to-right flow of hexagons: 'Inbound Documents Received' (document/email icons) -> 'Prepare Documents' -> 'Understand Meaning Intent & Document Type' (brain icon) -> 'Extract Data' -> 'Validate, Verify & Enrich' -> branches to 'Deliver to Line of Business System' and 'Action Triggered - Including data exports, delivery, payment and email responses'. An arc above spans from 'Understand Meaning' to 'Validate' labelled 'Human in the Loop - When confidence is low, inSTREAM refers exceptions to operators in an easy to use GUI and learns from the actions and decisions they make.' 'RPA Bots' icons attach at the start, at 'Internal & External Systems' and at the delivery step; a 'Reports & Insight' caption sits bottom left. The page also embeds 1 YouTube video(s), not opened (operator no-media rule 2026-09-26).

## Observations (description only, no interpretation)

- **AI activity - function:** 'Understand Meaning Intent & Document Type', 'Extract Data' (ML recognition/classification/extraction)
- **AI activity - element type:** a labelled hexagon (brain icon) in an informal marketing flow
- **Authority - downstream:** 'Deliver to Line of Business System'; 'Action Triggered' (data exports, delivery, payment and email responses)
- **Authority - data:** extracted data delivered to line-of-business systems
- **Authority - control:** low confidence routes exceptions to operators ('Human in the Loop')
- **Input provenance:** 'Inbound Documents Received' (documents, email, attachments)
- **Guards present:** 'Human in the Loop' on low confidence; 'Validate, Verify & Enrich' step
- **Prompt / model detail visible:** none

## Notes for the researcher

Native asset legible. The page also embeds one YouTube video, left unplayed and unfetched (operator no-media rule).
