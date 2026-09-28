---
source: pegasystems
source_name: Pegasystems (Pega Platform docs: Agent Steps, Case Lifecycle, Process Modeler)
source_type: vendor documentation
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: YES (AI in the process model; whether that model is BPMN is C2)
  C2_native_bpmn20: NO (operator ruling B12 2026-09-24: Pega Case Lifecycle / Process Modeler flow shapes; BPMN import only)
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES
access: public
population_type: enumerable
population_estimate: 30
effort: medium
needs_logged_in_browser: false
status: OUT-C2 (not surveyed; kept for audit trail)
---

## Why this file is provisional

C1 is YES: Pega places AI agents directly in the process model. **C2 is the open question**:
Pega models work as a Case Lifecycle (stages and steps) and as Process Modeler flows built
from Pega-specific shapes, and it treats BPMN as an import format. See ruling **B12** in
`OPERATOR-TODO.md`. If the ruling is "not BPMN", this becomes the clearest C2 `OUT` in the
record: an AI-in-process vendor excluded on notation alone.

## Criteria evidence

- **C1 YES**: https://docs.pega.com/bundle/ai-pega/page/platform/gen-ai/agent-steps.html
  (2026-09-24): "Agent Steps incorporate AI agents directly into your Case Type workflow.
  When a Case reaches an Agent Step, the assigned Agent performs the defined action in the
  background". The page has a figure captioned "Agent Step in the Case lifecycle".
- **C2 UNCLEAR (leans NO)**:
  - https://docs.pega.com/bundle/blueprint/page/platform/blueprint/blueprint-case-types.html:
    "You can also create Case Types by uploading BPMN files with your existing business
    processes", followed by "Save and Regenerate Case Lifecycle". BPMN comes in and is
    converted to Stages and Steps.
  - https://docs.pega.com/bundle/platform/page/platform/case-management/assignment-shapes-processes.html
    (Pega Platform '26): "Assignment shapes represent tasks that users complete in a
    Process". Shapes come from "Case Lifecycle Designer" or "Process Modeler". The page
    does not mention BPMN. The shape icon is a rounded rectangle, which is ambiguous.
- **C3 YES**: docs.pega.com is anonymous. "Register / Log in" is optional.
- **C4 YES**: Pega is a major enterprise BPM/case-management vendor.

## Entry points

- The Agent Steps page (anchor)
- Google result titles, not opened: "Optimizing work with Agents", "Automating work by
  running an Agent", "Supporting users with [GenAI]", "Comparing Pega GenAI features",
  "Steps in a Case Lifecycle", "Case Lifecycle elements", "Process shapes", "Configuring
  complex Processes" (**404s under `/bundle/ai-pega/`**, see gotchas)
- Process-mining pages that mention BPMN ("Drawing a BPMN reference model", "Saving a Process
  Map as a BPMN reference model") belong to Pega Process Mining. They are mining reference
  models, not executable processes.

## Enumeration instructions

Only if B12 rules C2 in: enumerate the `gen-ai` agent pages plus the Case Management
"Process shapes" subtree from the docs table of contents (not from Google). Judge every
figure individually for notation. A Case Lifecycle stage/step view, if C2 is ruled in for
Process Modeler only, is `E1-not-bpmn` and should be named "Pega Case Lifecycle".

## Artefact mechanics

- Docs are HTML. Content loads after a few seconds. Shape icons are small PNGs (~90×46).
- Figures sit inside the page body. Image `alt` text was empty on the pages checked.

## Known gotchas

- **Google's index is stale.** Several URLs under `/bundle/ai-pega/page/platform/case-management/`
  return "We've been doing some housecleaning" 404s. The live equivalent sits under
  `/bundle/platform/`. Navigate from the docs TOC.
- **On-site search (`docs.pega.com/search`) froze the browser renderer** (CDP timeout at
  45 s) on 2026-09-24. Avoid it, or run it in a disposable tab.

## Spot checks performed by Pass 1

- Agent Steps page: opened, C1 quote read.
- Blueprint "Configuring Case Types": opened, BPMN-import sentences read.
- "Assignment shapes in Processes": opened, text read, one screenshot of the shape icon.

## RESUME

(empty)
