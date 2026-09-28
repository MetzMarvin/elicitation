---
n: 22
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Zoom Connector
url: https://marketplace.camunda.com/apps/782061/zoom-connector
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: true
question: The only AI evidence here is an element-template glyph in a published figure: 'Pick Best Time for Meeting' carries the violet four-pointed star that the XML-proved AI-agent task 'Agent as a Judge' (io.camunda.connectors.agenticai.aiagent.v1, n=006) and the AI-named tasks in n=008 also display, while the page text never says AI and no .bpmn is published. Confirm that reading, or reclassify if a non-AI template shares that glyph.
needs_visual_check: false
bpmn_evidence: Camunda Web Modeler canvas published as the listing's overview asset (also published at 1x as the overview image); no .bpmn downloadable. Read natively: start event, four rounded-rectangle service tasks in sequence, end event.
bpmn_evidence_quote: "Receive Email from Client"
ai_evidence: The third task, 'Pick Best Time for Meeting', carries the violet disc with a white four-pointed star - the AI-agent element-template glyph. It is not one of the Zoom connector's operations: the page lists the connector as 'schedule meetings, retrieve/update/delete meetings, manage registrants', so a task that picks the best time is a reasoning step, not a Zoom REST call. The page's own text contains no AI mention at all.
ai_evidence_quote: "Pick Best Time for Meeting"
artefacts:
  screenshot: 022_zoom-connector-ai-pick-best-time.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own overview asset; native read at 1100x559, then 10x-16x zoom crops of each task's element-template glyph
---

## What the page shows

A meeting-scheduling demo published on the Zoom Connector listing. A client's email arrives ('Receive Email from Client', email connector glyph), the process lists the user's upcoming meetings ('List Upcoming Meetings', Zoom glyph), then 'Pick Best Time for Meeting' (violet four-pointed-star glyph) and creates the meeting ('Create Zoom Meeting', Zoom glyph).

## Observations (description only, no interpretation)

- **AI activity - function:** the task name says the decision ('Pick Best Time for Meeting'); the page does not describe it.
- **AI activity - element type:** a `serviceTask` carrying the AI-agent element-template glyph; no `.bpmn` is published, so the binding cannot be read as XML.
- **Authority - downstream:** 'Create Zoom Meeting' consumes the chosen slot; before it, the Zoom connector task 'List Upcoming Meetings' supplies the candidates.
- **Authority - data:** not visible on the page.
- **Authority - control:** none - the four tasks are in a straight sequence with no gateway.
- **Input provenance:** the client's email and the user's Zoom meeting list.
- **Guards present:** none observed.
- **Prompt / model detail visible:** not visible on the page.

## Notes for the researcher

This is the source's clearest case where the only AI evidence is an element glyph in a published figure, and the page text is silent: its verdict rests on the glyph being the same mark that the XML-proved 'Agent as a Judge' task (io.camunda.connectors.agenticai.aiagent.v1, n=006) and the AI-labelled tasks in n=008 display. Flagged for the researcher's ruling for that reason.
