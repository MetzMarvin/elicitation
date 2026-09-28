---
n: 214
source: bizagi
source_name: Bizagi (vendor documentation, help.bizagi.com)
source_type: vendor docs
title: Executing a configured UiPath bot from a Process
url: https://help.bizagi.com/platform/en/uipath-executing-a-configured-bot-from-a-process.htm
accessed: 2026-09-24
verdict: UNCERTAIN
needs_human_ruling: true
question: "The Activity actions menu lists an "AI Bot" action type on a BPMN task (screenshot uipath-bot08.png). Is an "AI Bot" activity action an AI/LLM element, or an RPA-bot variant?"
needs_visual_check: true
bpmn_evidence: vendor figure: BPMN pool/lane model with tasks Submit CV and Read CV behind the Activity actions menu
bpmn_evidence_quote: "Submit CV, Read CV"
ai_evidence: page text + the vendor figure
ai_evidence_quote: "AI Bot"
artefacts:
  screenshot: 009_uipath-bot08.png
  archive: 009_uipath-executing-a-configured-bot-from-a-process.page.html
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1400
capture_method: curl of the vendor's own .png asset at its native URL (help.bizagi.com documentation image)
---

## What the page shows

A Bizagi Studio process model for CV screening: pool with lanes (`Candidate`, screening
side), start event -> gateway -> task `Submit CV` -> task `Read CV` -> further tasks, and
the `Activity actions` dialog open with the right-click menu listing the action types -
`Expression`, `Sub-process`, `Script`, `C#`, `SAP`, `Connector`, `AI Bot`, `Pipeline`,
`Task`, `Properties`. The page documents executing a configured UiPath bot from a
process. The identical figures are published on the Automation Anywhere and Blue Prism
bot-integration pages of the same documentation set.

## Observations (description only, no interpretation)

- **AI activity - function:** not described in the page text. The page text contains no
  standalone "AI" token at all; the only AI evidence is the `AI Bot` entry in the action
  menu shown in the figure.
- **AI activity - element type:** an Activity Action type selectable on a BPMN task.
- **Authority - downstream:** not visible on the page.
- **Authority - data:** not visible on the page.
- **Authority - control:** not visible on the page.
- **Input provenance:** not visible on the page (the figure's task labels `Submit CV` /
  `Read CV` suggest a document, but the page does not say).
- **Guards present:** none observed.
- **Prompt / model detail visible:** not visible on the page.

## Notes for the researcher

- **This record is the weakest in the source and is flagged for a ruling.** The page text
  says only: "There are two different ways of configuring the execution of an RPA bot from
  Bizagi: From an Activity Action and Defining an integration interface." The claim rests
  on a small menu label inside the figure (`capture_quality: legible`, 1400 px - the
  researcher can read it directly in `009_...png`). If the entry reads otherwise, the
  correct verdict is `E2-no-ai-element`.
- The same figures are republished on the Automation Anywhere and Blue Prism pages; those
  two rows are recorded as E3 duplicates of this record.
