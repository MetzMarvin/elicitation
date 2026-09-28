---
n: 134
record: 008
url: https://community.ibm.com/HigherLogic/System/DownloadDocumentFile.ashx?DocumentFileKey=14c6c7fc-2fd0-4dcc-8467-c77b0c394830&forceDialog=0
source: ibm-bamoe
surface: community:ibm.com
accessed: 2026-09-25
verdict: INCLUDE
needs_human_ruling: true
question: >
  Page 26 of this deck is a stylised illustration drawn with BPMN-like shapes (events, gateways,
  lanes) but with no readable labels at any rasterisation, and no AI element visible in it; its
  slide title says "AI integration - AI Agent Task for BPMN (Tech Preview)". Is it a second artefact
  of this deck (and if so, is the artwork a real process diagram with an AI element?), or a
  marketing illustration to be dismissed? Its capture is attached so the call can be made by eye.
bpmn_evidence: |
  Page 29 of the deck is a BAMOE Canvas screen with the watermark "BPMN 2.0": the editor tab reads
  "rotate_api_keys.bpmn", and on the canvas a start event, the task "Open PR", the task "Review PR"
  (selected) and an end event are joined by sequence flows. The node's panel is open on the right -
  "Review PR", "Langflow Account *", "Agent *", "Input *" with "Please review the following PR:
  {{prLink}}", the Preview table (Variable prLink / Value https://github.com/ibm/bamoe/pulls...),
  "Test Agent", "Data mapping (in: 2, out: 1)", "onEntry / onExit", "Metadata" - and the canvas
  carries the sign-in overlay "Sign in with Langflow to use BAMOE Developer Tools (1)". The slide's
  own text, from the deck's text layer, is "AI Agent Task for BPMN (Tech Preview)".
ai_evidence: |
  The selected node "Review PR" is an AI Agent Task (the deck's text layer names the feature "AI
  Agent Task for BPMN (Tech Preview)" and page 27 states it is "Compatible with Langflow" and
  "Configured out-of-the-box on BAMOE Canvas and BAMOE Developer Tools for VS Code"). Page 30 gives
  the deployment keys: "bamoe.workflow.ai-agent-task.provider.langflow.base-url",
  "-api-key", "-log-requests", "-log-responses" in src/main/resources/application.properties.
  Page 28 shows the Canvas home screen with the project "PR REVIEW _ BAMOE 931 DEMO" tagged Workflow.
artefacts:
  - screenshot: 008_ibm-bamoe-deck931-review-pr-canvas.png
  - screenshot: 008_ibm-bamoe-deck931-p26-illustration.png
  - file: ledgers/_bamoe_comm/webinar_931.pdf
  - file: ledgers/_bamoe_comm/w931_hi_29-29.png
  - file: ledgers/_bamoe_comm/sheet_deck_w931.png
capture_quality: legible
capture_width_px: 1734
---

## What the file shows

A 32-page webinar deck, "What's new in IBM Business Automation Manager Open Editions 9.3.1"
(agenda: introduction, MCP Server updates, Process Instance Migration, WS-HumanTask support, "AI
Agent Task for BPMN (Tech Preview)" by Tiago Bento, Q&A). The pages that matter:

- **p29, the artefact**: BAMOE Canvas with the process start → **"Open PR"** → **"Review PR"**
  (AI Agent Task, selected) → end, watermark "BPMN 2.0", tab `rotate_api_keys.bpmn`; the node's
  panel open with the Langflow account unset, the input `Please review the following PR: {{prLink}}`,
  the Preview pointing at a github.com/ibm/bamoe PR URL, and the not-authenticated overlay offering
  "Sign in with Langflow to use BAMOE Developer Tools (1)".
- **p27**: the same node's panel filled in against the Langflow provider card, with the slide's
  bullets: "Configured out-of-the-box on BAMOE Canvas and BAMOE Developer Tools for VS Code",
  "WIH pre-configured for Spring Boot (Full) and Quarkus (Full) Accelerators", the two
  `com.ibm.bamoe : bamoe-ai-agent-task-work-item-handler-*` coordinates, "Interactive properties
  panel for faster experimentation", "Process Variable interpolation", "Compatible with Langflow".
- **p28**: the Canvas home screen, "Recent models: PR REVIEW _ BAMOE 931 DEMO [Workflow]".
- **p30**: the `bamoe.workflow.ai-agent-task.provider.langflow.*` binding keys.
- Not BPMN: p7 (component architecture box diagram), p24 (the WS-HumanTask 1.1 lifecycle state
  diagram, footer `https://docs.oasis-open.org/bpel4people/ws-humantask-1.1-spec-cs-01.html`), p26
  (a stylised, unlabelled illustration - see the ruling question), p10/p16/p19/p20/p22
  (illustrations and timelines).

## Observations

- This is the second artefact in the corpus in which an **AI Agent Task is wired into a process** -
  a three-element BPMN process whose middle task is the AI one - as opposed to merely dropped on a
  canvas (records 006 and 007).
- The AI node here is bound to a *named Langflow account* and an agent, so the AI is configured as
  an external agent call from inside the process; the input is a process variable (`{{prLink}}`).
- The deck documents the same node type twice over: the demo (p29) and the configuration
  (p27, p30), the latter in the deployment `application.properties` - i.e. the AI binding has a
  server-side configuration surface as well as the in-editor panel.

## Notes for the researcher

- **The ruling question is the only reason this row is flagged.** Everything in the record above is
  legible and verified; the doubt is confined to p26's illustration, whose capture
  (`008_ibm-bamoe-deck931-p26-illustration.png`, 2934x1650 at 220 dpi) shows why: the artwork uses
  BPMN-like shapes with no labels anywhere.
- The deck is one enumerated item (one document, one row); its pages are not separate rows. The
  second capture is attached to this record so page 26 can be ruled on without reopening the PDF.
- The deck's download URL is the community platform's attachment endpoint and was verified to
  resolve (HTTP 302 → higherlogicdownload.s3.amazonaws.com/IMWUC/<key>_file.pdf); the page that
  published the link was not preserved in this session's captures, so the referring page is not
  claimed here.
