---
n: 1428
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: "Optimizing a Process for Target KPIs with AI: A Job Analysts Used to Do by Hand"
url: https://camunda.com/blog/2026/09/optimizing-a-process-for-target-kpis-with-ai-a-job-analysts-used-to-do-by-hand/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "the artefact is the figure the record captures; the page names BPMN itself: 'This was tested in practice, using Camunda's open AI Skills, just like last time.'"
bpmn_evidence_quote: "This was tested in practice, using Camunda's open AI Skills, just like last time."
ai_evidence: "AI appears only around the process (AI Skills (coding assistance)): 'Building a process from scratch is one thing.'"
ai_evidence_quote: "Building a process from scratch is one thing."
artefacts:
  screenshot: 121_optimizing-a-process-for-target-kpis-with-ai-a-job-analysts-used-to-do.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 2048
capture_method: figure downloaded at w=1400 from the asset URL the saved page names (cdn.sanity.io), fetched 2026-09-26
---

## What the page shows

The post is Camunda's own write-up of "Optimizing a Process for Target KPIs with AI: A Job Analysts Used to Do by Hand".
The line the record quotes on the AI element is: "Building a process from scratch is one thing."

The captured figure is the page's 2048x517 asset with alt text "BPMN". The contact-sheet pass over the same asset read it as class "-" with ai_visible=-, in its own words: (not in the sheets)

## Observations (description only, no interpretation)

- **AI activity - function:** the page mentions AI only around the process - "Building a process from scratch is one thing." refers to AI Skills (coding assistance), not to an element inside it; no AI function is described inside the process itself
- **AI activity - element type:** the page gives the figure the alt text "BPMN"; no element-template binding is visible
- **Authority - downstream:** the page: "removed the extra crossing arrows between the security and risk department lanes, and made the “approve (dual review)” and “approve (single review)” lines less tangled."
- **Authority - data:** the page: "Moving the risk check earlier, adding a timer escalation, and pre-packaging data for reviewers are all low-risk and can move faster."
- **Authority - control:** the page: "how accurate its forecast was, whether the DMN thresholds backed by real data , or how solid the merged AI calls were—they said so, plainly."
- **Input provenance:** the page: "of open Camunda skills from the camunda/skills repository (camunda-bpmn, camunda-dmn, camunda-forms, camunda-ai-agents, and others), the same model (Sonnet 5), and the same architect running them,"
- **Guards present:** the page: "exact math: even if manual escalation drops to the 10% target, one 45-minute manual step alone adds 0.10 × 45 = 4.5 minutes—almost the whole"
- **Prompt / model detail visible:** not visible on the page - no model name, prompt text or parameter is printed

## Notes for the researcher

**This item is UNCERTAIN and needs a human ruling.** Open question: Does any element of the BPMN diagram on this page call an AI/LLM service? The page text mentions AI but never binds it to a process element.

The AI call here rests on the material above. The page does mention AI, but only around the process - AI Skills (coding assistance).

Capture: the page's 2048x517 asset, downloaded at w=1400 and stored as 121_optimizing-a-process-for-target-kpis-with-ai-a-job-analysts-used-to-do.png; the contact-sheet reading of the same asset is class - / ai_visible -. Figure choice: alt 'BPMN' + sheet note ''.
