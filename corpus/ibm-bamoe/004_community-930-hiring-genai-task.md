---
n: 119
record: 004
url: https://community.ibm.com/community/user/blogs/phil-simpson/2025/09/25/announcing-ibm-business-automation-manager-open-ed
source: ibm-bamoe
surface: community:ibm.com
accessed: 2026-09-25
verdict: INCLUDE
needs_human_ruling: false
question:
bpmn_evidence: |
  Figure2 (3292x1358) is a full BAMOE Canvas screenshot with the watermark "BPMN 2.0" readable
  under the canvas, showing a complete hiring process: a start event, the user task "New Hiring",
  "Create Offer" (carrying the AI sparkle), the user tasks "HR Interview" and "IT Interview" (both
  with timer boundary events), "Send Offer to Candidate", "Send notification HR Interview avoided"
  and "Application denied", the exclusive gateways between them, a sequence-flow label "Candidate
  doesn't meet requirements", and end events. The task boundaries, sequence flows, gateway crosses
  and timer overlays are the notation evidence; the watermark is the editor's own statement of the
  notation.
ai_evidence: |
  "Create Offer" is a Gen AI task - the sparkle in its top-left corner - and the same screenshot has
  its property panel open on the right: "AI Provider" watsonx, "Model" ibm/granite-3-2b-instruct,
  "Temperature" 0.7, "Token Limit" 500, and a prompt over the process variables {{candidate}},
  {{category}}, {{baseSalary}} and {{bonus}} that ends "welcoming message to IBM, Armonk."
artefacts:
  - screenshot: 004_ibm-bamoe-930-hiring-genai-task.png
  - file: ledgers/_bamoe_comm/figs/p930__n5lTaIudTQCCXzwCOGW0_Figure2.png
  - file: ledgers/_bamoe_comm/figs/p930__f6ypPRhSQpG7MTFEd04K_Figure3.png
capture_quality: legible
capture_width_px: 3292
---

## What the file shows

The IBM Community blog post announcing BAMOE 9.3.0, whose second figure is the hiring process in
BAMOE Canvas with the Gen AI task "Create Offer" selected and its AI panel open.

Process, as legible in the capture: start event → user task **"New Hiring"** → exclusive gateway
→ **"Create Offer" (Gen AI task, the sparkle in its corner)** → user task "HR Interview" with a
timer boundary event → user task "IT Interview" with a timer boundary event → exclusive gateway →
"Send Offer to Candidate" service task → end event. From the first gateway a long sequence flow
labelled **"Candidate doesn't meet requirements"** runs down to a second exclusive gateway; the
HR Interview timer boundary leads through another gateway to the service task "Send notification HR
Interview avoided", and both that task and the IT Interview timer boundary lead into the same lower
gateway, which continues to "Application denied" → end event. The canvas watermark reads
**"BPMN 2.0"** and the editor footer "React Flow".

Panel, as legible in the capture: the selected node "Create Offer" with the sparkle, AI Provider
`watsonx`, Model `ibm/granite-3-2b-instruct`, Temperature `0.7`, Token Limit `500`, and the prompt:
"Generate an Offer letter to {{candidate}} specifying his position as {{category}}, his base salary
as {{baseSalary}}, and a bonus with the value of {{bonus}}. Format the value in the table, using $
for the salary and bonus. Conclude the letter with a congratulations and welcoming message to IBM,
Armonk." Below it the panel notes "This prompt includes a system message that helps guide the
response."

## Observations

- The AI element is *inside the process*: the sparkle-bearing node is one of the process's tasks,
  with sequence flows on both sides, so the AI is a step of the workflow rather than a tool that
  draws it.
- The same post's Figure3 is an MCP architecture box diagram (AI agents → BAMOE MCP Server →
  business services), not BPMN; it is kept with the record as the second artefact but is not the
  reason for the verdict.
- **Cross-reference worth keeping**: the TechXchange deck in record 009 shows the *same* hiring
  process at version 9.2.0 with two ordinary tasks in that position - "Generate base Offer" and
  "Log Offer" - and no AI element anywhere in the diagram. The 9.3.0 capture here shows the same
  process with a single Gen AI task "Create Offer" carrying the sparkle and the watsonx binding.
  That pairing is the corpus's clearest before/after of an AI node entering an existing process.
  (The two captures are different diagrams and are not duplicates of one another.)

## Notes for the researcher

- Figure2 is high-resolution (3292x1358) and legible; the panel text was read at full size, so the
  model name and the sampling settings are quoted from the pixels, not from the post's prose.
- The post is the 9.3.0 announcement; the two community posts that carry the *same* hiring process
  in other states are row 133 (lugli, record 007) and, for the pre-AI form, the deck page described
  in record 009. They were kept as separate rows: the captures differ in panel state and in which
  AI node type is shown, so they are similar-but-different, not duplicates.
