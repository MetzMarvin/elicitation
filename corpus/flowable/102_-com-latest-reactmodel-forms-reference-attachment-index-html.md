---
n: 507
source: flowable
source_name: Flowable (enterprise documentation, vendor blog/marketing site, training site)
title: Attachment | Flowable Enterprise Documentation
url: https://documentation.flowable.com/latest/reactmodel/forms/reference/attachment/index.html
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "How should a form-level AI binding be recorded when the page publishes no process diagram at all? The Attachment reference page documents an AI agent bound to the form component ('uploaded documents are analysed by a document-analysis agent', with a 'Document agent' reference property), but all 11 of its figures are UI screenshots and no BPMN process diagram is published. (a) Does an AI-agent binding on a form used by process tasks count as an AI element inside the process for the corpus, even with no process diagram to show it; and (b) is the pair of side-by-side diagrams visible only as a roughly 120x30 px thumbnail on page 2 of the embedded 'Case Management Overview' one-pager inside the document-viewer screenshot a BPMN/CMMN example that should be read from the one-pager's full-resolution original?"
needs_visual_check: true
bpmn_evidence: sighted confirmation 2026-09-25 (shard s3) — the page publishes NO BPMN 2.0 diagram. All 11 figures were looked at; they are UI screenshots of the form designer (Attachment component plus its properties panel and a form preview), Microsoft SharePoint file pickers, a SharePoint permission page, a document list with a context menu, and a SharePoint document viewer. No pool, lane, gateway, event or task shape appears anywhere. The earlier bpmn_evidence line here rested on a figure file name and alt text, which are not evidence on this source.
bpmn_evidence_quote: "Use prefixes to define the scope of the value, for example, 'root.' for referencing the root case/process to store the value in."
ai_evidence: AI is in the page TEXT, not in a figure: the properties table binds an AI agent to the form component — Document analysis (Boolean, 'When enabled, uploaded documents are analysed by a document-analysis agent so the extracted values can be mapped to form variables'), Document agent (Reference, 'The document agent to be used for the document analysis'), and Map response to form fields (DocumentAnalysisMapping, 'Add each content model the agent may match and map its fields to form values'). The earlier ai_evidence line here (OCR labels of a SharePoint screenshot) was the known OCR false positive and is superseded.
ai_evidence_quote: "uploaded documents are analysed by a document-analysis agent so the extracted values can be mapped to form variables"
artefacts:
  screenshot: 102_-com-latest-reactmodel-forms-reference-attachment-index-html.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1920
capture_method: urllib download of https://documentation.flowable.com/latest/assets/images/using_sharepoint_integration_8-896b62fc2c45f5869ffcce21ca004131.png (asset published by the page); labels inside read with RapidOCR, this session cannot receive image content
---

## Why this row is UNCERTAIN

The sighted pass (shard s3) settles the notation question — no BPMN 2.0 diagram is
published on this page — but leaves two things that need a human ruling, both recorded in
the frontmatter `question`: whether a form-level AI-agent binding counts as an AI element
inside the process when no process diagram exists to show it, and whether the marketing
one-pager illustration that is only legible as a thumbnail inside one screenshot is a
BPMN/CMMN example. Per CLAUDE.md section 5 an unresolved figure is UNCERTAIN with
needs_visual_check, never an exclusion.

## Observations (description only, no interpretation)

- **Figures on the page:** Sharepoint Files | using_sharepoint_integration_8-896b62fc2c45f5869ff
- **OCR labels of the captured figure:** CaseManagement_Overview.docx | Download file | Open in sharepoint | Back to list | PDF | 100% | Document details | Name | ZFlowable | CaseManagement_Overview.docx | making process personal | Owner | Case Management Overview | 0 AlexW@ysfrc.onmicrosoft.com | Size | Case Management can be leveraged to manage complex business activities that require a mix of human and digital actions,
- **Page text quote:** Use prefixes to define the scope of the value, for example, 'root.' for referencing the root case/process to store the value in.
- **Captured asset:** https://documentation.flowable.com/latest/assets/images/using_sharepoint_integration_8-896b62fc2c45f5869ffcce21ca004131.png (1920x705)

## Sighted check (shard s3, 2026-09-25) — all 11 figures looked at

- **Is it BPMN 2.0?** No. Nothing on the page is a process diagram. The two largest
  figures were read at native resolution: `modelling-items-source` (1645x643) is the
  Flowable form designer, showing the *Attachment - Attachment* component ("Update file
  URL", "Delete URL", "Allow file deletions: New only", "Preview type: None", "Max. files
  reached text", "File source: Local") next to a form preview of Name / Surname / Address /
  Zipcode / City / Documents; `using_sharepoint_integration_8` (1920x705) is a Microsoft
  SharePoint document viewer for `CaseManagement_Overview.docx`. The remaining nine are the
  same kind of UI screenshot: a SharePoint "You need permission to access this site." page,
  the *Create case or process* form with an attachment field, four Microsoft SharePoint
  file-picker dialogs, the filled form with two attached documents, a document list with the
  *Rename / Add content type / Open in sharepoint / Download file / Move or Copy / Delete
  file* context menu, and a browser window showing `flowable.png`.
- **Where the AI sits.** Not in any figure — in the page's properties table, which binds an
  AI agent to the form component: *Document analysis* ("uploaded documents are analysed by a
  document-analysis agent"), *Document agent* (Reference), and *Map response to form fields*
  (DocumentAnalysisMapping). A form-level AI binding, with no process diagram on the page to
  place it in.
- **Unresolved.** Page 2 of the *Case Management Overview* one-pager embedded in the
  document-viewer screenshot carries a pair of side-by-side box-and-arrow panels, about
  120x30 px inside the 1920x705 capture (intrinsic to the source image, not a fetch
  problem). It could not be read at native resolution and may be a BPMN/CMMN comparison
  illustration. Both open points are recorded as the question in the frontmatter.

## What to check (original, superseded)

Whether the captured figure (or another figure on the page) is a BPMN 2.0 process
diagram and whether an AI/LLM element sits inside that process.
