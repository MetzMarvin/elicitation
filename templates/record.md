# Record format: one file per collected artefact

Path: `notes/elicitation/corpus/<source-slug>/NNN_<slug>.md`. YAML frontmatter (parsable,
used by the reconciliation pass) followed by prose. Every field is mandatory; use `null`
rather than omitting a field, and never invent a value.

```markdown
---
n: 7
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog            # vendor blog | vendor docs | vendor marketplace | vendor live modeller | practitioner blog | consultancy | community | academic
title: The Benefits of BPMN AI Agents
url: https://camunda.com/blog/2025/05/benefits-bpmn-ai-agents/
accessed: 2026-09-21
verdict: INCLUDE                    # INCLUDE | UNCERTAIN
needs_human_ruling: false
question: null                      # the exact question, if needs_human_ruling
needs_visual_check: false           # true if the agent could not read the diagram itself
bpmn_evidence: rendered bpmn-js canvas, djs-element classes on 14 shapes
bpmn_evidence_quote: "Do we need to run some tools?"
ai_evidence: task labelled "AI Task Agent" bound to an ad-hoc sub-process of tools
ai_evidence_quote: "AI Task Agent"
artefacts:
  screenshot: 007_ai-task-agent-message-delivery.png
  archive: 007_ai-task-agent-message-delivery.page.html  # or fullpage-screenshot | null
  bpmn_xml: null                                          # or 007_...bpmn
duplicate_of: null                  # record path, if E3 within this source
access: public                      # public | free-account | paid-trial
capture_source: original-asset      # bpmn-xml | original-asset | element-screenshot | fullpage-screenshot
capture_quality: legible            # legible | marginal | poor (say what is unreadable)
capture_width_px: 1920              # measured on the file that landed on disk
capture_method: chrome-devtools-mcp, get_network_request filePath on the diagram asset
---

## What the page shows

Two or three sentences, verbatim-grounded, on the process the diagram depicts and where
the AI element sits. Quote element labels exactly as printed.

## Observations (description only, no interpretation)

- **AI activity - function:** what the page says the AI element does, quoted.
- **AI activity - element type:** how it appears in BPMN terms (service task, dedicated
  AI task node type, ad-hoc sub-process, user task with AI assist, task with an AI
  implementation binding, whole-process delegation to an agent).
- **Authority - downstream:** tasks, service calls, connectors, tools the AI element can
  invoke, as named on the page.
- **Authority - data:** data objects, variables, records it writes or updates.
- **Authority - control:** gateways, decisions, human steps that consume its output.
- **Input provenance:** where the content reaching the AI element comes from (email body,
  uploaded document, fetched web page, customer message, internal database, human form).
- **Guards present:** human review, confirmation gate, filter, prompt guard, audit log -
  or `none observed`.
- **Prompt / model detail visible:** model names, system or user prompt text, template
  variables, tool definitions. Quote them; this is the most valuable evidence there is.

Write `not visible on the page` wherever the page does not say. Do not infer, do not
classify into a pattern, do not name threats or rate risk: pattern derivation and threat
modelling are the researcher's manual steps and your interpretation would contaminate
them.

## Notes for the researcher

Anything unusual: a vendor mechanic that differs from other sources, a page that seems to
have more artefacts behind it, a listing that looked templated, something you had to
toggle in a vendor editor and reverted.
```
