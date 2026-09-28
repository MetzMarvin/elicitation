---
n: 239
source: frends-docs
source_name: Frends documentation (docs.frends.com)
title: "Using Expressions in Frends Processes"
url: https://docs.frends.com/guides/development/using-expressions-in-frends-processes
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
needs_visual_check: false
bpmn_evidence: "BPMN 2.0 process diagram on the Frends Process Editor canvas: the AI Connector task sits in the Process flow and is fed by the steps before it."
bpmn_evidence_quote: "In order to pass in Process data to the AI Connector shape, Handlebars and C# expressions are needed."
ai_evidence: "The AI Connector is a shape inside the Process and its prompt is composed from the Process data produced by earlier tasks."
ai_evidence_quote: "In this example, the details of a Customer that we obtained from a web service are passed in to the AI for generating a summary of the customer's information."
artefacts:
  screenshot: 009_ai-connector-summary.png
  assets: [009_ai-connector-summary.png]
  bpmn_xml: []
  archive: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: "figure fetched from its native asset URL on the Frends documentation site and opened at full size on 2026-09-26"
judgment: true
---

## What the artefact is

`https://docs.frends.com/guides/development/using-expressions-in-frends-processes` (ledger row n=239), figure asset `/spaces/0p415NUmUmiF4ayjI81L/uploads/Bay4Jd8hcVKSxSHitq4L/image.png`.

## What the figure shows

Process Editor canvas with an AI Connector shape labelled "Generate Customer Summary" and its configuration panel open, showing the user prompt built from Handlebars and C# expressions over Process data. (009_ai-connector-summary.png)

## bpmn_evidence

BPMN 2.0 process diagram on the Frends Process Editor canvas: the AI Connector task sits in the Process flow and is fed by the steps before it.

## ai_evidence

The AI Connector is a shape inside the Process and its prompt is composed from the Process data produced by earlier tasks.

## Notes for the researcher

- Found late: the figure sits in the "### AI Connectors" section of an expressions guide and neither its caption nor the page title mentions AI. It was caught by looking at the figures of every page whose prose names an AI process element.
- Good example of a prompt bound to upstream process data.
- Evidence read from the markdown twin https://docs.frends.com/guides/development/using-expressions-in-frends-processes.md.
