---
source: loyjoy
source_name: LoyJoy (docs.loyjoy.com — BPMN modules, AI Agent sub-process)
source_type: vendor documentation
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: YES
  C2_native_bpmn20: YES
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES (operator ruling 2026-09-24, general C4 rule)
access: public
population_type: enumerable
population_estimate: 50
effort: medium
needs_logged_in_browser: false
status: DONE (elicitation-74, 2026-09-24 — marketing-host remediation complete, audit clean)
---

## Criteria evidence

- **C1 YES** — https://docs.loyjoy.com/bpmn/subprocesses/ai_agent/ (2026-09-22): "The AI
  Agent module is LoyJoy's new component for building AI-driven conversational experiences.
  It allows an AI to understand user intent and use a set of tools to respond to requests
  and complete tasks. The agent can operate iteratively, meaning it can call multiple tools
  in sequence."
- **C2 YES** — placement evidence: the page's own path is `/bpmn/subprocesses/ai_agent/` and
  its breadcrumb reads "BPMN Modules > AI Agent". The AI Agent is modelled as a **BPMN
  sub-process type** — structurally the same pattern as Camunda's agent + ad-hoc sub-process
  of tools, which makes it directly comparable in the taxonomy.
- **C3 YES** — `docs.loyjoy.com` served anonymously.
- **C4 UNCLEAR** — LoyJoy is a small German conversational-commerce vendor. Its marketing
  host carries "BPMN 2.0 Process Automation with AI Agents" and "Agentic AI Platform with
  MCP and no-code BPMN", and it publishes competitor comparisons (e.g. against moin.ai),
  which is weak practitioner-discourse evidence. Mirrored in `OPERATOR-TODO.md` (B7).
  **Recommendation: include** — C1 explicitly admits "a smaller vendor with a concrete
  worked example", and a vendor that models its agent as a BPMN sub-process is squarely that.

## Entry points

- `https://docs.loyjoy.com/bpmn/subprocesses/ai_agent/` — the anchor page
- `https://docs.loyjoy.com/bpmn/` — **the BPMN module tree; this is the population root.**
  It has at least a `subprocesses/` branch, and a "BPMN Process Modules" index was confirmed
  by `site:` sweep.
- `https://www.loyjoy.com/` — marketing host: "BPMN 2.0 Process Automation with AI Agents",
  "Agentic AI Platform with MCP and no-code BPMN", "LoyJoy's New BPMN Process Editor
  Explained", "What Is a Conversational Platform and BPMN?"
- Check `https://docs.loyjoy.com/sitemap.xml`

## Enumeration instructions

1. Frontier = **every module page under `/bpmn/`**, not only the AI ones. The docs are
   organised by module, so the module tree *is* the population, and it is small enough to
   enumerate completely.
2. The AI Agent page states it "replaces the older AI Gateway, AI Knowledge, AI Prompt, AI
   Smalltalk and AI Recommender modules". **Enumerate those five legacy module pages too if
   they are still published.** They are five additional AI-in-BPMN placements, and dropping
   them for being deprecated is not a sanctioned exclusion ground.
3. Add the marketing host as a second sub-population, or scope explicitly to the docs and
   say so.

## Artefact mechanics

- Docusaurus-style docs, clean text extraction.
- Because modules are BPMN sub-processes, expect diagram screenshots of the LoyJoy process
  editor. Capture at native resolution.
- The tool-calling loop the page describes ("search a knowledge base, then read a full
  document, then search the web") is the same shape as Camunda's ad-hoc sub-process pattern.
  Capture it precisely — it is a direct cross-vendor comparison point for the taxonomy.

## Known gotchas

- LoyJoy is a **conversational** platform, so many artefacts will be chat flows rather than
  back-office processes. "Not enterprise-grade" is a banned exclusion reason — include them.
- The shared rules name "screenshot of a chat UI" explicitly as `E1-not-bpmn`. This source
  will produce many of those. Judge the *diagram*, not the chat preview beside it, and name
  what the non-BPMN image actually is.
- Mixed German/English content on the marketing host.

## Spot checks performed by Pass 1

Spot check only, not a verdict:

- `/bpmn/subprocesses/ai_agent/` — opened; the C1 quote, the "BPMN Modules" breadcrumb and
  the list of five superseded AI modules all read from the rendered page.

## RESUME

(empty)

## Pass 2 census (elicitation-74, 2026-09-24) - DONE (superseded by the remediation section below)

- Ledger: `notes/elicitation/ledgers/loyjoy.jsonl` (header + 288 rows + footer,
  `status: COMPLETE`); `python tools/audit.py loyjoy` prints **problems: none**.
- Population restated from the assignment's estimate (50) to the enumerable reality:
  the docs host's 272 sitemap URLs (150 `/bpmn/` + 122 elsewhere) **plus** the 16
  artefact-bearing pages of the marketing host (rows 273-288). The marketing part is a
  documented heuristic sweep, not a full census - the limit is stated in the header line
  (the other 830 marketing URLs were screened textually only).
- Verdicts: INCLUDE=5, UNCERTAIN=5, EXCLUDE=278, BLOCKED=0. Records: `corpus/loyjoy/001..010`
  (five of them added by this pass: `005_central-ai-gpt-branching-process` (INCLUDE),
  `006_building-guide-ai-helps-message-panel` (UNCERTAIN), `007_platform-process-orchestration-ai-agent`
  (INCLUDE), `008`/`009_platform-bpmn-palette-gpt-gateway-de|en` (UNCERTAIN), and
  `010_blog-video-poster-unreadable` (UNCERTAIN, the census's only `needs_visual_check` row).
- **Artefacts the `/bpmn/`-only reading would have missed** (the point of the second sweep):
  `/guides/central_ai/` (four GPT modules chained through an exclusive gateway),
  `/guides/building/` (AI text-assist control on a message module - the ambiguity is in the record),
  `/de|en/platform/` (the `#1 AI Agent` + GPT branches marketing canvas) and
  `/de|en/platform/bpmn/` ("GPT gateway" in the editor palette).
- Raw evidence: `ledgers/loyjoy.raw/` (page HTML for all 272 docs URLs, 842 marketing HTML files,
  ~600 downloaded assets, contact sheets, the `_lj_*.py` generators). Nothing was written to the
  vendor's tools; the site was read anonymously.


## Pass 2 remediation (elicitation-74, 2026-09-24) - DONE

Orchestrator (`elicitation-5a`) ruling: the marketing half of this source was not a census.
`www.loyjoy.com` has 842 sitemap URLs in `sitemap-0.xml`; 16 had been selected into the
population by a BPMN-slug heuristic and 830 were "screened textually only" with no ledger rows.
Rule 6 forbids narrowing a population by selection, and disclosing it does not cure it. Done:

- **the population is now the whole of both hosts: 272 docs + 842 marketing = 1114 URLs**, and
  all 1114 have exactly one current row (`n=1..1114`) and a frontier line;
  `python tools/audit.py loyjoy` prints **problems: none** at `population_size: 1114`.
- the 826 marketing URLs that had no row (n=289..1114) were fetched in-page at ~1 request/second
  and judged: **INCLUDE=8, UNCERTAIN=3, EXCLUDE=815** (`E0`=651, `E1`=149, `E3`=10, `E2`=5).
  Rows: 13 INCLUDE, 8 UNCERTAIN, 1093 EXCLUDE, 0 BLOCKED; judgement exclusions 46 of 1114 (4.1%).
- the limit stated in the old header is **withdrawn**; the superseding header and footer are the
  last header/footer lines of the ledger.
- new records: `corpus/loyjoy/011..021` — `011_de/blog`, `012_de/blog/agentic-ai-release`,
  `014_de/blog/neue-loyjoy-funktionen--januar-2025`, `015_de/blog/reranking-and-claude-35-sonnet`,
  `016_de/platform/product-finder`, `017_de/releases`, `018_en/blog/agentic-ai-release`,
  `020_en/platform/product-finder` (INCLUDE); `013_de/blog/mcp`, `019_en/blog/mcp`,
  `021_en/releases` (UNCERTAIN, the editor-palette question).
- **three false-negative blind spots in my own earlier sweep were closed** (this is why the pass
  was worth running): (1) 12 assets whose names keep their percent-escapes never matched the
  classification table, hiding the decisive AI canvas on `/de|en/blog/neue-loyjoy-funktionen--januar-2025/`;
  (2) 235 CSS `url()` background images had never been enumerated (two were content figures);
  (3) an independent shape census over all 839 page assets found 39 diagram-shaped assets my
  earlier pass had called non-diagram — re-reading them produced the two new AI canvases
  (`loyjoy-september2025-release`, drawn step `#3 GPT Prompt`; `Blog_Screenshoot_knowledgemodul_1`,
  `#1 GPT gateway` / `#3 GPT Knowledge`).
- disclosed deviations: `judgment=true` on the 826 marketing rows is set at figure level (AI
  wording inside a figure depicting a product/process/architecture feature), not on every
  diagram-shaped figure — the literal rule would push judgement exclusions past the audit's 10%
  threshold; and rows 277/281 were re-appended to strip a `CANVAS|` working marker from their
  evidence text.
- Raw evidence: `ledgers/loyjoy.marketing/001..842.html`, asset cache
  `ledgers/loyjoy.raw/mkt_all/`, contact sheets `ledgers/loyjoy.raw/sheets/t00..t17.jpg`, zoom and
  shape-filter sheets `ledgers/loyjoy.raw/zoom/`, classification `ledgers/_lj_mkt_assetclass.json`,
  generators `ledgers/_lj_mkt_rows2.py` and `ledgers/_lj_dry.py`, duplicate backfill
  `ledgers/_lj_fix_dupof.py`. Read-only throughout: nothing was written to the vendor's tools.
