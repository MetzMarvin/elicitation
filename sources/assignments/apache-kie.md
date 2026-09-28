---
source: apache-kie
source_name: Apache KIE upstream (jBPM / Kogito / Drools documentation)
source_type: open-source project documentation
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: NO (operator ruling 2026-09-24, batch C1 rule-out B14/B10)
  C2_native_bpmn20: YES
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES
access: public
population_type: enumerable
population_estimate: 10
effort: small
needs_logged_in_browser: false
status: OUT-C1 (not surveyed; kept for audit trail)
---

## Why this file exists

C1 alone cannot produce `OUT`, so a C1-failing source keeps a provisional file.
**Recommendation: rule out at Gate 1.** The expected yield is zero. See `candidate-vendors.md`
row 31.

## Criteria evidence

- **C1 NO-leaning**: the only AI material in a 10-result sweep (`site:kie.apache.org OR
  site:jbpm.org OR site:kie.org AI OR LLM OR agent BPMN`, 2026-09-24) is
  https://kie.apache.org/docs/10.2.x/drools/drools/pragmatic-ai/index.html: "you can
  integrate Machine Learning (ML) with Drools by using PMML files with Decision Model and
  Notation (DMN) models". That is ML in DMN decisions, not AI in a BPMN process.
- **C2 YES**: jBPM/Kogito are BPMN 2.0 engines (the "Kogito tooling for … BPMN
  visualization" and jBPM documentation results; no page opened for this, since it is
  uncontested).
- **C3 YES**, **C4 YES** (widely used engine, the basis of Red Hat PAM and IBM BAMOE).

## Entry points (only if ruled in)

- `kie.apache.org/docs/…/kogito`, `docs.jbpm.org` (html_single), `kogito.kie.org`
- The downstream AI add-ons live in `aletyx.md` and `ibm-bamoe.md`, not here.

## Enumeration instructions

Only if ruled in: search the single-page jBPM and Kogito docs for AI, LLM, agent, PMML and
"prediction service" (jBPM has a historical prediction-service API for task outcomes, which
would be a genuine, older AI-in-BPMN case). Record every hit.

## RESUME

(empty)
