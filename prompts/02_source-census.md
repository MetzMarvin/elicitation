# Pass 2 prompt: per-source census

Run **one agent per source**, each in its own Claude Code session (and its own browser
profile, see `notes/elicitation/SETUP.md`). Several can run in parallel. Paste everything
below the line, replacing `<SOURCE-SLUG>` with the assignment file's slug.

---

Your job is Pass 2 of Step 1 of a master thesis method: the **exhaustive census of one
source** for AI-enabled BPMN workflow artefacts. Your assigned source is
`<SOURCE-SLUG>`; its brief is `notes/elicitation/sources/assignments/<SOURCE-SLUG>.md`.

Exhaustiveness is the single most important property of your work. Not speed, not
precision, not a tidy result. The method claims that within each qualifying source every
published example was checked. You are what makes that claim true or false.

## Before you start (in order)

1. Read `notes/elicitation/prompts/00_shared-rules.md` in full. It defines your verdicts,
   the closed exclusion list, the banned reasons, the evidence rule, and your ledger.
2. Read your assignment file `notes/elicitation/sources/assignments/<SOURCE-SLUG>.md`,
   including any `RESUME` block at the bottom: if one is present, you are continuing an
   interrupted census. Read `notes/elicitation/ledgers/<SOURCE-SLUG>.jsonl` and resume at
   the next unjudged item instead of starting over.
3. Read `notes/elicitation/templates/record.md` and `notes/elicitation/templates/ledger.md`
   (your two output formats) and `notes/uipath-promotion-pattern/analysis.md` (the level of
   detail a record has to preserve). Do not read
   `notes/elicitation/sources/known-positives.md`: it would bias your enumeration.
4. Verify tooling: open the first entry point, extract page text, take one screenshot into
   `notes/elicitation/corpus/<SOURCE-SLUG>/`. If any of that fails, stop and report.

## Artefact-level inclusion criteria (from the method)

An artefact is collected if all three hold:

1. It is an actual BPMN diagram.
2. It contains an explicit AI/LLM element **as part of the process** (not AI used to
   generate the diagram, not AI mentioned in the surrounding marketing).
3. It is not a duplicate of an already-collected instance **from this source**.

Judge these under the rules of `00_shared-rules.md`: any hesitation becomes `UNCERTAIN`
with a full record, exclusions only under `E0`-`E3` with a verbatim quote.

Deliberately in scope, because the researcher wants them:

- diagrams where the AI element is only visible as a task *property* or implementation
  binding, not as a distinct BPMN element type;
- blank template diagrams whose tasks can be bound to an AI agent by the implementer
  (record what the binding options are, verdict `UNCERTAIN` if no task is AI-bound as
  shipped, and say so in the record);
- diagrams with an AI element *and* a guard, human review or filter in front of it (the
  mitigating element is exactly what must not be abstracted away later);
- the same pattern from many different pages inside your source: only a literally
  identical diagram is a duplicate;
- German or other non-English artefacts.

## Procedure

### Step A - establish the population (before judging anything)

1. Open each entry point in the assignment file.
2. Determine the finite population and how it is enumerated: catalogue pagination (record
   item count and page count), tag/archive index, docs section tree, `sitemap.xml`, or -
   best - the catalogue's own JSON/XHR endpoint with an exact total, which you can see in
   the network requests while paging.
3. Write the ledger **header line** with `population_size`, `enumeration_method`,
   `entry_points`, date, your model name, and the tool you drive the browser with.
4. If the assignment says `search-protocol` instead of `enumerable`, see Step E.
5. If your enumeration disagrees with the assignment's estimate by more than about 20
   percent, say so in the header `note` and trust your own enumeration.

Write the full list of enumerated item URLs into
`notes/elicitation/ledgers/<SOURCE-SLUG>.frontier.txt`, one per line, before judging.
That file is your worklist and the proof that you enumerated before selecting.

### Step B - judge every item in the frontier, in order

For each item, in this order, no skipping:

1. Open the item page (never judge from the listing text alone).
2. Look for the artefact and for BPMN evidence: rendered `bpmn-js` SVG
   (`djs-element`, `data-element-id`), inline or downloadable `.bpmn` XML, figure captions
   and `alt` text, prose naming BPMN elements, element labels in a live modeller.
3. Look for an AI element: task labels ("AI agent", "LLM", "agent", "copilot",
   "classify", "summarize", "extract"), task-type icons named in the DOM, task
   implementation properties / bindings, connector names, prompt text, model names
   (`gpt-*`, `claude-*`, `llama*`, `gemini*`), tool lists, ad-hoc sub-processes of tools.
   In platforms with delegated bindings (UiPath-style), an ordinary `serviceTask` may be
   AI-backed: check the task properties, not just the picture.
4. Decide the verdict under the shared rules.
5. `INCLUDE` / `UNCERTAIN`: capture evidence, then write the record (Step C).
6. Append the ledger row **now**, before moving on.

### Step C - evidence capture for every INCLUDE and UNCERTAIN

Into `notes/elicitation/corpus/<SOURCE-SLUG>/`:

**Capture quality is a hard requirement.** An earlier round of collection had to be
thrown away because the diagrams were captured as scaled-down page renders and the task
labels were unreadable. The abstraction step needs element labels, task-type icons and
implementation bindings to be legible. Capture in this order of preference, and record
which route you used in `capture_source`:

1. **`.bpmn` XML** if the page offers a download or exposes it in the DOM - lossless and
   worth more than any image.
2. **The original image asset at native resolution.** Read the `src` and the largest
   `srcset` candidate with `evaluate_script`, strip CDN resizing parameters
   (`?w=800`, `/resize/...`) where a larger original exists, then save the response body
   with `get_network_request` `filePath`, or fetch it with `curl` in Bash. Never
   re-screenshot an image you can download.
3. **Element screenshot** of a rendered `bpmn-js` canvas: enlarge the viewport, zoom the
   diagram until it fills it, then `take_screenshot` with the canvas `uid`.
4. **`fullPage` screenshot** only as a last resort.

Then verify what actually landed on disk before writing the record:

```bash
python -c "import struct,sys;d=open(sys.argv[1],'rb').read(24);print(struct.unpack('>II',d[16:24]))" <file>.png
```

Require **at least 1400 px width** for a diagram capture, and read the file back to
confirm the task labels are legible. If either check fails, re-capture at a larger
viewport or higher zoom. If it still fails, keep the best capture, set
`capture_quality: poor`, and say what is unreadable - never silently accept an unusable
image, and never exclude the item over it.

Files to write into `notes/elicitation/corpus/<SOURCE-SLUG>/`:

1. `NNN_<slug>.png` - the diagram capture that passed the checks above.
2. `NNN_<slug>.page.html` - an archive of the whole page, so the artefact survives the
   vendor editing the page later. Save the main document's response body via
   `get_network_request` with `filePath`. If that is impossible, add a `fullPage`
   screenshot instead and record `archive: fullpage-screenshot`.
3. `NNN_<slug>.bpmn` - the BPMN XML, whenever the page offers a download or exposes it in
   the DOM. This is the most valuable artefact of all: prefer it over anything else.
4. `NNN_<slug>.md` - the record, from `notes/elicitation/templates/record.md`.

`NNN` is a zero-padded per-source counter starting at `001`. Never renumber; the
reconciliation pass assigns corpus-wide numbers later.

The record's `observations` block is **verbatim description, not analysis**: what the page
literally shows about the AI activity's function, what it is wired to (downstream tasks,
data objects, gateways, human steps), and where its input comes from. Quote labels and
prompt text where visible. Do not classify the artefact into a pattern, do not name a
threat, do not rate anything: pattern derivation is the researcher's manual step and your
interpretation would contaminate it.

### Step D - self-audit before you report (mandatory)

1. Re-read every `EXCLUDE` row in your ledger.
2. For each, check: does it carry one of `E0`-`E3` *and* a verbatim quote that actually
   supports it? Is the reason on the banned list in section 4 of the shared rules?
   If either check fails, **flip it to `UNCERTAIN`**, go back, capture evidence, write the
   record.
3. Count `judgment_exclusions`: rows with `"judgment": true`. An `E2` on a page that
   contains no AI/LLM keyword at all is mechanical (`judgment: false`) and is expected to
   dominate a large catalogue. An `E2` on a page that *does* talk about AI, and an `E1` on
   a page that *does* show a diagram, are judgement calls. If judgement exclusions exceed
   10 percent of the population, you have been acting as a reviewer instead of a
   collector: re-examine all of them and flip the weaker half to `UNCERTAIN`.
   Regardless of the share, list every judgement exclusion in your final report.
4. Confirm ledger rows == `population_size` and that every `INCLUDE`/`UNCERTAIN` row has a
   record file and a capture on disk. Report any mismatch as an open gap.
5. Re-check every capture's pixel width. List every record with `capture_quality: poor` in
   your final report so the researcher can decide whether to re-capture by hand.

### Step E - `search-protocol` sources only

Where no index exists, a census is impossible, so document a search protocol instead of
faking exhaustiveness:

1. Build a query grid (topic terms x artefact terms x `site:` restriction) and log every
   query verbatim into the ledger header.
2. Screen **all** results per query down to a fixed depth (default: first 5 result pages),
   and judge every hit as in Step B. No relevance pruning.
3. Record saturation: queries that produced no new artefact.
4. Set `population_size: null` and `census: false` in the header, so the thesis can report
   this source honestly as search-based rather than enumerated.

## Hard rules recap

- Never stop because you think you have enough. Only exhaustion of the frontier or an
  operator `STOP`.
- Context filling up is not a stop: the harness auto-compacts. Keep going; after a
  compaction, re-read the ledger tail and the assignment file. Never exit early for context.
- Blocked: `BLOCKED` row plus an `OPERATOR-TODO.md` entry, then continue with the rest.
- Never guess URLs, never describe a page you did not open, never invent a quote.
- Read-only in vendor tools; revert anything you had to toggle; no git writes.

## Final report to the operator (in chat)

- `population_size`, items judged, `INCLUDE`, `UNCERTAIN`, `EXCLUDE` by code, `BLOCKED`.
- The judgement-exclusion share and how many verdicts your self-audit flipped.
- A table of collected artefacts: `NNN`, title, URL, one line on where the AI sits.
- Every `needs_human_ruling` question, verbatim.
- Open gaps: what you could not reach, what you are unsure you enumerated completely, and
  what the researcher should re-check by hand.
