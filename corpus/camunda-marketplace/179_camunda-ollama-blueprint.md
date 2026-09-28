---
n: 179
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Camunda + Ollama Blueprint
url: https://marketplace.camunda.com/apps/871406/camunda-ollama-blueprint
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: The page describes an AI-bound BPMN process in detail - a 'Give Prompt to Model' user task, a 'Process the Prompt' service task powered by a custom Ollama outbound connector, and a 'Result' task returning the model's output - and an element template that makes the Ollama task available natively in the BPMN palette, but it publishes no diagram: its only image is the cover slide of a 22-slide deck (byte-identical to the cover published by n=058) and the deck itself is not published. Is a documented AI-bound element template enough to record this listing, or is it E0-no-artefact? Same question as n=058's Ollama connector.
needs_visual_check: false
bpmn_evidence: No BPMN artefact published: the listing's only figure is the cover slide of a deck titled 'Camunda + Local AI with Ollama' (a byte-identical copy of the image published by n=058's Ollama connector listing, md5 710d903dcdcb0f4573a2540ed8a2dffd) and the deck itself is not published; there is no .bpmn link. The page describes the model in prose instead: 'It shows the full path from BPMN process design to a live AI response'.
bpmn_evidence_quote: "It shows the full path from BPMN process design to a live AI response"
ai_evidence: The AI-bound elements are named precisely and never drawn: the page describes 'a "Give Prompt to Model" user task, a "Process the Prompt" service task powered by the custom Ollama outbound connector, and a "Result" task returning the model's output', and it names 'the Camunda Modeler element template that makes the Ollama task available natively in the BPMN palette'. Its benefit list claims 'Use Ollama as a native BPMN task' and 'Swap in any Ollama-supported model'. No diagram, canvas or element template is published on the page.
ai_evidence_quote: "the Camunda Modeler element template that makes the Ollama task available natively in the BPMN palette"
artefacts:
  screenshot: 179_camunda-ollama-blueprint.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own asset (d3bql97l1ytoxn.cloudfront.net, app_resources/871406/overview/img16269040366677534986-2x.png, 1100x618 - the cover slide of the vendor's 22-slide deck, marked '1 / 22') and of its only other image (thumbs_112/img6951609913302434554-2x.png, 230x230); both read natively at full size
---

## What the page shows

A community blueprint for running Camunda with a local Ollama model (Quick Start, tagged 'Host yourself'). The listing explains the process, the Docker Compose setup and the element template in prose and publishes no model.

## Observations (description only, no interpretation)

- **AI activity - function:** a locally running open-weight model answering a prompt from inside the process, per the page's description of the flow.
- **AI activity - element type:** described as a service task powered by a custom Ollama outbound connector, with a companion element template for the Modeler palette; none of it is published.
- **Authority - downstream:** not shown - the described flow ends in a 'Result' task returning the model's output.
- **Authority - data:** not shown.
- **Authority - control:** not shown - the page describes no gateway.
- **Authority - control (human):** the described flow opens with a user task ('Give Prompt to Model'), i.e. a human supplies the prompt; nothing shows what follows the model's answer.
- **Input provenance:** the prompt typed into the user task, per the page's description.
- **Guards present:** none shown.
- **Prompt / model detail visible:** model families only ('llama3.2, mistral, qwen2.5'), in prose; no prompt, temperature or template configuration is published.

## Notes for the researcher

Same shape as n=058 (the Ollama connector), and literally the same cover image: the shared slide is a deck cover, not a diagram, so this is not an E3 duplicate; the two listings describe different deliverables (an element template for a connector vs. an end-to-end blueprint). Recorded UNCERTAIN with a question that mirrors n=058's.
