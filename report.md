# Pass 2 report: per-source census of AI elements in BPMN 2.0 artefacts

Step 1 (use-case elicitation) of the thesis method. Pass 2 ran from 2026-09-24 to 2026-09-27.
This report was written 2026-09-28.

All numbers are computed from the ledgers as they stand on disk. The last row per `n` counts
(superseded rows excluded). The computation script is `ledgers/_report/pass2_stats.py` and its raw
output is `ledgers/_report/pass2_stats.json`.

---

## 1. Summary

| | |
|---|---|
| Sources that qualified at Gate 1 | 27 |
| Ruled out during Pass 2 | 1 (Appian, operator ruling C2 "too proprietary", 2026-09-25) |
| Sources in scope for Pass 2 | 26 |
| Sources censused to completion | **25** |
| Not censused | 1: `uipath-marketplace` (frontier of 2,326 listings enumerated, not judged) |
| Partially uncovered | `camunda-docs-blog`: the docs half (`docs.camunda.io`) refuses this machine's connections, so 4 entry points are BLOCKED and the docs tree was never enumerated |
| **Items enumerated and judged (ledger rows)** | **22,731** |
| INCLUDE | **209** |
| UNCERTAIN | **381** |
| EXCLUDE | 22,133 |
| BLOCKED | 8 |
| Corpus records written (one per INCLUDE/UNCERTAIN) | **590** |
| Open questions for the researcher (`needs_human_ruling`) | 358 |
| Open visual checks (`needs_visual_check`) | 64 |
| Judgement exclusions (the rows where a false negative can hide) | 1,276 (5.6% of all rows) |
| Files saved as evidence (`ledgers/` + `corpus/`) | 50,667 files, 7.4 GB |

Every enumerated item has a row with a verdict and a verbatim quote. `python tools/audit.py <slug>`
prints `problems: none` for all 25 ledgers. For two of them the judgement share is above 10% and was
accepted by the operator (section 5.3).

---

## 2. How Pass 2 was conducted

### 2.1 Roles

| Session | Model / backend | Role |
|---|---|---|
| `elicitation-5a` | Claude Opus 5.5 (Anthropic API) | Orchestrator. Wrote the briefs and conventions, audited every returned ledger, sent defects back, patched `tools/audit.py`, relayed operator rulings. Judged directly only the 2 QuantumBPM figures (record 002 confirmed INCLUDE, 003 changed to E2) and 2 UiPath Maestro rows (error boundary events misread as agent markers, changed to E2). |
| `elicitation-3a` | Claude Code, Ollama-backed model | Worker: bizagi, atamya, citeck-ecos, quantumbpm, newgen, aletyx, ibm-developer-watsonx, frends-docs, firestart. It also had Appian until the operator ruled Appian out. |
| `elicitation-6f` | Claude Code, Ollama-backed model | Worker: oracle-oic, creatio, scheer-pas, bonitasoft, ibm-bamoe, processmaker, flowx-ai, trisotech, camunda-docs-blog. Ran 3 helper agents for the Camunda blog image skim. |
| `elicitation-74`, later `elicitation-aa` | Claude Code, Ollama-backed model | Worker: ifs-cloud-docs, loyjoy, cib-seven, uipath-maestro-docs, flowable (census). After a restart it did the Flowable visual pass with 8 shard helper agents, then camunda-marketplace. It had no shared-browser tools, so it used curl plus native image reads. |
| `elicitation-15` | Claude Opus 5.5, operator's UiPath-logged-in browser | Started `uipath-marketplace`: enumerated the 2,326-listing frontier and began the crawl. The session exited before judging anything. |

### 2.2 Protocol

The binding rules are `CLAUDE.md`, `prompts/02_source-census.md`, `prompts/02b_worker-adapter.md`
and `prompts/02c_parallel-workers.md`.

1. **Enumeration before judgement.** Each source's population came from the vendor's own index
   before any item was judged: a sitemap, `llms.txt`, a docs table-of-contents API, a marketplace
   JSON endpoint, or a GitHub tree. This population was written to `ledgers/<slug>.frontier.txt`
   and the ledger header. Keyword narrowing was forbidden. Facets were used only as cross-checks.
2. **One ledger row per enumerated item**, appended as the item was judged. There are three
   verdicts plus BLOCKED. Exclusion is allowed only under E0 (no artefact), E1 (not BPMN, notation
   named), E2 (no AI element inside the process, dismissed AI mention quoted) or E3 (duplicate
   within the source). Corrections were appended as superseding rows; no line was ever edited.
3. **When in doubt, UNCERTAIN.** Every INCLUDE and UNCERTAIN item received a record in
   `corpus/<slug>/` with an evidence capture. Every UNCERTAIN carries the exact question for the
   researcher.
4. **Tiered processing.** This is the basis of section 4.
   - Scripts fetched and screened whole populations: page text, figure inventory, AI lexicon, hash
     duplicates.
   - Agents read the pages that mention AI or carry a process artefact.
   - Agents looked at figures. Contact sheets (4 tiles, each at least 900 px wide) were used for
     forms, UI screenshots and logos. Anything diagram-shaped was read one image per call at
     native resolution.
   - Workers without image input used OCR (RapidOCR) plus a visual queue. The queue was later
     settled by sighted sessions.
5. **Shared browser discipline.** One Chrome, reached through `chrome-devtools-mcp` (`cdp1`,
   port 9222). Each worker used its own tab. Pages were loaded at about one per second, and work
   in vendor tools was read-only. There were no logins, no form submissions and no git writes.
6. **Audit gate.** A source counts as DONE only when `python tools/audit.py <slug>` prints
   `problems: none`.

### 2.3 What the audit enforces

The checks were added during Pass 2 as defects surfaced:

- ledger rows == population == frontier lines;
- closed exclusion codes;
- E3 must carry `duplicate_of`;
- EXCLUDE never combined with `needs_visual_check`;
- valid `capture_quality`;
- every INCLUDE/UNCERTAIN row has a record on disk;
- no orphan or duplicate record numbers;
- raw evidence kept out of `corpus/`;
- an E1 claim on figures nobody looked at is flagged (added 2026-09-25 after FlowX);
- judgement-exclusion share at most 10%, unless accepted by the operator in
  `tools/accepted_shares.json` (added 2026-09-26).

### 2.4 Operator rulings made during Pass 2

| Date | Ruling |
|---|---|
| 2026-09-24 | Workers are Ollama-backed Claude Code sessions. The orchestrator stays on the Anthropic API to save cost. |
| 2026-09-25 | Workers must not stop because context is filling up. The harness auto-compacts, and work continues through a compaction. |
| 2026-09-25 | Appian ruled OUT (C2, too proprietary). |
| 2026-09-26 | No YouTube, no video or audio playback. Video-only items stay UNCERTAIN, judged only on what the host page shows. All verdicts derived from already-watched Trisotech recordings were discarded. |
| 2026-09-26 | ibm-developer-watsonx judgement share of 12.9% accepted as is. |
| 2026-09-27 | camunda-docs-blog judgement share of 10.6% accepted as is. |
| 2026-09-27 | Firestart's 173 inline-SVG linear flow graphics become UNCERTAIN as one class, with a single class question. |

The orchestrator also applied these conventions under the existing rules, without asking the
operator:
- delegated binding (AI bound to an ordinary task) counts as INCLUDE;
- a lightning or zigzag circle on a task edge is an error boundary event, not an AI marker;
- CMMN or DMN without an AI element is E1, and CMMN with an AI element is UNCERTAIN;
- a UI screenshot is E1 with `judgment:false`, while a drawn non-BPMN diagram is E1 with
  `judgment:true`.

### 2.5 Defects caught by the orchestrator's audits and sent back

| Source | Defect | Fix |
|---|---|---|
| flows-for-apex (pilot) | 20 rows marked EXCLUDE together with `needs_visual_check` | Settled by viewing the figures; the audit now blocks this combination |
| bizagi, loyjoy, creatio | Keyword-narrowed or "JS-rendered" subsets left without rows | Full populations enumerated; loyjoy gained 8 INCLUDE |
| oracle-oic | 30 UNCERTAIN records whose figures were never examined | Visual pass: 29 changed to E1 |
| scheer-pas, bonitasoft | Delegated AI binding marked UNCERTAIN | Changed to INCLUDE |
| uipath-maestro-docs | 2 false INCLUDEs (error boundary events read as agent badges) | Changed to E2 |
| processmaker | Raw evidence not saved; judgement flags unverified | 2,458 files archived; 9 flags corrected |
| flowx-ai | 530 E1 rows claiming "UI screenshots" for figures nobody opened | 324 changed to mechanical E2; 206 pages (1,177 distinct figure URLs) viewed; 3 new UNCERTAIN |
| ibm-developer-watsonx | 190 drawn diagrams coded as mechanical E0 | Changed to E1 with `judgment:true`; self-audit flipped 14 to UNCERTAIN |
| frends-docs | Every "BPMN, no AI" row was set to `judgment:true` without a check | 131 changed to mechanical; share 15.7% → 1.8% |
| camunda-docs-blog | 110 `needs_visual_check` flags set only because a thumbnail was unreadable | All 110 read at native resolution: 56 → EXCLUDE, 11 → INCLUDE, 4 INCLUDE → UNCERTAIN; 3 false negatives restored in a post-pass check |
| firestart | 37.4% judgement share from 173 class-level E1 rows | Operator class ruling applied → UNCERTAIN; share 2.4% |

---

## 3. Outcomes per source

Legend:
- **JE** = judgement exclusions (EXCLUDE rows with `judgment: true`).
- **Rul.** = open `needs_human_ruling`.
- **Vis.** = open `needs_visual_check`.
- **Rec.** = records in `corpus/<slug>/`.

| Source | Population | INCLUDE | UNCERTAIN | EXCLUDE | BLOCKED | E0 | E1 | E2 | E3 | JE | JE % | Rul. | Vis. | Rec. |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| aletyx | 497 | 1 | 2 | 494 | 0 | 416 | 50 | 23 | 5 | 39 | 7.8 | 2 | 0 | 3 |
| atamya | 496 | 9 | 3 | 484 | 0 | 464 | 14 | 2 | 4 | 16 | 3.2 | 3 | 1 | 12 |
| bizagi | 2,225 | 2 | 7 | 2,212 | 4 | 1,868 | 66 | 273 | 5 | 55 | 2.5 | 7 | 2 | 9 |
| bonitasoft | 936 | 2 | 14 | 920 | 0 | 778 | 40 | 96 | 6 | 87 | 9.3 | 14 | 1 | 16 |
| camunda-docs-blog | 1,439 | 56 | 8 | 1,371 | 4 | 956 | 136 | 279 | 0 | 152 | 10.6* | 8 | 8 | 64 |
| camunda-marketplace | 255 | 52 | 23 | 180 | 0 | 9 | 10 | 159 | 2 | 17 | 6.7 | 24 | 12 | 75 |
| cib-seven | 591 | 6 | 3 | 582 | 0 | 383 | 104 | 83 | 12 | 22 | 3.7 | 3 | 0 | 9 |
| citeck-ecos | 994 | 1 | 6 | 987 | 0 | 914 | 7 | 64 | 2 | 14 | 1.4 | 3 | 5 | 7 |
| creatio | 2,194 | 2 | 4 | 2,188 | 0 | 1,272 | 593 | 323 | 0 | 153 | 7.0 | 4 | 0 | 6 |
| firestart | 494 | 13 | 179 | 302 | 0 | 249 | 6 | 6 | 41 | 12 | 2.4 | 179 | 6 | 192 |
| flowable | 1,361 | 3 | 11 | 1,347 | 0 | 1,116 | 175 | 54 | 2 | 92 | 6.8 | 11 | 1 | 14 |
| flows-for-apex | 362 | 4 | 8 | 350 | 0 | 91 | 3 | 246 | 10 | 13 | 3.6 | 8 | 1 | 12 |
| flowx-ai | 945 | 0 | 10 | 935 | 0 | 372 | 165 | 397 | 1 | 85 | 9.0 | 10 | 0 | 10 |
| frends-docs | 942 | 13 | 0 | 929 | 0 | 539 | 7 | 141 | 242 | 17 | 1.8 | 1 | 0 | 13 |
| ibm-bamoe | 137 | 7 | 2 | 128 | 0 | 104 | 15 | 9 | 0 | 9 | 6.6 | 3 | 1 | 9 |
| ibm-developer-watsonx | 1,983 | 1 | 46 | 1,936 | 0 | 1,668 | 254 | 0 | 14 | 256 | 12.9* | 47 | 0 | 47 |
| ifs-cloud-docs | 49 | 1 | 1 | 47 | 0 | 15 | 6 | 26 | 0 | 2 | 4.1 | 1 | 0 | 2 |
| loyjoy | 1,114 | 13 | 8 | 1,093 | 0 | 843 | 195 | 40 | 15 | 46 | 4.1 | 7 | 1 | 21 |
| newgen | 800 | 3 | 1 | 796 | 0 | 786 | 10 | 0 | 0 | 10 | 1.2 | 1 | 0 | 4 |
| oracle-oic | 823 | 1 | 1 | 821 | 0 | 670 | 107 | 44 | 0 | 17 | 2.1 | 1 | 0 | 2 |
| processmaker | 716 | 0 | 6 | 710 | 0 | 615 | 22 | 73 | 0 | 19 | 2.7 | 6 | 0 | 6 |
| quantumbpm | 100 | 2 | 0 | 98 | 0 | 79 | 6 | 13 | 0 | 7 | 7.0 | 0 | 0 | 2 |
| scheer-pas | 1,333 | 1 | 4 | 1,328 | 0 | 1,188 | 103 | 37 | 0 | 60 | 4.5 | 4 | 0 | 5 |
| trisotech | 1,622 | 8 | 28 | 1,586 | 0 | 937 | 38 | 610 | 1 | 53 | 3.3 | 5 | 25 | 36 |
| uipath-maestro-docs | 323 | 8 | 6 | 309 | 0 | 127 | 73 | 24 | 85 | 23 | 7.1 | 6 | 0 | 14 |
| **Total** | **22,731** | **209** | **381** | **22,133** | **8** | **16,459** | **2,205** | **3,022** | **447** | **1,276** | **5.6** | **358** | **64** | **590** |

\* Above 10%, accepted by the operator (`tools/accepted_shares.json`).

Notes on the table:
- In a few sources the Rul. count differs from the UNCERTAIN count. Some INCLUDE rows also carry a
  question (e.g. frends n=360), and some UNCERTAIN rows are pure visual checks.
- `uipath-marketplace` is not in the table: 0 rows judged, frontier of 2,326 listings.

### 3.1 Where the AI sits: headline findings per source

These are the workers' own characterisations, kept short.

- **camunda-marketplace (52 INCLUDE, the largest yield).** 12 records use an ad-hoc sub-process
  as the agent container. 11 are AI-agent service tasks or job-worker bindings. 26 are connector
  service tasks bound to an AI vendor's element template. The listings' own `.bpmn` files were
  downloaded and read.
- **camunda-docs-blog (56 INCLUDE).** Blog posts with Camunda Modeler diagrams, agentic ad-hoc
  sub-processes and AI connectors.
- **trisotech (8 INCLUDE).** AI appears inside the diagram in four ways:
  - AI as the performer of a user task (a drawn "AI Reviewer" badge);
  - LLM or prompt tasks;
  - a PMML task the vendor calls "an AI kind of task";
  - an NLP pipeline built from tasks.

  Counter-cases include the vendor claiming "AI agents act as performers" in a diagram that has
  no AI element.
- **ibm-bamoe (7 INCLUDE).** Dedicated AI node types in the palette ("Gen AI Task", "AI Agent
  Task"). Record 005 has two different AI task types in one process. There is also a before/after
  pair of the same hiring process, without and with AI.
- **flowable (3 INCLUDE).** Service tasks bound to Flowable's AI service ("Recognize intent",
  "Analyze sentiment"). The open-source BPMN manual contains no AI at all; AI exists only in the
  enterprise product. The rocket icon on a task is not an AI marker (Flowable's HTTP task uses it
  too).
- **frends-docs (13 INCLUDE).** bpmn-js task diagrams in the docs. Exactly one diagram carries an
  AI label (a ChatGPT task).
- **ibm-developer-watsonx (1 INCLUDE).** A tutorial that turns a `.bpmn` process into agents (the
  process-to-agent direction, admitted at Gate 1 B3). Everything else is ordered drawings of AI
  pipelines, which are UNCERTAIN.
- **flowx-ai, processmaker (0 INCLUDE).** AI lives in non-BPMN canvases, configuration panels and
  connectors. It is never drawn in a published BPMN diagram.
- **aletyx (1 INCLUDE).** The only AI element drawn in a process is in the GitHub `process.bpmn`
  (`drools:taskName="AletyxAI"` in the ad-hoc sub-process "Loan Investigation"). The website names
  "AI Agent nodes" only in prose.
- **firestart (13 INCLUDE, 179 UNCERTAIN).**
  - 13 exports carry an AI-bound task.
  - 173 inline-SVG linear flow graphics make up one class awaiting a single ruling:
    - 107 with an AI-labelled step;
    - 7 with AI only in the page text;
    - 59 with AI only in the site's navigation.

### 3.2 Recurring ruling classes (for the researcher's batch rulings)

1. AI named on the page but not drawn in the published diagram (prose, palette, legend, or
   configuration panel only).
2. Notation: CMMN versus BPMN (e.g. Flowable n=87). Mermaid or ASCII charts that use BPMN element
   names (FlowX 008–010, 468, 529). House-style or slide-style ordered drawings (IBM watsonx).
3. Is it AI? ABBYY Vantage IDP, a "digital assistant" bot, predictive or PMML models, OCR,
   voice-assistant or IVR tasks.
4. Process-to-agent versus AI inside the process (IBM watsonx n=765/1983, n=546).
5. Blank but bindable scaffolds, and element templates without a surrounding process.
6. The Firestart inline-flow class (one ruling covers 173 items).
7. Artefacts only inside a video: not opened, per the operator's 2026-09-26 instruction. That
   covers 22 Trisotech pages and 8 Camunda marketplace listings.
8. Unreadable conference or booth photographs (Flowable n=1098, 1135, 1136).

---

## 4. How each item was processed

### 4.1 Categories

Each of the 22,731 current ledger rows is assigned to exactly one category, using the row's own
provenance fields (`judged_from`, `figures_looked_at`, `seen`, `note`, `figure_note`,
`visual_evidence`, `figure_evidence`) and the visual-progress logs.

| Category | Definition |
|---|---|
| **A. Script only** | Decided by a scraping or screening script over saved pages, API payloads or file hashes, by a sanctioned mechanical rule: no artefact, no AI keyword in the page's own text, or a byte-identical duplicate. The item itself was **never loaded into an agent's context**; the agent saw only the script's aggregate output. These are EXCLUDE rows with `judgment:false` and no record of a look. |
| **B. Agent, text/DOM** | An agent read the page text, the live DOM, or model XML itself, but there is no record of it viewing an image. |
| **C. Agent, visual (contact sheet)** | The item's figures were viewed by an agent as tiles on contact sheets (4 tiles, each at least 900 px wide, or similar). |
| **D. Agent, visual (native)** | The decisive figure was read individually at full or native resolution, or the provenance names an eye ruling on that specific figure. |
| **E. Blocked** | Not reachable. |

### 4.2 Totals

| Category | Rows | Share |
|---|---:|---:|
| A. Script only (never in agent context) | **17,895** | 78.7% |
| B. Agent, text/DOM | **583** | 2.6% |
| C. Agent, visual (contact sheet) | **2,393** | 10.5% |
| D. Agent, visual (native resolution) | **1,852** | 8.1% |
| E. Blocked | **8** | 0.04% |
| **Total** | **22,731** | 100% |

Rows handled directly by an agent (B+C+D) total **4,828** (21.2%). Rows with a visual look (C+D)
total **4,245** (18.7%).

### 4.3 Per source

| Source | Rows | A. Script | B. Agent text | C. Visual (sheet) | D. Visual (native) | E. Blocked |
|---|---:|---:|---:|---:|---:|---:|
| aletyx | 497 | 455 | 42 | 0 | 0 | 0 |
| atamya | 496 | 468 | 28 | 0 | 0 | 0 |
| bizagi | 2,225 | 1,937 | 64 | 220 | 0 | 4 |
| bonitasoft | 936 | 701 | 2 | 11 | 222 | 0 |
| camunda-docs-blog | 1,439 | 344 | 0 | 981 | 110 | 4 |
| camunda-marketplace | 255 | 8 | 7 | 0 | 240 | 0 |
| cib-seven | 591 | 560 | 31 | 0 | 0 | 0 |
| citeck-ecos | 994 | 973 | 16 | 0 | 5 | 0 |
| creatio | 2,194 | 1,947 | 14 | 64 | 169 | 0 |
| firestart | 494 | 277 | 174 | 0 | 43 | 0 |
| flowable | 1,361 | 1,095 | 14 | 0 | 252 | 0 |
| flows-for-apex | 362 | 334 | 25 | 0 | 3 | 0 |
| flowx-ai | 945 | 720 | 21 | 177 | 27 | 0 |
| frends-docs | 942 | 903 | 9 | 11 | 19 | 0 |
| ibm-bamoe | 137 | 81 | 0 | 39 | 17 | 0 |
| ibm-developer-watsonx | 1,983 | 1,508 | 13 | 230 | 232 | 0 |
| ifs-cloud-docs | 49 | 42 | 3 | 0 | 4 | 0 |
| loyjoy | 1,114 | 263 | 25 | 651 | 175 | 0 |
| newgen | 800 | 781 | 12 | 0 | 7 | 0 |
| oracle-oic | 823 | 785 | 3 | 1 | 34 | 0 |
| processmaker | 716 | 580 | 0 | 0 | 136 | 0 |
| quantumbpm | 100 | 91 | 9 | 0 | 0 | 0 |
| scheer-pas | 1,333 | 1,268 | 32 | 8 | 25 | 0 |
| trisotech | 1,622 | 1,488 | 2 | 0 | 132 | 0 |
| uipath-maestro-docs | 323 | 286 | 37 | 0 | 0 | 0 |

### 4.4 Caveats on this classification

- **Visual counts are lower bounds.** Ten early ledgers carry no per-row provenance field
  (`judged_from` or similar), so their visual work is invisible to the classifier: aletyx,
  cib-seven, citeck-ecos, flowable's census rows, flows-for-apex, ifs-cloud-docs, newgen,
  oracle-oic, quantumbpm and uipath-maestro-docs. Their rows fall into A or B even where contact
  sheets exist on disk: aletyx 81 sheets over 464 figures, cib-seven 26, uipath-maestro-docs 30,
  and a 765-figure visual pass for citeck-ecos. The same applies to per-row notes whose wording
  the rules did not match.
- **Category A includes rows an agent opened but decided by a mechanical rule.** Example: a
  firestart route whose rendered text the agent read, excluded as E0 because it has no artefact.
  The defining property is that the verdict rests on a rule, not on the agent's interpretation.
- **Category B for firestart** (174) is mostly the 173 class rows. They were judged from the live
  DOM (inline `<svg>` labels) and rendered to PNG as captures afterwards.
- **Categories C and D count ledger rows, not images.** One row often covers several figures. The
  image-level counts are in section 5.
- The classification rules are in `ledgers/_report/pass2_stats.py` (`STRONG`, `SHEET`, `NATIVE`,
  `NEG`) and can be re-run.

---

## 5. What was scanned, scraped and classified

### 5.1 Files saved as evidence

These are all files under `ledgers/` and `corpus/`, as of 2026-09-28.

| Type | Files | Size |
|---|---:|---:|
| Images (figures, captures, renders, video frames) | 29,538 | 4,469 MB |
| Saved pages (HTML, markdown twins) | 13,427 | 1,117 MB |
| JSON (API payloads, indexes, decisions) | 1,697 | 401 MB |
| Contact sheets | 934 | 464 MB |
| Records (`corpus/*/NNN_*.md`) | 590 | 2 MB |
| Text, TSV, logs | 435 | 50 MB |
| Scripts (`.py`) | 268 | 3 MB |
| Process model files (`.bpmn`/`.dmn`/`.cmmn`) | 210 | 6 MB |
| Other XML | 50 | 4 MB |
| Ledgers (`.jsonl`) | 25 | 21 MB |
| PDF/PPTX | 2 | 3 MB |
| Other (extensionless assets, `.gif` frames, archives, etc.) | 3,491 | 861 MB |
| **Total** | **50,667** | **7.4 GB** |

In `corpus/` alone there are 590 records, 846 image captures and 39 `.bpmn` files, across 26
source folders.

Not every worker archived every fetched page. Early sources such as bizagi, creatio and scheer-pas
screened pages in memory or via cache files, so fewer pages were saved than were fetched. The file
counts are therefore a lower bound on what was fetched.

### 5.2 Visual work at image level (where logged)

- **Flowable visual pass.** 252 queue entries, all read at native resolution:
  - 20 by the first sighted session;
  - 222 by 8 shard agents;
  - 10 by `elicitation-aa` itself.

  Logs: `ledgers/flowable.raw/visual-progress.jsonl` (283 lines) plus 8 shard progress logs.
- **FlowX.ai re-check.** 1,177 distinct figure URLs retrieved, 538 tiles on 135 contact sheets.
  The 565 per-figure dispositions: UI 392, drawn non-BPMN 59, BPMN without AI 87, BPMN with AI 0,
  unclear 0.
- **Camunda blog.** 1,564 figures downloaded, 687 posts classified from contact sheets, then 110
  rows read at native resolution (122 progress lines across 8 logs).
- **Trisotech.** 106 slide decks (2,924 slides, 105 decks' per-slide text screened), 514 pages
  with figures, 7,268 image files on disk. 382 MB of video frames were captured before the
  no-video order; they are kept as evidence but are not the basis of any verdict.
- **IBM watsonx.** 2,424 images and 105 contact sheets.
- **ProcessMaker.** 1,701 images.
- **LoyJoy.** 2,127 images.

### 5.3 Judgement-exclusion shares

- Overall: 1,276 of 22,731 rows (5.6%).
- 23 sources are at or below 10%.
- Two are above 10% and were accepted by the operator after a documented step-3 self-audit:
  - ibm-developer-watsonx: 12.9% (256 of 1,983);
  - camunda-docs-blog: 10.6% (152 of 1,439).

  The excess in both comes from drawn architecture, component and UML diagrams on AI-saturated
  sites, each named as not BPMN.

---

## 6. Blockers and evidence gaps (`sources/OPERATOR-TODO.md`, Pass 2)

| # | Source | Status |
|---|---|---|
| P1 | bizagi | 3 sitemap URLs unfetchable; 4 BLOCKED rows |
| P2 | creatio | Incapsula / marketplace: resolved, no action |
| P3 | citeck-ecos | Read the Docs rate-limited figure fetches; evidence gap, census complete |
| P4 | bonitasoft | GitHub API rate limit; resolved |
| P5 | aletyx | Documented `.bpmn` sample returns 404 (dead link, E0) |
| P6 | aletyx | Placeholder image URL on one docs page |
| P7 | processmaker | German docs mirror does not exist; resolved |
| P8 | flowx-ai | 8 figure URLs are private on S3 (AccessDenied); no action possible |
| P9 | trisotech | One webinar gated; moot after the no-video ruling |
| **P10** | **camunda-docs-blog** | **`docs.camunda.io` refuses this machine's connections; docs half not enumerated; 4 BLOCKED rows. OPEN; the operator will cover it manually.** |
| P11 | ibm-developer-watsonx | 12.9% share: accepted |
| P12 | frends-docs | Share fixed (15.7% → 1.8%); one broken vendor figure |
| P13 | camunda-docs-blog | 10.6% share: accepted |
| P14 | firestart | Class ruling applied; one class ruling pending |

---

## 7. Open items

1. **uipath-marketplace:** not censused. The frontier (2,326 listings) and a partial crawl are in
   `ledgers/uipath-marketplace.frontier.txt` and `ledgers/uipath-marketplace.raw/`. The assignment
   still reads `IN-PROGRESS (elicitation-15)`. Judging it requires a logged-in session in UiPath
   Studio Web to read each task's Properties → Action.
2. **Camunda docs half:** blocked (P10). The operator will do it manually.
3. **Researcher review queue:** 590 records, 358 ruling questions and 64 visual checks.
   Batch-rule them by the classes in section 3.2.
4. **Corpus cap:** 590 collected items against the 60-example backstop. Selection is the
   researcher's step; no worker truncated.
5. **Reconciliation across sources** (cross-source deduplication) has not been done yet, by design.
6. **Sync to the thesis repository:** deferred by the operator until the elicitation is complete.

---

## 8. Usage statistics

Source: the Claude Code transcripts of this project in
`~/.claude/projects/C--Users-muffi-Desktop-Uni-Master-thesis-elicitation/`. There are 88 transcript
files, main sessions plus subagents, totalling 2.3 GB. The figures are summed from the `usage` block
of every assistant API response, deduplicated by message id. The script is
`ledgers/_report/usage_stats.py` and its per-file output is `ledgers/_report/usage_stats.json`. The
snapshot was taken 2026-09-28 at about 07:40 UTC; the UiPath session is still running.

Session files were mapped to worker names by the names each transcript uses for itself.
Restarts and `/clear` created new files, which are grouped under the worker.

### 8.1 Pass 2 workers (Claude Code on an Ollama backend, model `deepseek-v4.1-flash`)

| Worker | Transcript files | Active (UTC) | API calls | Uncached input tokens | Cache-read tokens | Output tokens | Tool calls | Subagents |
|---|---|---|---:|---:|---:|---:|---:|---:|
| elicitation-3a | fb90145d | 09-24 09:46 → 09-27 11:14 | 4,178 | 107,140,761 | 397,609,216 | 3,109,587 | 4,622 | 19 |
| elicitation-6f | eebb48e1, 6894d616 | 09-24 10:54 → 09-27 10:53 | 6,349 | 154,737,417 | 619,133,548 | 4,128,857 | 7,013 | 20 |
| elicitation-74 (before and after restart) | 53815744, f75b8500 | 09-24 10:54 → 09-25 12:49 | 1,843 | 65,195,913 | 142,810,772 | 1,409,131 | 2,316 | 29 |
| elicitation-aa | d10524fb | 09-25 12:49 → 09-27 09:21 | 2,993 | 196,927,134 | 241,161,344 | 1,419,869 | 3,134 | 8 |
| **Workers total** | 6 main + 76 subagent files | | **15,363** | **524,001,225** | **1,400,714,880** | **10,067,444** | **17,085** | **76** |

Tool mix:
- Bash about 8,100 and Read about 5,800 of the top-ranked calls.
- Shared-browser (`cdp1`) calls: `evaluate_script` 490, `navigate_page` 168, and screenshot, network
  and snapshot calls.

Three short set-up and test sessions on 2026-09-24 (browser access checks) add 26 API calls,
1,074,390 uncached input tokens and 1,460 output tokens: d69dcaaf on `deepseek-v4.1-flash`,
792c9091 on `glm-5.3-flash`, plus two empty files.

### 8.2 Anthropic API sessions (Claude Opus)

| Session | Scope | API calls | Uncached input | Cache-write | Cache-read | Output | Tool calls |
|---|---|---:|---:|---:|---:|---:|---:|
| elicitation-5a (orchestrator), **Pass 2 part** (from 2026-09-24 09:20 UTC, "do pass 2 now") | Briefing, auditing, rulings, this report | 294 | 718 | 1,880,204 | 49,165,790 | 187,660 | — |
| elicitation-5a, earlier part (Pass 1 and Gate 1, 2026-09-22 → 09-24) | For reference | 411 | 820 | 1,597,104 | 67,732,285 | 338,185 | — |
| elicitation-5a, whole session | | 704 | 1,536 | 3,473,181 | 116,659,637 | 524,835 | 699 |
| elicitation-15 / elicitation-7b (UiPath marketplace, Opus 5.5, running) | Frontier, crawl | 36 | 74 | 207,435 | 2,814,902 | 16,272 | 41 |

The orchestrator's tool calls over its whole life:
- Bash 205;
- Claude-in-Chrome 231 (Gate 1 website checks);
- Edit and Write 115;
- SendMessage 52 (the cross-session messages to the workers);
- AskUserQuestion 17.

### 8.3 Ratios

- **Orchestrator versus workers (Pass 2).** The orchestrator produced 187,660 output tokens; the
  workers produced 10,067,444. The orchestrator's share of all generated tokens is therefore
  **about 1.8%**. Its whole context re-read (cache-read) volume was 49.2 M tokens, against 1.92 G
  input (uncached plus cache-read) on the workers.
- **Per judged item.** Across the 22,731 ledger rows, the workers spent about 443 output tokens and
  about 84,700 input tokens (uncached plus cache-read) per row. The Opus orchestrator spent about
  8 output tokens per row.

### 8.4 Caveats

- **The Ollama figures are what the backend returned** in its Anthropic-compatible `usage` block.
  - Its split into "uncached input" and "cache-read" follows the backend's own accounting and may
    not match Anthropic's billing semantics.
  - It reported no cache-write tokens.
  - Treat these numbers as the backend's own accounting, not an Anthropic bill.
- **Subagent transcripts are counted under their parent worker.** For example, the 8 Flowable shard
  agents are under `elicitation-aa`, and the Camunda skim agents under `elicitation-6f`.
- **No monetary cost is computed here**, because the rate for the Ollama-hosted model is not known.
  To get a cost, apply your plan's rates to the token counts above.
- **The tool mix is taken from each file's top 12 tools**, so the small categories are undercounted.
  The tool-call totals themselves are exact.

---

## 9. Method lessons (for the write-up)

- **Mechanical versus judgement coding must be verified, not trusted.** Four sources
  under-reported judgement calls (FlowX, IBM watsonx, Frends, ProcessMaker) or over-reported them
  (Frends). The audit now catches E1 claims made on unviewed figures.
- **Site chrome contaminates keyword screens.** Mega-menus, navigation labels ("AI Workflows"),
  vendor names ("FlowX.AI") and HTTP headers ("User-Agent") produced false AI hits. Screens must
  read the page's own `<main>` region.
- **Contact-sheet thumbnails are too small to decide diagrams.** Of 110 Camunda rows flagged from
  thumbnails, 71 changed verdict at native resolution, and 3 real INCLUDEs were initially missed.
- **Icons are weak evidence.** The error boundary event (lightning) and Flowable's rocket (HTTP
  task) were both misread as AI markers. The robot face (Flowable) and the "AI Reviewer" badge
  (Trisotech) were the only reliable AI glyphs seen.
- **Version mirrors and translations multiply rows, not artefacts.** FlowX had 76 byte-identical
  page twins; Frends had 242 E3 rows. Hash-based deduplication made them cheap to settle.
- **Stopping for context was counter-productive.** Once auto-compaction was allowed, workers ran
  sources to completion without restarts.
