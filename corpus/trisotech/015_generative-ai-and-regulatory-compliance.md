# Generative AI and Regulatory Compliance (webinar recording) — UNCERTAIN (trisotech)

url: https://www.trisotech.com/generative-ai-and-regulatory-compliance/
accessed: 2026-09-25
title: Generative AI and Regulatory Compliance (webinar recording)
record: 015
Row status: UNCERTAIN + needs_visual_check - the artefact sits inside a recording, and the operator ruled on 2026-09-26 that recordings are not an admissible evidence source (note the video was inspected earlier the same day, before that ruling). The captures below stay as evidence for the human visual check.

bpmn_evidence:
  The artefact is inside the recording, and the recording was watched end to end this session
  (110 canvas frames on a 32 s grid over the 3507 s runtime; all 94 frames the capture flagged as
  screen changes were viewed as three contact sheets, and the model was then read at 2x and 8x).
  The talk is Dennis Gagné's / Tom DeBevoise's DecisionCAMP 2023 "Prompt Engineering for Laws and
  Regulations", presented live from a shared desktop whose browser shows the vendor's own modeller
  ("acr.trisotech.com/modeler/dmnmodeller/#", ribbon "Workflow Modeller", panel "Shapes: BPMN 2.0
  (Basic) Elements / BPMN 2.0 (Advanced) Elements / Workflow Patterns").
  The model open in it, named in the modeller's tab bar "Extract Terms from CFR", is BPMN 2.0
  (captured at 015_generative-ai-and-regulatory-compliance-bpmn-prompt-tasks.png): the chain
  start -> task "Initialize" -> task "CFR Text" -> exclusive gateway -> task "Execute Term Prompt"
  -> task "Flatten Term List" -> exclusive gateway -> task "Clear up Term List" -> task "Clean
  Terms" -> intermediate event "Next Definition", and a second chain -> exclusive gateway -> task
  "Plain Prompt" -> task "Make term definition" -> exclusive gateway -> task "Final Term
  Definitions" -> the end event "Term End", with the data objects "Extracts", "terms", "term list",
  "Clean term list", "List count", "Cleaned Term List", "Result", "Term Definitions", "cml" and
  "Definitions" on dotted data associations, and a later canvas showing the same talk's rule tasks
  ("Discount points rule", "Limits on points and fees", "Qualified Mortgage Small creditor",
  "Qualified Mortgage Seasoned Loan", "Mortgage Exception", "Monthly debt-to-income ratio") each
  linked to a knowledge source citing its regulation ("12 CFR 1026.32(b)(1)(i) (E) & (F) Discount
  point rules", "12 CFR 1026.43(e)(5) & (6) Small creditor portfolio loans", "12 CFR 1026.43(c)(2)(vi)
  Monthly debt to income ratio").
  The recording's other material is not BPMN: bullet slides on prompts, KEM and compliance practice,
  the diagram "The compliance challenge", the eCFR page with the regulation text being highlighted
  (t = 2368-2400 s), and a Zoom meeting window.

ai_evidence:
  The generative-AI step is inside the process. The model's own task names are the prompt-execution
  steps of a term-extraction pipeline: "Execute Term Prompt" and "Plain Prompt" (both read at 8x,
  pink-highlighted in the presenter's own colouring, each carrying the modeller's bookmark and
  protected-information markers), feeding "Flatten Term List" and "Make term definition" and
  producing the data objects "terms", "term list", "Term Definitions" and "Definitions".
  The recording shows those prompts being engineered and run against an LLM in the same session:
  the presenter's ChatGPT window (t = 2432 s, chat.openai.com, the GPT-3.5/GPT-4 selector visible, a
  chat list whose entries include "Discount Point Eligibility R..." and "Prompt Two") answers over
  the regulation text with per-rule reasoning that cites "12 CFR 1026.32(b)(1)(i)(F)" and the bona
  fide discount point rule, immediately after the eCFR page for 12 CFR 1026.32 is shown with the
  same paragraphs highlighted (t = 2368-2400 s). Read at contact-sheet resolution, so the ChatGPT
  answer is described rather than quoted verbatim. The deck of the same talk states the construct
  in prose ("Larger Language Models (LLM) are capable
  of the extraction, the terms, the concepts, and the regulations with natural language
  understanding"; "A prompt extracts the vocabulary, concepts, and business rules from the text of
  the regulation").

screenshot: 015_generative-ai-and-regulatory-compliance-bpmn-prompt-tasks.png
capture_quality: legible

note for the researcher:
  This is the recording of the talk whose deck is record 029 (INCLUDE: slide 19, "Term Extraction
  Process"). Not an E3 duplicate of it: the deck publishes an exported slide image of the pipeline,
  the recording publishes the model live in the modeller (toolbars, BPMN 2.0 shapes panel, the model
  in edit state, the prompt-task markers at 8x), the extracted definition text panel, the eCFR page
  it was extracted from, the ChatGPT prompt run, and the rule/knowledge-source canvas - so the
  recording carries the prompt-execution construct with its tooling, which the slide does not.
  Same pattern as record 028 (prompt-management tasks in BPMN) and record 003 (a ChatGPT task in a
  process model).
