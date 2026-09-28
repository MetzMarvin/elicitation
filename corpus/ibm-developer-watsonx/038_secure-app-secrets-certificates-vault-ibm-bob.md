---
n: 341
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Secure app secrets and certificates using shift-left security practices with HashiCorp Vault and IBM Bob"
url: https://developer.ibm.com/tutorials/secure-app-secrets-certificates-vault-ibm-bob/
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: "The figure's alt text calls it a 'Workflow diagram' and its five numbered steps (1. Scan, 2. Analyze, 3. Create Secrets & Certificates via Vault MCP Server, 4. Refactor, 5. Rotate) run between HashiCorp Vault Radar, IBM Bob, HashiCorp Vault Dedicated and 'Secured Code': does a numbered sequence of activities performed with an AI agent between system boxes count as an AI-in-BPMN candidate?"
needs_visual_check: false
bpmn_evidence: "The drawing is a component view in which the connectors are numbered steps carrying activity labels - scan, analyze, create, refactor, rotate - and one of the participants is an AI agent. Ordered, numbered, activity-labelled steps with an AI actor is the exact shape a BPMN reader recognises, and the page calls the figure a workflow diagram; that the boxes are products rather than lanes is the architecture reading, not a refutation of the process one."
bpmn_evidence_quote: "Before developers deploy applications to production, they must ensure credentials are not hardcoded and communications are secured with certificate authority (CA) infrastructure."
ai_evidence: "The AI element is a participant of the drawn sequence: one of the four boxes is IBM Bob, and one of the numbered steps is performed through the Vault MCP Server. The page's AI vocabulary is 'AI|Bob|MCP' (it also carries 'gateway' in its BPMN vocabulary) and its premise is verbatim 'Before developers deploy applications to production, they must ensure credentials are not hardcoded and communications are secured with certificate authority (CA) infrastructure.' Nothing here rests on the absence of an AI element."
ai_evidence_quote: "Before developers deploy applications to production, they must ensure credentials are not hardcoded and communications are secured with certificate authority (CA) infrastructure."
artefacts:
  screenshot: 038_341_architecture-v3.png
  assets: [038_341_architecture-v3.png]
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

`https://developer.ibm.com/tutorials/secure-app-secrets-certificates-vault-ibm-bob/` (ledger row n=341), figure `figs/341_architecture-v3.png`.

## What the figure shows

a four-component architecture with numbered interaction arrows: HashiCorp Vault Radar, IBM Bob, HashiCorp Vault Dedicated and 'Secured Code', joined by arrows labelled '1. Scan', '2. Analyze', '3. Create Secrets & Certificates via Vault MCP Server', '4. Refactor' and '5. Rotate'. The boxes are systems and the numbers number the interfaces between them; the page's alt text calls it a 'Workflow diagram: Vault Radar scans code...'. Component interactions, not activities performed in sequence.

## Why the row is UNCERTAIN and not an E1 exclusion

The drawing is a component view in which the connectors are numbered steps carrying activity labels - scan, analyze, create, refactor, rotate - and one of the participants is an AI agent. Ordered, numbered, activity-labelled steps with an AI actor is the exact shape a BPMN reader recognises, and the page calls the figure a workflow diagram; that the boxes are products rather than lanes is the architecture reading, not a refutation of the process one.

## AI evidence (why this is not an E2 exclusion)

The AI element is a participant of the drawn sequence: one of the four boxes is IBM Bob, and one of the numbered steps is performed through the Vault MCP Server. The page's AI vocabulary is 'AI|Bob|MCP' (it also carries 'gateway' in its BPMN vocabulary) and its premise is verbatim "Before developers deploy applications to production, they must ensure credentials are not hardcoded and communications are secured with certificate authority (CA) infrastructure." Nothing here rests on the absence of an AI element.

## Notes for the researcher

- This row was first coded `E0-no-artefact` with `judgment: false` by the census pass, then recoded `E1-not-bpmn` with `judgment: true` (a drawn non-BPMN diagram is a notation call: CLAUDE.md sec 3, prompts/02b), and then flipped to `UNCERTAIN` by the self-audit that `prompts/02_source-census.md` step 3 asks for over the judgment rows. The ledger keeps all three rows for this `n`; the `supersedes_row` row is the one that counts (tools/audit.py: the last row for an `n` wins).
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
