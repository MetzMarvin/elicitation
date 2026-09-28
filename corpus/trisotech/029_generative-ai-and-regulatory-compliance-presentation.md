# Generative AI and Regulatory Compliance — INCLUDE (trisotech)

url: https://www.trisotech.com/generative-ai-and-regulatory-compliance-presentation/
accessed: 2026-09-25
title: Prompt Engineering for Laws and Regulations (presentation deck, 28 slides, Tom DeBevoise / Denis Gagné)
record: 029

bpmn_evidence:
  Slide 19 ("Term Extraction Process") is a BPMN 2.0 model, viewed at full size (2048x1152): a start
  event "Terms extraction Start", the tasks "Initialize", "Extract Terms", "Execute Term Prompt"
  (drawn highlighted), "Flatten Term List", "Clean up Term List" and "Clean Terms", a loop back to
  the prompt step annotated "next citation", and the end event "Next Definition". A second chain
  below carries "Print Prompt", "Make term definition", "Final Term Definitions" and "Term End" with
  its own data objects ("Extracts", "terms", "term list", "Clean term list", "List count",
  "Cleaned Term List", "Result", "Term Definitions", "cql", "Definitions").
  The deck's own text names the notation on other slides of the same section ("DMN and other
  Standards", the BPMN/DMN/CMMN comparison) and the slide title names the process.

ai_evidence:
  The generative-AI step is inside the process: the highlighted task "Execute Term Prompt" and its
  sibling "Print Prompt" are the prompt-execution tasks of the term-extraction pipeline, and the deck
  is about prompt engineering over laws and regulations ("Prompt Engineering for Laws and
  Regulations - Extracting Terms, Concepts, and Business Rules with Engineered Prompts"; the deck's
  own bullet "Business rules can be modeled with prompts analysis").
  The AI element is therefore a task in the process, not a passing mention.

screenshot: 029_generative-ai-and-regulatory-compliance-bpmn-term-extraction.png
capture_quality: legible

note for the researcher:
  This is the same prompt-execution-as-a-task pattern as record 028, here applied to legal term
  extraction with an explicit loop over citations. The deck publishes the pipeline twice (slide 19's
  process and a later data-flow view), so both the control flow and the data objects are visible.
