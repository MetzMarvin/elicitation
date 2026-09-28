---
n: 496
source: flowable
source_name: Flowable (enterprise documentation, vendor blog/marketing site, training site)
title: Part 3: Add Conversations to the Process with Flowable Engage | Flowable Enterprise Documentation
url: https://documentation.flowable.com/latest/reactmodel/expert/conversations/index.html
accessed: 2026-09-25
verdict: UNCERTAIN
needs_human_ruling: true
question: "Is Flowable Engage's 'digital.assistant' sending user an AI/LLM-backed assistant (i.e. an AI element inside the process), or just a bot user account that posts modeller-authored templated messages? The page's BPMN Send message tasks carry Details>Sending user id = digital.assistant and the conversation shows a 'Digital Assistant' participant, but the page never calls it AI, LLM, agent or intelligence anywhere."
needs_visual_check: false
bpmn_evidence: sighted confirmation 2026-09-25 (shard s3) — the page publishes genuine BPMN 2.0. 59-initialization-process-1-react (904x236) is a straight-through process: start-event circle -> tasks 'Set case name', 'Start conversation', 'Post initial message', 'Post travel data' -> end-event circle. 65-conversational-approval-process-react (904x450) is a pool with two lanes, 'Travel requestor' and 'Travel approver', with an exclusive gateway labelled 'Request approved?' branching no/yes to 'Send no approval message' / 'Send approval message'. The page's prose builds exactly that: we want to send the message as the digital assistant helping us to understand the meaning of the created conversation
bpmn_evidence_quote: "we want to send the message as the digital assistant helping us to understand the meaning of the created conversation"
ai_evidence: UNCERTAIN on the AI question, not established either way. The page text contains no AI, LLM, agent, GPT or intelligence mention at all; what it does contain is a sending identity — set the property Details>Sending user id to digital.assistant — on BPMN Send message tasks, and a conversation participant named 'Digital Assistant' whose posts are modeller-authored templates (Details>Message content). The earlier ai_evidence line here (OCR labels of a Work case screen) was a false positive and is superseded; see What to check.
ai_evidence_quote: "set the property Details>Sending user id to digital.assistant"
artefacts:
  screenshot: 100_owable-com-latest-reactmodel-expert-conversations-index-html.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1384
capture_method: urllib download of https://documentation.flowable.com/latest/assets/images/62-case-overview-with-conversation-link-react-4f786e17abec0f854627b8552e09100e.png (asset published by the page); labels inside read with RapidOCR, this session cannot receive image content
---

## Why this row is UNCERTAIN

The page publishes figures and mentions AI, but the figure that would decide the
verdict could not be certified from the evidence this session can read (the DOM, the
page text, and OCR labels). Per CLAUDE.md section 5 an unresolved figure is UNCERTAIN
with needs_visual_check, never an exclusion.

## Observations (description only, no interpretation)

- **Figures on the page:** 62 case overview with conversation link | 62-case-overview-with-conversation-link-react-4f78; 64C conversation with task | 64C-conversation-with-task-react-bf239f71bb9acf524; 67 conversation with select approvers | 67-conversation-with-select-approvers-react-6cd280; 68 approver joining conversation | 68-approver-joining-conversation-react-014bf86ad15
- **OCR labels of the captured figure:** 白 Case | Travel Case for Shane Bowen (Workshop in Singapore) | 曲 Started: less than a minute ago | Started By:ShaneBowen | Define travel data | Approve travel | Organize travel | D Modify travel data | Save | βTerminate | .. | Sub-items | 目 Documents | Opentasks | Workform | History
- **Page text quote:** Part 3: Add Conversations to the Process with Flowable Engage
- **Captured asset:** https://documentation.flowable.com/latest/assets/images/62-case-overview-with-conversation-link-react-4f786e17abec0f854627b8552e09100e.png (1384x1332)

## Sighted check (shard s3, 2026-09-25) — all 16 figures looked at

- **Is it BPMN 2.0?** Yes. `59-initialization-process-1-react` (904x236) is a
  straight-through BPMN process — start-event circle, then the tasks *Set case name*,
  *Start conversation*, *Post initial message*, *Post travel data* (each with the Engage
  activity glyph), then an end-event circle. `65-conversational-approval-process-react`
  (904x450) is a BPMN **pool** split into two **lanes** (*Travel requestor*, *Travel
  approver*) with an **exclusive gateway** labelled *Request approved?* whose *no* / *yes*
  branches run to *Send no approval message* and *Send approval message*. The property
  panels behind them are the Engage bindings (*Scope type* `conversation`, *Scope Id*
  `${scopeId}`) on Human Task `Modify Travel Data (cmmnTask_6)` and User Event Listener
  *File for approval (cmmnEventListenter_9)* — i.e. CMMN elements carrying the bindings.
- **Is it CMMN?** The case side is: `57C-case-model-with-initialization` and
  `66-last-stage-with-message-task` draw the folder-shaped case plan model *Travel Request*
  with cut-corner stages *Define travel data* / *Approve travel* / *Organize travel*, a
  black sentry diamond on the *Approve travel* border, an *occur* event listener labelled
  *File for approval*, and repetition / user-listener markers on *Modify travel data*.
- **Where the AI question sits.** No figure shows an AI task, an agent, a model or an LLM
  element. What the processes do carry is a **sending identity**: the *Send message* tasks
  set `Details > Sending user id` to `digital.assistant`, and the conversation screenshots
  (`61-initial-conversation`, `64C-conversation-with-task`, `67`, `68`, `69`, `70`) show a
  participant named **Digital Assistant** posting messages. Those messages are
  Modeller-authored templates (`Details > Message content`, `Message content type` `MD`) —
  no model call is visible anywhere.
- **Unresolved.** Whether `digital.assistant` is an AI/LLM-backed assistant or simply a
  non-human user account. The page never says. This is the question recorded in the
  frontmatter; a human ruling settles whether this page is an AI-inside-the-process case.

## What to check (original, superseded)

Whether the captured figure (or another figure on the page) is a BPMN 2.0 process
diagram and whether an AI/LLM element sits inside that process.
