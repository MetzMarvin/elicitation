---
source: celonis
source_name: Celonis (Process Management / Process Designer, ex-Symbio; Orchestration Engine)
source_type: vendor site + developer portal (+ login-walled docs)
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: NO (operator ruling B11 2026-09-24: AI about processes, Signavio category)
  C2_native_bpmn20: YES
  C3_publicly_accessible: PARTIAL
  C4_enterprise_presence: YES
access: public (developer portal, marketing site) / blocked (docs.celonis.com, Celonis ID login)
population_type: enumerable
population_estimate: 40
effort: medium
needs_logged_in_browser: false
status: OUT-C1 (not surveyed; kept for audit trail)
---

## Why this file exists

Pass 1 expected Celonis to be a clean C2 rejection, since it is known for process mining.
It is not one. Celonis Process Management (the former Symbio modeller) is native BPMN 2.0,
and the product page promises "AI-insertion points" in the process model. See ruling
**B11** and blocker **A4** in `OPERATOR-TODO.md`.

## Criteria evidence

- **C2 YES**: https://developer.celonis.com/cpm/developer/services/graphic/elements_tasks
  (2026-09-24): "The task types that are defined by BPMN are: none service send receive
  receive and instantiate process manual user business role script". The page maps each
  type to BPMN XML, e.g. `<serviceTask> ... </serviceTask>`.
- **C1 UNCLEAR**: https://www.celonis.com/platform/process-management (2026-09-24):
  "Enable strategic process management and define guardrails, outcomes, and AI-insertion
  points." The same page also says "jump-starting your process-modeling efforts with
  generative AI process modeling", which is design-time AI (E2 territory). The question is
  whether an "AI-insertion point" ever shows up as an element in a BPMN diagram.
- **C3 PARTIAL**: every `docs.celonis.com` URL that was opened redirected to
  `celonis.my.site.com/docs/s/login/` ("Celonis ID Login / Celonaut Login"). The developer
  portal and the marketing site are anonymous.
- **C4 YES**: Celonis is a large process-intelligence vendor.

## Entry points

- `https://www.celonis.com/platform/process-management`: anchor for C1
- `https://developer.celonis.com/cpm/developer/services/graphic/elements_tasks` and its
  siblings (e.g. "BPMN sub-processes and call activities"): the public BPMN element
  reference for Celonis Process Management
- Google result titles, **not opened (login wall)**: "Creating Orchestration Engine
  overview", "Adding Process Copilot to Process Orchestration steps", "Celonis Process
  Management BPMN reference", "BPMN Importer Configuration", "Creating and importing process
  model diagrams"
- Google result titles, **not opened (public)**: "Celonis Showcases Latest Process
  Intelligence and AI …", "Making AI Agents Work for the Enterprise with Process …"
  (AgentC press release), "AI assistants, copilots, and agents: explained"

## Enumeration instructions

1. First settle C1 with one question: does any public Celonis artefact show an AI element
   inside a BPMN diagram? Candidates are the AI-insertion points in Process Designer and
   Process Copilot in Orchestration steps. Record the answer in the ledger header.
2. Population = the developer portal CPM section (enumerate from its nav tree) plus the
   Process Management / AI pages on `celonis.com`. The docs behind the login are a
   separate population and count as `BLOCKED` until A4 is resolved.
3. Do not keyword-filter.

## Artefact mechanics

- The developer portal pages carry element-mapping tables (JSON ↔ BPMN XML), not full
  diagrams. Expect `E0-no-artefact` for many reference pages. Record them anyway.
- Process-mining views (process explorer, directly-follows graphs) are **not** BPMN. Name
  them as such when excluding (`E1-not-bpmn`).

## Known gotchas

- **Process mining vs process management.** Most Celonis AI content is mining or
  analytics flavoured (AgentC, "Process Intelligence"). It is AI *about* processes, the
  same category as SAP Signavio and BOC ADONIS (see "An emerging category" in
  `candidate-vendors.md`).
- `docs.celonis.com` links in Google results look public but redirect to a login.
  Do not record them as `E0`. They are `BLOCKED`.

## Spot checks performed by Pass 1

Spot checks only, not verdicts:

- `developer.celonis.com/.../elements_tasks`: opened, BPMN task-type list read.
- `celonis.com/platform/process-management`: opened, "AI-insertion points" sentence read.
- Two `docs.celonis.com` result links: both redirected to the Celonis ID login.

## RESUME

(empty)
