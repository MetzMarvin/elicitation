---
n: 0
url: https://github.com/bonitasoft/bonita-connector-ai/blob/main/bonita-connector-ai-anthropic/src/test/resources/AnthropicAIDemo-1.0.proc
source: bonitasoft
accessed: 2026-09-25
verdict: INCLUDE
needs_human_ruling: false
question: >-
  ANSWERED (elicitation-5a, 2026-09-25): the census protocol puts this artefact class
  deliberately in scope - "diagrams where the AI element is only visible as a task
  *property* or implementation binding, not as a distinct BPMN element type" - so the
  verdict is INCLUDE and the question is closed. It is kept here as the record of what was
  asked before the ruling. It read: the file is a Bonita `.proc` process in which a BPMN
  service task "Ask Claude" carries the Anthropic connector
  (`definitionId="anthropic-ask"`, `event="ON_ENTER"`) with a prompt, shipped as a *test
  resource* of the connector's repository rather than a published product artefact - does
  it count as a corpus item, or as binding evidence only?
bpmn_evidence: >-
  The file is BPMN 2.0 XML in Bonita's `.proc` serialisation, so the BPMN evidence is decisive:
  `<process:MainProcess xmi:id="_AiDemoMp01" name="AnthropicAIDemo" bonitaModelVersion="9">`,
  the pool `process:Pool name="Anthropic AI Demo"`, the lane `process:Lane name="Employee lane"`,
  the start event `process:StartEvent name="Start"`, the service task `process:ServiceTask
  name="Ask Claude"`, and the sequence flows `_AiDemoFlow01` / `_AiDemoFlow02` that connect them.
ai_evidence: >-
  The AI element is inside the process: the connector `process:Connector xmi:id="_AiDemoConn01"
  name="Anthropic Ask" definitionId="anthropic-ask" event="ON_ENTER"` is attached to the service
  task "Ask Claude", and its parameters are set - `key="userPrompt"` with content "What is the
  capital of France? Answer with just the city name." and `key="systemPrompt"` with content "You
  are a helpful assistant." The connector's output is bound to the process variable `askResult`
  (`process:Data name="askResult"`), so the model's answer is a data object of the process.
artefacts:
  - screenshot: 010_anthropic-ai-demo-proc.png
  - file: ledgers/bonitasoft.raw/AnthropicAIDemo-1.0.proc
capture_quality: legible
capture_width_px: 1884
---

## What the file shows

The repository `github.com/bonitasoft/bonita-connector-ai` is the AI connector project (its
sibling modules are `bonita-connector-ai-azure`, `-openai`, `-mistral`, ...). Under
`bonita-connector-ai-anthropic/src/test/resources/` it ships `AnthropicAIDemo-1.0.proc`, the
process used to test the connector. Read as XML it is

- `process:MainProcess name="AnthropicAIDemo" bonitaModelVersion="9"`,
- a pool "Anthropic AI Demo" with one lane "Employee lane" (`actor="_AiDemoActor01"`),
- a start event "Start",
- a service task "Ask Claude" with the connector "Anthropic Ask" (`definitionId="anthropic-ask"`,
  `event="ON_ENTER"`, `definitionVersion="1.0.0"`) whose parameters are the two prompts quoted
  above,
- the connector's output bound to the process data `askResult` through an
  `expression:Operation` of type `ASSIGNMENT`,
- and the sequence flows that connect the elements.

The capture is a render of the file's own first lines (the header is one long line of namespace
declarations; the pool, lane, start event and service task follow).

## Observations

- This is the strongest AI-in-BPMN evidence in the whole source: the AI is not described, it is
  *declared* - a `process:ServiceTask` whose `process:Connector` is the Anthropic one, with the
  prompt constants and the output binding visible in the file itself.
- **It is INCLUDE, ruled by the orchestrator on 2026-09-25.** Its being a demo (the prompt asks for
  the capital of France) and a *test resource* of the vendor's public repository is not a ground
  for doubt: the census protocol lists "diagrams where the AI element is only visible as a task
  *property* or implementation binding" as deliberately in scope, and shared rules §4 bans
  "internal template / boilerplate listing" as a reason to hold an artefact back. The repository is
  inside this source's enumerated population, so the artefact is a collected instance.
- The raw file is kept beside this record in `ledgers/bonitasoft.raw/` so the XML can be read
  without hitting the network again.

## Notes for the researcher

Record 011 is the Azure twin of this file, from the same repository; it adds a user task "Review
Results" after the AI step, i.e. the human-in-the-loop element the protocol asks not to abstract
away. Records 001-009 are the connector *documentation* pages - the same binding, documented in
prose and a generic diagram rather than in a readable process file; they stay UNCERTAIN because the
cross-source question "AI in a process documented without a published diagram" is the researcher's
to rule on.
