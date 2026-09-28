---
n: 7
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Compliance Monitoring Agent
url: https://marketplace.camunda.com/apps/519670/compliance-monitoring-agent
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: The listing publishes only the vendor logo and no diagram; its only artefact is the 'Watch Demo' video (https://youtu.be/_9wxND807oI), which I did not open per the operator instruction of 2026-09-26. Does the video show the compliance-monitoring process as BPMN?
needs_visual_check: true
bpmn_evidence: No BPMN artefact on the page, and none downloadable. The only content image is the captured vendor logo ('BP-3'); there are no screenshots. Any process model would be inside the unopened demo video.
bpmn_evidence_quote: "Enhanced compliance, automated oversight"
ai_evidence: The AI claims are prose, not process elements: the tags 'Agentic AI orchestration' and 'AI Services', 'Instantly review every recorded event with AI, eliminating manual effort', 'Identify policy violations immediately with AI, replacing subjective human judgment with objective assessments', and 'Traceable AI reasoning ... Provides reliable compliance trails with explainable logic'. No published artefact shows an AI element in a process.
ai_evidence_quote: "Identify policy violations immediately with AI, replacing subjective human judgment with objective assessments"
artefacts:
  screenshot: 007_compliance-monitoring-agent.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 230
capture_method: curl of the listing's own overview asset (d3bql97l1ytoxn.cloudfront.net, overview/img556936864200150311.png, 230x147) - the listing's only content image; native read in full
---

## What the page shows

A BP-3 listing ('Listing Only', partner) for AI-driven compliance monitoring of recorded events in regulated industries: contextual analysis, policy-violation detection, role validation on sensitive data, and audit trails with explainable AI reasoning. The page publishes no model, only the vendor logo and the demo video.

## Observations (description only, no interpretation)

- **AI activity - function:** prose only - monitoring and analysis of every recorded event, policy detection, role validation.
- **AI activity - element type:** not visible - no process is published.
- **Authority - downstream / data / control:** not visible.
- **Input provenance:** 'every recorded event' in a highly regulated environment; not shown in a model.
- **Guards present:** claimed as 'traceable AI reasoning', 'explainable logic' and 'audit readiness'; no element is shown.
- **Prompt / model detail visible:** none.

## Notes for the researcher

Superseded the earlier E0-no-artefact row after the operator's video instruction. Capture is the listing's only content image (BP-3 logo); the substantive artefact, if any, is inside https://youtu.be/_9wxND807oI.
