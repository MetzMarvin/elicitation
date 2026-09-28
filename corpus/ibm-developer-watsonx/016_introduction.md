---
n: 1794
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Introduction to watsonx Orchestrate (Learning Path: Get started with watsonx Orchestrate) - the 'Architecture flow of multi-agent orchestration' figure"
url: https://developer.ibm.com/learningpaths/get-started-watsonx-orchestrate/introduction/
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "The page's multi-agent-orchestration.png is named by its own alt text the 'Architecture flow of multi-agent orchestration with watsonx Orchestrate': agent boxes (Orchestrator Agent, Cloud Sales Agent, Enterprise Agent, Agentic Platform Manager), tool boxes (Copilot, CRM, Slack, Zendesk) and platform bands, joined by numbered arrows that order the interaction. Its boxes are systems and agents; its connectors order steps. Is it a process artefact for the corpus, or an architecture view that E0-no-artefact excludes?"
needs_visual_check: false
bpmn_evidence: "png (contact sheet SHEET_VIEW08, row 2 col 1). a large multi-agent orchestration figure: an 'Agent Ops' band with 'Cloud Sales Agent', an 'Orchestrator Agent' box, an 'Agentic Platform Manager', an 'Enterprise Agent' and custom agents; a 'Custom Sales Agent' panel with 'Copilot' and tool icons (CRM, Slack, Zendesk); bands for 'OpenShift AI', 'IBM Cloud' and 'OpenAI GPT-3.5/4.0'; and numbered arrows running between the agents. The page's own alt text calls it the 'Architecture flow of multi-agent orchestration with watsonx Orchestrate' - it says both architecture and flow. The boxes are agents and tools (systems), the connectors are numbered and ordered. I hesitated; hesitation resolves to UNCERTAIN."
bpmn_evidence_quote: "Architecture flow of multi-agent orchestration with watsonx Orchestrate"
ai_evidence: "AI elements are inside the drawn figure: agent boxes ('Orchestrator Agent', 'Cloud Sales Agent', 'Enterprise Agent', 'Agentic Platform Manager') and the tool and model boxes they call, and the page's premise is verbatim 'Organizations are increasingly turning to multi-agent systems with interoperating AI agents that collaborate to solve large-scale problems.' UNCERTAIN because its own alt text calls it an 'Architecture flow' - the boxes are agents and systems while the numbered connectors order the interaction."
ai_evidence_quote: "Architecture flow of multi-agent orchestration with watsonx Orchestrate"
artefacts:
  screenshot: 016_1794_multi-agent-orchestration.png
  assets: [016_1794_multi-agent-orchestration.png]
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

`https://developer.ibm.com/learningpaths/get-started-watsonx-orchestrate/introduction/` (html, ledger row n=1794), figure `figs/1794_multi-agent-orchestration`.

## What the figure shows



## Why the row is UNCERTAIN

png (contact sheet SHEET_VIEW08, row 2 col 1). a large multi-agent orchestration figure: an 'Agent Ops' band with 'Cloud Sales Agent', an 'Orchestrator Agent' box, an 'Agentic Platform Manager', an 'Enterprise Agent' and custom agents; a 'Custom Sales Agent' panel with 'Copilot' and tool icons (CRM, Slack, Zendesk); bands for 'OpenShift AI', 'IBM Cloud' and 'OpenAI GPT-3.5/4.0'; and numbered arrows running between the agents. The page's own alt text calls it the 'Architecture flow of multi-agent orchestration with watsonx Orchestrate' - it says both architecture and flow. The boxes are agents and tools (systems), the connectors are numbered and ordered. I hesitated; hesitation resolves to UNCERTAIN.

## AI evidence (why this is not an E2 exclusion)

AI elements are inside the drawn figure: agent boxes ('Orchestrator Agent', 'Cloud Sales Agent', 'Enterprise Agent', 'Agentic Platform Manager') and the tool and model boxes they call, and the page's premise is verbatim "Organizations are increasingly turning to multi-agent systems with interoperating AI agents that collaborate to solve large-scale problems." UNCERTAIN because its own alt text calls it an 'Architecture flow' - the boxes are agents and systems while the numbered connectors order the interaction.

## Notes for the researcher

- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
