---
source: atamya
source_name: Atamya (Agentic PIM with embedded BPMN engine)
source_type: vendor site
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: YES
  C2_native_bpmn20: YES
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES (operator ruling 2026-09-24, general C4 rule)
access: public
population_type: sitemap census (robots.txt -> sitemap_index.xml -> 9 Yoast sub-sitemaps)
population_estimate: 496
effort: small
needs_logged_in_browser: false
status: DONE (elicitation-3a, 2026-09-24 - census complete, audit problems: none)
---

## Criteria evidence

- **C1/C2 YES**: https://www.atamya.com/en/agentic-pim/ai-powered-workflows/ (2026-09-24):
  AI "operates directly from within the process itself – as a native service task,
  orchestrated by a full-fledged BPMN engine". Also: "It's a BPMN service task – just
  like 'Active Object,' 'Edit Attribute Value,' or 'Synch with Shopware'".
- **C4 UNCLEAR**: a German PIM vendor. BPMN is embedded in a PIM product. See the general C4
  rule (B5–B7).

## Entry points

The anchor page ("See Our AI Workflow Live" may be a video or demo). "ATAMYA AI Foundations"
and "KI trifft auf PIM" (atamya.com/agentic-pim) were not opened.

## DONE

Census finished 2026-09-24 (agent elicitation-3a). 496/496 URLs judged, `tools/audit.py
atamya` prints `problems: none`. Result: 9 INCLUDE, 3 UNCERTAIN, 484 EXCLUDE
(E0 464 / E1 14 / E2 2 / E3 4), 0 BLOCKED; judgement-exclusion share 3.2%.

- 12 records in `corpus/atamya/` (001-012), each with the native asset(s) and a
  `.page.html` archive of the fetched body.
- The three `needs_human_ruling` questions are Q1 (notation: stylised BPMN-derived
  marketing render) and Q2 (AI element not visible in an unlabelled service task); they
  are written out verbatim in the ledger rows n=208, n=246, n=277 and in the record
  frontmatter of 001, 005, 006.
- Capture quality: 10 records at 640-1281 px (`poor` against the 1400 px bar), 2 at
  1804/1805 px (`legible`). The vendor never publishes a larger variant - checked in the
  page `srcset`, which offers only a 300 px thumbnail alongside the original.
- No blockers: every page loaded without login, captcha or interstitial.

## RESUME

(none - census complete; not a RESUME stop)

