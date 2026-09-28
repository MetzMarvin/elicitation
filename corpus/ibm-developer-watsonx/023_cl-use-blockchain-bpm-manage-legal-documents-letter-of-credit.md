---
n: 1020
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Use blockchain BPM to manage legal documents for a letter of credit - the letter-of-credit trade cycle figure with its numbered exchanges"
url: https://developer.ibm.com/tutorials/cl-use-blockchain-bpm-manage-legal-documents-letter-of-credit/
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "The page's figure is the letter-of-credit trade process drawn as a cycle between four participants ('BUYER', 'SELLER', 'BUYER'S BANK', 'SELLER'S BANK') whose curved arrows carry the same six exchanges the page lists as numbered steps 1-6 ('1. At buyer's request, buyer's bank sends LOC to seller's bank (Letter of Credit)' ... '6. Buyer takes delivery of goods from port (Goods)'). Its boxes are participants - parties, entities - joined by labelled message flows that read as steps, so the drawing can be read as a process (a numbered trade-finance cycle) or as an interaction/context picture between parties. The page is the source's blockchain-for-BPM tutorial about managing this process, and no BPMN 2.0 model appears anywhere in its figure list. Should this figure enter the corpus?"
needs_visual_check: false
bpmn_evidence: "png, the page's own figure at full size (SHEET_Z0801, sixth tile; contact sheet SHEET_GAP0801, row 3 col 1). the letter-of-credit trade process drawn as a cycle: four participant circles ('BUYER', 'SELLER', 'BUYER'S BANK', 'SELLER'S BANK') joined by curved arrows labelled 'Goods', 'Documents', 'Payment' and 'Letter of Credit', beside the page's numbered list of the same exchanges ('1. At buyer's request, buyer's bank sends LOC to seller's bank (Letter of Credit)', '2. Seller ships goods to port near buyer (Goods)', '3. Seller obtains receipt confirmation documents from port & forwards them to its bank (Documents)', '4. Seller's bank reviews documents and sends to buyer's bank (Documents)', '5. Buyer's bank reviews entire transaction and pays seller's bank, which pays seller (Payment)', '6. Buyer takes delivery of goods from port (Goods)'). The page's other figures are blockchain-UI captures whose alt text is the placeholder 'alt'."
bpmn_evidence_quote: "Archived content Archive date: 2019-05-01 This content is no longer being updated or maintained."
ai_evidence: "there is no AI, LLM or agent element anywhere on the page and none drawn inside the figure: the page is about blockchain business process management for a letter of credit (a trade-finance process drawn as a cycle between buyer, seller and their banks), so this is the same code-list situation as records 003, 017 and 022 - the artefact may be a process figure and E2-no-ai-element cannot be applied as written, because E2 requires quoting the AI mention being dismissed and there is none to quote."
ai_evidence_quote: "Archived content Archive date: 2019-05-01 This content is no longer being updated or maintained."
artefacts:
  screenshot: 023_1020_fig1.png
  assets: [023_1020_fig1.png]
  bpmn_xml: []
  archive: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: "the figure fetched from its native asset URL on developer.ibm.com and viewed at full size on 2026-09-25"
judgment: true
---

## What the artefact is

`https://developer.ibm.com/tutorials/cl-use-blockchain-bpm-manage-legal-documents-letter-of-credit/` (api, ledger row n=1020), figure `figs/1020_fig1`.

## What the figure shows



## Why the row is UNCERTAIN

png, the page's own figure at full size (SHEET_Z0801, sixth tile; contact sheet SHEET_GAP0801, row 3 col 1). the letter-of-credit trade process drawn as a cycle: four participant circles ('BUYER', 'SELLER', "BUYER'S BANK", "SELLER'S BANK") joined by curved arrows labelled 'Goods', 'Documents', 'Payment' and 'Letter of Credit', beside the page's numbered list of the same exchanges ('1. At buyer's request, buyer's bank sends LOC to seller's bank (Letter of Credit)', '2. Seller ships goods to port near buyer (Goods)', '3. Seller obtains receipt confirmation documents from port & forwards them to its bank (Documents)', '4. Seller's bank reviews documents and sends to buyer's bank (Documents)', '5. Buyer's bank reviews entire transaction and pays seller's bank, which pays seller (Payment)', '6. Buyer takes delivery of goods from port (Goods)'). The page's other figures are blockchain-UI captures whose alt text is the placeholder 'alt'.

## AI evidence (why this is not an E2 exclusion)

there is no AI, LLM or agent element anywhere on the page and none drawn inside the figure: the page is about blockchain business process management for a letter of credit (a trade-finance process drawn as a cycle between buyer, seller and their banks), so this is the same code-list situation as records 003, 017 and 022 - the artefact may be a process figure and E2-no-ai-element cannot be applied as written, because E2 requires quoting the AI mention being dismissed and there is none to quote.

## Notes for the researcher

- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
