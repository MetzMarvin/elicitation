---
n: 3
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Agentic Trade Exception Management
url: https://marketplace.camunda.com/apps/519051/agentic-trade-exception-management
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: The listing publishes one stock photograph and no diagram; its only artefact is the 'Watch Demo' video (https://youtu.be/DCMSC4gKaEY), which I did not open per the operator instruction of 2026-09-26. Does the video show a BPMN diagram for the agentic trade exception process?
needs_visual_check: true
bpmn_evidence: No BPMN artefact on the page, and none downloadable. The only content image is the captured stock photograph (a woman presenting in front of a dashboard); there are no screenshots. Any process model would be inside the unopened demo video.
bpmn_evidence_quote: "Streamline and automate trade exception handling"
ai_evidence: The AI claims are prose, not process elements: the catalogue tags 'Agentic AI orchestration' and 'Agentic Solutions', the feature 'End-to-end agentic orchestration drives faster settlements and lowers compliance risk', and 'A model-agnostic framework allows for plug-and-play upgrades to the model'. No published artefact shows an AI element in a process.
ai_evidence_quote: "End-to-end agentic orchestration drives faster settlements and lowers compliance risk"
artefacts:
  screenshot: 003_agentic-trade-exception-management.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1100
capture_method: curl of the listing's own overview asset (d3bql97l1ytoxn.cloudfront.net, overview/img17892371007765914427-2x.png, 1100x472) - the listing's only content image; native read in full
---

## What the page shows

An EY listing ('Listing Only') for agentic trade-exception management: remediating pre- and post-trade errors and handling exceptions across the trade lifecycle on Camunda. The page's claims are quantitative (up to 100% fewer human errors, 45% lower exception handling time) and the only published media are the stock photograph and the demo video.

## Observations (description only, no interpretation)

- **AI activity - function:** prose only ('agentic orchestration', 'model-agnostic framework').
- **AI activity - element type:** not visible - no process is published.
- **Authority - downstream / data / control:** not visible.
- **Input provenance:** described as pre- and post-trade errors; not shown in a model.
- **Guards present:** 'regulatory compliance' is claimed; no control element is shown.
- **Prompt / model detail visible:** none; only that the framework is model-agnostic.

## Notes for the researcher

Superseded the earlier E0-no-artefact row after the operator's video instruction. Capture is the listing's only content image (stock photograph); the substantive artefact, if any, is inside https://youtu.be/DCMSC4gKaEY.
