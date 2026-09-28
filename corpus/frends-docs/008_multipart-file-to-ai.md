---
n: 228
source: frends-docs
source_name: Frends documentation (docs.frends.com)
title: "How to Accept File Uploads & Multipart data to an API"
url: https://docs.frends.com/guides/development/how-to-accept-file-uploads-and-multipart-data-to-an-api
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
needs_visual_check: false
bpmn_evidence: "BPMN 2.0 process diagram on the Frends Process Editor canvas: an incoming File reference, an AI Connector task and the surrounding flow."
bpmn_evidence_quote: "The File attachment of the AI Connector can be provided as a filepath, and the task then reads the file content."
ai_evidence: "The AI Connector task performs OCR on the uploaded binary: the LLM step is inside the Process, downstream of a file-read step."
ai_evidence_quote: "Providing a written file as filepath to AI Connector."
artefacts:
  screenshot: 008_image-ocr-process.png
  assets: [008_image-ocr-process.png]
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

`https://docs.frends.com/guides/development/how-to-accept-file-uploads-and-multipart-data-to-an-api` (ledger row n=228), figure asset `/spaces/0p415NUmUmiF4ayjI81L/uploads/NTRzWdN3J88jg3XLDLdL/image.png`.

## What the figure shows

Process Editor canvas with a File/Read shape feeding a green "Perform Image OCR" AI Connector task, and the AI Connector panel showing the File attachment set to a shared filepath. (008_image-ocr-process.png)

## bpmn_evidence

BPMN 2.0 process diagram on the Frends Process Editor canvas: an incoming File reference, an AI Connector task and the surrounding flow.

## ai_evidence

The AI Connector task performs OCR on the uploaded binary: the LLM step is inside the Process, downstream of a file-read step.

## Notes for the researcher

- The same page also documents ParseMultipartRequest; the AI figure is the artefact of interest.
- Evidence read from the markdown twin https://docs.frends.com/guides/development/how-to-accept-file-uploads-and-multipart-data-to-an-api.md.
