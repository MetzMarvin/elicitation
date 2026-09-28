# Pass 2 worker adapter (read after `02_source-census.md`, overrides it where they differ)

The prompts were written for the thesis-repo layout. The census runs in the standalone
folder `C:\Users\muffi\Desktop\Uni\Master_thesis\elicitation\`. Apply these mappings.

## Paths

| Prompt says | Use instead |
|---|---|
| `notes/elicitation/<x>` | `C:\Users\muffi\Desktop\Uni\Master_thesis\elicitation\<x>` |
| `notes/elicitation/ledgers/` | `elicitation\ledgers\` (exists, empty) |
| `notes/elicitation/corpus/<slug>/` | `elicitation\corpus\<slug>\` (create it) |
| `notes/elicitation/sources/OPERATOR-TODO.md` | `elicitation\sources\OPERATOR-TODO.md` (append at the end, under a `## Pass 2 blockers` heading) |
| `notes/uipath-promotion-pattern/analysis.md` | `C:\Users\muffi\Desktop\Uni\Master_thesis\master-thesis-prompt-injections\notes\uipath-promotion-pattern\analysis.md` (read only) |
| `prompts/00_shared-rules.md` | the rules are also in `elicitation\CLAUDE.md`; either copy is fine |

Never write into `master-thesis-prompt-injections\notes\elicitation\`: that is an older,
out-of-sync copy. Never open `sources\known-positives.md`, and exclude it from any listing.

The `record` paths inside ledger rows stay relative to `elicitation\`
(`corpus/<slug>/NNN_x.md`).

## Browser tools (chrome-devtools-mcp, `mcp__cdp1__*`)

- `evaluate_script` = DOM/JS extraction; `take_snapshot` = accessibility tree;
  `take_screenshot` (with `uid` for element, `fullPage` last resort);
  `list_network_requests` / `get_network_request` with `filePath` = save original assets and
  the page HTML.
- `navigate_page` can report a 10 s timeout although the page loaded. Always confirm with
  `take_snapshot` before treating a page as failed or `BLOCKED`.
- If `get_network_request filePath` cannot save a binary asset, fetch the asset URL
  (extracted from the DOM, never guessed) with `curl -L -o` in Bash.
- Max about one page load per second.
- Cookie banners: dismiss or reject non-essential. Never accept terms, never log in, never
  submit forms. A captcha or bot challenge is a `BLOCKED` row and an OPERATOR-TODO entry.
  Do not attempt it.

## Lessons from the pilot (flows-for-apex)

- `EXCLUDE` and `needs_visual_check: true` never go together. If you could not read the image,
  the verdict is `UNCERTAIN` with a full record. `tools/audit.py` flags the combination as a
  hard problem.
- Pages whose prose announces AI *inside* the process ("agentic AI directly into your
  workflow") are never `E2` on prose alone. Their diagrams are `INCLUDE`, `UNCERTAIN` or `E3`.
- The frontier file holds URLs only: no `#` comment lines. The surface breakdown goes in the
  header `note`.
- Corrections are appended as new rows with the same `n` and `"supersedes_row": true`.
  Never edit earlier lines; the audit takes the last row per `n`.
- The tooling check screenshot goes to `ledgers/<slug>.step0.png`, not into `corpus/`.
- Before reporting, run `python tools/audit.py <slug>`. It must print `problems: none`.
- **No selected subsets.** Every URL you enumerate on a host that belongs to the source gets a
  frontier line and a ledger row. That includes marketing hosts and pages without AI
  keywords. "Screened textually, not in the ledger" is keyword narrowing, even when
  disclosed. Scripted fetching is fine for the mechanical rows (`judged_from`); pages that
  mention AI get their images looked at.
- **"JS-rendered" and "plain GET got an interstitial" are not blockers.** Open the page in your
  browser tab; for catalogues, find the XHR/JSON endpoint via `list_network_requests`. It is
  `BLOCKED` only if a human would have to solve a challenge or log in.
- **Look at every candidate diagram yourself** (Read the PNG). "Evidence before eyeballs"
  means DOM evidence first, not *instead of* eyes. Leave `needs_visual_check: true` only
  when you looked and still could not tell. "Not opened" is never a reason for it.
- **If you cannot see images** (Read on a PNG returns nothing): OCR the figure (e.g. RapidOCR)
  and quote the labels as evidence. A figure with AI-ish OCR text, or with no legible OCR at
  all, is `UNCERTAIN` + `needs_visual_check`; never exclude it. List every such figure in
  `ledgers/<slug>.raw/visual-queue.json` as `{n, url, record, figure_path, ocr_text, question}`
  for the central visual pass.
- **Know the BPMN glyphs before reading a badge as "AI".** A lightning or zigzag in a circle on
  a task's edge is an **error boundary event**, not an agent marker. That misreading produced
  two false INCLUDEs in uipath-maestro-docs. A task counts as AI only through its label, a
  binding, a properties panel or vendor prose, never through an unexplained icon alone
  (icon-only means `UNCERTAIN` with a question).
- `judgment` convention for `E1`: a drawn non-BPMN diagram (state chart, box diagram,
  proprietary flow canvas) is `judgment: true`, because naming the notation is an
  interpretive call. A screenshot of a UI, table, form or code listing is `judgment: false`.
- `NNN_` in `corpus/<slug>/` is reserved for records. Raw evidence for excluded rows
  (e.g. `.bpmn` files without AI) goes to `ledgers/<slug>.raw/`.
- **Do not stop for context.** Your harness auto-compacts; keep working through it. After a
  compaction, re-read the tail of your ledger (and `visual-progress.jsonl` if you have one)
  plus your assignment file, then carry on. A `RESUME` stop "at 70 %" or similar is wrong.
- **No YouTube, no playback (operator, 2026-09-26).** Never open or fetch youtube.com / youtu.be
  links, and never play an embedded video or audio player: it blares on the researcher's
  speakers, and YouTube is not an accepted source. If a page autoplays media, mute and pause it
  first (`document.querySelectorAll('video,audio').forEach(m=>{m.muted=true;m.pause()})`).
  A video-only item is `UNCERTAIN` + `needs_visual_check`, judged on what the host page itself
  shows, with the note "artefact inside a video; not opened per operator instruction".
- IFS docs: assets and `resources/*.zip` need the bot-challenge cookie. Fetch them in-page
  with `fetch()` and base64, not with curl. Oracle blogs: curl gets a 403 from Akamai, so
  fetch everything in the browser.

## Reporting to the orchestrator

The orchestrator is the session `elicitation-5a`. When your source is finished, send it
the final report defined at the end of `02_source-census.md`
via SendMessage. Also send a short message straight away if tooling fails in Step 0 of the
census or if a blocker needs the human.

No git write commands, ever.
