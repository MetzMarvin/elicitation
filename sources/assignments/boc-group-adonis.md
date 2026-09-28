---
source: boc-group-adonis
source_name: BOC Group (ADONIS) — blog and documentation portal
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

The sampling rules allow a hard `OUT` only under C2 or C3, on positive evidence. C1 is a
judgement criterion and **cannot produce an `OUT` on its own**, so a vendor failing only C1
is `UNCLEAR-NEEDS-RULING` and still gets a provisional assignment file. This is that file.

**My recommendation is to rule this source out at Gate 1** (see B8 in `OPERATOR-TODO.md`),
with one caveat named below. If the ruling is "out", delete this file and keep the rejection
row in `candidate-vendors.md`. If the ruling is "in", the work order below is ready to run.

## Criteria evidence

- **C1 NO, on positive evidence** —
  https://www.boc-group.com/en/blog/bpm/how-adonis-elevates-ai-powered-bpm/ (2026-09-22):
  "Instead of relying entirely on manual modelling and analysis, AI can assist by
  interpreting documentation, generating initial process drafts, and helping users interact
  with process knowledge more easily." The page's own feature headings are "Smarter Content
  Discovery", "AI-Assisted Process Modelling", "AI-Supported Process Analysis", "AI-Powered
  Process Understanding", "Multilingual Process Content with AI". Every one is
  **design-time**. No AI element inside a running process was found.
  This is the `E2-no-ai-element` situation lifted to vendor level: the AI generates and
  analyses the diagram rather than executing inside it.
- **C2 YES** — ADONIS is a BPMN 2.0 modelling suite with a documentation portal at
  `docs.boc-group.com`. Note that the vendor's page title "AI SOP to BPMN: Turn Process
  Documentation into BPMN" is itself further C1-NO evidence: it describes producing BPMN
  *from* documents.
- **C3 YES** — blog and docs portal served anonymously.
- **C4 YES** — BOC Group is an established European BPM/EA vendor (ADONIS, ADOIT) with a
  large public-sector and enterprise base, and it surfaced unprompted in the Channel 3 grid.

## The one caveat that could flip C1

`www.boc-group.com` publishes **"Let Your BPM Speak AI with MCP and ADONIS"** (surfaced by
the Channel 3 grid on 2026-09-22, **not opened**). An MCP server exposes the BPM repository
*to* external AI agents — the inverse direction from AI-in-BPMN, and close to IBM BAMOE's
"Exposing BAMOE capabilities to AI agents through MCP Server", which is inside a source that
qualifies. Whether that counts as an AI-in-BPMN integration capability is genuinely arguable.

**Open that page before ruling.** It is the only thing standing between this source and a
clean rejection.

## Entry points

- `https://www.boc-group.com/en/blog/bpm/` — BPM blog index
- `https://docs.boc-group.com/` — documentation portal; "Design Processes Using AI" and
  "Understand & Analyse Processes Using the AI Assistant" confirmed to exist by `site:` sweep
- "Let Your BPM Speak AI with MCP and ADONIS" — find it from the blog index; do not guess
  the slug

## Enumeration instructions

Only if the ruling is "in": enumerate the BPM blog index and the AI section of the docs
portal. Apply the runtime-vs-design-time test to every page, and expect a high, honest
`E2-no-ai-element` count with the vendor's own design-time wording quoted each time.

## Artefact mechanics

Blog posts carry static diagram images; the docs portal carries UI screenshots. Capture at
native resolution. No `.bpmn` export and no `bpmn-js` canvas was observed.

## Known gotchas

- This is the sample's clearest case of **AI-adjacent marketing without AI in the process**,
  which makes it a useful **negative control**: if a census agent returns `INCLUDE` rows
  here, that is a calibration signal that it is not applying the runtime/design-time
  distinction. Consider running it deliberately for that reason even if the ruling is "out".
- `boc-group.com` and `docs.boc-group.com` are separate hosts.

## Spot checks performed by Pass 1

Spot check only, not a verdict:

- `/en/blog/bpm/how-adonis-elevates-ai-powered-bpm/` — opened; all five named AI capabilities
  read from the rendered page, all design-time.

## RESUME

(empty)
