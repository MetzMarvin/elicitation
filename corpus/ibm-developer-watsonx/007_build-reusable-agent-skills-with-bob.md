---
n: 332
source: ibm-developer-watsonx
source_name: IBM Developer tutorials (watsonx Orchestrate, BPMN-to-agent)
title: "Build reusable Bob skills for developer workflow automation - the 'Iterative Bob skill validation process' figure"
url: https://developer.ibm.com/articles/build-reusable-agent-skills-with-bob/
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "This figure is laid out exactly like a process model: five numbered rounded activity boxes in sequence - 'Invoke Skill / Run the skill with current configuration', 'Verify Tool Calls / Check whether the correct tools were called and executed', 'Compare Dashboard / Compare the generated dashboard against the ground-truth example', 'Identify Gaps / Identify differences and gaps in functionality, data, or UI/UX', 'Refine Skill & Tools / Update SKILL.md instructions or improve tool implementations to address the gaps' - joined by solid arrows, ending in an empty decision diamond 'Meets Expectations?' whose 'Yes' branch goes to a green 'Done' box and whose dashed 'No' branch loops back to step 1, with a 'Repeat Until Satisfactory' loop annotation. There are no BPMN events (no start or end circles), no BPMN task types and no pools or lanes, and the page's own alt text calls it a 'process' ('Iterative Bob skill validation process'). Is this a BPMN 2.0 model drawn in the vendor's house style - in which case it belongs in the corpus, since the whole process is about an AI skill - or a proprietary flow illustration that E1-not-bpmn excludes?"
needs_visual_check: false
bpmn_evidence: "png (zoomed at full size). five numbered activity boxes with corner icons, plain decision diamond with Yes/No branches, dashed loop-back; page alt text calls it an 'Iterative Bob skill validation process'."
bpmn_evidence_quote: "Iterative Bob skill validation process:"
ai_evidence: "the page is about IBM Bob, an AI coding agent, and the figure draws the iteration in which Bob's skills are validated: numbered activity boxes with a 'Meets Expectations?' decision diamond, i.e. the AI's own workflow. The page states the shift verbatim: 'As AI agents become more capable, the challenge is not just writing code.' UNCERTAIN because the notation is a vendor house style rather than BPMN 2.0."
ai_evidence_quote: "Iterative Bob skill validation process:"
artefacts:
  screenshot: 007_332_image7.png
  assets: [007_332_image7.png]
  bpmn_xml: []
  archive: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: "the figure fetched from its native asset URL on developer.ibm.com and viewed at full size on 2026-09-25"
judgment: true
---

## What the artefact is

`https://developer.ibm.com/articles/build-reusable-agent-skills-with-bob/` (api, ledger row n=332), figure `figs/332_image7`.

## What the figure shows



## Why the row is UNCERTAIN

png (zoomed at full size). five numbered activity boxes with corner icons, plain decision diamond with Yes/No branches, dashed loop-back; page alt text calls it an 'Iterative Bob skill validation process'.

## AI evidence (why this is not an E2 exclusion)

the page is about IBM Bob, an AI coding agent, and the figure draws the iteration in which Bob's skills are validated: numbered activity boxes with a 'Meets Expectations?' decision diamond, i.e. the AI's own workflow. The page states the shift verbatim: "As AI agents become more capable, the challenge is not just writing code." UNCERTAIN because the notation is a vendor house style rather than BPMN 2.0.

## Notes for the researcher

- The page is a census item of the source; this ruling decides only whether the figure enters the corpus, not whether the page was enumerated.
- The row is `UNCERTAIN`, so it is handled downstream exactly like an `INCLUDE`; the question above is the single decision that needs a human.
