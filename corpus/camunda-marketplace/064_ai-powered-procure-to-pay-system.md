---
n: 64
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: AI-Powered Procure to Pay System
url: https://marketplace.camunda.com/apps/773521/ai-powered-procure-to-pay-system
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: BPMN diagrams published as the listing's own overview asset and screenshot gallery (Camunda element glyphs: start/end events, rounded-rectangle tasks with the call-activity marker, exclusive gateways drawn as X, a message catch event, an interrupting timer boundary event); no .bpmn is downloadable. The overview asset is the master process 'Purchase Request Submitted' -> ... -> 'P2P Cycle Completed' whose stages are call activities; the gallery expands each stage.
bpmn_evidence_quote: "Purchase Request Submitted"
ai_evidence: Two tasks carry the violet four-pointed-star element-template glyph (Camunda's agentic-AI template): 'AI: Classify Purchase Request' in the master process and 'Intelligent 3-Way Match' in the match stage. The invoice stage draws the AI extraction as 'Extract Invoice Data' feeding a gateway labelled 'High Confidence?' (branch 'Yes (>90%)'), and the page names the models behind the steps: 'AI-powered purchase requisition classification (GPT-4o-mini)', 'intelligent document processing for invoice extraction (AWS Textract + Claude Haiku)' and 'AI-driven three-way matching (GPT-4o) that automatically validates purchase orders, goods receipts, and invoices'.
ai_evidence_quote: "AI-powered purchase requisition classification (GPT-4o-mini)"
artefacts:
  screenshot: 064_ai-powered-procure-to-pay-system.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own overview asset (the master P2P process, 1100x73) and two of its six screenshots (the 3-way match stage, 1500x425, and the invoice stage, 1500x229); all three read natively at full size
---

## What the page shows

An Acheron procure-to-pay accelerator ('Listing Only', Solution Accelerators, AI Services and Supply Chain & Logistics tags). The page describes a platform orchestrating the procurement lifecycle with AI classification, DMN-routed approvals, AI document extraction, AI three-way matching with confidence scores, ERPNext integration and OpenSearch audit trails. Its six screenshots are the master P2P process plus one diagram per stage: PR approval, PO creation, goods receipt (with 'Quality: Inspect Goods' and 'Passed QC?'), invoice posting, 3-way match, and payment execution.

## Observations (description only, no interpretation)

- **AI activity - function:** classification of purchase requisitions, extraction of invoice data, and three-way match validation; the page also claims confidence scores and variance analysis from the matching step.
- **AI activity - element type:** two `serviceTask`-style activities carrying the violet AI-agent element-template glyph ('AI: Classify Purchase Request', 'Intelligent 3-Way Match'); the invoice extraction task is drawn as an ordinary task with a document glyph, and the remaining tasks carry an unidentified black circled-R connector glyph or the person glyph of a user task.
- **Authority - downstream:** the master process routes each stage as a call activity; in the match stage the AI task's result feeds 'Validate Against Tolerances' and then the 'Match Result?' gateway, whose branches are 'Log Auto-Approval' (Perfect Match), 'Review Match Exception' (Within Tolerance), 'Start Dispute Process' (Dispute) and 'Reject Invoice and Notify Supplier' (Beyond Tolerance).
- **Authority - data:** the invoice stage writes to the ERP ('Post Invoice to ERP', 'Add Invoice Line Item', 'Log Invoice Event'); the page names ERPNext, OpenSearch audit trails and a DMN decision table for approval routing.
- **Authority - control:** exclusive gateways on every decision ('Match Result?', 'Reviewer Decision?', 'Approval Type?', 'Approved?', 'High Confidence?', 'Valid?', 'Supplier Valid?', 'Quality Check Required?', 'Passed QC?', 'Payment Method?', 'CFO Approval Needed?'), a human 'Review Match Exception', the 'AP: Enter Invoice Manually' fallback on low extraction confidence, a 24h-SLA boundary event escalating to a director, and a multi-level approval sub-process (Level 1 Manager, Level 2 Director, Level 3 CFO).
- **Input provenance:** purchase requisitions, supplier invoices, goods receipts and physician-free procurement master data; the master process starts at 'Purchase Request Submitted'.
- **Guards present:** the 'High Confidence? (>90%)' confidence gateway with a manual-entry fallback, tolerance-based routing in the match stage, the human exception review, and the approval-level hierarchy.
- **Prompt / model detail visible:** model names are named on the page (GPT-4o-mini, GPT-4o, AWS Textract, Claude Haiku) but no prompt text, threshold value beyond '>90%', or tool definition is visible in the diagrams.

## Notes for the researcher

Captures: the master process (064_..._ai-powered-procure-to-pay-system.png) and two stage diagrams (-fig2.png = 3-way match, -fig3.png = invoice posting). The other three screenshots (PR approval 1500x684, PO creation 1500x421, goods receipt 1500x512, payment 1500x467) were read natively too and contain no AI element; their raw files are raw/figs/064/. The listing also links a 'Watch Demo' video (youtube.com/watch?v=DLGE8EyUzk8), not opened per the operator instruction of 2026-09-26 - it is not the listing's only artefact, so that instruction does not change the verdict.
