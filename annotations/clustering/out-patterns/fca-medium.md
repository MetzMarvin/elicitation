# Partial-profile review (medium level, lower bound)

91 chains / 79 annotatable / 97 workflows. Slots: structure, operations, autonomy, writer, shape, ungated-reach, mutates, guards.
Kept slots must include writer, >= 1 of structure/operations/autonomy, >= 1 of shape/ungated-reach/mutates.

## Coverage when k slots are left open

| k open | partial profiles with >= 3 workflows | workflows covered (of 90) | of 72 |
|---|---|---|---|
| 0 | 3 | 9 (9%) | 11% |
| 1 | 23 | 20 (21%) | 25% |
| 2 | 78 | 40 (41%) | 51% |
| 3 | 154 | 54 (56%) | 68% |
| 4 | 168 | 58 (60%) | 73% |

## Nearest neighbour

Differing slots between a chain and the closest chain of another workflow (undetermined slots count as agreeing):

| differing slots | chains |
|---|---|
| 0 | 32 |
| 1 | 35 |
| 2 | 21 |
| 3 | 3 |

## Concepts (distinct member sets), by fewest open slots then size

### K1: 3 workflows, 0 slot(s) open (-), 2 source(s)

Defined by: structure=single-call; operations={classify-or-decide}; autonomy=decides; writer=outsider; shape=closed-label; ungated-reach={control-flow}; mutates=none; guards=none
Closure (all members agree): structure=single-call; operations={classify-or-decide}; autonomy=decides; writer=outsider; shape=closed-label; ungated-reach={control-flow}; mutates=none; guards=none
Sources: camunda-marketplace 2, camunda-docs-blog 1
Members: camunda-docs-blog/007/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1

### K2: 3 workflows, 0 slot(s) open (-), 2 source(s)

Defined by: structure=fixed-sequence; operations={classify-or-decide, generate-or-summarise}; autonomy=decides; writer=outsider; shape=free-text; ungated-reach={control-flow, external-recipient}; mutates=none; guards=none
Closure (all members agree): structure=fixed-sequence; operations={classify-or-decide, generate-or-summarise}; autonomy=decides; writer=outsider; shape=free-text; ungated-reach={control-flow, external-recipient}; mutates=none; guards=none
Sources: flows-for-apex 2, quantumbpm 1
Members: flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1

### K3: 3 workflows, 0 slot(s) open (-), 2 source(s)

Defined by: structure=single-call; operations={classify-or-decide}; autonomy=decides; writer=outsider; shape=structured; ungated-reach={control-flow}; mutates=none; guards=none
Closure (all members agree): structure=single-call; operations={classify-or-decide}; autonomy=decides; writer=outsider; shape=structured; ungated-reach={control-flow}; mutates=none; guards=none
Sources: uipath-marketplace 2, trisotech 1
Members: trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/007/C2

### K4: 6 workflows, 1 slot(s) open (shape), 4 source(s)

Defined by: structure=single-call; operations={classify-or-decide}; autonomy=decides; writer=outsider; ungated-reach={control-flow}; mutates=none; guards=none
Closure (all members agree): structure=single-call; operations={classify-or-decide}; autonomy=decides; writer=outsider; ungated-reach={control-flow}; mutates=none; guards=none
Sources: camunda-marketplace 2, uipath-marketplace 2, camunda-docs-blog 1, trisotech 1
Members: camunda-docs-blog/007/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/007/C2

### K5: 4 workflows, 1 slot(s) open (mutates), 3 source(s)

Defined by: structure=single-call; operations={classify-or-decide}; autonomy=decides; writer=outsider; shape=closed-label; ungated-reach={control-flow}; guards=none
Closure (all members agree): structure=single-call; operations={classify-or-decide}; autonomy=decides; writer=outsider; shape=closed-label; ungated-reach={control-flow}; guards=none
Sources: camunda-marketplace 2, newgen 1, camunda-docs-blog 1
Members: camunda-docs-blog/007/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1, newgen/037/C1

### K6: 4 workflows, 1 slot(s) open (ungated-reach), 2 source(s)

Defined by: structure=agent-loop; operations={classify-or-decide, generate-or-summarise, plan-act}; autonomy=acts; writer=outsider; shape=free-text; mutates=internal-records; guards=none
Closure (all members agree): structure=agent-loop; operations={classify-or-decide, generate-or-summarise, plan-act}; autonomy=acts; writer=outsider; shape=free-text; mutates=internal-records; guards=none
Sources: camunda-docs-blog 3, camunda-marketplace 1
Members: camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-marketplace/006/C1

### K7: 3 workflows, 1 slot(s) open (ungated-reach), 2 source(s)

Defined by: structure=agent-loop; operations={classify-or-decide, generate-or-summarise, plan-act}; autonomy=acts; writer=outsider; shape=free-text; mutates=none; guards=none
Closure (all members agree): structure=agent-loop; operations={classify-or-decide, generate-or-summarise, plan-act}; autonomy=acts; writer=outsider; shape=free-text; mutates=none; guards=none
Sources: camunda-marketplace 2, camunda-docs-blog 1
Members: camunda-docs-blog/012/C1, camunda-marketplace/165/C1, camunda-marketplace/255/C1

### K8: 3 workflows, 1 slot(s) open (ungated-reach), 2 source(s)

Defined by: structure=agent-loop; operations={classify-or-decide, generate-or-summarise, plan-act}; autonomy=acts; writer=outsider; shape=free-text; mutates=none; guards=human-review
Closure (all members agree): structure=agent-loop; operations={classify-or-decide, generate-or-summarise, plan-act}; autonomy=acts; writer=outsider; shape=free-text; mutates=none; guards=human-review
Sources: camunda-marketplace 2, camunda-docs-blog 1
Members: camunda-docs-blog/024/C1, camunda-marketplace/005/C1, camunda-marketplace/188/C1

### K9: 7 workflows, 2 slot(s) open (ungated-reach, mutates), 2 source(s)

Defined by: structure=agent-loop; operations={classify-or-decide, generate-or-summarise, plan-act}; autonomy=acts; writer=outsider; shape=free-text; guards=none
Closure (all members agree): structure=agent-loop; operations={classify-or-decide, generate-or-summarise, plan-act}; autonomy=acts; writer=outsider; shape=free-text; guards=none
Sources: camunda-docs-blog 4, camunda-marketplace 3
Members: camunda-docs-blog/012/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-marketplace/006/C1, camunda-marketplace/165/C1, camunda-marketplace/255/C1

### K10: 7 workflows, 2 slot(s) open (shape, mutates), 5 source(s)

Defined by: structure=single-call; operations={classify-or-decide}; autonomy=decides; writer=outsider; ungated-reach={control-flow}; guards=none
Closure (all members agree): structure=single-call; operations={classify-or-decide}; autonomy=decides; writer=outsider; ungated-reach={control-flow}; guards=none
Sources: camunda-marketplace 2, uipath-marketplace 2, camunda-docs-blog 1, newgen 1, trisotech 1
Members: camunda-docs-blog/007/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1, newgen/037/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/007/C2

### K11: 7 workflows, 2 slot(s) open (operations, ungated-reach), 4 source(s)

Defined by: structure=agent-loop; autonomy=acts; writer=outsider; shape=free-text; mutates=internal-records; guards=none
Closure (all members agree): structure=agent-loop; autonomy=acts; writer=outsider; shape=free-text; mutates=internal-records; guards=none
Sources: camunda-docs-blog 4, uipath-marketplace 1, quantumbpm 1, camunda-marketplace 1
Members: camunda-docs-blog/019/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-marketplace/006/C1, quantumbpm/001/C1, uipath-marketplace/001/C1

### K12: 6 workflows, 2 slot(s) open (ungated-reach, guards), 2 source(s)

Defined by: structure=agent-loop; operations={classify-or-decide, generate-or-summarise, plan-act}; autonomy=acts; writer=outsider; shape=free-text; mutates=none
Closure (all members agree): structure=agent-loop; operations={classify-or-decide, generate-or-summarise, plan-act}; autonomy=acts; writer=outsider; shape=free-text; mutates=none
Sources: camunda-marketplace 4, camunda-docs-blog 2
Members: camunda-docs-blog/012/C1, camunda-docs-blog/024/C1, camunda-marketplace/005/C1, camunda-marketplace/165/C1, camunda-marketplace/188/C1, camunda-marketplace/255/C1

### K13: 5 workflows, 2 slot(s) open (ungated-reach, guards), 2 source(s)

Defined by: structure=agent-loop; operations={classify-or-decide, generate-or-summarise, plan-act}; autonomy=acts; writer=outsider; shape=free-text; mutates=internal-records
Closure (all members agree): structure=agent-loop; operations={classify-or-decide, generate-or-summarise, plan-act}; autonomy=acts; writer=outsider; shape=free-text; mutates=internal-records
Sources: camunda-docs-blog 4, camunda-marketplace 1
Members: camunda-docs-blog/021/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-marketplace/006/C1

### K14: 5 workflows, 2 slot(s) open (ungated-reach, mutates), 4 source(s)

Defined by: structure=single-call; operations={classify-or-decide}; autonomy=decides; writer=outsider; shape=closed-label; guards=none
Closure (all members agree): structure=single-call; operations={classify-or-decide}; autonomy=decides; writer=outsider; shape=closed-label; guards=none
Sources: camunda-marketplace 2, firestart 1, camunda-docs-blog 1, newgen 1
Members: camunda-docs-blog/007/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1, firestart/013/C1, newgen/037/C1

### K15: 4 workflows, 2 slot(s) open (ungated-reach, guards), 2 source(s)

Defined by: structure=single-call; operations={classify-or-decide}; autonomy=decides; writer=outsider; shape=closed-label; mutates=none
Closure (all members agree): structure=single-call; operations={classify-or-decide}; autonomy=decides; writer=outsider; shape=closed-label; mutates=none
Sources: camunda-docs-blog 2, camunda-marketplace 2
Members: camunda-docs-blog/001/C1, camunda-docs-blog/007/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1

### K16: 4 workflows, 2 slot(s) open (ungated-reach, mutates), 3 source(s)

Defined by: structure=single-call; operations={classify-or-decide}; autonomy=decides; writer=outsider; shape=structured; guards=none
Closure (all members agree): structure=single-call; operations={classify-or-decide}; autonomy=decides; writer=outsider; shape=structured; guards=none
Sources: uipath-marketplace 2, trisotech 1, camunda-marketplace 1
Members: camunda-marketplace/136/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K17: 4 workflows, 2 slot(s) open (autonomy, ungated-reach), 2 source(s)

Defined by: structure=agent-loop; operations={classify-or-decide, generate-or-summarise, plan-act}; writer=outsider; shape=free-text; mutates=none; guards=none
Closure (all members agree): structure=agent-loop; operations={classify-or-decide, generate-or-summarise, plan-act}; writer=outsider; shape=free-text; mutates=none; guards=none
Sources: camunda-docs-blog 2, camunda-marketplace 2
Members: camunda-docs-blog/012/C1, camunda-docs-blog/086/C1, camunda-marketplace/165/C1, camunda-marketplace/255/C1

### K18: 4 workflows, 2 slot(s) open (operations, guards), 3 source(s)

Defined by: structure=fixed-sequence; autonomy=decides; writer=outsider; shape=free-text; ungated-reach={control-flow, external-recipient}; mutates=none
Closure (all members agree): structure=fixed-sequence; autonomy=decides; writer=outsider; shape=free-text; ungated-reach={control-flow, external-recipient}; mutates=none
Sources: flows-for-apex 2, camunda-docs-blog 1, quantumbpm 1
Members: camunda-docs-blog/016/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1

### K19: 4 workflows, 2 slot(s) open (operations, ungated-reach), 3 source(s)

Defined by: structure=agent-loop; autonomy=acts; writer=outsider; shape=free-text; mutates=none; guards=none
Closure (all members agree): structure=agent-loop; autonomy=acts; writer=outsider; shape=free-text; mutates=none; guards=none
Sources: camunda-marketplace 2, uipath-marketplace 1, camunda-docs-blog 1
Members: camunda-docs-blog/012/C1, camunda-marketplace/165/C1, camunda-marketplace/255/C1, uipath-marketplace/002/C1

### K20: 3 workflows, 2 slot(s) open (mutates, guards), 1 source(s)

Defined by: structure=agent-loop; operations={classify-or-decide, generate-or-summarise, plan-act}; autonomy=acts; writer=outsider; shape=free-text; ungated-reach={control-flow, external-recipient, internal-human, internal-system}
Closure (all members agree): structure=agent-loop; operations={classify-or-decide, generate-or-summarise, plan-act}; autonomy=acts; writer=outsider; shape=free-text; ungated-reach={control-flow, external-recipient, internal-human, internal-system}
Sources: camunda-docs-blog 3
Members: camunda-docs-blog/013/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1

### K21: 3 workflows, 2 slot(s) open (ungated-reach, mutates), 2 source(s)

Defined by: structure=fixed-sequence; operations={classify-or-decide, extract}; autonomy=decides; writer=outsider; shape=structured; guards=none
Closure (all members agree): structure=fixed-sequence; operations={classify-or-decide, extract}; autonomy=decides; writer=outsider; shape=structured; guards=none
Sources: flowable 2, camunda-marketplace 1
Members: camunda-marketplace/067/C1, flowable/001/C1, flowable/166/C1

### K22: 3 workflows, 2 slot(s) open (operations, guards), 2 source(s)

Defined by: structure=agent-loop; autonomy=acts; writer=outsider; shape=free-text; ungated-reach={external-recipient, internal-human, internal-system}; mutates=internal-records
Closure (all members agree): structure=agent-loop; autonomy=acts; writer=outsider; shape=free-text; ungated-reach={external-recipient, internal-human, internal-system}; mutates=internal-records
Sources: camunda-docs-blog 2, camunda-marketplace 1
Members: camunda-docs-blog/021/C1, camunda-docs-blog/067/C1, camunda-marketplace/228/C1

### K23: 3 workflows, 2 slot(s) open (operations, mutates), 2 source(s)

Defined by: structure=single-call; autonomy=suggests; writer=insider; shape=structured; ungated-reach={}; guards=human-review
Closure (all members agree): structure=single-call; autonomy=suggests; writer=insider; shape=structured; ungated-reach={}; guards=human-review
Sources: firestart 2, bizagi 1
Members: bizagi/002/C1, firestart/003/C1, firestart/015/C1

### K24: 3 workflows, 2 slot(s) open (operations, mutates), 2 source(s)

Defined by: structure=agent-loop; autonomy=acts; writer=outsider; shape=free-text; ungated-reach={control-flow, external-recipient, internal-system}; guards=none
Closure (all members agree): structure=agent-loop; autonomy=acts; writer=outsider; shape=free-text; ungated-reach={control-flow, external-recipient, internal-system}; guards=none
Sources: camunda-marketplace 2, camunda-docs-blog 1
Members: camunda-docs-blog/121/C1, camunda-marketplace/006/C1, camunda-marketplace/023/C1

### K25: 13 workflows, 3 slot(s) open (operations, ungated-reach, mutates), 4 source(s)

Defined by: structure=agent-loop; autonomy=acts; writer=outsider; shape=free-text; guards=none
Closure (all members agree): structure=agent-loop; autonomy=acts; writer=outsider; shape=free-text; guards=none
Sources: camunda-docs-blog 6, camunda-marketplace 4, uipath-marketplace 2, quantumbpm 1
Members: camunda-docs-blog/012/C1, camunda-docs-blog/019/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/121/C1, camunda-marketplace/006/C1, camunda-marketplace/023/C1, camunda-marketplace/165/C1, camunda-marketplace/255/C1, quantumbpm/001/C1, uipath-marketplace/001/C1, uipath-marketplace/002/C1

### K26: 12 workflows, 3 slot(s) open (ungated-reach, mutates, guards), 2 source(s)

Defined by: structure=agent-loop; operations={classify-or-decide, generate-or-summarise, plan-act}; autonomy=acts; writer=outsider; shape=free-text
Closure (all members agree): structure=agent-loop; operations={classify-or-decide, generate-or-summarise, plan-act}; autonomy=acts; writer=outsider; shape=free-text
Sources: camunda-docs-blog 7, camunda-marketplace 5
Members: camunda-docs-blog/012/C1, camunda-docs-blog/013/C1, camunda-docs-blog/021/C1, camunda-docs-blog/024/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-marketplace/005/C1, camunda-marketplace/006/C1, camunda-marketplace/165/C1, camunda-marketplace/188/C1, camunda-marketplace/255/C1

### K27: 9 workflows, 3 slot(s) open (operations, ungated-reach, guards), 4 source(s)

Defined by: structure=agent-loop; autonomy=acts; writer=outsider; shape=free-text; mutates=internal-records
Closure (all members agree): structure=agent-loop; autonomy=acts; writer=outsider; shape=free-text; mutates=internal-records
Sources: camunda-docs-blog 5, camunda-marketplace 2, uipath-marketplace 1, quantumbpm 1
Members: camunda-docs-blog/019/C1, camunda-docs-blog/021/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-marketplace/006/C1, camunda-marketplace/228/C1, quantumbpm/001/C1, uipath-marketplace/001/C1

### K28: 8 workflows, 3 slot(s) open (autonomy, ungated-reach, mutates), 2 source(s)

Defined by: structure=agent-loop; operations={classify-or-decide, generate-or-summarise, plan-act}; writer=outsider; shape=free-text; guards=none
Closure (all members agree): structure=agent-loop; operations={classify-or-decide, generate-or-summarise, plan-act}; writer=outsider; shape=free-text; guards=none
Sources: camunda-docs-blog 5, camunda-marketplace 3
Members: camunda-docs-blog/012/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/086/C1, camunda-marketplace/006/C1, camunda-marketplace/165/C1, camunda-marketplace/255/C1

### K29: 7 workflows, 3 slot(s) open (shape, ungated-reach, guards), 4 source(s)

Defined by: structure=single-call; operations={classify-or-decide}; autonomy=decides; writer=outsider; mutates=none
Closure (all members agree): structure=single-call; operations={classify-or-decide}; autonomy=decides; writer=outsider; mutates=none
Sources: camunda-marketplace 2, camunda-docs-blog 2, uipath-marketplace 2, trisotech 1
Members: camunda-docs-blog/001/C1, camunda-docs-blog/007/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K30: 7 workflows, 3 slot(s) open (autonomy, ungated-reach, guards), 2 source(s)

Defined by: structure=agent-loop; operations={classify-or-decide, generate-or-summarise, plan-act}; writer=outsider; shape=free-text; mutates=none
Closure (all members agree): structure=agent-loop; operations={classify-or-decide, generate-or-summarise, plan-act}; writer=outsider; shape=free-text; mutates=none
Sources: camunda-marketplace 4, camunda-docs-blog 3
Members: camunda-docs-blog/012/C1, camunda-docs-blog/024/C1, camunda-docs-blog/086/C1, camunda-marketplace/005/C1, camunda-marketplace/165/C1, camunda-marketplace/188/C1, camunda-marketplace/255/C1

### K31: 7 workflows, 3 slot(s) open (operations, ungated-reach, guards), 3 source(s)

Defined by: structure=agent-loop; autonomy=acts; writer=outsider; shape=free-text; mutates=none
Closure (all members agree): structure=agent-loop; autonomy=acts; writer=outsider; shape=free-text; mutates=none
Sources: camunda-marketplace 4, camunda-docs-blog 2, uipath-marketplace 1
Members: camunda-docs-blog/012/C1, camunda-docs-blog/024/C1, camunda-marketplace/005/C1, camunda-marketplace/165/C1, camunda-marketplace/188/C1, camunda-marketplace/255/C1, uipath-marketplace/002/C1

### K32: 6 workflows, 3 slot(s) open (ungated-reach, mutates, guards), 4 source(s)

Defined by: structure=single-call; operations={classify-or-decide}; autonomy=decides; writer=outsider; shape=closed-label
Closure (all members agree): structure=single-call; operations={classify-or-decide}; autonomy=decides; writer=outsider; shape=closed-label
Sources: camunda-marketplace 2, camunda-docs-blog 2, firestart 1, newgen 1
Members: camunda-docs-blog/001/C1, camunda-docs-blog/007/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1, firestart/013/C1, newgen/037/C1

### K33: 6 workflows, 3 slot(s) open (autonomy, ungated-reach, mutates), 4 source(s)

Defined by: structure=single-call; operations={classify-or-decide}; writer=outsider; shape=structured; guards=none
Closure (all members agree): structure=single-call; operations={classify-or-decide}; writer=outsider; shape=structured; guards=none
Sources: uipath-marketplace 2, camunda-marketplace 2, trisotech 1, firestart 1
Members: camunda-marketplace/022/C1, camunda-marketplace/136/C1, firestart/011/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K34: 5 workflows, 3 slot(s) open (ungated-reach, mutates, guards), 4 source(s)

Defined by: structure=single-call; operations={classify-or-decide}; autonomy=decides; writer=outsider; shape=structured
Closure (all members agree): structure=single-call; operations={classify-or-decide}; autonomy=decides; writer=outsider; shape=structured
Sources: uipath-marketplace 2, bonitasoft 1, trisotech 1, camunda-marketplace 1
Members: bonitasoft/012/C1, camunda-marketplace/136/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K35: 5 workflows, 3 slot(s) open (operations, ungated-reach, mutates), 4 source(s)

Defined by: structure=single-call; autonomy=decides; writer=outsider; shape=structured; guards=none
Closure (all members agree): structure=single-call; autonomy=decides; writer=outsider; shape=structured; guards=none
Sources: uipath-marketplace 2, trisotech 1, camunda-marketplace 1, firestart 1
Members: camunda-marketplace/136/C1, firestart/002/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K36: 5 workflows, 3 slot(s) open (operations, autonomy, ungated-reach), 3 source(s)

Defined by: structure=agent-loop; writer=outsider; shape=free-text; mutates=none; guards=none
Closure (all members agree): structure=agent-loop; writer=outsider; shape=free-text; mutates=none; guards=none
Sources: camunda-docs-blog 2, camunda-marketplace 2, uipath-marketplace 1
Members: camunda-docs-blog/012/C1, camunda-docs-blog/086/C1, camunda-marketplace/165/C1, camunda-marketplace/255/C1, uipath-marketplace/002/C1

### K37: 4 workflows, 3 slot(s) open (ungated-reach, mutates, guards), 3 source(s)

Defined by: structure=fixed-sequence; operations={classify-or-decide, generate-or-summarise}; autonomy=decides; writer=outsider; shape=free-text
Closure (all members agree): structure=fixed-sequence; operations={classify-or-decide, generate-or-summarise}; autonomy=decides; writer=outsider; shape=free-text
Sources: flows-for-apex 2, camunda-docs-blog 1, quantumbpm 1
Members: camunda-docs-blog/008/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1

### K38: 4 workflows, 3 slot(s) open (ungated-reach, mutates, guards), 2 source(s)

Defined by: structure=fixed-sequence; operations={classify-or-decide, extract}; autonomy=decides; writer=outsider; shape=structured
Closure (all members agree): structure=fixed-sequence; operations={classify-or-decide, extract}; autonomy=decides; writer=outsider; shape=structured
Sources: flowable 2, camunda-marketplace 2
Members: camunda-marketplace/064/C2, camunda-marketplace/067/C1, flowable/001/C1, flowable/166/C1

### K39: 4 workflows, 3 slot(s) open (operations, ungated-reach, guards), 3 source(s)

Defined by: structure=single-call; autonomy=decides; writer=outsider; shape=structured; mutates=none
Closure (all members agree): structure=single-call; autonomy=decides; writer=outsider; shape=structured; mutates=none
Sources: uipath-marketplace 2, trisotech 1, firestart 1
Members: firestart/012/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K40: 4 workflows, 3 slot(s) open (operations, ungated-reach, mutates), 2 source(s)

Defined by: structure=agent-loop; autonomy=acts; writer=outsider; shape=free-text; guards=human-review
Closure (all members agree): structure=agent-loop; autonomy=acts; writer=outsider; shape=free-text; guards=human-review
Sources: camunda-marketplace 3, camunda-docs-blog 1
Members: camunda-docs-blog/024/C1, camunda-marketplace/005/C1, camunda-marketplace/188/C1, camunda-marketplace/228/C1

### K41: 4 workflows, 3 slot(s) open (operations, shape, ungated-reach), 3 source(s)

Defined by: structure=agent-loop; autonomy=acts; writer=outsider; mutates=external-systems; guards=none
Closure (all members agree): structure=agent-loop; autonomy=acts; writer=outsider; mutates=external-systems; guards=none
Sources: flows-for-apex 2, camunda-docs-blog 1, camunda-marketplace 1
Members: camunda-docs-blog/121/C1, camunda-marketplace/023/C1, flows-for-apex/002/C1, flows-for-apex/003/C1

### K42: 4 workflows, 3 slot(s) open (operations, shape, ungated-reach), 3 source(s)

Defined by: structure=fixed-sequence; autonomy=decides; writer=outsider; mutates=none; guards=none
Closure (all members agree): structure=fixed-sequence; autonomy=decides; writer=outsider; mutates=none; guards=none
Sources: flows-for-apex 2, quantumbpm 1, flowable 1
Members: flowable/001/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1

### K43: 4 workflows, 3 slot(s) open (operations, autonomy, mutates), 2 source(s)

Defined by: structure=agent-loop; writer=outsider; shape=free-text; ungated-reach={control-flow, external-recipient, internal-system}; guards=none
Closure (all members agree): structure=agent-loop; writer=outsider; shape=free-text; ungated-reach={control-flow, external-recipient, internal-system}; guards=none
Sources: camunda-docs-blog 2, camunda-marketplace 2
Members: camunda-docs-blog/086/C1, camunda-docs-blog/121/C1, camunda-marketplace/006/C1, camunda-marketplace/023/C1

### K44: 4 workflows, 3 slot(s) open (structure, operations, ungated-reach), 3 source(s)

Defined by: autonomy=decides; writer=outsider; shape=free-text; mutates=none; guards=none
Closure (all members agree): autonomy=decides; writer=outsider; shape=free-text; mutates=none; guards=none
Sources: flows-for-apex 2, camunda-docs-blog 1, quantumbpm 1
Members: camunda-docs-blog/086/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1

### K45: 4 workflows, 3 slot(s) open (structure, operations, ungated-reach), 3 source(s)

Defined by: autonomy=decides; writer=outsider; shape=structured; mutates=none; guards=none
Closure (all members agree): autonomy=decides; writer=outsider; shape=structured; mutates=none; guards=none
Sources: uipath-marketplace 2, trisotech 1, flowable 1
Members: flowable/001/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K46: 3 workflows, 3 slot(s) open (ungated-reach, mutates, guards), 3 source(s)

Defined by: structure=agent-loop; operations={generate-or-summarise, plan-act}; autonomy=acts; writer=outsider; shape=free-text
Closure (all members agree): structure=agent-loop; operations={generate-or-summarise, plan-act}; autonomy=acts; writer=outsider; shape=free-text
Sources: camunda-docs-blog 1, uipath-marketplace 1, camunda-marketplace 1
Members: camunda-docs-blog/019/C1, camunda-marketplace/228/C1, uipath-marketplace/002/C1

### K47: 3 workflows, 3 slot(s) open (ungated-reach, mutates, guards), 2 source(s)

Defined by: structure=agent-loop; operations={classify-or-decide, plan-act}; autonomy=acts; writer=outsider; shape=structured
Closure (all members agree): structure=agent-loop; operations={classify-or-decide, plan-act}; autonomy=acts; writer=outsider; shape=structured
Sources: flows-for-apex 2, camunda-docs-blog 1
Members: camunda-docs-blog/122/C1, flows-for-apex/002/C1, flows-for-apex/003/C1

### K48: 3 workflows, 3 slot(s) open (shape, ungated-reach, guards), 3 source(s)

Defined by: structure=agent-loop; operations={classify-or-decide, plan-act}; autonomy=acts; writer=outsider; mutates=internal-records
Closure (all members agree): structure=agent-loop; operations={classify-or-decide, plan-act}; autonomy=acts; writer=outsider; mutates=internal-records
Sources: camunda-docs-blog 1, quantumbpm 1, uipath-marketplace 1
Members: camunda-docs-blog/122/C1, quantumbpm/001/C1, uipath-marketplace/001/C1

### K49: 3 workflows, 3 slot(s) open (autonomy, ungated-reach, guards), 2 source(s)

Defined by: structure=single-call; operations={classify-or-decide}; writer=outsider; shape=structured; mutates=internal-records
Closure (all members agree): structure=single-call; operations={classify-or-decide}; writer=outsider; shape=structured; mutates=internal-records
Sources: firestart 2, bonitasoft 1
Members: bonitasoft/012/C1, firestart/006/C1, firestart/011/C1

### K50: 3 workflows, 3 slot(s) open (operations, ungated-reach, guards), 2 source(s)

Defined by: structure=agent-loop; autonomy=acts; writer=outsider; shape=free-text; mutates=external-systems
Closure (all members agree): structure=agent-loop; autonomy=acts; writer=outsider; shape=free-text; mutates=external-systems
Sources: camunda-docs-blog 2, camunda-marketplace 1
Members: camunda-docs-blog/013/C1, camunda-docs-blog/121/C1, camunda-marketplace/023/C1

### K51: 3 workflows, 3 slot(s) open (operations, ungated-reach, guards), 2 source(s)

Defined by: structure=agent-loop; autonomy=acts; writer=outsider; shape=structured; mutates=external-systems
Closure (all members agree): structure=agent-loop; autonomy=acts; writer=outsider; shape=structured; mutates=external-systems
Sources: flows-for-apex 2, camunda-marketplace 1
Members: camunda-marketplace/008/C1, flows-for-apex/002/C1, flows-for-apex/003/C1

### K52: 3 workflows, 3 slot(s) open (operations, ungated-reach, guards), 2 source(s)

Defined by: structure=single-call; autonomy=suggests; writer=outsider; shape=structured; mutates=internal-records
Closure (all members agree): structure=single-call; autonomy=suggests; writer=outsider; shape=structured; mutates=internal-records
Sources: firestart 2, uipath-marketplace 1
Members: firestart/006/C1, firestart/011/C1, uipath-marketplace/005/C3

### K53: 3 workflows, 3 slot(s) open (operations, ungated-reach, mutates), 2 source(s)

Defined by: structure=single-call; autonomy=suggests; writer=outsider; shape=structured; guards=none
Closure (all members agree): structure=single-call; autonomy=suggests; writer=outsider; shape=structured; guards=none
Sources: uipath-marketplace 2, firestart 1
Members: firestart/011/C1, uipath-marketplace/005/C3, uipath-marketplace/006/C4

### K54: 3 workflows, 3 slot(s) open (operations, shape, mutates), 3 source(s)

Defined by: structure=agent-loop; autonomy=acts; writer=outsider; ungated-reach={control-flow, external-recipient}; guards=none
Closure (all members agree): structure=agent-loop; autonomy=acts; writer=outsider; ungated-reach={control-flow, external-recipient}; guards=none
Sources: flows-for-apex 1, quantumbpm 1, camunda-marketplace 1
Members: camunda-marketplace/255/C1, flows-for-apex/002/C1, quantumbpm/001/C1

### K55: 3 workflows, 3 slot(s) open (operations, autonomy, ungated-reach), 2 source(s)

Defined by: structure=single-call; writer=outsider; shape=structured; mutates=external-systems; guards=none
Closure (all members agree): structure=single-call; writer=outsider; shape=structured; mutates=external-systems; guards=none
Sources: camunda-marketplace 2, firestart 1
Members: camunda-marketplace/022/C1, camunda-marketplace/136/C1, firestart/002/C1

### K56: 3 workflows, 3 slot(s) open (operations, autonomy, ungated-reach), 2 source(s)

Defined by: structure=single-call; writer=outsider; shape=structured; mutates=internal-records; guards=none
Closure (all members agree): structure=single-call; writer=outsider; shape=structured; mutates=internal-records; guards=none
Sources: firestart 2, uipath-marketplace 1
Members: firestart/008/C1, firestart/011/C1, uipath-marketplace/005/C3

### K57: 3 workflows, 3 slot(s) open (structure, mutates, guards), 2 source(s)

Defined by: operations={classify-or-decide, extract}; autonomy=decides; writer=outsider; shape=structured; ungated-reach={control-flow, internal-system}
Closure (all members agree): operations={classify-or-decide, extract}; autonomy=decides; writer=outsider; shape=structured; ungated-reach={control-flow, internal-system}
Sources: flowable 2, firestart 1
Members: firestart/012/C1, flowable/001/C1, flowable/166/C1

### K58: 3 workflows, 3 slot(s) open (structure, autonomy, ungated-reach), 3 source(s)

Defined by: operations={classify-or-decide, extract}; writer=outsider; shape=structured; mutates=internal-records; guards=none
Closure (all members agree): operations={classify-or-decide, extract}; writer=outsider; shape=structured; mutates=internal-records; guards=none
Sources: firestart 1, camunda-marketplace 1, uipath-marketplace 1
Members: camunda-marketplace/067/C1, firestart/008/C1, uipath-marketplace/005/C3

### K59: 3 workflows, 3 slot(s) open (structure, operations, ungated-reach), 2 source(s)

Defined by: autonomy=acts; writer=outsider; shape=structured; mutates=external-systems; guards=none
Closure (all members agree): autonomy=acts; writer=outsider; shape=structured; mutates=external-systems; guards=none
Sources: flows-for-apex 2, camunda-marketplace 1
Members: camunda-marketplace/022/C1, flows-for-apex/002/C1, flows-for-apex/003/C1

### K60: 19 workflows, 4 slot(s) open (operations, ungated-reach, mutates, guards), 4 source(s)

Defined by: structure=agent-loop; autonomy=acts; writer=outsider; shape=free-text
Closure (all members agree): structure=agent-loop; autonomy=acts; writer=outsider; shape=free-text
Sources: camunda-docs-blog 9, camunda-marketplace 7, uipath-marketplace 2, quantumbpm 1
Members: camunda-docs-blog/012/C1, camunda-docs-blog/013/C1, camunda-docs-blog/019/C1, camunda-docs-blog/021/C1, camunda-docs-blog/024/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/121/C1, camunda-marketplace/005/C1, camunda-marketplace/006/C1, camunda-marketplace/023/C1, camunda-marketplace/165/C1, camunda-marketplace/188/C1, camunda-marketplace/228/C1, camunda-marketplace/255/C1, quantumbpm/001/C1, uipath-marketplace/001/C1, uipath-marketplace/002/C1

### K61: 14 workflows, 4 slot(s) open (operations, autonomy, ungated-reach, mutates), 4 source(s)

Defined by: structure=agent-loop; writer=outsider; shape=free-text; guards=none
Closure (all members agree): structure=agent-loop; writer=outsider; shape=free-text; guards=none
Sources: camunda-docs-blog 7, camunda-marketplace 4, uipath-marketplace 2, quantumbpm 1
Members: camunda-docs-blog/012/C1, camunda-docs-blog/019/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/086/C1, camunda-docs-blog/121/C1, camunda-marketplace/006/C1, camunda-marketplace/023/C1, camunda-marketplace/165/C1, camunda-marketplace/255/C1, quantumbpm/001/C1, uipath-marketplace/001/C1, uipath-marketplace/002/C1

### K62: 13 workflows, 4 slot(s) open (autonomy, ungated-reach, mutates, guards), 2 source(s)

Defined by: structure=agent-loop; operations={classify-or-decide, generate-or-summarise, plan-act}; writer=outsider; shape=free-text
Closure (all members agree): structure=agent-loop; operations={classify-or-decide, generate-or-summarise, plan-act}; writer=outsider; shape=free-text
Sources: camunda-docs-blog 8, camunda-marketplace 5
Members: camunda-docs-blog/012/C1, camunda-docs-blog/013/C1, camunda-docs-blog/021/C1, camunda-docs-blog/024/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/086/C1, camunda-marketplace/005/C1, camunda-marketplace/006/C1, camunda-marketplace/165/C1, camunda-marketplace/188/C1, camunda-marketplace/255/C1

### K63: 11 workflows, 4 slot(s) open (structure, operations, shape, ungated-reach), 7 source(s)

Defined by: autonomy=decides; writer=outsider; mutates=none; guards=none
Closure (all members agree): autonomy=decides; writer=outsider; mutates=none; guards=none
Sources: camunda-marketplace 2, camunda-docs-blog 2, uipath-marketplace 2, flows-for-apex 2, quantumbpm 1, trisotech 1, flowable 1
Members: camunda-docs-blog/007/C1, camunda-docs-blog/086/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1, flowable/001/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K64: 10 workflows, 4 slot(s) open (operations, shape, ungated-reach, guards), 4 source(s)

Defined by: structure=agent-loop; autonomy=acts; writer=outsider; mutates=internal-records
Closure (all members agree): structure=agent-loop; autonomy=acts; writer=outsider; mutates=internal-records
Sources: camunda-docs-blog 6, camunda-marketplace 2, uipath-marketplace 1, quantumbpm 1
Members: camunda-docs-blog/019/C1, camunda-docs-blog/021/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/122/C1, camunda-marketplace/006/C1, camunda-marketplace/228/C1, quantumbpm/001/C1, uipath-marketplace/001/C1

### K65: 9 workflows, 4 slot(s) open (operations, autonomy, ungated-reach, mutates), 4 source(s)

Defined by: structure=single-call; writer=outsider; shape=structured; guards=none
Closure (all members agree): structure=single-call; writer=outsider; shape=structured; guards=none
Sources: uipath-marketplace 3, firestart 3, camunda-marketplace 2, trisotech 1
Members: camunda-marketplace/022/C1, camunda-marketplace/136/C1, firestart/002/C1, firestart/008/C1, firestart/011/C1, trisotech/001/C1, uipath-marketplace/005/C3, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/006/C4, uipath-marketplace/007/C2

### K66: 8 workflows, 4 slot(s) open (autonomy, ungated-reach, mutates, guards), 5 source(s)

Defined by: structure=single-call; operations={classify-or-decide}; writer=outsider; shape=structured
Closure (all members agree): structure=single-call; operations={classify-or-decide}; writer=outsider; shape=structured
Sources: uipath-marketplace 2, camunda-marketplace 2, firestart 2, bonitasoft 1, trisotech 1
Members: bonitasoft/012/C1, camunda-marketplace/022/C1, camunda-marketplace/136/C1, firestart/006/C1, firestart/011/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K67: 8 workflows, 4 slot(s) open (operations, shape, ungated-reach, guards), 5 source(s)

Defined by: structure=single-call; autonomy=decides; writer=outsider; mutates=none
Closure (all members agree): structure=single-call; autonomy=decides; writer=outsider; mutates=none
Sources: camunda-marketplace 2, camunda-docs-blog 2, uipath-marketplace 2, firestart 1, trisotech 1
Members: camunda-docs-blog/001/C1, camunda-docs-blog/007/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1, firestart/012/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K68: 8 workflows, 4 slot(s) open (operations, autonomy, ungated-reach, guards), 3 source(s)

Defined by: structure=agent-loop; writer=outsider; shape=free-text; mutates=none
Closure (all members agree): structure=agent-loop; writer=outsider; shape=free-text; mutates=none
Sources: camunda-marketplace 4, camunda-docs-blog 3, uipath-marketplace 1
Members: camunda-docs-blog/012/C1, camunda-docs-blog/024/C1, camunda-docs-blog/086/C1, camunda-marketplace/005/C1, camunda-marketplace/165/C1, camunda-marketplace/188/C1, camunda-marketplace/255/C1, uipath-marketplace/002/C1

### K69: 8 workflows, 4 slot(s) open (structure, operations, ungated-reach, mutates), 5 source(s)

Defined by: autonomy=decides; writer=outsider; shape=structured; guards=none
Closure (all members agree): autonomy=decides; writer=outsider; shape=structured; guards=none
Sources: flowable 2, uipath-marketplace 2, camunda-marketplace 2, trisotech 1, firestart 1
Members: camunda-marketplace/067/C1, camunda-marketplace/136/C1, firestart/002/C1, flowable/001/C1, flowable/166/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K70: 8 workflows, 4 slot(s) open (structure, operations, shape, ungated-reach), 5 source(s)

Defined by: autonomy=acts; writer=outsider; mutates=internal-records; guards=none
Closure (all members agree): autonomy=acts; writer=outsider; mutates=internal-records; guards=none
Sources: camunda-docs-blog 4, uipath-marketplace 1, quantumbpm 1, camunda-marketplace 1, firestart 1
Members: camunda-docs-blog/019/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-marketplace/006/C1, firestart/008/C1, quantumbpm/001/C1, uipath-marketplace/001/C1

### K71: 7 workflows, 4 slot(s) open (operations, ungated-reach, mutates, guards), 5 source(s)

Defined by: structure=single-call; autonomy=decides; writer=outsider; shape=structured
Closure (all members agree): structure=single-call; autonomy=decides; writer=outsider; shape=structured
Sources: firestart 2, uipath-marketplace 2, bonitasoft 1, trisotech 1, camunda-marketplace 1
Members: bonitasoft/012/C1, camunda-marketplace/136/C1, firestart/002/C1, firestart/012/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K72: 6 workflows, 4 slot(s) open (operations, shape, ungated-reach, guards), 3 source(s)

Defined by: structure=agent-loop; autonomy=acts; writer=outsider; mutates=external-systems
Closure (all members agree): structure=agent-loop; autonomy=acts; writer=outsider; mutates=external-systems
Sources: flows-for-apex 2, camunda-docs-blog 2, camunda-marketplace 2
Members: camunda-docs-blog/013/C1, camunda-docs-blog/121/C1, camunda-marketplace/008/C1, camunda-marketplace/023/C1, flows-for-apex/002/C1, flows-for-apex/003/C1

### K73: 5 workflows, 4 slot(s) open (autonomy, ungated-reach, mutates, guards), 3 source(s)

Defined by: structure=fixed-sequence; operations={classify-or-decide, extract}; writer=outsider; shape=structured
Closure (all members agree): structure=fixed-sequence; operations={classify-or-decide, extract}; writer=outsider; shape=structured
Sources: flowable 2, camunda-marketplace 2, firestart 1
Members: camunda-marketplace/064/C2, camunda-marketplace/067/C1, firestart/007/C1, flowable/001/C1, flowable/166/C1

### K74: 5 workflows, 4 slot(s) open (operations, ungated-reach, mutates, guards), 3 source(s)

Defined by: structure=fixed-sequence; autonomy=decides; writer=outsider; shape=free-text
Closure (all members agree): structure=fixed-sequence; autonomy=decides; writer=outsider; shape=free-text
Sources: camunda-docs-blog 2, flows-for-apex 2, quantumbpm 1
Members: camunda-docs-blog/008/C1, camunda-docs-blog/016/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1

### K75: 5 workflows, 4 slot(s) open (operations, ungated-reach, mutates, guards), 2 source(s)

Defined by: structure=single-call; autonomy=suggests; writer=outsider; shape=structured
Closure (all members agree): structure=single-call; autonomy=suggests; writer=outsider; shape=structured
Sources: firestart 3, uipath-marketplace 2
Members: firestart/001/C1, firestart/006/C1, firestart/011/C1, uipath-marketplace/005/C3, uipath-marketplace/006/C4

### K76: 5 workflows, 4 slot(s) open (operations, shape, ungated-reach, guards), 4 source(s)

Defined by: structure=fixed-sequence; autonomy=decides; writer=outsider; mutates=none
Closure (all members agree): structure=fixed-sequence; autonomy=decides; writer=outsider; mutates=none
Sources: flows-for-apex 2, camunda-docs-blog 1, quantumbpm 1, flowable 1
Members: camunda-docs-blog/016/C1, flowable/001/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1

### K77: 5 workflows, 4 slot(s) open (operations, autonomy, ungated-reach, guards), 3 source(s)

Defined by: structure=single-call; writer=outsider; shape=structured; mutates=internal-records
Closure (all members agree): structure=single-call; writer=outsider; shape=structured; mutates=internal-records
Sources: firestart 3, bonitasoft 1, uipath-marketplace 1
Members: bonitasoft/012/C1, firestart/006/C1, firestart/008/C1, firestart/011/C1, uipath-marketplace/005/C3

### K78: 5 workflows, 4 slot(s) open (operations, autonomy, ungated-reach, guards), 3 source(s)

Defined by: structure=single-call; writer=outsider; shape=structured; mutates=none
Closure (all members agree): structure=single-call; writer=outsider; shape=structured; mutates=none
Sources: firestart 2, uipath-marketplace 2, trisotech 1
Members: firestart/001/C1, firestart/012/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K79: 5 workflows, 4 slot(s) open (structure, ungated-reach, mutates, guards), 3 source(s)

Defined by: operations={classify-or-decide, extract}; autonomy=decides; writer=outsider; shape=structured
Closure (all members agree): operations={classify-or-decide, extract}; autonomy=decides; writer=outsider; shape=structured
Sources: flowable 2, camunda-marketplace 2, firestart 1
Members: camunda-marketplace/064/C2, camunda-marketplace/067/C1, firestart/012/C1, flowable/001/C1, flowable/166/C1

### K80: 5 workflows, 4 slot(s) open (structure, autonomy, ungated-reach, mutates), 4 source(s)

Defined by: operations={classify-or-decide, extract}; writer=outsider; shape=structured; guards=none
Closure (all members agree): operations={classify-or-decide, extract}; writer=outsider; shape=structured; guards=none
Sources: flowable 2, camunda-marketplace 1, uipath-marketplace 1, firestart 1
Members: camunda-marketplace/067/C1, firestart/008/C1, flowable/001/C1, flowable/166/C1, uipath-marketplace/005/C3

### K81: 5 workflows, 4 slot(s) open (structure, operations, ungated-reach, guards), 3 source(s)

Defined by: autonomy=decides; writer=outsider; shape=free-text; mutates=none
Closure (all members agree): autonomy=decides; writer=outsider; shape=free-text; mutates=none
Sources: camunda-docs-blog 2, flows-for-apex 2, quantumbpm 1
Members: camunda-docs-blog/016/C1, camunda-docs-blog/086/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1

### K82: 5 workflows, 4 slot(s) open (structure, operations, ungated-reach, guards), 4 source(s)

Defined by: autonomy=decides; writer=outsider; shape=structured; mutates=none
Closure (all members agree): autonomy=decides; writer=outsider; shape=structured; mutates=none
Sources: uipath-marketplace 2, firestart 1, trisotech 1, flowable 1
Members: firestart/012/C1, flowable/001/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K83: 5 workflows, 4 slot(s) open (structure, operations, shape, guards), 3 source(s)

Defined by: autonomy=decides; writer=outsider; ungated-reach={control-flow, external-recipient}; mutates=none
Closure (all members agree): autonomy=decides; writer=outsider; ungated-reach={control-flow, external-recipient}; mutates=none
Sources: camunda-docs-blog 2, flows-for-apex 2, quantumbpm 1
Members: camunda-docs-blog/001/C1, camunda-docs-blog/016/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1

### K84: 5 workflows, 4 slot(s) open (structure, operations, shape, ungated-reach), 3 source(s)

Defined by: autonomy=acts; writer=outsider; mutates=external-systems; guards=none
Closure (all members agree): autonomy=acts; writer=outsider; mutates=external-systems; guards=none
Sources: flows-for-apex 2, camunda-marketplace 2, camunda-docs-blog 1
Members: camunda-docs-blog/121/C1, camunda-marketplace/022/C1, camunda-marketplace/023/C1, flows-for-apex/002/C1, flows-for-apex/003/C1

### K85: 4 workflows, 4 slot(s) open (autonomy, shape, ungated-reach, guards), 2 source(s)

Defined by: structure=single-call; operations={classify-or-decide}; writer=outsider; mutates=internal-records
Closure (all members agree): structure=single-call; operations={classify-or-decide}; writer=outsider; mutates=internal-records
Sources: firestart 3, bonitasoft 1
Members: bonitasoft/012/C1, firestart/006/C1, firestart/011/C1, firestart/013/C1

### K86: 4 workflows, 4 slot(s) open (operations, ungated-reach, mutates, guards), 3 source(s)

Defined by: structure=agent-loop; autonomy=acts; writer=outsider; shape=structured
Closure (all members agree): structure=agent-loop; autonomy=acts; writer=outsider; shape=structured
Sources: flows-for-apex 2, camunda-docs-blog 1, camunda-marketplace 1
Members: camunda-docs-blog/122/C1, camunda-marketplace/008/C1, flows-for-apex/002/C1, flows-for-apex/003/C1

### K87: 4 workflows, 4 slot(s) open (operations, shape, mutates, guards), 2 source(s)

Defined by: structure=agent-loop; autonomy=acts; writer=outsider; ungated-reach={control-flow, external-recipient, internal-human, internal-system}
Closure (all members agree): structure=agent-loop; autonomy=acts; writer=outsider; ungated-reach={control-flow, external-recipient, internal-human, internal-system}
Sources: camunda-docs-blog 3, camunda-marketplace 1
Members: camunda-docs-blog/013/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-marketplace/008/C1

### K88: 4 workflows, 4 slot(s) open (operations, autonomy, ungated-reach, mutates), 2 source(s)

Defined by: structure=single-call; writer=outsider; shape=structured; guards=human-review
Closure (all members agree): structure=single-call; writer=outsider; shape=structured; guards=human-review
Sources: firestart 3, bonitasoft 1
Members: bonitasoft/012/C1, firestart/001/C1, firestart/006/C1, firestart/012/C1

### K89: 4 workflows, 4 slot(s) open (operations, autonomy, shape, ungated-reach), 2 source(s)

Defined by: structure=single-call; writer=outsider; mutates=none; guards=human-review
Closure (all members agree): structure=single-call; writer=outsider; mutates=none; guards=human-review
Sources: camunda-docs-blog 2, firestart 2
Members: camunda-docs-blog/001/C1, camunda-docs-blog/047/C1, firestart/001/C1, firestart/012/C1

### K90: 4 workflows, 4 slot(s) open (operations, autonomy, shape, ungated-reach), 3 source(s)

Defined by: structure=single-call; writer=outsider; mutates=external-systems; guards=none
Closure (all members agree): structure=single-call; writer=outsider; mutates=external-systems; guards=none
Sources: camunda-marketplace 2, uipath-marketplace 1, firestart 1
Members: camunda-marketplace/022/C1, camunda-marketplace/136/C1, firestart/002/C1, uipath-marketplace/007/C1

### K91: 4 workflows, 4 slot(s) open (operations, autonomy, shape, ungated-reach), 2 source(s)

Defined by: structure=single-call; writer=outsider; mutates=internal-records; guards=none
Closure (all members agree): structure=single-call; writer=outsider; mutates=internal-records; guards=none
Sources: firestart 3, uipath-marketplace 1
Members: firestart/008/C1, firestart/011/C1, firestart/013/C1, uipath-marketplace/005/C3

### K92: 4 workflows, 4 slot(s) open (structure, autonomy, ungated-reach, guards), 3 source(s)

Defined by: operations={classify-or-decide, extract}; writer=outsider; shape=structured; mutates=internal-records
Closure (all members agree): operations={classify-or-decide, extract}; writer=outsider; shape=structured; mutates=internal-records
Sources: firestart 2, camunda-marketplace 1, uipath-marketplace 1
Members: camunda-marketplace/067/C1, firestart/007/C1, firestart/008/C1, uipath-marketplace/005/C3

### K93: 4 workflows, 4 slot(s) open (structure, operations, mutates, guards), 3 source(s)

Defined by: autonomy=decides; writer=outsider; shape=structured; ungated-reach={control-flow, internal-system}
Closure (all members agree): autonomy=decides; writer=outsider; shape=structured; ungated-reach={control-flow, internal-system}
Sources: flowable 2, firestart 1, bonitasoft 1
Members: bonitasoft/012/C1, firestart/012/C1, flowable/001/C1, flowable/166/C1

### K94: 4 workflows, 4 slot(s) open (structure, operations, ungated-reach, guards), 2 source(s)

Defined by: autonomy=acts; writer=outsider; shape=structured; mutates=external-systems
Closure (all members agree): autonomy=acts; writer=outsider; shape=structured; mutates=external-systems
Sources: flows-for-apex 2, camunda-marketplace 2
Members: camunda-marketplace/008/C1, camunda-marketplace/022/C1, flows-for-apex/002/C1, flows-for-apex/003/C1

### K95: 4 workflows, 4 slot(s) open (structure, operations, ungated-reach, guards), 2 source(s)

Defined by: autonomy=suggests; writer=outsider; shape=structured; mutates=internal-records
Closure (all members agree): autonomy=suggests; writer=outsider; shape=structured; mutates=internal-records
Sources: firestart 3, uipath-marketplace 1
Members: firestart/006/C1, firestart/007/C1, firestart/011/C1, uipath-marketplace/005/C3

### K96: 4 workflows, 4 slot(s) open (structure, operations, ungated-reach, mutates), 3 source(s)

Defined by: autonomy=acts; writer=outsider; shape=structured; guards=none
Closure (all members agree): autonomy=acts; writer=outsider; shape=structured; guards=none
Sources: flows-for-apex 2, firestart 1, camunda-marketplace 1
Members: camunda-marketplace/022/C1, firestart/008/C1, flows-for-apex/002/C1, flows-for-apex/003/C1

### K97: 4 workflows, 4 slot(s) open (structure, operations, shape, mutates), 3 source(s)

Defined by: autonomy=decides; writer=outsider; ungated-reach={control-flow, external-recipient}; guards=none
Closure (all members agree): autonomy=decides; writer=outsider; ungated-reach={control-flow, external-recipient}; guards=none
Sources: flows-for-apex 2, firestart 1, quantumbpm 1
Members: firestart/002/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1

### K98: 3 workflows, 4 slot(s) open (autonomy, ungated-reach, mutates, guards), 2 source(s)

Defined by: structure=single-call; operations={classify-or-decide, extract}; writer=outsider; shape=structured
Closure (all members agree): structure=single-call; operations={classify-or-decide, extract}; writer=outsider; shape=structured
Sources: firestart 2, uipath-marketplace 1
Members: firestart/008/C1, firestart/012/C1, uipath-marketplace/005/C3

### K99: 3 workflows, 4 slot(s) open (operations, ungated-reach, mutates, guards), 3 source(s)

Defined by: structure=single-call; autonomy=suggests; writer=outsider; shape=free-text
Closure (all members agree): structure=single-call; autonomy=suggests; writer=outsider; shape=free-text
Sources: uipath-marketplace 1, uipath-maestro-docs 1, camunda-docs-blog 1
Members: camunda-docs-blog/047/C1, uipath-maestro-docs/192/C1, uipath-marketplace/007/C1

### K100: 3 workflows, 4 slot(s) open (operations, shape, mutates, guards), 2 source(s)

Defined by: structure=single-call; autonomy=decides; writer=outsider; ungated-reach={control-flow, internal-system}
Closure (all members agree): structure=single-call; autonomy=decides; writer=outsider; ungated-reach={control-flow, internal-system}
Sources: firestart 2, bonitasoft 1
Members: bonitasoft/012/C1, firestart/012/C1, firestart/013/C1

### K101: 3 workflows, 4 slot(s) open (structure, operations, ungated-reach, guards), 2 source(s)

Defined by: autonomy=decides; writer=outsider; shape=structured; mutates=external-systems
Closure (all members agree): autonomy=decides; writer=outsider; shape=structured; mutates=external-systems
Sources: camunda-marketplace 2, firestart 1
Members: camunda-marketplace/064/C2, camunda-marketplace/136/C1, firestart/002/C1

### K102: 3 workflows, 4 slot(s) open (structure, operations, ungated-reach, mutates), 1 source(s)

Defined by: autonomy=suggests; writer=outsider; shape=structured; guards=human-review
Closure (all members agree): autonomy=suggests; writer=outsider; shape=structured; guards=human-review
Sources: firestart 3
Members: firestart/001/C1, firestart/006/C1, firestart/007/C1

### K103: 3 workflows, 4 slot(s) open (structure, operations, shape, mutates), 3 source(s)

Defined by: autonomy=suggests; writer=outsider; ungated-reach={}; guards=human-review
Closure (all members agree): autonomy=suggests; writer=outsider; ungated-reach={}; guards=human-review
Sources: firestart 1, uipath-maestro-docs 1, camunda-docs-blog 1
Members: camunda-docs-blog/047/C1, firestart/007/C1, uipath-maestro-docs/192/C1

### K104: 3 workflows, 4 slot(s) open (structure, operations, shape, mutates), 2 source(s)

Defined by: autonomy=acts; writer=outsider; ungated-reach={external-recipient, internal-system}; guards=none
Closure (all members agree): autonomy=acts; writer=outsider; ungated-reach={external-recipient, internal-system}; guards=none
Sources: camunda-marketplace 2, firestart 1
Members: camunda-marketplace/022/C1, camunda-marketplace/165/C1, firestart/008/C1

### K105: 3 workflows, 4 slot(s) open (structure, operations, shape, mutates), 2 source(s)

Defined by: autonomy=decides; writer=outsider; ungated-reach={control-flow, internal-system}; guards=none
Closure (all members agree): autonomy=decides; writer=outsider; ungated-reach={control-flow, internal-system}; guards=none
Sources: flowable 2, firestart 1
Members: firestart/013/C1, flowable/001/C1, flowable/166/C1

### K106: 3 workflows, 4 slot(s) open (structure, operations, shape, ungated-reach), 2 source(s)

Defined by: autonomy=decides; writer=outsider; mutates=none; guards=human-review
Closure (all members agree): autonomy=decides; writer=outsider; mutates=none; guards=human-review
Sources: camunda-docs-blog 2, firestart 1
Members: camunda-docs-blog/001/C1, camunda-docs-blog/016/C1, firestart/012/C1
