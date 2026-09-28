---
n: 1274
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: How to use Camunda Platform 8 to Orchestrate Microservices
url: https://camunda.com/blog/2023/06/how-to-use-camunda-platform-8-orchestrate-microservices/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: downloadable BPMN 2.0 XML (<bpmn:process id="Process_songRequest" name="Song Request" isExecutable="true">, 6 bpmn:serviceTask, bpmn:eventBasedGateway, bpmn:exclusiveGateway, 2 bpmn:textAnnotation) linked from the page, plus the page's own figure alt "The BPMN diagram showing the process for song requests."
bpmn_evidence_quote: "Here’s my process diagram file named song-requests.bpmn that implements all the steps described above."
ai_evidence: two bpmn:serviceTask carry zeebe:modelerTemplate="io.camunda.connectors.OpenAI.v1" with the OpenAI icon embedded as zeebe:modelerTemplateIcon - "Analyze Song Request" (text annotation "Ask OpenAI whether this song is appropriate for the type of event") and "Get Song Lyrics"; both POST to https://api.openai.com/v1/chat/completions with operation=chat, internal_model=gpt-3.5-turbo, internal_systemMessage="You are a helpful assistant", authentication.token=secrets.OPENAI_API_KEY, resultVariable openaiResponse1/openaiResponse2
ai_evidence_quote: "Determine whether song is appropriate using OpenAI"
artefacts:
  screenshot: 001_song-requests-bpmn-diagram.png
  archive: null
  bpmn_xml: 001_song-requests.bpmn
duplicate_of: null
access: public
capture_source: bpmn-xml
capture_quality: legible
capture_width_px: 1400
capture_method: chrome-devtools-mcp page fetch, then the page's github.com blob link converted to raw.githubusercontent.com for the XML; the diagram figure taken from the cdn.sanity.io URL decoded out of the page's /_next/image proxy at w=1400
---

## What the page shows

The blog walks through a "Song Request" process that accepts song requests for an event
(wedding, company retreat) through a Google Form and decides whether each song is
appropriate. The rendered diagram (figure 1 of the post) is a BPMN process: a start event
"Create Instance", a service task "Ask for Song Request via Email", an event-based gateway
forking to a timer ("Wait to send reminder", P3D) and to the message catch event "Form
Submitted", then the task "Analyze Song Request" carrying the OpenAI connector icon, an
exclusive gateway "Is this song appropriate?" with "Yes" / "No" / "Maybe" flows into three
notification tasks, and a user task "Review Song Request" that consumes "Get Song Lyrics"
(the second OpenAI-bound task). Two text annotations sit on the canvas: "Ask OpenAI whether
this song is appropriate for the type of event" and "If OpenAI is unsure whether the song
is appropriate, use Camunda Forms to display the Song Lyrics and decide to approve or
reject".

## Observations (description only, no interpretation)

- **AI activity - function:** the page says the OpenAI task decides on the song: "the
  OpenAI Connector makes a call to the Chat Completions REST API and asks whether this song
  title and artist is appropriate for the event", and "OpenAI responds with either 'Yes,'
  'No,' or 'Maybe,' along with an explanation".
- **AI activity - element type:** two BPMN service tasks bound to an AI connector element
  template (`zeebe:modelerTemplate="io.camunda.connectors.OpenAI.v1"`), i.e. tasks whose
  implementation is the OpenAI Chat Completions API call.
- **Authority - downstream:** the AI output (`openaiResponse1`) is consumed by the
  exclusive gateway "Is this song appropriate?" which routes to "Notify Song Request
  Accepted!", "Notify Song Request Rejected" or "Notify Song Request Under Review"; the
  second call's output (`openaiResponse2`) feeds the user task "Review Song Request".
  Sending is done by four separate SendGrid connector tasks.
- **Authority - data:** process variables written by the start event are `person.name`,
  `person.email`, `eventType` (default "wedding"); the form message event maps
  `song.artist` and `song.title` from the form; the SendGrid tasks read `song.title`,
  `song.artist`, `song.lyrics`.
- **Authority - control:** the exclusive gateway "Is this song appropriate?" (default flow
  "Flow_0w1px0x") and the human task "Review Song Request" with the form
  `camunda-forms:bpmn:userTaskForm_10je4nr`.
- **Input provenance:** the song title and artist arrive from a Google Form submitted by an
  invited guest; the form submission calls a Google Cloud Function that publishes a Zeebe
  message which the process catches.
- **Guards present:** a human review gate - the "Maybe" branch routes to a user task where a
  person sees the lyrics and approves or rejects.
- **Prompt / model detail visible:** yes - `internal_model = gpt-3.5-turbo`,
  `internal_systemMessage = You are a helpful assistant`, `operation = chat`,
  `url = https://api.openai.com/v1/chat/completions`, `authentication.token =
  secrets.OPENAI_API_KEY`, `connectionTimeoutInSeconds = 30`. No user-prompt template text
  is visible in the XML beyond the message content sent by the connector.

## Notes for the researcher

The XML is byte-for-byte the model the post links (camunda-community-hub/camunda-song-request,
src/main/resources/song-requests.bpmn). The post is a 2023 microservices-orchestration
tutorial, not an article about AI - the AI element is simply one of several connectors used,
which makes it a clean example of an AI task embedded in an ordinary BPMN process. The two
OpenAI tasks are visually marked on the canvas by the OpenAI logo icon supplied as
`zeebe:modelerTemplateIcon` (a base64 SVG, title "OpenAI"); the icon is what makes the AI
element readable in the published figure.
