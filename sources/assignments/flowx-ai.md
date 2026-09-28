---
source: flowx-ai
source_name: FlowX.AI (product documentation — AI platform / using agents)
source_type: vendor documentation
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: YES
  C2_native_bpmn20: YES
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES (operator ruling 2026-09-24, general C4 rule)
access: public
population_type: enumerable
population_estimate: 945  # actual; the 40 estimate was the AI branch only
effort: medium
needs_logged_in_browser: false
status: DONE (elicitation-6f, 2026-09-25, second revision) — Census complete, population exhausted
  (945/945). After a peer's method challenge the E1 rows were re-judged by eye: 324 pages with no AI/LLM
  keyword in their main text became mechanical `E2-no-ai-element`, and every figure of the 206
  AI-discussing pages was opened (1177 distinct figure URLs, 538 tiles on contact sheets, each
  dispositioned in `ledgers/flowx-ai.raw/visual-progress.jsonl`). Three pages that publish a Mermaid
  process whose nodes are BPMN element names became UNCERTAIN with records 008/009/010.
  `tools/audit.py flowx-ai` → `problems: none`.
---

## Criteria evidence

- **C1 YES** — https://docs.flowx.ai/5.9/ai-platform/using-agents/bpmn-integration
  (2026-09-22): "Trigger AI agents from BPMN workflow nodes for automated document
  processing, decisions, and content generation." And: "Integrate AI agents directly into
  your BPMN processes to automate document processing, make intelligent decisions, and
  generate content without user interaction."
- **C2 YES** — same page, step-by-step instruction: "Add a Service Task node to your process
  where you want to trigger the agent." The overview also promises "Make AI-powered
  decisions at process gateways". Service task and gateway are both BPMN 2.0 elements.
- **C3 YES** — `docs.flowx.ai` served anonymously.
- **C4 UNCLEAR** — FlowX.AI targets banking and publishes customer-shaped content ("How
  Mid-Size Banks Automate Operations Without…", "Reducing Manual Back-Office Work at Global
  Banks", "Low-Code Automation Platforms Fortune 500 Banks Trust"), but those are marketing
  titles from a `site:` sweep, not verified customer evidence. Mirrored in
  `OPERATOR-TODO.md` (B6). **Recommendation: include** — the C1/C2 evidence here is among
  the most explicit in the whole sample.

## Entry points

- `https://docs.flowx.ai/5.9/ai-platform/using-agents/bpmn-integration` — the anchor page
- `https://docs.flowx.ai/5.9/ai-platform/using-agents/` — the "Using agents" branch root
- `https://docs.flowx.ai/5.9/ai-platform/` — the AI platform branch root
- Sibling pages confirmed by `site:` sweep: "AI Analyst", "Using AI agents", "Chat
  interface", "FlowX.AI architecture"
- `https://www.flowx.ai/` — separate marketing host with banking case studies
- Check `https://docs.flowx.ai/sitemap.xml`

## Enumeration instructions

1. Frontier = the whole `ai-platform` docs branch **plus** the process-designer branch. In
   tools of this shape the AI node is documented in both places, and enumerating only the
   AI branch is the keyword-narrowing that shared rules section 6 forbids.
2. **Pin the docs version.** The path carries `/5.9/`; search results may point at older
   versions. Normalise before building the frontier and record the version in the ledger
   header.
3. Add the `flowx.ai` blog as a second sub-population with its own enumeration method, or
   state explicitly that you scoped to the docs only.

## Artefact mechanics

- Mintlify-style docs (the page carries a "Copy page" control): clean text and numbered step
  blocks. Prose names BPMN elements directly, which is good textual evidence.
- The "Copy page" affordance suggests a raw-markdown endpoint may exist. If it does, that is
  the cheapest and highest-fidelity read — look for it before scraping HTML.
- Expect UI screenshots of the process designer rather than exported diagram assets. Capture
  at native resolution.

## Known gotchas

- FlowX.AI also ships an "AI Analyst" and a "Chat interface". These may be design-time or
  end-user-facing rather than in-process. Apply the same runtime-vs-design-time test used
  for CIB seven, and quote whatever you dismiss.
- The marketing host gates much of its content behind demo forms; the docs are open. A
  gated post is `BLOCKED`, not an exclusion.

## Spot checks performed by Pass 1

Spot check only, not a verdict:

- `/5.9/ai-platform/using-agents/bpmn-integration` — opened; both C1 quotes and the "Add a
  Service Task node" instruction read from the rendered page.

## RESUME

(empty — census finished; population exhausted, 945/945 rows)

## Census record (elicitation-6f, 2026-09-25)

**Status: IN-PROGRESS (revised 2026-09-25).** Population exhausted; 945 of 945 rows. A first
E1 screen was mechanical and is being superseded (see `## Delta` at the end). `tools/audit.py flowx-ai` →
`problems: none`.

### Population and method

The source is one Mintlify documentation host, and it publishes three indexes of itself, so the
population is their union, frozen before any row was judged
(`ledgers/flowx-ai.raw/population.json`, 945 URLs):

- `sitemap.xml` — 926 `<loc>` entries;
- `llms.txt` — 386 entries (the index the site publishes for LLM crawlers);
- the 11 `/_llms/*` machine indexes `llms.txt` points at (v4.7.x, v5.1, 5.9 and their
  sub-lists, release-notes), which list pages by heading.

Nothing was narrowed: all four published version trees (5.9 = 381, 5.1 = 228, 4.7.x = 205,
release-notes = 120, plus the 11 `_llms` indexes) are in the population. No version facet, no
keyword filter, no search box.

Access: every page's **own published markdown twin** (`<url>.md`, the "Copy page" endpoint this
Mintlify site exposes), ~1 request/second, anonymously — no login, no captcha, nothing blocked.
The 11 `/_llms/*` pages have no twin and were read from the site's own `llms-full.txt` bundle.
945/945 pages read; the whole population could therefore be screened for AI terms rather than a
search result.

Files: `ledgers/flowx-ai.jsonl` (header + 945 rows + footer), `ledgers/flowx-ai.frontier.txt`
(945 URLs), `ledgers/flowx-ai.quotes.txt` (the evidence audit, below), `corpus/flowx-ai/`
(10 records + 10 captures), raw material in `ledgers/flowx-ai.raw/` (the 945 markdown twins, the
538-tile contact sheets, `visual-progress.jsonl`, `figs_inventory.json`).

### Headline finding: AI reaches BPMN in FlowX only by delegation

- The **5.9 BPMN Process Designer is genuine BPMN 2.0**: pools and lanes (`Default`), start and
  end event circles, user tasks, service tasks, send/receive message tasks, business-rule
  service tasks, exclusive and parallel gateways, boundary events, call activities — read from
  the published canvases and from the pages' own prose ("The Process Designer provides a visual,
  BPMN 2.0-compliant environment").
- Its **"Process Nodes" palette offers no AI node type** (checked by eye against the palette
  figure). AI enters a BPMN process only by **delegation**: a Service Task — or a Send/Receive
  Message Task pair — carrying the **`Start Integration Workflow`** action, which invokes a
  *workflow* (Integration Designer / agent workflow) that contains the AI nodes.
- The AI-native canvases (Integration Designer, Agent Builder) are the vendor's **own notation,
  not BPMN**: the site's own glossary says "a workflow is **Not a BPMN process**: workflows are
  started from processes or triggers, and their nodes are grouped into Flow Control, Data
  Operations, Tools, and AI categories".

This is why the census's E2 (36 pages) is so large: many pages discuss AI at length and publish
a BPMN figure, but the AI sits in the *workflow* the BPMN node calls, never inside the BPMN
diagram itself. Every dismissal is quoted in the row's `note`.

### Verdicts

| | |
|---|---|
| rows | 945 = population |
| EXCLUDE | 935 — E0-no-artefact 372, E1-not-bpmn 165, E2-no-ai-element 397, E3-duplicate 1 |
| UNCERTAIN | 10 (full records written; each carries its own question) |
| BLOCKED | 0 |
| judgement exclusions | 85 (9.0%) — the review queue for false negatives |

The E1 rows are now evidence-based: every one of them is either a product-UI screenshot of the vendor's
own screens (judgment `false` — a screenshot is not a drawn diagram), a *drawn* diagram that is not BPMN
(the vendor's Integration Designer / Agent Builder / Workflow canvas, an architecture box chart, a D2
render, a stylised illustration — judgment `true`, named in the note), or a fenced diagram read verbatim
from the page (Mermaid = drawn, `true`; an arrow sketch in text = a listing, `false`). No `bpmn-ai` tile
exists anywhere in the 538: on this source the AI never sits inside a BPMN diagram.

### The ten records

The decisive one is **001 `/5.9/ai-platform/tutorials/document-processing`**: the only page where
a genuine BPMN process is published *together with* AI inside it. Its process is a Mermaid
`flowchart TD` whose nodes are BPMN elements (User Task, Send/Receive Message Task, Business
Rule, Exclusive Gateway, End Event) alongside an AI node-type table (Document Understanding,
Document Extraction, Text Understanding, Text Generation), with a Custom Agent variant of the same
pipeline on SaaS 5.11+. It is published as Mermaid, not as a `.bpmn` file — which is exactly the
open question the record carries.

The others: **002** `passing-data-between-nodes` (prose binding: a Service Task carrying "Start
Integration Workflow"), **003** `start-integration-workflow` (the action that carries the
binding), **004** `bpmn-integration` (three ASCII arrow sketches whose nodes are BPMN elements),
**005** `custom-agent-node` (the AI node on the vendor's own canvas — 11-figure contact sheet),
**006** `agent-typologies` (prose: the surrounding BPMN process presents the agent's output as a
User Task), **007** `roles-permissions-matrix` (5.1; `aiagent_edit`), and the three added by the
eye-pass: **008** `/4.7.x/.../ai-core/ai-developer` and **009**
`/5.9/ai-platform/pre-built-agents/ai-developer` (a Mermaid `graph TD` whose endpoints are BPMN
event circles `([Start])`/`([END])` and whose middle is a subgraph of four AI task names —
'Classify Document', 'Summarize', 'Identify process', 'Extract Prompt' — then 'Generate Business
rule'; the two versions differ only in the subgraph label, so they are separate items), and
**010** `/5.9/ai-platform/tutorials/customer-onboarding` (the whole onboarding process as a
Mermaid flowchart whose 13 node labels are BPMN element names — four User Tasks, a Send/Receive
Message Task pair carrying the edge label 'Workflow: kycVerification', an Exclusive Gateway with
PASSED / FAILED-REVIEW conditions, a 48h timer boundary event, two End events — i.e. record 001's
shape). All three were also read in the browser: the diagrams are live Mermaid `<svg
class="flowchart">` elements whose `<g class="node">` labels and `<g class="cluster">` names were
read from the DOM, not from a picture.


**E3 precedent:** the only duplicate in this source is 002's 5.1 twin, whose diagram fence is
byte-identical; `duplicate_of` names record 002. Similar-but-different diagrams were *not*
deduped (a Mermaid fence on the 5.1 page that differs from its 5.9 twin is a separate row, per
shared rule 3).

### Named and undone lexicon false positives (for the method chapter)

- **`FlowX.AI`** — the vendor's own name stands on every page and satisfied both `ai` and `llms`
  matches; stripping it (`strip_fp`) is what made the AI count meaningful.
- **`User-Agent`** — the HTTP-header example on the integration pages matched `agent`.
- **`ai.flowx.*`** — the platform's own Kafka topic namespace, not an AI marker.
- **Site chrome** — every `docs.flowx.ai` page carries AI words *outside* `<main>`: the nav tab "AI
  Platform", the nav item "Using FlowX docs with AI assistants", the footer nav, and the disclaimer
  "Responses are generated using AI and may contain mistakes." This is why the census screened each
  page's own markdown twin rather than the rendered DOM.
- **`model` alone is deliberately absent** from the lexicon: FlowX writes "data model", "process
  model" and "Project Data Model" on hundreds of pages. Same class of correction the
  processmaker census made.
- **Ordinary words** that matched and were stripped before counting: `prompt(s)`, `classification(s)`,
  `retrieval`, `intelligent`, `intelligence`, `semantic`, `summarise/recommend`, `vector`, and the
  person-noun `agent` ("Support agent needs to find customer's account quickly").

### Evidence audit artifact

`ledgers/flowx-ai.quotes.txt`: every double-quoted span in all 945 rows' `evidence` and `note`
fields, tested against the page that row judges — **0 failures**. Convention, recorded in each
record's header: double quotes = the judged page's own words (whitespace and curly/straight
quotes normalised only); single quotes = a quotation from another named source (the glossary, or
a label read in a figure).

### Caveats the researcher should know

1. **The markdown twin is not always the whole page.** On the `document-processing` tutorial the
   twin carries the Mermaid diagram and the workflow table, but the numbered build steps
   (`<Steps>` component content) appear only in the rendered page — verified in the browser on
   2026-09-25. The twin was sufficient for this census's artefact test on that page, but a
   reviewer re-checking a rejection should look at the rendered page, not only the twin.
2. **Version mirroring is pervasive:** 76 pages are byte-identical to another version's page
   after normalising the version segment (38 pairs); separately, 22 pages (11 pairs) publish a
   byte-identical *diagram fence* under another version URL. Every such pair is recorded in the
   row's note, so the corpus is not padded by re-publication.
3. The marketing host `www.flowx.ai` was outside this assignment's scope (the operator's
   population is the docs host); C4 evidence for it sits in `OPERATOR-TODO.md` B6.

## Delta: E1 rows re-judged by eye (elicitation-6f, 2026-09-25) — CLOSED

The first build's 530 `E1-not-bpmn` rows were produced by an offline screen: the note named a category
("product UI screenshots of the vendor's own screens") from the page's *figure count* alone, without
opening the figures. A peer (`elicitation-5a`) challenged it, correctly: that is an evidence-free claim,
and a BPMN canvas with an AI element on it would be a false negative, the one error this census must not
make. What was done, and what it changed:

1. **324 rows** whose page carries no AI/LLM keyword anywhere (main text, figure filenames and alt texts
   all screened) → `E2-no-ai-element`, `judgment: false`, mechanical, with the note stating exactly what
   was and was not looked at (`ledgers/_fx_fix.py recode-a`).
2. **206 rows** whose page does discuss AI → every figure opened. 1177 distinct figure URLs fetched into
   `ledgers/flowx-ai.raw/figures2/` and tiled 4 per sheet at ≥900 px (135 sheets,
   `ledgers/flowx-ai.raw/sheets/`); each of the 538 tiles dispositioned one by one and logged in
   `ledgers/flowx-ai.raw/visual-progress.jsonl` (`ui` 392, `drawn` 59, `bpmn-noai` 87; **0 unclear, 0
   broken, 0 `bpmn-ai`**). Emission rule in `ledgers/_fx_caseb.py`: any `drawn` tile → E1 `judgment:true`,
   the note naming what each drawn figure is; all `ui` → E1 `judgment:false`; a `bpmn-noai` tile →
   `E2-no-ai-element` with `judgment` = whether a real AI term survives the named false positives; a
   fenced diagram and no image → E1 judged on the fence's own source text (Mermaid = drawn, `true`;
   arrow sketch = listing, `false`); no image and no fence → `E0-no-artefact`.
3. **3 rows** that publish a Mermaid process whose nodes are BPMN element names and which contains AI task
   names (n=95, n=464, n=467) → `UNCERTAIN` + `needs_human_ruling`, with records 008/009/010. These are
   the nearest misses in the whole source: not exclusions, because naming their notation is the
   researcher's call, not mine.

Result: EXCLUDE 938 → 935, UNCERTAIN 7 → 10, E1 530 → 165, E2 36+324 → 397, judgement exclusions 62
(6.6%) → 85 (9.0%). The share rose because opening the figures replaced a mechanical screen with a real
one; it stays under the audit's 10% line. If the researcher wants it lower, the honest lever is the
corpus's notation rule for Mermaid processes (which would move all three records), not reclassifying
rows. The peer convention applied throughout: a screenshot of a UI, form, table or code listing is E1
with `judgment:false`; only a *drawn* non-BPMN diagram is `judgment:true`.

The eight figures that could not be opened are S3 objects the vendor has made private (AccessDenied) —
documented in `OPERATOR-TODO.md` P8 (n=103, 221, 285, 500, 567, 667, 674, 929); no operator action is
available, and those rows' verdicts rest on the figures that were retrieved.

