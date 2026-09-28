# The Role of GenAI — INCLUDE (trisotech)

url: https://www.trisotech.com/the-role-of-genai-presentation/
accessed: 2026-09-25
title: The Role of GenAI (presentation deck, 27 slides)
record: 028

bpmn_evidence:
  Slide 24 ("Using BPMN for Effective Prompt Management") publishes what the slide itself calls a
  "Notional BPMN Diagram to ease understanding", viewed at full size (2048x1152): a start event
  "Execute Prompt", the user tasks "Entry Prompts", "Build EE by Topic Prompt", "Prompt Execution",
  "Decide Output from Prompt Output" and "Assign String to Object" (the latter inside the loop the
  slide labels "Stress test loop"), exclusive gateways, an end event "Prompt Execution Results", and
  the data objects "Prompt", "Free Text", "Prompt Type", "Prompt Output", "Prompt Result",
  "EE Prompt Object" and "Prompt Datastore" (drawn with the database icon) attached by dotted data
  associations.

ai_evidence:
  The generative-AI element is inside the modelled process: the task "Prompt Execution" and the two
  "...Prompt" build tasks are the steps that call the model, and the slide's own bullets name it -
  "The interactions between the prompt and the LLM is complex", "Store prompts in datastores",
  "Consider provisions for stress testing prompts". The deck's framing sentence on the same slide is
  "Using BPMN for Effective Prompt Management".
  Elsewhere in the deck the AI mentions are about the LLM as an artefact of prompt engineering
  ("The new wave of Large Language Models (LLMs) research has offered new and enhanced language
  capabilities"), not about a task in a process.

screenshot: 028_the-role-of-genai-bpmn-prompt-management.png
capture_quality: legible

note for the researcher:
  The slide calls its own model "notional", so the diagram is illustrative rather than a deployed
  process - it is nevertheless a BPMN task set with the prompt-execution step inside it, which is
  what the criteria ask for. The prompt-management loop (build prompt, execute, decide output,
  re-enter) is the interesting part: it models prompt engineering itself as a process.
