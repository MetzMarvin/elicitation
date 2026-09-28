---
n: 348
source: citeck-ecos
source_name: Citeck ECOS (citeck-ecos.readthedocs.io documentation + Citeck/ecos-demo-app)
source_type: vendor documentation page (BPMN editor component reference)
title: AI Task (BPMN editor component reference)
url: https://citeck-ecos.readthedocs.io/en/latest/settings_kb/processes/ecos_bpmn/editor/components/ecos_bpmn_components_ai_task.html
accessed: 2026-09-24
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "documentation of one BPMN editor element type, with two complete BPMN 2.0 process files offered for download - both hold a <bpmn:task> carrying ecos:taskType=\"aiTask\""
bpmn_evidence_quote: "A task responsible for calling an AI based on a specified prompt. Subsequently, depending on business requirements, it can perform any action BPMN allows"
ai_evidence: "the AI sits inside the process as a task type: the downloaded processes are a signal start event -> AI task -> end event chain, and a status-triggered deal process whose AI task writes its answer into a document attribute"
ai_evidence_quote: "<bpmn:task name=\"Генерация текста КП\" id=\"Activity_0hzr440\" ecos:aiSaveResultToDocument=\"has-offer-text:offerText\" ecos:taskType=\"aiTask\">"
artefacts:
  screenshot: 001_example_3.png
  assets: [001_01_13.png, 001_example_1.png, 001_0228.png, 001_0419.png, 001_0519.png, 001_0620.png, 001_0131.png, 001_0321.png]
  bpmn_xml: [001_contract-content-diff-ai-process.bpmn, 001_crm-deal-ai-process.bpmn]
  archive: 001_en_ecos_bpmn_components_ai_task.page.html
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: poor
capture_width_px: 444
capture_method: curl of the Sphinx _images/ assets and of the two _downloads/*.bpmn.xml files, at their native URLs
---
## What the page shows

The page is the reference entry for one BPMN editor element type, "AI Task", and carries
eleven content figures plus two downloadable process files. Both files are BPMN 2.0 XML
served by the docs under `_downloads/<hash>/` and were fetched verbatim (the site's
`.bpmn.xml` name is kept, only the `.xml` suffix dropped so the file reads as BPMN):

* `contract-content-diff-ai-process` - `bpmn:startEvent` with a `bpmn:signalEventDefinition`
  (signal `RECORD_CHANGED;ANY;emodel/type@ecos-contract;...`) -> `bpmn:task`
  name="Комментарий сравнение версий" id="Activity_1o76vd3" -> `bpmn:endEvent`, 2 sequence flows.
* `crm-deal-ai-process` - `bpmn:startEvent` name="Сделка: статус Подготовка КП" (signal
  `RECORD_STATUS_CHANGED;ANY;emodel/type@deal;...`) -> `bpmn:task` name="Генерация текста КП"
  id="Activity_0hzr440" -> `bpmn:scriptTask` name="Генерация шаблона КП" -> `bpmn:endEvent`
  name="Завершение", 3 sequence flows.

Figures: `01_13.png` and `example_1.png` draw the contract process (signal circle -> AI task
-> end circle, the task rounded rectangle carrying the AI star badge); `example_3.png` draws
the CRM process (start circle "Сделка: статус Подготовка КП" -> AI task "Генерация текста
КП" -> script task "Генерация шаблона КП" -> end circle "Завершение"); `0131.png` is the
bpmn-js palette with the AI-task icon selected; `0228.png` is the element properties panel
("AI Task", "ID элемента Activity_1o76vd3", "Имя Комментарий сравнение версий");
`0321.png` "Предобработка", `0419.png` "Запрос к AI" with the prompt text and the
"Включить документ в контекст" checkbox, `0519.png` "Постобработка", `0620.png`
"Асинхронное выполнение" are the four property groups of the element. `example_2.png` and
`example_4.png` are the AI's output rendered as documents (a contract card comment and a
commercial proposal), not diagrams.

## Observations (description only, no interpretation)

- **AI activity - function:** the page's own words: "A task responsible for calling an AI
  based on a specified prompt"; the two examples call it for a contract-content diff
  ("Какие были последние изменения в содержимом договора?") and for commercial-proposal text.
- **AI activity - element type:** a BPMN `task` with `ecos:taskType="aiTask"`; in the palette
  figure it is a rounded rectangle with a star badge, i.e. a real element of the notation,
  not a sub-process or an external call.
- **Authority - downstream:** the AI task runs after a signal start event
  (`RECORD_CHANGED` / `RECORD_STATUS_CHANGED`) and its result is consumed by the process.
- **Authority - data:** `ecos:aiAddDocumentToContext="true"` on both tasks - the business
  document is put into the AI context; `ecos:aiSaveResultToDocument="has-offer-text:offerText"`
  on the CRM task - the answer is written into a named document attribute.
- **Authority - control:** `ecos:asyncConfig` on both tasks sets asyncBefore/asyncAfter and
  `exclusive`; the page documents "Асинхронно «перед»" / "Асинхронно «после»" behaviour and
  the page's `0620.png` shows both checkboxes unticked.
- **Input provenance:** `ecos:aiPreprocessingScript` (JavaScript run before the request) builds
  `aiRecordsContext` from document references, or loads attributes
  (`document.load("counterparty.fullOrganizationName")`) into process variables that the
  prompt then interpolates as `${counterparty}`, `${legalEntity}`, `${pas}`.
- **Guards present:** none visible beyond the async/exclusive flags; the page documents no
  timeout, retry or fallback path for the AI task, and no human confirmation step.
- **Prompt / model detail visible:** the prompt text is a value of the element
  (`ecos:aiUserInput`, shown in `0419.png` as the "Текст запроса" field); no model or
  provider name is set on the element, and the page names none for it.
- **Result handling:** `ecos:aiPostprocessingScript` (JavaScript after the response) reads the
  fixed variable `aiResponse`; the contract example turns it into a comment record.

## Notes for the researcher

- Two separate BPMN artefacts sit on one documentation page, so both are recorded here
  rather than as two records; each is a complete, downloadable process file, which makes this
  the strongest evidence in this source (decisive per the evidence rule: `<bpmn:task>` with an
  AI-bound attribute set, and the element type named in the notation).
- Capture: the two process diagrams are small (444 x 152 and 776 x 176 px), so
  `capture_quality: poor` by the 1400 px bar - but the `.bpmn` files themselves are the
  artefact and are byte-exact. The `.bpmn` files are the site's `*.bpmn.xml`; only the file
  name was shortened.
- The page's Russian twin (`/ru/develop/...`) is a separate population item and is judged on
  its own row.
