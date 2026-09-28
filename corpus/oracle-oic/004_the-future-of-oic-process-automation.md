---
n: 9
source: oracle-oic
source_name: Oracle Integration blog (blogs.oracle.com/integration)
source_type: vendor blog
title: The future of OIC Process Automation
url: https://blogs.oracle.com/integration/the-future-of-oic-process-automation
accessed: 2026-09-24
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "figure 3 (004_figure-3-invoice-before-after.png, 1440x968) is captioned 'The same invoice process before and after': the 'Before' panel is a BPMN 2.0 process model of supplier-invoice handling (start event circle, thick end event circle, two lanes labelled 'AP lane' and 'Approver lane', nine rounded-rectangle tasks, two gateway diamonds labelled 'ok?' and '>10k?', dashed exception sequence flows), the 'After' panel replaces it with an agent-led architecture. The prose names BPMN elements verbatim. Confirmed by eye in the visual pass of 2026-09-24."
bpmn_evidence_quote: "every branch is a gateway, every call to another system is a service task, every rule is a decision table, every human step is a task in a queue"
ai_evidence: "the two-patterns paragraph is the AI element: an agent invoked as a step inside a deterministic flow, versus an agent that holds control of a probabilistic flow; figure 1 shows an 'agent' step in the deterministic lane, figure 3's 'After' panel is the agent-led variant. OIC Agent is described as 'configured with instructions that define the agent, a written procedure for the process it runs, a model, and the set of tools it is permitted to use'."
ai_evidence_quote: "deterministic flows, which increasingly invoke an agent as a step, and probabilistic flows, where the agent holds control"
artefacts:
  screenshot: 004_figure-3-invoice-before-after.png
  archive: 004_the-future-of-oic-process-automation.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1440
capture_method: same-origin fetch of the WordPress asset URLs with the resize suffix stripped (figure-3-invoice-before-after-1, figure-2-agent-led-architecture-2, figure-1-two-patterns, image-12), source served image/jpeg, stored here transcoded to PNG; page HTML archived with the same fetch
---

## What the page shows

An essay-length position paper on where OIC Process Automation is going. It opens on the standards
history ("BPMN turned a whiteboard sketch into an executable model: a lane for every owner, a diamond
for every decision, and a task for every step"), states the thesis that agents change "what a process
model is: no longer a description of the path, but a description of the goal, the surrounding context,
the tools the agent may use and the limits it must respect", and then names the two patterns that the
assignment's C1 question turns on:

> "In customer estates today we see two patterns: deterministic flows, which increasingly invoke an
> agent as a step, and probabilistic flows, where the agent holds control. We expect both to converge
> on one architecture, and we are building Oracle Integration (OIC) to be the platform for it."

The paper's own worked example is a BPMN invoice process: "A worked example: accounts payable invoice
processing. Take a typical BPMN model for supplier invoices." Figure 3 is captioned "The same invoice
process before and after." Four images are published: `figure-1-two-patterns` (Figure 1, "The two
patterns differ in one thing: who holds control of the flow"), `figure-2-agent-led-architecture`,
`figure-3-invoice-before-after` and a decorative header image.

## Observations (description only, no interpretation)

- **AI activity - function:** two readings are present on the same page. In the deterministic pattern the
  agent is a step inside a flow the process engine owns; in the probabilistic pattern the agent owns the
  flow. Both are stated in the paragraph quoted above.
- **AI activity - element type:** the page describes the agent at architecture level, not as a BPMN
  element: "OIC Agent, instructions and skill ... Agents, configured with instructions that define the
  agent, a written procedure for the process it runs, a model, and the set of tools it is permitted to
  use." What the modeller looks like on the canvas is not shown.
- **Authority - downstream:** the tools the agent is permitted to use ("the set of tools it is permitted
  to use"); the deterministic side keeps "Deterministic integrations: OIC Integrations: the orchestration
  engine, hundreds of adapters, mapping, error handling, scheduling and event handling."
- **Authority - control:** bounded by the business, not by the prompt: the agent asks "for help at the
  points the business chooses", and the model is a "description of the goal ... and the limits it must
  respect".
- **Guards present:** an explicit human-in-the-loop construct is named as a separate product surface
  ("the components, with waiting state held by the HITL workflow and resume flows triggered on its
  outcome"); no prompt text, turn limits or model identifiers are shown on this page.
- **Input provenance:** not an artefact in the corpus sense - this page is a position paper. The three
  figures are: Figure 1, a stylised two-lane comparison of the two patterns whose deterministic lane
  carries an "agent" labelled step (notation is illustrative, not a full BPMN 2.0 model); Figure 2, an
  architecture box diagram of the agent-led platform (boxes and arrows, not BPMN); Figure 3, the
  before/after invoice process, where the "Before" panel is a BPMN 2.0 process model and the "After"
  panel is the agent-led replacement.
- **Figure-by-figure reading (visual pass, 2026-09-24).** *Figure 3, "Before" panel:* BPMN 2.0. The
  sequence reads "receive -> extract -> validate vendor -> 3-way match", then the gateway diamond "ok?"
  whose "no" branch drops to the "clerk resolves" task and returns to "validate vendor", then the
  diamond ">10k?" leading to the "Approver lane" tasks "manager" and "controller" (dashed flows),
  and on the "AP lane" the tasks "post" and "pay" ending in the thick end-event circle. No AI/LLM
  element appears inside this panel. *Figure 1, "Deterministic":* "receive -> validate -> agent: resolve
  -> approve -> post" with a dashed arrow from the "agent: resolve" pill down to a dashed
  "exception queue" box; *"Probabilistic":* a purple pill "agent / follows the procedure" feeding
  "receive validate approve post", captioned "the same steps, now tools the agent calls in the order the
  case needs". Boxes and arrows, no BPMN events, gateways, lanes or pools. *Figure 3, "After" panel:*
  not BPMN - an architecture diagram with two top boxes ("MCP App in the chat client": "AP submits the
  invoice. Approvers see the case and act on it. Both via tools."; "AP agent": "Skill/Instruction: post
  every valid supplier invoice within terms. Never post twice, never over the threshold without approval.
  Run the match. If it fails, find out why. No PO: search open POs by vendor and amount. One fit, use it.
  Several, ask AP. Partial delivery: match what was received. Duplicate: hold." and "Judgement: read the
  invoice, choose the path, frame the exception for a person."), a "MCP Gateway" band ("Exposes the six
  AP tools to this agent and to the app, and nothing else. Masks bank details in responses. Flags unusual
  amounts to finance. Logs every call, from agent or person, under the invoice id."), and six tiles
  "Integration: submit" / "Integration: match" / "Decisions" / "Knowledge Base" / "HITL" / "Integration:
  post". *Figure 2:* architecture box diagram ("Agent skill and instructions", "Agent", "Tool governance
  (MCP Gateway)", then "Integrations", "HITL", "Knowledge base", "Decisions", "MCP Apps", "External MCP
  servers"). *Hero banner* (`004_hero-banner.png`): decorative header image, no process content.

## Notes for the researcher

This is the anchor page named in the assignment. **The ruling question is settled: Gate 1 ruling B3
(2026-09-24) says process-to-agent substitution counts as C1 for this source**, so both readings on this
page are positives and the record stands as INCLUDE with no open question. The visual check on all four
images was completed on 2026-09-24 by worker `elicitation-6f` and is written up under "Figure-by-figure
reading" above.

One point for the abstraction step, stated as description and not as a verdict: within figure 3 the BPMN
2.0 panel is the "Before" state and it contains **no** AI element; the AI element (the AP agent) is in
the "After" panel of the same figure and in the article prose. The diagram that carries the AI is
therefore the non-BPMN half of the figure, and the BPMN half is the process the agent replaces.

Supporting captures, not themselves records: `004_figure-1-two-patterns.png` (1440x520),
`004_figure-2-agent-led-architecture.png` (1440x980), `004_hero-banner.png` (1087x613, decorative
header image, no process content).
