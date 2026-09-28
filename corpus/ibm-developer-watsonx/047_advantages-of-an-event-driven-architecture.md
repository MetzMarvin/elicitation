---
n: 1291
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Advantages of the event-driven architecture pattern"
url: https://developer.ibm.com/articles/advantages-of-an-event-driven-architecture/
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: "The figure draws eight rounded event pills in a row - 'Customer order created', 'Item added to customer order', 'Customer order shipped', 'Customer address changed', 'Customer account created' and three blank - with a dashed timeline arrow underneath, and its alt text calls it an 'immutable, ordered stream of events representing state changes': an ordered event sequence - BPMN-like, or a data illustration?"
needs_visual_check: false
bpmn_evidence: "The shapes are rounded, they carry event names in a fixed order, and the page's own alt text asserts an ordered stream of events - which is the vocabulary of BPMN events on a timeline, and the closest thing in this source to an event-driven process drawing. Against that, the pills are a narrative illustration with no connectors between them and three of the eight are blank, so the ordering is carried by the drawing's layout rather than by any flow. I can name the notation (a narrative pill band), but not confidently enough to keep it out of the review queue."
bpmn_evidence_quote: "Diagram showing a business narrative as an immutable, ordered stream of events representing state changes"
ai_evidence: "The AI element is in the page's own vocabulary rather than in the figure: the pill band is about order events, and the page carries 'machine learning|predictive' in its AI vocabulary under the title 'Advantages of the event-driven architecture pattern'. This is one of the rows CLAUDE.md warns about in the other direction - the artefact is ordered and event-shaped, so the question for the researcher is whether an event sequence with no AI element inside it belongs in the corpus at all, which is a ruling I am not authorised to make (cf. records 003, 017, 022, 023, where E2 could not be applied as written for the same reason)."
ai_evidence_quote: "Diagram showing a business narrative as an immutable, ordered stream of events representing state changes"
artefacts:
  screenshot: 047_1291X_business-narrative.png
  assets: [047_1291X_business-narrative.png]
  bpmn_xml: []
  archive: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: "the figure fetched from its native asset URL on developer.ibm.com and viewed at full size on 2026-09-25, re-opened in the self-audit montage on 2026-09-26"
judgment: true
---

## What the artefact is

`https://developer.ibm.com/articles/advantages-of-an-event-driven-architecture/` (ledger row n=1291), figure `figs/1291X_business-narrative.png`.

## What the figure shows

the event-driven-architecture article: 'business-narrative.png' draws eight vertical blue pill shapes in a row - three of them blank, five labelled 'Customer order created', 'Item added to customer order', 'Customer order shipped', 'Customer address changed' and 'Customer account created' - with a dashed left-pointing timeline arrow running underneath them; the page's other two figures are 'Example of an event-driven architecture, showing loosely coupled microservices' (event-driven-architecture-example.png) and 'Diagram comparing push-based and pull-based messaging patterns in event-driven architecture' (push-pull-messaging.png).

## Why the row is UNCERTAIN and not an E1 exclusion

The shapes are rounded, they carry event names in a fixed order, and the page's own alt text asserts an ordered stream of events - which is the vocabulary of BPMN events on a timeline, and the closest thing in this source to an event-driven process drawing. Against that, the pills are a narrative illustration with no connectors between them and three of the eight are blank, so the ordering is carried by the drawing's layout rather than by any flow. I can name the notation (a narrative pill band), but not confidently enough to keep it out of the review queue.

## AI evidence (why this is not an E2 exclusion)

The AI element is in the page's own vocabulary rather than in the figure: the pill band is about order events, and the page carries 'machine learning|predictive' in its AI vocabulary under the title 'Advantages of the event-driven architecture pattern'. This is one of the rows CLAUDE.md warns about in the other direction - the artefact is ordered and event-shaped, so the question for the researcher is whether an event sequence with no AI element inside it belongs in the corpus at all, which is a ruling I am not authorised to make (cf. records 003, 017, 022, 023, where E2 could not be applied as written for the same reason).

## Notes for the researcher

- This row was first coded `E0-no-artefact` with `judgment: false` by the census pass, then recoded `E1-not-bpmn` with `judgment: true` (a drawn non-BPMN diagram is a notation call: CLAUDE.md sec 3, prompts/02b), and then flipped to `UNCERTAIN` by the self-audit that `prompts/02_source-census.md` step 3 asks for over the judgment rows. The ledger keeps all three rows for this `n`; the `supersedes_row` row is the one that counts (tools/audit.py: the last row for an `n` wins).
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
