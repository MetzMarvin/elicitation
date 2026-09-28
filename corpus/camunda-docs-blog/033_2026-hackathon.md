---
n: 496
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: "A Look Back at the Camunda 2026 Kickoff Hackathon"
url: https://camunda.com/blog/2026/02/2026-hackathon/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "the visual pass reads the captured figure as class 'screenshot': Modeler; 'AWS Bedrock outbound connector' task, Invoke Model"
bpmn_evidence_quote: "Hackathon screenshot"
ai_evidence: "the capture (Modeler, read at 1400 px) shows a task labelled 'Bedrock Connector' with the applied template 'AWS BEDROCK OUTBOUND CONNECTOR' and Configuration Action 'Invoke Model', plus Authentication fields Access key / Secret key - an LLM-bound task inside the process. The page text never names Bedrock, so the AI element is visible in the figure only; the quote is the page's nearest line about connectors on the canvas"
ai_evidence_quote: "Users can easily select a connector and remain focused on building their automation rather than hunting down connector configuration parameters."
artefacts:
  screenshot: 033_2026-hackathon.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1999
capture_method: figure downloaded at w=1400 from the asset URL the saved page names (cdn.sanity.io), fetched 2026-09-26
---

## What the page shows

The post is Camunda's own write-up of "A Look Back at the Camunda 2026 Kickoff Hackathon".
The line the record quotes on the AI element is: "Test anything, not just anywhere, but in the Modeler: This project enables task testing for sub-processes (including agentic ad-hoc sub-processes) so they can be tested in the Modeler."

The captured figure is the page's 1999x1451 asset with alt text "Hackathon screenshot". The contact-sheet pass over the same asset read it as class "screenshot" with ai_visible=yes, in its own words: Modeler; "AWS Bedrock outbound connector" task, Invoke Model

## Observations (description only, no interpretation)

- **AI activity - function:** the page's own words bind the AI to the process: "Test anything, not just anywhere, but in the Modeler:" - the AI-bearing element it names is ad-hoc sub-process
- **AI activity - element type:** the captured figure is what the contact-sheet pass read as class "screenshot" (ai_visible=yes), in its words: Modeler; "AWS Bedrock outbound connector" task, Invoke Model
- **Authority - downstream:** not visible on the page - the page does not say what the AI's output acts on
- **Authority - data:** not visible on the page - no variable, payload or document is named
- **Authority - control:** not visible on the page - no gateway, threshold or routing rule is named
- **Input provenance:** the page: "Web Modeler become pull requests and automated deployments, letting users keep Git as the source of truth while using Camunda to orchestrate Camunda’s own release"
- **Guards present:** the page: "Changes are planned first, then approved, allowing the user to review a list of changes before deploying them."
- **Prompt / model detail visible:** not visible on the page - no model name, prompt text or parameter is printed

## Notes for the researcher

The AI call here rests on the page's own words, not on a reading of the figure. 

Capture: the page's 1999x1451 asset, downloaded at w=1400 and stored as 033_2026-hackathon.png; the contact-sheet reading of the same asset is class screenshot / ai_visible yes. Figure choice: forced by gen_overrides.json: figure 1 is a chat panel; figure 2 is the Modeler capture with the Bedrock connector task.
