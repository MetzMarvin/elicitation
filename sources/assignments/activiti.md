---
source: activiti
source_name: Activiti (Alfresco / Hyland Process Automation; activiti.org, Hyland Connect)
source_type: open-source project + vendor community
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: NO (operator ruling 2026-09-24, batch C1 rule-out B14/B10)
  C2_native_bpmn20: YES
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES
access: public
population_type: enumerable
population_estimate: 5
effort: small
needs_logged_in_browser: false
status: OUT-C1 (not surveyed; kept for audit trail)
---

## Why this file exists

C1 alone cannot produce `OUT`. **Recommendation: rule out at Gate 1.**

## Criteria evidence

- **C1 NO-leaning**: two sweeps (2026-09-24, q24 and q25 in `search-protocol.md`) found no
  vendor material promoting AI inside Activiti BPMN processes. The only AI hit, opened at
  https://connect.hyland.com/t5/alfresco-forum/bringing-alfresco-content-and-workflows-into-the-ai-era-help-us/td-p/499497,
  is a community member's post (17 July 2026) about "securely feeding Enterprise Content and
  Workflow data into Vector Databases". That is AI about workflow data, not AI in a process.
- **C2 YES**: Activiti is a BPMN 2.0 engine (uncontested; forum threads on "service Task",
  "SubProcess" and "end error event" in the same result list).
- **C3 YES**, **C4 YES** (a historically very widely deployed engine, embedded in Alfresco).

## Entry points (only if ruled in)

- Alfresco Process Automation docs ("Alfresco Modeling Application",
  `alfresco.com/…/activiti-enterprise/docs`), Hyland Connect Alfresco blog

## RESUME

(empty)
