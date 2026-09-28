# Assignment format: one file per source, written by Pass 1, consumed by Pass 2

Path: `notes/elicitation/sources/assignments/<source-slug>.md`.

```markdown
---
source: uipath-marketplace
source_name: UiPath Marketplace (Maestro process templates)
source_type: vendor marketplace
provisional: false            # true if the source is UNCLEAR-NEEDS-RULING
criteria:
  C1_promotes_ai_in_bpmn: YES     # YES | NO | UNCLEAR, evidence below
  C2_native_bpmn20: YES
  C3_publicly_accessible: UNCLEAR
  C4_enterprise_presence: YES
access: free-account          # public | free-account | paid-trial | blocked
population_type: enumerable   # enumerable | search-protocol
population_estimate: 214
effort: large                 # small | medium | large
needs_logged_in_browser: true # if true, run this source serially in the attached browser
status: READY                 # READY | RUNNING | RESUME | COMPLETE | STOP
---

## Criteria evidence

One line per criterion: URL plus a verbatim quote supporting the verdict. For every
`UNCLEAR`, state the precise question the researcher must answer, and note that it is
mirrored in `OPERATOR-TODO.md`.

## Entry points

Concrete URLs the population is enumerated from, with the mechanism:

- `https://marketplace.uipath.com/listings?tag=maestro` - catalogue, 24 per page, 9 pages
- XHR `GET /api/listings?page=N&size=24` returns `totalCount` - preferred enumeration
- `https://marketplace.uipath.com/sitemap.xml` - cross-check for listings outside the tag

## Enumeration instructions

How Pass 2 should build the frontier, including which facets to avoid, and the
cross-check that proves no artefact sits outside a facet that was used.

## Artefact mechanics

Where the diagram lives and how to read it without vision: static PNG, rendered bpmn-js
canvas, downloadable `.bpmn`, live in-browser modeller (name the clicks needed to reach
the task-properties panel). Say which evidence route to prefer.

## Known gotchas

Cookie banners, bot walls, slugs that differ from titles, non-English pages, listings all
published under one internal account, editors that must not be saved, rate limits.

## Spot checks performed by Pass 1

One or two example items opened to verify the mechanics, with URLs. Explicitly marked as
spot checks, not verdicts: Pass 2 judges them again as part of the frontier.

## RESUME

Written by a Pass 2 agent that ran out of context. Next frontier index, pagination cursor,
open blockers, anything half-captured. Delete once the census is COMPLETE.
```
