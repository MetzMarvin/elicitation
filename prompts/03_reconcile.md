# Pass 3 prompt: reconciliation, cross-source dedup, corpus index

Run as **one agent** after the census agents have finished (or after a first wave of
them). It needs no browser, only the files on disk.

---

Your job is Pass 3 of Step 1: turn the per-source census output into one auditable corpus
and one review worklist for the researcher. You add no new artefacts and you visit no
websites; if something is missing, you report it as a gap.

## Before you start

Read `notes/elicitation/prompts/00_shared-rules.md`, then inventory:
`notes/elicitation/ledgers/*.jsonl`, `notes/elicitation/corpus/*/`,
`notes/elicitation/sources/assignments/*.md`, and
`notes/elicitation/sources/known-positives.md` (nine artefacts found by hand in a previous
round; their captures were discarded as unusable, the URLs are known good).

## Tasks

1. **Integrity check.** Per source: ledger rows vs `population_size`; every
   `INCLUDE`/`UNCERTAIN` row has a record file, a screenshot, and a resolvable source URL;
   every record has the required fields from `notes/elicitation/templates/record.md`; every
   `EXCLUDE` row has a sanctioned code and a quote; every `BLOCKED` row appears in
   `OPERATOR-TODO.md`. List violations per source, do not fix them silently.
2. **Cross-source duplicates.** Census agents were forbidden to dedupe across sources, so
   do it here. Two records are duplicates only if they show the *same diagram* (same
   image re-published, same docs page under two domains, vendor blog post syndicated to a
   partner site). Same pattern from two vendors is **not** a duplicate and both stay.
   Record duplicates as `duplicate_of:` in the later record and keep both files; deletion
   is the researcher's call.
3. **Seeded recall test.** For each of the nine URLs in `known-positives.md`, find the
   matching ledger row. Classify as `found-included`, `found-uncertain`,
   `found-excluded` (quote the exclusion reason), `not-enumerated` (the URL never entered
   the frontier), or `source-not-censused`. Report the result as a table: these are known
   positives, so every miss is measured recall loss, not a curiosity. Do **not** add a
   missed artefact to the corpus yourself - report it, and let the researcher decide
   whether to re-run that source.
4. **Corpus index.** Write `notes/elicitation/corpus/INDEX.md`: corpus-wide number, source,
   record path, capture path, source URL, access date, verdict, `capture_quality`,
   `needs_human_ruling`, one-line description.
5. **Source table for the thesis.** Write `notes/elicitation/corpus/SOURCE-TABLE.md`: one
   row per source with population size, enumeration method, census or search-protocol,
   items judged, contributed examples (`INCLUDE` + `UNCERTAIN`), exclusions by code, access
   tier, date range. This is the raw material for Section `sec:pattern_taxonomy:sources`
   and for the corpus-size discussion against the 60-example scope backstop.
6. **Review worklist.** Write `notes/elicitation/corpus/REVIEW-QUEUE.md`, ordered so the
   researcher's time goes where errors are most likely:
   1. every `needs_visual_check` record, and every `capture_quality: poor` record
      (the agent looked and could not resolve it, or could not capture it legibly),
   2. every `needs_human_ruling` record, with its question,
   3. every `E1-not-bpmn` and `E2-no-ai-element` exclusion, with its quote and URL - this
      is the false-negative review, the only place where an omission can still be caught,
   4. all remaining `INCLUDE` records for confirmation.
   Give counts per group up front so the researcher can budget the review.
7. **Recall diagnostics.** Per source and overall: judgement-exclusion share, verdicts
   flipped during the agents' self-audit (from their reports, if available), and sources
   where the exclusion pattern looks suspicious (e.g. a whole page of listings excluded
   under one code with near-identical quotes). Name them explicitly.

## Report

Corpus size (with and without `UNCERTAIN`), per-source contributions, the seeded recall
result (n found of nine, with every miss named), duplicate pairs found, integrity
violations, capture-quality failures, the review-queue counts, and the single source you
would re-run first if the researcher only had time for one.
