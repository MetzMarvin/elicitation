---
source: gbtec
source_name: GBTEC (BIC Process Design, Work Orchestrator, "Arty")
source_type: vendor site
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: NO (operator ruling 2026-09-24)
  C2_native_bpmn20: YES (Process Design) / UNVERIFIED (Work Orchestrator)
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES
access: public
population_type: enumerable
population_estimate: 25
effort: small
needs_logged_in_browser: false
status: OUT-C1 (not surveyed; kept for audit trail)
---

## Criteria evidence

- **C1 UNCLEAR**: https://www.gbtec.com/company/news-article/arty-ai-enhanced-process-transformation/
  (release dated 9 April 2024): "Arty features an AI Modeler® that instantly generates
  process models in various notations" (design-time). But also: "As a 'Digital Worker,'
  Arty will collaborate side by side with process stakeholders ('Human Workers')". And
  https://www.gbtec.com/webinars-events/ai-in-pex-od/: "no-code AI and agentic automation
  are reshaping business operations".
- **C2**: BPMN material is abundant for Process Design (result titles "BPMN 2.0 Leitfaden",
  "Process modeling with BPMN 2.0" poster). **Work Orchestrator** (the execution product with
  "Intelligent Document Processing") was not shown to be BPMN.
- **C3 YES**, **C4 YES** (Carlyle-backed German BPM vendor; the page mentions "Carlyle to
  invest in business software vendor GBTEC").

## The deciding check

Is there a Work Orchestrator workflow with an AI/IDP/agent step, and is it drawn in BPMN?
Yes to both flips C1 to YES. If the AI is only Arty (modelling assistance), recommend out.

## Entry points

- The two pages above; `…/gbtec-work-orchestrator/document-processing/`
- `academy.gbtec.com` course "Meistern Sie KI-gesteuertes BPMN mit Arty" (not opened; may
  need an account, in which case mark it `BLOCKED`)
- German page "Next-Level BPM: Mit diesen KI-Funktionen gelingt Ihre…" (not opened)

## RESUME

(empty)
