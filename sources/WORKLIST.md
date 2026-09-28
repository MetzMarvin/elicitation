# Gate 1 worklist for the researcher

This is a short checklist. The detail behind each item is in `OPERATOR-TODO.md` (ids
in brackets) and the evidence is in `candidate-vendors.md`. When you rule on a source,
edit `criteria:` and `provisional:` in its `assignments/<slug>.md`.

State as of 2026-09-24: **53 sources assessed.** 14 `QUALIFIES`, 33 `UNCLEAR-NEEDS-RULING`,
5 `OUT` (C2), 1 not identified. There are 47 assignment files.

## 1. Rulings that settle many sources at once (≈15 min)

- [x] **General C4 rule** [B5–B7] — ADOPTED as worded 2026-09-24; 11 files flipped, Imixs later dropped by operator (OUT C4): "sells a commercially supported BPMN engine/suite *and*
      is found through ≥2 search channels". Admits: FireStart, Frends, CIB seven, FlowX.AI,
      LoyJoy, Scheer PAS, Aletyx, Imixs (needs a 2nd channel), QuantumBPM, Flows for APEX,
      Atamya, Citeck.
- [x] **Batch C1 rule-out** [B14] — RULED OUT (C1), all 12 incl. Signavio, 2026-09-24: ADONIS, Apache KIE, Operaton, Activiti, ARIS, iGrafx,
      OpenText, TIBCO, Visual Paradigm, Cardanit, Modelio. **Add SAP Signavio** [B10]: the
      check has been run and nothing was found.
- [x] **B3, process-to-agent substitution counts as C1?** — YES 2026-09-24; IBM watsonx and Oracle OIC now qualify. Affects IBM watsonx. Oracle is
      recommended in either case.
- [x] **B4, practitioner/consultancy sources in scope?** — NO, vendors only (2026-09-24). Miragon OUT-SCOPE; Channel 6 closed. Method chapter must state the restriction. Affects Miragon and the whole
      Channel 6 list.

## 2. Single-source rulings (≈10 min)

- [x] **B12 Pega** — OUT (C2) 2026-09-24, operator checked canvas.: is Case Lifecycle / Process Modeler BPMN 2.0? Recommendation: `OUT (C2)`.
- [x] **AgilePoint** — OUT (C2) 2026-09-24, operator checked canvas. [B14 note]: same question. One canvas screenshot settles it.
- [x] **B11 Celonis** — OUT (C1) 2026-09-24, AI about processes; A4 moot.: "AI-insertion points" is C1? Is the docs login a free account?
- [x] **B9 Nintex**, **GBTEC**, **Comidor** — all OUT (C1) 2026-09-24.: C1 open, low priority.
- [x] **B13 "Berger BPM"** — name withdrawn by operator 2026-09-24.: which vendor did you mean?

## 3. Access actions (you, in the browser profile)

- [x] **A1** (operator logged in 2026-09-24; verify at Pass 2 start) UiPath free tenant `masterthesismetz`: log in and leave the session open.
- [x] **A4** (moot, Celonis OUT) Celonis ID: does a free sign-up exist? If yes, create an account.
- [ ] **A2/A2b**: be available for IFS bot challenges and Google captchas during Pass 2.

## 4. Thesis text follow-ups

- [ ] Tighten C3 wording in `sec:method:vendor_sampling` to "no paid subscription and no sales
      gate" (follows from B0).
- [ ] State the vendors-only restriction of Step 1 (B4) and that process-to-agent
      substitution counts as C1 (B3).
- [ ] Report the Gate 1 outcome: 53 assessed → 27 qualify, 16 OUT (C1), 7 OUT (C2),
      1 OUT (C4, Imixs), 1 OUT (scope), 1 withdrawn. Table: `candidate-vendors.md`, "Gate 1
      outcome". Note that Celonis (expected to fail C2) was BPMN and failed on C1 instead,
      and that Pega only fell under C2 after a human looked at the canvas.
- [ ] Consider the "AI about processes vs AI in processes" finding. The modelling vendors
      (Signavio, ARIS, ADONIS, iGrafx) are on the one side and the engine vendors on the
      other. See `candidate-vendors.md`, "An emerging category".

## 5. Optional recall work (only if you want more coverage)

- [x] (declined 2026-09-24) Channel 5 (G2/Capterra) has never been worked.
- [x] (declined 2026-09-24) Channel 7 (academic) has never been worked.
- [x] (declined 2026-09-24) Unopened grid names: Tallyfy, Moxo, JointJS, Lucidflow.ai, ba-copilot, MarvelX,
      Entoura, processcamp.io, justflow.it, yourcompanyos.io, Sapiens Decision, Eraser.io,
      Lucid, Visio, aiprocess.design. ZeaProcess and Dragon1 are opened but unscored.
- [x] SAP Hub and the Pega gallery are moot (both vendors OUT). The Bizagi and Appian template galleries move to Pass 2 as entry points of their assignments.

## 6. Housekeeping

- [ ] (deferred by operator: sync after the full elicitation, 2026-09-24) Copy `elicitation/sources/` into the thesis repo's `notes/elicitation/sources/` (the
      two copies are out of sync). No git actions have been taken.
