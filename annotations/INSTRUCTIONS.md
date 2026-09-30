# Annotation instructions (Step 2, Pattern Abstraction: annotation step)

Method reference: `chapters/thesis/004_method.tex`, Section `sec:method:pattern_abstraction:procedure`,
step one ("each artefact in the corpus is annotated along the security-relevant dimensions").
Input: the 90 reviewed workflows in `../corpus/<source>/NNN_*.md` (+ image / `.bpmn` next to each).
Output: one YAML file per workflow in `annotations/<source>/NNN.yaml`.

## 1. Workflow (Claude picks the next item, the researcher reads it first)

1. Claude presents the next unticked workflow from `PROGRESS.md`, in list order: its id, title,
   URL and the path of its image / `.bpmn` file. Nothing else: no summary, no reading of the
   diagram, so the researcher's reading is not anchored.
2. The researcher describes the workflow in prose, as rough as they like.
3. Claude reads the record (and its image or `.bpmn` if needed) and writes the YAML file from the
   researcher's prose. **The researcher's reading is authoritative.** Claude does not add
   properties the researcher did not state.
4. Before or right after writing, Claude reports in chat, as questions, not as edits:
   - contradictions between the prose and the record or diagram;
   - things the prose did not cover that the schema asks for (e.g. no statement on sensitive reads);
   - AI elements visible in the diagram that the prose did not mention.
   The researcher decides. Anything left unresolved goes into `open_questions`.
5. The researcher confirms; Claude ticks the workflow in `PROGRESS.md`.

Claude never edits `../corpus/` (the reviewed corpus is final) and never runs git write commands.

**The image (or `.bpmn`) is authoritative over the record.** Record texts are of low quality; where
the record's description and the diagram disagree, annotate the diagram and do not raise the
mismatch as a question.

**Machine translation counts as an AI element.**

## 2. Unit of annotation: the AI chain

The unit is the workflow. Inside it, annotate **AI chains**: the AI activities connected by data
flow, plus what they read and where their output goes.

- Most workflows have exactly one chain (`C1`).
- Split into `C1`, `C2`, ... only if AI parts share **no** data flow (e.g. an intake classifier and
  an unrelated closure summariser). Never combine properties across chains: untrusted input in C1
  and an external sink in C2 are not a combination.
- A chain carries the **widest** value of each property among its elements (highest autonomy,
  widest output shape, least-trusted writer). Risk is set by the weakest point.

## 3. No business logic

Record security-relevant roles only. No task names, no lane names, no domain nouns in coded fields.
Domain meaning is allowed only in `function.description` and `notes`, and only as much as needed to
recognise the workflow again. Paths are written in roles: `AI -> human -> external`.

## 4. `unknown` is not `none`

- `none`: the diagram shows the property is absent.
- `unknown`: the diagram does not show it (hidden data mappings, connector config, prompts).
Never write `none` because nothing is visible. Undercoding authority understates risk.

## 5. Schema

```yaml
artefact: <source>/<NNN>
annotated: YYYY-MM-DD
annotatable: true            # false: kept in the denominator, see section 6
chains:
  - id: C1
    ai_elements: <int>       # count of AI-bound elements in the chain, no labels
    structure: <single-call | fixed-sequence | agent-loop>
    function:
      description: "<short free text>"
      operations: [<classify | extract | summarise | generate | decide | plan-act>]
      autonomy: <suggests | decides | acts>
    reads_untrusted:         # who can write to what the chain ingests
      - writer: <outsider-writable | insider-writable | system-generated | unknown>
        evidence: <image | record | bpmn-xml | inferred | not-visible>
    reads_sensitive:         # confidential data in the chain's context
      - kind: <customer-pii | internal-docs | business-records | credentials | knowledge-base | none | unknown>
        evidence: <...>
    output:
      shape: <free-text | structured | closed-label>
      sinks:
        - audience: <external-recipient | public | internal-human | internal-system | control-flow>
          path: "<role path, e.g. AI -> human -> external>"
          human_gate: <true | false | unknown>
          evidence: <...>
    authority:
      invokes_without_gate: <int | unknown>   # tool/service calls reachable with no human in between
      mutates: <none | internal-records | external-systems | unknown>
    guards: [<human-review | error-path-to-human | validation | prompt-guard | confidence-threshold | ...>]
    notes: ""
open_questions: []
```

### Field definitions

| Field | Meaning |
|---|---|
| `structure` | `single-call`: one model call. `fixed-sequence`: several AI calls in a modelled order. `agent-loop`: the model chooses tools or next steps itself (e.g. ad-hoc sub-process driven by an agent). |
| `operations` | Verb classes, not business labels. `plan-act` = the model selects and triggers actions. |
| `autonomy` | `suggests`: a human consumes the output. `decides`: the output sets the process path (gateway, routing). `acts`: the model calls tools / triggers effects itself. |
| `writer` | Who can place content into the chain's input. `outsider-writable`: email, upload, web page, customer chat. `insider-writable`: employee form, internal ticket. `system-generated`: upstream task or database output. If the input derives from an earlier AI output fed by outsider content, it is `outsider-writable`. |
| `reads_sensitive.kind` | What confidential data sits in the model's context (retrieval, lookups, attached records). |
| `shape` | `closed-label`: one of a fixed set of values (low exfiltration bandwidth). `structured`: fields / JSON. `free-text`: prose, drafts. |
| `audience` | Who receives the output. `control-flow`: it decides a gateway. |
| `human_gate` | Whether a human sees the output before it reaches that sink. |
| `invokes_without_gate` | Count of service/tool calls the chain can trigger with no human in between. |
| `evidence` | Where the claim comes from: seen in the `image`, stated in the `record` text, read in `bpmn-xml`, `inferred` by the researcher, or `not-visible` (goes with `unknown`). |

Controlled values may grow: a new value needs the researcher's approval and a line in section 7.

## 6. Non-annotatable workflows

If the workflow cannot be read (illegible, too little visible): `annotatable: false`, no `chains`,
reason in `open_questions`. It stays in the classification denominator; it is never deleted.

## 7. Vocabulary changes

Append one line per change (date, field, value added or redefined, reason).

- 2026-09-30: schema frozen for annotation start.
