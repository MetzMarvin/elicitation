---
n: 85
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: ABBYY Vantage Connector
url: https://marketplace.camunda.com/apps/676529/abbyy-vantage-connector
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: BPMN diagram published as the listing's overview asset (Camunda Web Modeler canvas with element-template glyphs); no .bpmn downloadable. Read natively: start event -> 'Upload File to ABBYY Vantage' -> 'Launch Transaction' -> 'Check Transaction Status' -> 'Download Results' -> 'Send Result Files Via Email' -> 'Send Email to Applicant' -> end event. The three middle tasks carry the collapsed-sub-process marker; the two mail tasks carry the mail element-template glyph and the first task carries ABBYY's own connector glyph.
bpmn_evidence_quote: "Upload File to ABBYY Vantage"
ai_evidence: The AI element is the process step that executes an ABBYY Vantage document-AI Skill: the page says 'The connector lets you call any ABBYY Vantage Process Skill directly from a BPMN process model' and 'ABBYY Vantage transforms unstructured documents into accurate, structured data', listing the extraction of 'fields, tables, amounts, names, dates' plus Vantage's 'built-in validation intelligence'. In the diagram that step is 'Launch Transaction', which asks Vantage to run the Skill and is followed by 'Check Transaction Status' and 'Download Results'. The glyph drawn on it is ABBYY's connector icon, not Camunda's AI-agent star.
ai_evidence_quote: "The connector lets you call any ABBYY Vantage Process Skill directly from a BPMN process model"
artefacts:
  screenshot: 085_abbyy-vantage-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own overview asset (d3bql97l1ytoxn.cloudfront.net, overview/img14629936260482908070-2x.png, 1100x452); native read at full size
---

## What the page shows

ABBYY's Vantage connector listing (Partner, 8.8/8.9, 'Reliable document AI for process orchestration'). The page describes an IDP connector that lets a Camunda process call an ABBYY Vantage Process Skill - a trained document-AI skill that classifies and extracts structured data, runs validation and matching rules, and can return a manual-review link - and its published diagram shows that call as one step of a small document-handling process.

## Observations (description only, no interpretation)

- **AI activity - function:** execute a document-AI Skill (classify, extract fields/tables, validate) on an uploaded document and return the structured result to the process.
- **AI activity - element type:** an ordinary task bound to the ABBYY Vantage connector, drawn with ABBYY's own glyph; the transaction steps are modelled as collapsed sub-processes (marker visible), no AI-agent/ad-hoc element is used.
- **Authority - downstream:** 'Check Transaction Status' and 'Download Results' consume the Skill's output, and the process ends by mailing the result files and an email to the applicant.
- **Authority - data:** the document uploaded in the first task and the extracted structured data returned by the Skill; the page states the data is returned 'as structured JSON or file formats'.
- **Authority - control:** none drawn - the diagram has no gateway, no confidence threshold and no human review step; the page describes Vantage's Manual Review link as a feature ('If Vantage determines that a document needs manual verification, the connector provides access to Vantage's Manual Review link'), which the model does not show.
- **Input provenance:** the first task uploads the document to ABBYY Vantage; the document's own origin is not modelled.
- **Guards present:** none visible in the diagram; the page's only accuracy claims are the Skill's validation rules and the Manual Review link.
- **Prompt / model detail visible:** none; the Skill is trained and configured in ABBYY Vantage, so neither its model nor any prompt appears in the BPMN.

## Notes for the researcher

Recorded as INCLUDE because the AI capability is attached to an element that is actually in the process (the Skill-executing step), which is the same basis on which this census recorded Acheron's Google Cloud AI connector (n=027). What the diagram cannot show is whether the researcher counts a call to an external document-AI service as an 'AI element', since the drawn glyph is the vendor's connector icon rather than Camunda's AI-agent template; a reviewer who reads the criterion strictly as 'AI element template' would drop this record. The page's own wording ties the AI to the process step, so E2 is not available here.
