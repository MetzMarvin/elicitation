---
source: bonitasoft
source_name: Bonitasoft / Ofelia (Bonita BPM docs + Ofelia product pages)
source_type: vendor documentation + vendor site
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: YES
  C2_native_bpmn20: YES
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES
access: public
population_type: enumerable
population_estimate: 35
effort: medium
needs_logged_in_browser: false
status: DONE (elicitation-6f, 2026-09-25; 936 rows == population 936, 2 INCLUDE, audit problems: none)
---

## Criteria evidence

- **C1 YES**: https://documentation.ofelia.com/bonita/latest/process/ai-connector
  (2026-09-24): "Bonita AI connectors let you integrate advanced language models like
  OpenAI, Anthropic, Google Gemini, Mistral, Azure AI Foundry, Ollama, DeepSeek, Groq, and
  Cohere into your business processes." The connectors are "available for Bonita 10.2
  Community (2024.3) version and above".
  https://www.ofelia.com/product/bonita-bpm: "AI Connectors OpenAI & Mistral native + AI
  Agent Orchestrator" and "Secure LLM integration within deterministic workflows."
- **C2 YES**: https://documentation.ofelia.com/bonita/latest/process/diagram-overview:
  "A process diagram is the representation in the Bonita studio of a group of processes
  (BPMN pools)." Items are dragged from "the BPMN elements menu".
- **C3 YES**: anonymous. The AI connectors ship in the Community edition.
- **C4 YES**: a long-standing open-source BPM vendor.

## Promotion mode

Connectors attach to BPMN activities as implementation. The diagram probably shows an
ordinary task, and the AI binding lives in the connector configuration. That is the
**delegated-binding** mode, as for UiPath and Scheer PAS. **Judge accordingly:** a plain
task whose surrounding text binds it to an AI connector is `UNCERTAIN` with the binding
quoted, never `E2`.

## Entry points

- `documentation.ofelia.com/bonita/latest/process/ai-connector`: anchor
- Bonita docs indexes seen in results: "Connectors", "Process diagrams" (`diagrams-index`),
  "Getting Started Tutorial", "Start building an application: draw a BPMN process diagram"
- `www.ofelia.com/product/bonita-bpm`, plus the Ofelia home page ("AI Orchestration Platform for
  Enterprise Operations"). The "AI Agent Orchestrator" and "Ofelia Agentic" pages were not
  opened.
- The GitHub repos of the AI connectors (likely `bonitasoft/bonita-connector-ai*`) are
  **not verified**. Do not guess. Find them via links on the docs page.

## Enumeration instructions

1. Pin the docs version (`latest`, resolve it to a number and record it).
2. Frontier = AI connectors page(s) + Process diagrams index + Getting Started tutorial +
   the Ofelia product/agentic pages.
3. Look for example processes that use an AI connector: tutorial diagrams, community
   examples, and the connector repos' README diagrams.

## Artefact mechanics

- Docs are Antora-style HTML. `article` holds the content.
- Bonita Studio diagrams appear as screenshots. `.bos` / `.proc` exports may exist in
  example repos. `.proc` is Bonita's own format, **not** `.bpmn`, but Bonita Studio can export
  BPMN 2.0.

## Known gotchas

- **Rebrand drift:** bonitasoft.com → ofelia.com, and documentation.bonitasoft.com →
  documentation.ofelia.com. Record both hosts and treat them as one source.
- "Natural language -> BPMN modeling" on the product page is design-time AI (E2).

## Spot checks performed by Pass 1

- Product page, AI connectors page and Process Diagram overview: opened and quoted.

## Census record (elicitation-6f, 2026-09-25)

**Status DONE. `python tools/audit.py bonitasoft` → `problems: none`. 936 rows == population 936 == 936
frontier lines; ledger `ledgers/bonitasoft.jsonl` opened with a header and closed with
`status: DONE`.**

**Enumeration.** Two groups, both finite. (1) The portal: the docs sitemap index
(`documentation.ofelia.com/sitemap.xml`) gives one sitemap per component with an exact URL count, and
the marketing sitemap (`www.ofelia.com/sitemap.xml`) has one `<loc>` per hreflang — the population is
the `latest` version of all 7 doc components (bcd 9, bonita 374, cloud 30, labs 20, process-designer
41, test-toolkit 15, ui-builder 44 = 533), plus the 20 paths published only under an older version,
plus the 254 English pages of www.ofelia.com (of 1067 `<loc>`, the rest being fr/es locales of the
same pages) = **807 pages**. `latest` resolves to **2026.2**. No keyword facet narrowed anything: every
page's content region is screened for process/AI tokens and diagram-bearing figures, and everything
that fires is judged by eye. (2) The linked GitHub repositories: every repository URL extracted from
the crawled pages (never guessed), enumerated as one row per repository (**53** canonical, after
collapsing two `.git` duplicates) plus one row per `.bpmn`/`.proc` file in their trees (**76**) =
**129 rows**. `population_size: 936`.

**Verdicts.** **2 INCLUDE**, 14 UNCERTAIN (every one with `needs_human_ruling` and a corpus record),
920 EXCLUDE (`E0-no-artefact` 778, `E1-not-bpmn` 40, `E2-no-ai-element` 96, `E3-duplicate` 6),
0 BLOCKED. Judgement exclusions **87 of 936 = 9.3 %** (inside the 10 % gate): 92 pages plus 2 process
files whose figures were looked at one at a time, all enumerated in the footer's `figures_looked`.

**The two INCLUDEs are superseding rows, appended after the footer.** Records `010`–`011` (the AI
connector demo processes) were first written UNCERTAIN, each carrying the question "worked example in
the vendor's code, or corpus item?". The orchestrator settled it on 2026-09-25: delegated binding is
deliberately in scope — "diagrams where the AI element is only visible as a task *property* or
implementation binding, not as a distinct BPMN element type" (prompts/02_source-census.md) — and a
test resource in a repository inside the enumerated population is not a ground for doubt (shared
rules §4 bans "internal template / boilerplate listing" as a reason to hold back). The INCLUDE rows
are therefore appended with `supersedes_row` / `prior_verdict` / `correction`, and the superseded
UNCERTAIN rows stay in the ledger so the correction is auditable (`tools/audit.py` reads
"+2 superseded rows"; the last row for an `n` wins). Both records now read `verdict: INCLUDE`, with
the answered question kept in the front matter as the record of what was asked.

**The promotion mode the assignment predicted is the one that exists.** Elsewhere AI reaches the
process as a **connector bound to a plain task**, so the nine connector *documentation* pages are
UNCERTAIN with the binding quoted, never E2:
- records `001`–`009` — the nine AI connector pages (Anthropic, Azure, Cohere, DeepSeek, Gemini,
  Groq, Mistral, Ollama, OpenAI). Each page publishes the same `connector-process-flow` diagram: a
  task whose *label* is generic and whose AI identity lives in the surrounding page text and the
  connector's own definition (e.g. `anthropic-ask`). Delegated binding in its purest form, but
  documented in prose with no process file or diagram the reviewer can read the binding off — the
  cross-source question "AI in a process documented without a published diagram" is the researcher's
  to rule on once.
- records `010`–`011` — the two demo files in `bonitasoft/bonita-connector-ai`, read as XML:
  `AnthropicAIDemo-1.0.proc` and `AzureOpenAIDemo-1.0.proc`. The strongest evidence the source
  yields: the AI is a **connector definition on the service task**
  (`definitionId="anthropic-ask" event="ON_ENTER"`, with `userPrompt` "What is the capital of France?
  Answer with just the city name." and the output bound to `askResult`), and record 011 adds a user
  task "Review Results" after the AI step — the human review the protocol asks not to abstract away.
  **Both INCLUDE.**

**The two E1 findings that matter for the method.** The source publishes several diagrams that are
genuinely *not* BPMN, and the calibration pass turned four mechanical E0 rows into named-notation E1
rows rather than leaving them as "no artefact at all": a CI/CD pipeline (`bcd/latest/`), a radial
project concept map (`bonita-overview/project-structure`), a GraphQL Voyager schema graph
(`data/data-management`) and two Git branch diagrams (`ui-builder/git/resolve-merge-conflicts`). A
fifth, `labs/latest/bici/architecture`, is a deployment architecture diagram. All five verdicts were
E0/E1 exclusions either way — what changed is the ledger's claim about what is on the page.

**The nearest miss, and why it is UNCERTAIN.** Record `012` (the ofelia KYC article) publishes a
bpmn-js BPMN 2.0 diagram (the only site SVG carrying the `<!-- created with bpmn-js / http://bpmn.io
-->` provenance comment) whose tasks include "Verify identity" and "Check background", while the
page's prose puts **AI/ML document comparison inside that scrutiny** ("Artificial intelligence (AI)
and machine learning tools can analyze customer data and compare submitted documents—such as
passports or driver's licenses—against official databases"). Whether that AI element is *inside* the
process is exactly the boundary question the method reserves for the researcher. Its capture is
marginal (1400x152 of a 2492x270 canvas whose text is drawn as paths), so the row also carries
`needs_visual_check: true`.

**Corpus records (16), all in `corpus/bonitasoft/`:** two INCLUDE (the connector demo `.proc` files
`010`–`011`), nine AI connector pages (`001`–`009`, UNCERTAIN with the cross-source question), the
KYC bpmn-js diagram (`012`, UNCERTAIN, marginal capture, `needs_visual_check`), the Studio AI
Assistant illustration whose lanes are a vendor mockup, not BPMN (`013`), and three site artefacts
(`014` Ofelia workflow card, `015` Ofelia agent-runtime diagram — a Figma-style export with no
`<text>` nodes, `016` the AI BPMN generator promo). Records `013`–`016` are the site group: each was
captured, looked at and recorded rather than excluded, because the site's marketing material *is*
evidence.

**Limits and non-blockers, recorded in full at `sources/OPERATOR-TODO.md` §P4:** the unauthenticated
GitHub API's 60 req/hour limit (resolved — 53/53 repositories readable, 0 blocked); the 403 Webflow
lazy-load asset `placeholder.60f9b1840c.svg` on 22 site pages (inspected and explained — the real
figures of those pages were fetched, nothing is hidden behind it); 15 sampled SVG figures with no
decoder here (icons, logos and a gradient, judged by name); and one page whose entire content region
is an empty Antora `<article>` (`cloud/latest/Security`, quoted as such in its row).
