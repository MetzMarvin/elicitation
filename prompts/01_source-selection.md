# Pass 1 prompt: source selection (vendor sampling)

Run this as **one single agent**, in one session, before any census agent starts.
Paste everything below the line into a fresh Claude Code session in the thesis repo.

---

Your job is Pass 1 of Step 1 of a master thesis method: **applying the vendor sampling
frame** that bounds which sources are surveyed for AI-enabled BPMN workflow examples.
You do **not** collect workflow examples in this pass. You decide *where* they will be
collected from, and you prepare the ground for the agents that do the collecting.

## Before you start (do these first, in order)

1. Read `notes/elicitation/prompts/00_shared-rules.md` in full. Those rules bind you,
   especially the evidence rule and the recall bias.
2. Read `chapters/thesis/004_method.tex`, Section `sec:method:vendor_sampling` (the four
   criteria) and Section `sec:method:stopping_rule` (what the census agents will do).
3. Read `notes/uipath-promotion-pattern/analysis.md` to see what these artefacts look
   like and how differently vendors promote them.
4. Read `notes/elicitation/templates/assignment.md` (the output format you must produce
   per qualifying source).
5. Confirm your browser tooling works: open one page, get its text, take one screenshot.
   If it does not work, stop and report; do not proceed blind.

## The four inclusion criteria (from the method; apply them exactly)

A vendor or source qualifies only if **all four** hold:

1. **C1 - promotes AI-in-BPMN publicly and prominently**, as a named feature, not as a
   hypothetical extension point. Vendor size is irrelevant: a small vendor with a
   concrete worked example is in, a large vendor with no public AI-in-BPMN story is out.
2. **C2 - native BPMN 2.0 notation**: the promoted artefact is an actual BPMN diagram,
   not a proprietary flowchart notation relabelled as a process.
3. **C3 - publicly accessible**: reachable without NDA, sales contact, or paid
   subscription, so an independent researcher can reproduce the sampling.
4. **C4 - dominant or actively discussed presence in the enterprise market**, established
   qualitatively (vendor-reported customer base, practitioner discourse, mentions in
   academic literature), not by a market-share number.

### How to apply them (this part is not negotiable)

Per criterion, record one of `YES` / `NO` / `UNCLEAR`, each with a URL and a verbatim
quote as evidence. Then:

- **Only C2 and C3 can produce a hard `OUT`**, and only on positive evidence:
  C2 `OUT` requires you to name the non-BPMN notation actually used; C3 `OUT` requires
  you to show the material is behind a paywall, sales gate, or NDA *with no public
  equivalent*.
- **C1 and C4 can never produce an `OUT` on their own.** They are judgement calls, and
  "prominent" and "actively discussed" are exactly the kind of judgement you are not
  authorised to make alone. If C1 or C4 is the only thing failing or unclear, the verdict
  is `UNCLEAR-NEEDS-RULING`, and the source still gets an assignment file marked
  `provisional: true`.
- **A free account requirement is not a C3 failure.** It is an access tier. Record it as
  `access: free-account` and raise it in `OPERATOR-TODO.md` for the researcher to rule on
  (precedent: UiPath's marketplace was used this way already). Paid trial that requires
  credit-card entry: `access: paid-trial`, also a ruling, not your decision.
- If a vendor fails C1 today but shipped an AI-in-BPMN *feature* you can see in its docs,
  that is a `YES` for C1 (documented named feature = promoted).

Three verdicts only: `QUALIFIES`, `UNCLEAR-NEEDS-RULING`, `OUT` (with code `C2` or `C3`
plus evidence).

## Discovery: be exhaustive about channels, not about vendors

You cannot enumerate "all vendors in the world". What you *can* do, and must do, is work
a fixed set of discovery channels to saturation and log it. Work **every** channel below,
and log each query you run (channel, query string, date, how many results you screened):

1. **Seed set already in the corpus** (verify each still qualifies, do not assume):
   Camunda, IBM watsonx Orchestrate, IBM BAMOE, IFS Cloud, Frends, UiPath (Maestro /
   Marketplace), FireStart.
2. **BPMN-engine and BPM-suite vendors** (check each for an AI-in-BPMN story; this list is
   a starting point, not a boundary): SAP Signavio, Bizagi, Appian, Pega, Flowable,
   ProcessMaker, Bonitasoft, Trisotech, GBTEC (BIC), Scheer PAS, Software AG ARIS,
   iGrafx, Newgen, Oracle, TIBCO, OpenText, Nintex, Kissflow, Creatio, AgilePoint,
   Comidor, Imixs, Operaton, Activiti, jBPM/Kogito, Modelio, Visual Paradigm, Cardanit,
   Miragon, Berger BPM. Add every additional vendor you encounter while searching.
3. **Search-engine sweeps** with an explicit query grid, e.g. the cross product of
   {`BPMN`} x {`AI agent`, `LLM`, `agentic`, `AI task`, `copilot`, `GenAI`} x
   {`tutorial`, `docs`, `blog`, `template`, `marketplace`, `example`}, plus
   `site:` variants for each vendor domain. Log every query.
4. **Marketplaces and template catalogues** (these are the richest census populations, so
   flag them prominently): UiPath Marketplace, Camunda Marketplace / community hub,
   Bizagi / Appian / Pega / ProcessMaker template galleries, SAP Business Accelerator Hub.
5. **Software directories** for vendors you have not seen yet: G2 and Capterra categories
   for "Business Process Management", "Workflow Automation", "BPMN tools".
6. **Practitioner and community channels**: Camunda forum and Discourse, vendor community
   blogs, consultancies (BP3, NTConsult, Miragon, Berner&Mattner-style integrators),
   Medium/LinkedIn articles, YouTube conference talks (CamundaCon, BPM conferences).
7. **Academic pointers**: papers on agentic BPM / LLMs in BPM that name concrete tools;
   follow their tool citations back to the vendor material.
8. **Competitor-page trick**: on each vendor site, open the "alternatives", "compare",
   or "vs" pages: they enumerate competitors you have not yet considered.

Stop a channel only when it stops producing vendor names you have not already logged
(saturation), and write that saturation statement into the report.

## Reconnaissance per candidate source (this is what makes Pass 2 possible)

For every `QUALIFIES` or `UNCLEAR-NEEDS-RULING` source, do a short recon pass and fill
`notes/elicitation/templates/assignment.md` into
`notes/elicitation/sources/assignments/<source-slug>.md`:

- **Entry points**: the concrete URLs from which the artefact population can be
  enumerated (marketplace catalogue with its pagination, blog tag index, docs section
  root, `sitemap.xml`).
- **Population type**: `enumerable` (a finite catalogue/index you can page through) or
  `search-protocol` (scattered artefacts with no index, e.g. a consultancy's blog with no
  usable archive). Prefer `enumerable`; use `search-protocol` only when you verified no
  index exists, and say what you checked.
- **Population size estimate** and how you got it (page count x items per page, an XHR
  `totalCount`, number of sitemap entries).
- **Access tier**: `public`, `free-account`, `paid-trial`, `blocked`.
- **Artefact mechanics**: where the diagrams live and how they can be read
  (static PNG in a blog post, rendered `bpmn-js` canvas, downloadable `.bpmn` XML, live
  in-browser modeller). Say which evidence route the census agent should use.
- **Known gotchas**: cookie banners, bot walls, URL slugs that differ from titles,
  German-language pages, listings published under one internal account, etc.
- **Estimated effort** (small / medium / large) so the researcher can parallelise.

Do not enumerate or judge artefacts yourself. One or two spot checks to confirm the
mechanics are enough, and mark them as spot checks.

## Outputs (write these files; create dirs as needed)

1. `notes/elicitation/sources/candidate-vendors.md`
   - A decision table, one row per candidate vendor/source ever considered, including
     the ones you ruled `OUT`: name, URL, C1..C4 verdicts, overall verdict, access tier,
     population type, size estimate, one-line evidence per criterion.
   - The `OUT` rows matter as much as the others: the thesis has to report the application
     of the sampling frame, and the researcher must be able to audit your rejections.
2. `notes/elicitation/sources/search-protocol.md`
   - Every channel worked, every query string, the search engine used, dates, how many
     results were screened per query, and the saturation statement per channel. This is
     the reproducibility record for the grey-literature search (the method cites
     Garousi et al.'s guidelines for exactly this).
3. `notes/elicitation/sources/assignments/<source-slug>.md`
   - One file per `QUALIFIES` / `UNCLEAR-NEEDS-RULING` source, from the template.
4. `notes/elicitation/sources/OPERATOR-TODO.md`
   - The researcher's action list, each item with: source, what is needed, exact URL, why
     it blocks, and what happens if it is skipped. Three groups:
     - **Access actions**: accounts to create, logins to perform in the automation browser
       profile, captchas to solve by hand.
     - **Rulings needed**: every `UNCLEAR-NEEDS-RULING` source with the precise question
       (e.g. "Is a free account still 'publicly accessible' under C3?"), your
       recommendation, and the consequence either way.
     - **Tooling gaps**: sources your browser tooling could not read at all and that will
       need the fallback browser.

Write files incrementally as you go, not in one burst at the end.

## Final report to the operator (in chat)

- Counts: candidates considered, `QUALIFIES`, `UNCLEAR-NEEDS-RULING`, `OUT` (by code).
- The assignment list with population-size estimates and a suggested parallelisation
  (which sources can run concurrently, which need the logged-in browser and must run
  serially).
- Total estimated artefact population across all sources, flagged against the thesis's
  60-example scope backstop, as information for the researcher, not as a reason to prune.
- The single biggest recall risk you are aware of in your own work: which channel you
  believe you worked least well, and what you would run next.
