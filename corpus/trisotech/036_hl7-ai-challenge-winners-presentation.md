# HL7 AI Challenge Winners — UNCERTAIN (trisotech)

url: https://www.trisotech.com/hl7-ai-challenge-winners-presentation/
accessed: 2026-09-25
title: Unleashing Innovation: HL7 AI Challenge Winners (presentation deck, 10 slides)
record: 036

bpmn_evidence:
  Slide 7 ("Some Trisotech AI Features") draws three task boxes in the vendor's BPMN task shape,
  viewed at full size (2048x1152): "REST call to an LLM" carrying the gear marker (service task) and
  the OpenAI swirl, "A user Task" carrying a person/agent marker, and an LLM "brain" icon wired by
  an "MCP" connector to a dashed BPM+ box holding the DMN, BPMN and CMMN model icons. The three
  features are labelled "REST Call to an LLM", "Agent as Performer" and "Expose BPM+ Models as MCP
  Servers".
  The shapes are BPMN task shapes, but the slide is a capability listing: the boxes carry no sequence
  flows, no start or end event, and the red curved arrows on them are annotations.
  Slide 3 is an architecture/icon drawing (Clinician and AI icons above the HL7 BPM Community of
  Practice logo, the Workflow/Case/Decision model icons and the CDS Hooks / SMART / FHIR Server
  boxes). The remaining eight slides are text.

ai_evidence:
  Both AI elements are named on the slide itself: "REST call to an LLM" (with "Call any LLM API of
  your choice with mappings in and out of the task" underneath) and "Agent as Performer" (with "Agent
  is provided with task description, Inputs and expected outputs"). Slide 2 states the deck's claim:
  "BPM+ Determinism and HL7 Integration for AI Agents - Use the same Clinical Pathways and Clinical
  Decision Support for both Clinicians and AI".
  The uncertainty: the LLM/agent bindings are drawn onto BPMN task shapes but outside any process
  flow, and the deck never publishes the clinical pathway itself.

screenshot: 036_hl7-ai-challenge-winners-agent-as-performer-features.png
capture_quality: legible

note for the researcher:
  needs_visual_check and needs_human_ruling. This is the vendor's own catalogue of the AI bindings
  available on a BPMN task ("REST call to an LLM", "Agent as Performer", "Expose BPM+ Models as MCP
  Servers"), drawn with task shapes but with no process around them - a feature scaffold rather than
  a modelled process. It is worth the ruling for exactly that reason: it fixes whether the binding
  catalogue alone, without a surrounding process, qualifies, and it is the same construct that
  appears bound inside a real process in records 026 and 027.
