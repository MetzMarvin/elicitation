---
source: citeck-ecos
source_name: Citeck ECOS (citeck-ecos.readthedocs.io)
source_type: vendor documentation
provisional: false
criteria:
  C1_promotes_ai_in_bpmn: YES (thin)
  C2_native_bpmn20: YES (thin)
  C3_publicly_accessible: YES
  C4_enterprise_presence: YES (operator ruling 2026-09-24, general C4 rule)
access: public
population_type: enumerable
population_estimate: 10
effort: small
needs_logged_in_browser: false
status: DONE (elicitation-3a, 2026-09-25; census + 765-figure visual backstop complete, audit clean)
---

## Criteria evidence

- **C1/C2 (thin)**: https://citeck-ecos.readthedocs.io/en/latest/general/AI_instruments/user_agents.html
  (2026-09-24): custom AI agents are "Used in BPMN processes via POST
  /api/ai-agent/execute". That is the only sentence tying the agents to BPMN.
- **C4 UNCLEAR**: a small Alfresco/Flowable integrator with its own platform.

## Entry points

The `AI_instruments/` section of the Read the Docs tree (enumerate from the nav), and
`github.com/Citeck/ecos-demo-app`.

## RESUME

(empty)

## Result

Census complete 2026-09-24 (elicitation-3a). Population 994 = 993 docs URLs
(395 en @ /en/latest/ + 598 ru union across 17 distinct builds, judged at the newest
build containing each) + 1 repository item. Rows 994; `tools/audit.py citeck-ecos`
prints `problems: none`.

- INCLUDE 1 — `corpus/citeck-ecos/001_en_ecos_bpmn_components_ai_task.md`
  (AI Task reference page; two downloadable `.bpmn` files carrying `aiTask`,
  `aiUserInput`, `aiPreprocessingScript`, `aiPostprocessingScript`,
  `aiAddDocumentToContext`, `aiSaveResultToDocument`, `aiResponse`).
- UNCERTAIN 1 — `corpus/citeck-ecos/002_en_ecos_bpmn_components.md`
  (needs_human_ruling; question recorded in the ledger row's `question` field: the
  element legend lists an AI-bound task type but the page's own diagram is not
  visible at legible resolution).
- EXCLUDE 992 — E0 916 / E2 67 / E1 7 / E3 2; judgement exclusions 14 (1.4 %).
- BLOCKED 0.

Open gaps recorded in the ledger header note: Read the Docs answered HTTP 429 to the
later figure bursts, so ~535 supporting figures of non-AI pages were not fetched (the
E2/E1 rows there rest on page heading + text); the ru `develop` build's `_images/` URLs
404. Not a blocker for judgement — the decisive `.bpmn` XML channel is complete (6 pages,
4 files) and the page-text channel is complete for all 993 URLs.

## Result, DELTA 1 — figure backstop closed (elicitation-3a, 2026-09-25)

The HTTP-429 gap above is now **closed**: all **765 raw figures of 116 pages** were
downloaded and viewed as 64 contact sheets with a per-tile sidecar, every process-shaped or
unreadable tile re-read at native size. `tools/audit.py citeck-ecos` -> `problems: none`;
`population 994, rows 994 (+5 superseded rows)`, `EXCLUDE 987, INCLUDE 1, UNCERTAIN 6`,
`E0 914 / E2 64 / E1 7 / E3 2`, `judgement exclusions 14 (1.4%)`,
`review queue: visual-check=5 rulings=1`.

- **The backstop confirmed the census's central find rather than adding to it.** The Citeck
  AI Task is a first-class BPMN element in the platform's palette, drawn as a rounded
  rectangle with a four-point sparkle type marker and the label "AI Task", shown
  end-to-end in two processes ("Комментарий сравнение версий", "Генерация текста КП") and
  documented by its own properties panel ("Запрос к AI", "Постобработка", ID
  Activity_1o76vd3). Already recorded at rows 348 (INCLUDE, record 001) and 368
  (UNCERTAIN, record 002), with the RU mirror rows 940/960 as `E3-duplicate`. **No new
  record was needed**; no other figure in the source holds an AI-labelled element inside a
  diagram.
- Two figure families that look like process models are not, and are recorded in the header
  note: the Architecture-page box-and-arrow schematics (rows 622, 985, 387, 110) and the
  DMN decision tables (948_process_04, 356_process_04). The AI-agent / RAG screenshots
  (rows 525, 531, 638, 940 panel shots) are configuration UI, not process models.
- **Five rows superseded to `UNCERTAIN` + `needs_visual_check`** (new records 003-007,
  captures in `corpus/citeck-ecos/`), because rule 5 makes an unresolved image an UNCERTAIN
  and never an exclusion: row 185 (`185_bp3.png`, lane BPMN board 1709x3000),
  row 738 (`738_194.png`, a 3000x241 cropped BPMN fragment), row 740 (`740_bp_scheme.png`,
  BPMN board 3000x1213 with collapsed sub-processes), row 930 (`930_adm_31.png`, a "Схема"
  BPMN panel on a dashboard page the census had called E0 — that code is wrong whatever the
  labels say), row 957 (`957_bpmn_start_event_example.png`). Every one is a readability
  limit at the asset's own resolution, not a notation question; each row's `question` field
  names the file and says what to check.
- Residual doubt left standing (listed in the header note, not flipped, because the tiles
  *were* looked at and showed no AI label at sheet scale): 946_bpmn_notification_example_
  process.png, 948_59/60/61/62, 948_sample_011, the 956/957 start-event and sub-process
  example figures, 889_History_3.png, 743_desk_8/9.png, 744_tasks_1.png.
- Method note carried into the ledger: within a multi-image read the images can return in a
  different order than they were requested, so every decisive claim was re-read one file per
  call with FILE names taken from the sidecar. All AI-related tiles were individually
  re-verified at native size on that basis.
