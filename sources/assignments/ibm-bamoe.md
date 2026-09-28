---
source: ibm-bamoe
source_name: IBM Business Automation Manager Open Editions (BAMOE) documentation + IBM Community
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
effort: medium
needs_logged_in_browser: false
status: DONE (elicitation-6f, 2026-09-25; 117 docs topics + 18 community + 2 adjacent surfaces = 137 rows, audit problems: none; 7 INCLUDE + 2 UNCERTAIN, 9 records)
---

## Criteria evidence

- **C1 YES** — https://www.ibm.com/docs/en/ibamoe/9.3.x?topic=ia-using-ai-agent-tasks-in-workflows-tech-preview
  (2026-09-22): "The AI Agent task (technology preview) in the BPMN Editor, powered by
  Langflow, allows you to add AI Agents in the BPMN Workflows." BAMOE also ships a second
  named feature, "Using Gen AI Tasks in Workflows", and an MCP server
  ("Exposing BAMOE capabilities to AI agents through MCP Server (Tech Preview)").
- **C2 YES** — same page: "Drag and drop the AI Agent node from the palette" and "Reuse
  your agents or flows in different BPMN Workflows." This is a **dedicated native BPMN node
  type** in the vendor's own BPMN editor, which is the strongest form of C2 evidence in the
  whole sample.
- **C3 YES** — `ibm.com/docs` served anonymously; no login prompt, no paywall.
- **C4 YES** — IBM. BAMOE is the supported commercial edition of the jBPM/Kogito lineage
  and is documented across releases 8.0.x through 9.5.x.

## Entry points

- `https://www.ibm.com/docs/en/ibamoe/9.3.x` — docs root. The table of contents observed on
  2026-09-22 is the population outline: Release notes, Overview and Architecture,
  Installing, Upgrading, Getting started, Available features, Developing Decisions Rules
  and Test Scenarios, **Developing stateful Workflows**, Building and deploying Business
  Services, Managing and Monitoring Business Services, **Integrating with AI**, Reference,
  Support, Notices.
- The **"Integrating with AI"** branch is the dense part; its children observed in the ToC:
  - "Using Gen AI Tasks in Workflows"
  - "Exposing BAMOE capabilities to AI agents through MCP Server (Tech Preview)"
  - "Using AI Agent Tasks in Workflows (Tech Preview)"
- "Developing stateful Workflows" contains "Authoring Workflows with BPMN" (surfaced by a
  `site:ibm.com` search on 2026-09-22) — that is where the worked BPMN diagrams live.
- **Version switcher**: 9.5.x, 9.4.x, 9.3.x, 9.2.x, 9.1.x, 9.0.x, 8.0.x. The AI features
  are newest, so enumerate the **latest** release (9.5.x) and record which one you used.
- Companion channel, treat as part of this source: the IBM Community blog, e.g.
  https://community.ibm.com/community/user/blogs/adarsh-v-k/2025/11/28/introducing-ai-agent-task-advanced-ai-integration
  and "Introducing the BAMOE Gen AI Task for workflows". Enumerate via the IBM Community
  search for BAMOE rather than by guessing blog URLs.
- Also present: a **VS Code marketplace** extension, "BAMOE Developer Tools". If it ships
  sample `.bpmn` files, those are artefacts — check it.

## Enumeration instructions

1. Frontier = the full ToC of one BAMOE release (prefer 9.5.x), **plus** the IBM Community
   BAMOE blog posts found by search. Record the two enumeration methods separately in the
   ledger header.
2. Do not restrict to the "Integrating with AI" branch: "Authoring Workflows with BPMN"
   under "Developing stateful Workflows" is where complete diagrams appear.
3. Each ToC entry is addressed by a `?topic=` query parameter, not a path
   (`.../ibamoe/9.3.x?topic=ia-using-ai-agent-tasks-in-workflows-tech-preview`). Extract
   these from the ToC DOM; the slugs are not derivable from titles.
4. The IBM Community half of this source has **no complete index** — it is a
   `search-protocol` stream grafted onto an `enumerable` one. Log every query verbatim in
   the ledger header `queries` array, and say in the header note that the docs half is a
   census and the community half is a search protocol.

## Artefact mechanics

- Docs diagrams are static images plus prose that names palette elements explicitly
  ("Drag and drop the AI Agent node from the palette", "Navigate to the property panel of
  the AI Agent task"). Prose is strong evidence here because the node type is named.
- Because BAMOE has a **dedicated AI Agent node type**, the diagram itself carries a
  visual signal — unlike UiPath. Record that contrast; it is directly relevant to the
  detectability argument in `notes/uipath-promotion-pattern/analysis.md`.
- Check the IBM Community posts for downloadable `.bpmn` attachments or GitHub links;
  `<bpmn:process>` XML would be decisive evidence.

## Known gotchas

- `ibm.com/docs` is a single-page app: the `?topic=` parameter drives the content, so the
  browser URL and the rendered content can desynchronise if you navigate too fast. Wait for
  the content pane, and verify the rendered `h1` matches the topic you asked for before
  recording evidence.
- German mirrors exist ("Verwendung einer Gen AI-Aufgabe in der BPMN"). Stay on `/en/` and
  do not record the mirror as a separate artefact — that would be an `E3-duplicate`.
- Tech-preview pages can disappear between releases. Record `accessed` dates carefully.
- BAMOE, jBPM, Kogito and Aletyx share a lineage and will show similar diagrams. That is
  **not** `E3-duplicate`: never dedupe across sources.

## Spot checks performed by Pass 1

Spot checks only, not verdicts:

- `?topic=ia-using-ai-agent-tasks-in-workflows-tech-preview` — opened; AI Agent node type,
  Langflow binding and property panel described.
- `site:ibm.com BAMOE "Gen AI task" BPMN` — 10 results screened, confirming the sibling
  pages "Using a Gen AI task in BPMN", "GenAI Task WorkItemHandler" and "Authoring
  Workflows with BPMN" exist.

## Census record (elicitation-6f, 2026-09-25)

**Status DONE. `python tools/audit.py ibm-bamoe` → `problems: none`. 137 rows == population 137 ==
137 frontier lines; ledger `ledgers/ibm-bamoe.jsonl` opened with a header and closed with
`status: DONE`.**

**Enumeration, in the two halves the assignment asked to keep separate** (both recorded in the ledger
header's `enumeration_method`; the queries verbatim in `queries_log`).

1. **Docs half — a census.** The ToC was read from IBM's own docs API
   (`https://1.www.s81c.com/docs/api/v1/toc/ibamoe/9.5.x?lang=en`, `productKey SSFVHI5_9.5.0`):
   **117 topics**, an exact count from the ToC itself — no facet, no keyword filter. Every topic was
   fetched through the content API (`/api/v1/content/<href>?parsebody=true&lang=en`) and screened
   offline (`ledgers/_bamoe/screen.json`, content in `content_9.5.x.json`, 324 figures decoded into
   `ledgers/_bamoe.raw/`). Versions 9.3.x/9.4.x/9.6.0 publish the same topics as a version facet and
   are not counted twice; they are covered through the community half's release posts.
2. **Community half — a search protocol, not a census.** The frontier is "the IBM Community BAMOE
   posts found by search", so the population *is* the query set, logged verbatim. **14 posts + 2
   pages + 2 webinar decks**; all 42 post figures were downloaded and classified by contact sheet
   (`ledgers/_bamoe_comm/figs/`), and both decks were rasterised page by page (32 and 20 pages).
3. **Two adjacent surfaces** the assignment names: the **VS Code marketplace listing** and the
   **accelerator GitHub repository** linked from the community library page = 2 rows.

`population_size: 137`.

**Verdicts.** **7 INCLUDE**, 2 UNCERTAIN (both with `needs_human_ruling` and a corpus record),
128 EXCLUDE (`E0-no-artefact` 104, `E1-not-bpmn` 15, `E2-no-ai-element` 9), 0 BLOCKED. Judgement
exclusions **9 of 137 = 6.6 %** (inside the 10 % gate), all enumerated in the footer's
`judgement_rows` / `figures_looked`.

**The AI node type is the finding, and it is the contrast the assignment predicted.** Unlike UiPath
(where the AI lives in a task's *binding*), BAMOE ships **dedicated AI BPMN node types** in its own
BPMN editor, so the diagram carries a visual signal: the palette's **AI** group holds **Gen AI Task**
(a sparkle glyph) and **AI Agent Task** (a robot glyph). The seven INCLUDEs split along exactly that
line:

- **Wired into a process** (the AI element is an activity in the control flow): record `004` (n=119,
  the 9.3.0 announcement: the hiring process's "Create Offer" task *carries the sparkle*, panel filled
  with watsonx / `ibm/granite-3-2-8b-instruct` / temperature 0.7 / 500 tokens / the offer-letter
  prompt); record `005` (n=120, the 9.3.1 insurance-claims process — the strongest single diagram in
  the source: **two AI node types of different kinds in one process**, "Gen AI Task: Summarize Claim
  Documents" (sparkle) and "Agentic AI Task: Research & Investigation" (robot, Langflow account
  `Langflow - 9december`, agent `Tax document`), sitting on either side of a **DMN decision** "Claim
  Complexity Assessment" and its exclusive gateway); record `008`
  (n=134, the 9.3.1 deck p29: start → "Open PR" → **"Review PR"** (AI Agent Task, Langflow-bound via
  `bamoe.workflow.ai-agent-task.provider.langflow.*`) → end); record `009` (n=135, the TechXchange p12
  Gen AI Task demo: start → **"Generate some content"** (sparkle) → end — the minimal case, the AI task
  is the *only* activity in the process).
- **Node type only — placed on the canvas, not yet connected**: record `006` (n=132, the AI Agent Task
  drag-and-drop animation) and record `007` (n=133, the Gen AI Task animation, node dropped *below* the
  hiring process with no sequence flow reaching it). Both are INCLUDE — an AI node type of a BPMN 2.0
  editor on a BPMN 2.0 canvas, published by the vendor as the introduction of that node — but the
  "connected vs merely placed" distinction is recorded in both records so the researcher can narrow the
  criterion without reopening the images.
- **The docs half's two UNCERTAINs** (n=78 record `002`, n=107 record `003`) are the source's own
  anchor pages for those node types: the BPMN editor's palette and the AI Agent task's property panel,
  documented in prose and panel screenshots with **no published process model** — the same
  palette-of-in-process-elements boundary question as creatio record 005.

**The corpus's cleanest negative comes free with record `009`.** Deck page 10 shows the same hiring
process at **9.2.0** with two *plain* tasks ("Generate base Offer" → "Log Offer") and no AI anywhere,
while record `004` shows that position holding the Gen AI task. That gives an explicit before/after
pair (9.2.0 deck p10 → 9.3.0 record 004), with record `007` as the intermediate state — a negative
control for "full BPMN 2.0 diagram with no AI element" (events, exclusive gateways, timer boundary
events, compensation, a sub-process). It is *not* a separate row: the deck is one enumerated item; the
pre-AI diagram is kept at `ledgers/_bamoe_comm/tx_hi_10-10.png` for lifting if wanted.

**Corpus records (9), all in `corpus/ibm-bamoe/`:** `001`–`003` = the docs half (n=105 INCLUDE;
n=78, n=107 UNCERTAIN + ruling question), `004`–`007` = the community posts (4 INCLUDE), `008`–`009`
= the two decks (2 INCLUDE; `008` also `needs_visual_check` on its p26 illustration).

**Review queue: 3 rulings, 1 visual check, 0 blocked.** The two docs rulings ask the palette/panel
boundary question; record `008`'s ruling is confined to deck p26, a stylised BPMN-shaped illustration
with no readable labels at any rasterisation and no visible AI element (capture attached at 220 dpi so
the call can be made by eye); its `needs_visual_check: true` sits on that same row, which is why the
visual-check count is 1 rather than 0.

**Not-BPMN material named in the ledger, per the `E1` rule:** architecture box diagrams (n=10, deck
p7), a topology diagram (n=12), the WS-HumanTask 1.1 lifecycle state diagram (deck p24, footer
`docs.oasis-open.org/bpel4people/ws-humantask-1.1-spec-cs-01.html`), DMN/DRD/DRL and Test Scenario
figures in the decisions branch, and product screens.

**Provenance gap, recorded rather than papered over.** Both decks were downloaded from the community
platform's attachment endpoint (`DownloadDocumentFile.ashx?DocumentFileKey=…`, verified to resolve
HTTP 302 → `higherlogicdownload.s3.amazonaws.com/IMWUC/<key>_file.pdf`). The *referring page* was not
preserved in this session's captures, so it is not claimed in either record — see the honest wording
at the end of records `008` and `009`.

**Gotcha the assignment warned about, and how it was handled.** `ibm.com/docs` is a SPA whose
`?topic=` parameter drives the content; instead of racing the rendered pane, the ToC and every page
body were read from the docs API directly (text + figure list), and the human `?topic=` URL is
recorded per row from the ToC's own `href`. The German mirror was never enumerated (`/en/` throughout),
so no `E3-duplicate` arises from it.

