---
source: opentext
source_name: OpenText Process Automation (ex-AppWorks)
source_type: vendor site + developer docs
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: NO (operator ruling 2026-09-24, batch C1 rule-out B14/B10)
  C2_native_bpmn20: UNVERIFIED
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES
access: public
population_type: not established
population_estimate: 10
effort: small
needs_logged_in_browser: false
status: OUT-C1 (not surveyed; kept for audit trail)
---

## Why this file exists

C1 alone cannot produce `OUT`. **Recommendation: rule out at Gate 1**, unless the
deciding check below finds something.

## Criteria evidence

- **C1 NO-leaning**: https://www.opentext.com/products/process-automation (2026-09-24):
  "Create and scale applications faster with Developer Aviator for low-code, AI-assisted
  development". That is design-time AI. No AI step in a process was found.
- **C2 UNVERIFIED**: BPMN does not appear on the product page. The "Workflow Modeler
  Overview" docs (developer-qa.dev.ca.opentext.com, a **QA host** in the search index) were
  not opened.

## The deciding check

Open the production developer docs for Workflow Modeler (find via developer.opentext.com
nav, not the QA host): BPMN notation, and any AI/Aviator activity type?

## RESUME

(empty)
