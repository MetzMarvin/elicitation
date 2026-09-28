---
source: scheer-pas
source_name: Scheer PAS (Designer docs + Academy AI tutorials)
source_type: vendor documentation
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: YES
  C2_native_bpmn20: YES
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES (operator ruling 2026-09-24, general C4 rule)
access: public
population_type: enumerable
population_estimate: 30
effort: small
needs_logged_in_browser: false
status: DONE (elicitation-6f, 2026-09-25; 14 doc spaces = 1333 pages, audit problems: none; 5 records written, 1 INCLUDE + 4 UNCERTAIN rulings; row n=68 superseded UNCERTAIN->INCLUDE per protocol clause "Deliberately in scope")
---

## Criteria evidence

- **C1 YES**:
  https://doc.scheer-pas.com/academy/latest/step-3-integrating-the-agent-to-the-process
  (2026-09-24): "You created the CaseAgent to execute process step Analyze customer
  request", then "Click Analyze customer request to open its execution model… drag & drop
  the agent's execute operation to the execution model".
  The AI tutorials overview says: "how to integrate your AI agent into a Designer process".
- **C2 YES**: the figure on the same page shows a BPMN 2.0 diagram: a start event "Start
  insurance case auto-processing", a user task "Enter insurance request", and a task
  "Analyze customer request". The page also points to "the chapters Modeling BPMN and
  Implementing Your Process in the Designer Guide".
- **C3 YES**: served anonymously. The tutorial states two product prerequisites, "The AI
  agent feature is only available in a Kubernetes setup" and "you need an account with an AI
  service provider". Neither gates the documentation.
- **C4 UNCLEAR**: Scheer is an established DACH BPM company, but no customer-base evidence
  was read. This falls under the general C4 rule proposed at B5–B7 in `OPERATOR-TODO.md`.

## Why this source matters for the taxonomy

The AI agent is **not** a BPMN element type. It is an operation inside the xUML
**execution model** that sits behind an ordinary BPMN task. From the diagram you cannot
tell that "Analyze customer request" is AI-bound. That is the **delegated-binding** mode,
already documented for UiPath (`notes/uipath-promotion-pattern/analysis.md`). Scheer PAS
is a second, independent instance of it.

**Consequence for artefact judging:** a BPMN diagram from this source will often show *no*
visible AI element, while the prose says the task runs an agent. **That is `UNCERTAIN`
with the binding quoted, never `E2`.**

## Entry points

- `https://doc.scheer-pas.com/academy/latest/ai-tutorials`: AI tutorials hub
- `/academy/latest/tutorial-1-using-an-ai-agent` and its steps: `preparations-ai-tutorial-1`,
  `step-1-creating-the-ai-agent`, `step-2-prompting-and-testing-the-ai-agent`,
  `step-3-integrating-the-agent-to-the-process`, `step-4-testing-the-process` (all
  extracted from the page nav)
- Designer Guide "Using AI Agents" (linked from the AI tutorials page as `/designer/`)
- Google result titles, not opened: "Using an AI Agent in an xUML Service", "Testing an
  AI Agent", "Microsoft Foundry AI Service Provider Reference", release notes PAS 25.3 /
  26.0
- Every page offers "View as Markdown" (`<page>.md`), which is useful for text extraction.

## Enumeration instructions

1. Enumerate the Academy "AI Tutorials" subtree and the Designer Guide "Using AI Agents"
   subtree from the left-hand navigation tree.
2. Also check the Designer Guide's "Modeling BPMN" chapter, which may contain AI-bound
   example processes.
3. Release notes (PAS 25.3, 26.0) are `E0` unless they carry a diagram. Record them.
4. Pin the docs version (the site selector showed `26.2`) and record it.

## Artefact mechanics

- Figures are PNG screenshots of the Designer (e.g. 1388×832), with `alt` equal to the file
  name (`grafik-YYYYMMDD-HHMMSS.png`). Alt text carries no information.
- Most figures are close-ups of the execution model (xUML) rather than the BPMN level.
  Name xUML figures as such when judging.

## Known gotchas

- A **Privacy Preference** cookie banner overlays screenshots. Do not accept it without
  the operator's permission. Scroll the figure clear of it or use element-cropped capture.
- The xUML vs BPMN distinction: capture the BPMN-level figure and the execution-model
  figure as a pair, because the binding is only visible in the second.

## Spot checks performed by Pass 1

- AI Tutorials hub, Tutorial 1 overview, and Step 3: opened. Step 3's first figure was
  viewed via screenshot.

## RESUME

(empty)
