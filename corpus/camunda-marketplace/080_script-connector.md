---
n: 80
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Script Connector
url: https://marketplace.camunda.com/apps/810748/script-connector
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: The listing's canvas images are cropped: they show one start event with the element-template picker open on 'Script Connector' plus four properties panels, and no complete process (no end event, no other activity) is published anywhere on the page. Is a cropped canvas fragment enough to count as a process artefact for this census, or should the listing be E0-no-artefact?
needs_visual_check: true
bpmn_evidence: Camunda Web Modeler canvas published as the listing's own screenshots; no .bpmn downloadable. Every published view is cropped: the widest shows an incomplete start event at the left edge with the 'Change element' picker open on 'Script Connector / A connector to execute a script' (the picker also offers 'Ad-hoc tools schema - Connector to fetch tools schema infor...' and 'Script task'), and the remaining four views are the task's properties panels (Type Embedded with Script 'a + b' in javascript; Type Resource with 'file:./script.js'; output mapping to the variable 'AplusB'). No end event and no second activity is visible in any asset.
bpmn_evidence_quote: "A connector to execute a script"
ai_evidence: No AI element is visible in any published view, and the page carries no AI or LLM mention at all (the listing's own description is 'Teams migrating from Camunda 7 to Camunda 8 often depend on embedded scripts for lightweight business logic'). The modelled task is the Script Connector element template - an outbound connector that executes a script, here either an embedded 'a + b' in javascript or the resource 'file:./script.js'. The 'Ad-hoc tools schema' entry that appears in one screenshot is a row in the element-template picker dialog, not an element used in a published model.
ai_evidence_quote: "Execute scripts within your processes"
artefacts:
  screenshot: 080_script-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: marginal
capture_width_px: null
capture_method: curl of the listing's own overview image (d3bql97l1ytoxn.cloudfront.net, overview/img1734796207572782182.png, 426x330); native read at full size. The widest published view is this one, so the capture is the crop itself.
---

## What the page shows

Camunda's Script Connector listing (Community, Camunda Connectors Bundle, 8.6-8.9). The page explains that the connector gives Camunda 8 processes the embedded-script capability that Camunda 7 users relied on, with a choice between an inline script and a classpath or file resource. The published images are canvas crops of that task being configured, not a process.

## Observations (description only, no interpretation)

- **AI activity - function:** none visible.
- **AI activity - element type:** one `serviceTask` bound to the Script Connector element template; the properties panels show Type = Embedded (Script 'a + b', Script Language javascript) and Type = Resource (Script resource 'file:./script.js').
- **Authority - downstream:** not visible; the fragment ends at the task and the properties panel only maps the result to the variable 'AplusB'.
- **Authority - data:** the script context is shown as `{ a: 3, b: 5 }`; no external data source is involved.
- **Authority - control:** none visible - the crop contains no gateway, no boundary event and no end event.
- **Input provenance:** not visible; only a start event is shown, with no visible connection to the task.
- **Guards present:** none visible.
- **Prompt / model detail visible:** not applicable; the configured artefact is a javascript expression.

## Notes for the researcher

Captured as UNCERTAIN because the artefact, not the AI question, is what cannot be settled: the page publishes only crops, so the census cannot say what the surrounding process does, and a fragment with a start event but no reachable end is not a process diagram in the sense the other listings publish. The capture is graded 'marginal' for that reason. If the researcher rules that a cropped canvas counts, the listing still shows no AI element and would read as E2-no-ai-element; if a complete model is required, it is E0-no-artefact - either way the fragment is what the page offers.
