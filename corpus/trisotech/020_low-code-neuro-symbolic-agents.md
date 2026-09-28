# DecisionCAMP 2023: "Low Code Neuro-Symbolic Agents" (webinar recording) — UNCERTAIN (trisotech)

url: https://www.trisotech.com/low-code-neuro-symbolic-agents/
accessed: 2026-09-25
title: DecisionCAMP 2023: "Low Code Neuro-Symbolic Agents" (webinar recording)
record: 020
Row status: UNCERTAIN + needs_visual_check - the artefact sits inside a recording, and the operator ruled on 2026-09-26 that recordings are not an admissible evidence source (note the video was inspected earlier the same day, before that ruling). The captures below stay as evidence for the human visual check.

bpmn_evidence:
  The recording was watched end to end this session (109 canvas frames on a 34 s grid over the
  3689 s runtime; all 73 frames the capture flagged as screen changes were viewed as four contact
  sheets, and the demonstration screens were then read at full frame and zoomed 5x).
  The talk is Denis Gagné's DecisionCAMP 2023 presentation "Low Code Neuro-Symbolic Agents -
  Prompt Engineering through Process and Decision Orchestration", and it demonstrates a real BPMN
  model live in the vendor's modeller (captured at
  020_low-code-neuro-symbolic-agents-bpmn-structured-prompt-model.png).
  The modeller screen (t = 2414 s) shows the browser at "demo.trisotech.com/modeler/bpmmmodeler/#"
  with the ribbon tab "Workflow Modeler" (FILE / HOME / VIEW / BPMN / IMPORT-EXPORT / EXECUTION /
  TEAMWORK / SIMULATION / ANIMATOR / LEARN), the Shapes panel listing "BPMN (Basic)", "BPMN
  (Advanced)" and "Workflow Patterns" with Task, Sub-Process, Expanded Sub-Process, Start Event,
  Exclusive Gateway, Intermediate Event, End Event, Sequence Flow, Message Flow, Association, Data
  Association, Data Object Reference, Data Store Reference, Group, Annotation, Image, Knowledge
  Source, Pool and Lane, and the breadcrumb "Examples Conferences > DecisionCamp2023 >
  Presentation Examples > Structured Prompt" beside the model tab "Structured Prompt P... -
  Workflow".
  The model drawn in it is BPMN 2.0 (read at 5x in
  raw/video/low-code-neuro-symbolic-agents/z_tasks.png): a start event -> the task "Structured
  Prompt" (carrying the business-rule / decision-table marker and the protected-information padlock
  marker) -> the task "Creates a completion for the provided prompt and parameters" -> the end
  event, with the data objects "Role", "Task", "Tone", "State", "Format", "Length", "User Input",
  "Prompt" and "Completion" feeding the tasks and produced by them on dotted data associations
  (the "Prompt" object flows into the second task, the "Completion" object out of it).
  The recording then executes both models as generated applications of the same suite: the
  browser at "demo.trisotech.com/execution/bpmm/form/genai/bpmm/structured-prompt" (t = 2448 s)
  renders the "Structured Prompt" workflow as a form with the fields User Input ("Why did the
  chicken cross the..."), Role, Tone, Task, Format, Style and Length and a SUBMIT button, and the
  browser at "demo.trisotech.com/execution/bpmm/form/genai/bpmm/sentiment-analysis-minute-app"
  (t = 2278 s) renders another of the suite's GenAI applications, showing "Results: Positive".
  The rest of the talk is slide material, not models: the AI taxonomy slides ("The main approaches
  to AI", "Symbolic AI" vs "Sub-Symbolic AI", "Symbolic and Sub-Symbolic AI Characteristics"), the
  Generative-AI teaching slides (ChatGPT Revelation, Advent of Generative AI, LLMs, GPT-3/GPT-4
  parameter counts, Prompt Completion, Foundation Models Main Settings, tokens / temperature / top
  p, hallucination), the prompt-engineering slides, and the illustration drawings "GenAI
  Orchestration", "Structured Prompt Completion" (User -> the Foundation Model -> Completion),
  "Retrieval Augmented Generation (RAG)", "Chatbot Orchestration", "Agent Orchestration" and
  "Co-Pilot", whose boxes are teaching pictures built out of rounded boxes and arrows rather than
  models (no events, no pools, no gateways).

ai_evidence:
  The AI step is drawn inside the process as a task: "Creates a completion for the provided prompt
  and parameters" is the LLM completion call itself (its wording is the completion endpoint's own
  description), it is fed by the data object "Prompt" and produces "Completion", it is preceded by
  the business-rule task "Structured Prompt" that assembles the prompt from Role / Task / Tone /
  State / Format / Length / User Input, and its top-left corner carries a small badge that is
  neither the business-rule marker nor the padlock (read at 5x: a robot/AI glyph). The talk's own
  slides state the construct: "Reusable GenAI Components - Structured Prompt Generator ...
  Narrative Generator ... Text Summarization ... Text Transformation ... Text Translation ... Text
  Generation ... Image Generation", "GenAI Feature Set Exploration - Neuro-Symbolic AI: the
  building blocks of prompt orchestration", and "Co-Pilot - I like the term co-pilot as it implies
  human control: the essence of engineered GenAI prompt orchestration is that we can add
  validation and business logic as a wrapper to ensure desired behavior."
  The page frames the same construct: "This presentation aims to provide a comprehensive
  understanding of a form of neuro-symbolic AI, prompt engineering, and the role of process and
  decision orchestration in achieving optimal outcomes."

screenshot: 020_low-code-neuro-symbolic-agents-bpmn-structured-prompt-model.png,
  020_low-code-neuro-symbolic-agents-poster-frame.png
capture_quality: legible

note for the researcher:
  Two of the suite's GenAI applications are executed live in the recording (the prompt form and
  the sentiment-analysis form); the model itself is shown in the modeller for the "Structured
  Prompt" workflow, which is the screen captured here. (The later demonstration screens in this
  long recording were not all read at full frame - the ones I read are the executed applications
  and the service panels - so a reviewer wanting the full inventory of models shown should re-watch
  t = 2100-2600 s.) The paired deck of this
  same talk is E1-not-bpmn in this ledger (row 444, "No BPMN 2.0 process diagram is published" in
  its 55 slides), so this row is not an E3 duplicate of it: what the recording adds is the live
  modeller and the executed applications, the same medium relationship this source already treats
  as two publications (records 005/027, 015/029).
