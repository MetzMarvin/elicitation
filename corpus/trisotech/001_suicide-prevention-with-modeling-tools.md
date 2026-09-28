# Suicide Prevention with Modeling Tools — INCLUDE (trisotech)

url: https://www.trisotech.com/suicide-prevention-with-modeling-tools/
accessed: 2026-09-25
title: Suicide Prevention with Modeling Tools (blog, Dr. John Svirbely)
record: 001

bpmn_evidence:
  Figures 2 (2830x752) and 3 (2449x1691), both viewed at full size, are BPMN 2.0 process diagrams.
  Figure 2: a start event; user tasks carrying the person marker ("How do you feel today?", "Call
  9-8-8 to talk to someone", "Hot Line Recommendation"); a task carrying the OpenAI/ChatGPT marker
  ("Monitor Suicide Ideation"); data objects ("Journal", "High Risk Words", "Detection", "Triage
  Rules", "Hot Line Action") attached by dotted data associations; an exclusive gateway branching
  Low / High / Intermediate / Crisis; and end events ("Call Behavioral Specialist", "Refer to ER").
  Figure 3: three pools with lanes — "Behavioral Specialist"; "ER Suicide Prevention" with lanes
  Emergency Care Team and Behavioral Specialist; "Hospital In-Patient" with lanes Care Team and Case
  Worker — plus a separate pool "Behavioral Monitoring App", message start and intermediate events,
  exclusive and parallel gateways, the business-rule task "Triage Rules" carrying the table marker,
  and send tasks. The two drawings share task names, so figure 3 reads as the fuller version of the
  same clinical process.
  Negative check: the site publishes no .bpmn/.dmn/.cmmn XML anywhere (checked across all 768 saved
  content pages; the only .bpmn-looking hrefs are links out to bpmn.org), so the notation call is
  read from the drawings themselves.

ai_evidence:
  Inside the process: the task "Monitor Suicide Ideation" in figure 2 carries the OpenAI/ChatGPT
  swirl marker — the same mark this source uses for its "OpenAI Connector" logo — i.e. an LLM task
  bound into the process flow, not an AI mention in prose only. Figure 3 shows the same process
  without that marker (the human-only baseline).
  Page prose: "Figure 2 shows such a model that does monitoring a patient's personal journal using
  Generative AI." and "Several investigators have taken the approach of early detection of suicidal
  ideation, using natural language processing." and "Figure 2: A model using natural language
  monitoring to detect suicidal thoughts."

screenshot: 001_suicide-prevention-figure2-bpmn-ai-task.png
capture_quality: legible

researcher notes:
  * figure 1 on the page is a CDC statistics card, not a process artefact.
  * the page's own region carries AI terms: AI, natural language processing.
  * nothing was changed in any vendor tool; the figures were read from the saved page HTML.
