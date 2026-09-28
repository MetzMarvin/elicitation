---
source: flowable
source_name: Flowable (enterprise documentation + vendor blog)
source_type: vendor documentation and blog
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: YES
  C2_native_bpmn20: YES
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES
access: public
population_type: enumerable
population_estimate: 80
effort: medium
needs_logged_in_browser: false
status: DONE (visual pass elicitation-aa, 2026-09-26)
---

## Criteria evidence

- **C1 YES** — https://documentation.flowable.com/latest/reactmodel/bpmn/reference/ai-agent
  (2026-09-22): "The AI Agent Task allows to execute an AI Agent of the type utility,
  document, knowledge and external." Marked "2025.1.01+", i.e. a shipped, versioned feature.
- **C2 YES** — decisive placement evidence: that page sits in the **BPMN reference**, in the
  alphabetical element list between "Adhoc Subprocess" and "Audit", alongside "Exclusive
  Gateway", "Business Rule Task", "Call Activity", "Error Boundary Event". Flowable treats
  the AI Agent Task as a **first-class BPMN element**, like IBM BAMOE and unlike UiPath.
- **C3 YES** — `documentation.flowable.com` and `flowable.com/blog` served anonymously.
- **C4 YES** — Flowable is a long-established BPMN engine (the Activiti fork) with an
  enterprise edition, its own training platform (`training.flowable.com`) and active
  practitioner discourse; its own blog post "BPMN is dead, long live BPMN" was the top
  organic result for two separate grid queries.

## Entry points

- `https://documentation.flowable.com/latest/reactmodel/bpmn/reference/ai-agent` — the AI
  Agent element reference
- The **BPMN Reference index** (parent of the above) — the full alphabetical element list;
  every element page is a frontier item
- The **AI section** of the docs, reachable from the top nav item "AI". Pages confirmed to
  exist by a `site:` sweep on 2026-09-22: "AI Capabilities Overview"
  (`.../ai/ai-introduction`), "Multi-agent Orchestration in CMMN and BPMN"
  (`.../ai/ai-orchestration`), "Advanced Usage Patterns" (`.../latest/ai-orchestration/...`),
  "Agent Introduction", "Creating a Utility Agent" (`.../agent/example`), and the agent
  reference pages "Utility Agent", "External Agent", "Knowledge Agent" plus "Operations"
  (`.../agent/concepts`).
- `https://www.flowable.com/blog` — vendor blog, with Engineering / Business / Releases
  categories. Known AI posts: "Using AI with Flowable", "Bespoke AI agents: Your
  automation's Swiss Army Knife", "Adding AI agents to your business: What you need to
  know", "Flowable 2026.1: Agentic AI, fully orchestrated", "BPMN is dead, long live BPMN".
- `https://training.flowable.com` — course catalogue; "Agentic Process Automation with
  Flowable" exists. Check the access tier: if the course body needs an account, that is
  `free-account` or `BLOCKED`, not an exclusion.

## Enumeration instructions

1. Two sub-populations: the **docs tree** (enumerable from the left nav) and the **blog**
   (enumerable from its category indexes or a sitemap). Record both enumeration methods.
2. Check for `https://documentation.flowable.com/sitemap.xml` and
   `https://www.flowable.com/sitemap.xml` first — cheaper and more complete than walking
   the nav.
3. Enumerate the **whole BPMN reference**, not just `ai-agent`. "Multi-agent Orchestration
   in CMMN and BPMN" implies AI elements also appear in CMMN pages; CMMN is **not** BPMN,
   so a CMMN-only diagram is a legitimate `E1-not-bpmn` — but you must name CMMN as the
   notation, and a page showing both belongs in the corpus.

## Artefact mechanics

- Docs are Docusaurus-style: clean HTML, good text extraction, element reference pages
  carry a properties table (Model Id, Name, Documentation, "Store result variable
  transiently", …). The properties table is strong textual evidence of what the AI element
  can be bound to.
- Diagram images are static assets; capture at native resolution.
- No downloadable `.bpmn` confirmed in Pass 1.

## Known gotchas

- **URL shape is unstable.** `documentation.flowable.com/latest/model/bpmn/reference/`
  redirects to `/latest/reactmodel/bpmn/reference/` and then 404s ("Page Not Found. We
  could not find what you were looking for."). The working path observed is
  `/latest/reactmodel/bpmn/reference/ai-agent`. **Navigate from real links only** — this
  was a guessed URL in Pass 1 and it failed.
- The docs shell has several product tabs (How to / Modeler / Administrator / Developer /
  User / AI / Cloud / Flowable Open Source). "Flowable Open Source" is a different docs set
  from the enterprise one; decide which you enumerate and record it. Both may hold
  artefacts.
- Flowable is the Activiti fork. If Activiti is later admitted as its own source,
  reconciliation must not treat shared lineage diagrams as duplicates.

## Spot checks performed by Pass 1

Spot checks only, not verdicts:

- `/latest/reactmodel/bpmn/reference/ai-agent` — opened; C1 quote and the BPMN-reference
  placement both confirmed from the rendered page.
- `site:documentation.flowable.com "AI Agent" BPMN` — 10 results screened, establishing the
  AI-section page list above.

## RESUME

(empty — census COMPLETE 2026-09-25, `python tools/audit.py flowable` prints `problems: none`)

## Census result (Pass 2, elicitation-74, 2026-09-25)

`ledgers/flowable.jsonl`: header + 1361 rows + COMPLETE footer, 1361 frontier lines.
INCLUDE 2 · UNCERTAIN 250 · EXCLUDE 1109 (E0 1089, E1 14, E2 6) · BLOCKED 0 ·
judgement-exclusion share 1.0 %. `corpus/flowable/`: 255 records, 256 captures.

Two things the researcher should look at before the source is treated as final:

1. **The visual channel is OCR, not sight.** This session receives no image content
   (`Read` on a PNG returns nothing). Every figure claim rests on the page's alt text,
   the asset file name, or RapidOCR labels over the native-resolution asset (1453
   figures read). 250 rows are UNCERTAIN for exactly this reason and are listed in
   `ledgers/flowable.raw/visual-queue.json` (252 entries including two from earlier
   decisions) for the central sighted pass. The two INCLUDE records
   (`001`/`002`/`003`) also rest partly on OCR labels, though their prose certifies
   both BPMN and the AI element on its own.
2. **1089 E0 rows are mechanical** (`judgment: false`): dead link, no figure at all, or
   figures whose alt, file name and OCR labels name no process artefact. Each such row
   carries `figure_note` with the page's actual figure names, so the call is auditable
   without re-opening the page. If the method wants a sighted confirmation of the
   mechanical mass, the cheapest sample is "docs pages whose figures are named
   `*-editor-*` / `*-canvas-*`" (17 pages; 14 judged E1, 3 left UNCERTAIN).

## Visual channel re-tested (elicitation-74, 2026-09-25) — still no image content

Re-tested on request, because it was suggested this session might receive visual
feedback. It does not. Test: two 900×240 PNGs were rendered with random tokens
drawn in 150 pt text, and the tokens were written to a file the agent never read
until after attempting to see them. `Read` on a PNG returns no image content
(the literal string `kwargs`) for all four files tried, and a CDP screenshot of
a page rendering the PNG in the agent's own tab returns only the text "Took a
screenshot of the current page's viewport." The files themselves are fine:
25 608 / 25 156 ink pixels, and RapidOCR read them back as the exact hidden
tokens. The agent could not name either token from looking, so any figure
description it produced would have been reconstructed from OCR text it already
held — i.e. not a sighted check. Smoke artefacts were deleted after the test.

Consequence: `flowable.raw/visual-queue.json` (252 entries, all figures present
on disk) is **unconsumed** and still needs a session that receives pixels. Do
not treat the 250 UNCERTAIN rows as sighted-confirmed.

Structural findings worth carrying into the method chapter: no `bpmn-js`/`djs-*`
rendering exists anywhere on the Flowable site (all BPMN evidence is static images, and
no docs page offers a `.bpmn` download); the AI docs section is dominated by UI
screenshots of the agent model editor; the BPMN reference section publishes essentially
no diagrams; and `training.flowable.com` is not login-gated on its public course pages
(37 live, 84 stale sitemap URLs that now 404 — recorded as E0 with the 404 body quoted).

## RESUME — visual pass `elicitation-aa`, 2026-09-25

Stopped for **context**, not because the source was done. Vision works in this session
(STEP 0 passed; confirmed to elicitation-5a), so this is a genuine sighted pass.

**State: 20 of 252 queue entries settled.** Progress log `ledgers/flowable.raw/visual-progress.jsonl`
has 20 lines, one per entry, `{n, figure_path, outcome, seen}`; `seen` is true for all 20.

**Where to resume:** the queue is processed **in order**, so the next entry is the one after the
last logged one — `ledgers/flowable.raw/visual-queue.json` index 30, `n=223`. The 20 done are
n = 7, 8, 19, 20, 33, 41, 44, 77, 78, 79, 81, 82, 83, 86, 87, 89, 90, 93, 95, 285. Everything
from index 30 onward is untouched.

**Counts so far:** INCLUDE 2, UNCERTAIN 1, EXCLUDE 17 (E1-not-bpmn 15, E2-no-ai-element 2).
Judgement-exclusion share is 1.3% (18/1361 rows), far under the 10% audit cap.

**Tooling, all in `ledgers/flowable.raw/`:** `fig.py` (fetch a page's own figures at native
resolution, contact sheets, crops), `run.py` (`batch <start>`, `sheets <start> <end>`,
`done <n> <outcome>`), `vp.py` (append-only writer for the superseding ledger row, the progress
line, and the move of an excluded record bundle to `flowable.raw/excluded/`). Rebuild a triage
sheet with `python ledgers/flowable.raw/run.py batch 30`.

**Two traps, both already hit once.** (1) A contact sheet is only for triage — twice a 400 px tile
looked like an AI flow and was natively something else (n=33 is a deployment architecture diagram
with nginx/elasticsearch boxes; n=93 is a UI config form). Every decision needs a look at the
figure itself at native resolution or as a crop. (2) 10 captures in `corpus/flowable/` are SVG
logos/badges stored with a `.png` extension and cannot be opened as images — read their source as
text instead of judging the notation.

**No blockers.** Nothing in the source needed a login, captcha or paywall; no `BLOCKED` rows; no
`OPERATOR-TODO.md` entries from this pass.

### Orchestrator method change for the next visual-pass session (elicitation-5a, 2026-09-25)

The first session settled 20 of 252 entries in a whole context window, which is too slow
(~12 more restarts). Use a tiered triage from now on:

1. **Tier A, cheap:** for each entry, first read its `ocr_text` and the figure pixel sizes (PIL,
   no image read). Build contact sheets of **4 tiles at ≥900 px wide** (not 16 tiles at 400 px:
   both early misreads came from 400 px tiles), grouping 4 entries per sheet.
2. **Decide from the sheet only** the unambiguous non-diagram cases: forms, property panels,
   agent/model editor screens, dashboards, logos, photos, code or text listings. Those are
   `E1-not-bpmn` (UI screenshot, judgment:false) or `E0`. Record `"seen":"sheet-900"` in the progress log.
3. **Tier B, native:** anything with diagram-like shapes (circles, diamonds, boxes joined by
   arrows, lanes, stages) is read one image per call at native size and decided under the
   original rules (BPMN+AI → INCLUDE; BPMN no AI → E2; CMMN/DMN/other → E1 named; still unclear →
   UNCERTAIN with a question).
4. Duplicate records for one n have been merged (002/023/064 moved to
   `ledgers/flowable.raw/orphans/`). `tools/audit.py` now flags any record that no current row
   references.
5. SVGs saved as `.png` (about 10): read them as text (`<text>` nodes). If they are logos or badges, they are E0.

## Parallel completion of the visual pass (elicitation-aa, 2026-09-25)

Rather than resume serially, the remaining 230 queue entries were split into **8 contiguous
slices** and handed to eight fresh workers, briefed from `ledgers/flowable.raw/AGENT-BRIEF.md`.
Each worker was gated on a **STEP 0 vision test** before it was allowed to judge anything: read one
designated figure and describe it. All eight descriptions were checked against ground truth and
matched; a worker that could not see images was instructed to write nothing and stop, because a
fabricated sighting is the one unrecoverable failure in this task.

**Why shards.** Eight processes appending to one ledger could interleave partial lines, and the
canonical ledger is the artefact the method's exhaustiveness claim rests on. So each worker writes
its own `ledgers/flowable.raw/shards/<name>.jsonl` plus `<name>.progress.jsonl`, and reads the
canonical ledger read-only for the fields of the row it supersedes. A single writer merges:

    python ledgers/flowable.raw/merge.py            # dry run: validate every shard, write nothing
    python ledgers/flowable.raw/merge.py --write    # append rows, then a fresh footer

`merge.py` validates each shard before merging and **refuses to merge a shard with any problem**:
verdict vocabulary, closed exclusion codes, evidence present, `EXCLUDE` never carrying a record path
or a visual-check flag, `needs_human_ruling` always carrying a question, no `n` judged twice, the
`visual pass elicitation-aa` marker in the note (proof the row went through `vp.py`), and a
`seen: true` progress line behind every row. It also repairs one specific side-effect: an `EXCLUDE`
whose record bundle a worker left sitting in `corpus/flowable/` is shelved at merge time. Rows go in
appended *after* the old footer, with a recomputed footer appended last, since the audit takes the
last footer it sees and the ledger stays append-only.

To finish: run the merge, then `python tools/audit.py flowable` must print `problems: none`, then
set this file's status to `DONE (visual pass elicitation-aa, 2026-09-25)`.

### Amendment 2026-09-25: do not stop for context

Rule change relayed from the researcher via `elicitation-5a`: never stop or write a RESUME block
because context is filling up. The harness auto-compacts, so work continues through a compaction.
After one, re-read `ledgers/flowable.raw/visual-progress.jsonl` (and, for a shard worker, its own
`shards/<name>.progress.jsonl`) and this file, then continue with the next queue entry. The only
legitimate stop is the queue being exhausted and `python tools/audit.py flowable` printing
`problems: none`.

This supersedes the earlier "RESUME when context runs low" instruction in this file and in
`CLAUDE.md` section 8 for this source. `ledgers/flowable.raw/AGENT-BRIEF.md` has been updated to
match, and all eight shard workers were notified.

### Glyph reference established by sight (2026-09-25) — corrects one census finding

The sighted pass established what Flowable's AI element looks like when it is **drawn**: a small
**robot-face glyph** (rounded square, two dots, a top bar) at the top-left of a plan item. Exactly
one instance exists in this corpus, on **n=720** (`/latest/user/inspect`, figure
`inspect-execution-tree`): a CMMN case "Classify documents" whose *Payout* stage holds a plan item
labelled **AI Agent**. It is CMMN, so the artefact is `E1-not-bpmn` even with the AI inside it, and
the page's BPMN half (`Agent Service Process`: `Get Weather` service task → `Review Weather` user
task) shows no AI glyph — which is why n=720 stays UNCERTAIN: its instance invoked the agent
`E2E Weather Agent`, but no figure exposes the binding.

Two consequences for the method chapter:

- The census finding "the AI docs section publishes no rendered diagram" stands, but "no AI element
  is ever rendered" was too strong. The element's glyph is renderable and appears once, in CMMN.
- **Glyph absence on a BPMN canvas does not rule out an AI element.** The method's strongest
  positive (n=95, record `001`) is plain service tasks whose AI lives only in the Service Registry
  binding — nothing in the shape says AI.

Two other Flowable task glyphs identified by comparison, both useful for future sighted passes: a
**speech bubble** = Engage message task (n=496 `Post initial message`, and n=218 `Alert`), and a
**page/document outline with a diamond inside** = document task (n=218 `Create…`, consistent with
that screen's "Generate document" panel). A **lightning bolt in a circle** stays the error boundary
event warned about in the brief; a **clock circle on a task border** is a timer boundary event, and
is decisive BPMN evidence (CMMN has none) — that is what settles n=218's notation as BPMN 2.0,
together with two X-in-diamond exclusive gateways.

### A second rendered AI element, and the source's strongest record (n=787)

The visual pass found the source's strongest positive and reversed a census UNCERTAIN:
**n=787** (`www.flowable.com/blog/business/flowable-ai-service`) publishes a rendered **BPMN 2.0**
diagram — captioned "Simplified process with Flowable's AI service" — with **two pools**
(`Process Customer Request` with lanes `System` and `Help Desk Member`), an envelope **message start
event** `Email received`, four automation tasks (**`Recognize intent`**, **`Analyze sentiment`**,
**`Extract data according intent`**, **`Process intent automatically`**) each carrying a small
**rocket** task-type marker, X-*exclusive gateways* labelled `Intent recognized?` /
`Bad sentiment?` / `Process manually?`, three person-icon **user tasks**, and an end event. The
rocket-marked tasks call the AI-type service definition the same page publishes (`Service: Sample AI
Service`, Service type **AI**, operations `recognizeIntent` / `getSentimentScore`), whose LLM prompt
editor is also published. This is the method's "AI element visible only as a task property or
binding" case, but with a task marker on top of it.

Consequences for the method chapter:

- The census's "**no rendered BPMN canvas anywhere** on the Flowable site" is **too strong**. It
  holds for the docs tree (checked by four shards independently), but the **blog** publishes one,
  and it is the record that carries the source's best artefact.
- The AI task marker is a **rocket**; the AI Agent element is a **robot face** (n=720, CMMN). A
  sighted pass can therefore sometimes see the AI *in the shape*, which the AI-docs pages never
  allowed.
- `Process intent automatically` is drawn with a **thick border** while its three siblings are not
  — thick borders are BPMN call-activity styling, so a reviewer should not read it as a plain task.

### Gap-fill 2026-09-25: 32 queue entries were initially unowned

The eight slice ranges were handed out as queue-index ranges and left **32 entries unowned** at
their boundaries — indices 34, 35, 47–49, 99–108, 164–166, 195, 212–224 (n = 238 … 1221). This was
an error in the assignment, not in any worker's execution: each worker correctly judged exactly its
own range and reported its boundaries accurately.

The gap was found by auditing coverage programmatically — the queue minus every shard row minus
every hand-pass row, written to `ledgers/flowable.raw/gaps.json` — rather than by trusting the
slice table, and it would otherwise have silently broken the exhaustiveness claim. The entries it
hid were not the unimportant ones: they included five **Flowable open-source BPMN/CMMN
documentation** pages (`bpmn/ch02-GettingStarted`, `ch07a-BPMN-Introduction`, `ch07b-BPMN-Constructs`,
`ch09-JPA`, `cmmn/ch06-cmmn`) and three AI blog posts (`ai-assisted-content-analysis`,
`ai-assisted-process-and-case-modeling`, `process-intelligence`) — precisely the pages most likely to
publish a rendered diagram with an AI element.

The 32 were redistributed to the five workers still live (s1 5, s3 6, s5 7, s6 5 — one was dropped
because the worker's own slice had reached it by then — and s7 8) and judged under the same rules.

Lesson for the method chapter: slice boundaries must be **derived from the queue length**, not
hand-written, and coverage must be asserted as `set(queue_n) == set(rows_n)`, never inferred from a
slice table. The same assertion has to be re-run after the merge, before the source is called done.

### Closing 2026-09-26: the last 10 entries judged by hand, pass complete

Two workers (s5, s7) still owned ten queue entries when the operator stopped every agent for API rate
limits, and the harness refuses to resume a user-stopped agent. Rather than leave coverage at 242/252
or spawn an unrequested replacement, I judged those ten myself by sight, from the census captures plus
each page's own assets fetched at native resolution:

- idx 107 n=594, idx 108 n=596 → `E1-not-bpmn`, judgment false (editor/config UI screenshots)
- idx 217 n=1183 → `E1-not-bpmn`, false (marketing photograph; the monitor shows the Work task UI)
- idx 218 n=1185 → `E1-not-bpmn`, **true** (nine abstract marketing illustrations, none notation)
- idx 219 n=1197 → `E1-not-bpmn`, false (product dashboard screenshot + marketing photograph)
- idx 220 n=1198, 221 n=1204, 222 n=1205, 223 n=1207 → `E2-no-ai-element`, false (open-source BPMN manual)
- idx 224 n=1221 → `E1-not-bpmn` naming **CMMN 1.1**, true (open-source CMMN manual)

Three method-relevant findings from that work:

- **The open-source manual is the negative control this source needed.** The four BPMN manual pages are
  genuine BPMN 2.0 (event circles, X-marked gateways, person/gear task markers, `${loanRequest.approved}`
  branch conditions) with no AI element, and their body text contains **zero** AI/LLM/agent tokens
  (34 102 / 20 071 / 241 309 / 13 331 body chars scanned on the live pages, 0 hits each). Flowable's AI
  elements live in the enterprise product; its BPMN reference is plain BPMN. The CMMN manual page (n=1221)
  is CMMN 1.1: folder-shaped plan model with its tab, cut-corner stages, plan items, milestone, and
  sentry diamonds straddling stage borders, labelled as such by the figures themselves.
- **The rocket glyph is not an AI marker.** n=594's palette list shows the **HTTP task** with the same
  rocket seen on the enterprise AI-service tasks, so within Flowable the rocket marks a typed/connector
  task. The n=787 INCLUDE does not rest on it: it rests on the tasks' names matching the operations of a
  service definition of type "AI" plus the page's own "AI service invocation" prose.
- **One unusable census capture, recorded so it is not mistaken for an empty page:** `223_flowable-com-index.png`
  (n=1197) is the page's `logo.svg` stored with a `.png` extension and cannot be opened as an image.

`ledgers/flowable.raw/merge.py`'s conflict guard was corrected during the merge: it had compared each
worker row against **any** canonical row, so all 240 census rows that awaited a sighted ruling were
reported as disagreements. It now conflicts only with a canonical row that is itself a visual-pass row
(`supersedes_row`), and reports the census-level supersessions separately (214 of them).

Final state: `python tools/audit.py flowable` → population 1361, rows 1361, INCLUDE 3, UNCERTAIN 11,
EXCLUDE 1347 (E0 1116, E1 175, E2 54, E3 2), judgement exclusions 92 (6.8 %), visual-check 1, rulings 11,
`problems: none`.
