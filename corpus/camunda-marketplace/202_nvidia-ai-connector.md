---
n: 202
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: NVIDIA AI Connector
url: https://marketplace.camunda.com/apps/795294/nvidia-ai-connector
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: A Camunda Modeler capture: none start event -> serviceTask 'Nvidia ai connector' (selected) -> none end event, with the element template's properties panel open on the right: header 'NVIDIA AI CONNECTOR / Nvidia ai connector', template state 'Applied', and the fields Authentication, Payload (Model, Prompt, Input prompt for the model) and Response mapping (Result Variable). No .bpmn is downloadable.
bpmn_evidence_quote: "NVIDIA AI CONNECTOR"
ai_evidence: The task's element template is named 'NVIDIA AI CONNECTOR' and its description reads 'Execute AI-driven task completions using NVIDIA AI models for automated processes'; the panel binds a model ('Select the Model: DeepSeek V3.2'), a prompt ('What is camunda 8') and a result variable ('notificationResult'). The page's own copy: 'seamless integration of NVIDIA AI chat and completion APIs into Camunda-based business processes' and 'dynamically invoke multiple AI models directly from BPMN process models'. Tags: 'AI Services', 'Agentic AI orchestration'.
ai_evidence_quote: "seamless integration of NVIDIA AI chat and completion APIs into Camunda-based business processes"
artefacts:
  screenshot: 202_nvidia-ai-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1100
capture_method: curl of the listing's own asset (d3bql97l1ytoxn.cloudfront.net, app_resources/795294/overview/img4124654465262150472-2x.png, 1100x425); native read at full size - a Camunda Modeler canvas with the task's properties panel open
---

## What the page shows

The NVIDIA AI Connector (community connector by Aakash Chaudhari). One model call in place: a chat/completion request to an NVIDIA-hosted model whose name and prompt are set in the element template and whose answer is mapped to a process variable.

## Observations (description only, no interpretation)

- **AI activity - function:** a chat/completion call - the process sends a prompt to a named model and stores the answer in a variable.
- **AI activity - element type:** one serviceTask bound to the 'NVIDIA AI CONNECTOR' element template; no agent element and no container.
- **Authority - downstream:** the response is mapped to a process variable ('notificationResult'), i.e. the model's output becomes process data available to later steps.
- **Authority - data:** the prompt field holds the text sent to the model; the panel shows no retrieval source, no context documents and no tool binding.
- **Authority - control:** none - no gateway or threshold is drawn.
- **Authority - control (human):** none drawn; the single task sits between a start and an end event.
- **Input provenance:** the prompt typed into the template ('What is camunda 8'), i.e. a static, modeler-authored prompt rather than data from an upstream step.
- **Guards present:** none shown.
- **Prompt / model detail visible:** fully visible - the template's Payload section shows the model selection ('Select the Model: DeepSeek V3.2'), the prompt ('What is camunda 8'), and the response mapping to 'notificationResult'; the panel's authentication field is populated in the capture (value not transcribed).

## Notes for the researcher

The clearest model binding in this batch: the element template is named after AI, the model is chosen in a dropdown and the prompt is written in the panel, so the AI element is not a matter of inference. Compare n=097 (OpenAI GPT-4 extraction task) for the same 'binding visible in the properties panel' evidence class.
