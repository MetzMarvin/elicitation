---
n: 323
source: flows-for-apex
source_name: Flows for APEX (FlowQuest; flowsforapex.org docs, flowquest.net, GitHub)
source_type: vendor docs
title: Flows for APEX v26.1 (Archived Draft)
url: https://flowquest.net/Flows4APEX261Features-old/
accessed: 2026-09-24
verdict: UNCERTAIN
needs_human_ruling: true
question: "The archived v26.1 draft announces AI-driven ad-hoc sub-processes and its runtime task list shows cases of the 'Autonomous Luggage Agent', but none of its six images shows an AI element inside a BPMN process - is the runtime task list an AI-in-process artefact to collect, or is this E2 because the AI appears only in the release-note prose?"
needs_visual_check: false
bpmn_evidence: BPMN 2.0 diagrams in the modeler (bpmn-js canvas with BPMN.io watermark), an async script task model and a user-task configuration; page prose names the constructs ("AI-Driven Adhoc Sub Processes and BPMN-Defined Agents")
bpmn_evidence_quote: "AI -Driven Adhoc Sub Processes and BPMN-Defined Agents*"
ai_evidence: the page announces that AI can now operate inside an ad-hoc sub-process, and its runtime task list shows live cases of the "Autonomous Luggage Agent"; no BPMN diagram on the page carries an AI element
ai_evidence_quote: "AI can now operate inside"
artefacts:
  screenshot: 011_261-autonomous-agent-task-list.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: poor
capture_width_px: 1333
capture_method: curl -L on the asset src read from the page DOM; six images enumerated and read at native resolution (this is the widest image that carries the page's AI evidence, 1333 px, below the 1400 px bar and not published larger)
---

## What the page shows

The archived draft of the Flows for APEX v26.1 feature page. Its release-notes prose
announces an AI feature: "AI -Driven Adhoc Sub Processes and BPMN-Defined Agents* AI can now
operate inside". The six artefacts it carries are: an animation of running flows, the AskFlo
explainer panel, an async script-task model ("approve payroll run" -> gateway -> "run
payroll"), a user task configured as an APEX Page call ("Enter Order"), a user task using an
APEX Approval definition ("Approve Promotion"), and a runtime task list. The task list is the
only artefact on the page that shows the AI feature in operation: it lists cases named
"Autonomous Luggage Agent - Case 646 - BA123456" and "Autonomous Luggage Agent - Case 648 -
Emily Thompson LHR-SIN (BA123456)" from the process "Lost Luggage Agent", alongside a "Manual
Luggage Agent" case from "Luggage Finder Workbench" and an "Assisted Luggage Agent" case.

## Observations (description only, no interpretation)

- **AI activity - function:** the page says AI "can now operate inside" an ad-hoc sub-process;
  the runtime list shows cases of an "Autonomous Luggage Agent" being initiated and running.
- **AI activity - element type:** no AI element is visible in any BPMN diagram on this page.
  The models shown are an ordinary script task (properties panel: Task Type "PL/SQL") and
  user tasks (Task Type "APEX Human Task" / APEX Page / APEX Approval). The AI appears as a
  task-list subject line and as release-note prose.
- **Authority - downstream:** not visible on the page for the AI; the task list entries carry
  a "Workflow" link per case.
- **Authority - data:** not visible on the page. The task list shows a case business reference
  and a due date only.
- **Authority - control:** not visible on the page.
- **Input provenance:** not visible on the page.
- **Guards present:** the task list carries a "Show expired tasks" filter and a due-date sort;
  no review gate for an AI decision is visible.
- **Prompt / model detail visible:** none on this page. The AskFlo panel here is the
  documented "Flo, the Flows for APEX AI advisor" summarising an unrelated iterations model
  ("A25f - Sequential Iterations with SubProcesses"), i.e. modeller assistance.

## Notes for the researcher

This is the archived draft of the page recorded as 002 (`flowquest.net/Flows4APEX261Features/`).
It is **not** a duplicate of it: the published version carries the AI artefact
(`ahsp-261-autonomous-def.png`, the autonomous AHSP definition), while this draft does not -
it carries the runtime task list instead. The two pages share no byte-identical image -
verified by SHA-256 over all six of this draft's assets against all five of the published
page's assets (ahsp-261-manual-def.png, ahsp-261-autonomous-def.png, 261-ai-dev-bundle.png,
261-dev-features.png, async-task-261.png): no hash collides. The judgement call this record
asks for is whether the runtime task list of an AI-driven agent process is an artefact worth
collecting when the underlying model on the same page is annotated Manual elsewhere in the
source.
