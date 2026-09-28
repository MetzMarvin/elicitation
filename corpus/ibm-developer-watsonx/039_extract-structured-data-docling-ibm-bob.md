---
n: 377
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Extract structured data from messy documents with Docling for IBM watsonx and IBM Bob"
url: https://developer.ibm.com/tutorials/extract-structured-data-docling-ibm-bob/
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: "The figure is captioned 'Purchase order processing architecture diagram' and its arrows are labelled with activities - 'User upload PDFs', 'Send PDFs', 'Returns Data', 'Display Results' - running between IBM Bob, a Carbon Design UI, a Python Flask App and Docling for watsonx: does an architecture whose connectors carry the activities count as a process artefact for the corpus?"
needs_visual_check: false
bpmn_evidence: "The boxes are systems, which is my architecture reading, but every connector is labelled with what happens on it and the page frames the drawing as purchase order processing, so a reader can see a four-step interaction process with IBM Bob as the AI participant. Activity-labelled connectors are how a BPMN reader reads message flows, and I cannot show the drawing is not a process - only that it is not BPMN 2.0 notation, which is not the same claim."
bpmn_evidence_quote: "Users (procurement teams, inventory managers, finance teams, and supply chain coordinators) upload multiple PO PDFs."
ai_evidence: "The AI element is a participant that acts in the sequence: one of the four boxes is IBM Bob, the AI coding agent, which is what 'Send PDFs', 'Returns Data' in the drawing turn on. The page's AI vocabulary is 'AI|Bob|MCP|watsonx Orchestrate' and the page is a tutorial for extracting structured data with Docling for watsonx, so an E2 exclusion would be false - the AI is inside the drawn interaction."
ai_evidence_quote: "Users (procurement teams, inventory managers, finance teams, and supply chain coordinators) upload multiple PO PDFs."
artefacts:
  screenshot: 039_377_architecture-v2.png
  assets: [039_377_architecture-v2.png]
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

`https://developer.ibm.com/tutorials/extract-structured-data-docling-ibm-bob/` (ledger row n=377), figure `figs/377_architecture-v2.png`.

## What the figure shows

a component view: IBM Bob with arrows labelled 'User upload PDFs', 'Send PDFs', 'Returns Data' and 'Display Results' to a Carbon Design UI, a Python Flask App and Docling for watsonx; alt text 'Purchase order processing architecture d...'.

## Why the row is UNCERTAIN and not an E1 exclusion

The boxes are systems, which is my architecture reading, but every connector is labelled with what happens on it and the page frames the drawing as purchase order processing, so a reader can see a four-step interaction process with IBM Bob as the AI participant. Activity-labelled connectors are how a BPMN reader reads message flows, and I cannot show the drawing is not a process - only that it is not BPMN 2.0 notation, which is not the same claim.

## AI evidence (why this is not an E2 exclusion)

The AI element is a participant that acts in the sequence: one of the four boxes is IBM Bob, the AI coding agent, which is what 'Send PDFs', 'Returns Data' in the drawing turn on. The page's AI vocabulary is 'AI|Bob|MCP|watsonx Orchestrate' and the page is a tutorial for extracting structured data with Docling for watsonx, so an E2 exclusion would be false - the AI is inside the drawn interaction.

## Notes for the researcher

- This row was first coded `E0-no-artefact` with `judgment: false` by the census pass, then recoded `E1-not-bpmn` with `judgment: true` (a drawn non-BPMN diagram is a notation call: CLAUDE.md sec 3, prompts/02b), and then flipped to `UNCERTAIN` by the self-audit that `prompts/02_source-census.md` step 3 asks for over the judgment rows. The ledger keeps all three rows for this `n`; the `supersedes_row` row is the one that counts (tools/audit.py: the last row for an `n` wins).
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
