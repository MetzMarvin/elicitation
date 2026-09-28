# Operator action list (Gate 1)

Written by Pass 1 (source selection), 2026-09-22/23, and continued 2026-09-24. Pass 2 census agents
append to this file as they hit blockers (shared rules section 9).

**New since 2026-09-23:** B0 ruled (yes). A4 (Celonis login) added. B3 extended to Oracle.
B5–B7 gained Scheer PAS, Aletyx and Imixs. B11 (Celonis), B12 (Pega C2), B13 (Berger BPM)
and B14 (batch C1 rule-out) added. Tooling gap C1 (Pega) partly resolved.

Each item states: the source, what is needed, the exact URL, why it blocks, and what
happens if it is skipped.

---

## Group A — Access actions

Accounts to create, logins to perform **inside the automation browser profile**, captchas
to solve by hand.

### A1. UiPath Automation Cloud account (free) — `uipath-marketplace`

- **What is needed:** a free UiPath Automation Cloud tenant, logged in inside the agent's
  Chrome profile, so that marketplace process templates can be opened in **Studio Web**.
- **Exact URL:** listing pages are public at `https://marketplace.uipath.com/listings/<slug>`;
  template inspection happens at
  `https://cloud.uipath.com/<tenant>/marketplace_/listings/<slug>`.
  The tenant used in the July 2026 round was `masterthesismetz`.
- **Why it blocks:** the BPMN diagram is **not** on the public listing page. Whether a task
  is AI-bound is visible only in the Studio Web properties panel
  (`Action: Start and wait for agent`). Without the login, every Maestro template in the
  census can only be judged `BLOCKED` or `UNCERTAIN`, never `INCLUDE`.
- **Items behind it:** up to 86 accelerators + 76 agent-catalogue listings; the wider
  frontier is 2326 listings.
- **If skipped:** UiPath contributes only listing-page metadata. The delegated-binding
  finding in `notes/uipath-promotion-pattern/analysis.md` — which is arguably the thesis's
  sharpest single observation — cannot be re-evidenced at the required capture resolution.
- **Note:** shared rules section 10 applies inside Studio Web. Read-only; if a property is
  changed to reveal a binding, revert it and record that.

### A2. IFS docs bot challenge — `ifs-cloud-docs`

- **What is needed:** nothing, probably. Recorded so Pass 2 does not misread it.
- **Exact URL:** any page under `https://docs.ifs.com/techdocs/26r1/...`
- **What happens:** the first load serves "Verifying your browser … Solving challenge...
  (80000 attempts)". It clears itself in roughly 8–12 seconds and the real page renders in
  the same tab.
- **Action:** none unless it stops clearing. Pass 2 must **wait**, not retry, and must not
  log a `BLOCKED` row for this.

### A2b. Search-engine CAPTCHA — affects discovery, not a single source

- **What happened:** Google served a CAPTCHA partway through the Pass 1 vendor sweeps. The
  operator solved it by hand in the browser and the sweeps resumed.
- **Why it matters far more than it sounds:** the agent was issuing queries with `fetch()`
  rather than tab navigation. A challenge page returns **HTTP 200 with no results container**,
  so the agent recorded *zero results* instead of a blocker. Three sources that are now in
  the sample (CIB seven, FlowX.AI, LoyJoy) had been recorded as zero-result vendors minutes
  earlier.
- **Standing instruction for Pass 2, agreed with the operator:** on a zero-result search,
  do **not** record a finding. Either switch search engine, or stop and wait for the
  operator to solve the captcha. A captcha is a `BLOCKED` row plus an entry in this file
  (shared rules section 9), never an exclusion and never a silent empty result.
- **Implementation note:** prefer real tab navigation for search, which renders the
  challenge visibly. If `fetch()` is used for speed, assert the results container exists and
  raise a blocker when it does not.

### A3. Browser tooling substitution — all sources

- **What happened:** `SETUP.md` specifies `chrome-devtools-mcp` over CDP. This session had
  only the **`claude-in-chrome` extension**. Everything in Pass 1 was done with the
  extension.
- **Consequences the operator should know about before Pass 2:**
  - The extension's privacy filter **redacts any `href` containing a query string**
    (returns `[BLOCKED: Cookie/query string data]`). Link extraction must go through
    `new URL(a.href).pathname`. This is noted as a gotcha in each affected assignment file.
  - The extension **disconnected twice mid-batch** during Pass 1 and returned with a new
    tab id. Recoverable, but a long census will hit it. The CDP server in `SETUP.md` is the
    better bet for Pass 2.
  - `take_screenshot` with `filePath` and `uid` (element-cropped capture), which the Step C
    capture rules depend on, is a **chrome-devtools-mcp** feature. The extension's
    `computer:screenshot` writes to a temp path instead. **If Pass 2 runs on the
    extension, the July 2026 pixelation failure can repeat.** Prefer CDP, or verify the
    pixel width on disk before writing each record, as `prompts/02_source-census.md`
    Step C already requires.

### A4. Celonis documentation login (`celonis.md`)

- **URL:** any `docs.celonis.com/...` page (e.g. "Adding Process Copilot to Process
  Orchestration steps", "Celonis Process Management BPMN reference"). All of them redirect to
  `celonis.my.site.com/docs/s/login/` ("Celonis ID Login / Celonaut Login").
- **What is required:** a Celonis ID. I did not check whether self-service free sign-up
  exists, and I did not attempt to sign up.
- **Items behind it:** unknown. The Process Management and Orchestration Engine doc
  sections were not enumerable from outside.
- **Operator action:** check whether a free Celonis ID (or an academic account) exists. If
  one does, create it and leave a logged-in session for Pass 2.

---

## Group B — Rulings needed

Every `UNCLEAR-NEEDS-RULING` source, with the precise question, my recommendation, and the
consequence either way. Answer by editing the `criteria:` block and `provisional:` flag in
the named assignment file.

### B0. Standing question: does a free account satisfy C3? — affects `uipath-marketplace`

> **RULED 2026-09-24 by operator: YES.** A self-service free account counts as publicly
> accessible. UiPath Marketplace stays `QUALIFIES`. Follow-up for the thesis text: tighten
> `sec:method:vendor_sampling` C3 wording to "no paid subscription and no sales gate".

- **Question:** C3 says "publicly accessible, reachable without an NDA, sales contact, or
  paid subscription". Does a **free account** (no payment, no sales contact, self-service
  signup) still count as publicly accessible?
- **Recommendation: yes.** The criterion's stated purpose is reproducibility by an
  independent researcher, and a self-service free signup preserves that. The July 2026
  round already used UiPath's catalogue this way, so ruling "no" now would retroactively
  invalidate a source already in the corpus. `README.md` records this as decision 1 of the
  two you still owe the workflow.
- **If yes:** UiPath stays `QUALIFIES`; the thesis wording in
  `sec:method:vendor_sampling` should be tightened to "no paid subscription and no sales
  gate" so the text matches what was done.
- **If no:** UiPath Marketplace drops out, and with it the delegated-binding pattern. The
  thesis would have to report that the single most distinctive promotion mode in the sample
  was excluded on an access technicality.

### B1. FireStart — C4 "dominant or actively discussed presence" — `firestart.md`

- **Question:** FireStart is an Austrian vendor explicitly positioned for the DACH
  mid-market ("made in Austria, hosted in the EU, built for DACH enterprises",
  `/en/platform-overview`). Named customers and a "1st Place – Toolmasters 2026 · Category:
  Process Automation" banner are public. Is regional mid-market presence enough for C4?
- **Recommendation: yes, include.** C1's own wording anticipates this case: "a smaller
  vendor with a concrete worked example is in scope". FireStart's C2 is unusually explicit
  ("built on BPMN 2.0 — … ISO 19510"), and it was already a known positive (#02).
- **If yes:** census 28 AI use cases + 85 blog posts.
- **If no:** the sample loses its only DACH mid-market vendor, and the corpus skews to
  large US/global vendors — worth a sentence in threats to validity either way.

### B2. Frends — C4 — `frends-docs.md`

- **Question:** Frends is a Finnish iPaaS vendor with Nordic enterprise customers. Same
  question as B1: does that clear "dominant or actively discussed presence in the
  enterprise market"?
- **Recommendation: yes, include.** Precedent: Frends is known positive #08. Its C1/C2
  evidence is explicit ("BPMN 2.0 with AI Connector enables AI Orchestrations").
- **If yes:** census the `llms.txt` docs index.
- **If no:** loses the "AI decision audit log" artefact recorded in the July round, which is
  the corpus's clearest governance-flavoured example.

### B3. IBM Developer / watsonx Orchestrate — C1 direction of travel — `ibm-developer-watsonx.md`

- **Question, and the most consequential one on this list:** the tutorial transforms **BPMN
  models into agents** ("using Bob skills to transform BPMN process models into SOP-driven
  … watsonx Orchestrate agents"). The BPMN diagram is the *input* that the agent replaces,
  rather than a process with AI placed *inside* it. Does "promotes an AI-in-BPMN integration
  capability" cover **BPMN-to-agent conversion**?
- **Recommendation: yes, include, and treat it as its own point on the exposure axis.**
  The July round recorded it as "whole BPMN order-processing flow converted into one
  autonomous agent owning all six steps as tools" — that is the maximum-authority end of the
  axis the thesis is mapping, and excluding it would silently truncate the range.
- **If yes:** it needs a named category in the taxonomy alongside "labelled AI task"
  (Camunda), "dedicated native node type" (BAMOE) and "delegated implementation binding"
  (UiPath). Suggested name: *wholesale process-to-agent substitution*.
- **If no:** known positive #03 leaves the corpus and Pass 3's seeded recall test must be
  re-scored against eight positives, not nine.
- **Downstream instruction already written into the assignment:** Pass 2 must **not**
  resolve this itself. A diagram whose AI relationship is "this becomes an agent" is
  `UNCERTAIN` + `needs_human_ruling`, never `E2-no-ai-element`.
- **Extended 2026-09-24 to Oracle OIC Process Automation (`oracle-oic.md`, row 39).** Oracle
  promotes *both* modes in one post: "deterministic flows, which increasingly invoke an
  agent as a step" (AI-in-BPMN, which qualifies on its own) *and* decomposition of existing
  BPMN models into an agent architecture (substitution). Recommendation: include Oracle
  regardless of the B3 answer, because the agent-as-step half satisfies C1 by itself.

### B5–B7. Three mid-size vendors, one identical C4 question

`cib-seven.md`, `flowx-ai.md`, `loyjoy.md`. All three have **explicit, strong C1 and C2
evidence** — stronger, in FlowX.AI's and CIB seven's case, than some of the seed sources —
and all three are held up only by C4.

- **B5. CIB seven** — the maintained continuation of Camunda 7, by CIB (DE), with an
  enterprise edition and public pricing. *Recommendation: include.* Camunda 7's installed
  base is very large, so its successor is by construction actively discussed. It is also the
  single best-documented example of the runtime-vs-design-time AI distinction in the sample.
- **B6. FlowX.AI** — banking-focused low-code vendor. *Recommendation: include.* "Trigger AI
  agents from BPMN workflow nodes" plus "Add a Service Task node to your process where you
  want to trigger the agent" is about as unambiguous as C1/C2 evidence gets.
- **B7. LoyJoy** — small German conversational-commerce vendor that models its AI Agent as a
  BPMN sub-process. *Recommendation: include.* C1's own wording admits "a smaller vendor
  with a concrete worked example".

**Consequence if all three are excluded:** the sample collapses towards large vendors, and
the taxonomy loses three independent instances of the *agent-with-tools sub-process* pattern
that would otherwise corroborate Camunda's. **Consequence if all three are included:** about
150 additional frontier items, all `public` and all cheap to census.

**Suggested general ruling rather than three separate ones:** treat C4 as satisfied by any
vendor that (a) sells a commercially supported BPMN engine or suite, and (b) is discoverable
through at least two independent channels of the search protocol. That rule admits B1, B2,
B5, B6 and B7 and is reportable in one sentence in the thesis.

**Added 2026-09-24. More sources held up only by C4 (strong C1+C2):** Scheer PAS
(`scheer-pas.md`, a second instance of the delegated-binding mode after UiPath), Aletyx
(`aletyx.md`, AI orchestrating an ad-hoc sub-process in Kogito), Imixs-Workflow
(`imixs.md`, LLM binding via BPMN annotations, possibly a new mode). **The general rule
above would admit all three**, provided each is found through two channels. Scheer PAS
and Aletyx were found through Channel 2 plus Channel 3. Imixs so far only through Channel 2,
so it needs a second-channel check before the rule applies.

### B8. BOC Group (ADONIS) — C1 failure, but C1 cannot exclude on its own

- **Question:** every named ADONIS AI capability is design-time — "AI-Assisted Process
  Modelling", "AI-Supported Process Analysis", "generating initial process drafts". That is
  the vendor-level version of `E2-no-ai-element`. The rules still forbid an `OUT` on C1
  alone, so it currently sits at `UNCLEAR-NEEDS-RULING` with a provisional assignment file.
- **Recommendation: rule it out — but open one page first.**
  `www.boc-group.com` publishes "Let Your BPM Speak AI with MCP and ADONIS", which was
  surfaced by the Channel 3 grid and **not opened**. An MCP server exposing the BPM
  repository to external agents is the inverse direction of AI-in-BPMN, and the equivalent
  BAMOE feature sits inside a source that qualifies. That page is the only thing standing
  between ADONIS and a clean rejection.
- **Page opened 2026-09-24 (q46):** https://www.boc-group.com/en/blog/bpm/ai-in-bpm-with-mcp/.
  The three "Key MCP Use Cases" are all *external* agents consuming the repository: "Smart
  navigator: fetches all relevant contextual data such as models…", "Process optimizer:
  retrieves information and invokes analysis tools", and "AI executor: retrieves, analyzes,
  and acts upon knowledge from the BPM suite. It can… trigger actions in business systems
  such as automated workflows." No AI element sits inside a modelled process. **C1 NO
  confirmed. The rejection is clean.** ADONIS is already in the B14 batch.
- **Worth noting either way:** ADONIS is the sample's cleanest **negative control**. If a
  census agent returns `INCLUDE` rows here, that is direct evidence the agent is not
  applying the runtime-vs-design-time distinction. Running it deliberately for that reason
  has methodological value even if the verdict is "out".

### B9. Nintex — two products, one missing bridge — `nintex.md`

- **Question:** Nintex has BPMN (in *Nintex Process Manager*, documentation-oriented) and
  AI agents (in *Nintex Automation*, a separate non-BPMN workflow engine). Does any single
  Nintex artefact put an AI element inside a BPMN diagram? If not, C1 fails.
- **Recommendation: let Pass 2 answer it empirically rather than ruling now.** The
  assignment file instructs the census agent to work the BPMN pages and the AI pages first
  and report the intersection explicitly. It is a cheap check on a small source.
- **Either way it is reportable:** a vendor that promotes BPMN *and* AI but never AI-in-BPMN
  is a genuine negative data point about the state of the market, and worth a sentence in
  the taxonomy chapter alongside the positive cases.

### B10. SAP Signavio — one sentence decides it — `sap-signavio.md`

- **Question:** Signavio's AI story is agent *governance*, not agent *hosting*: "Design and
  deploy AI agents **using the platform of your choice**". On that basis C1 is NO. But one
  capability line reads "Control your business process execution, carried out by your
  employees and AI agents" — a process model whose **performers** include AI agents, which
  is structurally the same claim Trisotech makes (and Trisotech qualifies).
- **The deciding check, which takes one page:** does SAP Signavio publish a concrete BPMN
  diagram in which an agent is a lane, a pool participant, or a task performer? Yes → C1
  flips and the source qualifies. No → C1 stays NO.
- **Recommendation: run that one check before ruling.** Do not reject SAP's BPMN vendor on
  a marketing-page reading when a single artefact settles it.
- **Check run 2026-09-24 (q45).** `site:signavio.com OR site:community.sap.com Signavio BPMN
  "AI agent" lane OR "service task" OR performer` returned 10 results. They were BPMN
  teaching posts (pools and lanes, multi-instance user tasks), release notes and a RACI
  post. None showed an AI agent as a lane or performer. The February 2026 release post
  (opened) names Signavio's own agents: "Dashboard Analyzer Agent… interprets your charts
  and metrics" and "Process Content Recommender Agent". Both are Joule assistants *about*
  the modelling work. **Updated recommendation: rule out (C1 NO). It can join the B14
  batch.** The "employees and AI agents" sentence stays unsupported by any artefact.
- **Consequence:** Signavio is the largest pure-play BPMN modelling vendor in the sample. If
  it is out, say so explicitly in `sec:pattern_taxonomy:sources` rather than omitting it —
  see the "emerging category" note in `candidate-vendors.md`, which pairs it with BOC Group
  as vendors promoting AI *about* processes rather than *in* them. That pairing is a finding
  about the market, not an absence of data.

### B11. Celonis: expected C2 rejection turned out to be BPMN, so C1 and C3 need rulings (`celonis.md`)

- **Question 1 (C1):** Celonis Process Management is native BPMN 2.0. Its product page says
  "define guardrails, outcomes, and AI-insertion points". Is that AI-in-BPMN, or AI about
  processes (the Signavio/ADONIS category)? This is the same kind of question as B10, and
  it has the same one-artefact test.
- **Question 2 (C3):** the full documentation (`docs.celonis.com`) is behind a Celonis ID
  login, while the developer portal is public. If a Celonis ID can be created self-service
  for free, B0 makes the docs public. If it cannot, only the developer portal and the
  marketing site count, and the docs are `BLOCKED`.
- **Recommendation:** treat it like Signavio. Run the one-artefact check first. If C1 fails,
  add Celonis to the "AI about processes" category note.

### B12. Pegasystems: is Pega's process notation "native BPMN 2.0"? (`pegasystems.md`)

- **Question:** Pega places AI directly in the process ("Agent Steps incorporate AI agents
  directly into your Case Type workflow"), so C1 is YES. But Pega models processes as a
  **Case Lifecycle** (stages and steps) and as **Process Modeler** flows made of
  Pega-named shapes ("Assignment shapes"). BPMN is only an **import** format ("uploading
  BPMN files… Save and Regenerate Case Lifecycle"). Does that satisfy C2?
- **Recommendation: OUT under C2**, with the notation named "Pega Case Lifecycle / Pega
  Process Modeler flow shapes". I did not record it as `OUT` myself, because the shape
  icon (a rounded rectangle) is too ambiguous for me to name a non-BPMN notation with
  confidence, and the rules resolve hesitation upward. One look at a full Process Modeler
  canvas by a human settles it.
- **Why it matters:** Pega would be the thesis's best example of the frame biting. It is a
  major vendor with genuine AI-in-process, excluded on notation alone.

### B13. "Berger BPM": which vendor did the method prompt mean?

- `"Berger" BPM BPMN AI OR KI OR agent OR LLM` (q44) returned only academic papers. No
  vendor surfaced, and I did not guess a domain. Please give the vendor's URL or delete
  the name from the list.

### B14. Batch ruling: eleven sources that fail C1 only (or C1 plus C4). Recommend rule out

The rules forbid `OUT` on C1 alone, so each of these has a provisional assignment file.
All were checked on at least one opened page on 2026-09-24. None shows AI *inside* a
BPMN process. The AI is design-time, mining or governance, or absent. **One tick can
dispose of all of them.** Evidence is in `candidate-vendors.md`, rows as listed:

| Row | Source | Why C1 fails | File |
|---|---|---|---|
| 20 | BOC ADONIS | design-time only (see B8, one page still to open) | `boc-group-adonis.md` |
| 31 | Apache KIE upstream | ML in DMN/Drools only | `apache-kie.md` |
| 32 | Operaton | "Manage Operaton engines via MCP" only | `operaton.md` |
| 33 | Activiti | no vendor AI material; community RAG post only | `activiti.md` |
| 36 | ARIS | AI Companion = text-to-model; BPM as AI governance | `aris.md` |
| 37 | iGrafx | Pia = text-to-BPMN | `igrafx.md` |
| 40 | OpenText | Developer Aviator = AI-assisted development | `opentext.md` |
| 41 | TIBCO | no AI material; "agents" = BusinessEvents | `tibco.md` |
| 45 | Visual Paradigm | AI BPMN generator | `visual-paradigm.md` |
| 46 | Cardanit | AI BPMN generator | `cardanit.md` |
| 47 | Modelio | no AI at all | `modelio.md` |

(SAP Signavio B10, Celonis B11 and GBTEC below are **not** in this batch. Each has a live
wrinkle that one page could flip.)

- **GBTEC (`gbtec.md`, row 35):** Arty is design-time, but "agentic automation" and the Work
  Orchestrator IDP product leave C1 open. One check: is there a Work Orchestrator BPMN
  workflow with an AI step?
- **Comidor (`comidor.md`, row 44):** only generic "AI/ML + BPM" claims, and C2 is not
  quoted. Low priority.
- **AgilePoint (`agilepoint.md`, row 43):** C1 YES, and C2 is the question. It is the same
  kind of question as B12 (Pega), and one canvas screenshot settles it.

**Suggested thesis sentence if B14 is ticked:** "Eleven vendors satisfied C2–C4 but promoted
AI only for modelling assistance, process mining or agent governance, not as an element of
the executed process. They were excluded under C1 at Gate 1."

### B4. Scope question the method does not yet answer — affects several sources

- **Question:** `README.md` decision 2. The vendor sampling frame has four criteria for
  *vendors*, but the grey-literature search surfaced a substantial **practitioner** layer
  (consultancies and independent BPM writers publishing worked AI-in-BPMN diagrams). Several
  have no archive index, so "exhaustive within the source" is undefined for them.
- **Recommendation:** admit them under an explicitly documented `census: false` search
  protocol, and add one paragraph to `sec:method:use_case_elicitation` describing that
  second stream. The alternative — restricting Step 1 to enumerable vendor sources — is
  defensible but must then be *stated*, because the title promises real-world use cases.
- **Status:** unresolved at the time of writing; the affected sources are still being
  worked in Channel 6 and are not yet in the decision table.

---

## Group C — Tooling gaps

Sources the browser tooling could not read at all, and that need the fallback browser.

### C1. Pegasystems — documentation site unreachable from search results

- **What is needed:** resolve Pega's C2 from Pega's **own on-site documentation search**,
  not from a search engine.
- **Exact URLs tried, all 404:**
  - `docs.pega.com/bundle/pega-cloud/page/platform/case-management/configuring-complex-processes.html`
  - `docs.pega.com/bundle/notes-blueprint/page/platform/case-management/getting-started-introduction-case-management.html`
  Each returned "ERROR CODE: 404 Page Not Found — We've been doing some housecleaning."
  Pega restructured its documentation and Google's index is stale; four separate indexed
  results for "Configuring complex Processes" all pointed at dead bundle paths.
- **Why it blocks:** Pega is a major enterprise BPM vendor and **the most plausible genuine
  `OUT` in the whole sample.** Its modelling surface is case-life-cycle and flow-shape
  based. If it is not BPMN 2.0, that is a C2 rejection with the notation named — the only
  kind of hard exclusion the sampling frame permits, and a valuable one for the thesis,
  because reporting a *reasoned* rejection of a major vendor is what demonstrates the frame
  actually bites.
- **If skipped:** Pega stays `PENDING-VERIFICATION` and the thesis cannot say whether the
  largest case-management vendor was in or out of scope — a conspicuous hole in a sampling
  frame that claims to be criterion-based.
- **Suggested route:** `docs.pega.com` → its own search box → "flow shapes" / "BPMN"; or the
  Pega Academy. Budget 15 minutes.
- **Update 2026-09-24, partly resolved.** The on-site search froze the renderer (CDP
  `Runtime.evaluate` timed out after 45 s, and the tab had to be discarded). A fresh
  `site:docs.pega.com` Google sweep did find live pages under `/bundle/platform/`,
  `/bundle/blueprint/` and `/bundle/ai-pega/…/gen-ai/`. C1 and most of C2 were read from
  those pages. The remaining question is now a ruling, not a blocker. See **B12**.

### C2. UiPath Studio Web — canvas app

`marketplace.uipath.com` template inspection runs inside Studio Web: a canvas app with a
thin accessibility tree, requiring coordinate clicking **and** a logged-in session. See A1
and A3. Not yet confirmed as a tooling failure, but it is the most likely one.

---

## Appendix — guessed-URL failures recorded for the audit trail

The evidence rule forbids guessing URLs. Two guesses were made in Pass 1 and both are
recorded here so the reflex is visible to the reviewer:

- `https://marketplace.camunda.com/en-US/search` → served `/status/404`. The real catalogue
  path, `/listing`, was then extracted from the home page DOM.
- `https://marketplace.uipath.com/listings` → 404 ("Entschuldigung! Anscheinend fehlt die
  Seite."). The real enumeration entry point, `/sitemap`, was extracted from the footer.

Both are now written into the relevant assignment files as gotchas so Pass 2 does not
repeat them.

---

## Pass 2 blockers

Pass 2 blockers are numbered P1, P2, ... (the B-series is taken by the Gate 1 rulings). Workers: take the next free P number.

### P1. www.bizagi.com — 3 sitemap URLs unfetchable (elicitation-3a, 2026-09-24)

The marketing half of the `bizagi` source was enumerated from `https://www.bizagi.com/home/sitemap`
(645 en URLs, 577 content URLs). Three of them could not be read by plain HTTPS fetch and are
`BLOCKED` rows (n=222, n=223 region) in `ledgers/bizagi.jsonl`:

- `https://www.bizagi.com/blogs/manufacturing/infographic-automate-to-innovate` — connection reset (curl 35/56)
- `https://www.bizagi.com/contents/News/bizagi&apos;s-ceo-gustavo-gomez-named.html` — HTTP 403 (URL is stored HTML-escaped in the sitemap; the escaped form is what was requested)
- `https://www.bizagi.com/en/blog/business-process-automation` — connection reset (curl 000, twice)

What was required: nothing but a fetch — no account, no captcha, no login. Two of the three
failed intermittently, so a browser fetch from the shared Chrome tab will very likely succeed.
What was tried: `curl -sSL` with a desktop User-Agent, twice for the reset ones; all other 574
sitemap URLs fetched fine on the same run, so this is per-URL flakiness, not a bot challenge.

Items behind the blocker: **3**. Everything else in the source is judged; these three pages are
an "infographic-automate-to-innovate" post, a corporate news page and a blog index page, so the
expected artefact yield is low — but the census is incomplete until they are read.

**Added 2026-09-24 (same session, docs half).** The `help.bizagi.com` half is now a full census of
all 1644 ToC topics, each fetched by direct HTTP. One topic could not be read and is a `BLOCKED`
row (`n=2225`) in the same ledger:

- `https://help.bizagi.com/platform/en/your_opinion_matters.htm` — returns the frameset shell with
  no topic body (`hmcontent.htm` loads, the topic iframe does not); the URL is a real ToC entry, not
  a guess. It is a feedback/"your opinion matters" topic, so no artefact is expected, but it needs a
  browser fetch (or the topic id confirmed against the live ToC) to be judged.

Items behind this blocker: **1**. A browser fetch of the topic iframe from the shared Chrome tab
will settle it; there is no account, captcha or login involved.

### P2. Creatio: Incapsula / marketplace, RESOLVED, no operator action (elicitation-6f, 2026-09-24)

**Added 2026-09-24 (creatio, elicitation-6f); revised same day — no blocker remains.** The Academy
census is closed at **1657 rows** (`python tools/audit.py creatio` → `problems: none`): the whole
enumerated v10 guide tree (1656 items: 1653 fetched pages + the 3 in-scope links that 404) plus one
item of the second surface below. Status of the two entry points that were listed here as blocked:

- `https://www.creatio.com/page/bpmn` ("Business Process Modeling in BPMN Notation") — **NOT
  blocked.** The Incapsula interstitial answers a plain GET only; the page loads in the shared Chrome
  tab (a real browser). It has been enumerated and judged: ledger row `n=1657`, `surface:
  creatio.com-landing`, corpus record `005_business-process-modeling-in-bpmn-notation.md` (UNCERTAIN
  + `needs_human_ruling`, three captures). Nothing further is needed from an operator.
- `https://marketplace.creatio.com/` — **enumerable, and being enumerated.** The catalogue is
  server-rendered *and* exposes its own JSON endpoint, found in the browser's network panel:

      POST https://marketplace.creatio.com/search/ai
      {"sort":"popularity","ai_filter":null,"search":null,"facets":{},"offset":0,"count":20}
      -> {"numFound": 524, "results": [...]}

  `numFound: 524` is the catalogue's own exact total, enumerated unfiltered (the platform's own
  `is_ai` flag marks 26 items and is used only as a screen, never to narrow the population). Every
  listing page is also server-rendered HTML to a plain GET (no Incapsula challenge on this host), so
  the 524 listing pages are cached by `ledgers/_creatio_mp_crawl.py` and judged from the cache. The
  blog index (`/blog?page=N`) walks to exhaustion at **13 articles**. This is a separate surface from
  the Academy and is ledgered as such (`surface: marketplace` / `marketplace-blog`).

Nothing in this block now needs an operator action. It is kept for the record of what was tried and
of the corrected facts: the earlier claim that `/catalog` "returns an empty shell to a plain GET" was
wrong (it returns the shell *with* its facets and the "Over 524 results" counter; only the cards come
from the XHR endpoint), and Incapsula answers the plain GET on `www.creatio.com`, not the browser.

**Closed 2026-09-24 (creatio, elicitation-6f).** The marketplace surface is enumerated **and judged**;
no blocker and no operator action remain. 524 listings + 13 blog articles = 537 rows appended
(`population 2194 == rows 2194`, `python tools/audit.py creatio` → `problems: none`). Judgement split:
394 listings carry no process-model language anywhere in body text, image alt text, image file names or
the 'Business Process Element' / 'AI Workflow' tags, and are `E0-no-artefact` (mechanical, from the
cache); the 143 that do carry such language had **every figure looked at by eye** - 883 non-chrome
figures tiled into contact sheets (`ledgers/_creatio_mp_sheets.py`) and read, plus the 46 figures that
sheet's noise filter had dropped, tiled and read separately (`ledgers/_creatio_mp_noise_sheet.py`; no
diagram among them). Result: 22 listings publish a genuine Creatio process-designer BPMN 2.0 model
(`E2-no-ai-element`) and none of them has an AI element inside it; the other 121 publish no process
model at all, with named non-BPMN artefacts among them (Zapier's and Make.com's proprietary iPaaS
editors, Creatio's campaign designer - square step tiles, dotted connectors, SAVE/CANCEL toolbar - which
is distinguishable from the process designer's event circles, gateway diamonds and SAVE/RUN/CANCEL/ACTIONS
toolbar, InterWeave's architecture box diagrams, Kanban boards, a whiteboard, a relationship map, a Power
BI report, a call-script decision tree). One UNCERTAIN: `corpus/creatio/006_banza-bot-constructor-creatio.md`
(its BPMN model is a chatbot's dialogue logic and the listing advertises free-text input, so an AI-bound
implementation could hide behind a task the diagram does not show - rule 3's UNCERTAIN case). The
marketplace therefore yields **no AI-in-process example**, which is a result: its AI apps ('AI Skill',
'AI Agent', 'AI Workflow' tags) expose their AI as a chat panel or a marketing card, never as an element
inside a published process model.

### P3. citeck-ecos — Read the Docs rate-limited the figure fetches; evidence gap, census is complete (elicitation-3a, 2026-09-24)

**Not a blocker for judgement: no item is unreadable and there is no `BLOCKED` row.** Recorded because an
evidence channel is incomplete and the reviewer should know which rows rest on what.

- **What happened:** the `citeck-ecos` census is complete (993/993 documentation URLs fetched, 994 rows,
  population 994, `python tools/audit.py citeck-ecos` → `problems: none`). The decisive channel — the whole
  population carries exactly four `.bpmn` files on six pages, all four downloaded and parsed — and the
  complete page-text/DOM channel for all 993 URLs are unaffected. But the *visual* pass over the remaining
  diagram figures could not be finished: Read the Docs started answering **HTTP 429** to the figure bursts
  from `https://citeck-ecos.readthedocs.io/_images/...` after roughly 780 successful downloads, and kept
  answering 429 to a slowed retry (3 s spacing, backoff to 60 s, run for ~10 min, zero progress).
- **What was tried:** the plain burst (`cdl.py fetch`, 0.4 s spacing) — 781 figures downloaded, then mass
  HTTPError; a slow retry (`retry.py`, 3 s spacing, 429 backoff 5/15/40/60 s) — no progress, stopped.
  Plain `curl` probes to single image URLs also returned 429, so it is host-wide throttling of this client,
  not a per-URL problem.
- **Items affected:** **~535 figures** on pages that publish no AI artefact. The E2/E1 rows there rest on
  the page's own heading and text plus the verified sample of figures that *were* fetched (contact-sheet
  inspection confirmed the drawn processes are bpmn-js/BPMN 2.0 diagrams and the rest are UI screenshots).
  Recorded as a limitation in the ledger header `note`; the residual risk is an AI element drawn inside a
  figure whose page never mentions AI in its text (no such page exists — the AI keyword population of 40
  pages was read in full).
- **Operator action, optional and only if you want the visual pass airtight:** after the throttle cools
  (an hour or a different network), run the retry again —
  `python C:\Users\muffi\AppData\Local\Temp\citeck\retry.py` — which fetches only the missing targets and
  leaves `canon.json` untouched. **Expectation: it will confirm the existing verdicts and change nothing**;
  the rows are not waiting on it.
- **Also noted:** three image references in the Russian `develop` build
  (`ru/develop/_images/*.png`) 404 — a broken reference in that build, not a blocked item.
- **UPDATE 2026-09-25 (elicitation-3a, orchestrator request): figures downloaded; visual pass
  pending.** All **765/765** target figures are now on disk in `ledgers/citeck-ecos.raw/figs/`
  (24.4 MB), with `figs/manifest.json` mapping every file to its ledger row `n`, its page URL,
  its asset URL, the section heading it sat under and the rule that made it a candidate
  (`why`). 254 came from the earlier scratch downloads, 510 were fetched fresh at one request
  every two seconds with 429/503 backoff — the throttle had cooled, so there were no 429s this
  time. Four files are genuinely tiny (167–262 bytes: the multi-instance marker and the
  pool/participant glyphs) and are valid PNGs, not error pages. The old `P3` blocker is
  closed on the collection side; what remains is the researcher's visual pass over those 765
  figures, which is not something a worker can do for them.

### P4. bonitasoft — no outstanding blocker; the GitHub API's rate limit and three evidence limitations, all resolved and recorded (elicitation-6f, 2026-09-25)

**Added 2026-09-25 (bonitasoft, elicitation-6f); nothing here needs an operator action.** The census
is closed at **936 rows** (`python tools/audit.py bonitasoft` → `problems: none`): the portal's 807
pages (documentation.ofelia.com `latest` per component, the paths published only under an older
version, and the 254 English www.ofelia.com pages) **plus** the second population group — the 53
GitHub repositories the portal links to, enumerated as one row per repository *plus* one row per
`.bpmn`/`.proc` process file found in their trees (76 files). **0 BLOCKED rows.** Kept here because
the two channels that nearly produced a blocker, and three evidence limitations, should be on the
record.

- **The GitHub API's rate limit, not access, was the whole problem.** The API is unauthenticated
  here, so it allows 60 requests/hour; repository-tree fetches came back **HTTP 403** and would have
  made reachable repositories look `BLOCKED`. Two things were wrong on my side, both fixed rather
  than worked around: (1) the first enumeration tried only branches `main`/`master`, but 11 of the 53
  repositories keep their default branch at `dev`/`1.0`/`1.3`/`4.0` — reading each repository's own
  `default_branch` took the process-file population from 2 to **76** and the repository rows from 55
  to 53 canonical (the extra two were `.git` duplicates); (2) `ledgers/_bonita_repos_trees.py` seeded
  its cache with `setdefault`, so a remembered 403 outlived a good reading and the next run refetched
  — and re-lost — five repository trees. It now lets any reading overwrite a remembered failure and
  keeps the last successful reading when a later retry is refused. After the rate limit reset,
  `python ledgers/_bonita_repos_trees.py` reported **53 repos known, unreachable 0, process files
  76**. No operator action is needed; a re-run needs no network at all (trees, file bodies and
  READMEs are cached under `ledgers/_bonita/`).
- **`placeholder.60f9b1840c.svg` (403) — inspected, explained, not a blocker.** 22 www.ofelia.com
  pages reference Webflow's lazy-load asset
  `https://cdn.prod.website-files.com/plugins/Basic/assets/placeholder.60f9b1840c.svg`, which answers
  **403** to any non-browser client. It is one asset of the site's own chrome — the `src` of
  not-yet-loaded images, with an **empty `alt`**, the identical URL on all 22 pages — and the *real*
  figures of those same pages were fetched (e.g. `/blog` yielded its nine article images as `.webp`
  beside it). Nothing is hidden behind it, so no row rests on it; it is recorded in the ledger
  footer (`figures_looked.raw_assets_not_fetched`) and needed no browser fetch.
- **15 sampled figures have no decoder in this environment.** They are SVG files — `edit.svg`,
  `history.svg`, `info.svg` (UI icons), a `*_grad-lat-*.svg` gradient and 11 `*_black.svg` customer
  logos on the use-case pages. Each was judged by its name and by the role it plays in the page; none
  is a diagram. They are named in the ledger footer (`figures_looked.undecodable`), so the reviewer can
  see exactly which tiles of the calibration contact sheet were read by name rather than by pixels.
- **One capture is `marginal`, and its row is flagged for the eye.** Corpus record
  `012_kyc-bpmn-diagram.md` (the ofelia KYC article) publishes a 2492x270 bpmn-js diagram whose export
  draws its text as paths; the capture is 1400x152. Its ledger row is `UNCERTAIN` with
  `needs_human_ruling` **and** `needs_visual_check: true` (`ledgers/_bonita_write.py`, `VISUAL_CHECK`),
  naming the one thing to verify: the task labels around the "Verify identity" / "Check background"
  tasks, and whether any of them names an AI/ML step. All other 15 records are `capture_quality:
  legible`.
- **No login, captcha, paywall or walled page was hit in this source.** The portal, the marketing
  site and the GitHub repositories are all public; the shared browser tab was used read-only, as
  §10 requires, and this source's own `sources/assignments/bonitasoft.md` records the STOP/`RESUME`
  state.

### P5. aletyx — one documented `.bpmn` sample file returns 404 (elicitation-3a, 2026-09-25)

- **URL, exactly as the docs page links it:**
  `https://github.com/aletyx-labs/examples/raw/main/employee-onboarding/src/main/resources/employee-onboarding.bpmn`
  (the link text on `https://aletyx.ai/docs/guides/tutorials/bpmn-example` is "sample onboarding
  process file"; the same page names the path `src/main/resources/employee-onboarding.bpmn` and the
  file name `employee-onboarding.bpmn`).
- **What happens:** the URL returns **HTTP 404** to an anonymous fetch. The org it points at,
  `https://github.com/aletyx-labs` (note: **`aletyx-labs`**, a different org from the one this
  source enumerates, `github.com/aletyx`), answers **302** — i.e. the `examples` repository is
  private, renamed or organisation-gated. Not a captcha or a rate limit: one request, 404.
- **What was tried:** direct `curl -sSL` of the raw URL (404); the org page
  `github.com/aletyx-labs?tab=repositories` (302, no listing). No login was attempted, and none
  should be: §10 forbids credential entry unless the operator stages a session.
- **How many items sit behind it:** one file, and it is **not** the source's decisive artefact —
  the same process model is available in full inside `github.com/aletyx/aletyx-kogito-ai-addons`
  (`examples/quarkus/src/main/resources/process.bpmn`, byte-identical to the springboot copy,
  sha256 prefix `154f36c847982f6c`; ad-hoc sub-process "Loan Investigation" holding the custom task
  `drople:taskName="AletyxAI"` / name "Aletyx Intelligence" beside the user tasks RiskAssessment,
  PropertyAssessment and ApplicantVerification). The 404 costs the census a *tutorial* copy of a
  diagram it already holds, not an unseen artefact.
- **Operator action needed:** none, unless the operator wants the tutorial file itself; if so, a
  GitHub session with access to `aletyx-labs/examples` would be required. Until then the ledger
  records the item as `BLOCKED` with this URL.

### P6. aletyx — a docs page references a literal placeholder image URL (elicitation-3a, 2026-09-25)

- **URL:** `https://placeholder-image-url.com/drools-components.png`, referenced as a figure by a
  page of `https://aletyx.ai/docs` (the reference is in the page's own HTML, alongside real
  `mintcdn.com` figures). The host does not resolve (curl error 6).
- **What happens:** not a blocker of the vendor's — the docs simply ship a placeholder that was
  never replaced. It is recorded so the census's figure count reconciles: **464 of the 465 figure
  references were fetched**, and this is the one that could not be, because there is nothing there.
- **Operator action:** none.


### P7. processmaker — the German mirror `docs.processmaker.com/de/` does not exist; checked and resolved, no operator action (elicitation-6f, 2026-09-25)

- **What was asked:** the orchestrator asked the census to enumerate a German mirror of the
  ProcessMaker docs at `docs.processmaker.com/de/` and to give every German URL a frontier line and a
  row, using figure-hash identity against the English counterpart for `E3-duplicate`.
- **What happens:** there is no such tree. The probes, all anonymous `curl -sSL`, on 2026-09-25:
  - `https://docs.processmaker.com/de/sitemap.xml` → **404** (281,461 bytes: the platform's own 404
    shell, HTML).
  - `https://docs.processmaker.com/de/llms.txt` → **404**, 9 bytes of `text/plain` (`Not Found`).
  - `https://docs.processmaker.com/de/docs/add-a-genie-in-a-process` → **404** (271,667 bytes, the
    same 404 shell as `/de/docs/designer`, `/de-de/...`, `/de-DE/...`, `/es/...`, `/german/...`,
    `/docs/de`, `/de`: every one of these returns that identical shell, i.e. the platform answers
    unknown routes with the SPA shell and status 404).
  - The site's **own two indexes contain no locale tree at all**: `sitemap-en.xml` (707 `<loc>`) has
    no `hreflang` alternates and no `/de/` path; `llms.txt` (715 entries) has zero `/de/` entries.
  - The served page declares `<html lang="en">`, carries **no `hreflang` `<link>` elements** and
    contains the string "Deutsch" **nowhere** in its shell (the Document360 header does carry a
    language *button*, but with an empty `language-code` and no second locale configured).
  - The alternate origin `https://processmaker.document360.io/llms.txt` is **byte-identical**
    (70,918 bytes) to the custom-domain copy, and `/de/llms.txt` on that origin is 404 too.
  - The only German-language ProcessMaker pages that ever existed are on the **marketing** host, not
    the docs host: `www.processmaker.com/de/...` (e.g. `/de/customers/support/`, "Unterstützung |
    ProcessMaker"), and those now **301-redirect to `decisions.com`** (the vendor rebrand the
    assignment already records). All four marketing `/de/` paths probed redirect to the same
    `decisions.com` page.
- **How many items sit behind it:** zero. The census population for this source is `docs.processmaker.com`,
  and that host publishes exactly one language.
- **Operator action:** none. If the orchestrator has a concrete URL that returns 200 on a German
  page of the docs host, this note is the place to put it and the census will enumerate it; the
  716-row census stands as the complete population of the source as published.

### P8. flowx-ai — 8 figure URLs are S3 `AccessDenied` (object no longer public); no operator action available (elicitation-6f, 2026-09-25)

**Recorded because the census's visual pass cannot reach them, not because a page is unreadable.**
All 945 **pages** were read. The figures below are the residue: 8 of the 1312 distinct figure URLs
referenced by this source's pages answer **HTTP 403 `AccessDenied`** from the vendor's own bucket, so
the vendor's own rendered pages show a broken image for each of them.

- **The URLs** (all on `s3.eu-west-1.amazonaws.com/docx.flowx.ai`, all the vendor's own links, none
  guessed — each was extracted from the page's published markdown):
  - `/5.x/ml1.gif`, `/5.x/ml10.png` — on `/4.7.x/docs/platform-deep-dive/core-extensions/content-management/media-library` (row `n=103`)
  - `/release34/start_subprocess_action_config.png` — on `/5.1/…/actions/start-subprocess-action` (`n=221`) and `/5.9/…/actions/start-subprocess-action` (`n=500`)
  - `/5.5/multiple-file-upload-overview.png` — on `/5.1/…/ui-component-types/multiple-file-upload` (`n=285`) and `/5.9/…/ui-component-types/multiple-file-upload` (`n=567`) — **the page's only figure**
  - `/5.x/input_parameters.png` and `/5.x/wf_ex2.png` — on `/5.9/docs/platform-deep-dive/integrations/workflow-data-models` (`n=667`)
  - `/5.9/anonymous-share-modal.png` — on `/5.9/docs/platform-deep-dive/user-roles-management/anonymous-runtime-access` (`n=674`) — **the page's only figure**
  - `/5.x/intent_classification_node.png` — on `/release-notes/v5.x/v5.6.0-march-2026/v5.6.0-march-2026` (`n=929`)
- **What was tried:** `urllib` with a desktop User-Agent and `Referer: https://docs.flowx.ai/`;
  `curl -sSL` with no headers, with the Referer, and with a browser User-Agent + `Accept:
  image/avif,image/webp,*/*`. All four returned **403** with the bucket's own body:
  `<Error><Code>AccessDenied</Code><Message>Access Denied</Message>` (RequestIds `N1RV60T6K43EBGYR`,
  `QE19919ES404AFYQ`). **Confirmed in the browser too:** on the rendered
  `/5.9/…/multiple-file-upload` page the figure's `naturalWidth` is `0` and its `alt` is
  `"Multiple file upload component"` — the vendor's own site renders the gap.
- **Items behind it:** **8 figures across 8 pages.** Three are the *only* figure on their page
  (`n=285`, `n=567`, `n=674`); two sit on pages that do discuss AI (`n=667`, `n=929`), where an
  unscreenable figure is the one place an AI element could hide. The other 1304 distinct figures
  were fetched (1292 ok, 8 = these).
- **Operator action: none available.** This is not a login, captcha or paywall — the S3 objects are
  simply no longer world-readable, so no session the operator could stage would reach them. Recorded
  so the reviewer knows which rows rest on a figure that cannot be re-verified: on the two
  AI-discussing pages the verdict rests on the figures that *were* retrieved, and the unscreenable
  two are named in those rows' notes.
- **Separately noted for the method chapter (not a blocker):** every page of `docs.flowx.ai` carries
  AI words in its *site chrome* — the header nav tab `AI Platform`, a nav item `Using FlowX docs with
  AI assistants`, and the assistant disclaimer `Responses are generated using AI and may contain
  mistakes.` These are outside `<main>` on every page and are why the census screened the author's own
  markdown twin rather than the rendered DOM.


### P9. trisotech — one webinar recording is gated by "Viewer discretion is advised"; frames unreachable without a signed-in session (elicitation-6f, 2026-09-25)

- **Source and item:** `trisotech`, item `https://www.trisotech.com/ai-fhir-and-bpm-in-suicide-prevention/`
  (ledger row key `ai-fhir-and-bpm-in-suicide-prevention`, verdict `UNCERTAIN`, corpus record 011).
- **What is needed:** nothing but playback — but playback is gated on a signed-in YouTube session.
  The player's own words in the embed are **"Viewer discretion is advised"** with a single
  **"Watch on YouTube"** control; that is the embed's response to a video whose playback YouTube
  will not serve anonymously. A YouTube session staged in the automation profile (as A1 does for
  UiPath) would clear it; so would the operator downloading the frames by hand while signed in.
- **Exact URLs tried, all gated, all 2026-09-25, all in the shared Chrome profile, read-only:**
  - `https://www.youtube.com/embed/fcC-fgC--QY?autoplay=1&mute=1&playsinline=1&origin=https%3A%2F%2Fwww.trisotech.com`
    — `document.querySelector('video')` exists but `readyState` 0, `duration` NaN, `videoWidth` 0.
  - `https://www.youtube-nocookie.com/embed/fcC-fgC--QY?…` (same query, same Referer header naming
    the embedding page) — identical: "Viewer discretion is advised".
  - `https://www.youtube.com/watch?v=fcC-fgC--QY` — the title resolves
    ("AI, FHIR, and BPM+ in Suicide Prevention: From Early Detection to Coordinated Care") but the
    player never becomes ready; the call that tried to start it was killed after 120 s.
  - The Referer header `https://www.trisotech.com/` was set on the browser context; it is what makes
    every *other* video of this source playable (without it the embed returns Error 153), so the gate
    is specific to this video, not to the route.
- **What was NOT done, deliberately:** no click on the discretion/age control, no "Sign in" click, no
  credential entry — §10 forbids all three unless the operator stages a session.
- **Items behind it:** **1 recording** (this one). It is the only gated video of the 22 in the source's
  video class; the other 21 were all played and inspected frame by frame.
- **If skipped:** the census still holds the item (row `UNCERTAIN`, record 011, poster frame captured),
  but no frame of the recording is read. The talk's written version is record 001 and its paired deck
  is already the source's one `E3-duplicate` against record 001, so what is unreachable is any live
  demonstration the slides do not carry.
- **Update 2026-09-26 (elicitation-6f): the gate no longer blocks anything.** The operator ruled
  that recordings are not an admissible source for this pass, so all 22 video rows of `trisotech`
  were superseded back to `UNCERTAIN` + `needs_visual_check` and rest on the host page alone. No
  frames are needed for the census, and the YouTube session this item asks for is no longer required.

### P10. camunda-docs-blog — the whole docs host refuses this machine's egress (elicitation-6f, 2026-09-26)

- **Source and items:** `camunda-docs-blog`. Every `docs.camunda.io` URL of the assignment's docs
  population is unreachable, and so is the Camunda 7 tree on `docs.camunda.org`.
- **Exact URLs tried, all 2026-09-26, read-only, no login and no captcha involved:**
  - `https://docs.camunda.io/sitemap.xml` — `curl`, exit 7 (no connection).
  - `https://docs.camunda.io/` — `curl` 000; a fresh Chrome tab returns `net::ERR_CONNECTION_REFUSED`.
  - `https://docs.camunda.io/docs/components/agentic-orchestration/` and
    `https://docs.camunda.io/docs/components/agentic-orchestration/ai-agents/` — same refusal.
  - `https://docs.camunda.org/` — same refusal.
  - Control in the same session, same `curl` and same browser: `https://camunda.com/` returns 200 and
    renders, and the blog sitemap at `https://camunda.com/blog/sitemap.xml` returns 200 with 1453
    `<loc>` entries. DNS for `docs.camunda.io` resolves (18.193.107.15); the refusal is at connection
    level, not DNS and not an HTTP status.
- **What was deliberately NOT done:** pinning the hostname to that raw IP with `--resolve`, a proxy,
  a mirror, or the assistant-side fetch tool. The harness flagged the IP pinning as routing around the
  egress control, so the block is treated as intended and is not worked around by any route.
- **What is needed:** either unblock `docs.camunda.io` and `docs.camunda.org` for this machine, or
  stage those two hosts' content (a saved copy of the `docs/components/agentic-orchestration/` subtree
  and its `.bpmn` asset links) where the agent can read it.
- **Items behind it:** the **entire docs half of the source**. Even the sitemap is refused, so the size
  of the docs tree cannot be enumerated from here — the assignment's `population_estimate: 120` cannot
  be checked for the docs part. The blog half is unaffected and is being censused in full.
- **If skipped:** the source still yields a complete blog census (sitemap-derived, 1435 unique posts),
  but two things are lost: (a) the docs pages that carry the source's C1/C2 evidence — "The AI Agent
  connector is the primary Camunda connector for building AI agents" and the ad-hoc sub-process tool
  feedback loop — can only be re-quoted from the assignment file, not re-evidenced; (b) any
  `docs.camunda.io` `.bpmn` asset links, the assignment's preferred evidence route, remain unread.

### P11. ibm-developer-watsonx — judgement-exclusion share is 12.9%, above the 10% ceiling, and that is the honest number (elicitation-3a, 2026-09-26)

**RESOLVED 2026-09-26 by the operator: 12.9% accepted as is** (no further flips). Recorded in `tools/accepted_shares.json` (max 256 judgement exclusions); `tools/audit.py` accepts the source at or below that count.

- **Source and items:** `ibm-developer-watsonx`. Not a fetch blocker — nothing is unreachable.
  The census is complete (1983 rows == population 1983, every row carrying verbatim evidence) and
  `python tools/audit.py ibm-developer-watsonx` reports exactly **one** problem: the
  judgement-exclusion share, 256 of 1983 rows (12.9%), against the 10% ceiling at
  `tools/audit.py` lines 85-88.
- **How it got there.** The first pass coded every page whose figure is a drawn
  architecture / component / block / pipeline / agent diagram as the *mechanical* E0-no-artefact
  with `judgment: false` — a code that asserts no judgement was made, when a notation call was in
  fact made on each. CLAUDE.md §3 lists "architecture box diagram" as an `E1-not-bpmn` example and
  `prompts/02b` states the convention (drawn non-BPMN diagram = `judgment: true`; screenshot of a
  UI/table/form/code listing = `judgment: false`), so 190 of those rows were recoded to `E1-not-bpmn`
  as appended superseding rows (`ledgers/ibm-developer-watsonx.raw/html/supersedes.json`), and the
  self-audit that `prompts/02_source-census.md` step 3 asks for flipped the 14 figures that carry
  process semantics to `UNCERTAIN` with a record and a tailored question each
  (`html/flips.json`, corpus records 034-047). Share went 4.0% -> 12.9%. The same exclusion
  decisions, now labelled as the notation calls they always were — this is not 190 new exclusions.
- **Why it cannot be lowered honestly.** The only two ways under the ceiling are (a) coding a drawn
  architecture diagram as "no artefact", which is the fault just corrected, or (b) claiming
  hesitation I do not have about a layer, tier, zone or topology diagram, i.e. moving ~242
  confidently-named `E1` rows to `UNCERTAIN`. (b) is mechanically possible — each would need a
  corpus record, an extra ~242 records on top of the current 47 — but it would misreport my
  confidence and dilute the flip signal the ceiling exists to protect, so I have not done it.
- **What is needed:** an operator ruling, either way.
  1. **Accept** 12.9% as a property of this source (it is saturated with drawn non-BPMN diagrams on
     AI pages) and treat `problems: 1` for this ledger as known and reviewed; or
  2. rule that structured (non-process) diagrams excluded on notation should be `UNCERTAIN` rather
     than `E1` for the whole sample — which changes the rule, not just this ledger, and I can
     re-run it here if instructed.
- **What was NOT done:** `tools/audit.py` was not edited, no threshold was worked around, and no row
  was left without evidence to lower a count. The 256 flagged rows are the ones to sample, and every
  one of them names in words the notation its figure is drawn in.
- **Items behind it:** none — nothing in this source is blocked or unreachable. This entry exists
  only so the single audit problem is visible to the operator rather than absorbed silently.

### P12. frends-docs — judgement-exclusion share 15.7%, RESOLVED to 1.8% by re-coding the `judgment` flags; one figure is broken at the vendor's source, no action (elicitation-3a, 2026-09-26)

**Two items, neither a fetch blocker. Nothing in this source is unreachable.**

**RESOLVED 2026-09-26 (same session, elicitation-3a) — item 1 was a coding artefact, not a
judgement count, and is now closed; item 2 stands as written and needs no operator action.
`python tools/audit.py frends-docs` → `problems: none`.** The 15.7% came from `decide.py`'s
`canvas-nonai` branch, which set `judgment: true` on all 141 E2 rows unconditionally, while
`templates/ledger.md` and `prompts/02_source-census.md` step 3 define an E2 as *mechanical*
(`judgment: false`) whenever the page's own text carries no AI/LLM term, and a judgement call
only when it does. Each of the 141 pages was re-read from its own markdown twin with the
per-page GitBook chrome removed (the platform injects "both humans and AI agents can read…"
into every page, so counting the chrome would make every row a judgement call for a reason
that is not the vendor's content): **131 pages carry no AI/LLM term** and were superseded to
`judgment: false` (`ledgers/frends-docs.raw/recode.py` + `supersede.py`; 141 appended
superseding rows, none rewritten, old footer kept and a new one appended); the **10 pages that
do** carry one keep `judgment: true`, with `judged_from` extended to record that the diagram's
own labels were read (SVG label text for the `.svg` exports, or the PNG read by eye on a named
contact sheet). Two hits that were English verbs ("embed C#" n=311, "embedding the Subprocess"
n=324) were re-coded; one page whose only hit is the word "chatbots" (n=766, where it names a
lead-capture source *outside* the process) was kept as the judgement it is. Every row being
downgraded was additionally swept for AI-adjacent vocabulary (smart, learn, predict, recogni,
vision, speech, translat, sentiment, anomal, recommend, generat, model, train, bot, decision
table, knowledge, copilot, assistant) and every hit is a non-AI usage named in the row's
`judged_from`. Share **148 (15.71%) → 17 (1.80%)**, below the ceiling, so no ruling is needed.

*The original item, kept for the record:*

**1. Judgement-exclusion share 15.7% (148 of 942 rows), above the 10% ceiling.** The census is
complete (942 rows == population 942, every row carrying verbatim evidence) and
`python tools/audit.py frends-docs` reports exactly this one problem. It is the same shape as P11
(ibm-developer-watsonx) but with a simpler cause: **frends-docs is the manual of a BPMN 2.0 tool**,
so 141 of its pages publish a genuine Process Editor diagram that contains no AI element
(`E2-no-ai-element`, `judgment: true`, because a notation call was made) and 7 publish a non-BPMN
artefact (`E1-not-bpmn`). The only way under the ceiling would be to call a diagram I have
confidently identified as BPMN "no artefact" — which is the fault the ceiling exists to catch — or
to claim hesitation I do not have across ~141 rows. Neither was done.

- **What was done instead**, because the ceiling's purpose is to make false negatives visible:
  every judged-excluded page carrying AI vocabulary (24 pages) was listed, its AI sentence read,
  and its figures opened. Two near-misses were promoted to INCLUDE — n=203 and n=239, whose AI
  shapes sit under captions that never say "AI" — and the other 22 are dismissed row by row, each
  quoting the AI mention and naming what it actually refers to (the AI Code Assistant, the AI
  Documentation Assistant, "AI & ML" as a connector-category heading, or the English words
  "prompted"/"prompt" and the substrings inside "WAITING" and "embedding"). One row's reason was
  corrected from E2 to E0 (n=40: no figure on it is a process diagram). Three archive pages
  (n=93, 147, 148) were re-coded from `E1` to `E3-duplicate` after a guard was fixed that had
  skipped the duplicate check for chat-classed pages under a version root; that correction, not a
  re-threshold, is why the share moved 16.1% -> 15.7%.
- **What is needed:** a ruling, either way. (a) Accept 15.7% as a property of a BPMN vendor's own
  manual and treat `problems: 1` for this ledger as known and reviewed; or (b) rule that a page
  whose diagram genuinely is BPMN 2.0 but carries no AI element should be `UNCERTAIN` rather than
  `E2` for the whole sample — a change to the rule, not to this ledger, which I can re-run if
  instructed.
- **What was NOT done:** `tools/audit.py` was not edited, no threshold was worked around, and no
  row was stripped of evidence to lower a count.

**2. `https://docs.frends.com/bap/general/single-sign-on` — its only figure is broken at the
vendor's source.** The vendor's own markdown twin publishes the image as
`<img src="broken://files/oH85GMcOLRjv7m4KGNcN">` — a GitBook placeholder for an asset that no
longer resolves on its storage — so the figure could not be fetched by any client, browser or not.

- **What was tried:** the figure was fetched from the asset URL in the page's markdown; the
  markdown itself is what carries the `broken://` scheme, i.e. the break is upstream of me.
  Nothing was guessed and no image was substituted.
- **What was done:** the page is judged on its caption alone ("Entra ID app registration view.",
  an Entra ID setup screenshot — application chrome), so its row is `E0-no-artefact` with the
  break recorded in the row's note and in the ledger header. Its verdict would not change if the
  image reappeared: it is not a process diagram either way.
- **Operator action: none available, and none needed.** If the vendor republishes the asset, the
  row could be re-checked visually; it is named here so the reviewer knows which single row of
  942 rests on a caption rather than on a figure that was looked at.

### P13. camunda-docs-blog — judgement-exclusion share is 10.6%, just over the 10% ceiling, and that is the honest number after the visual pass (elicitation-6f, 2026-09-27)

**RESOLVED 2026-09-27 by the operator: 10.6% accepted as is** (no further flips, option 1
below). Recorded in `tools/accepted_shares.json` (max 152 judgement exclusions); re-run here
after the operator's edit, `python tools/audit.py camunda-docs-blog` prints `problems: none`.
Nothing here is unreachable: the census is
complete (1439 rows == population 1439, every row carrying verbatim evidence) and the blog half
was fully readable — the four `BLOCKED` rows are the docs half, i.e. P10, which this entry does
not touch.

- **Source and items:** `camunda-docs-blog`. `python tools/audit.py camunda-docs-blog` reports
  exactly **one** problem: the judgement-exclusion share, 152 of 1439 rows (**10.6%**), against
  the 10% ceiling at `tools/audit.py` lines 85–88. Pre-pass it was 141 rows (9.8%).
- **What the 152 are.** `E1-not-bpmn` 126 and `E2-no-ai-element` 26. The 126 are drawn non-BPMN
  diagrams on pages that do mention AI — box/block/component/layer diagrams 59, architecture
  diagrams 37, UML 1, mockup/wireframe 1, and each row's note names in words what its figure is
  drawn in. `CLAUDE.md` §3 lists "architecture box diagram" as an `E1` example and `prompts/02b`
  states the convention: a drawn non-BPMN diagram is `judgment: true`, a screenshot of a
  UI/table/form/code listing is `judgment: false`. The 26 `E2` rows each quote verbatim the AI
  mention they dismiss and say what it refers to (a release-note bullet about a connector, an
  Optimize analytics feature, prose about the Copilot that *authors* the diagram).
- **How it moved.** The native-resolution pass over the 110 `needs_visual_check` rows disposed
  all of them (`ledgers/camunda-docs-blog.raw/visual-review.txt`, `visual-progress*.jsonl`) and
  converted 56 rows the pre-pass had left `UNCERTAIN` — which count as neither inclusion nor
  exclusion — into `E2`/`E1` exclusions. Eleven of those are judgement-true, so the share is
  141 → 152. This is the pass doing what it was asked to do, not new judgement.
- **Not forced down, and the two ways down are dishonest here.** (a) Coding a drawn architecture
  diagram as `E0-no-artefact` would assert that no notation call was made when one was — that is
  the exact fault the ibm-developer-watsonx recode (P11) corrected. (b) Claiming hesitation I do
  not have about a layer/tier/topology diagram, i.e. moving ~126 confidently-named `E1` rows to
  `UNCERTAIN`, would misreport my confidence and dilute the flip signal the ceiling protects.
  Seven rows *were* moved the honest way: n=77, 106, 422, 980, 1036, 1302, 1358 carried
  `judgment: true` on pages whose only "AI term" is a substring ("promptly", "prompts",
  "prompting", "embedding") or the ordinary word "model" in "the BPMN model" — those flags were
  reset to false, which is a correction to the labels, not a threshold.
- **What was needed** (ruled 2026-09-27 — the operator took option 1, so nothing below is
  outstanding): an operator ruling, either way —
  1. **Accept** 10.6% for this source (a vendor blog and docs site saturated with drawn
     architecture diagrams on AI pages), by adding it to the operator-owned
     `tools/accepted_shares.json` with `max_exclusions` ≥ 152, as was done for
     ibm-developer-watsonx (P11); or
  2. rule that a structured non-process diagram excluded on notation should be `UNCERTAIN` rather
     than `E1` for the whole sample — a change to the rule, not to this ledger, which I can
     re-run here if instructed.
- **What was NOT done:** `tools/audit.py` was not edited, `tools/accepted_shares.json` was not
  edited (operator-owned), no threshold was worked around, and no row was stripped of evidence to
  lower a count. The 152 flagged rows are the ones to sample; every one names the notation its
  figure is drawn in or quotes the AI mention it dismisses.

### P14. firestart — judgement-exclusion share was 37.4%, above the 10% ceiling. **RESOLVED 2026-09-27 by operator: class → UNCERTAIN, one class ruling pending** (elicitation-3a, 2026-09-27)

`python tools/audit.py firestart` → one problem, exactly this. Census is closed at **494 rows**
(header + 494 item rows + footer; `firestart.frontier.txt` = 494 URLs, `problems` otherwise none):
`INCLUDE=13, UNCERTAIN=6, EXCLUDE=475` → `E0-no-artefact=249, E1-not-bpmn=179,
E2-no-ai-element=6, E3-duplicate=41`, `BLOCKED=0`.

- **Why the share is 37.4% (185 of 494, of which 179 are E1, 6 are E2).** This is not a thin
  census: 173 of the 179 E1 rows are **one homogeneous class**, and the class is a finding in its
  own right. They are real process depictions with AI-labelled steps — the inline SVGs carry the
  labels "KI-Analyse", "AI routing", "OCR-Erfassung", "KI-Klassifikation", "Muster erkennen",
  "Anomalie erkennen", "Human-Freigabe" — which the site hand-authored as marketing graphics rather
  than modelling them. The DOM settles the notation call for every one of them: the route's live
  DOM has 0 elements carrying a `djs-*`/`bpmn-*` class, 0 `data-element-id`, 0 `<canvas>` and no
  `<bpmn:process>`, and 171 of the 173 contain **no circle/ellipse and no polygon at all** — i.e.
  no event and no gateway, so nothing that could be read as BPMN 2.0. The remaining 6 E1 rows are
  a product-comparison infographic (`n=81`) and a Nintex-designer screenshot on four language
  mirrors (`n=413–416`); the 6 E2 rows are the four platform/homepage process exports whose pages
  do discuss AI (`n=1, 2, 15, 16, 325, 422`).
- **What was done instead of trimming.** The six exports whose task markers match none of this
  source's AI markers were moved **from E2 to UNCERTAIN** with `needs_human_ruling` and the exact
  question (11 route-instances, `corpus/firestart/004, 005, 009, 010, 016, 017`); the comparison
  infographic and the four designer mirrors were moved from E0 to E1 after opening them at full
  size; one route was added to the population after being found only as an iframe on the homepage
  (`/preview/persona-mockups`, an interactive app mockup whose step 2 is "KI/OCR"). All 11 flips
  moved **towards inclusion**, i.e. they raise the share, which is the direction CLAUDE.md §2
  prescribes. No row was re-coded to move it down.
- **What is needed:** an operator ruling, either way —
  1. **Accept** 37.4% for this source by adding it to the operator-owned
     `tools/accepted_shares.json` with `max_exclusions` ≥ 185, as was done for
     ibm-developer-watsonx (P11); and/or
  2. accept that the 173-row class needs only a **sample** review rather than 173 individual ones —
     one row per label family ("KI-Analyse", "AI routing", "OCR-Erfassung", "Human-Freigabe")
     exercises the whole class, because the class is homogeneous by construction (every one of the
     173 has ≥3 boxes, ≥3 arrows and at least one AI-labelled step, and none has an event or a
     gateway); or
  3. rule that a hand-authored SVG flow graphic on an AI page should be `UNCERTAIN` rather than
     `E1` for the whole sample — a change to the rule, not to this ledger.
- **What was NOT done:** `tools/audit.py` was not edited, `tools/accepted_shares.json` was not
  edited (operator-owned), no threshold was worked around, and no evidence was removed from a row
  to lower a count. Every E1 row names the notation its graphic is drawn in and quotes its own
  labels; every E2 row quotes the AI mention it dismisses and says what that mention refers to.

**Resolution (elicitation-3a, 2026-09-27).** The operator ruled option 3, as one class: the 173
inline-SVG linear-flow rows are `UNCERTAIN`, because rounded boxes plus arrows can be read as BPMN
tasks and sequence flows, and CLAUDE.md §3 says an ambiguous notation is `UNCERTAIN`, never `E1`.

- **Applied:** 173 superseding rows appended to `ledgers/firestart.jsonl` (same `n`,
  `supersedes_row: true`, `judgment: true`, `needs_human_ruling: true`, `needs_visual_check: false`,
  `class: firestart-inline-flow`, one class question prefixed `CLASS firestart-inline-flow:`). Each
  has its own record in `corpus/firestart/` (NNN 020–192) with the page quote, the step labels as
  printed, a white-background PNG render of the route's own inline `<svg>` and the markup archived
  beside it as `.svg`. The 6 remaining E1 rows are n=81, n=413–416 (product figures that are not
  linear flows) and n=494 (interactive app mockup) — unchanged.
- **Re-audit:** `python tools/audit.py firestart` → **problems: none**. `EXCLUDE=302, INCLUDE=13,
  UNCERTAIN=179, BLOCKED=0`; judgement exclusions 12 (2.4%), review queue `rulings=179`,
  192 records, 175 superseded rows.
- **One class ruling still pending, because the class is not uniform in where the AI sits.** The
  operator's question assumed an AI-labelled step in every member; that holds for **107** rows
  ("AI routing", "KI-Analyse", "OCR-Erfassung", "KI-Skill-Extraktion"), but **7** rows name the AI
  only in the page's own solution prose, and **59** rows have no AI in the graphic and none in the
  page's own text — the only AI string on those 59 pages is the site chrome ("KI Workflows" /
  "AI Workflows" in the navigation). The class question carries all three variant clauses, so one
  ruling still covers the class; for the 59, criterion C1 is the researcher's call. `E2` would be
  the mechanical reading there and I did **not** take it — the operator ruled the class collect,
  and every such row now carries the question in its own record instead of being silently dropped.
- **Two sub-case rows:** n=326 and n=327 (the two language mirrors of the same blog post) serve
  stacked-zone architecture figures rather than linear flows; their question says so explicitly.
- **Also corrected while resolving this:** the ledger header's `date_start` is 2026-09-26 (earliest
  artefact on disk) and each row's `accessed` now carries the date of the reading its verdict rests
  on (2026-09-27 for the 428 rows judged from the route's rendered text, 2026-09-26 for the 66
  judged from the crawl and the downloaded export).



### P15. uipath-marketplace — opening a template in Studio Web created a draft solution in the tenant; two blockers pending (elicitation-7b, 2026-09-28)

- **Incident (needs a human, one item):** at about 08:50 GMT the in-tenant marketplace page
  `https://cloud.uipath.com/masterthesismetz/marketplace_/listings/loan-processing1915` offered
  "Use in Studio Web" → `portal_/cloudrpa?redirectPath=studio_/templates/47becc70-617c-4120-bb28-0a81417c9bfb`.
  Navigating that link (expected: template preview) redirected to
  `studio_/designer/bc903037-b95a-40ea-be71-ef7a9b068030?solutionId=786fa94d-a4dc-4f25-b93f-08df1807e6ac`
  and the Cloud Workspace list now shows **"Loan Processing 1 6 1 4 2" — Draft — edited "19 seconds
  ago"**. Nothing was edited, saved, published, renamed or deleted; the draft was left in place.
  **Action:** delete or keep that draft; the agent does not delete in vendor tools.
  **Ruling 2026-09-28: the researcher deletes it** (listed in
  `ledgers/uipath-marketplace.raw/tenant-drafts-created.md`). Studio Web: option (ii), existing drafts only.
- **Second incident, cleanup needed (2026-09-28 ~09:20 GMT):** under ruling (a) the existing July draft
  "Summarize Outlook email attachments with AI 1 1" (solutionId a61a72a5-7e18-49fc-8d49-08dee9718be7) was
  opened. On opening its Process.bpmn, Studio Web by itself created 4 folders and 4 files (an "evals"
  folder appeared), posted EntryPoints, and re-saved 4 files **including Process.bpmn** (fileId
  f2b79695-323d-4c3f-afaf-63f7813dbf51); a first PUT had already hit the agent project on open
  (file 0e4867bb-c875-4648-a849-07e4a63044a4). `checksession` returned 503 twice, so Studio Web was stopped.
  **Action:** review/revert or delete that draft's added "evals" folder and files if the July state matters;
  every request is itemised in `ledgers/uipath-marketplace.raw/tenant-drafts-created.md`.
  **Ruling (via elicitation-5a): no further Studio Web**; Maestro/agent templates without inspected evidence
  are `UNCERTAIN` with the ruling-(ii) question.
- **Ruling needed (Studio Web mechanics):** there is no read-only way to open a marketplace
  template — every open creates a draft solution. Options sent to the orchestrator: (i) allow opens
  and list the created drafts for cleanup (as the July precedent did — about 40 drafts from it
  still sit in the workspace, "2 months ago"); (ii) inspect only the existing July drafts
  read-only, as dated evidence; (iii) no Studio Web, every Maestro template `UNCERTAIN`.
  Studio Web opens are paused until ruled.
- **Blocker (listing crawl):** 1658 of 2326 listing pages returned HTTP 429 with
  `Cf-Mitigated: challenge` (Cloudflare challenging scripted GETs from this IP) after about 190
  fetches at 1 req/s. The orchestrator's protocol applies: probe once after ≥ 60 min, resume at
  ≤ 1 req/5 s with exponential backoff, stop after three consecutive challenges, then `BLOCKED` rows.
  URLs are in `ledgers/uipath-marketplace.frontier.txt`. Status updates follow here.
