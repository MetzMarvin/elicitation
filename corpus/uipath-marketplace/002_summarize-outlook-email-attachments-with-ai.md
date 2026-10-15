---
n: 2
source: uipath-marketplace
source_name: UiPath Studio Web template gallery (Maestro BPMN solutions)
source_type: vendor marketplace
title: "Summarize Outlook email attachments with AI"
url: https://cloud.uipath.com/masterthesismetz/studio_/templates
accessed: 2026-10-11
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "Exported .bpmn 2.0 XML (bpmn:definitions with uipath namespace, bpmn:process, bpmndi diagram interchange) from the solution created via 'Create in Local Workspace'."
bpmn_evidence_quote: "bpmn:process id='Process_1'"
ai_evidence: "Service task 'Agent - Analyze Attachments' bound to Orchestrator.StartAgentJob (binding 'Agent - Analyze Attachments'); the agent's only tool 'Analyze Files' is described as analysing files 'with an LLM'."
ai_evidence_quote: "Agent - Analyze Attachments"
artefacts:
  screenshot: null
  archive: "Summarize Outlook email attachments with AI/"
  bpmn_xml: 002_summarize-outlook-email-attachments-with-ai.bpmn
duplicate_of: null
access: free-account
capture_source: bpmn-xml
capture_quality: legible
capture_width_px: null
capture_method: researcher exported the solution from the Studio Web template gallery ('Create in Local Workspace'); .bpmn copied from the solution folder
---

## What the page shows

Gallery card (Templates tab, filter 'Maestro BPMN', search 'AI'), verbatim:

> "A Maestro pattern that retrieves the newest email from a specified Outlook folder, downloads its attachments, and uses an AI agent to generate a concise description of each file's contents."

Card footer: "Created by UiPath", "Used in 158 automations", type "Solution".

Process: start, 'Get Newest Email' (Integration Service), 'Get Attachment List' (HTTP request), script 'Get the Array of Attachments', 'Download Email Attachments', service task 'Agent - Analyze Attachments', end.

## Observations (description only, no interpretation)

- **AI activity - function:** Service task 'Agent - Analyze Attachments' bound to Orchestrator.StartAgentJob (binding 'Agent - Analyze Attachments'); the agent's only tool 'Analyze Files' is described as analysing files 'with an LLM'.
- **AI activity - element type:** Service task with implementation Orchestrator.StartAgentJob; agent project in the same solution.
- **Authority - downstream:** Agent tool 'Analyze Files' (internal tool: 'Analyze one or more files with an LLM to extract, synthesize, or answer queries about their content.').
- **Authority - data:** Output schema 'file_Summaries': array of {filename, description}.
- **Authority - control:** Agent task flows directly to the end event; no gateway or human step.
- **Input provenance:** Attachments of the newest email in a configured Outlook folder.
- **Guards present:** none observed
- **Prompt / model detail visible:** System prompt: 'You are a file description assistant. You receive one or more files and return a concise description of each file's contents.' Model gpt-4o-2024-11-20.

## Notes for the researcher

Researcher pre-vetted this template (2026-10-11). Full solution export kept in `Summarize Outlook email attachments with AI/`. 
