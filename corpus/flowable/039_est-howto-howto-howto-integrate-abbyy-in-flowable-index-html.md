---
n: 239
source: flowable
source_name: Flowable (enterprise documentation, vendor blog/marketing site, training site)
title: Integrate ABBYY Vantage with Flowable | Flowable Enterprise Documentation
url: https://documentation.flowable.com/latest/howto/howto/howto-integrate-abbyy-in-flowable/index.html
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "The figure abbyy-design-service-task-configure-1-3aff344d892e6cf3d50ffc3780932f3e.png is settled by sight: a genuine BPMN 2.0 process in the Flowable Design modeller (start event circle -> 'ABBYY Service Task' with the gear glyph -> 'Classify Data' call activity -> 'Review Claim' user task -> exclusive gateway drawn as a diamond with an X labelled 'claim valid' -> second X gateway -> 'Notify Customer about declined dispute' user task -> end circle). The selected task's properties panel reads 'ABBYY Service Task - General', Model Id ABBYYServiceTask_59, Input documents ${document}, 'Skill ID: FlowMoney Inc. Transaction Dispute Manual Review', Output variable name extractedVariables, Save output variables as transient variable: False. No element in that process carries an AI label and none carries Flowable's AI Agent glyph (small robot face). The page prose never uses the word AI - it only says 'use the ABBYY Vantage service to extract data from documents'. So the whole question is a definitional one: does a service task bound to an ABBYY Vantage skill count as an AI/LLM element inside the process for this method? ABBYY Vantage is intelligent document processing (ML-trained extraction skills), and the method's scope note puts 'AI element visible only as a task property or binding' in scope; if the researcher counts it, this entry is INCLUDE, and if not it is E2-no-ai-element."
needs_visual_check: false
bpmn_evidence: settled by sight: abbyy-design-service-task-configure-1 is a BPMN 2.0 process diagram (start event circle, service task carrying the gear glyph, a call activity drawn as a thick-bordered rectangle, a user task with the person glyph, and two exclusive gateways drawn as diamonds with an X). The page prose itself names the artefacts only as "processes or cases".
bpmn_evidence_quote: "With the ABBYY Service Task, you can trigger the extraction of data from a document."
ai_evidence: not established: the process's only candidate AI element is the 'ABBYY Service Task' bound to an ABBYY Vantage skill (Skill ID 'FlowMoney Inc. Transaction Dispute Manual Review'), which carries the gear task-type glyph, not an AI label and not Flowable's robot-face AI glyph; the page prose never uses the word AI. Whether an ABBYY Vantage skill binding counts as an AI/LLM element for this method is the definitional question in the frontmatter. The census line here previously read "the page text discusses AI: With the ABBYY Service Task..." - templated, false, corrected 2026-09-26.
ai_evidence_quote: none - the page contains no AI mention to quote; the ABBYY sentence quoted under bpmn_evidence_quote is not an AI quote.
artefacts:
  screenshot: 039_est-howto-howto-howto-integrate-abbyy-in-flowable-index-html.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: poor
capture_width_px: 0
capture_method: urllib download of https://documentation.flowable.com/latest/assets/images/abbyy-configuration-menu-14b0544ffaf57974b59c823139974803.png (asset published by the page); labels inside read with RapidOCR, this session cannot receive image content
---

## Why this row is UNCERTAIN

The figure is now certified (see the sighted pass below): it is a BPMN 2.0 process whose
only candidate AI element is a service task bound to an **ABBYY Vantage** skill. Whether
that binding is an AI/LLM element for this method is a definitional call the researcher
must make, so the row is UNCERTAIN with `needs_human_ruling` and the exact question in the
frontmatter - not E2, because an element whose implementation may be AI-bound but is not
visible must never be excluded (CLAUDE.md section 3).

## Observations (description only, no interpretation)

- **Figures on the page:** ABBYY configuration menu | abbyy-configuration-menu-14b0544ffaf57974b59c82313; ABBYY configuration menu | abbyy-configuration-menu-public-api-c76d5218cd6427; ABBYY configuration menu | abbyy-configuration-menu-add-client-97a31ea0bd7555; ABBYY configuration menu | abbyy-configuration-menu-client-credentials-746cdb
- **OCR labels of the captured figure:** (none legible)
- **Page text quote:** With the ABBYY Service Task, you can trigger the extraction of data from a document.
- **Captured asset:** https://documentation.flowable.com/latest/assets/images/abbyy-configuration-menu-14b0544ffaf57974b59c823139974803.png (0x0)

## What to check

Whether the captured figure (or another figure on the page) is a BPMN 2.0 process
diagram and whether an AI/LLM element sits inside that process.

## Sighted pass (shard s1, 2026-09-25)

`needs_visual_check` is now **false**: all 11 figures were looked at with real vision
(Read on the PNGs), four of them natively.

- **abbyy-design-service-task-configure-1-3aff344d892e6cf3d50ffc3780932f3e.png** is the
  decisive figure and it is a **BPMN 2.0** process in Flowable Design: start event circle
  → ``ABBYY Service Task`` (gear glyph) → ``Classify Data`` (thick border, i.e. a call
  activity) → ``Review Claim`` (person glyph) → exclusive gateway drawn as a diamond with
  an X, labelled ``claim valid`` → branch to ``Notify Customer about declined dispute``
  (person glyph) → end circle, and a second X gateway on the other branch. The selected
  task's properties panel is ``ABBYY Service Task - General`` with Model Id
  ``ABBYYServiceTask_59``, Input documents ``${document}``, ``Skill ID: FlowMoney Inc.
  Transaction Dispute Manual Review``, Output variable name ``extractedVariables``,
  ``Save output variables as transient variable: False``.
- Nothing in that process carries an AI label or Flowable's AI Agent glyph (the small
  robot face recorded on n=720's CMMN case ``Classify documents``), so the element's
  AI-ness can only come from what the ABBYY Vantage service *is*, not from anything the
  page shows or says.
- The rest of the figures: the ABBYY Vantage web console (Skills / Skill Monitor / Skill
  Designer / Data Catalogs / Manual Review / Users menus, the Public API Client with
  ``Allow client credentials flow`` ticked, Authorized Redirect URLs under OAuth 2.0 Flow
  Settings, Manage Roles), two further ABBYY Service Task property dialogs over the same
  modeller, the Design form editor with ``abbbyManualReviewForm``, the Flowable Work task
  showing the embedded ABBYY Vantage Manual Review iframe over a
  ``FlowMoney Inc. Transaction Dispute Form``, and a Form configuration panel whose
  ``Manual review form`` field points at ``abbyyManualReviewForm``.
- Note for the reviewer: the census row's ``ai_evidence_quote`` - "With the ABBYY Service
  Task, you can trigger the extraction of data from a document." - contains **no AI
  mention** and is a false positive, and no figure or paragraph on the page contains the
  string AI/LLM/agent at all. The verdict is UNCERTAIN because the AI-ness of an ABBYY
  Vantage service binding is a definitional call for the researcher, not for this
  collection instrument.
