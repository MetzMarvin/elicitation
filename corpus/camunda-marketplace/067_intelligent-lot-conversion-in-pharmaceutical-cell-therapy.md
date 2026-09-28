---
n: 67
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Intelligent Lot Conversion in Pharmaceutical Cell Therapy
url: https://marketplace.camunda.com/apps/780873/intelligent-lot-conversion-in-pharmaceutical-cell-therapy
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: BPMN diagrams inside a published Cognizant slide ('Camunda + Agentic AI based implementation', slide 6 of the deck, footer '2025-2027 Cognizant | Private'). Three separate models are drawn: the lot-disposition process (start event 'Physician Email Received', a large ad-hoc sub-process with the tilde marker, end event 'Lot Disposition Complete'), the conversion process ('Create QMS Change Order' -> 'Log Compliance Information' -> 'Lot Converted') and a small investigation process ('Create Investigation Case' -> 'Material Review Board (MRB) Decision' -> 'Investigation Complete').
bpmn_evidence_quote: "Physician Email Received"
ai_evidence: Two tasks in the lot-disposition process carry the violet four-pointed-star element-template glyph (Camunda's agentic-AI template): 'Parse Lot Data - Physician Email' and 'Determine Lot Disposition'. The page's feature list says the agent '[a]utomatically extracts data from physician emails and QC reports, improving accuracy and accelerating lot disposition decisions', and its catalogue tags include 'Agentic AI orchestration' and 'AI Services'. The listing's overview image is a second slide (domain/process architecture boxes, not BPMN).
ai_evidence_quote: "Automatically extracts data from physician emails and QC reports"
artefacts:
  screenshot: 067_intelligent-lot-conversion-in-pharmaceutical-cell-therapy.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own screenshot (d3bql97l1ytoxn.cloudfront.net, screenshot/img3196294786674242296.png, 1500x779); native read at full size, plus the same slide at 750x390 and the listing's overview slide at 1100x619
---

## What the page shows

A Cognizant 'Listing Only' solution accelerator for out-of-spec lot conversion in cell and gene therapy. The page describes orchestrating lot conversion across commercial and clinical pathways, with agent-driven decision support extracting data from physician emails and QC reports, human-in-the-loop governance, and multi-system updates (quality, manufacturing, regulatory, supply chain). The published BPMN slide shows the disposition process branching inside an ad-hoc sub-process into 'Convert Lot to Clinical', 'Convert Lot for Research', 'Discard: Log Discard & Notify', 'Recollect: Request Sample Re-Collection', 'Log Compliance Data' and the human 'Escalate: Investigate Anomaly', then the downstream system updates.

## Observations (description only, no interpretation)

- **AI activity - function:** parse the physician email and decide the lot disposition; the page adds extraction from QC reports and 'AI-driven disposition decisions'.
- **AI activity - element type:** `serviceTask`-style activities carrying the violet AI-agent element-template glyph; the tools they feed sit inside an ad-hoc sub-process (tilde marker).
- **Authority - downstream:** the disposition branch tasks (convert to clinical / convert for research / discard / recollect / log compliance data / escalate to investigation) and the downstream update tasks 'Update Infinify', 'Update SAP', 'Update LMS' in the conversion process.
- **Authority - data:** physician emails and QC reports as input; SAP, LMS and Infinify as written systems; a canonical data-mapping step ('Map to Canonical Data Mapping UDM').
- **Authority - control:** the ad-hoc sub-process boundary, the parallel gateways around the three system updates, and the human steps 'Escalate: Investigate Anomaly' and 'Material Review Board (MRB) Decision'.
- **Input provenance:** the physician's email (start event 'Physician Email Received').
- **Guards present:** the page names 'Human-in-the-loop governance' as a feature, and the diagram routes anomalies to a human investigation path with an MRB decision.
- **Prompt / model detail visible:** none visible; the page names no model or prompt.

## Notes for the researcher

Captures: the BPMN slide at full size. The listing also publishes its overview slide (1100x619, 'Out of the Spec Process in Cell Therapy Value Chain - Life Sciences'), which is a domain/architecture box diagram rather than BPMN, and links a 'Watch Demo' video (youtu.be/nY0eTVygdPg) that was not opened per the operator instruction of 2026-09-26; the listing publishes BPMN figures, so it is not a video-only listing.
