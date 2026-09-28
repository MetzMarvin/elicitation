---
source: uipath-marketplace
source_name: UiPath Marketplace (listings, accelerators, agent catalogue)
source_type: vendor marketplace
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: YES
  C2_native_bpmn20: YES
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES
access: free-account
population_type: enumerable
population_estimate: 2326
effort: large
needs_logged_in_browser: true
status: IN-PROGRESS (elicitation-7b)
---

## Criteria evidence

- **C1 YES** — https://marketplace.uipath.com/products/gen-ai (2026-09-22): the catalogue
  is titled "Agentenkatalog | 76 Ergebnisse" and offers listings of type "Agent-Vorlage"
  (agent template), e.g. "Invoice Validation Against Contract Agreement — Agent validates
  invoice details against a contract agreement by identifying discrepancies in pricing".
  UiPath additionally markets Maestro as "Business Orchestration with BPMN and AI"
  (uipath.com, Google result 2026-09-22).
- **C2 YES** — via UiPath Maestro, whose modeller is native BPMN; see
  `uipath-maestro-docs.md` for the quote. The prior deep dive
  (`notes/uipath-promotion-pattern/analysis.md`) established that an agent-bound task in a
  Maestro template is a plain `<bpmn:serviceTask>` in the XML.
- **C3 YES with an access tier** — listing pages render anonymously; **inspecting a
  process template's task bindings requires opening it in UiPath Studio Web inside a
  tenant**, which needs a free UiPath Automation Cloud account. Per the sampling rules a
  free account is an access tier, not a C3 failure. Recorded as `access: free-account` and
  raised in `OPERATOR-TODO.md`.
- **C4 YES** — UiPath is one of the largest RPA vendors by customer base and runs its own
  academy (`academy.uipath.com`, "Introduction to BPMN concepts Course"). The marketplace
  itself lists 2326 public listings and an application directory spanning ABBYY through
  Workday, which is itself evidence of enterprise ecosystem presence.

## Entry points

- **`https://marketplace.uipath.com/sitemap`** — the single strongest entry point. This one
  HTML page enumerates the whole catalogue: 2671 anchors, of which **2326 unique
  `/listings/<slug>` paths**, plus every `/collections/*`, `/applications/*` and
  `/integrations/*` index. Take the frontier from here.
- `https://marketplace.uipath.com/products/accelerators` — "Beschleuniger | 86 Ergebnisse"
  (solution accelerators; where the Maestro process templates now live)
- `https://marketplace.uipath.com/products/gen-ai` — "Agentenkatalog | 76 Ergebnisse"
  (agent templates)
- `https://marketplace.uipath.com/collections/artificial-intelligence` and
  `/collections/solution-accelerators` — curated collections
- Listing detail path shape (observed): `https://marketplace.uipath.com/listings/<slug>`,
  e.g. `/listings/chatbot-with-dialogflow-ai`.

## Enumeration instructions

1. Frontier = the 2326 `/listings/` paths from `/sitemap`. Write it to
   `ledgers/uipath-marketplace.frontier.txt` **before** judging anything.
2. This is by far the largest population in the sample and most of it is classic RPA
   activity packages with no BPMN artefact at all. Those are honest `E0-no-artefact` or
   `E2-no-ai-element` rows — mechanical, `judgment: false` — not a reason to narrow the
   frontier. A large mechanical `E2` count on a big catalogue is expected and explicitly
   sanctioned by `templates/ledger.md`.
3. If context forces a stop, use the `RESUME` protocol; do **not** substitute the 86 + 76
   facet lists for the population. If the researcher rules that the facets may stand in
   for the population, they must write that ruling into this file and it must be reported
   in the thesis as a deviation from the census.
4. The two facet counts (86 accelerators, 76 agent catalogue) are recorded here so the
   facet-vs-population cross-check of shared rules section 6 can be performed cheaply.

## Artefact mechanics

This source has the most demanding mechanics in the sample, and they are already
documented in `notes/uipath-promotion-pattern/analysis.md`. Summary for Pass 2:

- A listing page shows title, generic boilerplate description and screenshots. **The BPMN
  diagram is usually not on the listing page.**
- The diagram becomes inspectable only by opening the template in **UiPath Studio Web**
  inside a tenant (`https://cloud.uipath.com/<tenant>/marketplace_/listings/<slug>`).
  There, an AI-bound task is a `bpmn:serviceTask` whose `Action` property reads
  "Start and wait for agent".
- **There is no diagram-level visual signal** distinguishing an AI-backed task from a
  deterministic one. You must open each task's Properties panel and read `Action`. Prefer
  the DOM of the properties panel over a screenshot.
- Many Maestro templates ship with every task at `Implementation → Action: None`. Per the
  prior analysis these blank-but-bindable scaffolds are a finding in their own right, not
  an exclusion. Verdict `UNCERTAIN` with the question already formulated in
  `templates/ledger.md`.
- **Read-only conduct is binding here.** Shared rules section 10: do not save, publish or
  deploy in Studio Web. If you must change a property to reveal a binding, revert it and
  record that you did.

## Known gotchas

- **`https://marketplace.uipath.com/listings` (the index) returns 404** — "Entschuldigung!
  Anscheinend fehlt die Seite." Only `/listings/<slug>` detail pages exist. Use `/sitemap`.
- **German localisation.** The site served German from this location
  ("Auflistungen", "Ergebnisse", "Anmelden"). Result counts and facet labels are German.
  If you need English, use the language switcher in the footer rather than guessing a
  `/en/` prefix.
- Some slugs carry a numeric suffix that does not appear in the title
  (`/listings/system-service-manager-583801`, `/listings/loan-processing1915`). Never infer
  a slug from a title.
- Most "maestro"-tagged templates are published under a single `Internal Labs` account
  with near-verbatim boilerplate descriptions. Boilerplate is not an exclusion ground.
- Studio Web is a canvas app with a thin accessibility tree; coordinate-based clicking plus
  DOM reads of the properties panel is the working idiom.

## Spot checks performed by Pass 1

Spot checks only, not verdicts:

- `/sitemap` opened and parsed: 2326 unique `/listings/` paths.
- `/products/accelerators` rendered "Beschleuniger | 86 Ergebnisse".
- `/products/gen-ai` rendered "Agentenkatalog | 76 Ergebnisse".
- No listing detail page was opened and no template was opened in Studio Web in Pass 1.

## Incident and ruling (elicitation-7b, 2026-09-28)

- Opening a marketplace template via the in-tenant "Use in Studio Web" link **creates a draft
  solution** in the tenant; there is no read-only template open. One draft was created this way
  ("Loan Processing 1 6 1 4 2", solutionId 786fa94d-a4dc-4f25-b93f-08df1807e6ac, 2026-09-28 ~08:50
  GMT); cleanup list: `ledgers/uipath-marketplace.raw/tenant-drafts-created.md`, OPERATOR-TODO P15.
- **Operator ruling 2026-09-28: option (ii).** Inspect only drafts that already exist in the Cloud
  Workspace (about 40 from the July precedent, plus the draft above), read-only. Never click "Use in
  Studio Web" or any template link again. Templates without an existing draft: `UNCERTAIN` +
  `needs_visual_check`, question "Maestro/agent template not opened in Studio Web (operator ruling
  2026-09-28: opening creates a tenant draft); task bindings not inspected. Does any task bind an
  agent/LLM?"; listing page and screenshots judged as usual (INCLUDE allowed if a screenshot already
  shows an agent-bound task).
- **Second incident and final ruling (2026-09-28 ~09:20 GMT).** Under a follow-up ruling (a) one existing
  draft ("Summarize Outlook email attachments with AI 1 1") was opened; opening its Process.bpmn made Studio
  Web create folders/files ("evals"), post EntryPoints and re-save Process.bpmn, and `checksession` returned
  503. Studio Web was stopped. **Final ruling: no further Studio Web.** Every Maestro/agent template without
  inspected evidence is `UNCERTAIN` + `needs_visual_check` with the ruling-(ii) question; the one opened draft is
  recorded from what was visible (`ledgers/uipath-marketplace.raw/studioweb-outlook-draft-evidence.md`,
  labelled post-open editor re-save).
- Listing crawl: Cloudflare challenges scripted GETs after ~190 fetches (HTTP 429, `Cf-Mitigated:
  challenge`); operator protocol (b): probe after >= 60 min, <= 1 req/5 s, exponential backoff, stop
  after three consecutive challenges, then BLOCKED rows. In-browser fetch() of challenged pages is
  not allowed (circumvention).

## RESUME

(empty)
