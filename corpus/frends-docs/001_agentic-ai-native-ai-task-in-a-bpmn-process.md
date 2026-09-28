---
n: 2
source: frends-docs
source_name: Frends documentation (docs.frends.com)
title: "Agentic AI"
url: https://docs.frends.com/frends-development/agentic-ai
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
needs_visual_check: false
bpmn_evidence: "The figure is a capture of the Frends Process Editor canvas, and what the canvas draws is BPMN 2.0 notation: a start event circle, rounded activity boxes, an XOR gateway diamond with a labelled outgoing branch, a timer intermediate event on the process border, dashed subprocess containers, error end events, and arrowed sequence flows between them. The vendor documents the notation itself on its Process shape reference page, opened 2026-09-26: “Enables exporting the BPMN diagram for the Frends Process in XML format.” and “exporting and importing Frends Processes is not done through BPMN diagram files. Exporting and importing Frends Processes uses instead a proprietary JSON format file to include both the BPMN diagram as well as related C# code” - i.e. the diagram is BPMN, the Frends-specific configuration is not. No BPMN XML is offered on the page, so the notation call rests on the drawing and on the vendor's own naming of it."
bpmn_evidence_quote: "BPMN 2.0 with AI Connector enables AI Orchestrations."
ai_evidence: "The AI element sits inside the drawn process, not beside it: the diagram's lower-left legend names the 'Native AI Task' shape and the page's caption for this figure is “AI operates as part of your Processes, not replacing them.” The page text says verbatim that “Frends Agentic AI enables AI to take action within your Processes rather than simply producing output for a predetermined BPMN flow to work on”, and that “The Process remains the outer structure, controlling when the agentic step runs, what data it receives, and what happens with the result.” The second capture shows the same shape's configuration surface: a User Prompt block and a Frends system prompt."
ai_evidence_quote: "Frends Agentic AI enables AI to take action within your Processes rather than simply producing output for a predetermined BPMN flow to work on."
artefacts:
  screenshot: 001_invoice-exception-process-with-native-ai-task.png
  assets: [001_invoice-exception-process-with-native-ai-task.png, 001_ai-connector-shape-in-the-process-editor.png]
  bpmn_xml: []
  archive: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: "figure fetched from its native asset URL on the Frends documentation site and opened at full size on 2026-09-26"
judgment: true
---

## What the artefact is

`https://docs.frends.com/frends-development/agentic-ai` (ledger row n=2), figure asset `/spaces/QI65mBosbdweu563CvPI/uploads/y4Liqx9b4yO91TpxLZlA/image.png`.

## What the figure shows

the Frends Process Editor canvas holding a full BPMN 2.0 diagram (start event, XOR gateways, a timer intermediate event, subprocess containers, error and end events) with the Native AI Task shape inside the process (001_invoice-exception-process-with-native-ai-task.png); the AI Connector shape on the editor canvas with its User Prompt and System prompts panel open (001_ai-connector-shape-in-the-process-editor.png)

## bpmn_evidence

The figure is a capture of the Frends Process Editor canvas, and what the canvas draws is BPMN 2.0 notation: a start event circle, rounded activity boxes, an XOR gateway diamond with a labelled outgoing branch, a timer intermediate event on the process border, dashed subprocess containers, error end events, and arrowed sequence flows between them. The vendor documents the notation itself on its Process shape reference page, opened 2026-09-26: “Enables exporting the BPMN diagram for the Frends Process in XML format.” and “exporting and importing Frends Processes is not done through BPMN diagram files. Exporting and importing Frends Processes uses instead a proprietary JSON format file to include both the BPMN diagram as well as related C# code” - i.e. the diagram is BPMN, the Frends-specific configuration is not. No BPMN XML is offered on the page, so the notation call rests on the drawing and on the vendor's own naming of it.

## ai_evidence

The AI element sits inside the drawn process, not beside it: the diagram's lower-left legend names the 'Native AI Task' shape and the page's caption for this figure is “AI operates as part of your Processes, not replacing them.” The page text says verbatim that “Frends Agentic AI enables AI to take action within your Processes rather than simply producing output for a predetermined BPMN flow to work on”, and that “The Process remains the outer structure, controlling when the agentic step runs, what data it receives, and what happens with the result.” The second capture shows the same shape's configuration surface: a User Prompt block and a Frends system prompt.

## Notes for the researcher

- The page also states the limit of the pattern and it matters for the corpus: “When the decision logic is variable enough that encoding it as explicit BPMN branches becomes impractical, the Agentic AI approach allows the Process to define a goal and a set of permitted tools instead.” The AI step therefore replaces modelled branching inside an otherwise modelled process - an AI element inside a BPMN artefact, which is what this source was collected for.
- Two further figures on the page (“AI Connector with MCP Tools enabled.” and “MCP Trigger in action.”) are the same canvas with MCP tool configuration open; they are recorded as captures of the shape's MCP surface, not as separate records.
- Verdict INCLUDE, no hesitation: the notation is BPMN 2.0 by the vendor's own account, and the AI element is a shape inside the process diagram.
