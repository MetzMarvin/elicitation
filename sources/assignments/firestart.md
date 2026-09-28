---
source: firestart
source_name: FireStart (AI Workflows use-case catalogue + AI blog)
source_type: vendor product site
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: YES
  C2_native_bpmn20: YES
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES (operator ruling 2026-09-24, general C4 rule)
access: public
population_type: enumerable
population_estimate: 113
effort: medium
needs_logged_in_browser: false
status: DONE (elicitation-3a, 2026-09-27 — census closed at 494 rows, `python tools/audit.py firestart` problems: none except the judgement-exclusion share, which is P14 in OPERATOR-TODO.md)
---

## Criteria evidence

- **C1 YES** — https://www.firestart.com/en/ai-workflows (2026-09-22): "AI-Powered Process
  Automation. Integrate AI seamlessly into your workflows. OCR, NLP, classification,
  summaries – all GDPR compliant and with human control." Named feature area with its own
  navigation entry ("AI Workflows"), its own use-case filter and its own blog tag.
- **C2 YES** — https://www.firestart.com/en/platform-overview (2026-09-22): "FireStart is
  built on BPMN 2.0 — the international ISO standard for business process modeling
  (ISO 19510)." The site logo's `alt` text is "FireStart BPMN 2.0 Workflow Automation
  Platform".
- **C3 YES** — all pages served anonymously; the only gates are HubSpot demo-booking links.
- **C4 UNCLEAR** — FireStart is an Austrian vendor positioned explicitly for the DACH
  mid-market ("made in Austria, hosted in the EU, built for DACH enterprises"). Named
  customers and an award banner are present ("1st Place – Toolmasters 2026 · Category:
  Process Automation"), but this is regional rather than dominant enterprise presence, and
  I am not authorised to settle "actively discussed" alone. **Question for the researcher
  is mirrored in `OPERATOR-TODO.md`.** Note that C4 is written to admit exactly this case:
  "a smaller vendor with a concrete worked example is in scope".

## Entry points

- `https://www.firestart.com/en/solutions?ai=1` — use-case catalogue with the AI facet
  applied; rendered "28 Use Cases gefunden" on 2026-09-22.
- `https://www.firestart.com/en/solutions` — the **unfiltered** catalogue. The platform
  page claims "See 65+ Use Cases", so the unfiltered population is larger than 28 and the
  facet cross-check of shared rules section 6 is mandatory here.
- `https://www.firestart.com/en/ai-blog` — curated AI blog index, 8 posts on 2026-09-22.
- `https://www.firestart.com/en/blog` — full blog index.
- `https://www.firestart.com/sitemap.xml` — 417 URLs, of which 85 are `/blog/` posts.
- `https://www.firestart.com/llms.txt` and `https://www.firestart.com/api/llm-pack` —
  machine-readable site digests, worth pulling as a cross-check on the sitemap.

## Enumeration instructions

1. **The sitemap does not contain the use-case pages.** Of 417 sitemap URLs, `0` matched
   `/use-cases/`. The use-case catalogue is client-rendered and its links only exist in the
   DOM after the filter component mounts. So the frontier is built from **two** sources:
   the sitemap (blog + static pages) **and** the DOM of `/en/solutions`.
2. Enumerate `/en/solutions` **unfiltered first**, capture every `/en/use-cases/<slug>`
   href, then apply `?ai=1` and confirm the 28 AI-flagged pages are a subset of the
   unfiltered set. Record that check in the ledger header. This is the facet cross-check.
3. Do not skip the 85 blog posts. Diagrams on this site are spread across product pages and
   blog posts.

## Artefact mechanics

- Individual use-case pages observed in Pass 1 are **prose only** — no diagram. Example:
  `/en/use-cases/vertragsanalyse-ki` contains problem/solution/KPI text and only the logo
  as an image. Expect a large, honest `E0-no-artefact` / `E2-no-ai-element` count here.
- Where diagrams do appear they are `.webp` image assets served from the site's own CDN
  with cache-busting filenames. Capture the original asset URL at native resolution.
- No `bpmn-js` canvas and no downloadable `.bpmn` were found on the public site in Pass 1.
  The evidence route is therefore image asset + prose.

## Known gotchas

- **The site may have been redesigned recently.** Diagrams that once sat on marketing pages
  may have moved. Enumerate the whole site structure, not just the AI-workflows page.
- **Mixed language.** Use-case slugs are German (`vertragsanalyse-ki`,
  `gefahrgut-klassifikation-ki`) while the page bodies are English on `/en/`. The catalogue
  even mixes UI strings ("28 Use Cases gefunden"). "Not in English" is a banned exclusion
  reason.
- The `?ai=1` facet is a query parameter on a client-rendered list; it does not change the
  path, so a naive href-based frontier will miss the distinction. Record the facet state.
- Cookie/consent: none blocked access from this location, but choose the
  most privacy-preserving option if one appears.

## Spot checks performed by Pass 1

Spot checks only, not verdicts:

- `/en/solutions?ai=1` — "28 Use Cases gefunden"; 28 `/en/use-cases/*-ki` hrefs extracted.
- `/en/use-cases/vertragsanalyse-ki` — opened; no BPMN diagram, no `djs-*` nodes, no "BPMN"
  string in the body.
- `/en/platform-overview` — opened; carries the BPMN 2.0 / ISO 19510 claim.
- `/en/ai-blog` — opened; 8 AI-tagged posts listed.

## RESUME

(empty)
