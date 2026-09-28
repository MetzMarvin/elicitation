---
n: 1794
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: "Resume Sourcing Support"
url: https://marketplace.uipath.com/listings/resume-sourcing-support
accessed: 2026-09-28
verdict: UNCERTAIN
needs_human_ruling: true
question: "Informal box-and-arrow solution design (no BPMN shapes, events or gateways) with a 'Prompt Engineering & Gen AI' step feeding a UiPath Apps review UI. Does it count as a BPMN diagram?"
needs_visual_check: false
bpmn_evidence: slide 'High level solution design': four labelled boxes with arrows (Dispatcher Process, Prompt Engineering & Gen AI, Performer Process, UiPath Apps) and an 'ICIMS / ATS' source icon; no BPMN shapes
bpmn_evidence_quote: "The code in this Solution Accelerator package processes resume sourcing support in this progression:"
ai_evidence: box 'Prompt Engineering & Gen AI - GenAI - Prompt using GenAI, against requisition for Details Extraction'; UiPath Apps box 'Running GenAI verification'
ai_evidence_quote: "Automate, add consistency and quality to the recruitment process – and improve talent quality at the same time with the Resume Sourcing Support Solution Accelerator."
artefacts:
  screenshot: 017_resume-sourcing-support.png
  archive: 017_resume-sourcing-support.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: marginal
capture_width_px: 1600
capture_method: python urllib GET of the original marketplace-cdn.uipath.com asset (cdn-cgi resize wrapper stripped); 1600 px is the native size; a 3x LANCZOS crop of the diagram region is saved as 017_resume-sourcing-support_diagram-crop-3x.png (3420 px)
---

## What the page shows

A Solution Accelerator for recruiting. Its second image, 'High level solution design': 'ICIMS / ATS' -> 'Dispatcher Process - Extract Details - Requisition check against dashboard for new Job Entries; Extract details from each Requisition' -> 'Prompt Engineering & Gen AI - GenAI - Prompt using GenAI, against requisition for Details Extraction' -> 'Performer Process - Validation and Verification - Checking for applied Resume details and allows for validation'; arrows from Dispatcher, GenAI and Performer to 'UiPath Apps - User Interface - Running GenAI verification; Visualization of Data; Fetching and Validating information'. The title slide lists 'Prompt Engineering & Gen AI capabilities' and 'Human in the loop - Validation and Action options for Resume details'.

## Observations (description only, no interpretation)

- **AI activity - function:** 'Prompt using GenAI, against requisition for Details Extraction'
- **AI activity - element type:** a labelled rectangle 'Prompt Engineering & Gen AI' in an informal box diagram
- **Authority - downstream:** 'Performer Process - Validation and Verification'; 'UiPath Apps' user interface
- **Authority - data:** extracted requisition / resume details; 'Recruiter receives daily or weekly report to review candidates in a CSV report' (prose)
- **Authority - control:** 'Performer Process ... allows for validation'; UiPath Apps 'Fetching and Validating information'
- **Input provenance:** requisitions from 'ICIMS / ATS'; uploaded resumes ('Upload Resume' in the interface example)
- **Guards present:** 'Human in the loop - Validation and Action options for Resume details' (title slide); 'Running GenAI verification' in UiPath Apps
- **Prompt / model detail visible:** none

## Notes for the researcher

Native asset 1600 px; the 3x crop is legible.
