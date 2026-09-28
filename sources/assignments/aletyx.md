---
source: aletyx
source_name: Aletyx (Kogito AI add-ons, aletyx.ai)
source_type: vendor GitHub repository + vendor site
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: YES
  C2_native_bpmn20: YES
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES (operator ruling 2026-09-24, general C4 rule)
access: public
population_type: enumerable
population_estimate: 25
effort: small
needs_logged_in_browser: false
status: DONE (elicitation-3a, 2026-09-25; census complete, `python tools/audit.py aletyx` = problems: none)
---

## Criteria evidence

- **C1 YES**: https://github.com/aletyx/aletyx-kogito-ai-addons/blob/main/README.md
  (2026-09-24): "Kogito add-ons that give BPMN processes first-class access to
  large-language-model capabilities (task selection, prompt formulation, structured-output
  execution, tool calling, and execution history)". The "Ad-Hoc Subprocess" add-on is
  described as "An AI orchestrator that drives a Kogito ad-hoc subprocess: picks the next
  user task to run".
- **C2 YES**: "From the palette, expand the Custom Tasks → Aletyx AI category and drag the
  Ad-hoc Intelligence task inside the ad-hoc subprocess. Add your other (human) tasks
  inside the same ad-hoc subprocess." The README mentions `.bpmn` models and a `.wid`
  work-item definition.
- **C3 YES**: public GitHub repository.
- **C4 UNCLEAR**: small, young vendor (the commercial successor of the Red Hat jBPM/Kogito
  team). No customer-base evidence was read. See the general C4 rule proposed at B5–B7.

## Promotion mode

A custom BPMN task (display name "Ad-hoc Intelligence", category "Aletyx AI") placed
**inside an ad-hoc sub-process**, where it orchestrates the human tasks. This is
structurally the same as Camunda's AI Agent in an ad-hoc sub-process, reached
independently in the KIE lineage.

## Entry points

- `github.com/aletyx/aletyx-kogito-ai-addons`: README (anchor). Enumerate the repo tree for
  `.bpmn` files, examples and per-add-on READMEs.
- `aletyx.ai/intelligent-process-automation` ("jBPM & KIE Server Modernization") and
  `aletyx.ai/resources` ("All Resources"): Google result titles, **not opened**.
- A LinkedIn post "How to integrate AI in jBPM workflows" (20+ reactions) appeared in the
  results. It belongs to the practitioner layer: out of scope per Gate 1 ruling B4, do not enumerate. Not opened.

## Enumeration instructions

1. Enumerate the repo: every `.bpmn` file (decisive evidence: `<bpmn:adHocSubProcess>` with
   the custom task inside), every README, and every example project.
2. Then the `aletyx.ai/resources` index.
3. Do not keyword-filter.

## Artefact mechanics

- `.bpmn` XML in the repo is the best evidence available. Read it raw via GitHub's "Raw"
  link (extract the link, do not guess the raw URL).
- **Tooling gotcha:** the `claude-in-chrome` privacy filter blocked the *entire* README text
  output because the page contains URL-like tokens with query strings. Strip `\S*[?=&]\S*`
  tokens before returning text.

## Spot checks performed by Pass 1

- README opened. The add-on description and the modelling instructions were quoted.

## Completion (elicitation-3a, 2026-09-25)

**Done.** The RESUME block this replaces is superseded; everything it listed was executed.

- Ledger: `ledgers/aletyx.jsonl` - 497 rows, `population_size: 497`, `status: COMPLETE`.
  Frontier: `ledgers/aletyx.frontier.txt` (497 lines). `python tools/audit.py aletyx`:
  **problems: none**.
- Verdicts: INCLUDE 1, UNCERTAIN 2, EXCLUDE 494 (E0 416, E1 50, E2 23, E3 5), BLOCKED 0.
  Judgement exclusions 39 = **7.8 %** (cap 10 %).
- Records: `corpus/aletyx/001_process-bpmn-adhoc-intelligence.md` (+ `001_process.bpmn`,
  66 950 B, sha256 `154f36c847982f6c`), `003_enterprise-kogito-ai-agent-nodes.md`
  (+ `003_*.png`), `004_intelligent-process-automation-ai-agent-node.md` (+ `004_*.png`).

### Two deviations from the RESUME plan, both deliberate

1. **Population is 497, not 498/499.** Surface C contributes **7** rows (n=491-497), not 8:
   `aletyx-kogito-ai-addons` is the eighth org repository but *is* Surface A, enumerated
   exhaustively at file level (n=1-162), so a repo-level row for it would have to carry a
   verdict about a repository that does contain a process artefact. The ledger header `note`
   states this.
2. **No `BLOCKED` row, no OPERATOR-TODO entry.** Blocker P5 (the tutorial's `.bpmn`
   download, `/docs/guides/tutorials/bpmn-example`) is not a blocker: the link
   `github.com/aletyx-labs/examples/raw/main/.../employee-onboarding.bpmn` is a **dead link**
   that returns GitHub's "Page not found" HTML (268 999 B, sha256 `4d2049c2d2cbf63c`). A dead
   link is a sanctioned `E0-no-artefact`, so that page is an ordinary EXCLUDE row (n=440)
   with the dead link as its evidence.

### The two ruling questions (verbatim, also on the ledger rows)

- **n=199** `https://aletyx.ai/enterprise-kogito/` - the page asserts AI Agent nodes inside the
  process ("AI Agent nodes handle ad-hoc intelligent tasks inside workflows.") while the only
  BPMN figure it draws (the Dev Console process-instance monitor) shows no AI-labelled element.
  *Is that page an artefact to record, or is the assertion a product claim that stays
  E2-no-ai-element?*
- **n=206** `https://aletyx.ai/intelligent-process-automation/` - same pattern: "AI Agent Node
  integrates LLMs directly into your process flow." against a clean hiring-process drawing with
  no AI element. *Artefact, or product claim that stays E2-no-ai-element?*

### Notes for the researcher

- The source's only AI element drawn **inside** a process model is the repo file (n=139,
  `process.bpmn`): an ad-hoc sub-process "Loan Investigation" whose children include a
  `drools:taskName="AletyxAI"` task named "Aletyx Intelligence". The vendor's website names the
  AI node in prose on four pages and never draws it.
- Two visual determinations were made from images and are worth a second look:
  `ledgers/aletyx.raw/visual/002_rules-editor-dmn-drd.png` (the blurred canvas figure on
  `/blog/2026-mortgage-gse-compliance/`, ruled a DMN decision-requirements diagram -> E1) and
  the two UNCERTAIN records' figures (`corpus/aletyx/003_*.png`, `004_*.png`).
- `ledgers/aletyx.raw/` holds all raw evidence (fetched pages, figures, contact sheets, the
  unpacked repo, the row-building scripts) and is not needed to read the ledger.
