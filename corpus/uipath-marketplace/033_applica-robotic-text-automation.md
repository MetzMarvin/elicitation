---
n: 537
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
title: "Applica - Robotic Text Automation"
url: https://marketplace.uipath.com/listings/applica-robotic-text-processing
accessed: 2026-09-28
verdict: UNCERTAIN
needs_human_ruling: true
question: "Informal box sketch joined by dashed lines (no BPMN shapes, events or gateways) in which Applica.ai steps 'Business Context Identification', 'Information Extraction' and 'Decision Making' sit next to a 'Manual Validation' box. Does it count as a BPMN diagram? (A second listing image, media/0537_0, is an Enterprise-Integration-Patterns architecture diagram, not BPMN.)"
needs_visual_check: false
bpmn_evidence: listing image 13 of 13 (media/0537_12): boxes Document Scanning (optional) / Document Retrieval & OCR (optional) -> Business Context Identification -> Information Extraction -> Decision Making -> Further Process Automation, with 'Manual Validation' above Decision Making and 'Validation against Customer DBs' below Business Context Identification, dashed connectors, UiPath/Applica icons; no BPMN shapes. media/0537_0 uses Enterprise Integration Patterns icons (message channel, router, translator) in 'UiPath area' / 'Deep Text area' frames
bpmn_evidence_quote: "enabling decision making and further document processing using UiPath RPA."
ai_evidence: boxes with the Applica.ai icon: 'Business Context Identification', 'Information Extraction', 'Decision Making'; prose on AI contextual document interpretation and self-learning from end users
ai_evidence_quote: "Automating text-intensive business processes through AI."
artefacts:
  screenshot: 033_applica-robotic-text-automation.png
  archive: 033_applica-robotic-text-automation.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1577
capture_method: python urllib GET of the original marketplace-cdn.uipath.com asset (cdn-cgi resize wrapper stripped); 1577 px is the native size
---

## What the page shows

An Applica.ai connector for text-intensive document processing. One of 13 listing images is a sketch of boxes joined by dashed lines: 'Document Scanning (optional)' above 'Document Retrieval & OCR (optional)' (UiPath icon) -> 'Business Context Identification' (Applica icon; below it 'Validation against Customer DBs', UiPath icon) -> 'Information Extraction' (Applica icon) -> 'Decision Making' (Applica icon; above it 'Manual Validation') -> 'Further Process Automation' (UiPath icon); Applica.AI and UiPath logos underneath. Other images: an Enterprise-Integration-Patterns architecture diagram (UiPath area / Deep Text area), a UiPath Studio flowchart, and Applica training/validation UI screenshots.

## Observations (description only, no interpretation)

- **AI activity - function:** 'Business Context Identification', 'Information Extraction', 'Decision Making' (Applica.ai)
- **AI activity - element type:** boxes marked with the Applica.ai icon in an informal sketch
- **Authority - downstream:** 'Further Process Automation' (UiPath)
- **Authority - data:** not visible on the page
- **Authority - control:** 'Decision Making' box attributed to Applica.ai
- **Input provenance:** documents from 'Document Retrieval & OCR (optional)'
- **Guards present:** 'Manual Validation' box attached to 'Decision Making'; 'Validation against Customer DBs' (UiPath)
- **Prompt / model detail visible:** none

## Notes for the researcher

Native asset legible; connector lines are undirected dashed lines, so the flow direction is read from left-to-right layout only.
