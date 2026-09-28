---
source: creatio
source_name: Creatio (Creatio Academy: process elements reference, Creatio.ai)
source_type: vendor documentation
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: YES
  C2_native_bpmn20: YES
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES
access: public
population_type: enumerable
population_estimate: 30
effort: medium
needs_logged_in_browser: false
status: DONE (elicitation-6f, 2026-09-24; Academy + marketplace + landing, 2194 rows, audit problems: none)
---

## Criteria evidence

- **C1 YES**: https://academy.creatio.com/guides/no-code-customization/bpm-tools/process-elements-reference/system-actions/call-creatio-ai-element
  (2026-09-24): "Use the Call Creatio.ai business process element to integrate Creatio
  Sub-agents into any business process." The page continues: "When the business process
  activates the Call Creatio.ai element, the element executes the following actions: Call
  and execute the requested skill… Receive response from Creatio AI."
- **C2 YES**: https://academy.creatio.com/guides/no-code-customization/bpm-tools/business-process-setup/process-designer-basics:
  "Gateways that activate one ore more outgoing flows depending on the gateway type:
  'exclusive OR,' 'inclusive OR,' 'parallel AND.'" Academy result titles also include
  "Import *.BPMN files" and "Add a BPMN business process to a section".
- **C3 YES**: anonymous. **C4 YES**: an established CRM/BPM vendor.

## Promotion mode

A **dedicated native node type** ("Call Creatio.ai", under System actions in the process
elements reference) that calls a "Sub-agent" / "skill". Same family as BAMOE, Flowable and
ProcessMaker.

## Entry points

- The anchor page, and its siblings under `process-elements-reference/` (the full element
  palette)
- "Develop Creatio Sub-agent" (linked from the anchor, not opened)
- `www.creatio.com/page/bpmn` ("Business Process Modeling in BPMN Notation", not opened)
- Creatio Marketplace (`marketplace.creatio.com`, **not verified**; find it via links)
  may hold AI process templates. It is a possible second population.

## Enumeration instructions

1. Enumerate the `process-elements-reference` subtree and the Creatio.ai / Sub-agent
   development subtree from the Academy nav.
2. Check the Academy for example processes that use "Call Creatio.ai".
3. `community.creatio.com` is separate and non-enumerable. Scope it per B4.

## Known gotchas

- Community thread "Can Creatio.ai generate a complete Business Process…" is design-time
  (E2).
- The Academy is versioned. Pin the version and record it.

## RESULT (elicitation-6f, 2026-09-24; revised same day)

**Census complete on the Academy surface, plus the two named second surfaces.** Population **1657
rows**, all audited (`python tools/audit.py creatio` → `problems: none`). Verdicts: **EXCLUDE 1652**
(E0 875, E1 475, E2 302), **INCLUDE 2**, **UNCERTAIN 3**; judgement-exclusions 11 (0.7%), blocked 0,
visual-check rows remaining 0. Surfaces: `academy` 306, `academy-outside-scope` 1350,
`creatio.com-landing` 1; the marketplace is enumerated as its own surface (below).

The Academy population is the **whole** enumerated v10 guide tree, not a keyword-narrowed subset:
1653 fetched `/guides/**` pages (BFS run to exhaustion) + the 3 in-scope links that 404 = **1656
items, each with a row**. 1067 of those were judged mechanically from the cached HTML
(`judged_from: bfs-cache`) by `ledgers/_creatio_backfill.py`; the 38 rows whose figures the caption
classifier could not settle were then looked at directly (contact sheets) and superseded: 35 E1, 3
E0, 2 E2, 1 promoted to INCLUDE (record 004). The three in-scope prefixes were a platform facet, so
the unfiltered check was made the other way round: all 1347 out-of-scope pages were keyword-scanned
too, and every one carrying an AI/LLM token in its article region has a row. Known false positive of
the AI screen: the keyword `auto-generated`, which names the Auto-generated page element.

Second surface 1 — `www.creatio.com/page/bpmn`: **not blocked**. The Incapsula interstitial answers a
plain GET only; the page loads in a real browser, and it was enumerated and judged (row `n=1657`,
`surface: creatio.com-landing`, record `005`). It publishes eight full BPMN process diagrams (all
looked at) and five element-palette figures; none of the diagrams contains an AI element, while the
"System Actions in Creatio" palette figure lists **Predict data**. Verdict UNCERTAIN +
`needs_human_ruling` (the palette-of-in-process-elements boundary question, same shape as records
002/003).

Second surface 2 — `marketplace.creatio.com`: enumerated from the catalogue's own JSON endpoint
(`POST /search/ai`, `ai_filter: null`) which reports `numFound: 524` — the exact unfiltered total;
listing pages are server-rendered and cached; the blog index walks to exhaustion at 13 articles. See
`ledgers/_creatio_mp_crawl.py`, `ledgers/_creatio_mp_rows.py` and the ledger's `surface: marketplace`
/ `marketplace-blog` rows.

Corpus records (5):
- `001_implement-prediction-models.md` (n=41) — INCLUDE: BPMN process "Account added → Predict account
  category → end", the task being the *Predict data* ML element.
- `004_handle-system-level-data-creatio-ai.md` (n=500) — INCLUDE: the "Summarize contact information"
  process, published three times as a diagram, with the task **Run the AI Sub-agent** (a Sub-agent
  element calling the "Contact summary" Creatio.ai agent) and the auto-generated page task after it.
- `002_call-creatio-ai-element.md` (n=151), `003_predict-data-process-element.md` (n=159) and
  `005_business-process-modeling-in-bpmn-notation.md` (n=1657) — UNCERTAIN with `needs_human_ruling`:
  the source's own anchor pages for the in-process AI elements, documented in prose and element panels
  with **no published process model**, and (record 005) the vendor's BPMN showcase, whose only
  AI-bound content is the element palette. Same boundary question as oracle-oic record 032.

