---
n: 120
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: SOAP Connector
url: https://marketplace.camunda.com/apps/565583/soap-connector
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: The published canvas is a cropped view: it shows the start event, the service task 'Call SOAP Service' (properties panel open on its SOAP body XML template and the secrets context 'usernamePassword') and a stretch of empty canvas to the right, with no end event and no other element visible anywhere on the page - the listing's only other image is the connector's icon. Is that fragment the whole process, or is the cropped canvas an incomplete artefact that should not count?
needs_visual_check: false
bpmn_evidence: BPMN diagram published as the listing's overview asset; no .bpmn downloadable. Read natively: start event -> service task 'Call SOAP Service' (connector glyph, element-template marker) with the properties panel open beside it, and empty canvas to the right of the task. No end event and no second element is visible; the Modeler palette sits at the image's left edge, so the screenshot is a crop of a wider canvas rather than a zoom on the task.
bpmn_evidence_quote: "Call SOAP Service"
ai_evidence: Nothing AI-bound is claimed or shown: the listing's own content contains no AI, LLM, model or AI-service term at all ('The SOAP connector allows Camunda users to interact with SOAP-based web services directly within BPMN-based processes'), and the visible element is a WSDL-driven SOAP call whose panel shows the XML body template '<sam:login><username>{{username}}</username><password>{{password}}</password></sam:login>' filled from the secrets context 'usernamePassword'. No AI element is visible, but neither is the whole process.
ai_evidence_quote: "The SOAP connector allows Camunda users to interact with SOAP-based web services directly within BPMN-based processes"
artefacts:
  screenshot: 120_soap-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own overview asset (d3bql97l1ytoxn.cloudfront.net, overview/img2971822995392944687-2x.png, 1096x660); native read at full size - a Web Modeler screenshot with the task's properties panel open
---

## What the page shows

Camunda's own SOAP Connector listing (Camunda, Community, 'Technical Protocols', 8.5-8.8). The page describes calling WSDL-defined operations from BPMN processes, with WSDL operation discovery, XML or expression-based payloads, custom headers and namespaces, response mapping to process variables and basic authentication. Its published artefact is a cropped Modeller screenshot of the connector's task.

## Observations (description only, no interpretation)

- **AI activity - function:** none claimed.
- **AI activity - element type:** the visible element is an ordinary `serviceTask` bound to the SOAP connector element template; no AI element is shown.
- **Authority - downstream / data / control:** not visible - the published crop contains only the start event and the one task.
- **Authority - control (human):** none visible.
- **Input provenance:** SOAP request data built from process variables through the XML template ({{username}}, {{password}}).
- **Guards present:** the page advertises authentication configuration (basic auth or custom headers) and response mapping; nothing is drawn.
- **Prompt / model detail visible:** not applicable.

## Notes for the researcher

This is the batch's second cropped-canvas case after the Script Connector (n=080), handled the same way: CLAUDE.md forbids excluding a diagram for being cropped or only partially visible, so the fragment is captured and the completeness question goes to the researcher. The page's own content names no AI or LLM technology at all, so if the fragment is the whole process the listing is E2-no-ai-element.
