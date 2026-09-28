---
source: frends-docs
source_name: Frends iPaaS (product documentation, Agentic AI section)
source_type: vendor documentation
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: YES
  C2_native_bpmn20: YES
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES (operator ruling 2026-09-24, general C4 rule)
access: public
population_type: enumerable
population_estimate: 976
effort: medium
needs_logged_in_browser: false
status: DONE (elicitation-3a, 2026-09-26; census complete - 942 rows == population 942, 13 INCLUDE
  records, one audit problem: the 15.7% judgement-exclusion share, reported not gamed - see OPERATOR-TODO P12)
---

## Criteria evidence

- **C1 YES** — https://docs.frends.com/frends-development/agentic-ai/intelligent-ai-connector
  (2026-09-22): "In Frends, AI can be included in the Processes natively using Intelligent
  AI Connector, automating tasks that have so far required human input." The docs carry a
  whole "Agentic AI" branch (Intelligent AI Connector, Model Context Protocol, Frends MCP,
  AI Assistance).
- **C2 YES** — same page: "BPMN 2.0 with AI Connector enables AI Orchestrations.
  Practically, you can implement the thought process of an employee as steps and
  decisions." An image on the page carries the `alt` text "Picture showing the Native AI
  shape as p[art of a process]".
- **C3 YES** — served anonymously on GitBook; no login, no paywall.
- **C4 UNCLEAR** — Frends is a Finnish iPaaS vendor with a real enterprise customer base in
  the Nordics and a Gartner-recognised iPaaS positioning, but it is not a dominant global
  BPM vendor and I cannot settle "actively discussed" from the vendor's own site.
  **Question mirrored in `OPERATOR-TODO.md`.** (Ruled YES at Gate 1, 2026-09-24.)

## Entry points

- **`https://docs.frends.com/llms.txt`** — the strongest entry point: a machine-readable
  index of the entire documentation set, 135 604 characters / 976 lines, one markdown
  bullet per page with URL and description, e.g.
  `- [Welcome](https://docs.frends.com/readme.md)`. The docs footer itself points at it:
  "For the complete documentation index, see llms.txt."
- `https://docs.frends.com/frends-development/agentic-ai/` — the Agentic AI branch root
  (Intelligent AI Connector, Model Context Protocol, Frends MCP, AI Assistance).
- Every page is also available as raw markdown by appending `.md` to its path — this is
  how `llms.txt` addresses them, and it is the cheapest possible read for Pass 2.

## Enumeration instructions

1. Frontier = every URL in `llms.txt`. Parse it, write the frontier file, record
   `enumeration_method` as "llms.txt index, 976 lines, parsed 2026-09-22".
2. The 976 lines include non-page lines (headings, blank lines); count the actual
   `- [title](url)` bullets and use **that** as `population_size`, not 976.
3. Do **not** restrict to the `agentic-ai/` branch. AI elements appear in Process examples,
   Task documentation and release notes as well. Enumerate the whole docs set — this is
   cheap here because of the `.md` endpoints.
4. Release notes carry version-specific AI features; include them.

## Artefact mechanics

- Frends renders process diagrams as images served through GitBook's image proxy
  (`.../image?url=https%3A%2F%2F421307484-files.gitbook.io%2F...`). **The real asset URL is
  inside the `url` query parameter** — decode it and fetch the original, rather than
  capturing the proxied/resized version. This is precisely the "scaled re-render" trap that
  destroyed the July 2026 captures.
- `alt` text on content images is descriptive and usable as evidence ("Picture showing the
  Native AI shape as part of a Process").
- Prefer the `.md` version of a page for text evidence: it gives you the figure references
  and prose without the GitBook shell.
- No downloadable `.bpmn` and no `bpmn-js` canvas were found on the public docs.

## Known gotchas

- GitBook's image proxy (see above) — decode `?url=` or you capture a resized copy.
- The docs are versioned in the header ("Frends 6.3.0"). Record the version you enumerated.
- Frends calls its BPMN diagrams "Processes" and its AI element an "Intelligent AI
  Connector" / "Native AI shape", not a "service task". Prose evidence will not contain the
  word "serviceTask"; look for the shape names the vendor actually uses.
- There is an "Ask Docs" AI search box on every page. It is a documentation-search
  assistant, i.e. an AI mention that is **not** an AI element inside a process. Under the
  shared rules that is an `E2` you must quote and dismiss explicitly, not a reason to
  include a page.

## Spot checks performed by Pass 1

Spot checks only, not verdicts:

- `/frends-development/agentic-ai/intelligent-ai-connector` — opened; carries both the C1
  and the C2 quote, plus the "Native AI shape" image.
- `https://docs.frends.com/llms.txt` — fetched, HTTP 200, 135 604 chars, 976 lines.

## RESUME

(empty - census closed 2026-09-26, see the DONE block below.)

---

## DONE (elicitation-3a, 2026-09-26)

**Ledger** `ledgers/frends-docs.jsonl` + `ledgers/frends-docs.frontier.txt` (942 frontier lines,
one row each). **Audit:** `python tools/audit.py frends-docs` ->
`population 942, census=True, rows=942; EXCLUDE=929, INCLUDE=13; E0=539, E1=7, E2=141, E3=242;
judgement exclusions 148 (15.7%); visual-check=0, rulings=1, blocked=0; problems: 1`.

### Population - the assignment's 976 is not the population; 942 is

`population_estimate: 976` above is the **line count** of `llms.txt`, which the assignment itself
warns not to use as `population_size` (instruction 2). The actual census:

- `https://docs.frends.com/sitemap.xml` is a **sitemap index** of 11 child sitemaps whose union is
  **933** URLs. Independently, `llms-full.txt` declares the same total for itself: pages 1-100 of
  933. Two enumerations, one number.
- `llms.txt` carries **807** of those URLs plus **9** section-root URLs that appear in no sitemap
  (the `/docs/frends-6.1.0/welcome` and `/reference/frends-6.1.0/reference` style roots), so the
  frontier is 933 + 9 = **942** and every line was fetched and judged.
- Currency: the unversioned pages are the **6.3.0** documentation; every `/docs/frends-6.x.y/` URL
  is an archive copy of a current page and is E3-duplicate of it (242 rows).

### The 13 INCLUDE records (`corpus/frends-docs/`, one per row)

`001_agentic-ai-native-ai-task-in-a-bpmn-process` (n=2) -
`002_intelligent-ai-connector-shape-in-a-bpmn-process` (n=4) -
`003_model-context-protocol` (n=5) - `004_semi-deterministic-ai-process` (n=203) -
`005_simple-rag` (n=205) - `006_azure-ai-inference` (n=208) - `007_on-premise-ollama` (n=209) -
`008_multipart-file-to-ai` (n=228) - `009_expressions-to-ai-connector` (n=239) -
`010_activity-shapes` (n=321) - `011_ai-connector-shape` (n=322) - `012_mcp-trigger` (n=360,
+`needs_human_ruling`) - `013_openai-task` (n=804). Every record carries at least one figure
capture (`capture_quality: legible` throughout) and quotes both its BPMN and its AI evidence.

**One question for the researcher, verbatim on the row (n=360, MCP Trigger):** *the MCP Trigger is
an AI-facing interface shape at the start of the Process rather than an AI task inside the flow -
does it count as an AI element inside the process for the corpus?* It is kept as INCLUDE because
the trigger is a shape in the process diagram and the page states it exists so that AI agents and
LLMs can call the Process.

### BPMN evidence - the assignment's "no bpmn-js canvas was found" is wrong

The assignment's Artefact mechanics say "No downloadable `.bpmn` and no `bpmn-js` canvas were found
on the public docs." **Both are wrong**, and this is the source's most useful discovery:

- 123 of the task-library diagrams are **bpmn-js exports**: the file itself begins
  `<!-- created with bpmn-js / http://bpmn.io -->` and carries `data-element-id` attributes. The
  notation of those pages is settled by the asset, not by a caption.
- Their text labels were read one by one (all 123). Exactly **one** carries an AI label: n=804
  `chat-gpt.svg` ("Call ChatGPT with customer prompt"). That is record 013 - the smallest complete
  AI-in-BPMN example in the source, and it was found by scanning assets, not by trusting prose.
- The Process Editor canvas itself is BPMN 2.0 by the vendor's own statement: "Process Editor uses
  BPMN 2.0 and C# to create integration flows."
- GitBook serves every page as a `.md` twin and every figure as a native asset URL; the
  `image?url=` proxy the assignment warns about was bypassed by reading the markdown twin rather
  than the rendered page.

### Dedupe method (E3)

By **content**, not by URL: the versioned docs live in a different GitBook space, so the same
diagram re-published under 6.1.0/6.2.0 has a different asset URL and a byte-identical file. md5
identity decides E3; where the archive copy's figures were not re-served, the claim falls back to
same-path-under-a-version-root. Three rows (n=93, 147, 148) were re-coded from `E1` to
`E3-duplicate` late, after fixing a guard that had skipped the duplicate check for chat-classed
pages under a version root.

### Why the 15.7% judgement share is high, and what was done about it

This is the manual of a BPMN 2.0 tool: 141 pages show a genuine Process Editor diagram with no AI
element in it (E2, `judgment: true`) and 7 show a non-BPMN artefact (E1). The ceiling was reported,
not gamed (OPERATOR-TODO **P12**, including the ruling options). To make false negatives visible
rather than assume there were none, every judged-excluded page carrying AI vocabulary (24 pages)
was listed, its AI sentence read, and its figures opened:

- **Two near-misses promoted to INCLUDE:** n=203 and n=239, whose AI shapes sit under captions
  that never say "AI". A text-only pass would have lost both.
- **One reason corrected:** n=40, from E2 to E0 (no figure on the page is a process diagram).
- **The rest dismissed in writing**, each row quoting the AI mention and naming what it refers to
  (the AI Code Assistant, the AI Documentation Assistant, "AI & ML" as a connector-category
  heading, or the English words "prompted"/"prompt" and the substrings inside "WAITING" and
  "embedding").

### Known gap

`https://docs.frends.com/bap/general/single-sign-on` publishes its only figure as
`src="broken://files/oH85GMcOLRjv7m4KGNcN"`, a GitBook placeholder for an asset that no longer
resolves, so the break is upstream of any client. Its row is E0 on the caption ("Entra ID app
registration view.", application chrome) and is named in OPERATOR-TODO P12. It is the one row of
942 that rests on a caption rather than on a figure that was looked at.

