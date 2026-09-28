---
n: 27
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Google Cloud AI Connector
url: https://marketplace.camunda.com/apps/429506/google-cloud-ai-connector
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: Camunda Web Modeler canvas published as the listing's own screenshots (Design / Implement / Play tabs, bpmn-io palette, comments panel); no .bpmn is downloadable. Three canvases are published, each a start event -> one service task -> end event: 'Execute Prompt', 'Getting labels from an image' and 'Track objects in a video'.
bpmn_evidence_quote: "Track objects in a video"
ai_evidence: The AI element is the single service task of each canvas, and its name is the connector's AI operation: 'Execute Prompt' for the page's 'Prompt Functionality', 'Getting labels from an image' for image labeling, and 'Track objects in a video' for video object tracking. Each task carries an element-template avatar at its top-left (the connector's own icon, not Camunda's AI-agent star) and each canvas carries a text annotation naming the operation ('prompt', 'Image', 'video'). The page's overview image is a logo board (Acheron, Google Cloud, vertex.ai, Process Accelerator), not a diagram.
ai_evidence_quote: "The Google Cloud AI Connector combines Vertex AI with a cutting-edge generative AI model."
artefacts:
  screenshot: 027_google-cloud-ai-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own screenshot (d3bql97l1ytoxn.cloudfront.net, screenshot/img6629776316101586683.png, 1500x686); native read at full size, plus an 8x crop of the task's element-template glyph
---

## What the page shows

Acheron's Google Cloud AI connector listing: the page describes a connector that 'combines Vertex AI with a cutting-edge generative AI model' and offers pre-trained models for image labeling and video object tracking, custom-model batch predictions, generative-AI prompt functionality and batch-job status monitoring. The published artefacts are three Web Modeler canvases, each one a minimal process: start event -> the connector's task -> end event.

## Observations (description only, no interpretation)

- **AI activity - function:** one AI operation per process - execute a prompt, get labels from an image, track objects in a video.
- **AI activity - element type:** a single ordinary `serviceTask` per process, carrying the connector's element-template avatar (no AI-agent/ad-hoc sub-process is used here).
- **Authority - downstream:** the task's output is the process's only result; nothing consumes or checks it in the published canvases.
- **Authority - data:** not visible; no properties panel is published for these canvases.
- **Authority - control:** none - no gateway, no human task, no error path in any of the three canvases.
- **Input provenance:** not shown; the task is the process's first activity after the start event.
- **Guards present:** none in the models; the page's 'Job Status Monitoring' feature describes alerts on batch-prediction job status.
- **Prompt / model detail visible:** the page names Vertex AI and a generative AI model, and 'pre-trained models'; no prompt text, model id or confidence threshold is visible in the artefacts.

## Notes for the researcher

The listing's resources are a 'View Screenshots' tab and the connector's GitHub README (github.com/Acheron-Camunda/gcp-ai-connector). Each canvas is published twice (1500px and 750px, plus a 1100x619 logo board as the overview); the capture here is the 'Execute Prompt' canvas at full size. The element-template avatar on the task is an unresolvable 20px icon - the AI identification rests on the task names matching the page's AI feature list, not on that glyph.
