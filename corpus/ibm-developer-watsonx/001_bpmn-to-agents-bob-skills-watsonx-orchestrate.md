---
n: 765
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Turn BPMN diagrams into production-ready agents with Bob skills and watsonx Orchestrate — the anchor tutorial: a BPMN 2.0 order process that Bob converts into a watsonx Orchestrate agent"
url: https://developer.ibm.com/tutorials/bpmn-to-agents-bob-skills-watsonx-orchestrate/
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "The page's artefact is a BPMN 2.0 process model with no AI element inside it; the AI relationship is that the model is the INPUT that Bob converts into a watsonx Orchestrate agent ('this diagram becomes an agent', not 'this diagram contains an agent'). Does that count as an AI-in-BPMN artefact for the corpus, or is it a process-to-agent substitution that the corpus should record as no AI element inside the process (E2-no-ai-element)?"
needs_visual_check: false
bpmn_evidence: "image1.png (alt=\"bpnm\") is a rendered BPMN 2.0 diagram and its source XML ships in the linked companion repository: <bpmn:process name=\"Order Processing Workflow\"> with <bpmn:startEvent name=\"Order Received\">, <bpmn:task name=\"Validate Order\">, <bpmn:exclusiveGateway name=\"Items in Stock?\">, <bpmn:serviceTask name=\"Process Payment\">, <bpmn:userTask name=\"Notify Customer\">, <bpmn:task name=\"Ship Order\">, <bpmn:sendTask name=\"Send Confirmation\"> and two <bpmn:endEvent> nodes (Order Complete / Order Cancelled); the picture matches the XML label for label (start circle, X-diamond gateway with Yes/No flows, gear/person/envelope task markers, double-circle end events)"
bpmn_evidence_quote: "The business process is defined using BPMN notation and includes a clear inventory decision that determines whether an order is completed or canceled."
ai_evidence: "no AI element is drawn inside the process: the page's AI content is the tooling around the model — Bob reads the .bpmn and generates a watsonx Orchestrate agent, flow and Python tools. Verbatim: \"Bob analyzes the BPMN model and converts the business process into a working watsonx Orchestrate solution.\" and \"Use IBM Bob skills to transform a BPMN business process into a fully working watsonx Orchestrate agent.\""
ai_evidence_quote: "Use IBM Bob skills to transform a BPMN business process into a fully working watsonx Orchestrate agent."
artefacts:
  screenshot: 001_bpmn-order-process-diagram.png
  assets: [001_bpmn-order-process-diagram.png, 001_BPMN-order-process.bpmn, 001_bpmn-architecture-of-the-solution.png]
  bpmn_xml: [001_BPMN-order-process.bpmn]
  archive: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: "figures fetched at their native asset URLs (developer.ibm.com/developer/default/tutorials/<slug>/images/image1.png); the .bpmn XML fetched from the raw.githubusercontent URL of the link the tutorial itself gives (github.com/IBM/oic-i-agentic-ai-tutorials/blob/main/bpmn/BPMN-order-process.bpmn)"
judgment: true
---

## What the artefact is

The anchor tutorial of the source, published 2026-04-09, updated 2026-07-27
(`publish_date` / `updated_date` from the site's own content API). It carries **two** drawn
figures and one downloadable model:

- `images/image1.png`, alt text `bpnm` — the BPMN diagram of the order process, 39 steps in
  the tutorial are Bob IDE screenshots, this is the only process drawing.
- `images/image2.png`, alt text `architecture` — the solution architecture: a rounded `User`
  node, an `Order Processing Agent` box, an `Order Processing Flow` box and six
  snake_case tool boxes (`validate_order`, `check_inventory`, `process_payment`,
  `ship_order`, `send_notification cancellation`, `send_notification confirmation`). This is
  a **box diagram, not BPMN** — no events, no gateways, no sequence flows. Judged
  `E1-not-bpmn` where it stands alone; here it is recorded as part of the same page's capture
  because the BPMN figure sits above it.
- `BPMN-order-process.bpmn` (2 994 B, sha256 prefix `309d7230a8ff28e9`), linked from the
  tutorial (`Download the file BPMN-order-process.bpmn into this folder`) and served from the
  companion repository `github.com/IBM/oic-i-agentic-ai-tutorials` under `bpmn/`.

## Observations (description only, no interpretation)

- The `.bpmn` file is a valid BPMN 2.0 model (`<bpmn:definitions
  xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL">`, with a `bpmndi:BPMNDiagram`
  section). Elements, in document order: `startEvent` *Order Received*; `task` *Validate
  Order*; `exclusiveGateway` *Items in Stock?* with sequence flows named *Yes* and *No*;
  `serviceTask` *Process Payment*; `userTask` *Notify Customer*; `task` *Ship Order*;
  `sendTask` *Send Confirmation*; `endEvent` *Order Complete*; `endEvent` *Order Cancelled*.
- **No AI element is present in the model.** No `serviceTask` named for an AI/LLM/agent, no
  vendor extension attribute, no AI-labelled task. The only AI-bearing nouns on the page are
  Bob, watsonx Orchestrate, the MCP servers and the generated `Order Processing Agent`.
- The page's own framing of the notation, verbatim: "Turning business process diagrams into
  working software usually takes time, specialized skills, and many handoffs between teams."
  and "The business process is defined using BPMN notation and includes a clear inventory
  decision that determines whether an order is completed or canceled."
- The tutorial's 39 images beyond `image1`/`image2` are Bob IDE screenshots (permission
  dialogs, task lists, test reports) — UI captures, not process drawings.
- Companion repo tree (GitHub `git/trees/main?recursive=1`, 1 405 entries, `truncated:
  false`): exactly **one** `.bpmn` file in the whole repository — `bpmn/BPMN-order-process.bpmn`,
  2 994 B. No `.dmn`, no `.bar`.

## Notes for the researcher

- **This is the source's central artefact and its central ambiguity.** The BPMN model is
  clean BPMN 2.0 and it is *decisive* evidence of C2 for the source, but nothing AI-shaped is
  inside the process: the AI is the *consumer* of the model. Gate 1 already ruled (B3,
  2026-09-24) that process-to-agent substitution counts for C1 at the source level; whether it
  also yields an artefact for the corpus is the ruling question above, which the assignment
  file says explicitly must not be resolved by the agent (`prompts/02b`, "Known gotchas").
- The `.bpmn` file itself is a separate ledger row (surface: the companion repository), with
  the same question attached, because the assignment lists repo files as "artefacts in their
  own right".
- If the researcher rules that a process-model-as-input counts, this row is the corpus's
  cleanest example of the substitution mode and the `.bpmn` should be promoted; if not, the
  row becomes `E2-no-ai-element` with the quotes above as the dismissal evidence.
