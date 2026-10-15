---
n: 3
source: uipath-marketplace
source_name: UiPath Studio Web template gallery (Maestro BPMN solutions)
source_type: vendor marketplace
title: "Extract Meeting Minutes and Action Items From Transcripts"
url: https://cloud.uipath.com/masterthesismetz/studio_/templates
accessed: 2026-10-11
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "Exported .bpmn 2.0 XML (bpmn:definitions with uipath namespace, bpmn:process, bpmndi diagram interchange) from the solution created via 'Create in Local Workspace'."
bpmn_evidence_quote: "bpmn:process id='Process_1'"
ai_evidence: "Service task 'Communication Extractor Agent' (Orchestrator.StartAgentJob); agent.json: 'You are an AI meeting-analysis agent.' No tools configured."
ai_evidence_quote: "You are an AI meeting-analysis agent. Your job is to extract structured insights from raw meeting transcripts."
artefacts:
  screenshot: null
  archive: "Extract Meeting Minutes and Action Items From Transcripts/"
  bpmn_xml: 003_extract-meeting-minutes-and-action-items-from-transcripts.bpmn
duplicate_of: null
access: free-account
capture_source: bpmn-xml
capture_quality: legible
capture_width_px: null
capture_method: researcher exported the solution from the Studio Web template gallery ('Create in Local Workspace'); .bpmn copied from the solution folder
---

## What the page shows

Gallery card (Templates tab, filter 'Maestro BPMN', search 'AI'), verbatim:

> "Process meeting transcripts from Teams, Zoom, or Google Meet to extract structured summaries, decisions, risks, and action items, then generate Jira-ready task details for each follow-up."

Card footer: "Created by UiPath", "Used in 111 automations", type "Solution".

Process: start, flow 'User Input' to 'Assign Value For Agent Input in BPMN' (RPA job), service task 'Communication Extractor Agent', service task 'JIRA Tickets Creation' (RPA job), end.

## Observations (description only, no interpretation)

- **AI activity - function:** Service task 'Communication Extractor Agent' (Orchestrator.StartAgentJob); agent.json: 'You are an AI meeting-analysis agent.' No tools configured.
- **AI activity - element type:** Service task with implementation Orchestrator.StartAgentJob.
- **Authority - downstream:** Service task 'JIRA Tickets Creation' starts RPA process 'Create JIRA Ticket' ('Deserialize JSON', 'For Each', 'Create Issue') over the agent's 'jira_tickets' output.
- **Authority - data:** Agent output: 'agentRawOutput' and 'agentRawOutput_Markdown' (strings) with summary, decisions, risks, action items, Jira tickets.
- **Authority - control:** No gateway or human step between the agent and Jira issue creation.
- **Input provenance:** Meeting transcript ('Raw transcript text from Teams, Zoom, or Google Meet.'), assigned by RPA job 'Assign Value For Agent Input in BPMN' after the 'User Input' start.
- **Guards present:** none observed
- **Prompt / model detail visible:** 'Do not add information that is not explicitly stated in the transcript.' User prompt: 'Please process the following meeting transcript ... {{meeting_transcript}}'. Model gpt-4o-2024-11-20.

## Notes for the researcher

Researcher pre-vetted this template (2026-10-11). Full solution export kept in `Extract Meeting Minutes and Action Items From Transcripts/`. 
