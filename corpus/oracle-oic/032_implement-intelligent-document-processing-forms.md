---
n: 769
source: oracle-oic
source_name: OCI Process Automation documentation (docs.oracle.com/en/cloud/paas/process-automation)
source_type: vendor product documentation
title: Implement Intelligent Document Processing in Forms
url: https://docs.oracle.com/en/cloud/paas/process-automation/user-process-automation/implement-intelligent-document-processing-forms.html
accessed: 2026-09-24
verdict: UNCERTAIN
needs_human_ruling: true
question: "This docs page documents an AI element that sits INSIDE the process - the Document Understanding form control, backed by two pretrained OCI Document Understanding AI models, whose extracted text 'can be used for process routing, approvals or ... sent to a downstream system' - but it publishes no diagram of any kind (the archived HTML has zero img/figure/video elements). Does the source contribute an artefact here (prose-documented AI-in-process, capture = full-page screenshot), or does the absence of a published BPMN model mean E0-no-artefact? I did not exclude it because the AI element is inside the process rather than adjacent to it, and a wrong exclusion here is unrecoverable (shared rules 1 and 2)."
needs_visual_check: false
bpmn_evidence: "NONE - and this is the finding. The archived page HTML contains no img, figure, svg, video or iframe element at all (verified 2026-09-24 by inspecting the saved HTML and by looking at the full-page screenshot): the page is prose, definition tables and Notes only. So this page is NOT an artefact in the corpus sense; it is the prose description of an AI element that the product places inside a process. Everything known about the control on this page is textual: its fields (Name, Label, Accept only these file types, Maximum Upload Size, Help, Required, Read Only, Visible) and its behaviour."
bpmn_evidence_quote: "In the Forms palette, expand AI Services and then drag and drop a document understanding control onto the canvas"
ai_evidence: "The AI element is the Document Understanding control, placed on a form that a process activity shows. Two pretrained OCI Document Understanding AI models do the work (Document Classification classifies the uploaded document; Key Value Extraction returns values for predefined key/value pairs), and the extracted text is consumed by the process itself. The page also names the realm gate (preregistered for tenancies in the OC1 realm) and the palette path under which the control is found ('AI Services')."
ai_evidence_quote: "the extracted text can be used for process routing, approvals or can be sent to a downstream system"
artefacts:
  screenshot: 032_implement-intelligent-document-processing-forms.fullpage.png
  archive: 032_implement-intelligent-document-processing-forms.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: fullpage-screenshot
capture_quality: legible
capture_width_px: 1609
capture_method: "full-page screenshot of the live page taken in this worker's own browser tab (chrome-devtools-mcp, page 5) with the page's own full-page capture, 1609x4426; the page HTML was archived separately by the docs-surface fetcher. There is no figure to capture - the screenshot exists to document that the page publishes no diagram."
---

## What the page shows

The single AI-in-process evidence of the whole OCI Process Automation documentation surface. The page
states that "Intelligent document processing applies artificial intelligence (AI) and machine learning
techniques to capture, extract, and process structured, semi-structured, and unstructured data from a
variety of document formats", and then locates that capability precisely:

> "In Process Automation forms, intelligent document processsing is implemented with the Document
> Understanding control that uses out of the box pretrained AI models from Oracle Cloud Infrastructure
> (OCI) Document Understanding AI service to automatically detect, classify and extract texts and
> objects from uploaded documents."

Two models do the work: "The Document Classification AI model is used to classify the document uploaded
to the document understanding control" and "The Key Value Extraction AI model is used to extract values
for predefined key value pairs in the uploaded document" (the example given is a passport's nationality
and date of issue). The extracted text is then consumed by the process: "The extracted text can be used
for process routing, approvals or can be sent to a downstream system."

The page is a how-to: it lists the control's fields in a table, notes the OC1-realm gate, and starts the
configuration with "In the Forms palette, expand AI Services and then drag and drop a document
understanding control onto the canvas".

## Observations (description only, no interpretation)

- **AI activity - function:** classification and key/value extraction over uploaded documents; the
  output feeds routing, approval or a downstream system. The AI is invoked by the process, not by a
  prompt written in the process model.
- **AI activity - element type:** a form control (Document Understanding) inside the Forms palette's
  "AI Services" group. It is a *form* element, i.e. it appears where a human-task form is rendered, not
  as a BPMN task type or a gateway.
- **AI activity - model binding:** the binding is to OCI Document Understanding AI service models
  (Document Classification, Key Value Extraction), named but not versioned or configured here.
- **Authority - downstream:** the extracted text is passed to process routing, approval or a downstream
  system; the page names no review or correction step for the extracted values.
- **Authority - control:** the process holds control; the page never describes the model deciding the
  path itself.
- **Authority - data:** the uploaded document (with a configured accepted-file-type list and a maximum
  upload size, default 2 MB).
- **Guards present:** the file-type and size limits are configuration guards, not AI guards. No
  confidence threshold, no human-confirmation step and no prompt text appear on the page.
- **Input provenance:** the model is the vendor's own pretrained service, invoked in-tenant.
- **Availability:** gated - "The document understanding control is available in the Forms palette only
  if your tenancy is in the OC1 realm."

## Notes for the researcher

The corpus question this page raises is a boundary question, and I have recorded it as `UNCERTAIN`
rather than resolving it: **the AI element is documented but not drawn.** Every other docs page in this
surface publishes figures (88 of 594 pages do); this one publishes none, so the AI-in-process evidence
is prose only.

For the abstraction step, the wording is the interesting part, and it is verbatim above: the control
"uses out of the box pretrained AI models", the two models are named, and the output destination is
"process routing, approvals or ... a downstream system". That is an AI element whose result conditions
the process path, implemented as a form control inside a human task rather than as a task or gateway in
the model.

How this page was found: the docs surface (594 URLs) was enumerated from every book's own `toc.htm` and
fetched once per URL at ~1 request per second; the full text of every page was keyword-scanned for
AI/LLM terms. This page is one of five hits; the other four are keyword false positives ("prompting",
"prompts users", "user agent (browser)", "travel agent"). Its TOC entry gives no hint of the AI content,
and it is the only AI-bearing page in the docs surface that has real AI content.
