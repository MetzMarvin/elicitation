---
source: bizagi
source_name: Bizagi (help.bizagi.com — AI Hub / AI Agents documentation)
source_type: vendor documentation
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: YES
  C2_native_bpmn20: YES
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES
access: public
population_type: enumerable
population_estimate: 20
effort: small
needs_logged_in_browser: false
status: DONE (elicitation-3a)
---

## Criteria evidence

- **C1 YES** — https://help.bizagi.com/platform/en/index.html?ai_agents_form_actions_sentiment_analysis.htm
  (2026-09-22): "With the Execute AI Agents in Form Actions feature, you can make use of AI
  Agents in a Form in a running process. This feature integrates the use of Artificial
  Intelligence with the execution of Form Actions so that you can customize the actions
  needed in your business process." The documentation tree carries a named **"AI Hub"**
  branch with "AI Agents", "AI Agents configuration", "AI Agents execution", "AI Workers"
  and "Enterprise Knowledge".
- **C1 strengthened** — the same nav contains **"Execute AI Agents from Activity Actions"**,
  i.e. AI bound to a process *activity*, not only to a form. That is AI inside the process
  flow and it is the page Pass 2 should prioritise.
- **C2 YES** — Bizagi is a BPMN-notation vendor; `bizagi.com` publishes "BPMN 2.0 - A
  Standard for BPM platform development", "A Quick Guide to BPMN", "Process Modeling
  Software - Bizagi Modeler", and `help.bizagi.com` has "Standards support", "Exporting to
  BPMN" and "Modeling for execution". **Caveat for Pass 2:** these titles came from a
  `site:` result list, not from an opened page. Open one and quote it before recording the
  C2 evidence in the ledger header — the evidence rule forbids relying on a result snippet.
- **C3 YES** — `help.bizagi.com` served anonymously.
- **C4 YES** — Bizagi is a long-standing enterprise BPM vendor with a large free-modeller
  install base; it is routinely named in BPM tool comparisons (it publishes its own
  "5 Appian Competitors" page, and it appears in the UiPath Marketplace application
  directory).

## Entry points

- `https://help.bizagi.com/platform/en/index.html` — documentation shell. The AI Hub branch
  observed in the ToC on 2026-09-22:
  - AI Hub → AI Agents
    - AI Agents configuration
    - AI Agents execution
      - **Execute AI Agents from Activity Actions**  ← highest priority
      - Execute AI Agents from Form Actions
        - Compare two text files
        - Describe Image File
        - Translate Text from File
        - Analyze file sentiment
      - Execute AI Agents from Entity Forms
      - Execute AI Agents in Pipelines
    - AI Agents FAQs
  - AI Hub → AI Workers
  - AI Hub → Enterprise Knowledge
- Also confirmed to exist by `site:` sweep: "Configure an AI Agent" (`.../ai_agents`) and
  "Files as inputs use cases" (`.../ai_agents_files_use_cases`).
- `https://www.bizagi.com/home/sitemap` — marketing-site sitemap, for the blog half.

- **Template gallery (added at Gate 1, 2026-09-24):** Bizagi's process template gallery was never opened in Pass 1. Reach it by navigating from the vendor site (do not guess the URL) and enumerate it as a sub-population.

## Enumeration instructions

1. Frontier = the whole **AI Hub** branch of the ToC, plus any page the branch links into.
   Extract the ToC from the navigation iframe (see gotchas), do not hand-copy it.
2. Then check `bizagi.com` (the marketing site, separate from `help.bizagi.com`) for AI +
   BPMN blog posts and add them. Record the two enumeration methods separately.
3. Small source — expect it to complete in one session.

## Artefact mechanics

- Each worked example page has an explicit **"Process Model"** section. On the sentiment
  page it reads: "The following is the example process, which has only a Review Documents
  activity" — so the diagrams are small, deliberate, worked examples. Good.
- Diagrams are static `.png` assets with **numbered, non-descriptive filenames**
  (`ai_agents_from_forms09.png`, `ai_agents_from_forms39.png`) and `alt` text that merely
  repeats the filename. **`alt` is not an evidence route here.** Use the surrounding prose
  and the image itself.
- Capture the `.png` at its native URL.
- Note for the taxonomy: the sentiment example binds the agent to a **form button**
  ("buttons are implemented as the executors of AI Agent actions"), not to a BPMN task.
  That is a distinct placement — AI attached to the UI layer of a user task rather than to
  the process flow — and it is exactly the kind of boundary case that should be `UNCERTAIN`
  with the question attached, not an `E2`.

## Known gotchas

- **The documentation is frameset-based.** `index.html?<topic>.htm` loads two iframes:
  `hmcontent.htm` (the ToC) and the topic page. `document.body.innerText` on the outer page
  returns nothing. Read `iframe.contentDocument` (same-origin, so it works) or navigate to
  the inner `.htm` directly.
- The URL carries the topic as a **query string**, which the browser extension's privacy
  filter redacts. Capture topic ids from the ToC iframe DOM rather than from `location`.
- Deep links to a topic sometimes land on the shell with the default topic if the frameset
  has not initialised. Verify the rendered breadcrumb matches the topic you asked for
  before recording evidence.

## Spot checks performed by Pass 1

Spot checks only, not verdicts:

- `index.html?ai_agents_form_actions_sentiment_analysis.htm` — opened; C1 quote, the
  "Process Model" section and the AI Hub ToC all read out of the iframes.
- `site:help.bizagi.com "AI Agents from Activity Actions"` — 3 results, confirming the
  activity-bound page exists. **It was not opened.** Pass 2 must open it first.

## RESUME

(census complete 2026-09-24, ledger `ledgers/bizagi.jsonl`, audit clean.

Result after the orchestrator's recall review: population 2225 rows = **all 1644 help.bizagi.com ToC
topics** (1643 fetched and judged + 1 BLOCKED) + 577 www.bizagi.com sitemap URLs (574 read, 3
BLOCKED). 2 INCLUDE, 7 UNCERTAIN (each with a ruling request), 1868 E0, 66 E1, 273 E2, 5 E3, 4
BLOCKED; judgement-exclusion share 2.5%. 9 records in `corpus/bizagi/`.

Amendment (elicitation-5a review, 2026-09-24): the docs half was originally keyword-narrowed to the
221 topics carrying an AI token — a recall gap, because AI can sit in a diagram whose page text
carries no AI token. All 1644 ToC topics are now in the frontier and the ledger; the 1423 newly
fetched topics are judged from the fetched body **plus every image filename and alt text**, and each
carries `judged_from: http-fetch`. Separately, every www.bizagi.com page whose body mentions AI
(238 pages) had **all** its content images viewed (628 raster images in contact sheets, 252 SVGs
scanned for label text, the process-drawn figures then read at native resolution) and its row
re-issued with `supersedes_row: true`.

Finding of both re-looks: no marketing page carries a BPMN diagram with an AI element. The
AI-bearing marketing figures are product-UI mocks (the AI Agent editor, the template picker, AI
Workers) and step timelines (an "Obfuscation AI Agent" / "Create Email AI Agent" complaint timeline;
an RPA onboarding chevron strip whose architecture layer names "Machine Learning/RPA/AI") — none of
them BPMN 2.0 — and the two real BPMN models on the marketing site (invoice approval, employee
onboarding) contain no AI element. The AI-in-process artefacts of this vendor live in the product
docs, which is where records 001 and 002 come from.

Known gaps: 4 BLOCKED rows (3 marketing URLs, 1 docs topic) — OPERATOR-TODO **P1**; 6 image assets
that would not download are named in the row notes. Population note: the brief estimated ~20; the
shared-rule-6 unfiltered census is why it is 2225.)
