---
n: 176
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Smarter Letters of Credit
url: https://marketplace.camunda.com/apps/634342/smarter-letters-of-credit
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: The page describes autonomous AI agents operating inside the process - handling 'document parsing, compliance checks and exception handling, while working seamlessly with human reviewers and backend systems' - and applies DMN tables for trade compliance, but the listing publishes no BPMN artefact at all: no screenshots, no .bpmn link, and its only published images are a partnership banner and the HCLTech wordmark. Is a described-but-unpublished agentic process enough to record this listing, or is it E0-no-artefact? Same question as the Ollama connector (n=058), the GCP Document AI connector (n=116) and the Taktile agent (n=166).
needs_visual_check: false
bpmn_evidence: No BPMN artefact published: the listing's only images are a marketing banner ('HCLTech and Camunda Partnership') and the partner's wordmark, its screenshots list is empty, and it carries no .bpmn link. The listing is tagged 'Listing Only'.
bpmn_evidence_quote: "Listing Only"
ai_evidence: The AI element is described - inside the process, in the page's own words - and never shown: 'Agentic orchestration - Executes autonomous AI agents to handle document parsing, compliance checks and exception handling, while working seamlessly with human reviewers and backend systems', alongside 'Smart document processing' and a compliance feature that applies trade standards 'using decision model and notation tables (DMN)'. The page is tagged 'Agentic AI orchestration' and 'AI Services'. Nothing is published to inspect.
ai_evidence_quote: "Executes autonomous AI agents to handle document parsing, compliance checks and exception handling"
artefacts:
  screenshot: 176_smarter-letters-of-credit.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own asset (d3bql97l1ytoxn.cloudfront.net, app_resources/634342/overview/img6683210170475611657-2x.png, 1100x376 - a partner banner) and of its only other image (thumbs_112/img3644826144661512103-2x.png, 230x69 - the HCLTech wordmark); both read natively at full size
---

## What the page shows

HCLTech's Smarter Letters of Credit (partner solution accelerator, tagged 'Listing Only'). The listing describes agentic orchestration of trade-finance compliance and document processing but publishes only marketing imagery.

## Observations (description only, no interpretation)

- **AI activity - function:** document parsing, compliance checks and exception handling by 'autonomous AI agents', per the page's feature text.
- **AI activity - element type:** none published - no BPMN element, canvas, template or diagram appears anywhere on the listing.
- **Authority - downstream:** not shown.
- **Authority - data:** not shown; the page mentions trade documents and DMN-based compliance rules.
- **Authority - control:** not shown.
- **Authority - control (human):** claimed in prose - the agents work 'seamlessly with human reviewers'; no artefact shows where.
- **Input provenance:** trade documents (letters of credit); no wiring is published.
- **Guards present:** none visible.
- **Prompt / model detail visible:** none - no model, provider or prompt is named.

## Notes for the researcher

One of the AI-heavy 'Listing Only' partner entries in this source: strong AI vocabulary in the benefit text, nothing published but a banner. Recorded UNCERTAIN rather than E0 because the page places the AI agents inside the process in its own words, which is the same reasoning used for n=116 and n=058.
