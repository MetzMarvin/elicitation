---
n: 1434
source: camunda-blog
source_name: Camunda (vendor blog)
source_type: vendor blog
title: Three Ways Camunda Speaks MCP (And Why the Direction Matters) | Camunda
url: https://camunda.com/blog/2026/08/three-ways-camunda-speaks-mcp-and-why-the-direction-matters/
accessed: 2026-09-26
verdict: INCLUDE
needs_human_ruling: false
question: null
needs_visual_check: false
bpmn_evidence: the captured figure is a BPMN model - a large container labelled "Plan rebooking (AI agent)" with the purple star badge at its top-left corner and the ad-hoc tilde at its bottom edge, two green tool tasks inside it ("Find alternate flights", "Find overnight hotel"), a nested sub-process "Commit rebooking (requires approval)" holding a start event "Commit requested", the user task "Approve rebooking", the exclusive gateway "Approved?" with "yes" / "no" flows into "Build confirmed result" / "Build rejected result", a "Merge" gateway and the "Commit result ready" event, two start events outside the container ("Disruption reported" and "Disruption reported (via MCP tool)", the latter with an MCP glyph), and the end event "Travel summary"
bpmn_evidence_quote: "It's modeled as a BPMN ad-hoc sub-process, a set of tools the agent selects from at runtime"
ai_evidence: the AI element is the ad-hoc sub-process itself - the container "Plan rebooking (AI agent)" (purple star, tilde) whose two boxes are the agent's tools - and the page binds it explicitly: "This pattern is Camunda as an MCP client . It lives inside the AI Agent connector's ad-hoc sub-process model." and "Handle Flight Disruption wraps an AI Agent connector in an ad-hoc sub-process with two MCP tools available to it: find_alternate_flights on a flight-status MCP server, and find_overnight_hotel on a hotel MCP server."
ai_evidence_quote: "This pattern is Camunda as an MCP client . It lives inside the AI Agent connector's ad-hoc sub-process model."
artefacts:
  screenshot: 024_three-ways-camunda-speaks-mcp-and-why-the-direction-matters.png
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

The post lays out three ways Camunda meets the Model Context Protocol (as MCP client, as MCP
server, and as a process exposed as an MCP tool), and its second figure (alt "Human in the
loop pattern") is the BPMN model behind the first of those. The model's centre is the large
container labelled "Plan rebooking (AI agent)" - purple star badge at its top-left corner,
ad-hoc tilde at its bottom edge - which holds two green tool tasks, "Find alternate flights"
and "Find overnight hotel", each carrying an MCP connector glyph and a small counter badge.

Nested inside that container is the sub-process "Commit rebooking (requires approval)":
a start event "Commit requested" into the user task "Approve rebooking", the exclusive
gateway "Approved?" whose "yes" and "no" flows run into "Build confirmed result" and "Build
rejected result", then a "Merge" gateway and the "Commit result ready" event. Two start
events feed the model from outside, "Disruption reported" and "Disruption reported (via MCP
tool)", and the flow leaves the container to the end event "Travel summary".

## Observations (description only, no interpretation)

- **AI activity - function:** the page says of this model "The agent gets the disrupted
  flight and decides what it needs.", and of the pattern generally "You give an LLM-backed
  agent a set of tools to choose from, and one (or several) of those tools can be an MCP
  Client connector pointing at any external MCP server".
- **AI activity - element type:** a BPMN ad-hoc sub-process configured as an AI agent - the
  page's own words are "This pattern is Camunda as an MCP client . It lives inside the AI
  Agent connector's ad-hoc sub-process model." and "Handle Flight Disruption wraps an AI Agent
  connector in an ad-hoc sub-process with two MCP tools available to it".
- **Authority - downstream:** the agent's tools as printed in the figure are "Find alternate
  flights" (counter badge "2") and "Find overnight hotel" (counter badge "1"), which the page
  names as "find_alternate_flights on a flight-status MCP server, and find_overnight_hotel on
  a hotel MCP server"; the commits the agent can make are the nested sub-process's "Build
  confirmed result" and "Build rejected result".
- **Authority - data:** `not visible on the page` for this figure (no variables or data
  objects are printed in it). The only field names the page gives belong to a different
  artefact - the MCP start event of the "Rebook Trip" process, "with travelerId and
  originalFlightNumber as required inputs".
- **Authority - control:** the user task "Approve rebooking" inside "Commit rebooking
  (requires approval)" and the gateway "Approved?" with its "yes" / "no" flows, the "Merge"
  gateway and the "Commit result ready" event; the page describes the intent as "an
  intermediate event can gate an MCP tool call behind a confirmation step before it executes.
  In the demo, that gate sits in front of anything that actually commits the traveler to a
  new booking".
- **Input provenance:** the two start events "Disruption reported" and "Disruption reported
  (via MCP tool)" (the second carrying an MCP glyph), which the page ties to the agent
  receiving the disrupted flight.
- **Guards present:** the human confirmation gate - "Approve rebooking" with the "Approved?"
  gateway - inside the commit sub-process; the page says of the wider design "Camunda doesn't
  hide 'which tool did the agent pick' inside a black box. It's modeled as a BPMN ad-hoc
  sub-process, a set of tools the agent selects from at runtime, so tool selection is a
  visible, auditable part of the process".
- **Prompt / model detail visible:** `not visible on the page` - no model id and no prompt
  text are printed; the page describes the agent only as "an LLM-backed agent". The tool
  names it prints are "find_alternate_flights" and "find_overnight_hotel".

## Notes for the researcher

The captured figure is the post's only BPMN figure; its other figure (alt "Diagram showing
Camunda cluster with three doorways for working with MCP") is an architecture box diagram and
is not captured. The figure is a Camunda Modeler canvas with blue/orange annotation frames
added over the model, and its labels are readable at 1400 px (verified by enlarging the
container and its tools). `needs_visual_check` stays true because the AI element is
identified by the container's label and the purple star rather than by a task-level AI icon -
the two tool tasks carry MCP connector glyphs instead.
