---
n: 192
source: uipath-maestro-docs
source_name: UiPath Maestro user guide (docs.uipath.com)
source_type: vendor documentation
title: Downloads
url: https://docs.uipath.com/maestro/automation-cloud/latest/user-guide/references-templates
accessed: 2026-09-25
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "Published .bpmn 2.0 XML: bpmn:definitions with the uipath namespace, bpmn:process isExecutable='false', serviceTask/userTask/sendTask/receiveTask/manualTask, exclusiveGateway/parallelGateway/eventBasedGateway, boundaryEvent, intermediateCatchEvent, bpmndi diagram interchange."
bpmn_evidence_quote: "bpmn:process id='Process_1' isExecutable='false'"
ai_evidence: "Invoice_Processing_Template.bpmn carries the text annotation '(Agent) Dispute investigation and resolution' (sibling annotations: '(Automation) 2-way matching process', '(Action Center) App Task form ...', '(Integration Service) Send email', '(Business Rule) decision table ...')."
ai_evidence_quote: "(Agent) Dispute investigation and resolution"
artefacts:
  screenshot: null
  archive: null
  bpmn_xml: 192_invoice-processing-template.bpmn, 192_loan-processing-template-bpmn.bpmn, 192_supplier-onboarding-template-bpmn.bpmn
duplicate_of: null
access: public
capture_source: page asset at its native URL (dev-assets.cms.uipath.com, .webp converted to .png) or the page's own downloadable model file
capture_quality: legible
capture_width_px: null
capture_method: plain GET of the figure asset listed on the page (ledgers/uipath-maestro-docs.raw/img/)
---

## What the page shows

Verbatim from the page:

> "Downloads link Downloadable BPMN template files for Maestro, including invoice processing and loan workflow templates for exploring platform capabilities."

## Judgement

Downloads page publishing three BPMN 2.0 model files; the invoice model contains a textAnnotation "(Agent) Dispute investigation and resolution" next to its service task.

## Artefact reading (native resolution unless stated)

- **BPMN:** Published .bpmn 2.0 XML: bpmn:definitions with the uipath namespace, bpmn:process isExecutable="false", serviceTask/userTask/sendTask/receiveTask/manualTask, exclusiveGateway/parallelGateway/eventBasedGateway, boundaryEvent, intermediateCatchEvent, bpmndi diagram interchange.
- **AI element:** Invoice_Processing_Template.bpmn carries the text annotation "(Agent) Dispute investigation and resolution" (sibling annotations: "(Automation) 2-way matching process", "(Action Center) App Task form ...", "(Integration Service) Send email", "(Business Rule) decision table ...").

- `192_invoice-processing-template.bpmn` - the published invoice model (contains the Agent annotation)
- `192_loan-processing-template-bpmn.bpmn` - the published loan model
- `192_supplier-onboarding-template-bpmn.bpmn` - the published supplier-onboarding model

## Notes for the researcher

Figure alt text on the page (verbatim): 
