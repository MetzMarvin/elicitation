---
n: 218
source: flowable
source_name: Flowable (enterprise documentation, vendor blog/marketing site, training site)
title: Loan App: First experience with Flowable | Flowable Enterprise Documentation
url: https://documentation.flowable.com/latest/howto/cloud/cloud-loan/index.html
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "intro-4d3408687128e84b5708006d0055fa14.png is settled as BPMN 2.0 (Review carries a timer boundary event, and two exclusive gateways are drawn as diamonds with an X; no CMMN cut-corner stages, sentry diamonds or folder case plan model). Its two glyph-carrying tasks are NOT AI elements by glyph: Alert carries a rounded speech bubble with a lower-left tail (the same glyph as the Engage message tasks, e.g. Post initial message on n=496) and Create... carries a page/document outline with a diamond inside it, consistent with the document-type glyph and with the Generate document side panel on the same screen. Neither matches Flowable's AI Agent glyph, which is a small robot face (rounded square, two dots, a top bar) rendered on n=720's CMMN case. So the remaining question is not the glyphs: (a) is any element of this process AI-bound while carrying no distinguishing glyph at all - in particular the two message/document tasks - given that a BPMN service task bound to an AI service definition shows no special glyph (n=95 is the source's strongest positive, AI visible only in the Service Registry binding)? (b) The figure is cropped at its bottom edge: does that missing part hide an AI-bound element? If either yields an AI-bound element the verdict is INCLUDE; if both are clean it is E2-no-ai-element."
needs_visual_check: false
bpmn_evidence: settled by sight: the figure is a BPMN 2.0 process, certified by two decisive markers - Review carries a timer boundary event (clock circle straddling its lower border) and two exclusive gateways are drawn as diamonds with an X. The page prose itself does not name BPMN constructs, so the verbatim quote kept here is the page sentence the census had captured, not notation evidence.
bpmn_evidence_quote: "Our goal is that within 10 minutes, you will have run your first demo that includes case, process, decision and content management!"
ai_evidence: not established: no AI element is visible in the loan-app process and the page prose never uses AI, LLM, agent or intelligence. Two task-type glyphs on the process (a speech-bubble marker on 'Alert', a page-with-plus marker on 'Create...') could not be explained; neither is Flowable's robot-face AI glyph, and the figure is cut off at its bottom edge, so the process is only partly published. Whether either task is AI-bound is the question in the frontmatter. The census line here previously read "the page text discusses AI: Our goal is that within 10 minutes..." - templated, false, corrected 2026-09-26.
ai_evidence_quote: none - the page contains no AI mention to quote; the sentence quoted under bpmn_evidence_quote is a non-AI page sentence.
artefacts:
  screenshot: 033_tation-flowable-com-latest-howto-cloud-cloud-loan-index-html.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: poor
capture_width_px: 0
capture_method: urllib download of https://documentation.flowable.com/latest/assets/images/intro-4d3408687128e84b5708006d0055fa14.png (asset published by the page); labels inside read with RapidOCR, this session cannot receive image content
---

## Why this row is UNCERTAIN

The page publishes figures and mentions AI, but the figure that would decide the
verdict could not be certified from the evidence this session can read (the DOM, the
page text, and OCR labels). Per CLAUDE.md section 5 an unresolved figure is UNCERTAIN
with needs_visual_check, never an exclusion.

## Observations (description only, no interpretation)

- **Figures on the page:** New case | intro-4d3408687128e84b5708006d0055fa14.png; New case | dashboard-a33614b4f769c08b9609d316d9d644c3.png; Start form | start-form-bc4eafc75c16474cc326130727f30dad.png; Case View 1 | case-1-5651ccec0ce3032267056d7e0e5be7c4.png
- **OCR labels of the captured figure:** (none legible)
- **Page text quote:** Our goal is that within 10 minutes, you will have run your first demo that includes case, process, decision and content management!
- **Captured asset:** https://documentation.flowable.com/latest/assets/images/intro-4d3408687128e84b5708006d0055fa14.png (0x0)

## What to check

Whether the captured figure (or another figure on the page) is a BPMN 2.0 process
diagram and whether an AI/LLM element sits inside that process.

## Sighted pass (shard s1, 2026-09-25)

`needs_visual_check` is now **false**: the figures were looked at with real vision
(Read on the PNGs), and intro-4d3408687128e84b5708006d0055fa14.png was additionally
cropped at 4x, 8x and 9x.

- **intro-4d3408687128e84b5708006d0055fa14.png** is a screenshot of the Flowable Design
  modeller (workspace tabs Apps, Cases, Processes, Decisions, Forms, Pages, Others,
  Design; model tabs "Loan application" and "Loan details"; a "Generate document" side
  panel) holding a genuine **BPMN 2.0** process: start glyph → ``Get details`` (person
  glyph) → ``Loan advice`` (calendar glyph) → ``Review`` (person glyph) with a **boundary
  timer event** on its lower border → **X exclusive gateway** → ``Reject`` / ``Escalate``
  / ``Assign`` (person glyphs) → second X gateway → end, plus a branch to ``Alert``. No
  CMMN stage rectangles, no sentry diamonds, no case-plan folder: the notation is BPMN.
- No AI element is labelled in that process, and the page text carries **no AI content**
  at all (the only ``AI`` string on the rendered page is the docs top-nav tab). Note that
  the census row's ``ai_evidence_quote`` — "Our goal is that within 10 minutes, you will
  have run your first demo that includes case, process, decision and content management!"
  — contains no AI mention and is therefore a false positive in the census row.
- **Unresolved:** ``Alert`` carries a speech-bubble task marker and ``Create...`` carries
  a page-with-plus marker; neither maps to a Flowable element type I could confirm, and
  Flowable's AI Agent Task is a first-class BPMN element whose icon could not be compared.
  The figure is also cropped at its bottom edge, so part of the process is not published.
  This is why the row stays UNCERTAIN rather than E2 (icon-only ⇒ UNCERTAIN, never E2 and
  never INCLUDE).
- The other 19 figures are Flowable Work / Engage UI screenshots of the trial Loan App
  (Loans home dashboard, New Loan Request dialog, case detail with a 5-stage header,
  Review application / Get application details forms with Accept / Reject / Escalate,
  Escalated review, Assign manager, Acceptance letter, Early Repayment, Closing Stage,
  Completed Tasks, Collect repayment). None is a process diagram.
- The figure's ``alt`` is "New case", which is inaccurate — the figure shows the Design
  modeller, not a case view. Consistent with the known unreliability of alt text here.

### Narrowing added after this shard's sighted pass (coordinator, 2026-09-25; amended)

The notation half of the question is now settled by a second sighted look, and the
question above was rewritten to drop it:

- It is **BPMN 2.0**: ``Review`` carries a **timer boundary event** (clock circle straddling
  its lower border) and there are two **exclusive gateways drawn as diamonds with an X**,
  which CMMN has no equivalent of. No cut-corner stages, no sentry diamonds on borders,
  no folder case plan model — so `E1-not-bpmn` is off the table. ``bpmn_evidence`` above was
  upgraded accordingly; the page's own prose never names BPMN constructs, so the
  ``bpmn_evidence_quote`` field keeps the page sentence the census had captured.
- **Flowable's AI Agent glyph is known**: a small **robot face** (rounded square, two dots,
  a top bar), rendered once in this corpus on n=720's CMMN case ``Classify documents``,
  whose Payout-stage plan item is literally labelled ``AI Agent``. The **glyph comparison
  can therefore be made**, and neither glyph here is a robot face: ``Alert`` carries a
  rounded speech bubble with a lower-left tail, the same glyph as the Engage tutorial's
  message tasks (``Post initial message`` on n=496's ``59-initialization-process-1-react``),
  and ``Create...`` carries a page/document outline with a diamond inside it — the same
  document-task family as the page-with-star glyph confirmed by this shard on n=233 and the
  ``Create content object`` / ``Create letter`` glyphs read at 7x on n=257, and consistent
  with the "Generate document" side panel visible on the same screen.
- It nevertheless stays UNCERTAIN, for two reasons that glyph absence cannot answer: a BPMN
  service task **bound to an AI service definition carries no special glyph at all** (n=95
  is the source's strongest positive — plain service tasks, AI visible only in the Service
  Registry binding), so the two message/document tasks could still be AI-bound; and the
  figure remains **cropped at its bottom edge**, so an unpublished element could be too.
- Note for the reviewer: n=262 publishes a figure set that is **byte-identical** to this
  one (all 20 files, MD5-compared, and the same guide prose), and has been recorded as
  `E3-duplicate` pointing back at this record, so this same figure and question recur there.
- One further element of this figure is now accounted for and is **not** an AI binding: the
  ``Loan advice`` task is a **DMN decision task**, not a service task. n=259's prose (the
  "How it was all put together" page of the same Loan App tutorial) says "In the Loan
  application process a simple decision table is used to guide the process flow" and that
  clicking on the ``Loan Advice`` task opens a "Decision table reference". It therefore does
  not narrow the question above, which stays open for the two message/document tasks.
