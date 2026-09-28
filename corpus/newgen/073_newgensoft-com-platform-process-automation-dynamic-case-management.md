---
n: 073
source: newgen
source_name: Newgen (Newgen Software - NewgenONE low-code process automation / BPM platform and NewgenONE Marvin GenAI; newgensoft.com)
title: AI-first Dynamic Case Management Software | Newgen Software
url: https://newgensoft.com/platform/process-automation/dynamic-case-management/
accessed: 2026-09-25
verdict: INCLUDE
row: 513
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: screenshot of the product's own BPMN modeller (newgenONE Process Designer, "BPMN View")
bpmn_evidence_quote: "'BPMN View' tab, palette 'Task Templates / Start Events / Activities / Intermediate Events / Gateways / Integration Points / End Events / Artifacts', pool lane 'Swimlane'"
ai_evidence: element label inside the model
ai_evidence_quote: "service task 'AI Rule Engine' whose outgoing sequence flow is 'AI Decisioning'; lane band 'AI assisted Data Processing'"
artefacts:
  screenshot: corpus/newgen/073_newgensoft-com-platform-process-automation-dynamic-case-management_Dynamic-Case-Management-.png
  assets:
    - https://newgensoft.com/wp-content/uploads/2023/08/Dynamic-Case-Management-center-scaled-1.webp
  bpmn_xml: null
  archive: null
duplicate_of: null
access: public
capture_source: page asset, found by the visual backstop pass (the asset is not named in the page text and its alt text is "arrow icon")
capture_quality: legible
capture_width_px: 2560
capture_method: downloaded from the page's own HTML, converted webp -> png
---

## What the page shows

A macOS monitor mock-up. The screen is the newgenONE Process Designer on a process called
"Credit Card Issuance v6.0 (Draft)", inside a browser tab reading "Credit Card Issua...".
The modelling surface is in BPMN view: a header button "BPMN View", a vertical element palette
(Task Templates, Start Events, Activities, Intermediate Events, Gateways, Integration Points,
End Events, Artifacts) and a second palette "Global Task Templates -> New Task / Process Task /
Address_Verification / Background_Ver...". The canvas carries the pool lane name "Swimlane" and
three stage bands: "Initiation", "AI assisted Data Processing", "Automation". Round call-outs
magnify the palette and one task, "Initiate Re-KYC".

Visible elements: start events Web, Mobile, Chatbot, Email; a task "AI Rule Engine" with its
outgoing sequence flow labelled "AI Decisioning"; a task "BOT Processing"; intermediate/boundary
markers; gateways "BOT_Decision", "Exp_Dec", "Checker_Dec", "Maker_Dec"; tasks "KYC Maker",
"KYC Checker", "Case Manager", "Exception Wo..."; an end event.

The page's own copy: "Orchestrate complex, unstructured work across knowledge workers, AI agents, and enterprise systems." It also states: "'Ensure compliance and consistency with CMMN 1.1
standards , enabling transparent and efficient case management across complex workflows."

## Observations (description only, no interpretation)

- The AI-labelled element is a task inside the model, and the sequence flow leaving it is also
  AI-labelled; both sit in the lane band "AI assisted Data Processing".
- The lane band "Automation" holds the BOT_/KYC_/Case_Manager tasks; "BOT Processing" and
  "BOT_Decision" are plain RPA vocabulary and are not counted as AI elements.
- The page text talks about AI agents and AI-powered case creation; nothing on the page names
  this figure, whose alt text is the site-wide placeholder "arrow icon".
- The same "Credit Card Issuance" process also appears in record 037 (row 511) as the asset
  Dynamic-Case-Management-1.png; this record's asset is a different file
  (Dynamic-Case-Management-center-scaled-1.webp, 2560x1057, with call-out circles).

## Notes for the researcher

Found by the visual backstop pass over the 1117 broader-set figures, not by the DOM/text pass:
this page was excluded E0-no-artefact because its only process-named figure was the stock
pictogram diagram-project.svg, and this asset carries no process hint in its file name or alt.

The near-duplicate relation to record 037 is left for the reconciliation step; the two files
differ (different dimensions, different crop, call-outs present here), so they were not merged.
