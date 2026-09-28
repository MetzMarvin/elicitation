---
n: 962
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: "Let's Face it, BPMN and DMN Rock!"
url: https://camunda.com/blog/2018/05/camunda-aws-rekognition/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "the visual pass reads the captured figure as class 'bpmn': AWS Recognition lane, Perform Face Match; AI not labelled; the page names BPMN itself: 'Let’s Face it, BPMN and DMN Rock!'"
bpmn_evidence_quote: "Let’s Face it, BPMN and DMN Rock!"
ai_evidence: "no AI/LLM element is bound to a process element on this page; the judgement rests on the figure and the page text: 'Let’s Face it, BPMN and DMN Rock!'"
ai_evidence_quote: "Let’s Face it, BPMN and DMN Rock!"
artefacts:
  screenshot: 094_camunda-aws-rekognition.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: marginal
capture_width_px: 602
capture_method: figure downloaded at w=1400 from the asset URL the saved page names (cdn.sanity.io), fetched 2026-09-26
---

## What the page shows

The post is Camunda's own write-up of "Let's Face it, BPMN and DMN Rock!".
The line the record quotes on the AI element is: "Let’s Face it, BPMN and DMN Rock!"

The captured figure is the page's 602x345 asset with alt text "sample process outline". The contact-sheet pass over the same asset read it as class "bpmn" with ai_visible=unclear, in its own words: AWS Recognition lane, Perform Face Match; AI not labelled

## Observations (description only, no interpretation)

- **AI activity - function:** not visible on the page - the post names no AI/LLM activity
- **AI activity - element type:** the captured figure is what the contact-sheet pass read as class "bpmn" (ai_visible=unclear), in its words: AWS Recognition lane, Perform Face Match; AI not labelled
- **Authority - downstream:** the page: "def compareFacesResult=rekognitionClient.compareFaces(request); I am using Camunda Spin to persist the response as a Json process variable."
- **Authority - data:** not visible on the page - no variable, payload or document is named
- **Authority - control:** not visible on the page - no gateway, threshold or routing rule is named
- **Input provenance:** the page: "implementation I used a start event listener and some groovy script to render the bounding boxes from the Recognition service onto the source and target"
- **Guards present:** not visible on the page - no human review, threshold or validation step is named
- **Prompt / model detail visible:** not visible on the page - no model name, prompt text or parameter is printed

## Notes for the researcher

**This item is UNCERTAIN and needs a human ruling.** Open question: Does any element of the BPMN diagram on this page call an AI/LLM service? The page text mentions AI but never binds it to a process element.

The AI call here rests on the material above. 

Capture: the page's 602x345 asset, downloaded at w=1400 and stored as 094_camunda-aws-rekognition.png; the contact-sheet reading of the same asset is class bpmn / ai_visible unclear. Figure choice: alt 'sample process outline' + sheet note 'AWS Recognition lane, Perform Face Match; AI not labelled'.
