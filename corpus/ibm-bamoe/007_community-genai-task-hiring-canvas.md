---
n: 133
record: 007
url: https://community.ibm.com/community/user/blogs/thiago-lugli/2025/09/23/introducing-the-bamoe-gen-ai-task-for-workflows
source: ibm-bamoe
surface: community:ibm.com
accessed: 2026-09-25
verdict: INCLUDE
needs_human_ruling: false
question:
bpmn_evidence: |
  The post's animation (ezgif-71d8d34e475aa4.gif, 215 frames at 800x494) is a BAMOE Canvas session on the
  project header "Workflow | Sample" with the tab bar reading "BPMN Editor", the canvas watermark
  "BPMN 2.0" (footer "React Flow"), and the palette panel open on the left showing the "AI" group
  with "Gen AI Task" above "Flexible processes > Milestone". On the canvas the hiring process is
  drawn in full - "…w Hiring" (New Hiring), two exclusive gateways, "Create Offer", "HR Interview"
  and "IT Interview" (both with timer boundary events), "Send Offer to Candidate", "Send
  notification HR Interview avoided", the sequence-flow label "Candidate doesn't meet requirements"
  and "Application d…" (Application denied) - and below it a Gen AI Task node carrying the sparkle
  has been dropped on the canvas by the recorded gesture.
ai_evidence: |
  The dropped node is the "Gen AI Task" (the sparkle glyph), and its property panel is open on the
  right with the AI fields unfilled at that moment: "AI Provider *" ("Select a Provider"), "Model *"
  ("Select a model"), "Temperature *" (hint "0.0 to 2.0, e.g. 0.3"), "Token Limit *" (hint
  "e.g. 1400"), "Prompt *", a greyed "Preview", and below them "Data mapping (in: -, out: 1)" and
  "onEntry / onExit". The post's own description: it introduces "the BAMOE Gen AI Task for
  workflows".
artefacts:
  - screenshot: 007_ibm-bamoe-genai-task-hiring-canvas.png
  - file: ledgers/_bamoe_comm/genai_g3.gif
  - file: ledgers/_bamoe_comm/genai_g3_f214_2x.png
  - file: ledgers/_bamoe_comm/sheet_aiagenttask.png
capture_quality: legible
capture_width_px: 1600
---

## What the file shows

The IBM Community post "Introducing the BAMOE Gen AI Task for workflows" (23 September 2025), whose
animation records the Gen AI Task being dragged out of the palette's AI group and dropped on the
canvas, next to the hiring process the editor already has open.

The capture (frame 214 of the animation's 215 frames, upscaled 2x) shows the whole screen: palette
with the AI group, the hiring process on the canvas, the freshly dropped **Gen AI Task** node
(sparkle) below the process, and the node's panel with its AI fields still empty.

## Observations

- **The dropped node is not connected to the process in this capture.** It sits on the canvas below
  the hiring process with no sequence flow reaching it. So this artefact shows the AI node *type*
  and its panel being introduced, not the AI step executing inside the control flow.
- The same hiring process appears in this source in three states, and the comparison is the most
  useful thing in the record: here "Create Offer" is an ordinary task with no AI marker and the Gen
  AI Task sits beside the process, unconnected (row 133); in the 9.3.0 announcement (row 119,
  record 004) the task **"Create Offer" itself carries the sparkle** and its panel is filled with
  watsonx / granite / 0.7 / 500 and the offer-letter prompt; in the 9.2.0 deck slide (record 009)
  that position holds two plain tasks, "Generate base Offer" and "Log Offer", with no AI anywhere.
- The palette panel is open in the same frame as the canvas, which is why this capture is the one
  that shows the AI group and a process diagram together.

## Notes for the researcher

- The verdict is INCLUDE because an AI node type of the BPMN editor sits on a BPMN 2.0 canvas, in a
  figure published by the vendor as the introduction of that node. If your artefact criterion
  requires the AI element to be *wired into* the process, this row and row 132 (record 006) are the
  two that would fail it - both drop the node on the canvas without a sequence flow - while rows
  119, 120, 134 and 135 (records 004, 005, 008, 009) pass it. That distinction is recorded here so
  the call can be made without reopening the images.
- The frames are small (800x404 in the source GIF); the 2x upscale used as the capture is legible
  for the panel labels and the process labels, which is what the record quotes.
- The post's other five figures were screened on the contact sheet as further dialog captures (the
  provider list, the VS Code sign-in, the data mapping and the model list); the capture and the GIF
  are the artefacts this record rests on.
