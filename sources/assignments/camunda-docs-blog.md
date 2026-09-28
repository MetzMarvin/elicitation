---
source: camunda-docs-blog
source_name: Camunda 8 (product documentation + vendor blog)
source_type: vendor documentation and blog
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: YES
  C2_native_bpmn20: YES
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES
access: public
population_type: enumerable
population_estimate: 120
effort: large
needs_logged_in_browser: false
status: DONE
---

## Criteria evidence

- **C1 YES** — https://docs.camunda.io/docs/components/agentic-orchestration/ai-agents/
  (2026-09-22): "The AI Agent connector is the primary Camunda connector for building AI
  agents. It integrates an LLM with your BPMN process". A named, shipped feature with its
  own documentation tree (`components/agentic-orchestration/`), not an extension point.
- **C2 YES** — same page: "If the LLM determines that a tool call is needed, Camunda
  activates the corresponding BPMN activity in the ad-hoc sub-process." The promoted
  construct is a BPMN 2.0 ad-hoc sub-process, an element of the standard.
- **C3 YES** — `docs.camunda.io` and `camunda.com/blog` served without login, paywall or
  consent gate in a clean tab; the blog post at
  https://camunda.com/blog/2025/05/benefits-bpmn-ai-agents/ returned full article text
  anonymously.
- **C4 YES** — https://camunda.com/blog/ index (2026-09-22) links a post titled "Camunda
  Recognized as a Visionary in Gartner BOAT Magic Quadrant 2026". Independent corroboration:
  IFS Cloud's own technical documentation links to `docs.camunda.org` for its workflow
  expression language, i.e. another enterprise vendor builds on Camunda.

## Entry points

- `https://camunda.com/blog/tag/agentic-ai/` — blog tag index (paginated)
- `https://camunda.com/blog/tag/ai/` — blog tag index (paginated)
- `https://camunda.com/blog/category/agentic-orchestration/` — blog category index
- `https://docs.camunda.io/docs/components/agentic-orchestration/` — docs section root;
  the left-hand tree under it is the docs population
- `https://camunda.com/sitemap.xml` and `https://docs.camunda.io/sitemap.xml` —
  cross-check for AI posts that carry none of the three tags above

## Enumeration instructions

1. Build the frontier from the **sitemaps first**, not from the tag indexes. The tag
   indexes are a convenient facet, and the shared rules (section 6) require that any facet
   be cross-checked against the unfiltered population. Take every `camunda.com/blog/*`
   entry and every `docs.camunda.io/docs/components/agentic-orchestration/*` entry.
2. Then open the three tag/category indexes above and confirm every post they list is
   already in the sitemap-derived frontier. Record that check in the ledger header `note`.
3. Do **not** filter the blog frontier by keyword. Camunda publishes AI-in-BPMN diagrams
   inside posts whose titles mention neither AI nor BPMN (release notes, CamundaCon recaps).
4. Known-positive seeds exist for this source and are deliberately withheld from you.
   Enumerate normally.

## Artefact mechanics

Three routes, in descending order of evidence strength:

1. **Downloadable or inline `.bpmn` XML.** Camunda tutorials frequently link a `.bpmn`
   file on GitHub (`github.com/camunda/camunda-8-tutorials`, e.g.
   `ai-agent-chat-with-tools.bpmn`, surfaced by Google on 2026-09-22). Decisive evidence:
   look for `<bpmn:adHocSubProcess>` and a `zeebe:taskDefinition` naming an agentic task
   type. **Prefer this route.**
2. **Static images in blog posts.** Blog diagrams are `<img>` assets. Capture the
   **original asset URL at native resolution** (the `src`), never a scaled page render —
   that is exactly the failure that destroyed the July 2026 round.
3. **Docs pages** embed diagrams as images plus prose naming the elements ("ad-hoc
   sub-process", "AI Agent connector", "tool feedback loop"), which is good textual
   evidence of BPMN-ness without vision.

## Known gotchas

- The blog index is client-rendered and lazy-loads; a page-text read under-reports posts.
  Extract hrefs from the DOM, or use the sitemap.
- Camunda ships **two** distinct AI features and they must not be conflated. The *AI Agent
  connector / AI Agent sub-process* is AI **inside** the process (in scope). **BPMN
  Copilot** is AI that **generates the diagram** — at artefact level that is the
  `E2-no-ai-element` case in the shared rules. Do not exclude a page just because Copilot
  is mentioned; exclude only if the AI mention is *only* Copilot, and quote it.
- Camunda 7 (`docs.camunda.org`) is a separate, largely frozen docs tree. Material found
  there belongs in this ledger, but flag it: CIB seven is a Camunda 7 fork and
  reconciliation must not double-count shared material.
- `marketplace.camunda.com` is a **separate source** with its own assignment file
  (`camunda-marketplace`). Do not enumerate it here.

## Spot checks performed by Pass 1

Spot checks only, not verdicts — Pass 2 judges these again as part of the frontier:

- https://camunda.com/blog/2025/05/benefits-bpmn-ai-agents/ — full article text retrieved
  anonymously; prose names "AI Task Agent activity" and "ad-hoc sub-process".
- https://docs.camunda.io/docs/components/agentic-orchestration/ai-agents/ — docs page
  retrieved; describes the AI Agent Sub-process and the tool feedback loop.

## Split

No split (elicitation-6f, 2026-09-26, answer to elicitation-5a). The blog half of the
frontier (indices 1–1435) is already crawled to disk — `ledgers/camunda-docs-blog.raw/`
holds the saved HTML of all 1435 posts, the extracted text/imgs/files record, and every
selected figure at reduced width — so a second worker would need no browser but would
either duplicate the visual pass that is running now or judge posts whose figures I am
mid-way through. The docs half (1436–1439) is not a slice at all: it is four BLOCKED rows
behind the docs-host egress refusal (P10). So there is nothing to hand over.

## RESUME

(empty)

## DONE — census complete, native-resolution pass closed (elicitation-6f, 2026-09-27)

`ledgers/camunda-docs-blog.jsonl`: 1439 rows = population_size, footer `status: COMPLETE`.
`python tools/audit.py camunda-docs-blog` reports **one** problem: the judgement-exclusion
share (see P13 in `sources/OPERATOR-TODO.md`); everything else is clean, and
`ledgers/_cmdb_verify.py` checks 64 corpus records with 0 problems.

| | final | (pre-visual-pass) |
|---|---|---|
| INCLUDE | 56 | 49 |
| UNCERTAIN | 8 (all with `needs_human_ruling` + question) | 71 |
| EXCLUDE | 1371 — E0-no-artefact 956, E2-no-ai-element 279, E1-not-bpmn 136 | 1315 — E0 956, E2 233, E1 126 |
| BLOCKED | 4 (frontier 1436–1439, the docs host; P10 in `sources/OPERATOR-TODO.md`) | 4 |
| judgement-exclusion share | 152 rows, 10.6% — **above** the 10% audit bar, reported not forced down | 141 rows, 9.8% |
| corpus records | 64 in `corpus/camunda-docs-blog/`, 56 in `raw/excluded/` (120 in total, as before) | 120 in corpus |
| review queue | visual-check 0 (was 110), rulings 8 (was 71), blocked 4 | visual-check 110, rulings 71 |
| self-audit flips | 17 of 44 hand rulings overruled the mechanical call (`raw/self_audit.json`) | same |

### The native-resolution pass (all 110 rows disposed)

Every `needs_visual_check` row was re-read at native width, one image per call, by seven
striped workers plus myself; each disposition is logged the moment it was made
(`raw/visual-progress*.jsonl`, last row per `n` wins) and folded into the ledger by
`python ledgers/_cmdb_vis.py build` as superseding rows. The pass's own record is
`raw/visual-review.txt`. Flips on those 110 rows:

| pre-pass → final | rows |
|---|---|
| UNCERTAIN → EXCLUDE | 56 |
| UNCERTAIN → INCLUDE | 11 |
| INCLUDE → UNCERTAIN | 4 |
| unchanged (INCLUDE 35, UNCERTAIN 4) | 39 |

Then the safety review over the direction that can lose artefacts (a wrong exclusion is
invisible; a wrong inclusion costs 30 seconds) found and fixed five things:

- **Three verdicts restored — n=302, n=362, n=398.** Each had been flipped to EXCLUDE judging
  the row's *captured* figure alone, while the page carried the decisive figure the worker
  never opened. Re-read at native width from the pages' own asset URLs (kept in
  `raw/_extra/`): 302's "AI as another endpoint in a process" (OpenAI element-template badge on
  two service tasks), 362's two AI-agent BPMN animations (purple AI Agent connector badge on
  "Validate Document"; Operate drawing ad-hoc sub-process "Trade Validation Agent" with its
  tools), 398's "Updated BPMN process model with new HR guardrail step" (ad-hoc sub-process
  "Message Delivery Agent", its tools, "AI Effectiveness Judge", "Check with HR"). These were
  the only two `INCLUDE → EXCLUDE` flips in the pass and one of the 56 `UNCERTAIN → EXCLUDE`.
- **Seven `judgment` flags reset to false** (n=77, 106, 422, 980, 1036, 1302, 1358): the page
  either scores 0 on the census's own AI-term list or the match is a substring ("promptly",
  "prompts", "prompting", "embedding") or the ordinary word "model" in "the BPMN model".
  Leaving them set would have inflated the judgement share with keyword artefacts.
- **n=44's evidence replaced** with the mention it actually dismisses (a judgment=true E2 row
  must quote the dismissed mention; this one had inherited a BPMN quote).
- **n=30's evidence was a paraphrase** — "analyze how the branches of Gateway_injury affect the
  probability that an instance reached claimPaid" fused page prose with two element ids read in
  the figure and matched no page text. `_cmdb_rows.py check` caught it on the re-emit; replaced
  with the page's own sentence, the ids stay in the note.
- **Bookkeeping**: 56 bundles whose final verdict is EXCLUDE moved from
  `corpus/camunda-docs-blog/` to `raw/excluded/` (nothing deleted, nothing rewritten); the four
  verdict-governed frontmatter keys of 53 records synced to the final verdict.

### Why the judgement share is 10.6% and why it is not forced down

152 of 1439 rows: **126 E1-not-bpmn** and **26 E2-no-ai-element**. The 126 are drawn non-BPMN
diagrams (box/block/component/layer diagrams 59, architecture diagrams 37, UML 1, mockups 1) on
pages that do mention AI — the notation call is the judgement, and `prompts/02b` says a drawn
non-BPMN diagram is `judgment: true` while a screenshot of a UI/table/form is `judgment: false`.
The 26 E2 rows each quote the AI mention they dismiss. The visual pass contributed a net **+11**:
it converted 56 rows the pre-pass had left UNCERTAIN (not counted as exclusions at all) into
E2/E1 exclusions, 11 of which are judgement-true. The two honest ways back under the bar would be
to code a drawn architecture diagram as "no artefact" — a false statement — or to claim
hesitation I do not have about a layer or topology diagram, which would dilute the signal the
ceiling protects. `tools/audit.py` and `tools/accepted_shares.json` were not touched; the
operator ruling is queued as **P13**.

Notes for the researcher, beyond the ledger:

- **The final corpus is 64 records plus 56 in `raw/excluded/`.** The cap is the researcher's
  instrument, not mine, so nothing was truncated to fit the 60-example backstop — but the choice
  of which 60 to keep is a live decision, and the ledger's `record` field plus the eight
  UNCERTAIN questions are what it should be made from. The excluded bundles are kept as raw
  evidence, not deleted.
- **Eight rows are `UNCERTAIN`, each with a tailored question** (the queue's front): they are
  figures that stayed genuinely ambiguous after a native read — e.g. n=216, where the AI binding
  rests on prose and colour rather than on a badge read in the figure (`raw/_extra/216_fig1.png`,
  a 5× upscale of the two magenta tasks, is the evidence).
- **Four rows were re-quoted during verification.** The page's own words replaced three
  paraphrases in the rulings (n=570, 1263, 1340) and one sentence that appears nowhere on
  its page (n=1390). The record for n=1390 was regenerated for the same reason.
- **n=271 and n=338 were UNCERTAIN on unreadable animations and are now E2 exclusions**,
  decided by reading the full-resolution frames: 271's demo is a Camunda Modeler pool
  ('Payment process') whose labels are legible at 1400 px and which holds no AI element;
  338's Copilot animation builds a plain human-task/gateway mortgage model, so the AI is the
  diagram's *generator* — the E2 case — not an element inside it. The frames relied on are
  kept in `ledgers/camunda-docs-blog.raw/_gifprobe/`.
- **n=876** was nearly dropped with no verdict: the page links two Atlassian marketplace
  plugin pages whose paths end in `.bpmn`/`.dmn`, which the model route mistook for a
  downloadable model. Judged from its figures instead (E2). Worth knowing if another source
  lists model links: a path suffix is not a model.
- **A page's captured figure is not the page.** The pass's three restorations all failed the
  same way — a contact-sheet capture that happened to be a UI screenshot while the page's real
  BPMN model sat in a later figure. Any future source where a row is captured from one figure
  and judged on it alone should re-run this check: `raw/_extra/_sweep.py`.


