---
n: 571
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: "Intelligent Process Automation with Camunda and Amazon Comprehend"
url: https://camunda.com/blog/2021/06/intelligent-process-automation-with-camunda-and-amazon-comprehend/
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: "This row's captured asset is a hero photograph, but the page refers to a second picture ('The picture below shows the architecture of the project'), which was not captured. Is that architecture picture a BPMN 2.0 diagram, and does it contain an AI/ML element inside the process (e.g. the Amazon Comprehend extraction task)?"
needs_visual_check: true
bpmn_evidence: "the visual pass reads the captured figure as class 'photo': woman with tablet in corridor; the page names BPMN itself: 'The picture below shows the architecture of the project (code available here ).'"
bpmn_evidence_quote: "The picture below shows the architecture of the project (code available here )."
ai_evidence: "the page binds AI to a process element (Amazon AI service, intelligent document analysis): 'Intelligent Process Automation with Camunda and Amazon Comprehend'; the contact-sheet pass reads the captured figure as ai_visible=no"
ai_evidence_quote: "Intelligent Process Automation with Camunda and Amazon Comprehend"
artefacts:
  screenshot: 090_intelligent-process-automation-with-camunda-and-amazon-comprehend.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 2400
capture_method: figure downloaded at w=1400 from the asset URL the saved page names (cdn.sanity.io), fetched 2026-09-26
---

## What the page shows

The post is Camunda's own write-up of "Intelligent Process Automation with Camunda and Amazon Comprehend".
The line the record quotes on the AI element is: "Intelligent Process Automation with Camunda and Amazon Comprehend"

The captured figure is the page's 2400x1602 asset with alt text "Intelligent Process Automation with Camunda and Amazon Comprehend". The contact-sheet pass over the same asset read it as class "photo" with ai_visible=no, in its own words: woman with tablet in corridor

## Observations (description only, no interpretation)

- **AI activity - function:** the page's own words bind the AI to the process: "Intelligent Process Automation with Camunda and Amazon Comprehend" - the AI-bearing element it names is Amazon AI service; elsewhere: "Intelligent Process Automation with Camunda and Amazon Comprehend" (Amazon AI service)
- **AI activity - element type:** the captured figure is what the contact-sheet pass read as class "photo" (ai_visible=no), in its words: woman with tablet in corridor
- **Authority - downstream:** not visible on the page - the page does not say what the AI's output acts on
- **Authority - data:** the page: "need a service that extracts the required data from the invoice documents (e.g., name, amount, date, type of service, etc.), provides them to the Invoice"
- **Authority - control:** not visible on the page - no gateway, threshold or routing rule is named
- **Input provenance:** the page: "These data are then sent to the Invoice Department in the form of an email, and the process completes."
- **Guards present:** not visible on the page - no human review, threshold or validation step is named
- **Prompt / model detail visible:** the page: "We chose the Embedded Task Forms that allow for embedding Custom HTML and Javascript forms into the Camunda Tasklist."

## Notes for the researcher

The AI call here rests on the page's own words, not on a reading of the figure. 

Capture: the page's 2400x1602 asset, downloaded at w=1400 and stored as 090_intelligent-process-automation-with-camunda-and-amazon-comprehend.png; the contact-sheet reading of the same asset is class photo / ai_visible no. Figure choice: alt 'Intelligent Process Automation with Camunda and Am' + sheet note 'woman with tablet in corridor'.
