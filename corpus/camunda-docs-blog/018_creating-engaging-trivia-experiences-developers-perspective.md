---
n: 1376
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: Creating Engaging Trivia Experiences: A Developer's Perspective | Camunda
url: https://camunda.com/blog/2024/01/creating-engaging-trivia-experiences-developers-perspective/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: the captured figure is a BPMN process model - a start event "Play Trivia Game", rounded-rectangle tasks, two parallel gateways (plus marker) and two exclusive gateways (X marker) with "Yes" / "No" labelled flows, a sequence-flow loop from the "Lives left?" gateway back to "Get Trivia Question", and two end events ("Win", "lose"); the figure's own alt text names it a bpmn model
bpmn_evidence_quote: "Basic-trivia-bpmn-model-plus-openai"
ai_evidence: three tasks in the model carry the OpenAI connector's swirl glyph and are the tasks the page's AI text refers to - "Check Answer" (the page's answer-checking step), "Get celebration message" and "Get inspiration" ("generating some words of encouragement for folks who lost the game"); the other tasks carry a user glyph or a REST glyph, so the AI-bound tasks are visually distinct inside the process
ai_evidence_quote: "I used the OpenAI connector and added the prompt:"
artefacts:
  screenshot: 018_basic-trivia-bpmn-model-plus-openai.png
  archive: null
  bpmn_xml: null
duplicate_of: null
access: public
capture_source: original-asset
capture_quality: legible
capture_width_px: 1400
capture_method: chrome-devtools-mcp page fetch; the figure's cdn.sanity.io URL decoded out of the page's /_next/image proxy, downloaded at w=1400
---

## What the page shows

The post describes a trivia game built for a conference and the BPMN model behind it. The
captured figure (alt "Basic-trivia-bpmn-model-plus-openai") is that model: the start event
"Play Trivia Game" into the task "Get Trivia Question" (which carries the REST connector
glyph), the user task "Guess Answer to Question", a parallel gateway that opens "Show
Answer" alongside "Check Answer", the user task "Show what Chat Suggests" consuming the
"Check Answer" result, a second parallel gateway, the exclusive gateway "Did you answer
correctly" ("Yes" into "Get celebration message" and the user task "Collect Prize", ending
at "Win"; "No" into "Lose a life" and the gateway "Lives left?", whose "Yes" flow loops back
to "Get Trivia Question" and whose other flow goes into "Get inspiration" and the user task
"You lose", ending at "lose").

Three of those tasks - "Check Answer", "Get celebration message", "Get inspiration" - carry
the OpenAI connector's swirl glyph, while the other tasks carry a user or a REST glyph. The
page's text ties them to the AI steps it describes: the answer check, the hint, and "some
words of encouragement for folks who lost the game".

## Observations (description only, no interpretation)

- **AI activity - function:** the page says it used the OpenAI connector to check an answer
  automatically ("I used the OpenAI connector and added the prompt:") and, for hints, that
  "if a user needed a hint, they'd just tick the box and I would ask ChatGPT for a hint to
  the answer of the question. I also asked that emojis be included."
- **AI activity - element type:** three ordinary BPMN tasks in the process ("Check Answer",
  "Get celebration message", "Get inspiration") whose corner glyph is the OpenAI connector
  icon - i.e. tasks with an AI connector implementation binding, not a separate node type.
- **Authority - downstream:** the AI task "Check Answer" feeds the human task "Show what
  Chat Suggests"; "Get celebration message" feeds "Collect Prize"; "Get inspiration" feeds
  "You lose". The page also names a second, non-AI binding in the same model: "a REST
  Connector is used to query a service that returns a question and its answer".
- **Authority - data:** `not visible on the page` (the figure prints labels only; no
  variables or data objects appear in the brief or in the image).
- **Authority - control:** the exclusive gateway "Did you answer correctly" ("Yes" / "No")
  and the gateway "Lives left?" with its loop back to "Get Trivia Question", plus the human
  tasks "Show what Chat Suggests", "Collect Prize" and "You lose" that sit downstream of the
  AI tasks.
- **Input provenance:** the page says "A user is asked to enter a category for the trivia
  question. Then, a REST Connector is used to query a service that returns a question and
  its answer. The user then sees the question, types in their answer" - i.e. the AI check
  consumes the question and the typed answer.
- **Guards present:** the human task "Show what Chat Suggests" sits directly after "Check
  Answer", and the page says the user is shown both answers; no filter, prompt guard or
  audit log is named on the page.
- **Prompt / model detail visible:** the page states a prompt was added to the OpenAI
  connector - "I used the OpenAI connector and added the prompt:" - but the prompt text
  itself is not present in the brief and no model id is printed anywhere on the page.

## Notes for the researcher

The record captures the "Basic-trivia-bpmn-model-plus-openai" figure, not the sheet's
figure 1 (alt "Trivia-question-final-bpmn-model"), because the rulings file names the
former. The same post also shows the later, extended model ("Trivia-question-final-bpmn-model",
alt "Trivia-question-final-bpmn-model-optimize" for the Optimize heatmap view) and several
form screenshots; only the named figure is captured here. The OpenAI-bound tasks are
readable at 1400 px (verified by cropping and enlarging the glyphs: the swirl icon appears
on "Check Answer", "Get celebration message" and "Get inspiration"), but whether the glyph
is the connector's icon rather than a generic marker is a visual judgement, hence
`needs_visual_check: true`.
