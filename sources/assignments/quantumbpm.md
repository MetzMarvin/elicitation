---
source: quantumbpm
source_name: QuantumBPM (BPMN engine vendor; quantumbpm.com blog + docs)
source_type: vendor blog
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: YES
  C2_native_bpmn20: YES
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES (operator ruling 2026-09-24, general C4 rule)
access: public
population_type: enumerable
population_estimate: 10
effort: small
needs_logged_in_browser: false
status: DONE (elicitation-3a, 2026-09-25)
---

## Result

Population **100**, closed and fully enumerated: the site's own `sitemap.xml` (84 URLs) plus
the blog taxonomy/author routes the sitemap omits (11 tag pages, `/blog/tags`,
`/blog/archive`, 2 author pages) and 2 docs category pages, all found by diffing the union of
in-page links against the sitemap (never guessed); the diff is now empty. 100/100 rows,
`python tools/audit.py quantumbpm` → **`problems: none`**.

Verdicts: INCLUDE 2, UNCERTAIN 0, EXCLUDE 98 (E0 79, E2 13, E1 6), BLOCKED 0. Judgement
exclusions 7 = 7.0 % (under the 10 % cap). Review queue: visual-check 0, rulings 0. Three rows
carry appended corrections (the header line, row 13's visual flag, row 1's verdict); the
visual checks were done by the orchestrator (elicitation-5a, 2026-09-25).

Collected artefacts:

| # | page | artefact | AI element inside the process |
|---|---|---|---|
| 001 | blog/orchestrating-ai-agents-with-bpmn | downloadable `.bpmn` + `.dmn` (captured byte-exact) | `serviceTask` "Agent: plan & act" with `quantum:taskDefinition type="agent-plan"` inside an `adHocSubProcess` ("Resolve", `quantum:adHoc activeElementsCollection=["Task_agent_plan"]`, `completionCondition resolved = true`); DMN decision `route-support-ticket` (hitPolicy FIRST, confidence `>= 0.7`) gates the `Auto-resolvable?` exclusive gateway |
| 002 | blog/how-bpmn-engines-work | two figures (1578×458, 1720×462), read out by the orchestrator's visual check | "AI analyzes request" and "AI Generates Response" as service tasks either side of a gateway in `ai-support-triage`; "AI Classification" as a service task before the human-review gateway in `invoice-processing`; prose: "An AI step is an ordinary service task" |

Not collected, and why:

- `/` (landing page, n=1) — the hero is a BPMN holiday-booking saga in the modeler (start →
  "Validate Budget" → parallel gateway → "Book Rental Car" / "Book Hotel" / "Book Flight"
  with compensation boundary events → parallel join; run panel lists TASK_BOOKCAR /
  TASK_BOOKHOTEL / TASK_BOOKFLIGHT) with **no AI element** anywhere in the diagram or panels
  → `E2-no-ai-element` (judgement row). Its captures moved to `ledgers/quantumbpm.raw/`.

Open gaps / caveats:

- **Image rendering was unavailable to this session** (opening a downloaded PNG returned no
  viewable content) — it could see images in the previous session, so the cause is on the
  agent side, not the sources. Worked around for this source: the orchestrator ran the visual
  checks and the verdicts were appended. For the rest of the queue the plan is to capture
  every candidate figure, keep the row UNCERTAIN + `needs_visual_check` with the alt/caption
  text, and list the figure paths in the report for the orchestrator to read.
- Residual risk of that limitation: an AI element drawn inside a figure whose page never
  names AI in text, alt or filename. No such page exists by any other channel in this source.
- The site chrome repeats post titles ("Orchestrating AI Agents with BPMN") on every page, so
  the whole-page AI keyword test flags all 100 items; the mechanical E2 test was applied to
  the page's own `<article>` body (documented in the ledger header).

## Criteria evidence

- **C1/C2 YES**: https://quantumbpm.com/blog/orchestrating-ai-agents-with-bpmn (13 June
  2026): "A single agent step is a service task. A reasoning loop is an ad-hoc
  sub-process." Also: "When a token enters an ad-hoc sub-process, the engine parks it and
  exposes the inner activities as separately triggerable steps."
- **C3 YES**. **C4 UNCLEAR**: a small, young vendor. See the general C4 rule (B5–B7).

## Promotion mode

AI orchestrating an ad-hoc sub-process, plus an agent step as a service task. This is the
same pattern as Camunda (1) and Aletyx (30), reached independently.

## Entry points

- The anchor post. It contains about 10 figures/SVGs/code blocks. Check each one for BPMN
  diagrams and XML.
- `quantumbpm.com/blog/tags/agents` ("2 posts tagged with 'AI Agents'"), `quantumbpm.com/blog`
- "How a BPMN Engine Works, and What You Can Build With One" (blog)

## Enumeration instructions

Enumerate the full blog index (small), then any docs/examples section linked from the site
nav. Inline BPMN XML in `<pre>` blocks is decisive evidence.

## RESUME

(not needed: the source is DONE; no checkpoint was taken)
