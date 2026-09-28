# Shared rules for all elicitation agents (read in full before your first action)

These rules bind every agent working on Step 1 of the thesis method (Use-Case
Elicitation, `chapters/thesis/004_method.tex`, Section `sec:method:use_case_elicitation`).
They override your own judgement about what makes a "good" example.

## 1. What you are

You are a **collection instrument**, not a reviewer. A human researcher reviews every
item you surface, one by one, and throws out what does not belong. They cannot review what
you never surfaced.

Consequences you must internalise:

- A wrongly **included** item costs the researcher about 30 seconds.
- A wrongly **excluded** item is invisible, unrecoverable, and silently falsifies the
  method's claim that collection inside each source was *exhaustive*.

**Therefore: when in doubt, include. Always.** Being over-inclusive is the correct
behaviour here, not a failure mode. Do not try to hand in a clean list.

## 2. Three verdicts, no fourth

| Verdict | Meaning | What you do |
|---|---|---|
| `INCLUDE` | meets the artefact criteria | full record + evidence capture |
| `UNCERTAIN` | you hesitated, for any reason at all | full record + evidence capture, `needs_human_ruling: true` plus the exact question |
| `EXCLUDE` | fails a *sanctioned* criterion, with evidence | ledger row only, no record |
| `BLOCKED` | you could not reach or inspect it | ledger row + entry in `OPERATOR-TODO.md` |

`UNCERTAIN` is handled downstream exactly like `INCLUDE`. It is cheap. Use it freely.
Hesitation of any kind resolves to `UNCERTAIN`, never to `EXCLUDE`.

## 3. Sanctioned exclusion reasons: a closed list

An item may be excluded **only** under one of these codes, and only with verbatim
evidence quoted from the page:

- `E0-no-artefact` - the enumerated item contains no process artefact at all (pricing
  page, login form, empty listing, dead link, changelog entry). Mechanical, checkable.
- `E1-not-bpmn` - the artefact exists but is demonstrably **not** BPMN 2.0 notation
  (proprietary flowchart, architecture box diagram, UML, marketing illustration,
  screenshot of a chat UI). You must name what it is instead. If you cannot tell what
  notation it is, the verdict is `UNCERTAIN`, never `E1`.
- `E2-no-ai-element` - the BPMN artefact contains no AI/LLM element **inside the
  process** (the page's only AI mention is about AI generating the diagram, AI on the
  vendor's roadmap, or AI used for documentation). You must quote the AI mention you are
  dismissing and say what it refers to instead. If the AI mention is ambiguous, or an
  element's implementation might be AI-bound but is not visible, the verdict is
  `UNCERTAIN`, never `E2`.
- `E3-duplicate` - the **same diagram** is already recorded in this source's ledger
  (re-published identical image, one docs page under two URLs). You must name
  `duplicate_of`. Similar-but-different diagrams are not duplicates: include them. Never
  dedupe across sources, that is the reconciliation step's job.

Anything else is not an exclusion ground. If your reason does not fit one of these four
codes exactly, the verdict is `INCLUDE` or `UNCERTAIN`.

## 4. Banned reasons (each of these means: include it)

If you catch yourself writing or thinking any of the following, flip the verdict to
`INCLUDE` or `UNCERTAIN` immediately:

- "similar to one I already collected", "this pattern is already represented"
- "not a good / clean / interesting / illustrative example"
- "looks like marketing material" (marketing material *is* the evidence base here)
- "too simple", "trivial AI element", "only one AI task"
- "probably not a real BPMN diagram" (probably means `UNCERTAIN`)
- "low image quality", "diagram is cropped or only partially visible"
- "not in English", "German labels", "not enterprise-grade", "fictional company"
- "internal template / boilerplate listing" (a blank scaffold whose tasks can be AI-bound
  is a finding in its own right, see `notes/uipath-promotion-pattern/analysis.md`)
- "I have enough examples", "the cap is nearly reached", "diminishing returns"
- "running low on context or time" (context compacts automatically; keep going, see section 8)

The corpus cap of 60 and any notion of representativeness are the researcher's
instruments, applied after your work. They are not yours. Never truncate for them.

## 5. Evidence rule (anti-hallucination)

- Every ledger row and every record field must be grounded in a page you actually
  opened, with **at least one verbatim quote** (max 25 words) copied from that page.
- Never infer content from a URL slug, a search-result snippet, or a listing title.
- **Never guess a URL.** Navigate by extracting real links from catalogues or search
  results. A guessed URL that 404s wastes a step; a guessed URL that resolves to
  something else produces a fabricated record.
- You can see images, but a picture is the *weakest* evidence available and the most
  expensive to carry. Prefer textual and DOM evidence for "is it BPMN?", and use the
  screenshot to confirm rather than to discover:
  - a rendered `bpmn-js` canvas exposes `<svg>` nodes with classes `djs-element`,
    `djs-shape`, `djs-connection` and `data-element-id` attributes: strong evidence;
  - inline or downloadable `.bpmn` XML with `<bpmn:process>`, `<bpmn:serviceTask>`,
    `<bpmn:exclusiveGateway>`: decisive evidence;
  - figure captions, `alt` text, prose naming BPMN elements ("pool", "lane", "gateway",
    "service task", "ad-hoc sub-process"): good evidence;
  - element labels readable in the DOM of a live modeller: good evidence.
- If you looked at the image and are still not sure (too small, cut off, labels
  unreadable, notation ambiguous): **capture it, verdict `UNCERTAIN`,
  `needs_visual_check: true`**, and say what you could not resolve. Do not guess, and do
  not exclude.

## 6. Enumeration before judgement

Before judging a single item, establish the **population** and write it into the ledger
header. Collection is a census, so the population must be finite and enumerable:

- marketplace or catalogue with pagination: record total item count and page count;
- blog tag/archive index, docs section tree, `sitemap.xml`: record the index URLs;
- best case: the catalogue's own JSON/XHR endpoint seen in the network panel, which
  usually returns an exact total: record it.

Never treat "the first page of results", "top hits", or a relevance-ranked search-engine
list as a population.

Filters: do not narrow the population with keyword filters (`ai`, `agent`, ...) to save
effort. If you use a platform facet, you must *also* enumerate unfiltered and confirm
that no AI artefact sits outside the facet. Record that check.

## 7. Ledger discipline (append-only, written as you go)

One JSON object per line in `notes/elicitation/ledgers/<source-slug>.jsonl`, appended
**immediately after each item is judged**, never batched at the end. The ledger is your
state: a fresh agent must be able to resume from it alone. Schema and example:
`notes/elicitation/templates/ledger.md`.

Every enumerated item gets a row, including excluded ones. The ledger is what makes the
exhaustiveness claim auditable and lets the researcher review your *rejections*, which is
the only way a false negative can ever be caught.

## 8. Stopping

Exactly two legitimate stops:

1. the population is exhausted (ledger rows == `population_size`), or
2. the operator wrote `STOP` into your assignment file.

Nothing else. A full context window is **not** a stop: your harness compacts the
conversation automatically, and you keep working through it. Because the ledger is
written row by row (section 7), you lose nothing when that happens. After a compaction,
re-read the tail of your ledger and your assignment file before the next item. Never
stop, hand back or write a `RESUME` block pre-emptively because context is "getting
full". Write `RESUME` only if the session is actually being ended from outside.

## 9. Blockers: never silently skip

Login wall, free-account requirement, captcha, Cloudflare interstitial, paywall,
geo-block, rate limit, JS-only content you cannot read, a page needing a human click:

1. append a `BLOCKED` ledger row (not `EXCLUDE`);
2. append an entry to `notes/elicitation/sources/OPERATOR-TODO.md` with the exact URL,
   what is required (account? login? manual captcha?), what you already tried, and how
   many items sit behind the blocker;
3. continue with the rest of the population.

## 10. Conduct in vendor tools

- Read-only. Do not save, publish, deploy, download-to-account, rename or delete anything
  in a vendor editor or org. If you must change a property to reveal a binding, revert it
  and record that you did (precedent: `notes/uipath-promotion-pattern/analysis.md`).
- No auth bypass, no paywall circumvention, no credential entry unless the operator
  explicitly staged a session for you. Roughly one page load per second at most.
- Do not run `git commit`, `git add`, or any other git write command.
