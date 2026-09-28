---
n: 58
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Ollama Connector
url: https://marketplace.camunda.com/apps/871407/ollama-connector
accessed: 2026-09-26
verdict: UNCERTAIN
needs_human_ruling: true
question: The listing documents an 'Ollama Chat' element template for a Camunda Modeler task but publishes no process diagram: its only image is the cover slide of a 22-slide 'Camunda + Local AI with Ollama' deck, and the deck itself is not published on the page. Is a documented AI-bound element template enough to record this listing, or is it E0-no-artefact?
needs_visual_check: false
bpmn_evidence: No BPMN artefact on the page, and none downloadable. The listing publishes one content image only - the cover slide of an 'ENGINEERING WALKTHROUGH' deck marked '1 / 22' - and no screenshots; its 'Read Documentation' resource is a GitHub README, not a process file.
bpmn_evidence_quote: "ships with a Camunda Modeler element template"
ai_evidence: The AI element is described, not shown: the page says the connector 'sends a prompt from a BPMN process to Ollama's OpenAI-compatible local API' and returns the model's response into the process, that it ships an 'Ollama Chat' element template 'so the task appears natively in the palette', and that it keeps prompts and responses on local infrastructure. No published artefact shows where that task sits in a process.
ai_evidence_quote: "Cloud AI APIs add per-request costs and send prompts outside your infrastructure"
artefacts:
  screenshot: 058_ollama-connector.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: null
capture_method: curl of the listing's own overview asset (d3bql97l1ytoxn.cloudfront.net, overview/img15265190083386916757-2x.png, 1100x618); native read at full size
---

## What the page shows

A community Ollama connector listing (Camunda Services GmbH, 'Host yourself', AI Services tag). The page describes a connector that lets a BPMN process call locally running open-weight models (llama3.2, mistral, qwen2.5, gpt-oss:20b) through Ollama's OpenAI-compatible API on localhost, with endpoint, model name and prompt/output variable mapping configured from the BPMN task, and an installation recipe extending Camunda's official Self-Managed Docker Compose setup. Its published media is the deck cover only.

## Observations (description only, no interpretation)

- **AI activity - function:** send a prompt to a local LLM and return its response into the process; the page also names prompt/response variable mapping.
- **AI activity - element type:** described as an ordinary BPMN task bound to an 'Ollama Chat' element template; not visible - no process is published.
- **Authority - downstream / data / control:** not visible - no process is published.
- **Input provenance:** named as prompts configured on the task; not shown.
- **Guards present:** none shown; the page's selling point is that prompts and responses stay on local infrastructure.
- **Prompt / model detail visible:** the model names are listed (llama3.2, mistral, qwen2.5, gpt-oss:20b) and the endpoint is named (http://localhost:11434/v1); no prompt text is shown.

## Notes for the researcher

Recorded as UNCERTAIN under this source's connector rule: a listing that names an AI-bound element template but publishes no full diagram is neither provable from an image (there is none) nor a description-only listing (the template is named). Capture is the only image the listing publishes - the deck cover - which is not a process artefact. No video is involved, so the operator's video instruction does not apply here.
