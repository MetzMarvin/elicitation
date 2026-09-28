---
source: cib-seven
source_name: CIB seven (Camunda 7 fork — manual, examples and tutorials)
source_type: vendor documentation
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: YES
  C2_native_bpmn20: YES
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES (operator ruling 2026-09-24, general C4 rule)
access: public
population_type: enumerable
population_estimate: 60
effort: medium
needs_logged_in_browser: false
status: DONE (elicitation-74)
---

## Criteria evidence

- **C1 YES** — https://docs.cibseven.org/manual/latest/reference/connect/ai-agent-connector/
  (2026-09-22): "LLM agent loop — sends your message plus a system prompt to an
  OpenAI-compatible model and returns the model's text answer." Same page: "Tools (function
  calling) — the model can call Java @Tool classes and MCP servers. A built-in
  ProcessStarterTool lets the agent launch a CIB seven process by key and react to its
  result." And: "Chat memory — keep a multi-turn conversation across BPMN steps".
- **C2 YES** — the connector is documented in the engine reference under
  `reference/connect/ai-agent`, i.e. a runtime connector bound to BPMN activities, and CIB
  seven is a fork of the Camunda 7 BPMN 2.0 engine.
- **C3 YES** — `docs.cibseven.org` served anonymously.
- **C4 UNCLEAR** — CIB seven is the maintained continuation of Camunda 7 after Camunda ended
  Camunda 7 support, published by CIB (a German vendor), with an enterprise edition and
  public pricing. That is a real market position, but no customer-base or
  practitioner-discourse evidence was actually read. Mirrored in `OPERATOR-TODO.md` (B5).
  **Recommendation: include** — Camunda 7 has a very large installed base, so its successor
  is by construction "actively discussed".

## Entry points

- `https://docs.cibseven.org/manual/latest/reference/connect/ai-agent-connector/` — the AI
  Agent Connector reference (the AI-in-process feature)
- `https://docs.cibseven.org/manual/2.2/webapps/modeler/user-guide/bpmn-ai-chat/` — the
  Modeler "BPMN AI Agent" (the design-time feature; see the warning below)
- Manual nav observed 2026-09-22: Introduction, Download, Licenses, Implemented Standards,
  Architecture, Extensions, Public API, **User Guide**, Process Engine (Concepts, Delegation
  Code, Expression Language, External Tasks, **Connectors**, Process Versioning), Database,
  History, **Examples & Tutorials**
- **"Examples & Tutorials"** is the highest-yield section — expand it fully
- Sibling pages confirmed by `site:` sweep: "AI Agent Connector", "BPMN AI Agent", "Chat
  Memory", "Web Modeler and AI Features in CIB seven 2.2", "Enterprise features",
  "Processes", "CIB seven 2.2.0 EE — Release Notes"
- Check `https://docs.cibseven.org/sitemap.xml` before walking the nav

## Enumeration instructions

1. Enumerate the whole manual for **one** version. The docs expose both `/manual/latest/`
   and `/manual/2.2/` and the same page exists under both. Pin one, record it, and do not
   mix. The other version is not an `E3-duplicate` — it is simply out of scope for the run.
2. Include the release notes: CIB seven ships AI features incrementally and names them there.
3. Include "Examples & Tutorials" in full.

## Artefact mechanics

- Docusaurus-style docs: clean text, good headings.
- The AI Agent Connector page uses a **comparison table**, not a diagram. Table text is good
  evidence of what the element does, but it is not itself a process artefact — a page with
  only a table and no diagram is `E0-no-artefact`, not `INCLUDE`. Read before judging.
- Look for the connector's element template (JSON); it names the bindable properties.

## Known gotchas

- **This source contains both kinds of AI feature, and the vendor labels them itself.** The
  AI Agent Connector page tabulates the distinction explicitly: the connector is
  "Runtime — executes during a process instance", while the Modeler wizard is
  "Design-time — helps you author BPMN". A page about the Modeler wizard is the
  `E2-no-ai-element` case; quote the vendor's own "Design-time" label when dismissing it.
  **This is the cleanest worked statement of that distinction found anywhere in the sample —
  use it as the reference case when judging other sources.**
- CIB seven is a **Camunda 7 fork**. Shared lineage means diagrams may resemble Camunda's.
  That is never `E3-duplicate`; never dedupe across sources.
- `cibseven.org` (marketing, incl. Pricing) and `docs.cibseven.org` (manual) are different
  hosts. Enumerate both or state which you scoped to.

## Spot checks performed by Pass 1

Spot check only, not a verdict:

- `/manual/latest/reference/connect/ai-agent-connector/` — opened; the runtime/design-time
  comparison table, the tools/RAG/chat-memory feature list and the ProcessStarterTool were
  all read from the rendered page.

## RESUME

(empty — census complete 2026-09-25)

## Completion (elicitation-74, 2026-09-25)

Population **591** = 467 pages of `docs.cibseven.org/manual/latest/` (the pinned version's
global sidebar; the host has no sitemap) + 124 urls of `cibseven.org` (Yoast sitemap index:
page 80, academy 12, galleryui 28, category 4; de/en/es/pt). Rows 591; `audit.py` →
`problems: none`.

Verdicts: **INCLUDE 6, UNCERTAIN 3, EXCLUDE 582** (E0 383 / E1 104 / E2 83 / E3 12),
judgement exclusions 22 (3.7 %). No blockers.

Collected (records + captures in `corpus/cib-seven/`):

| n | page | artefact | verdict |
|---|---|---|---|
| 97 | `reference/connect/ai-agent-connector/getting-started/` | published BPMN 2.0 XML, `camunda:modelerTemplate="org.cibseven.connect.ai.agent"` | INCLUDE |
| 409 | `webapps/cockpit/bpmn/process-instance-chat/` | rendered BPMN: pools "AI Process" / "Human in the AI Agent Loop", `ai-agent-with-human` | INCLUDE |
| 443 | `webapps/modeler/user-guide/bpmn-ai-chat/` | Modeler canvas with the AI Agent element template *applied* on a service task | INCLUDE |
| 468 | `cibseven.org/` | hero: Modeler + "CIB SEVEN - AI AGENT" template panel over a BPMN canvas | INCLUDE |
| 473 | `cibseven.org/blog/` | teaser: "BPMN AI Agent — Review changes" panel over a BPMN diagram | INCLUDE |
| 506 | `cibseven.org/en/online-session-preview-cibseven-2-2/` | session cover: "BPMN AI Agent" panel over a BPMN model | INCLUDE |
| 96 | conn. `examples/` | 4 connector-XML fragments, no enclosing `serviceTask` | UNCERTAIN |
| 100 | conn. `rag/` | `cibseven-knowledge-ingestor` connector XML, no enclosing task | UNCERTAIN |
| 474 | `cibseven.org/casestudy/` | BPMN token-flow with the tokens held by a robotic hand | UNCERTAIN |

Notes for the researcher: (1) the "BPMN AI Agent" Modeler page (443) was collected rather
than dismissed under the design-time rule — its figures show the AI Agent element template
**applied to a service task inside a process**, i.e. the runtime binding, not just the wizard.
(2) `webapps/modeler/user-guide/form-ai-chat/` (448) is the E2 case the assignment predicts,
with the design-time label quoted; read strictly it has no BPMN artefact at all (E0), which
is flagged in its ledger evidence. (3) 47 pages publish BPMN 2.0 XML in code blocks → E2,
XML quoted; a first draft had them as E0 and was corrected. (4) Cockpit screenshots that
render the process canvas are classed E2 (the canvas *is* BPMN); pure UI screenshots are E1.
