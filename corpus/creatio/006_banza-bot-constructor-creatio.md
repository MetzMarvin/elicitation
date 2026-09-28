---
n: 2143
source: creatio
source_name: Creatio Marketplace (marketplace.creatio.com) - third surface of the creatio assignment
source_type: vendor product marketplace (app listing)
title: Banza Bot Constructor for Creatio
url: https://marketplace.creatio.com/app/banza-bot-constructor-creatio
accessed: 2026-09-24
verdict: UNCERTAIN
needs_human_ruling: true
question: "This listing publishes a genuine Creatio process-designer model (BPMN 2.0) - the 'Banza Bot Process' with a start event, gateway diamonds carrying Yes/No labels, tasks and terminate end events - and NO AI/LLM element appears anywhere inside it. But the model IS a chatbot's dialogue logic, the page calls the product an 'assistant', and one of its figures advertises free-text input ('Support both quick-reply buttons and free-text input'), which is exactly the place where a bot's intent/message handling could be an LLM call that the model does not show. Rule 3 of the shared rules says an element whose implementation might be AI-bound but is not visible is UNCERTAIN, never E2. Does the researcher read this as a plain rule-based bot (E2, no AI element inside the process) or as an AI-bound-but-invisible case worth keeping? I recorded UNCERTAIN because the hesitation is real and a wrong exclusion is unrecoverable."
bpmn_evidence: "Decisive: the figure the listing publishes is a Creatio process-designer canvas (BPMN 2.0). It is headed 'Banza Bot Process' and carries the designer's own chrome - the SAVE / RUN / CANCEL / ACTIONS toolbar, a zoom control at 74%, the left element palette, an element-type legend (Game bot, Main menu, Q_quests), and the right-hand element-parameter panel ('Bot message', with the MESSAGE and PARAMETERS tabs). On the canvas itself: a plain start circle at 'Bot session', tasks drawn as rounded rectangles with element icons ('Contact identification', 'Set contact', 'Check admin role', 'Parse chatbot', 'Link a contact to a chat', 'Info about the bot', 'Selecting an option', 'Message with quest...', 'Set id of active record'), orange gateway diamonds with Yes/No flow labels ('Contact found?', 'Check admin role', 'Main menu'), a red-bordered 'Exit' start event, and terminate end events drawn as red-bordered circles with a filled dot."
bpmn_evidence_quote: "Banza Bot Process"
ai_evidence: "No AI element is visible inside the process model. The page's AI-adjacent material is the word 'assistant' used as a description of the chatbot product it builds ('The chatbot is B2C/B2B assistant for active and personalized communication with your customers'), and a feature line offering free-text input alongside buttons ('Support both quick-reply buttons and free-text input for dynamic user interaction'). Neither is an element on the canvas: every task on the canvas is a record/database or messaging operation, and the parameter panel shown is a bot-message template. The page also lists 'Use of chatbots in business processes' and the setup step 'Create a business process and set one into the bot dialogue tree', i.e. the app's process is the artefact, and no AI task is drawn in it."
ai_evidence_quote: "The chatbot is B2C/B2B assistant for active and personalized communication with your customers."
artefacts:
  screenshot: 006_banza-bot-constructor-creatio_fig1.png
  archive: null
  bpmn_xml: null
capture_source: figure-as-published
capture_quality: legible
capture_width_px: 1919
capture_method: "the listing's own figure b_BanzaChatBotConstructor_08_0.png (1919x931), downloaded from the marketplace CDN and kept unmodified"
duplicate_of: null
access: public
---

## What the page shows

The listing of **Banza Bot Constructor for Creatio**, an app that builds chatbots on the Creatio platform.
The product description is written around the chatbot it produces:

> "Banza bot constructor for Creatio allows creating of chatbots for your 24/7 service. Optimize expenses
> and offer customers and colleagues an additional channel of interaction."

and its use cases name the assistant:

> "The chatbot is B2C/B2B assistant for active and personalized communication with your customers."

The feature list contains one process sentence - "Use of chatbots in business processes" - and the
installation card says "Create a business process and set one into the bot dialogue tree."

The listing's figure is the **Banza Bot Process** opened in the Creatio process designer: the designer
toolbar (SAVE / RUN / CANCEL / ACTIONS, zoom 74%), the left element palette, an element-type legend, the
canvas with a start event, nine tasks, three gateway diamonds with Yes/No labels, an "Exit" start event
and terminate end events, and the right-hand element-parameter panel for the selected element ("Bot
message", with its MESSAGE / PARAMETERS tabs and the button rows "Open in Creatio", "Approve",
"Decline").

## Observations (description only, no interpretation)

- **AI activity:** none is drawn. No task, gateway, event or annotation on the canvas names an AI/LLM
  function; the panel shown configures a bot message, not a model call.
- **AI adjacency:** the page's AI-adjacent tokens are the word "assistant" (naming the chatbot) and the
  free-text input feature line. Both are outside the model.
- **Process model:** yes - a genuine BPMN 2.0 drawing in the vendor's own process designer, i.e. the
  artefact class this method looks for, published here on the marketplace surface.
- **Model binding:** the chatbot dialogue is itself the process; the diagram is what the app's "dialogue
  tree" is made of.
- **Guards present:** the canvas has an explicit "Check admin role" gateway with Yes/No branches, i.e. an
  authority check, but nothing of the kind around any AI step (there is none).
- **Input provenance:** end-customer input over Telegram, Viber, Facebook Messenger or WhatsApp
  (per the feature list), i.e. untrusted external input reaching the bot.
- **Availability:** the listing is live and free/paid per bot licence; no availability gate on the page.

## Notes for the researcher

This is the only one of the twenty-two marketplace listings that publish a BPMN 2.0 model where the
model has any AI adjacency at all, and it is a narrow adjacency: the model is a rule-based button/record
dialogue, but "Support both quick-reply buttons and free-text input" is the one path along which an
LLM-based intent step could be hidden behind a task whose implementation the diagram does not show. The
shared rules force UNCERTAIN for that case rather than E2, so the row is UNCERTAIN and the researcher
rules on it.

For the method's purposes: if the researcher reads the bot as rule-based, this listing is E2 (a BPMN
model with no AI element inside it) and the marketplace surface contributes no AI-in-process example at
all - which is the surface's finding, not a gap. If the researcher reads free-text bot input as
AI-bound, the correct next step is to open the app's manual or the vendor's site for the element
implementation, which this pass did not do (the marketplace listing is the enumerated unit).
