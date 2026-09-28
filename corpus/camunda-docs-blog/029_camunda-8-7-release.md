---
n: 272
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: "Camunda 8.7 Release is Here"
url: https://camunda.com/blog/2025/04/camunda-8-7-release/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "the visual pass reads the captured figure as class 'screenshot': modeler canvas with properties panel; the page names BPMN itself: 'The new Camunda version supports a new BPMN element: the ad-hoc sub-process.'"
bpmn_evidence_quote: "The new Camunda version supports a new BPMN element: the ad-hoc sub-process."
ai_evidence: "the captured IDP process runs three parallel extraction service tasks - 'Extract IDs', 'W2 Extraction', 'Paystub Extraction' - whose properties bind the 'IDENTIFICATION EXTRACTION' template to AWS Textract and an S3 bucket (idp-extraction-connector, region us-east-1, 'stored temporarily during Textract analysis'), read at 1400 px; the page frames IDP as its AI investment ('We accompany this investment in AI with the power of Intelligent Document Management (IDP)'). No model name is printed on the canvas: the AI-ness rests on the connector template and the page's own words"
ai_evidence_quote: "We accompany this investment in AI with the power of Intelligent Document Management (IDP), Robotic Process Automation (RPA), SAP Integration, Camunda Copilot and more. This"
artefacts:
  screenshot: 029_camunda-8-7-release.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1059
capture_method: figure downloaded at w=1400 from the asset URL the saved page names (cdn.sanity.io), fetched 2026-09-26
---

## What the page shows

The post is Camunda's own write-up of "Camunda 8.7 Release is Here".
The line the record quotes on the AI element is: "We accompany this investment in AI with the power of Intelligent Document Management (IDP), Robotic Process Automation (RPA), SAP Integration, Camunda Copilot and more."

The captured figure is the page's 1059x918 asset with alt text "Image1". The contact-sheet pass over the same asset read it as class "screenshot" with ai_visible=no, in its own words: modeler canvas with properties panel

## Observations (description only, no interpretation)

- **AI activity - function:** the page's own words bind the AI to the process: "We accompany this investment in AI with the power of Intelligent Document Management (IDP), Robotic Process Automation (RPA), SAP Integration, Camunda Copilot and more." - the AI-bearing element it names is ad-hoc sub-process; elsewhere: "Support for ad-hoc sub-processes" (ad-hoc sub-process)
- **AI activity - element type:** the captured figure is what the contact-sheet pass read as class "screenshot" (ai_visible=no), in its words: modeler canvas with properties panel
- **Authority - downstream:** the page: "handling support has been added to over ten (10) connectors, allowing users to send documents via Microsoft Teams , Slack , or as email attachments."
- **Authority - data:** the page: "and LLM technologies, intelligent document processing (IDP) helps you integrate automated document processing by extracting desired data fields and using them later into your end-to-end"
- **Authority - control:** not visible on the page - no gateway, threshold or routing rule is named
- **Input provenance:** the page: "Web Modeler now offers form review support for process application versions."
- **Guards present:** the page: "Play supports manual testing; however, this approach often leads to limited test coverage, lacks protection against regressions, and involves repetitive, error-prone tasks."
- **Prompt / model detail visible:** not visible on the page - no model name, prompt text or parameter is printed

## Notes for the researcher

The AI call here rests on the page's own words, not on a reading of the figure. 

Capture: the page's 1059x918 asset, downloaded at w=1400 and stored as 029_camunda-8-7-release.png; the contact-sheet reading of the same asset is class screenshot / ai_visible no. Figure choice: forced by gen_overrides.json: figure 1 is a BPMN-file dependency map, not a process; figure 2 is the IDP extraction process.
