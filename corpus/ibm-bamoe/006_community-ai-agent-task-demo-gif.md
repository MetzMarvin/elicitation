---
n: 132
record: 006
url: https://community.ibm.com/community/user/blogs/adarsh-v-k/2025/11/28/introducing-ai-agent-task-advanced-ai-integration
source: ibm-bamoe
surface: community:ibm.com
accessed: 2026-09-25
verdict: INCLUDE
needs_human_ruling: false
question:
bpmn_evidence: |
  The post's animation (ai-agent-task.gif, 1200x675, 234 frames) is a BAMOE Canvas session on the
  project header "Workflow | Demo" with the tab bar reading "BPMN Editor" and the canvas watermark
  "BPMN 2.0" (footer "React Flow"). Across the frames the BAMOE Canvas palette is shown with its
  "AI" group expanded - "Gen AI Task" (sparkle) and "AI Agent Task" (robot) - next to "Flexible
  processes > Milestone", and an AI Agent Task node is dragged from the palette and placed on the
  dotted process canvas. The placed node, the dotted canvas and the editor chrome are the evidence;
  the node is a task shape standing alone on the canvas, so no sequence flow is visible in this
  capture.
ai_evidence: |
  The placed node's panel is open in the final frames: "AI Agent Task" with Langflow Account *
  ("Select a Langflow account"), Agent * ("Select an agent"), Input * `{{aiAgentInput}}` with the
  hint "The input data for the agent. Use {{variableName}} for dynamic content.", a Preview table
  (Variable aiAgentInput / "Enter the value"), a greyed "Test Agent" button and the warning "You are
  not currently authenticated with Langflow, or your session has expired. Please authenticate to
  continue.", and the node's "Data mapping (in: 1, out: 1)" and "onEntry / onExit" sections.
artefacts:
  - screenshot: 006_ibm-bamoe-ai-agent-task-gif-frame212.png
  - screenshot: 006_ibm-bamoe-ai-agent-task-provider-dialog.png
  - file: ledgers/_bamoe_comm/ai-agent-task.gif
  - file: ledgers/_bamoe_comm/gif_strip.png
capture_quality: legible
capture_width_px: 1200
---

## What the file shows

The IBM Community post "Introducing AI Agent Task: Advanced AI Integration for BAMOE Business
Processes", whose opening animation is a screen recording of the BAMOE Canvas editor. Its own words
for the node: "This is a new BPMN workflow node that helps you use any AI agent or flow you build in
Langflow, right inside your BPMN workflows."

- Frames early in the animation: the empty canvas and the palette's "AI" group holding **Gen AI
  Task** and **AI Agent Task**, above "Flexible processes > Milestone".
- Frame 212 (the capture): the **AI Agent Task** node placed on the canvas and selected, with its
  property panel open (Langflow Account, Agent, Input `{{aiAgentInput}}`, Preview, Test Agent,
  Data mapping, onEntry/onExit), and the not-authenticated warning visible.
- The second capture is the post's "Select a provider" dialog (2400x1796): the AI section listing
  watsonx, Ollama and OpenAI with **Langflow** highlighted, above the Git section (GitHub, Bitbucket,
  GitHub IBM, GitLab) and the Cloud section.

## Observations

- The AI node here is a node the editor lets you *drag into* a BPMN model - the recorded gesture is
  exactly the claim in the post's text ("a BPMN workflow node ... right inside your BPMN workflows").
- Both AI node types appear together in the palette in one frame, side by side: the sparkle (Gen AI
  Task, record 001) and the robot (AI Agent Task, records 003 and 008). This is the widest single
  view of the AI palette in the corpus.
- The provider dialog shows the AI providers as *one* section of the provider list, alongside Git and
  Cloud providers - the AI binding is an account-level connection in the same UI as a Git connection.

## Notes for the researcher

- The GIF is the primary evidence and is kept whole (`ledgers/_bamoe_comm/ai-agent-task.gif`, 234
  frames); frame 212 is extracted as the still capture because it is the frame where the node is
  placed *and* the panel is open. The six-frame strip `gif_strip.png` shows the gesture end to end.
- The node is placed on an otherwise empty canvas in this animation: the post demonstrates the node
  type, not a process. For the node inside a complete process, records 005 and 008 are the captures.
- The post's remaining figures were screened on contact sheets as the node's configuration dialogs
  (provider/account connection, VS Code sign-in, agent selection, data mapping, test, logs); the two
  artefacts listed above are the ones read at full size and are the ones this record rests on.
