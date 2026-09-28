---
n: 110
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: bpmn.ai: Orchestrate AI Services in Business Processes
url: https://camunda.com/blog/2020/11/bpmn-ai-process-patterns-to-orchestrate-your-ai-services-in-business-processes/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: the captured figure is a BPMN process diagram, read at full width - a start event, the two tasks "Entity Extraction" and "Process classifier" (the latter drawn with a cog icon), an exclusive gateway with an X marker, two sub-processes drawn as rounded boxes with a collapse marker labelled "Process Y" and "Process X", a second exclusive gateway with an X marker, and an end event
bpmn_evidence_quote: "In this way, an XOR gateway can be used to control automation levels."
ai_evidence: the task "Process classifier" is the AI classification step the page describes - "An example: In input management an AI classifies incoming business documents and forwards them to the responsible processes." - and the captured figure shows exactly that shape: the classifier task feeding an exclusive gateway that routes to the two downstream processes "Process Y" and "Process X"
ai_evidence_quote: An example: In input management an AI classifies incoming business documents and forwards them to the responsible processes.
artefacts:
  screenshot: 006_bpmn-ai-process-patterns-to-orchestrate-your-ai-services-in-business-processes.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1400
capture_method: chrome-devtools-mcp page fetch; the figure's cdn.sanity.io URL decoded out of the page's /_next/image proxy, downloaded at w=1400
---

## What the page shows

The post is a catalogue of integration patterns for putting AI services into business
processes, grouped into sections ("Group 1: Getting Started", "Group 4: Multi-Model
Patterns") and framed as something that can serve "as a means of communication between Data
Scientists and Process Owners or Process Automation Specialists". The captured figure is the
pattern drawn as "Process Choice": a linear BPMN model with a start event into the task
"Entity Extraction", then the task "Process classifier" - the one carrying a cog icon -
then an exclusive gateway with an X marker that forks into the two downstream processes
drawn as collapsed rounded boxes labelled "Process Y" and "Process X", which merge again
into a second exclusive gateway and an end event.

The AI element is the classifier task, and the page supplies its example directly: "In input
management an AI classifies incoming business documents and forwards them to the responsible
processes. The machine learning model to accomplish this will learn from the history of
manual classifications and try to classify them in the same way." The routing step after it
is described elsewhere on the page as the control point: "In this way, an XOR gateway can be
used to control automation levels."

## Observations (description only, no interpretation)

- **AI activity - function:** classification of incoming work and routing of it - "An
  example: In input management an AI classifies incoming business documents and forwards
  them to the responsible processes"; the page also describes the AI component as indicating
  its own certainty: "Besides the decision itself, the AI component indicates how confident
  it is with its own decision (Confidence)."
- **AI activity - element type:** a BPMN task inside the process - the captured figure draws
  the AI step as the task "Process classifier" feeding an exclusive gateway; no dedicated AI
  node type and no visible element-template binding are shown.
- **Authority - downstream:** the two processes the classifier selects between, drawn as the
  collapsed sub-process boxes "Process Y" and "Process X" in the captured figure, which the
  page's example calls "the responsible processes".
- **Authority - data:** the page names the training source - "The machine learning model to
  accomplish this will learn from the history of manual classifications" - and describes the
  AI component's output as "the decision itself" plus a "Confidence" value "usually given in
  the value range 0.0 to 1.0"; no variable names are printed in the captured figure.
- **Authority - control:** the exclusive gateway immediately after the classifier, and the
  minimum-confidence threshold the page describes as the automation control - "Minimum
  confidence = 100% – this would be equivalent to a test or pilot operation. The AI component
  operates live on the real data, but will never make a decision autonomously because the
  100% threshold is never reached."
- **Input provenance:** incoming business documents from input management, per the page's
  example; the captured figure shows them arriving through "Entity Extraction" before the
  classifier.
- **Guards present:** a confidence threshold rather than a human gate - "Minimum confidence =
  0.00% – The AI always decides autonomously, even if uncertainties are clear. Often, this is
  not a reasonable configuration."; the page also describes the related pattern in which "a
  machine learning component is always called before a human decision".
- **Prompt / model detail visible:** not visible on the page - no model name, prompt text or
  parameter is printed; the page stays at the level of confidence thresholds and pattern
  descriptions.

## Notes for the researcher

This is a pre-LLM (2020) pattern catalogue for machine-learning services rather than for
generative AI, which makes it a different flavour of AI-in-process evidence from the later
posts in this source. The page carries at least nine figures ("Drift Detection", "Controlled
Confidence", "GDPR Consent", "Anomaly Detection First", "DMN as runtime", "Ensemble",
"Anomaly Detection last", "Decision Support - AI first"); only the "Process Choice" figure
is captured here. The source asset is 2163x666 and the w=1400 download is a downscale to
1400x431, so the labels are sharp.
