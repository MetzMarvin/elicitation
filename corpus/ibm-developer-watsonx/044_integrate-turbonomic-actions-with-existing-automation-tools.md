---
n: 544
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Integrate Turbonomic actions with existing automation tools"
url: https://developer.ibm.com/tutorials/integrate-turbonomic-actions-with-existing-automation-tools/
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: "The figure is captioned a Turbonomic action-orchestration architecture and numbers six action flows between Turbonomic's panels (Discovery & Analysis, Generate Actions, Cost Analysis, Action Automation, Action Orchestration), an Action Server and the cloud target environment: an automation action workflow or an architecture with numbered interfaces?"
needs_visual_check: false
bpmn_evidence: "The contents of the panels are actions - discover and analyse, generate actions, automate, orchestrate, execute - and the numbered flows order them across the system boundary, so the figure reads as a sequence of automation steps performed on a target, which is what the page is about. My first-pass note called it a layered architecture and that reading is available too (the panels are tiers), but the drawing itself does not settle which one it is, and it is not drawn in a notation I can name."
bpmn_evidence_quote: "Turbonomic provides automated action execution across the target infrastructure to optimize the infrastructure."
ai_evidence: "AI is the page's own framing of the artefact rather than a box inside it: the page is about automating Turbonomic's action pipeline, its AI vocabulary is 'AI' (AIOps-style automated action generation), and its premise is verbatim 'Turbonomic provides automated action execution across the target infrastructure to optimize the infrastructure.' The row is UNCERTAIN on notation and ordered steps; the researcher's question is the reading above."
ai_evidence_quote: "Turbonomic provides automated action execution across the target infrastructure to optimize the infrastructure."
artefacts:
  screenshot: 044_544_turbonomic-architecture-action-orchestration.png
  assets: [044_544_turbonomic-architecture-action-orchestration.png]
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

`https://developer.ibm.com/tutorials/integrate-turbonomic-actions-with-existing-automation-tools/` (ledger row n=544), figure `figs/544_turbonomic-architecture-action-orchestration.png`.

## What the figure shows

a layered architecture: a Turbonomic panel (USER INTERFACE / ANALYSIS POLICY / ACTIONS with Discovery & Analysis, Generate Actions, Cost Analysis, Action Automation, Action Orchestration) beside 'Action Server' and 'Cloud Target Environment' bands, with numbered flows; alt text 'Turbonomic action orchestration architec...'.

## Why the row is UNCERTAIN and not an E1 exclusion

The contents of the panels are actions - discover and analyse, generate actions, automate, orchestrate, execute - and the numbered flows order them across the system boundary, so the figure reads as a sequence of automation steps performed on a target, which is what the page is about. My first-pass note called it a layered architecture and that reading is available too (the panels are tiers), but the drawing itself does not settle which one it is, and it is not drawn in a notation I can name.

## AI evidence (why this is not an E2 exclusion)

AI is the page's own framing of the artefact rather than a box inside it: the page is about automating Turbonomic's action pipeline, its AI vocabulary is 'AI' (AIOps-style automated action generation), and its premise is verbatim "Turbonomic provides automated action execution across the target infrastructure to optimize the infrastructure." The row is UNCERTAIN on notation and ordered steps; the researcher's question is the reading above.

## Notes for the researcher

- This row was first coded `E0-no-artefact` with `judgment: false` by the census pass, then recoded `E1-not-bpmn` with `judgment: true` (a drawn non-BPMN diagram is a notation call: CLAUDE.md sec 3, prompts/02b), and then flipped to `UNCERTAIN` by the self-audit that `prompts/02_source-census.md` step 3 asks for over the judgment rows. The ledger keeps all three rows for this `n`; the `supersedes_row` row is the one that counts (tools/audit.py: the last row for an `n` wins).
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
