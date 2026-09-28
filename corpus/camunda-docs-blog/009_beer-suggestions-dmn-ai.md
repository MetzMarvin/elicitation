---
n: 152
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: Beer Suggestions with DMN and AI
url: https://camunda.com/blog/2024/09/beer-suggestions-dmn-ai/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: the captured figure is a BPMN model, read at full width - start event "Give Taste Preferences", the task "Decide on Beer Style" (drawn with a decision-table icon), an exclusive gateway with an X marker labelled "Was a suitable beer Found?", the tasks "Find Beer In Location" and "Find Alternative", the task "Create Email Body", a second exclusive gateway with an X marker, the task "Send Email with Beer Suggestions" (drawn with a blue SendGrid-style icon) and the end event "Suggestion Given"
bpmn_evidence_quote: "Adding this DMN table to a BPMN model lets us expand the scope of this invaluable process"
ai_evidence: two tasks in the captured model carry the same rosette-shaped connector icon - "Find Beer In Location" (on the gateway's "found a beer" branch) and "Find Alternative" (on the other branch) - and the page identifies the implementation: "I use the OpenAI Connector to ask ChatGPT to suggest places to find nearby beers in that style. If not, you can trust ChatGPT to suggest an alternative."
ai_evidence_quote: If the DMN table did manage to find a beer for you, I use the OpenAI Connector to ask ChatGPT to suggest places to find
artefacts:
  screenshot: 009_beer-suggestions-dmn-ai.png
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

The post describes a small beer-recommendation use case, and the captured figure is its BPMN
model: start event "Give Taste Preferences" into the task "Decide on Beer Style" - the step
backed by the DMN table the post is about - then the exclusive gateway "Was a suitable beer
Found?". The "found" branch runs through the task "Find Beer In Location" to a second
exclusive gateway; the other branch runs through "Find Alternative" and "Create Email Body"
into the same gateway; both merge into the task "Send Email with Beer Suggestions" and the
end event "Suggestion Given".

Two of those tasks carry the same rosette-shaped connector icon, and the page names what they
are bound to: "I use the OpenAI Connector to ask ChatGPT to suggest places to find nearby
beers in that style. If not, you can trust ChatGPT to suggest an alternative." The page also
states the surrounding orchestration - "Adding this DMN table to a BPMN model lets us expand
the scope of this invaluable process by letting us integrate other systems and also address
different responses depending on the results" - and the delivery step: "In both cases, then
an email is sent using the SendGrid Connector with the suggested beverage."

## Observations (description only, no interpretation)

- **AI activity - function:** suggesting places and alternatives - "ask ChatGPT to suggest
  places to find nearby beers in that style"; on the other branch "you can trust ChatGPT to
  suggest an alternative".
- **AI activity - element type:** two BPMN tasks in the model, distinguished on the canvas by
  the connector's icon, whose implementation is the OpenAI Connector; a third task ("Decide
  on Beer Style") is the DMN-backed decision, drawn with a decision-table icon rather than
  the connector icon.
- **Authority - downstream:** the second exclusive gateway, which merges both branches into
  the task "Send Email with Beer Suggestions"; delivery itself is not the AI element's job -
  "an email is sent using the SendGrid Connector with the suggested beverage."
- **Authority - data:** not visible on the page - the captured figure prints no variables or
  data objects, and the brief carries no mapping detail.
- **Authority - control:** the exclusive gateway "Was a suitable beer Found?" that decides
  which of the two AI tasks runs, and the merging gateway before the email task.
- **Input provenance:** the taste preferences entered at the start of the process ("Give Taste
  Preferences"); the page describes the DMN table's output as "one or more beer styles that
  would suit your preferences", which is what the AI task then works from.
- **Guards present:** not visible on the page - the model has no review or confirmation step
  in the captured figure and the page describes none.
- **Prompt / model detail visible:** not visible on the page - the page names ChatGPT and the
  OpenAI Connector, but no model id, prompt text or connector parameter appears in the brief.

## Notes for the researcher

The BPMN figure is the post's own model (alt "Bpmn-beer-recommendations-camunda"), but it is
not one of the two cells the visual pass selected, so it is reached with `shotall`; the
`bpmn_evidence_quote` is the opening clause of a longer page sentence, which continues "by
letting us integrate other systems and also address different responses depending on the
results"; the
selected cells are the form screenshot (alt "Deploy-process") and a Monitor view (alt
"Monitor-process"). The page also carries a DRD figure ("A DRD with options for deciding which
beer to recommend") and a rules table ("Beer-rules") that document the DMN side of this same
model, plus an email screenshot ("Beer-suggestions-email"). The source asset is 1200x278 and
the w=1400 download is an upscale to 1400x324; the labels are readable at that width.
