---
source: sap-signavio
source_name: SAP Signavio (Process Transformation Suite — AI agent governance)
source_type: vendor site
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: NO (operator ruling 2026-09-24, batch C1 rule-out B14/B10)
  C2_native_bpmn20: YES
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES
access: public
population_type: enumerable
population_estimate: 30
effort: small
needs_logged_in_browser: false
status: OUT-C1 (not surveyed; kept for audit trail)
---

## Why this file exists even though C1 is NO

Same reason as `boc-group-adonis.md`: C1 is a judgement criterion and cannot produce an
`OUT` on its own, so a vendor failing only C1 is `UNCLEAR-NEEDS-RULING` and keeps a
provisional assignment file. See ruling **B10** in `OPERATOR-TODO.md`.

Unlike ADONIS, I am **not** recommending rejection outright — one sentence on the anchor
page could flip it. See "The wrinkle" below.

## Criteria evidence

- **C1 NO, on positive evidence** —
  https://www.signavio.com/highlights/ai-agent-excellence/ (2026-09-23). The four named
  capabilities are "Identify AI Agent Opportunities", "Design and Build AI Agents", "Infuse
  Context into AI Agents", "Control Agentic Execution". The decisive sentence is:
  "Design and deploy AI agents **using the platform of your choice**" — Signavio does not
  host the agent. Its role is upstream ("SAP Signavio solutions help you identify where
  exactly in your processes you can gain the most value from leveraging AI agents") and
  downstream ("Mine AI agent behavior to ensure ongoing compliance and measurable
  outcomes"). Neither is an AI element executing inside a BPMN process.
- **C2 YES** — Signavio is a BPMN-notation vendor of long standing. Evidence from the same
  page's own footer: "Free BPMN 2.0 poster", "Free BPMN 2.0 and DMN 1.0 Poster",
  "BPMN 2.0 Insights".
- **C3 YES** — served anonymously; "Free Trial" and "Request a demo" are optional CTAs
  beside free content, not gates on it.
- **C4 YES** — SAP. Also self-reported: "SAP Signavio has been positioned as the Most
  Valuable Pioneer in QKS's AI Matrix assessment."

## The wrinkle that must be checked before ruling

One capability line on the anchor page reads:

> "Control your business process execution, carried out by your employees and AI agents"

A process model whose **performers** include AI agents is arguably AI-in-BPMN at model
level. That is structurally the same claim Trisotech makes in "BPMN User Tasks for Humans
and AI Agents" — and Trisotech qualifies (row 12).

**Action:** find whether SAP Signavio publishes a concrete BPMN diagram in which an agent is
a lane, a pool participant, or a task performer. If yes, C1 flips to YES and this source
qualifies. If the only artefacts are dashboards, mining views and journey maps, C1 stays NO.
That single check decides the source. It was not performed in Pass 1.

## Entry points

- `https://www.signavio.com/highlights/ai-agent-excellence/` — the anchor page
- Pages confirmed to exist by `site:` sweep on 2026-09-22 (titles from result lists, **not
  opened**): "4-step guide to AI agent excellence", "Unleashing the full potential of AI
  agents with SAP Signavio", "Governing the Autonomous Enterprise: AI Agent Mining…",
  "Why Enterprise Agents Need SAP Signavio's Company…", "Fast track process design with AI
  driven recommendations", "SAP Business AI", "SAP Signavio Process Transformation Suite
  February 2026…"
- `https://www.signavio.com/` footer sections: "BPMN 2.0 Insights", "Process Transformation
  Wiki", "Business Scenarios", "Webcasts", "Downloads"
- `community.sap.com` — SAP Community carries Signavio content ("Generate Process Models
  with GenAI", "AI-assisted process modeling: instantly transform text into…"). **Note both
  of those titles are design-time AI**, i.e. further C1-NO evidence.
- **SAP Business Accelerator Hub** — named in the method prompt as a marketplace to check.
  **Not reached in Pass 1.** If Signavio is ruled in, that hub is the likeliest home of
  concrete process content and should get its own entry point here.

## Enumeration instructions

Only if the ruling is "in": enumerate the `highlights/` section and the "BPMN 2.0 Insights"
area, then the SAP Community Signavio tag as a logged `search-protocol` sub-stream. Apply
the runtime-vs-design-time test to every page and expect a high `E2-no-ai-element` count
with the vendor's own wording quoted.

## Artefact mechanics

- The site is **heavily client-rendered**: `main`/`article` returned 130 characters on first
  load and the real content only appeared in `document.body` after a further ~6 seconds.
  Wait and read `body`, then strip the nav, or you will record an empty page.
- Expect dashboards, journey maps and mining screenshots rather than BPMN diagrams on the AI
  pages. A journey map is not BPMN — name it when excluding.
- Signavio's genuine BPMN artefacts live in the modelling/teaching material ("BPMN 2.0
  poster", "BPMN 2.0 Insights"), which is where a diagram showing an agent performer would
  most plausibly appear.

## Known gotchas

- **The strongest C1-NO signal is easy to miss**: "using the platform of your choice" is one
  clause in a long bullet. Quote it — it is the sentence that distinguishes this vendor from
  Camunda, Flowable and BAMOE.
- Signavio material is spread across `signavio.com`, `sap.com` and `community.sap.com`.
  Decide the scope and record it; do not silently drift across hosts.
- Much AI content is process-*mining* flavoured (agent behaviour analytics). Mining views
  are `E0-no-artefact` or `E1-not-bpmn`, not `E2`.

## Spot checks performed by Pass 1

Spot check only, not a verdict:

- `/highlights/ai-agent-excellence/` — opened; all four capability headings, the "platform
  of your choice" clause and the "employees and AI agents" clause read from the page body
  after waiting for client-side rendering.

## RESUME

(empty)
