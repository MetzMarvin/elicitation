---
n: 139
source: aletyx
source_name: Aletyx (Kogito AI add-ons, aletyx.ai)
title: "process.bpmn - the vendor's own Kogito example: an ad-hoc sub-process in which the AI task 'Aletyx Intelligence' orchestrates the human tasks"
url: https://github.com/aletyx/aletyx-kogito-ai-addons/blob/main/examples/quarkus/src/main/resources/process.bpmn
accessed: 2026-09-25
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "a valid BPMN 2.0 model, process id='process' name='process', containing an ad-hoc sub-process 'Loan Investigation' whose children are the AI task plus three user tasks (RiskAssessment, PropertyAssessment, ApplicantVerification); top level: one start event, two script tasks (Set Denial, Check Agreement), user task HumanReview, two diverging exclusive gateways and two end events; no pools/lanes, one empty laneSet"
bpmn_evidence_quote: "<adHocSubProcess id=\"_F86C1989-80CF-4170-AA29-9524EC4D37D8\" triggeredByEvent=\"false\" name=\"Loan Investigation\">"
ai_evidence: "an AI element sits inside the process: a task named 'Aletyx Intelligence' bound to the custom work item AletyxAI, placed INSIDE the ad-hoc sub-process together with the human tasks it drives"
ai_evidence_quote: "<task id=\"_597E1259-1738-4B1C-B363-875400A63087\" drools:taskName=\"AletyxAI\" name=\"Aletyx Intelligence\">"
artefacts:
  screenshot: 001_process.bpmn
  assets: [001_process.bpmn]
  bpmn_xml: [001_process.bpmn]
  archive: null
duplicate_of: null
access: public
capture_source: original-file
capture_quality: legible
capture_width_px: null
capture_method: codeload archive of branch main (repo_main.zip, 450877 B), file read as text on 2026-09-25; no browser render needed - the element is decisive in the XML
judgment: false
---

## What the artefact is

`examples/quarkus/src/main/resources/process.bpmn` of `github.com/aletyx/aletyx-kogito-ai-addons`,
branch `main`, 66 950 bytes, sha256 prefix `154f36c847982f6c`. It has a byte-identical twin at
`examples/springboot/src/main/resources/process.bpmn` (same hash, same size) - that twin is the
`E3-duplicate` row; the Kogito render `examples/quarkus/src/main/resources/META-INF/processSVG/process.svg`
(45 506 B) draws the same diagram (`<tspan>Aletyx Intelligence</tspan>` among its ten labels) and is the
second `E3-duplicate`.

Root element carries the BPMN 2.0 model namespace with the default (unprefixed) element form, so the
elements appear as `<process>`, `<adHocSubProcess>`, `<userTask>`, `<scriptTask>`, `<exclusiveGateway>`,
`<startEvent>`, `<endEvent>` - the `bpmn:` prefix is not used in this file.

## Observations (description only, no interpretation)

- `<process id="process" name="process">`; one empty `<laneSet>`; no pools, no lanes.
- Top level: `<startEvent id="_8454B237-...">`, `<scriptTask ... name="Set Denial">`,
  `<scriptTask ... name="Check Agreement">`, `<userTask ... name="HumanReview">`,
  two `<exclusiveGateway ... gatewayDirection="Diverging">` (each with a `default` flow),
  two `<endEvent>`.
- `<adHocSubProcess ... name="Loan Investigation">` with `<drools:metaData name="customAutoStart">`
  `false`, and children: `<task ... drools:taskName="AletyxAI" name="Aletyx Intelligence">`
  (id `_597E1259-1738-4B1C-B363-875400A63087`), `<userTask name="RiskAssessment">`,
  `<userTask name="PropertyAssessment">`, `<userTask name="ApplicantVerification">`.
- Companion work-item definition `global/aletyx-ai.wid` (15 468 B, sha256 `f19fbf171b6cd9bd`;
  byte-identical copy under `examples/springboot/global/`): `"name": "AletyxAI"`,
  `"category": "Aletyx AI"`, `"displayName": "Ad-hoc Intelligence"`, plus parameters
  `SkillResource, HumanRequired, PreHumanRequired, PostHumanRequired, MaxEvaluationLoops` and a
  base64 PNG icon. It is what puts the task on the modelling palette; it is not itself a process
  model.
- Two DMN files ship with the same examples (`eligible.dmn`, `underwriting-decision.dmn`) and four
  elsewhere in the tree - DMN 1.x decision models, judged `E1-not-bpmn` in their own ledger rows.
- README (same commit), verbatim: "From the palette, expand the **Custom Tasks -> Aletyx AI**
  category and ..." ; "| **Ad-Hoc Subprocess** | An AI orchestrator that drives a Kogito ad-hoc
  subprocess: picks the next user task to run ...".

## Notes for the researcher

This is the source's only artefact in which an AI-labelled element sits inside a process model -
found in the vendor's repository, not on the vendor's website. The website describes the same
mechanism in prose on `/enterprise-kogito/`, `/intelligent-process-automation/` and
`/aletyx-vs-bamoe-vs-apache-kie/` ("AI Agent nodes handle ad-hoc intelligent tasks inside
workflows"), but every BPMN diagram the site actually draws is AI-free; those three pages are
separate `UNCERTAIN` rows with their own ruling questions.

Nothing was excluded for being marketing material, small, simple, non-English or similar to another
item. The twin file and the SVG render were excluded only as byte-identical/re-serialised copies of
this same diagram (`E3-duplicate`).
