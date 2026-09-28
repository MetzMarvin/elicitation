---
source: processmaker
source_name: ProcessMaker (docs.processmaker.com; vendor now part of Decisions)
source_type: vendor documentation
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: YES
  C2_native_bpmn20: YES
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES
access: public
population_type: enumerable
population_estimate: 40
population_actual: 716
effort: medium
needs_logged_in_browser: false
status: DONE (elicitation-6f, 2026-09-25)
---

## Criteria evidence

- **C1 YES**: https://docs.processmaker.com/docs/add-a-genie-in-a-process (2026-09-24):
  "Add a FlowGenie object from one of the following locations in Process Modeler" and "If
  your process has a Pool object, the FlowGenie object cannot be placed outside of the
  Pool". The page also lists "Add boundary events" and the loop modes "No Loop Mode Loop
  Multi-instance(Parallel) Multi-instance(Sequential)".
  https://docs.processmaker.com/docs/flowgenie: "Add a Genie to a process using a modeling
  object in the Modeler"; "extract data using the vision model of OpenAI".
- **C2 YES**: https://docs.processmaker.com/docs/validate-your-process-is-bpmn-20-compliant:
  "Before you deploy your Process model to production, ensure that it is BPMN 2.0
  compliant".
- **C3 YES**: served anonymously.
- **C4 YES**: an established open-source BPM vendor. `processmaker.com` now redirects to
  `decisions.com` (see `search-protocol.md` Channel 8).

## Promotion mode

A **dedicated native node type** (the "FlowGenie object"), with BPMN activity semantics:
boundary events, multi-instance, and pool containment. This is the same mode as IBM BAMOE
and Flowable.

## Entry points

- `/docs/flowgenie` and its category: "Create a Genie in the FlowGenie Studio", "FlowGenie
  Configuration", "Add a Genie in a Process", "View and Manage Genies"
- `/docs/update-a-rag-collection-from-a-process` (RAG Collections, process-bound)
- `/docs/modeling-objects`: the full object palette (7 articles, 6 sub-categories)
- Release notes (Spring 2025, Summer 2025, Release Notes 2026) for AI-feature introductions
- The docs nav tree shows DESIGNER > Processes, Screens, FlowGenie, Decision Tables, Scripts,
  Data Connectors, Collections, RAG Collections

## Enumeration instructions

1. Frontier = the DESIGNER > FlowGenie category + RAG Collections + Processes > Modeling
   Objects + the Process Modeler articles. Enumerate from the left nav, not from Google.
2. The "EXAMPLES" and "BEST PRACTICES" sections in the nav may contain full example
   processes. Enumerate them too.
3. Do not keyword-filter.

## Artefact mechanics

- Docs are rendered by a hosted documentation platform ("Powered by Documentation").
  `main`/`article` includes the nav tree. Slice from the page H1.
- Expect screenshots of the Process Modeler. Genie nodes should be visible as a distinct
  shape.

## Known gotchas

- **Design-time AI traps in the same tree:** "AI Generated Object", "AI Asset Generation"
  and "Create a Process from Text" describe AI generating the model. Those are `E2` unless
  the generated process also contains a Genie node.
- The vendor rebrand: `processmaker.com` marketing now redirects to `decisions.com`. Stay
  on `docs.processmaker.com` and record any drift.

## Spot checks performed by Pass 1

- "Modeling Objects", "Add a Genie in a Process", "FlowGenie", "Validate Your Process is
  BPMN 2.0 Compliant": opened and quoted.

## Census record (Pass 2, elicitation-6f, 2026-09-25)

**Population: 716, not the estimated 40.** The estimate was of the *frontier* (the AI-adjacent
articles the assignment names); the census population is the whole documentation set, because the
assignment's own instruction is "do not keyword-filter" and the exhaustiveness claim requires a
finite, enumerable whole. The population is the **union of the two indexes the site publishes**:
`sitemap-en.xml` (707 `<loc>`) and `llms.txt` (715 entries) → **716 URLs**, frozen in
`ledgers/processmaker.raw/pages/population.json` (sorted) before any row was judged. The 9 URLs in `llms.txt` and
not in the sitemap are exactly the EXAMPLES and BEST PRACTICES articles the assignment asked to
enumerate too; neither index is a superset of the other, so union rather than intersection. The
site's own nav tree (DESIGNER > Processes / Screens / FlowGenie / Decision Tables / Scripts / Data
Connectors / Collections / RAG Collections) was read to confirm the two indexes agree. All 716
pages were fetched (documentation platform twins at `<url>.md`) and screened full-text; no facet
and no search box was used to narrow anything.

**Result: 716 rows, 716 frontier lines.** `python tools/audit.py processmaker` → `problems: none`.

| | |
|---|---|
| verdicts | EXCLUDE 710, UNCERTAIN 6 |
| exclusions | `E0-no-artefact` 615, `E2-no-ai-element` 73, `E1-not-bpmn` 22 |
| judgement exclusions | 19 (2.7%, well under the 10% gate) |
| superseding rows | 9 (`supersedes_row: true`, appended; see correction 2 below) |
| review queue | rulings 6, visual-check 0, blocked 0 |
| corpus records | 6, all in `corpus/processmaker/`, all UNCERTAIN with `needs_human_ruling` |

**The headline finding: this source never draws its AI inside a process.** No page among the 716
publishes a BPMN process model containing an AI node. ProcessMaker's AI surfaces as (a) modelling
**objects** — FlowGenie/Genie, AI Generated Object, Smart Extract, the IDP connector — shown as
rounded BPMN activity rectangles on the Modeler's dotted canvas grid, or as palette/object cards,
with their configuration panels beside them; (b) **design-time generators** that produce a process,
a screen or a script from a prompt; and (c) **runtime bindings that are not visually distinguishable
from ordinary connectors** — a Data Connector Task that writes into a RAG Collection, an IDP
connector that extracts document fields mid-Request. The last group is the analytically interesting
one and is why the source contributes six UNCERTAIN records rather than six INCLUDEs: the AI is
*really there at runtime*, but the source's own documentation admits it cannot be read off the
diagram (record 005 quotes the imported-template checklist: "Inspect the Process model for an IDP
connector").

**The six records.** `001 add-a-genie-in-a-process` — the promotion-mode artefact: a dedicated
native node type with full BPMN activity semantics (pool containment, boundary events, the four loop
modes), captured as its object card plus Configuration panel. `002 ai-generated-object` — the shape
the Modeler emits when the AI Assistant generates an asset. `003 smart-extract` — a document
extraction object "configured with a specific extraction model" whose page never uses the word AI
(UNCERTAIN, not E2, per CLAUDE.md §3). `004 idp-connector` — an AI/ML-bound connector whose AI
nature is stated only on `apidocs/idp-package` of the same source. `005 import-a-process-template` —
the only page in the source that publishes a **full BPMN model** (the "Expense Approval" template
cover: pool, two lanes, four tasks, two exclusive gateways, three events) and simultaneously
documents an AI-bound connector shipping inside templates of that kind. `006
update-a-rag-collection-from-a-process` — the only page placing an AI store inside a running
process ("Each time a case runs, the Data Connector will automatically insert the uploaded file as a
new record in the RAG Collection").

**Calibration that mattered.** A first-figure-only screen left 16 pages as E0; reading their *later*
figures found a Modeler canvas or a BPMN-notated object card on each, and all 16 were moved to
`E2-no-ai-element` (mechanical, `judgment: false`) rather than staying "no artefact at all". The
rows say so. Two spurious AI keyword hits were handled as explicit judgement-true E2 rows with notes
naming the false positive rather than silently quoting them: `form-task` ("Embedding Rules" — the
third-party embedding of Web Entries) and `actions-by-email-connector` ("natural language" — the
language of the email). The 22 E1 rows are all named: Screen Builder control documentation, chat-UI
Conversational Screens (the codebook's own E1 example), Genies/scripts/dashboard listing and
configuration screens, and the in-platform documentation chatbot.

**Limits.** 322 of the 323 figure-bearing pages had their first figure read by eye; the exception is
the one HTML-only landing page, which has no markdown twin. All figures of the 42 AI-keyword pages
were read, and the 16 pages above were read figure by figure. Rows decided mechanically record
`judged_from='mechanical screen (no figure opened by eye)'` so the researcher can see exactly which
rows rest on text alone.

**Raw evidence.** Every page fetched for this census, its figures and the contact sheets the figures
were read on are in `ledgers/processmaker.raw/` — `pages/` (the 716 markdown twins plus the HTML-only
root, `population.json`, both indexes and the fetch log), `figures/` (per-page figure directories and
the `sh_*.png` sheets), `first_figure/` (the first figure of each of the 323 figure-bearing pages, the
input to the subtree sample), `screen/` (the screening census), `ai_pages/`, `inline_figures/` and
`_working/`. Any row of the ledger can be re-checked against the page and the figure it was judged
from without re-fetching anything.

**Three corrections after the first DONE pass** (all three by the Pass-2 coordinator, all three
recorded here rather than rewritten silently):

1. **Raw evidence location** — the caches were moved from `ledgers/_pm_*` into
   `ledgers/processmaker.raw/` and every path reference in the corpus records and the helper scripts
   was updated to match.
2. **Judgement flag on the E2 rows** — the coordinator's broad AI lexicon
   (`AI/LLM/agent/genie/GPT/model/IDP/RAG/intelligent`) was run over the article text of all 64
   `judgment: false` E2 rows. It matched 62, but **54 of those matched only the word "model"** in
   "Process model" / "Process Modeler" / "data model" — the BPMN process model, not a model in the AI
   sense — so those 54 stay mechanical, which is what `templates/ledger.md` means by "no AI/LLM
   keyword anywhere". The remaining **9 rows** (`boundary-conditional-event`, `boundary-error-event`,
   `boundary-message-event`, `boundary-signal-event`, `boundary-timer-event`,
   `process-modeling-best-practices`, `process-modeling-best-practices-1`,
   `process-modeling-object-descriptions`, `sequence-flow-element`) name something AI-bound in the
   page's own prose — an "IDP connector" entry in an associable-object or palette list, "ProcessMaker
   Intelligent Document Processing (IDP)" as an external database, or "AI Generated"/"FlowGenie" in
   the sequence-flow element's connectable-object list — so dismissing each one took reading the
   sentence in context. All 9 were re-judged in a superseding row (`supersedes_row: true`, same `n`,
   appended, `superseded_rows: 9` in the footer) with `judgment: true` and a note naming the term and
   what it refers to. **Verdicts unchanged** — in every one of the 9, the AI-bound object is a palette
   entry or an external system, never an element of the diagram the page publishes, which is the test
   `E2-no-ai-element` states. Judgement exclusions: 19 (2.7%), still far below the 10% gate, so the
   step-3 self-audit is not triggered. One candidate was rejected: `start-event` matched only on
   "embedding" (the Web Entry embedding feature, not an embedding model), which is why the broad
   lexicon is a *screen* and each hit was read.
3. **The German mirror** — `docs.processmaker.com/de/` was checked exhaustively and does not exist
   (probe evidence in `sources/OPERATOR-TODO.md` §P7: both indexes carry no locale tree, the shell
   declares `<html lang="en">` with no `hreflang`, and every candidate locale path returns the
   platform's 404 shell, including `/de/sitemap.xml` and `/de/llms.txt`). The German-language pages
   that did exist are on the *marketing* host, not the docs host, and now redirect to `decisions.com`.
   No frontier line was added because there is no item to enumerate; if the coordinator has a concrete
   German docs URL that returns 200, it can be added and the population updated.

## RESUME

(empty)
