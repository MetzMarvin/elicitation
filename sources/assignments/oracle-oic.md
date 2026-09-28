---
source: oracle-oic
source_name: Oracle Integration (OIC) Process Automation (blogs.oracle.com/integration + docs)
source_type: vendor blog + documentation
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: YES (operator ruling B3 2026-09-24: substitution counts; agent-as-step also present)
  C2_native_bpmn20: YES
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES
access: public
population_type: enumerable
population_estimate: 30
effort: medium
needs_logged_in_browser: false
status: DONE (elicitation-6f; both surfaces complete, ledger audits clean - see DONE block)
---

## Criteria evidence

- **C1 UNCLEAR** (the B3 question, extended to Oracle):
  https://blogs.oracle.com/integration/the-future-of-oic-process-automation (10 September
  2026): "In customer estates today we see two patterns: deterministic flows, which
  increasingly invoke an agent as a step, and probabilistic flows, where the agent holds
  control. We expect both to converge on one architecture". It also says agents change
  "what a process model is: no longer a description of the path, but a description of the
  goal". That is partly AI-in-BPMN (agent as a step) and partly process-to-agent
  substitution.
- **C2 YES**: same post: "Most customers reading this have a body of structured (BPMN) and
  dynamic (case-style) processes in production".
- **C3 YES**, **C4 YES**.

## Why capture artefacts even before the ruling

The post contains a worked example ("A worked example: accounts payable invoice
processing. Take a typical BPMN model for supplier invoices.") that decomposes a BPMN model
into an agent architecture. Whatever B3 decides, that diagram is direct evidence for the
taxonomy's substitution mode.

## Entry points

- The anchor post
- `blogs.oracle.com/integration/`: enumerate the blog archive. The Channel 2 sweep
  (2026-09-22) also saw "AI Agent Loop" posts.
- OIC Process Automation docs on docs.oracle.com (not reached; a `site:docs.oracle.com`
  query with many OR terms returned 0 results, so use simpler queries or the docs nav)
- Third-party result, not opened: "OCI Process Automation and Oracle Artificial
  Intelligence in…" (redthunder.blog, Oct 2023). That is the practitioner layer: out of scope per Gate 1 ruling B4, do not enumerate.

## Enumeration instructions

1. Enumerate the OIC blog archive, not only AI posts.
2. Reach the OIC Process Automation docs via their nav and look for an agent/AI step type
   in the process modeller.
3. Capture the worked-example figure(s) from the anchor post.

## Known gotchas

- "Oracle Process Automation" and "OCI Process Automation" are the same product under two
  names.
- The anchor post is long and essay-like. Quote precisely which paragraph a figure
  illustrates.

## DONE (elicitation-6f, 2026-09-24)

**State: this source is a complete census of both its surfaces and audits clean -
`python tools/audit.py oracle-oic` -> `problems: none`.**

- **Population 823 = 229 blog URLs (n=1-229) + 594 docs URLs (n=230-823).** Ledger rows 823,
  `frontier.txt` 823 lines, `population_size` 823. Blog: archive at `blogs.oracle.com/integration`
  enumerated in the browser by activating "View more" until it hid itself. Docs: every book landing of
  the OCI Process Automation library enumerated from its own `toc.htm` with href anchors stripped
  (`user-process-automation`, `admin-process-automation`, `rest-api-proca`, `whats-new-process`,
  `process-licensing`), plus `books.html`, `recipes.html`, `training.html`, the six recipe books behind
  `recipes.html` (resolved through `oracle.com/pls/topic/lookup`) and the cross-library known-issues
  and accessibility pages; 594 distinct URLs after de-duplicating six recipe landing pages that are
  reachable both as a book landing and as their toc target.
- **Verdicts** (post visual pass): INCLUDE 1, UNCERTAIN 1, EXCLUDE 821 (E0-no-artefact 670,
  E1-not-bpmn 107, E2-no-ai-element 44), BLOCKED 0. Judgement exclusions 17 (2.1%).
  32 superseded rows in the ledger (corrections are appended, never edited).
- **Records**: `corpus/oracle-oic/` holds the anchor record (004, n=9, INCLUDE) and the docs record
  (032, n=769, UNCERTAIN + `needs_human_ruling`). Excluded items' evidence is preserved in
  `ledgers/oracle-oic.raw/` (60 files) with `README.md` explaining the move and the reversal recipe.
- **Raw evidence for the docs surface**: `ledgers/_6f_docs/` - `pages/` (all 594 fetched HTML
  pages), `survey.json` + `survey_recipes.json` (title, text, image inventory, keyword counts per
  page), `figs/` + `figs_index.json` + `sheet_1..5.png` (140 figures of the 88 figure-bearing pages,
  downloaded and looked at in contact sheets), `_6f_oic_docs_rulings.json` and
  `_6f_oic_docs_figs_rulings.json` (the per-page rulings behind the docs rows).

### What the visual pass found (blog, 31 records)

All 34 captures were opened at native resolution and each of the 30 `needs_visual_check` rows was
ruled on. Result: 29 flips to `EXCLUDE` (E1-not-bpmn, naming the notation actually used: OCI
Integration orchestration canvas / agent-builder node graph / console panel / architecture box
diagram / slide) and **1 flip to `INCLUDE`**: the anchor post's figure 3, whose "Before" panel is a
genuine BPMN 2.0 process model (start event, two lanes, nine tasks, two labelled gateways, thick end
event). Question Q2 (n=8, 17, 31, 49, 63, 72, 81, 93) is closed - those are release-notes panels of
the AI adapter configuration, not BPMN. Per-row detail: `ledgers/_6f_oic_visual_decisions.json`;
the applied rows carry `visual_evidence` and `artifact_named`.

Note for the abstraction step (stated as description, not as a verdict): in the anchor post's
figure 3 the BPMN 2.0 panel is the "Before" state and it contains **no** AI element - the AI (the AP
agent) sits in the "After" panel of the same figure and in the prose. The diagram carrying the AI is
the non-BPMN half of that figure.

### What the docs surface found

**Zero AI-bearing diagrams.** No page of the 594 carries both an AI/LLM keyword and a figure: the
full text of all 594 pages was keyword-scanned, the alt text of all 517 `<img>` tags was scanned, and
no image filename in the whole surface contains an AI-ish token. 88 pages publish figures; 140 of
those figures were downloaded and looked at in contact sheets - they are the product's own UI
screenshots, DMN boxed expressions/decision tables, BPMN notation illustrations and, on 13 pages, real
BPMN process fragments (event sub-processes, gateways, sequence flows) - none contains an AI element.

The docs surface's one AI-in-process evidence is prose, not a diagram:
`user-process-automation/implement-intelligent-document-processing-forms.html` documents the
**Document Understanding** form control, which "uses out of the box pretrained AI models from Oracle
Cloud Infrastructure (OCI) Document Understanding AI service" and whose "extracted text can be used
for process routing, approvals or can be sent to a downstream system". It publishes **no figure at
all** (the archived HTML has zero `img`/`figure`/`video` elements). Verdict `UNCERTAIN` with
`needs_human_ruling: true` and the exact question, record `032`, capture = full-page screenshot.
The other four keyword hits are false positives: "prompting you to confirm" (work-processes),
"prompts users to enter a zip code" (execute-rest-connector-calls-events), "user agent (browser)" /
"command prompt" (OAuth_useincalls), "travel agent name" (define-conditions-data-associations).

Blockers: none in this pass. Note for whoever continues: `curl` is refused with HTTP 403 by Akamai for
HTML on `blogs.oracle.com` (all blog fetching had to go through the browser session), while
`docs.oracle.com` serves fine to `curl`/`urllib` at ~1 request per second.
