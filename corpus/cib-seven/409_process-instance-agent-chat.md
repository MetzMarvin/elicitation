---
n: 409
source: cib-seven
source_name: CIB seven manual (docs.cibseven.org, /manual/latest/ pinned)
source_type: vendor documentation
title: Agent Chat
url: https://docs.cibseven.org/manual/latest/webapps/cockpit/bpmn/process-instance-chat/
accessed: 2026-09-25
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "the page publishes cockpit-instance-agent-chat.png (3840x2482, read at native resolution in four tiles): the Cockpit Process Instance view with a rendered BPMN diagram of the definition key 'ai-agent-with-human', name 'Human in the AI Agent Loop'. Pool 'AI Process' runs Start Event > 'User Input' > 'Call AI Agent' > 'Show AI Output' > End Event; pool 'Human in the AI Agent Loop' runs 'Start Event AI' > gateway > 'AI Agent Call' > gateway 'One Shot?' (labels 'yes - no review' / 'no - with review') > 'Review AI Result' > gateway 'Is result approved?' (Yes / No) > 'End Event AI'. BPMN 2.0 shapes with sequence flows and exclusive gateways; the bpmn.io renderer mark is visible bottom right. Captured next to this record."
bpmn_evidence_quote: "Pool 'AI Process': User Input, Call AI Agent, Show AI Output. Pool 'Human in the AI Agent Loop': AI Agent Call, One Shot?, Review AI Result, Is result approved?"
ai_evidence: "the AI elements are inside the process: both pools exist to run and review the agent - the service tasks 'Call AI Agent' / 'AI Agent Call' are the AI Agent Connector calls, and 'Show AI Output' / 'Review AI Result' are the human steps that read the result. The right-hand Agent Chat panel shows the recorded session for the instance: a Request bubble, an 'AI Agent' bubble carrying {'text': '...', 'thinking': null}, and a Response bubble."
ai_evidence_quote: "Agent Chat panel: Request / 'AI Agent' {'text': 'BPMN (Business Process Mo... interactions are clear.', 'thinking': null} / Response 'BPMN is a standardized way to diagram business processes.'"
artefacts:
  screenshot: 409_process-instance-agent-chat.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: page asset from docs.cibseven.org (same-origin)
capture_quality: legible
capture_width_px: 3840
capture_method: plain GET of the page asset (ledgers/cib-seven.raw/img/), or the page's own XML block copied verbatim
---

## What the page shows

Verbatim from the page:

> "Agent Chat is not an interactive chat with an AI about the process instance - it is the recorded history of every AI Agent Connector session"

## Artefact reading (native resolution unless stated)

- **BPMN:** the page publishes cockpit-instance-agent-chat.png (3840x2482, read at native resolution in four tiles): the Cockpit Process Instance view with a rendered BPMN diagram of the definition key "ai-agent-with-human", name "Human in the AI Agent Loop". Pool "AI Process" runs Start Event > "User Input" > "Call AI Agent" > "Show AI Output" > End Event; pool "Human in the AI Agent Loop" runs "Start Event AI" > gateway > "AI Agent Call" > gateway "One Shot?" (labels "yes - no review" / "no - with review") > "Review AI Result" > gateway "Is result approved?" (Yes / No) > "End Event AI". BPMN 2.0 shapes with sequence flows and exclusive gateways; the bpmn.io renderer mark is visible bottom right. Captured next to this record.
- **AI element:** the AI elements are inside the process: both pools exist to run and review the agent - the service tasks "Call AI Agent" / "AI Agent Call" are the AI Agent Connector calls, and "Show AI Output" / "Review AI Result" are the human steps that read the result. The right-hand Agent Chat panel shows the recorded session for the instance: a Request bubble, an "AI Agent" bubble carrying {"text": "...", "thinking": null}, and a Response bubble.

## Captures

- `409_process-instance-agent-chat.png` (3840x2482) - from `281_webapps_cockpit_img_cockpit-instance-agent-chat.png`

## Notes for the researcher

This is the only page in the manual whose figure shows an AI agent *inside a rendered BPMN diagram* rather than in a table or a code block.
