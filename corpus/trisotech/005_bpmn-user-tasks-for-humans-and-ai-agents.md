# BPMN User Tasks for Humans and AI Agents (webinar recording) — UNCERTAIN (trisotech)

url: https://www.trisotech.com/bpmn-user-tasks-for-humans-and-ai-agents/
accessed: 2026-09-25
title: BPMN User Tasks for Humans and AI Agents (webinar recording)
record: 005
Row status: UNCERTAIN + needs_visual_check - the artefact sits inside a recording, and the operator ruled on 2026-09-26 that recordings are not an admissible evidence source (note the video was inspected earlier the same day, before that ruling). The captures below stay as evidence for the human visual check.

bpmn_evidence:
  The artefact is inside the recording, and the recording was watched end to end this session
  (106 canvas frames on an 18 s grid over the 1892 s runtime; all 50 frames the capture flagged as
  screen changes were viewed at full size). The recording is a live demonstration in the vendor's
  Workflow Modeller, whose own Shaper panel reads "BPMN 2.0 (Basic) / BPMN 2.0 (Advanced) /
  Workflow Patterns" and whose ribbon carries FILE / HOME / VIEW / BPMN / IMPORT-EXPORT /
  EXECUTION / TEAMWORK / SIMULATION / ANIMATOR / LEARN. Five models are built and run, all BPMN
  2.0: "Demo 1: Task Assignment", "Demo 2: Attended task", "Demo 3: Gated Review", "Demo 4:
  Dynamic Supervision", "Demo 5: Unsupervised".
  Demo 3 ("Supervision via branching; only borderline cases routed to a human", captured at
  005_...-demo3-gated-review.png): start event, user task "Evaluate Appraisal Quality", exclusive
  gateways on the appraisal score ("Between 5 and", ">8", "<6"), the user task "Manual Review",
  the gateway "Approved?", the end events "Appraisal Approved" and "Appraisal Rejected", and the
  data objects "House Appraisal", "Appraisal Quality", "Appraisal Quality (reviewed)", "Manual
  Approval" attached by dotted data associations.
  Demo 4 ("Next best action decided by human", captured at 005_...-demo4-dynamic-supervision.png,
  and in the deck at record 027): start event, the user tasks "Evaluate Appraisal Quality",
  "Determine Next Available Actions" (business-rule task, table marker plus the
  protected-information padlock), "Manual Review", "Senior Review", the exclusive gateways
  ("No"/"Yes", "Next action", "Request more comparable", "Escalate"), the end events "Appraisal
  Approved", "Request more comparables", "Appraisal Rejected", and the data objects "House
  Appraisal", "Appraisal Quality", "Next Available Actions", "Next Action".
  The modeller's own dialogs are shown: the task Data Mapping dialog for "Manual Review" (Input
  Mapping / Output Mapping, Context (input data Associations) = House Appraisal, Appraisal
  Quality, Next Available Actions, and a Mapping table of inner data inputs to mapping
  expressions), and the runtime Execution form of the appraisal process (the appraisal record -
  address, square footage, comparable sales with value adjustments, appraiser comments).

ai_evidence:
  The AI element is drawn inside the BPMN process. The user task "Evaluate Appraisal Quality"
  carries a blue performer badge under the task reading "AI Reviewer" with a count of 1 (zoomed
  from the Video at 12x: 005_...-ai-reviewer-badge-zoom.png) - the task's performer is an AI agent,
  in the same model where the sibling tasks "Manual Review", "Senior Review" and "Collateral R..."
  carry performer badges naming human roles. The demo slides of the same talk name the construct
  in the vendor's words: "patterns for orchestrating work across both human and AI performers",
  and Demo 5 is titled "Unsupervised Autonomous AI Performer" (record 027).
  The talk's own slides (read from the recording, not from the page text) frame it as
  coordination, not capability: "Without coordination, AI agents can recreate the same problems as
  unstructured work", and the closing slide reads "The goal is not simply to automate tasks with
  AI - The goal is to keep work coordinated, intelligible and governed: performer assignment, task
  interaction, review points, routing logic, human responsibility". The page's own C1 sentence is
  the one quoted in the ledger row: "Modern workflow applications can assign tasks to humans, AI
  agents, or AI agents operating under human supervision within the same orchestrated process."

screenshot: 005_bpmn-user-tasks-for-humans-and-ai-agents-demo4-dynamic-supervision.png,
  005_bpmn-user-tasks-for-humans-and-ai-agents-demo3-gated-review.png,
  005_bpmn-user-tasks-for-humans-and-ai-agents-ai-reviewer-badge-zoom.png
capture_quality: legible

note for the researcher:
  This is the recording of the talk whose deck is record 027 (INCLUDE, with the same "AI Reviewer"
  badge on the same two demo models). The video is not an E3 duplicate of the deck: it publishes
  the models live in the modeller - five demos, the data-mapping dialog, the AI-performer
  assignment and the runtime execution form -, where the deck publishes two exported model slides.
  The source's anchor page for C1/C2 is this same page, and its abstract carries the C1 evidence
  quoted in the assignment file.
