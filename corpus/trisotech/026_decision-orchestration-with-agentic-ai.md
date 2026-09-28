# Decision Orchestration with Agentic AI — INCLUDE (trisotech)

url: https://www.trisotech.com/decision-orchestration-with-agentic-ai/
accessed: 2026-09-25
title: Decision Orchestration with Agentic AI — Bruce Silver, read time 7 minutes
record: 026

bpmn_evidence:
  Figure 10 of the post (capture 026_...-figure10-bpmn-user-task.png, 854x866, viewed at full
  size) is a BPMN 2.0 diagram: a start event (thin circle), the user task "Validate Prescription"
  (rounded rectangle carrying the user-task person marker), an end event (thick circle), and the
  data objects "Prescription" and "Meet Criterias" attached by dotted data associations. The page's
  own text names the notation and the element: "In the second use case, a BPMN User task performer,
  normally a person, can be replaced by an agent." and "In this process a human task validates that
  a submitted prescription contains the required elements, again as specified in the task
  Description panel."
  Figure 12 of the same post (capture 026_...-figure12-ai-agent-performer.png, 1874x980, viewed at
  full size) is the Performers Details panel for that same task: an "Add AI Agent" control with
  "OpenAI Agent" selected and the option "Only if the performer of the previous activity can't
  perform this activity". Figure 11 shows the same task's Semantic description panel.

ai_evidence:
  "AI systems that act autonomously with a sense of purpose and adapt in real time are called
  agentic, and Trisotech now supports Agentic AI." and "A human workflow performer can be replaced
  by an automated AI agent. Trisotech calls this 'AI as a performer'." and "The agent must convert
  this prompt into the service inputs."
  The AI element sits inside the modelled process: the BPMN user task of figure 10 is bound to an
  OpenAI agent as its performer in figure 12, and the page's prose says exactly that. Distinct from
  the page's other AI mentions, which concern AI *generating* or *invoking* services
  ("Any Trisotech decision or process service can be discovered and executed by an AI agent",
  "Agent using deterministic tools"), not AI tasks inside a process diagram.

other figures on the page (not the artefact, recorded for completeness):
  figures 1-8 and 13 are the Azure Copilot / Copilot Studio tool screenshots and the MCP endpoint
  list; figure 2 is a DMN decision requirements diagram (decision "Determine BMI Category", input
  data Height/Weight, BKM "Determine English System Body Mass Index BMI"); figure 3 is a DMN
  decision table; figures 9 ("AI Agent Performing a BPM+ User Task") and 10's companion are
  architecture box diagrams. Only figure 10 is a BPMN diagram.

screenshot: 026_decision-orchestration-agentic-ai-figure10-bpmn-user-task.png
capture_quality: legible

note for the researcher:
  The AI binding is not drawn inside the BPMN diagram itself: figure 10 shows the user task, and
  figure 12 (the modeller's performer panel for that task) shows the OpenAI agent. Both are figures
  of the same post, and the page prose states the substitution, so the AI element inside the
  process is documented rather than inferred. This is the clearest published instance found in this
  source of an AI agent bound to a BPMN user task.
