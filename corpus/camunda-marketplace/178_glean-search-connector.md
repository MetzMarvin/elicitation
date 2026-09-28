---
n: 178
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Glean Search Connector
url: https://marketplace.camunda.com/apps/584408/glean-search-connector
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: BPMN diagram published as the listing's own asset (Camunda Web Modeler, canvas with palette and the element's action toolbar visible); no .bpmn downloadable. Read natively: start event -> serviceTask 'Search Glean - General' (carrying the connector's template glyph and a documentation icon) -> end event.
bpmn_evidence_quote: "Search Glean - General"
ai_evidence: The single task in the model is the AI-powered search call, and the page names it as such: 'Send questions directly from a Camunda-based process to Glean's AI-powered enterprise search API', with a feature list that includes 'AI-driven enterprise search from business processes' and the option of returning 'LLM-generated content'. The task carries the connector's element-template glyph on the canvas.
ai_evidence_quote: "Glean's AI-powered enterprise search API"
artefacts:
  screenshot: 178_glean-search-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own asset (d3bql97l1ytoxn.cloudfront.net, app_resources/584408/overview/img7949162463644361507-2x.png, 1100x437); native read at full size - a Camunda Web Modeler canvas
---

## What the page shows

The Glean Search Connector (community connector). The listing publishes a minimal model - start, one connector task, end - as the demonstration of how the connector is used inside a process; the page describes querying Glean's enterprise search and mapping the results into process variables.

## Observations (description only, no interpretation)

- **AI activity - function:** a question answered by Glean's AI-powered enterprise search API.
- **AI activity - element type:** an ordinary `serviceTask` labelled 'Search Glean - General' with the connector's template glyph; no agent element and no ad-hoc container.
- **Authority - downstream:** the end event - the published model has no branch after the search call.
- **Authority - data:** none drawn; the page says results are mapped 'into structured process variables for downstream tasks'.
- **Authority - control:** none - no gateway in the published model.
- **Authority - control (human):** none in the model.
- **Input provenance:** the query sent to the connector task (the page describes both static queries and 'a dynamic question assembled from process variables').
- **Guards present:** none drawn.
- **Prompt / model detail visible:** none - the page mentions the option to return LLM-generated content and parameters such as snippet and page size, but the published model shows no configuration.

## Notes for the researcher

A search-integration task that the vendor's own copy frames as AI ('AI-powered enterprise search', 'AI-driven enterprise search'). The artefact is minimal - start, task, end - so this listing is one of the thin ones; recorded INCLUDE because the AI element is inside the process and the page names the capability, not because the flow shows any control around it.
