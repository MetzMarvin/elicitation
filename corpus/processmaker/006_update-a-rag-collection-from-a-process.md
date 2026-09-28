---
n: 685
record: 006
url: https://docs.processmaker.com/docs/update-a-rag-collection-from-a-process
source: processmaker
surface: docs:processmaker
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: A page that documents inserting a Data Connector Task into a process so that each case writes into a RAG Collection (an AI/vector store) but publishes no process model - is the documented process an AI-enabled BPMN artefact (INCLUDE) or does the missing diagram make it E0-no-artefact?
bpmn_evidence: |
  No BPMN artefact is published on this page. Its two standalone images are product screens, not
  diagrams: image 3 is a data connector's REST test screen ("/ Designer / Data Connectors / tests /
  ListAll", a GET/POST request against `.../api/1.0/collections/34/records`, with the Body tab open on
  the JSON payload `{"data": [{"file": "{{file.id}}", "name": "{{file.name}}", "uploads": [...]}]}`),
  and image 5 is a Form Task's runtime screen with its Form and Data tabs and the file-upload control
  ("New File Upload", "test_2.pdf - 15 KB - success"). The other images on the page are further
  connector and case screens.
  What the page does publish is an instruction to put an element into a process: "Insert a Data
  Connector Task in your process, ensuring it comes after the file is uploaded and the file-related
  variables are populated." The process itself is never drawn.
ai_evidence: |
  The AI store is named, the AI element is not drawn. The page's purpose is to feed a RAG Collection -
  retrieval-augmented generation, an AI/vector store - from a process: "Each time a case runs, the Data
  Connector will automatically insert the uploaded file as a new record in the RAG Collection,
  triggering the appropriate analysis." The element inside the process is a Data Connector task; the AI
  is at the other end of it, in the RAG Collection and whatever analysis the collection triggers. The
  page's sibling `configure-a-rag-collection` (row 334) and the RAG Collections index (row 588) are
  recorded as E0, so this row is the source's only statement that a process feeds the AI store at
  runtime.
artefacts:
  - screenshot: 006_update-a-rag-collection-from-a-process.png
  - file: ledgers/processmaker.raw/figures/docs__update-a-rag-collection-from-a-process/001_Articles_Body_1_.png
  - file: ledgers/processmaker.raw/figures/docs__update-a-rag-collection-from-a-process/002_Articles_-_Case.png
  - file: ledgers/processmaker.raw/figures/sh_rag.png
capture_quality: legible
capture_width_px: 1144
---

## What the page is

`docs/update-a-rag-collection-from-a-process`, a child of the RAG Collections articles under DESIGNER.
It documents the two-step recipe for writing case data into a RAG Collection: configure a Data
Connector against the collection's records endpoint, then call it from a Data Connector Task in the
process.

## What the capture shows

- image 3 - the Data Connector's test screen: the request against
  `/api/1.0/collections/34/records` and the JSON body that maps the uploaded file
  (`{{file.id}}`, `{{file.name}}`) into a new record.
- image 5 - the Form Task's screen where the participant uploads the file (`test_2.pdf`, "success"),
  i.e. the step the Data Connector Task must follow.

## Why this is UNCERTAIN and not E0

`E0-no-artefact` is the code for an item whose figures contain no process artefact at all. Taken
literally, the figures here qualify - they are connector and form screens. But the page's text
describes a process with an AI-bound element in it, and the census's job is to surface what a human
must rule on rather than to make that ruling. Under CLAUDE.md section 3 the doubt resolves to
UNCERTAIN and the row is recorded in full; leaving it as E0 would drop the only page in the source
that places an AI store inside a running process.

## Observations

- This row and record 004 (`idp-connector`) are the two places in this source where the AI is genuinely
  *at runtime* rather than at design time - IDP extracting fields during a Request, and a Data Connector
  writing into a RAG Collection during a Request. Both are invisible in the source's diagrams for the
  same reason: ProcessMaker draws its AI-bound elements as ordinary connector or task shapes.
