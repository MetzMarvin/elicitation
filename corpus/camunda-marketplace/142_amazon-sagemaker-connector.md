---
n: 142
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Amazon SageMaker Connector
url: https://marketplace.camunda.com/apps/441206/amazon-sagemaker-connector
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: The listing's canvas shows two unlabelled service tasks carrying the same element-template glyph, with no end event and no legible labels, while the page describes Amazon SageMaker as an ML service. Is a model with two unreadable SageMaker-bound tasks enough to count as an AI element inside a process, or does the artefact need a legible AI task and a complete flow? The capture is in the corpus for the visual ruling.
needs_visual_check: true
bpmn_evidence: BPMN diagram published as the listing's own asset (Camunda Web Modeler, palette visible at the left edge); no .bpmn downloadable. Read natively: a start event followed by two service tasks carrying the same element-template glyph, connected in sequence; the tasks' labels are not legible in the published image, no end event is visible, and the listing has no second screenshot.
bpmn_evidence_quote: "orchestrate processes that use Amazon SageMaker"
ai_evidence: The page names the AI service the connector calls - 'This outbound Connector enables teams to orchestrate processes that use Amazon SageMaker, a fully managed machine learning (ML) service from AWS' - and the two tasks in the published canvas carry the connector's element-template glyph, but the implementation of neither task is readable: the labels are illegible at the published resolution and the page's feature list describes SageMaker's capabilities (automatic model tuning, frameworks) rather than the diagram.
ai_evidence_quote: "This outbound Connector enables teams to orchestrate processes that use Amazon SageMaker, a fully managed machine learning (ML) service from AWS"
artefacts:
  screenshot: 142_amazon-sagemaker-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: marginal
capture_width_px: null
capture_method: curl of the listing's own asset (d3bql97l1ytoxn.cloudfront.net, app_resources/441206/overview/img4548612040220063346-2x.png, 788x445); native read at full size - a Camunda Web Modeler canvas whose tasks are unlabelled at this zoom and whose palette is visible at the left
---

## What the page shows

The Amazon SageMaker Connector (Camunda Services GmbH, outbound connector). The listing publishes one Web Modeler canvas showing how the connector is placed in a process - a start event and two connector tasks in sequence - plus the page's description of SageMaker as a managed ML service.

## Observations (description only, no interpretation)

- **AI activity - function:** not readable - the tasks' labels are illegible in the published image; the page's features concern model training (hyperparameter optimization, framework choice).
- **AI activity - element type:** two `serviceTask`s carrying the connector's element-template glyph; no agent element and no ad-hoc container.
- **Authority - downstream:** none visible - the canvas shows no end event and no branch after the second task.
- **Authority - data:** none drawn.
- **Authority - control:** none drawn - no gateway in the published canvas.
- **Authority - control (human):** none drawn.
- **Input provenance:** not readable from the canvas.
- **Guards present:** none drawn.
- **Prompt / model detail visible:** none - the listing names no model, endpoint or prompt.

## Notes for the researcher

UNCERTAIN rather than E2 because the canvas does show connector-bound tasks inside a BPMN process and the page does call SageMaker an ML service; it is not a clean E2. But this is also the weakest artefact in the batch: two unlabelled tasks, no end event, no readable activity, and the only capture is the low-resolution overview asset - the listing publishes no second screenshot, so there is nothing better to look at.
