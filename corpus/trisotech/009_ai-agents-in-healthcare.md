# AI Agents You Can Actually Trust in Healthcare: From Opaque to Governed Automation (webinar recording) — UNCERTAIN (trisotech)

url: https://www.trisotech.com/ai-agents-in-healthcare/
accessed: 2026-09-25
title: AI Agents You Can Actually Trust in Healthcare: From Opaque to Governed Automation (webinar recording)
record: 009

bpmn_evidence:
  The artefact is inside the recording, and it was watched end to end this session (105 canvas
  frames on an 18 s grid over the 1883 s runtime; the 44 frames the capture flagged as slide
  transitions were viewed at full size). The recording's BPMN content is one real BPMN 2.0 process,
  "Initial Anemia Assessment (STP)", shown in the vendor's Workflow Modeller: start event "Evaluate
  for anemia", the task "Clinical Examination", the business-rule task "WHO Anemia Grades" (DMN
  table marker and protected-information padlock), the exclusive gateway "Anemia severity none?",
  the business-rule task "Classification of Anemia using MCV and RDW" (same two markers), end events
  "Workup Anemia Subtype" and "No anemia", and seven data objects (Anemia Severity, Age in Years,
  Sex Status, Hemoglobin in g per dL, Patient RDW in Percent, RDW Upper Limit of Normal, Type of
  Anemia) with their data associations. The diagram is captured whole at
  009_ai-agents-in-healthcare-anemia-process-bpmn.png, and a 4x zoom of both business-rule tasks
  shows only the DMN table and padlock markers - no AI marker of any kind.
  The same model is then shown in the vendor's Service Library as "Initial Anemia Assessment (MCP)",
  Service Type "Agent", Source "Trisotech", Tags "Agent; MCP", with a "Chat with service" control
  (captured at 009_ai-agents-in-healthcare-service-type-agent.png), and the model is driven from a
  Microsoft Copilot Studio agent ("GPT-5 Chat") in the second half of the demo.
  The page also publishes the video's poster frame (009_ai-agents-in-healthcare-poster-frame.png),
  which carries no diagram.

ai_evidence:
  "Using BPM+ standards, orchestration, decisions, and AI capabilities are kept separate."
  The AI that the recording demonstrates is real but sits outside the diagram: the process is
  packaged as a service of type "Agent" tagged MCP and invoked over MCP by an external LLM agent,
  and the agent's answer in the test chat is quoted on screen ("The anemia assessment yielded the
  following: ..."). No AI task, AI performer badge or LLM binding is drawn inside the BPMN process
  itself, which is the point the talk is making ("The barrier isn't capability, it's reliability and
  governance").

screenshot: 009_ai-agents-in-healthcare-anemia-process-bpmn.png, 009_ai-agents-in-healthcare-service-type-agent.png, 009_ai-agents-in-healthcare-poster-frame.png
capture_quality: legible

question for the researcher (needs_human_ruling):
  Does a BPMN model registered as a service of type "Agent" (tags "Agent; MCP") and invoked over
  MCP by an external LLM agent (here Microsoft Copilot Studio on GPT-5) count as an AI element
  inside the process, when the process diagram itself carries no AI task or AI performer?
  This is the same construct the source publishes as a feature catalogue in record 036 ("Expose
  BPM+ Models as MCP Servers"), here actually wired up.
