---
n: 166
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: The Taktile Financial Spreading Agent
url: https://marketplace.camunda.com/apps/808449/the-taktile-financial-spreading-agent
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: The page describes an AI element in the strongest terms - an 'AI-native' agent that 'uses frontier reasoning models' to turn loan documents into decision-ready financial models 'with human-in-the-loop oversight' - but the listing publishes no BPMN artefact at all (its screenshots list is empty; its only image is a 230x62 vendor thumbnail) and it is tagged 'Listing Only'. Its single demonstration resource is a video, which was not opened. Is a described-but-unpublished AI agent enough to record this listing, or is it E0-no-artefact? Same question as the Ollama connector (n=058) and the GCP Document AI connector (n=116).
needs_visual_check: true
bpmn_evidence: No BPMN artefact published: the listing's screenshots list is empty, it carries no .bpmn link, and its single image is a 230x62 vendor thumbnail. The listing is tagged 'Listing Only'. Its one demonstration resource is a YouTube link ('Watch Demo'), which was not opened under the operator instruction of 2026-09-26.
bpmn_evidence_quote: "Listing Only"
ai_evidence: The AI element is described in the strongest terms and never published: 'The Taktile Financial Spreading Agent is an AI-native solution designed to automate one of the most complex and manual tasks in commercial lending', and 'Unlike traditional OCR, this agent uses frontier reasoning models to handle complex financial nuances', with 'human-in-the-loop oversight' and '100% Traceability'. The page also carries the marketplace's 'Agentic AI orchestration', 'AI Services' and 'Agentic Solutions' attribute tags. Nothing is published to inspect: no diagram, no canvas, no element template.
ai_evidence_quote: "Unlike traditional OCR, this agent uses frontier reasoning models to handle complex financial nuances"
artefacts:
  screenshot: 166_the-taktile-financial-spreading-agent.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's only image (d3bql97l1ytoxn.cloudfront.net, app_resources/808449/thumbs_112/img8773377233667130761-2x.png, 230x62); native read at full size. The screenshots list is empty, so the vendor thumbnail is the only capturable image
---

## What the page shows

The Taktile Financial Spreading Agent (Taktile, partner solution accelerator). The listing describes an AI agent that converts unstructured lending documents into standardised financial models, with accuracy and traceability claims but no published process artefact.

## Observations (description only, no interpretation)

- **AI activity - function:** financial spreading - extraction and standardisation of lending documents by an agent using reasoning models.
- **AI activity - element type:** none published; the listing names 'agent configurations' and 'frontier reasoning models' but shows no BPMN element, template or canvas.
- **Authority - downstream:** not shown - the page claims 'human-in-the-loop oversight' and that 'every extracted value is linked back to the source document'.
- **Authority - data:** not shown; the page claims period harmonisation and LTM/YTD calculation as agent capabilities.
- **Authority - control:** not shown.
- **Authority - control (human):** claimed in prose ('built to operate with human-in-the-loop oversight'), not shown in any artefact.
- **Input provenance:** lending documents (tax filings, audited statements, PDFs, scans); no process wiring is published.
- **Guards present:** none visible.
- **Prompt / model detail visible:** none - the page names 'frontier reasoning models' generically and 'specialized agent configurations', with no model, provider or prompt.

## Notes for the researcher

Video-only listing: the demonstration is a YouTube link, which is not opened under the operator instruction of 2026-09-26 ('artefact inside a video; not opened per operator instruction 2026-09-26'), so the listing was judged only on what it publishes itself. That leaves a described-but-unpublished AI agent, i.e. the n=116/n=058 pattern, plus one unresolvable place where the artefact might live. Recorded UNCERTAIN with needs_visual_check for that reason.
