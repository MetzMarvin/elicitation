---
n: 549
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Securing autonomous AI agents: Applying Zero Trust to transformative AI - the dynamic-credential flow figure with numbered steps on its arrows"
url: https://developer.ibm.com/articles/securing-ai-agents/
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "The page's figure is an architecture diagram whose numbered arrows spell out an ordered procedure ('1. Authenticate', '2. Exchange user token with on-behalf-of token', '4a. Authenticate with HashiCorp Vault', '5a. Request dynamic credential', '6. Access resource using dynamic credential', '7. Close dynamic credential after time-to-live') between a user, an 'IBM watsonx Orchestrate Agent' (an AI agent), an 'MCP Server', 'IBM Verify' and 'HashiCorp Vault'. Its boxes are users, an AI agent and services (an architecture reading), while its numbered, labelled arrows order the steps (a process reading). Is it a process artefact the corpus records - an AI agent inside a drawn, numbered flow - or an architecture diagram that E0-no-artefact excludes?"
needs_visual_check: false
bpmn_evidence: "png, the page's own figure fetched at full size and viewed as the fourth tile of SHEET_Z0401; its alt text begins 'Architecture diagram showing how IBM Ver...'. an architecture diagram that also carries a numbered step sequence on its arrows: boxes for two user icons ('Bob (read and write)', 'Alice (read only)'), 'IBM Verify', 'HashiCorp Vault', a 'Web Application', an 'IBM watsonx Orchestrate Agent', an 'MCP Server' and a 'Resource', joined by numbered labelled arrows - '1. Authenticate', '2. Exchange user token with on-behalf-of token', '3b. Validate OBO Token', '4a. Authenticate with HashiCorp Vault', '4b. Validate token and permission scope', '5a. Request dynamic credential', '5b. Generate and provision dynamic credential', '6. Access resource using dynamic credential', '7. Close dynamic credential after time-to-live'. The boxes are users, an AI agent, services and a vault; the numbered arrows read as the steps of the flow. I hesitated between an architecture view and a process; hesitation resolves to UNCERTAIN."
bpmn_evidence_quote: "Architecture diagram showing how IBM Ver"
ai_evidence: "AI is inside the drawn figure and the whole page is about it: the flow's central box is an 'IBM watsonx Orchestrate Agent', the numbered arrows describe exchanging a user token for an on-behalf-of token and closing a dynamic credential after its time-to-live, and the page's premise is verbatim 'As AI agents gain autonomy, they need credentials that expire, scope narrowly, and leave an audit trail.' The page's digest AI vocabulary is 'AI|MCP|agentic|intelligent|watsonx Orchestrate'. UNCERTAIN because the boxes are users, an AI agent and services while the numbered arrows order the steps."
ai_evidence_quote: "Architecture diagram showing how IBM Ver"
artefacts:
  screenshot: 019_549_architecture-mitigating-cdp3.png
  assets: [019_549_architecture-mitigating-cdp3.png]
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

`https://developer.ibm.com/articles/securing-ai-agents/` (api, ledger row n=549), figure `figs/549_architecture-mitigating-cdp3`.

## What the figure shows



## Why the row is UNCERTAIN

png, the page's own figure fetched at full size and viewed as the fourth tile of SHEET_Z0401; its alt text begins 'Architecture diagram showing how IBM Ver...'. an architecture diagram that also carries a numbered step sequence on its arrows: boxes for two user icons ('Bob (read and write)', 'Alice (read only)'), 'IBM Verify', 'HashiCorp Vault', a 'Web Application', an 'IBM watsonx Orchestrate Agent', an 'MCP Server' and a 'Resource', joined by numbered labelled arrows - '1. Authenticate', '2. Exchange user token with on-behalf-of token', '3b. Validate OBO Token', '4a. Authenticate with HashiCorp Vault', '4b. Validate token and permission scope', '5a. Request dynamic credential', '5b. Generate and provision dynamic credential', '6. Access resource using dynamic credential', '7. Close dynamic credential after time-to-live'. The boxes are users, an AI agent, services and a vault; the numbered arrows read as the steps of the flow. I hesitated between an architecture view and a process; hesitation resolves to UNCERTAIN.

## AI evidence (why this is not an E2 exclusion)

AI is inside the drawn figure and the whole page is about it: the flow's central box is an 'IBM watsonx Orchestrate Agent', the numbered arrows describe exchanging a user token for an on-behalf-of token and closing a dynamic credential after its time-to-live, and the page's premise is verbatim "As AI agents gain autonomy, they need credentials that expire, scope narrowly, and leave an audit trail." The page's digest AI vocabulary is 'AI|MCP|agentic|intelligent|watsonx Orchestrate'. UNCERTAIN because the boxes are users, an AI agent and services while the numbered arrows order the steps.

## Notes for the researcher

- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
