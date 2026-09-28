---
n: 222
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: FHIR Solution
url: https://marketplace.camunda.com/apps/822034/fhir-solution
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: The listing publishes an element-template properties screenshot but no process diagram, and its only AI signal is the 'Agentic Solutions' category facet. Does this count as a collected artefact for the corpus (an element template without a visible process), or should it be ruled E0-no-artefact?
needs_visual_check: false
bpmn_evidence: The listing publishes no BPMN diagram at all. Its only artefact-shaped image is the element-template properties panel, cropped tight: header 'HAPI FHIR CONNECTOR / Read Practitioner', the Action dropdown set to 'Read Practitioner' ('Operation to perform on the Practitioner resource'), Practitioner ID '13520646' with the note 'Logical ID of the Practitioner on the FHIR server. Use a process variable: = practitionerId', and Output Mapping with the result variable 'createPractitionerResponse'. No canvas, no events, no sequence flow anywhere on the page; the second image is the Truvio Systems wordmark.
bpmn_evidence_quote: "Read Practitioner"
ai_evidence: No AI element is visible in the published artefact - the template shown is a plain FHIR read operation. The page's only AI signal is a category facet: 'Categories: Agentic Solutions' (with 'Solution Accelerators'), i.e. the marketplace's own product grouping, not an AI step in a process. The page's prose describes FHIR resource operations only.
ai_evidence_quote: "Categories: Agentic Solutions"
artefacts:
  screenshot: 222_fhir-solution.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: listing-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own asset (d3bql97l1ytoxn.cloudfront.net, app_resources/.../overview/img6117393677811025124-2x.png, 285x613), read natively at full size; the listing's other image is the vendor logo
---

## What the page shows

The FHIR Solution (Truvio Systems). A HAPI FHIR connector listing whose screenshots show the element template's properties panel ('Read Practitioner') and the vendor's logo; the listing's prose describes reading and writing FHIR resources from a process.

## Observations (description only, no interpretation)

- **AI activity - function:** none visible. The only operation shown is 'Read Practitioner' ('Operation to perform on the Practitioner resource') with Practitioner ID '13520646'.
- **AI activity - element type:** none; the shown artefact is an element-template properties panel, not a task in a process.
- **AI activity - models named:** none.
- **Authority - downstream:** not observable - no process is published, so nothing downstream of any task is visible.
- **Authority - control:** not observable.
- **Data reachable:** a FHIR Practitioner resource, addressed by logical ID via a process variable (= practitionerId).
- **Human role:** not observable.
- **Why UNCERTAIN:** the artefact exists as an element template but is not shown inside a process, and the page's 'Agentic Solutions' facet may or may not have been meant to signal AI tasks in the connector's wider operation set - neither can be settled from what is published.

## Notes for the researcher

Held as UNCERTAIN under the assignment's own rule for connector listings that publish an element template but no diagram, and because the marketplace's 'Agentic Solutions' facet on an otherwise plain FHIR connector is exactly the kind of signal a human ruling should settle: if the facet is the vendor's own classification it is a claim about AI worth recording; if it is a marketplace tag applied to any solution accelerator, the listing has no AI artefact at all. Nothing was guessed here - the record states only what the two images and the page text show.
