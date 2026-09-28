---
n: 787
source: flowable
source_name: Flowable (enterprise documentation, vendor blog/marketing site, training site)
title: Intelligent End-to-End Automation with Flowable’s AI Service
url: https://www.flowable.com/blog/business/flowable-ai-service
accessed: 2026-09-25
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: "BPMN 2.0 diagram seen natively in the page asset image-2024-7-16_15-27-24.png ('Simplified process with Flowable's AI service'): one pool 'Process Customer Request' with two lanes (System, Help Desk Member), message start event 'Email received', service tasks 'Recognize intent', 'Analyze sentiment', 'Extract data according intent', 'Process intent automatically', user tasks 'Review extracted intent and data / sentiment', 'Process intent manually', 'Analyze intent and handle request manually', exclusive gateways with X markers and yes/no branches, and an end event circle. bpmn_evidence_quote: 'Simplified process with Flowable's AI service' (asset caption); task labels read at native resolution"
bpmn_evidence_quote: "Simplified process with Flowable's AI service"
ai_evidence: "AI inside the process: the four service tasks are bound to the AI-type service definition the page also publishes - 'Service: Sample AI Service', Service type 'AI', operations 'Recognize Intent' (recognizeIntent) and 'Get Sentiment Score' (getSentimentScore) match the tasks 'Recognize intent' and 'Analyze sentiment' in the diagram, and the same page publishes that operation's prompt editor (system message 'Your working in the customer help desk team of a bank. Please try to recognize the intent of the customer...')."
ai_evidence_quote: "Service: Sample AI Service" / "Recognize Intent" / "recognizeIntent" / "Get Sentiment Score" / "getSentimentScore" (asset image-2024-7-16_15-10-43__1_.png)
artefacts:
  screenshot: 166_bpmn-simplified-process-with-flowable-ai-service.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 2000
capture_method: urllib download of https://images.ctfassets.net/chja9v5uur3u/5ht7jCgcboME9tdHsd3xp1/53786ac6f1a5ef7272dc2ec19ea85ce8/image-2024-7-16_15-27-24.png?fm=png&w=2000 (the page's own BPMN diagram asset, "Simplified process with Flowable's AI service", 2000x718); read natively in this session
---

## Why the text pass left this UNCERTAIN (now superseded by the sighted pass above)

The page publishes figures and mentions AI, but the figure that would decide the
verdict could not be certified from the evidence this session can read (the DOM, the
page text, and OCR labels). Per CLAUDE.md section 5 an unresolved figure is UNCERTAIN
with needs_visual_check, never an exclusion.

## Observations (description only, no interpretation)

- **Figures on the page:** Flowable AI service example | image-2024-7-16_15-10-43__1_.png; Simplified process with Flowable's AI service | image-2024-7-16_15-27-24.png; iStock-1357180459 | fl_ai-early-access_iStock-1357180459_2.jpg
- **OCR labels of the captured figure:** Sample Al Servi... | Service: Sample Al Service | There aretwotypes of servicedefinitionmodels.A standard servicemodel defines operationswith inputandoutput parameters infreeform.Adata model | based servicemodelisusedtodefinehowthedataforadata object modelisretrieved,created andmanaged.Thistypeof servicemodelis constrained bythe | datamodelstructure,whichdefinesalargepartofwhattheservicecando. | A
- **Page text quote:** Unpredictable outputs or "hallucinations" could disrupt process execution, leading to errors or delays.
- **Captured asset:** https://images.ctfassets.net/chja9v5uur3u/791Zjv7FtGVh8WITN0qCiW/38bab87418984babb967bf1ba5af22d3/image-2024-7-16_15-10-43__1_.png?fm=webp&q=75&bg=rgb%3Affffff&w=1920 (1920x1531)

## Sighted observations (visual pass elicitation-aa, shard s5, 2026-09-25) — INCLUDE

Read all three content figures of the page natively (Contentful assets fetched at
2000 px and read whole; task markers re-read as a 2x native crop).

- **The page's BPMN 2.0 diagram, with AI service tasks inside the process.** Published as
  "Simplified process with Flowable's AI service" (2000x718); captured for this record as
  `corpus/flowable/166_bpmn-simplified-process-with-flowable-ai-service.png`, source
  `https://images.ctfassets.net/chja9v5uur3u/5ht7jCgcboME9tdHsd3xp1/53786ac6f1a5ef7272dc2ec19ea85ce8/image-2024-7-16_15-27-24.png`.
  Two lanes inside one pool: the pool is **Process Customer Request** (label band down the
  left edge) and the lanes are **System** and **Help Desk Member**. In the System
  lane: message start event (envelope, label "Email received") -> service task **"Recognize
  intent"** -> service task **"Analyze sentiment"** -> exclusive gateway (X) with
  branches labelled "Intent recognized?" yes/no -> service task **"Extract data according
  intent"** -> gateway "Bad sentiment?" no/yes -> **"Process intent automatically"**
  (drawn with a **thick border**, i.e. call-activity styling, unlike the other three
  automation tasks, which have a thin border) -> two more gateways -> end event circle. In the human lane: user tasks (person icon) **"Analyze intent and handle request manually"**, **"Review
  extracted intent and data / sentiment"**, **"Process intent manually"**, feeding back
  into the gateways. Every one of the four automation tasks carries the same small
  **rocket** task-type marker in its top-left corner, confirmed by sight at 8x zoom on an
  original-resolution crop (a tilted rocket with fins and a window), i.e. a typed Flowable
  task, not the plain BPMN user-task icon used on the three human tasks.
- **The AI binding the tasks belong to, on the same page.**
  `.../791Zjv7FtGVh8WITN0qCiW/.../image-2024-7-16_15-10-43__1_.png` (the census capture,
  "Flowable AI service example") is the service-definition editor **"Service: Sample AI
  Service"** with **Service type = "AI"** and Operations: **Recognize Intent**
  (`recognizeIntent`), **Get Sentiment Score** (`getSentimentScore`), Extract Payment
  Instructions, Extract Account Balance Data, Extract New Address, Extract New Account
  Information. `.../3oPfcBfLRu5ACU19A4pzdi/.../image-2024-7-16_15-13-18.png` is that
  service operation's **Prompt** editor (User message "You receive the following message
  from a customer: ${content}", System message "Your working in the customer help desk
  team of a bank. Please try to recognize the intent of the customer ... reply with
  'unknown'"). The diagram's task names ("Recognize intent", "Analyze sentiment",
  "Extract data according intent") match this AI service's operation names, and the page
  text states "AI service invocation: The email content is passed to the AI service, which
  recognizes the customer's intent and analyzes sentiment."
- **Why INCLUDE.** An AI/LLM element sits inside a BPMN 2.0 process: service tasks bound
  to a service definition of type "AI" whose behaviour is an LLM prompt. The verdict does
  not rest on the task *type* of the fourth automation task - it is thick-bordered
  (call-activity styling), so it may be a call activity rather than a service task - but on
  the AI-bound service tasks "Recognize intent" / "Analyze sentiment" / "Extract data
  according intent" plus the "AI service invocation" the page describes, any of which puts
  an AI element inside the process. Only the fourth content figure is a stock photo
  (iStock-1357180459).

## What to check

Whether the captured figure (or another figure on the page) is a BPMN 2.0 process
diagram and whether an AI/LLM element sits inside that process.
