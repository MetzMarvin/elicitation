# Pattern specification (fixed 2026-10-07, before any results were computed)

Replaces silhouette-optimised partitioning (`cluster.py`) as the way candidate patterns are formed.
Method reference: `004_method.tex`, Abstraction Procedure (steps 2-4) and the minimum-instance rule.

## Unit and membership

- Unit: the AI chain from `annotations/<source>/NNN.yaml`. Coverage is reported per workflow
  (artefact): a workflow is covered if at least one of its chains is a member of a pattern.
- A **pattern** is a complete profile: every slot of the chosen level has one value. A chain is a
  member iff its value equals the profile's value in every slot. Membership is crisp; a chain matching
  no pattern is residue. Overlap is possible only across chains of one workflow.
- Candidate profiles are the distinct profiles of fully determined chains (no `unknown` in any slot).
- **Pattern status:** >= 3 distinct workflows. Single-source patterns are kept and flagged
  (template reuse).
- Partial profiles (FCA, wildcard slots) are used only afterwards, to review merging near-identical
  profiles; never as the definition.

## `unknown`

Each slot holds the set of values compatible with the annotation. `unknown` writer, mutates or
human gate widens the set.
- **Lower bound:** a chain is a member only if every slot is determined and equal.
- **Upper bound:** a chain is a member if the profile's value is compatible in every slot.
Headline coverage = lower bound; upper bound reported alongside.

## Slots and levels

| Dimension | Slot | Coarse | Medium (main) | Fine |
|---|---|---|---|---|
| Function | structure | agent / non-agent | single-call / fixed-sequence / agent-loop | as medium |
| | operations | - | set of bins: classify-or-decide, extract, generate-or-summarise, plan-act | exact set of the 6 values |
| | autonomy | suggests / {decides, acts} | suggests / decides / acts | as medium |
| Provenance | least-trusted writer | outsider / not outsider | outsider / insider / system | as medium |
| Authority | output shape | free-text / not | closed-label / structured / free-text | as medium |
| | ungated reach | reaches external-recipient or public without human gate: yes / no | set of sink audiences reached with `human_gate: false` | set of audience x gate over all sinks |
| | mutates | none / some | none / internal-records / external-systems | as medium |
| Guards | guards | human-review yes / no | none / human-review / other only | exact set |

Least-trusted writer: the maximum over the chain's known writers (system < insider < outsider).
`unknown` entries widen the set to every value >= the known maximum.

**Dropped (researcher, 2026-10-07):** ungated call count (`invokes_without_gate`), at every level.
**Descriptors only (not in the profile):** sensitive data kind, number of AI elements, business domain.

## Posture level (added 2026-10-07, after the coarse/medium/fine and partial-profile runs; main level from now on)

The partial-profile review showed that coverage depends on which slots may vary. Instead of opening
slots by coverage, every slot is split a priori into a **fixed** part (defines the pattern) and a
**variable** part (reported as variation inside a pattern). Rule: a value is fixed if changing it
changes whether an un-interrupted path from an attacker to an effect exists, or which STRIDE threats
apply; it is variable if it only changes severity / likelihood (-> NIST scoring) or business semantics.

| Slot | Fixed (pattern) | Variable (within pattern) |
|---|---|---|
| structure | agent / non-agent | single-call vs fixed-sequence |
| autonomy | suggests / decides / acts | - |
| writer | outsider / insider / system (insider threat stays relevant: researcher) | - |
| shape | free-text / bounded | closed-label vs structured |
| ungated reach | external-recipient or public reached without human gate: yes / no | which internal audiences |
| mutates | none / some | internal-records vs external-systems (impact severity) |
| guards | human-review yes / no (make-or-break: researcher) | error-path-to-human, validation (often only format validation: researcher) |
| operations | - | operation bins |

Membership, `unknown` handling, threshold (>= 3 workflows) and denominator as above.

## H1 reading

Denominator: all 90 workflows (non-annotatable ones stay in it, INSTRUCTIONS.md §6); coverage over the
72 annotatable ones is reported alongside. Report per level: number of patterns, share of workflows covered (lower / upper), share carried by
the largest patterns, residue list. "Most workflows do not fall into a small set of patterns" holds
if medium covers a minority and coarse does not turn that into a large majority.
