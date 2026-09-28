---
n: 220
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Amazon Comprehend Connector
url: https://marketplace.camunda.com/apps/477728/amazon-comprehend-connector
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: A Web Modeler canvas (Implement tab, Autosaved badge, Deploy/Run toolbar): start event 'Start' -> serviceTask 'Discover insights from documents' -> end event 'End'. A three-element process; the single task is where the artefact's content lives.
bpmn_evidence_quote: "Discover insights from documents"
ai_evidence: The task carries the violet AI element-template glyph - the published template icon (80x80) is a violet square holding a document and a lightbulb - and the connector behind it is an ML service: 'Amazon Comprehend uses machine learning (ML) and natural language processing (NLP) to process business documents and extract insights about their content', with the feature 'Gain Insights :: Quickly and accurately process and extract insights from a variety of document types'. The listing is by Camunda (open source, 8.7) and carries the 'AI Services' category.
ai_evidence_quote: "Amazon Comprehend uses machine learning (ML) and natural language processing (NLP) to process business documents and extract insights about their content."
artefacts:
  screenshot: 220_amazon-comprehend-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: listing-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own assets (d3bql97l1ytoxn.cloudfront.net, app_resources/.../overview/img2974485337038463946-2x.png, 1100x593, plus the 80x80 element-template icon img4472438420139265404-2x.png), both read natively at full size
---

## What the page shows

The Amazon Comprehend Connector (Camunda, open source, 8.7). A single task that sends a document to Amazon Comprehend and returns the insights it extracts; the published process is the minimum that shows the task in place, start to end.

## Observations (description only, no interpretation)

- **AI activity - function:** extract insights from the content of business documents (entities, key phrases, sentiment and the like - the connector's operation set is not shown in the figure).
- **AI activity - element type:** one serviceTask bound to the Comprehend element template, marked with the violet AI document/lightbulb glyph.
- **AI activity - models named:** none; the service is 'machine learning (ML) and natural language processing (NLP)' per the page's own description.
- **Authority - downstream:** nothing downstream in this figure - the extraction result is the last value before the end event, so the published process shows capability, not consequence.
- **Authority - control:** none visible; no gateway, threshold or human step in the fragment.
- **Data reachable by the model:** the document handed to the connector task; the page's description ('extract insights about their content') is the only statement about what is read.
- **Human role:** none in the published process.

## Notes for the researcher

A minimal published process whose only interesting content is the task: start -> 'Discover insights from documents' -> end. The AI signal is carried entirely by the element-template glyph plus the connector's identity as an ML service, which is why the template icon (fig2) is captured next to the canvas - the canvas alone shows no AI word. Compare the boundary case recorded at n=189 (a vendor ML platform called over plain HTTP): here the AI binding is Camunda's own published element template.
