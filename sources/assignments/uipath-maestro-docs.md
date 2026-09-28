---
source: uipath-maestro-docs
source_name: UiPath Maestro (product documentation)
source_type: vendor documentation
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: YES
  C2_native_bpmn20: YES
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES
access: public
population_type: enumerable
population_estimate: 60
effort: medium
needs_logged_in_browser: false
status: DONE (elicitation-74)
---

## Criteria evidence

- **C1 YES** — https://docs.uipath.com/maestro/automation-cloud/latest/user-guide/how-to-complex-process
  (2026-09-22, served in German): "Fügen Sie Agent als Anmerkung hinzu, um anzugeben, dass
  es sich um eine Agentenaufgabe handelt." ("Add Agent as an annotation to indicate that
  this is an agent task.") The same page walks the reader through creating a
  "Resolve Discrepancies Agent" with a system prompt and wiring it into the process.
- **C2 YES** — same page, image `alt` attribute: "BPMN-Diagramm des
  Rechnungsbearbeitungsprozesses"; page prose: "Dies ist das BPMN-Diagramm für den Prozess,
  den wir erstellen." The docs navigation carries a whole BPMN branch ("Grundlegendes zur
  BPMN-Modellierung von Maestro", "Leitfaden zu BPMN", "Ausrichten und Verbinden von
  BPMN-Elementen", "Einen komplexen BPMN-Prozess implementieren").
- **C3 YES** — page served anonymously; the "Anmelden" link is optional.
- **C4 YES** — see `uipath-marketplace.md` C4.

## Entry points

- `https://docs.uipath.com/maestro/automation-cloud/latest/user-guide/` — Maestro user
  guide root. The left navigation is the population: sections observed are EINLEITUNG,
  ERSTE SCHRITTE, ERSTELLEN MIT MAESTRO BPMN, ERSTELLEN MIT MAESTRO CASE, ERSTELLEN MIT
  MAESTRO FLOW, MAESTRO AUTOMATE, INTEGRATIONEN, BETRIEB, ÜBERWACHUNG, OPTIMIEREN,
  REFERENZINFORMATIONEN.
- The "ERSTELLEN MIT MAESTRO BPMN" branch is the dense part: "Grundlegendes zur
  BPMN-Implementierung von Maestro", "Einen einfachen BPMN-Prozess implementieren",
  "Einen komplexen BPMN-Prozess implementieren", "Häufige Implementierungsszenarien"
  (common implementation scenarios — likely several worked examples), "Debugging",
  "Simulieren", "Evaluations (Preview)", "Autopilot for Maestro (Vorschau)".
- Check for `https://docs.uipath.com/sitemap.xml` before paging the nav by hand.

## Enumeration instructions

1. Enumerate the **whole Maestro user guide nav tree**, not just the BPMN branch: Maestro
   Case and Maestro Flow pages also contain agent wiring, and the shared rules forbid
   narrowing by keyword.
2. "Häufige Implementierungsszenarien" (common implementation scenarios) is the highest
   yield sub-branch — expand it fully and put every scenario page on the frontier.
3. Record in the ledger header whether you enumerated from a sitemap or from the nav tree,
   and the exact nav root URL.

## Artefact mechanics

- Diagrams are static `.webp` images with descriptive German `alt` text (e.g.
  `maestro-process-diagram-599989-7f31b59a.webp`, alt "BPMN-Diagramm des
  Rechnungsbearbeitungsprozesses"). The `alt` text alone is good BPMN evidence.
- **Capture the `.webp` asset at its native URL.** Do not screenshot the rendered page.
- Element-level detail (which task is agent-bound) is carried in the surrounding prose and
  in screenshots of the properties panel, not in the diagram itself — same delegated-binding
  mechanic as the marketplace. Quote the prose.

## Known gotchas

- **Automatic German redirect.** `docs.uipath.com/maestro/...` redirected to
  `docs.uipath.com/de/maestro/...` from this location. Decide once whether the census runs
  on the `/de/` or the English tree and record it in the ledger header; do not mix.
  The page itself warns: "Es kann 1–2 Wochen dauern, bis die Lokalisierung neu
  veröffentlichter Inhalte verfügbar ist" — the German tree can lag the English one, which
  is a recall risk if you enumerate only in German.
- The docs shell is client-rendered; wait for the nav before extracting hrefs.
- There is a separate `academy.uipath.com` BPMN course. It is **not** part of this source;
  if it turns out to hold artefacts, it needs its own assignment file.

## Spot checks performed by Pass 1

Spot check only, not a verdict:

- https://docs.uipath.com/maestro/automation-cloud/latest/user-guide/how-to-complex-process
  — opened; BPMN diagram image with BPMN `alt` text present, agent creation walked through
  in prose, plus an error boundary event routing a failed agent task to a human.

## RESUME

(empty — census complete)

## Completion note (elicitation-74, 2026-09-25)

- **Ledger:** `notes/elicitation/ledgers/uipath-maestro-docs.jsonl` — 323 rows
  (= population_size), 10 INCLUDE, 6 UNCERTAIN, 307 EXCLUDE (E0 127, E1 73, E2 22,
  E3 85), 0 BLOCKED. Judgement exclusions 21 = 6.5 % (cap 10 %).
  `python tools/audit.py uipath-maestro-docs` → `problems: none`.
- **Records:** `corpus/uipath-maestro-docs/` — 16 records, 22 captures (21 figures at
  their native `.webp` URL, never a page screenshot, + 3 published `.bpmn` models).
- **How the population was settled.** The vendor sitemap for the product
  (`docs.uipath.com/products/maestro/sitemaps/en/sitemap.xml`) yields 317 urls: 222 on the
  Automation Cloud line, 95 on the Automation Suite 2.2510 line. Link-union closure added
  4 pages the sitemap omits and 2 closure-only urls that serve the Overview page.
  226 + 95 + 2 = 323. The **English tree** was enumerated (the German tree lags — the
  assignment's own recall warning); `/de/` is a translation, not a second population.
  Both publication lines were enumerated on purpose (over-inclusion): 80 of the 95 suite
  pages are byte-identical to their Cloud counterpart (E3 rows), 15 differ and were judged
  in their own right.
- **The agent marker.** A Maestro BPMN task bound to an agent carries a small **circular
  badge with a zigzag glyph** at the bottom edge of the card. It is distinct from the
  task-type icon (rounded square, top left: person = user task, gear = service task,
  envelope = send task) and from the marker glyphs (multi-instance/loop, bottom edge), and
  it is **not** the small blue square badge at the bottom right (that one sits on every
  executable card of the `subprocess` primer, including cards whose Action is unset).
  Verified against three tasks that are also agent-labelled in text: "Resolve
  discrepancies" (bracketed "Agent"), "Invoice Dispute Analysis (3rd Party AI Agent)",
  "Contact-Validation-Agent".
- **The six UNCERTAIN rows are one question.** `business-rule-task`, `receive-task`,
  `script-task`, `send-task`, `service-task`, `user-task` each publish a Studio Web
  properties-panel capture whose Action dropdown lists "Start and wait for agent" /
  "Start and wait for external agent", i.e. they document which implementations a BPMN
  task type can be bound to. If such a panel is an acceptable artefact they are INCLUDEs;
  if it fails E1 (not a process diagram) they are exclusions. The question is recorded
  verbatim in each record and ledger row.
- **Two artefacts are 2.2510-only and do not exist on the Cloud line:**
  `using-agents-in-maestro` (its Cloud url serves "Integrating systems and data" instead;
  the 2.2510 page states "Agents are represented in Maestro BPMN workflows as Service
  Tasks." and shows Action = "Start and wait for agent") and the `errors-and-recovery`
  diagram whose service task "Sync data" carries the agent marker. Both recorded.
- **One E3 across lines with different figures:** the 2.2510 `how-to-complex-process`
  revision publishes the same invoice-process diagram file
  (`maestro-process-diagram-599989`) as the Cloud revision; the surrounding figures differ,
  so it is recorded as a duplicate of the Cloud row, not as a second artefact.
- **Calibration basis for the mechanical E2 family** (BPMN figure, no agent badge, AI
  mention about the platform rather than an element): read at native resolution —
  `how-to-simple-process`, `understanding-process-implementation` (the page that shows
  user/service/send task icons side by side), `sequence-flows`, `subprocess`, `repetition`,
  `messages-and-updates`, `all-instances-view`/`all-incidents-view`. No task card in any of
  them carries an agent marker. Recorded in the ledger header so the criterion is auditable.
- **Not covered:** `academy.uipath.com` (separate property, needs its own assignment file)
  and the German tree (deliberate). Nothing was left BLOCKED; no login, captcha or paywall
  was met, and no vendor-side state was changed.
