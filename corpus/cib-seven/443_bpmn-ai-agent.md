---
n: 443
source: cib-seven
source_name: CIB seven manual (docs.cibseven.org, /manual/latest/ pinned)
source_type: vendor documentation
title: BPMN AI Agent
url: https://docs.cibseven.org/manual/latest/webapps/modeler/user-guide/bpmn-ai-chat/
accessed: 2026-09-25
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "two of the seven figures carry the artefact, both read at native resolution in tiles. bpmn-ai-chat-overview.png (3454x1930) is the Modeler canvas on the process 'Machine Part Per...': start event > 'Submit Permit Request' > 'Screen Part Compliance' > 'Derive Compliance Verdict' > gateway 'Compliant without warnings?' > 'Issue Permit Automatically'. The properties panel beside it is headed 'CIB SEVEN - AI AGENT / Screen Part Compliance', with Template 'Applied', Name 'CIB seven - AI Agent', Version 1, Description 'Element template for the cibseven-ai-agent connector.' and Input 'Agent name: Compliance Auditor Agent'. bpmn-ai-chat-diff.png (5124x2378) is the Modeler on the process 'Customer Onboa...': 'Perform Automated KYC' > gateway 'KYC Verification Outcome?' > gateway 'Approval Join' > 'Complete Customer Onboarding' (selected service task, Template '+ Select') > end event 'Onboarding Completed'. BPMN 2.0 shapes with sequence flows and exclusive gateways; the bpmn.io renderer mark is visible. Three figures are captured next to this record."
bpmn_evidence_quote: "properties panel 'CIB SEVEN - AI AGENT / Screen Part Compliance', Template 'Applied', Name 'CIB seven - AI Agent', Description 'Element template for the cibseven-ai-agent connector.'"
ai_evidence: "the AI element is inside the process: the service task 'Screen Part Compliance' carries the applied element template 'CIB seven - AI Agent' (the cibseven-ai-agent connector) with agent name 'Compliance Auditor Agent' and prompt 'Screen the following machine part permit request against the compliance guidelines.', and the model is annotated 'AI Agent auditor: declares the part compliant only when there are zero warnings; otherwise it flags the request for a supervisor.' The same page also documents the design-time agent (panel 'BPMN Agent BETA', 'Review changes', 'Changes applied') whose proposal names the connector parameters agentName, message, instruction, instructionMode, useChatMemory and agentOutput, agentOutput_aiMeta."
ai_evidence_quote: "'AI Agent auditor: declares the part compliant only when there are zero warnings; otherwise it flags the request for a supervisor.' (green annotation in bpmn-ai-chat-overview.png)"
artefacts:
  screenshot: 443_bpmn-ai-chat-overview.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: page asset from docs.cibseven.org (same-origin)
capture_quality: legible
capture_width_px: 3454
capture_method: plain GET of the page asset (ledgers/cib-seven.raw/img/), or the page's own XML block copied verbatim
---

## What the page shows

Verbatim from the page:

> "The BPMN AI Agent adds an LLM-powered chat assistant to CIB seven Modeler."

## Artefact reading (native resolution unless stated)

- **BPMN:** two of the seven figures carry the artefact, both read at native resolution in tiles. bpmn-ai-chat-overview.png (3454x1930) is the Modeler canvas on the process "Machine Part Per...": start event > "Submit Permit Request" > "Screen Part Compliance" > "Derive Compliance Verdict" > gateway "Compliant without warnings?" > "Issue Permit Automatically". The properties panel beside it is headed "CIB SEVEN - AI AGENT / Screen Part Compliance", with Template "Applied", Name "CIB seven - AI Agent", Version 1, Description "Element template for the cibseven-ai-agent connector." and Input "Agent name: Compliance Auditor Agent". bpmn-ai-chat-diff.png (5124x2378) is the Modeler on the process "Customer Onboa...": "Perform Automated KYC" > gateway "KYC Verification Outcome?" > gateway "Approval Join" > "Complete Customer Onboarding" (selected service task, Template "+ Select") > end event "Onboarding Completed". BPMN 2.0 shapes with sequence flows and exclusive gateways; the bpmn.io renderer mark is visible. Three figures are captured next to this record.
- **AI element:** the AI element is inside the process: the service task "Screen Part Compliance" carries the applied element template "CIB seven - AI Agent" (the cibseven-ai-agent connector) with agent name "Compliance Auditor Agent" and prompt "Screen the following machine part permit request against the compliance guidelines.", and the model is annotated "AI Agent auditor: declares the part compliant only when there are zero warnings; otherwise it flags the request for a supervisor." The same page also documents the design-time agent (panel "BPMN Agent BETA", "Review changes", "Changes applied") whose proposal names the connector parameters agentName, message, instruction, instructionMode, useChatMemory and agentOutput, agentOutput_aiMeta.

## Captures

- `443_bpmn-ai-chat-overview.png` (3454x1930) - from `349_webapps_modeler_user-guide_img_bpmn-ai-chat-overview.png`
- `443_bpmn-ai-chat-diff.png` (5124x2378) - from `348_webapps_modeler_user-guide_img_bpmn-ai-chat-diff.png`
- `443_bpmn-ai-chat-agent-panel.png` (3456x1938) - from `346_webapps_modeler_user-guide_img_bpmn-ai-chat-agent-panel.png`

## Notes for the researcher

The assignment warns that a page about the Modeler wizard is the E2-no-ai-element case and asks for the vendor's own "Design-time" label to be quoted when dismissing it. The label is real (the AI Agent Connector overview distinguishes "Runtime - executes during a process instance" from the Modeler wizard's "Design-time - helps you author BPMN"), but this page's figures also show the runtime binding: the overview figure has the AI Agent element template *applied* on a service task inside the process, so the page carries runtime AI and is collected, not dismissed.
