---
n: 252
source: camunda-marketplace
source_name: Camunda Marketplace
source_type: vendor marketplace
title: Agentic AI Orchestration with Form.io
url: https://marketplace.camunda.com/apps/719979/agentic-ai-orchestration-with-formio
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: A complete published process: message start event 'Leave request recieved' -> gateway -> serviceTask 'AI Agent Connector' (violet AI glyph) -> gateway 'Action needed?' -> 'tools' branch into an ad-hoc sub-process 'Tools' holding 'Check current amount of time off' and 'Get doctors note', and an 'approved' branch to gateway 'Is Approved?' -> userTask 'Approve leave request' -> end 'Leave request approved'; further-review paths lead to userTask 'Supervisor review leave request' -> gateway 'Is Approved?' (approved -> 'Leave request approved', denied -> userTask 'Manager review leave request' -> gateway 'Is Approved?' -> 'Leave request approved' or 'Leave request denied'); the tool results return from the 'Tools' container to the gateway before the AI Agent Connector.
bpmn_evidence_quote: "AI Agent Connector"
ai_evidence: The gateway 'Action needed?' has an explicit 'tools' branch out of the AI Agent Connector task into the Tools container, i.e. the agent decides whether to call a tool - the same pattern as Camunda's MCP tool calling, drawn by this vendor. The page describes the offer as 'Accelerate delivery of governed, end-to-end business processes by combining Form.io's standardized form and data capture with Camunda's process orchestration and automation capabilities', with the marketplace categories 'Agentic AI Orchestration' (listing title), 'Agentic Solutions', 'AI Services' and 'Solution Accelerators'; the listing is a partner accelerator tagged 'Listing Only'.
ai_evidence_quote: "Accelerate delivery of governed, end-to-end business processes by combining Form.io"
artefacts:
  screenshot: 252_agentic-ai-orchestration-with-form-io.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: listing-asset
capture_quality: legible
capture_width_px: 1100
capture_method: curl of the listing's own asset (d3bql97l1ytoxn.cloudfront.net, app_resources/719979/overview/img6840927305003297751-2x.png, 1100x637), read natively at full size
---

## What the page shows

Agentic AI Orchestration with Form.io (partner solution accelerator, 'Listing Only', 8.8/8.9). A leave-request process in which an AI agent task decides whether action is needed, calls tools (checking the leave balance, fetching a doctor's note from a form) when it is, and the outcome is routed through supervisor and manager human approvals with a loop back into the agent on denial.

## Observations (description only, no interpretation)

- **AI activity - function:** decide whether the request needs action at all and, when it does, call the tools needed to assess it ('Check current amount of time off', 'Get doctors note').
- **AI activity - element type:** one serviceTask 'AI Agent Connector' carrying the violet AI glyph, with an explicit 'tools' sequence flow from the following gateway into an ad-hoc 'Tools' container.
- **AI activity - models named:** none on the page or in the figure - the listing is a pattern, not a connector, so the model is left to the implementer.
- **Authority - downstream:** the agent's judgement gates the whole approval chain - nothing reaches a human approver until the agent says action is needed, and the tool results return to the gateway before the agent, so the loop is agent-decides, tool-answers, agent-decides again.
- **Authority - control (human):** three levels of human approval (Approve leave request, Supervisor review, Manager review), each behind its own 'Is Approved?' gateway, with a terminal 'Leave request denied' outcome.
- **Data reachable by the agent:** the leave request message, the leave-balance tool and the form-submitted doctor's note (Form.io is the form/data-capture half of the accelerator).
- **Human role:** the entire approval ladder, so the AI proposes and humans dispose - the page's stated aim is 'governed' processes; a denial is terminal ('Leave request denied'), not an AI retry.
- **Scope note:** tagged 'Listing Only' and publishing no .bpmn; the evidence is the canvas plus the feature prose.

## Notes for the researcher

A partner accelerator whose *only* AI element is a single agent task placed in front of a three-level human approval ladder - the most explicit 'AI triages, humans decide' structure in this source, and the clearest example of the agent-decides-whether-to-call-a-tool branch drawn as an ordinary sequence flow labelled 'tools'. Two reading notes: the listing is 'Listing Only' (no .bpmn to grep), and it is the only listing in this batch that names Form.io rather than a model provider - the form platform is what the tools read.
