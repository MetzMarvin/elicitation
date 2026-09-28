---
source: nintex
source_name: Nintex (Process Manager BPMN + Nintex Automation AI agents)
source_type: vendor site (blog + product docs)
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: NO (operator ruling 2026-09-24)
  C2_native_bpmn20: YES
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES
access: public
population_type: enumerable
population_estimate: 40
effort: medium
needs_logged_in_browser: false
status: OUT-C1 (not surveyed; kept for audit trail)
---

## Criteria evidence

- **C2 YES** — https://www.nintex.com/blog/technical-teams-document-complex-processes-with-bpmn/
  (blog dated 9 November 2023, read 2026-09-23): "we are thrilled to introduce the addition
  of BPMN (business process model and notation) process modeling capability to Nintex
  Process Manager. Nintex Process Modeling is set to transform the way organi[sations]…"
- **C1 UNCLEAR, for a structural reason worth stating precisely** — Nintex's AI story and
  its BPMN story appear to live in **two different products**:
  - **BPMN** is in *Nintex Process Manager* / *Nintex Process Modeling*, which is oriented
    to process **documentation**.
  - **AI agents** are marketed under *Nintex Automation* — the site-wide navigation reads
    "See how Nintex orchestrates your people, systems, and AI agents for effortless
    efficiency" — which is a separate, non-BPMN workflow engine.
  If the two never meet in a single artefact, Nintex promotes AI *and* BPMN without ever
  promoting AI-**in**-BPMN, and C1 fails. I could not settle this from the pages opened.
  Mirrored in `OPERATOR-TODO.md` (B9).
- **C3 YES** — blog and product pages served anonymously.
- **C4 YES** — Nintex is a large workflow-automation vendor with a substantial Microsoft-365
  install base and an active community (`community.nintex.com`).

## The question Pass 2 must answer first

**Does any Nintex artefact show an AI element inside a BPMN diagram?**

Answer that before enumerating the rest. If the answer is no after the AI pages and the
Process Manager BPMN pages have both been worked, then this source contributes zero
artefacts and that is a *finding* to report, not a failure — it is a clean example of a
vendor with both capabilities and no promoted integration between them.

## Entry points

- `https://www.nintex.com/blog/technical-teams-document-complex-processes-with-bpmn/` — the
  BPMN announcement (anchor page)
- Pages confirmed to exist by `site:` sweep on 2026-09-23 (titles from the result list,
  **not opened**):
  - "Artificial intelligence at Nintex"
  - "Nintex Unveils Latest AI Capabilities to Accelerate Process …"
  - "What's new in Nintex's Process Platforms"
  - "Process modeling: your blueprint for getting work done"
  - "Process Management"
  - "Why process mapping is more than just flow charts"
  - "Transform Your Visio Diagrams into Dynamic BPMN …" (`community.nintex.com`)
  - "Get started with Nintex Process Manager MCP" (`community.nintex.com`)
- `https://www.nintex.com/blog/` — blog index; check for `sitemap.xml` first

## Enumeration instructions

1. Work the **intersection first**: the BPMN pages and the AI pages, looking for any single
   artefact containing both. Record the result explicitly in the ledger header note.
2. Then enumerate the blog index in full. Do not keyword-filter.
3. `community.nintex.com` is a separate, non-enumerable population. Two community items are
   already known to be relevant ("Nintex Process Manager MCP", "Transform Your Visio
   Diagrams into Dynamic BPMN"). Treat the community as a `search-protocol` sub-stream with
   every query logged verbatim, or scope it out and say so.

## Artefact mechanics

- Marketing blog: static images, often stylised marketing illustrations rather than real
  diagrams. A marketing illustration is `E1-not-bpmn` — but name it as such.
- "Transform Your Visio Diagrams into Dynamic BPMN" implies Visio import. A Visio diagram
  rendered as BPMN is still BPMN; a Visio flowchart is not. Judge the output, not the input.
- Capture original image assets at native resolution.

## Known gotchas

- **The site navigation mentions AI agents on every single page.** "See how Nintex
  orchestrates your people, systems, and AI agents" is site chrome, not page content. Do
  **not** record it as evidence of an AI element in a process — it will otherwise produce a
  false `INCLUDE` on every page in the source. Extract from `main`/`article`, not `body`.
- Nintex Process Manager (documentation) and Nintex Automation (execution) are different
  products with different notations. Always record which product an artefact belongs to.
- The anchor blog post is from November 2023 and predates the current AI wave; do not assume
  it reflects the present product.

## Spot checks performed by Pass 1

Spot check only, not a verdict:

- The BPMN announcement blog post was opened and the C2 sentence read from the page body.
  The AI pages were **not** opened — which is exactly why C1 is `UNCLEAR`.

## RESUME

(empty)
