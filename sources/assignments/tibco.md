---
source: tibco
source_name: TIBCO (ActiveMatrix BPM / BusinessEvents; docs.tibco.com)
source_type: vendor documentation
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

- **C1 NO-leaning**: the 9-result sweep `site:tibco.com BPMN AI OR agent OR agentic OR LLM`
  (2026-09-24) contains no AI material. The "agent" hits are **BusinessEvents inference
  agents** ("Adding and Configuring Process Agent Class"), a rule-engine concept. That is a
  false friend for keyword sweeps.
- **C2 YES**: https://docs.tibco.com/pub/amx-bpm/4.3.0/doc/html/bpmhelp/GUID-18D8D888-FCAE-417C-9682-32ADD11EBBAD.html:
  "This release of TIBCO Business Studio (the TIBCO ActiveMatrix BPM design environment) is
  based on the BPMN Version 2.[0]".

## Note

ActiveMatrix BPM is a legacy line. TIBCO is now part of Cloud Software Group. A successor
product with AI in processes was not searched for. If ruled in, search for one first.

## RESUME

(empty)
