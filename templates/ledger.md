# Ledger format: `notes/elicitation/ledgers/<source-slug>.jsonl`

Append-only JSON Lines. One object per line. Write the header line first, then exactly one
row per enumerated item, appended immediately after that item is judged.

## Header line (first line of the file)

```json
{"type":"header","source":"uipath-marketplace","source_name":"UiPath Marketplace (Maestro process templates)","census":true,"population_size":214,"enumeration_method":"catalogue XHR /api/listings?page=N&size=24 returns totalCount=214; 9 pages paged through","entry_points":["https://marketplace.uipath.com/listings?tag=maestro"],"access":"free-account","date_start":"2026-09-21","agent_model":"kimi-k2.7-code:cloud","browser_tool":"chrome-devtools-mcp --browser-url 127.0.0.1:9222","queries":[],"note":""}
```

For `search-protocol` sources: `"census":false`, `"population_size":null`, and every query
verbatim in `"queries"`.

## Item rows

```json
{"n":1,"url":"https://marketplace.uipath.com/listings/loan-processing1915","title":"Loan Processing","verdict":"UNCERTAIN","reason":null,"judgment":true,"evidence":"This agentic process is built with Maestro; every task ships Implementation Action: None","record":"corpus/uipath-marketplace/001_loan-processing.md","needs_visual_check":false,"needs_human_ruling":true,"question":"No task is AI-bound as shipped; does a bindable blank template count as an AI element?","accessed":"2026-09-21"}
{"n":2,"url":"https://marketplace.uipath.com/listings/quarterly-close-checklist","title":"Quarterly Close Checklist","verdict":"EXCLUDE","reason":"E2-no-ai-element","judgment":false,"evidence":"Tasks: Collect ledgers, Reconcile, Approve. No agent, connector or model reference on the page.","record":null,"needs_visual_check":false,"needs_human_ruling":false,"accessed":"2026-09-21"}
{"n":3,"url":"https://marketplace.uipath.com/listings/pricing","title":"Pricing","verdict":"EXCLUDE","reason":"E0-no-artefact","judgment":false,"evidence":"Compare plans and contact sales","record":null,"accessed":"2026-09-21"}
{"n":4,"url":"https://marketplace.uipath.com/listings/claims-triage-agent","title":"Claims Triage Agent","verdict":"BLOCKED","reason":null,"judgment":false,"evidence":"Sign in to view this listing","blocker":"listing requires an authenticated session; OPERATOR-TODO entry written","record":null,"accessed":"2026-09-21"}
```

## Field rules

- `n` - frontier index, matches the line number in `<source-slug>.frontier.txt`.
- `verdict` - `INCLUDE` | `UNCERTAIN` | `EXCLUDE` | `BLOCKED`. Nothing else.
- `reason` - only for `EXCLUDE`: `E0-no-artefact` | `E1-not-bpmn` | `E2-no-ai-element` |
  `E3-duplicate` (with `"duplicate_of":"<record>"`). Never a free-text reason.
- `judgment` - `true` if the verdict required interpretation, `false` if mechanical.
  Mechanical: `E0`, `E3`, and an `E2` on a page with no AI/LLM keyword anywhere.
  Judgement: every `UNCERTAIN`, every `E1` on a page that does show a diagram, and every
  `E2` on a page that does discuss AI. Drives the judgement-exclusion share in the
  self-audit and the researcher's false-negative review.
- `evidence` - verbatim quote from the page, max 25 words. Mandatory on every row.
- `record` - repo-relative path under `notes/elicitation/`, or `null`.
- `needs_visual_check` - `true` when the only BPMN evidence was an image you could not read.
- `needs_human_ruling` + `question` - whenever the researcher must decide.

## Closing line (optional, written at the end of a session)

```json
{"type":"footer","date_end":"2026-09-21","rows":214,"include":11,"uncertain":7,"exclude":{"E0-no-artefact":3,"E1-not-bpmn":6,"E2-no-ai-element":185,"E3-duplicate":1},"blocked":1,"judgment_exclusion_share":0.04,"self_audit_flips":4,"status":"COMPLETE"}
```

`status` is `COMPLETE` or `RESUME`. If `RESUME`, the assignment file must carry the resume
block. A large `E2-no-ai-element` count on a big catalogue is normal and mostly
mechanical; what must stay small is `judgment_exclusion_share`, because those are the
rows where a false negative can hide.
