---
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
source_type: vendor developer portal
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: YES (operator ruling B3 2026-09-24: process-to-agent substitution counts)
  C2_native_bpmn20: YES
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES
access: public
population_type: enumerable
population_estimate: 25
effort: small
needs_logged_in_browser: false
status: DONE (elicitation-3a, 2026-09-26; census complete - 1983 rows == population 1983, plus
  204 superseding rows from the recode + self-audit below. `python tools/audit.py
  ibm-developer-watsonx` = 1 problem: judgement-exclusion share 12.9% > 10% ceiling, reported
  not worked around - see "CORRECTION: recode and self-audit")
---

## Criteria evidence

- **C1 UNCLEAR** — https://developer.ibm.com/tutorials/bpmn-to-agents-bob-skills-watsonx-orchestrate/
  (2026-09-22): "A hands-on guide for using Bob skills to transform BPMN process models
  into SOP-driven, fully tested, and deployable watsonx Orchestrate agents". The direction
  of travel here is **BPMN diagram → agent**, i.e. the BPMN model is the *input* that gets
  replaced by an agent, rather than AI being placed *inside* a running BPMN process. That
  is a materially different promotion mode from Camunda's or BAMOE's, and whether it counts
  as "promotes an AI-in-BPMN integration capability" is a judgement I am not authorised to
  make. **Question mirrored in `OPERATOR-TODO.md`.**
  (Ruled YES at Gate 1, B3, 2026-09-24.)
- **C2 YES** — the tutorial's companion repository contains a literal BPMN file:
  `BPMN-order-process.bpmn` in `IBM/oic-i-agentic-ai-tutorials` (surfaced by Google,
  2026-09-22). A `.bpmn` file is decisive C2 evidence.
- **C3 YES** — `developer.ibm.com` served anonymously; the trial links ("Try IBM Bob",
  "Try watsonx Orchestrate on IBM Cloud") are optional and sit beside the free content.
- **C4 YES** — IBM.

## Entry points

- `https://developer.ibm.com/tutorials/bpmn-to-agents-bob-skills-watsonx-orchestrate/` —
  the anchor tutorial.
- The tutorial's own "Related Topics" block links siblings: "Building an event-driven
  agentic AI system with Apache Kafka on Confluent Cloud and watsonx Orchestrate",
  "Build AI agents with IBM Bob and watsonx Orchestrate". Follow them — this is the
  competitor-page trick applied inside a docs portal.
- `https://github.com/IBM/oic-i-agentic-ai-tutorials` — the companion repo containing
  `BPMN-order-process.bpmn`. **Navigate to it from the tutorial page, do not guess the
  path**; the repo name above came from a search-result `cite` and must be confirmed.
- IBM Developer has a tutorial index with topic filters (watsonx Orchestrate, Agentic AI,
  Generative AI, Automation, IBM Bob were the categories printed on the anchor tutorial).
  Use the index, not the search box, so the population is finite.

## Enumeration instructions

1. Build the frontier from the IBM Developer **tutorial index filtered by the "watsonx
   Orchestrate" and "Automation" topics**, then confirm the anchor tutorial and its Related
   Topics siblings are all in it. If the index cannot be paged to a finite total, this
   source degrades to `census: false` / `search-protocol` — say so explicitly in the ledger
   header and log every query verbatim.
2. Follow every GitHub link out of a qualifying tutorial and enumerate `.bpmn` files in the
   linked repo. Those files are artefacts in their own right and they are the highest-grade
   evidence available anywhere in this sample.
3. Small source. If it runs short, that is a real result, not a stopping decision.

## Artefact mechanics

- **Downloadable `.bpmn` XML via the companion GitHub repos** — decisive, prefer it. Use
  the `raw.githubusercontent.com` URL so you get the XML, not GitHub's HTML viewer.
- Tutorial pages themselves carry architecture diagrams (see the "Architecture of the
  automated order processing solution" section). Be careful: an architecture box diagram is
  **not** BPMN, and under the shared rules that is `E1-not-bpmn` — but only if you can name
  it. If the same page also shows the BPMN process model, it is an `INCLUDE`.
- Capture tutorial images at their native asset URL.

## Known gotchas

- **The C1 ambiguity is the whole story of this source.** Do not resolve it yourself in
  Pass 2 either: if a tutorial shows a BPMN diagram whose AI relationship is "this diagram
  becomes an agent" rather than "this diagram contains an agent", the verdict is
  `UNCERTAIN` with `needs_human_ruling: true` and that exact question attached. It is not
  `E2-no-ai-element`.
- The anchor tutorial is long and heavily sectioned ("On this page" with nine steps);
  page-text extraction returns the nav and the abstract before the body. Scroll or read the
  article element specifically.
- IBM Developer and IBM Docs are different properties with different content. BAMOE lives
  on `ibm.com/docs` and has its own assignment file (`ibm-bamoe`); watsonx Orchestrate
  tutorials live here. Do not merge them, and do not dedupe across them.

## Spot checks performed by Pass 1

Spot checks only, not verdicts:

- The anchor tutorial was opened; title, abstract, author line, topic categories and the
  nine-step outline were read. The BPMN diagram itself was not inspected in Pass 1.
- `BPMN-order-process.bpmn` in `IBM/oic-i-agentic-ai-tutorials` was seen only as a Google
  result, **not opened**. Pass 2 must reach it by navigation and confirm it.

## DONE (elicitation-3a, 2026-09-26)

**Population and rows.** `ledgers/ibm-developer-watsonx.jsonl` holds 1983 rows == population
1983: the site's own sitemap (1982 URLs, `https://developer.ibm.com/middleware/v1/sitemap.xml`,
declared in robots.txt) plus the one `.bpmn` file in the two GitHub surfaces the source links
(`IBM/oic-i-agentic-ai-tutorials` blob `bpmn/BPMN-order-process.bpmn`, row n=1983 - it cannot
be reached from the sitemap, so it is appended last). `n` == line number in
`ledgers/ibm-developer-watsonx.frontier.txt`. Rows by verdict: **EXCLUDE 1936**
(E0-no-artefact 1668, E1-not-bpmn 254, E3-duplicate 14), **UNCERTAIN 46**, **INCLUDE 1**, BLOCKED 0.
`judgement_exclusion_share` **12.9%** (256 rows) - above the 10% ceiling in `tools/audit.py`,
so `python tools/audit.py ibm-developer-watsonx` reports exactly one problem; see the
correction note below, which is why the share is what it is and why it is reported rather than
forced down. Review queue: 47 `needs_human_ruling`, 0 `needs_visual_check`.
47 corpus records (`corpus/ibm-developer-watsonx/001`-`047`).

## CORRECTION: recode and self-audit (elicitation-3a, 2026-09-26)

The first pass had a coding fault, and the census is superseded rather than rewritten to fix it
(the ledger is append-only; `rows.py` emits the corrections last, so the last row for an `n`
wins - `tools/audit.py`).

1. **Recode, 190 rows: `E0-no-artefact` + `judgment:false` -> `E1-not-bpmn` + `judgment:true`**
   (`ledgers/ibm-developer-watsonx.raw/html/supersedes.json`). The fault was in `decide.py`'s
   `arch` class, which sent every page whose figure is a drawn architecture / component /
   block / pipeline / agent diagram through the *mechanical* E0 - a code that claims no
   judgement was made, when in fact a notation call was made on every one of them. CLAUDE.md §3
   names an architecture box diagram as an E1 example, and `prompts/02b` states the convention
   directly (a drawn non-BPMN diagram is `judgment: true`; a screenshot of a UI, table, form or
   code listing is `judgment: false`). The 190 rows are exactly the `arch` (156) and `chevron`
   (2) classes plus 32 hand-picked `uiarch`/`noartefact`/`ui` rows whose figure is a drawn
   diagram; each superseding row names the notation it is drawn in. `decide.py` itself was left
   untouched - this ledger supersedes its output.
2. **Self-audit, 14 flips to `UNCERTAIN`, each with a record and a tailored question**
   (`html/flips.json`, records `034`-`047`). Over the recoded figures the audit asked
   `prompts/02b`'s question - *could this be an ordered process with an AI step that a
   researcher might read as BPMN-like?* - and every figure carrying process semantics was
   flipped: start/end nodes (n=299), a split that merges (n=299, n=521), numbered
   activity-labelled steps (n=341, n=404, n=544), activity-labelled connectors (n=377, n=864),
   ordered activity stages (n=261, n=291, n=296, n=484, n=1119), an agent-and-tools flow
   (n=485) and an ordered event sequence (n=1291). Figures whose connected items are systems,
   components, tiers, zones, trees, cards, charts, wireframes, neural-network schematics or
   unlabelled nodes stayed `E1-not-bpmn`. Coverage: all 143 recoded rows whose reviewed note
   mentions a flow, step, stage, order or sequence were re-opened in montages
   (`figs/SA1`-`SA14`); 3 further figures had to be re-fetched and re-rendered before they could
   be judged at all (n=316, n=215, n=245 - two of them are transparent PNGs that render blank
   under a naive RGB conversion, one was stored as an HTML error page); the rest were
   re-checked from their reviewed notes. **One recode was reversed by the audit**: n=1250's
   figure, which the page's alt text calls a node-capacity diagram, is a capture of a
   resource-pool form in a running console, so it stays `E0-no-artefact` with `judgment:false`.
3. **What this does to the numbers**: `E0-no-artefact` 1858 -> 1668, `E1-not-bpmn` 78 -> 254,
   `UNCERTAIN` 32 -> 46, `judgement_exclusion_share` 4.0% -> **12.9%**. The share is *the same
   exclusion decisions, now labelled as the notation calls they always were* - not new
   exclusions. It exceeds the ceiling because this source is saturated with drawn non-BPMN
   diagrams on AI pages; the only ways under the ceiling would be to code a drawn architecture
   diagram as "no artefact" (the fault being fixed) or to claim hesitation I do not have about
   a layer or topology diagram, which would dilute the signal the ceiling protects. **Reported,
   not worked around**: `tools/audit.py` was not edited. The 256 flagged rows are the ones to
   sample, and each names the notation it is drawn in.

The artefact this source was collected for. n=765
(`tutorials/bpmn-to-agents-bob-skills-watsonx-orchestrate/`) is the only INCLUDE: record
`001_bpmn-to-agents-bob-skills-watsonx-orchestrate.md`. The `.bpmn` file it feeds to Bob is
record `002` and row n=1983, UNCERTAIN. The process-to-agent direction is what the operator
ruled on at Gate 1 (B3 2026-09-24); the row-level question is restated verbatim on both rows.

**Where the rest of the material is.** Most of the 1982 sitemap pages are ordinary developer
tutorials, and the source is AI-saturated: 46 pages carry an ordered, AI-bearing drawing that
is not demonstrably BPMN 2.0 (14 of them found by the recode's self-audit) - each is UNCERTAIN
with a tailored question and a record (004-047), so the borderline cases are surfaced for the
researcher rather than resolved by me. A further 254 rows are `E1-not-bpmn`, each naming the
notation its figure is drawn in (`arch` 156, hand-picked `uiarch`/`noartefact`/`ui` 32,
`chevron` 2, and the rest from `decide.py`). No row uses
`E2-no-ai-element`: an exclusion here rests on the figure not being a process artefact (E0) or
on its notation (E1), never on the absence of an AI element.

## Findings the researcher should see

1. **One live bpmn-js canvas in the whole source** (n=765's companion article), no BPMN XML
   anywhere on developer.ibm.com, and no diagram with `bpmn:` semantics except the GitHub file.
2. **108 Learning-Path item pages reproduce an in-population tutorial wholesale** - all of
   their images come from that one tutorial's image folder. They are `E3-duplicate` of the
   tutorial's own row (mapping: `ledgers/ibm-developer-watsonx.raw/html/lp_embed_map.tsv`;
   14 inherit the E3 verdict, the rest inherit the tutorial's E0/E1 reason).
3. **A retired URL family that redirects off-source.** Seven `learningpaths/get-started-watson-assistant/*`
   module URLs and `articles/introduction-watson-assistant/` no longer render on
   developer.ibm.com: they resolve to `cloud.ibm.com/docs/watson-assistant?topic=watson-assistant-*`,
   where the figures live. Row n=1527 records the redirect and judges the figure at the
   redirect target; n=1528/1529/1530/1678/1679/1731/1740/1773/1842 are `E3-duplicate` of it,
   and n=65 records the same for the article. Both rows say where the figure was actually read.
4. **Byte-identical figures re-used across pages** (recorded, not silently deduped):
   n=1811 vs n=1684 (22 identical Kafka figures), n=1838 vs n=1616
   (`credential_rotator_operator_2.png`, md5 `8e81141cb2...`), n=1643's shared asset noted in
   that row's `note` while the row keeps its own E0 verdict.
5. **Two figures exist only as SVG or not as usable files.** n=65's `arch-detail.svg` was
   rendered in my own browser tab to `figs/ZOOM_65_arch-detail_render.png`; the home page's
   `bob_speed.png` (alt "Bob speed") returns S3 `NoSuchKey` 404 - a dead figure, noted on row n=1.

## Audit-relevant tooling notes (raw dir: `ledgers/ibm-developer-watsonx.raw/`)

- The ledger would not build until a **path bug in `rows.py`** was fixed: it read
  `<raw>/decisions.json` while `decide.py` (writer) and `dupe.py` (reader) both use
  `<raw>/html/decisions.json`, so it saw zero decisions and reported 583 unjudged candidates.
  Fixed in `rows.py` only (one line, plus the docstring line that named the wrong path).
- A **record-path truncation mismatch** on record 031 (the ledger named `...for-your-pr.md`,
  `records.py` writes `...for-your-prob.md`) was fixed in the reviewed sheet so the name is now
  the one `records.py` generates.
- The header `note` in the ledger states what was actually reviewed (every candidate-signal
  page's figures via contact sheets; the 72 figure-less pages ruled textually, sheet
  `html/visual.d/20_nofig.json`), not the earlier over-broad "every figure was looked at", and
  the judgement-exclusion share it quotes is the measured 4.0%.

## RESUME

(empty)
