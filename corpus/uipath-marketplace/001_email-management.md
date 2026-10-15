---
n: 1
source: uipath-marketplace
source_name: UiPath Studio Web template gallery (Maestro BPMN solutions)
source_type: vendor marketplace
title: "Email Management"
url: https://cloud.uipath.com/masterthesismetz/studio_/templates
accessed: 2026-10-11
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "Exported .bpmn 2.0 XML (bpmn:definitions with uipath namespace, bpmn:process, bpmndi diagram interchange) from the solution created via 'Create in Local Workspace'."
bpmn_evidence_quote: "bpmn:process id='Process_1'"
ai_evidence: "Service task 'Analyze & Categorize'; the solution ships agent project 'Email Management Agent' (agent.json, gpt-4o-2024-11-20) whose tools are processes 'ReadLatestOutlookEmail' and 'MoveOutlooEmail'."
ai_evidence_quote: "categorize the email to the best of your ability into one of the below categories (and move to respective folders)"
artefacts:
  screenshot: null
  archive: "Email Management/"
  bpmn_xml: 001_email-management.bpmn
duplicate_of: null
access: free-account
capture_source: bpmn-xml
capture_quality: legible
capture_width_px: null
capture_method: researcher exported the solution from the Studio Web template gallery ('Create in Local Workspace'); .bpmn copied from the solution folder
---

## What the page shows

Gallery card (Templates tab, filter 'Maestro BPMN', search 'AI'), verbatim:

> "The Email Management agent is designed to organize Outlook inboxes by categorizing and moving emails based on their content, urgency, and relevance."

Card footer: "Created by UiPath", "Used in 754 automations", type "Solution".

Process 'Email Management Process': start, gateway 'Testing?', service task 'Read Latest Outlook Email' (or script 'Use Test Inputs'), service task 'Analyze & Categorize', service task 'Move Outlook Email', script 'Prepare Output', end.

## Observations (description only, no interpretation)

- **AI activity - function:** Service task 'Analyze & Categorize'; the solution ships agent project 'Email Management Agent' (agent.json, gpt-4o-2024-11-20) whose tools are processes 'ReadLatestOutlookEmail' and 'MoveOutlooEmail'.
- **AI activity - element type:** BPMN service task without binding in the shipped .bpmn; the agent is a separate project in the same solution.
- **Authority - downstream:** Agent tools 'ReadLatestOutlookEmail' and 'MoveOutlooEmail' (RPA processes, Outlook 'Get Newest Email - Inbox' / 'Move Email'); in the BPMN, service task 'Move Outlook Email' follows the AI task.
- **Authority - data:** Agent output schema: 'DestinationFolder' and 'Reasoning' (strings). Moves the email to a mailbox folder.
- **Authority - control:** No gateway or human step consumes the output; 'Prepare Output' script, then end.
- **Input provenance:** Latest email of the Outlook inbox (subject, body, message ID), or test subject/body from start-event variables.
- **Guards present:** none observed
- **Prompt / model detail visible:** System prompt (agent.json): 'You are a helpful email management assistant.' Folders: High Priority, Meetings, Social, Finance, Project X, Customer Support, Notifications, Inbox. Step 6: 'run MoveOutlookEmail tool'.

## Notes for the researcher

Researcher pre-vetted this template (2026-10-11). Full solution export kept in `Email Management/`. Service tasks in the .bpmn carry no implementation binding; the AI binding is established by the agent project shipped in the solution and the listing text.
