---
source: camunda-marketplace
source_name: Camunda Marketplace (connectors, blueprints, partner solutions)
source_type: vendor marketplace
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: YES
  C2_native_bpmn20: YES
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES
access: public
population_type: enumerable
population_estimate: 254
effort: large
needs_logged_in_browser: false
status: DONE (elicitation-aa, 2026-09-26)
---

## Tooling deviation (elicitation-aa, 2026-09-26)

This session has **no `mcp__cdp1__*` browser tools** available, so the shared-Chrome
protocol could not be used as written. Fallback, sanctioned by
`prompts/02b_worker-adapter.md`: every URL is fetched over HTTP with `curl` after being
extracted from a real page/DOM (never guessed), and every image is read natively. The
enumeration is stronger than the estimate below: the marketplace's own listing endpoint
`https://marketplace.camunda.com/api/marketplace/v1/listing` returns the entire
catalogue in one 2 MB JSON response and reports `totalCount: 255` (not 254 — the
assignment's estimate was taken from the rendered "254 Results" header, which lags the
catalogue). Detail pages are server-rendered: a plain GET returns a 550 KB page whose
`window.dataStore` blob carries the whole product record (`application.summary`,
`.overview`, `.features`, `.tags`, `.screenshots.items`, `.relatedContent`) — so the
client-rendered warning above applies to the *tile grid*, not to detail pages.

## Criteria evidence

- **C1 YES** — https://marketplace.camunda.com/en-US/home (2026-09-22): "AI Agents
  Implement enterprise-grade agents with governed planning and memory". The catalogue
  carries a first-class "AI Agents" section and an "Agentic AI orchestration" use-case
  facet.
- **C2 YES** — inherits Camunda 8's BPMN 2.0 engine; Blueprints are `.bpmn` diagrams. See
  `camunda-docs-blog.md` for the C2 quote. Confirm per listing during the census rather
  than assuming it.
- **C3 YES** — the catalogue at https://marketplace.camunda.com/listing rendered
  "254 Results" anonymously, with no login prompt.
- **C4 YES** — see `camunda-docs-blog.md` C4.

## Entry points

- `https://marketplace.camunda.com/listing` — browse-all catalogue; it redirects to
  `https://marketplace.camunda.com/en-US/listing?page=1&locale=en-US`
- Pagination: `?page=N&locale=en-US`. 12 tiles rendered per page at the viewport used,
  254 results total, so expect roughly 22 pages. **Verify the per-page count yourself**
  before fixing the page count: the grid is responsive and the tile count changes with
  viewport width.
- Listing detail path shape (observed, not guessed):
  `https://marketplace.camunda.com/en-US/apps/<numeric-id>/<slug>`, e.g.
  `/en-US/apps/519670/compliance-monitoring-agent`.
- The platform is **AppDirect**. Watch the network panel while paginating for its JSON
  endpoint; an exact `totalCount` from that XHR is the strongest possible
  `enumeration_method` and should replace the "254 Results" string if you find it.

## Enumeration instructions

1. Enumerate **unfiltered** from `/listing`, all 254 items. The facets ("Agentic AI
   orchestration" use case, "Blueprints" category, "AI Agents" section) are exactly the
   narrowing that shared rules section 6 forbids as a substitute for the population.
2. If you use a facet as a cross-check, you must also confirm that no AI artefact sits
   outside it, and record that check in the ledger header.
3. Facets available, for the record: Categories (Connectors, Blueprints, Partner
   Solutions), Creator (Camunda, Partner, Community), Version Compatibility (8.2–8.10),
   Availability (Open Source, Listing Only, Coming soon), Industry, Use Case.

## Artefact mechanics

- **Blueprints** are the richest: downloadable `.bpmn` files or diagrams rendered in an
  embedded `bpmn-js` viewer. `.bpmn` XML is decisive evidence — take it.
- **Connectors** typically ship an element template (JSON) plus a screenshot; the AI
  element may be visible only as a task type, so the element template and prose are the
  evidence route.
- **Partner Solutions / Solution Accelerators** are mostly marketing pages with one static
  diagram image. Capture the original image asset at native resolution, not a page render.

## Known gotchas

- Client-rendered (AppDirect). Wait for the tile grid before extracting; a bare page-text
  read returns site chrome and no listings.
- Several anchor `href`s carry query strings and are redacted by the browser extension's
  privacy filter. Read `new URL(a.href).pathname` instead of the raw `href`.
- `https://marketplace.camunda.com/en-US/search` does **not** exist (it serves
  `/status/404`). Navigate only from links you extracted — this was a guessed URL in Pass 1
  and it failed.
- Listings authored by Camunda itself and by partners sit in the same catalogue; both
  count. "Partner marketing page" is not an exclusion ground.

## Spot checks performed by Pass 1

Spot checks only, not verdicts:

- `/listing` rendered "254 Results" and a tile grid of 12 `/en-US/apps/...` links.
- Listing paths observed on the home page include
  `/en-US/apps/719979/agentic-ai-orchestration-with-formio` and
  `/en-US/apps/519046/agentic-ai-assisted-quality-audit-process`. Neither was opened;
  Pass 2 judges them as ordinary frontier items.

## RESUME

(empty)

## Closure (elicitation-aa, 2026-09-26)

Census closed. 255 of 255 listings judged (`rows == population_size`), `tools/audit.py`
prints `problems: none`. Counts: `INCLUDE` 52, `UNCERTAIN` 23, `EXCLUDE` 180
(`E0`=9, `E1`=10, `E2`=159, `E3`=2), `BLOCKED` 0; judgement exclusions 17 of 255 (6.7%);
review queue visual-check 12, human rulings 24. 75 records in
`notes/elicitation/corpus/camunda-marketplace/`. Code choices and the boundaries behind the
`UNCERTAIN` verdicts: `notes/elicitation/ledgers/camunda-marketplace.raw/DECISIONS.md`.
Tooling deviation unchanged: no browser tools in this session, all fetching via `curl` from
extracted links, all decisive figures read natively at full size.
