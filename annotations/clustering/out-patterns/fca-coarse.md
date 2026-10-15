# Partial-profile review (coarse level, lower bound)

91 chains / 79 annotatable / 97 workflows. Slots: structure, autonomy, writer, shape, outward-ungated, mutates, human-review.
Kept slots must include writer, >= 1 of structure/operations/autonomy, >= 1 of shape/ungated-reach/mutates.

## Coverage when k slots are left open

| k open | partial profiles with >= 3 workflows | workflows covered (of 90) | of 72 |
|---|---|---|---|
| 0 | 5 | 28 (29%) | 35% |
| 1 | 41 | 53 (55%) | 67% |
| 2 | 110 | 61 (63%) | 77% |
| 3 | 107 | 64 (66%) | 81% |
| 4 | 31 | 64 (66%) | 81% |

## Nearest neighbour

Differing slots between a chain and the closest chain of another workflow (undetermined slots count as agreeing):

| differing slots | chains |
|---|---|
| 0 | 77 |
| 1 | 14 |

## Concepts (distinct member sets), by fewest open slots then size

### K1: 9 workflows, 0 slot(s) open (-), 3 source(s)

Defined by: structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes; mutates=some; human-review=no
Closure (all members agree): structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes; mutates=some; human-review=no
Sources: camunda-docs-blog 6, camunda-marketplace 2, quantumbpm 1
Members: camunda-docs-blog/013/C1, camunda-docs-blog/021/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/121/C1, camunda-marketplace/006/C1, camunda-marketplace/023/C1, quantumbpm/001/C1

### K2: 7 workflows, 0 slot(s) open (-), 5 source(s)

Defined by: structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=no; mutates=none; human-review=no
Closure (all members agree): structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=no; mutates=none; human-review=no
Sources: uipath-marketplace 2, camunda-marketplace 2, trisotech 1, camunda-docs-blog 1, flowable 1
Members: camunda-docs-blog/007/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1, flowable/001/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K3: 5 workflows, 0 slot(s) open (-), 2 source(s)

Defined by: structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=yes; mutates=some; human-review=no
Closure (all members agree): structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=yes; mutates=some; human-review=no
Sources: camunda-marketplace 3, firestart 2
Members: camunda-marketplace/022/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, firestart/002/C1, firestart/008/C1

### K4: 4 workflows, 0 slot(s) open (-), 2 source(s)

Defined by: structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes; mutates=none; human-review=no
Closure (all members agree): structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes; mutates=none; human-review=no
Sources: camunda-docs-blog 2, camunda-marketplace 2
Members: camunda-docs-blog/012/C1, camunda-docs-blog/086/C1, camunda-marketplace/165/C1, camunda-marketplace/255/C1

### K5: 3 workflows, 0 slot(s) open (-), 2 source(s)

Defined by: structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes; mutates=none; human-review=no
Closure (all members agree): structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes; mutates=none; human-review=no
Sources: flows-for-apex 2, quantumbpm 1
Members: flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1

### K6: 13 workflows, 1 slot(s) open (mutates), 3 source(s)

Defined by: structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes; human-review=no
Closure (all members agree): structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes; human-review=no
Sources: camunda-docs-blog 8, camunda-marketplace 4, quantumbpm 1
Members: camunda-docs-blog/012/C1, camunda-docs-blog/013/C1, camunda-docs-blog/021/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/086/C1, camunda-docs-blog/121/C1, camunda-marketplace/006/C1, camunda-marketplace/023/C1, camunda-marketplace/165/C1, camunda-marketplace/255/C1, quantumbpm/001/C1

### K7: 11 workflows, 1 slot(s) open (mutates), 7 source(s)

Defined by: structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=no; human-review=no
Closure (all members agree): structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=no; human-review=no
Sources: camunda-marketplace 3, uipath-marketplace 2, flowable 2, trisotech 1, newgen 1, firestart 1, camunda-docs-blog 1
Members: camunda-docs-blog/007/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1, camunda-marketplace/136/C1, firestart/013/C1, flowable/001/C1, flowable/166/C1, newgen/037/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K8: 11 workflows, 1 slot(s) open (outward-ungated), 4 source(s)

Defined by: structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; mutates=some; human-review=no
Closure (all members agree): structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; mutates=some; human-review=no
Sources: camunda-docs-blog 7, camunda-marketplace 2, quantumbpm 1, uipath-marketplace 1
Members: camunda-docs-blog/013/C1, camunda-docs-blog/019/C1, camunda-docs-blog/021/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/121/C1, camunda-marketplace/006/C1, camunda-marketplace/023/C1, quantumbpm/001/C1, uipath-marketplace/001/C1

### K9: 10 workflows, 1 slot(s) open (human-review), 3 source(s)

Defined by: structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes; mutates=some
Closure (all members agree): structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes; mutates=some
Sources: camunda-docs-blog 6, camunda-marketplace 3, quantumbpm 1
Members: camunda-docs-blog/013/C1, camunda-docs-blog/021/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/121/C1, camunda-marketplace/006/C1, camunda-marketplace/023/C1, camunda-marketplace/228/C1, quantumbpm/001/C1

### K10: 10 workflows, 1 slot(s) open (shape), 4 source(s)

Defined by: structure=agent; autonomy=decides-or-acts; writer=outsider; outward-ungated=yes; mutates=some; human-review=no
Closure (all members agree): structure=agent; autonomy=decides-or-acts; writer=outsider; outward-ungated=yes; mutates=some; human-review=no
Sources: camunda-docs-blog 6, camunda-marketplace 2, quantumbpm 1, flows-for-apex 1
Members: camunda-docs-blog/013/C1, camunda-docs-blog/021/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/121/C1, camunda-marketplace/006/C1, camunda-marketplace/023/C1, flows-for-apex/002/C1, quantumbpm/001/C1

### K11: 8 workflows, 1 slot(s) open (human-review), 6 source(s)

Defined by: structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=no; mutates=none
Closure (all members agree): structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=no; mutates=none
Sources: uipath-marketplace 2, camunda-marketplace 2, trisotech 1, firestart 1, camunda-docs-blog 1, flowable 1
Members: camunda-docs-blog/007/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1, firestart/012/C1, flowable/001/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K12: 7 workflows, 1 slot(s) open (outward-ungated), 2 source(s)

Defined by: structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; mutates=some; human-review=no
Closure (all members agree): structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; mutates=some; human-review=no
Sources: camunda-marketplace 4, firestart 3
Members: camunda-marketplace/022/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, camunda-marketplace/136/C1, firestart/002/C1, firestart/008/C1, firestart/013/C1

### K13: 7 workflows, 1 slot(s) open (structure), 4 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes; mutates=none; human-review=no
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes; mutates=none; human-review=no
Sources: camunda-docs-blog 2, camunda-marketplace 2, flows-for-apex 2, quantumbpm 1
Members: camunda-docs-blog/012/C1, camunda-docs-blog/086/C1, camunda-marketplace/165/C1, camunda-marketplace/255/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1

### K14: 6 workflows, 1 slot(s) open (structure), 3 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=yes; mutates=some; human-review=no
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=yes; mutates=some; human-review=no
Sources: camunda-marketplace 3, firestart 2, flows-for-apex 1
Members: camunda-marketplace/022/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, firestart/002/C1, firestart/008/C1, flows-for-apex/002/C1

### K15: 5 workflows, 1 slot(s) open (human-review), 2 source(s)

Defined by: structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes; mutates=none
Closure (all members agree): structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes; mutates=none
Sources: camunda-docs-blog 3, camunda-marketplace 2
Members: camunda-docs-blog/012/C1, camunda-docs-blog/024/C1, camunda-docs-blog/086/C1, camunda-marketplace/165/C1, camunda-marketplace/255/C1

### K16: 5 workflows, 1 slot(s) open (outward-ungated), 3 source(s)

Defined by: structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; mutates=none; human-review=no
Closure (all members agree): structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; mutates=none; human-review=no
Sources: camunda-docs-blog 2, camunda-marketplace 2, uipath-marketplace 1
Members: camunda-docs-blog/012/C1, camunda-docs-blog/086/C1, camunda-marketplace/165/C1, camunda-marketplace/255/C1, uipath-marketplace/002/C1

### K17: 4 workflows, 1 slot(s) open (human-review), 3 source(s)

Defined by: structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes; mutates=none
Closure (all members agree): structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes; mutates=none
Sources: flows-for-apex 2, quantumbpm 1, camunda-docs-blog 1
Members: camunda-docs-blog/016/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1

### K18: 4 workflows, 1 slot(s) open (human-review), 2 source(s)

Defined by: structure=non-agent; autonomy=suggests; writer=outsider; shape=not-free-text; outward-ungated=no; mutates=some
Closure (all members agree): structure=non-agent; autonomy=suggests; writer=outsider; shape=not-free-text; outward-ungated=no; mutates=some
Sources: firestart 3, uipath-marketplace 1
Members: firestart/006/C1, firestart/007/C1, firestart/011/C1, uipath-marketplace/005/C3

### K19: 4 workflows, 1 slot(s) open (shape), 3 source(s)

Defined by: structure=agent; autonomy=decides-or-acts; writer=outsider; outward-ungated=no; mutates=some; human-review=no
Closure (all members agree): structure=agent; autonomy=decides-or-acts; writer=outsider; outward-ungated=no; mutates=some; human-review=no
Sources: camunda-docs-blog 2, uipath-marketplace 1, flows-for-apex 1
Members: camunda-docs-blog/019/C1, camunda-docs-blog/122/C1, flows-for-apex/003/C1, uipath-marketplace/001/C1

### K20: 4 workflows, 1 slot(s) open (autonomy), 3 source(s)

Defined by: structure=non-agent; writer=outsider; shape=not-free-text; outward-ungated=no; mutates=some; human-review=no
Closure (all members agree): structure=non-agent; writer=outsider; shape=not-free-text; outward-ungated=no; mutates=some; human-review=no
Sources: firestart 2, camunda-marketplace 1, uipath-marketplace 1
Members: camunda-marketplace/136/C1, firestart/011/C1, firestart/013/C1, uipath-marketplace/005/C3

### K21: 4 workflows, 1 slot(s) open (structure), 4 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=no; mutates=some; human-review=no
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=no; mutates=some; human-review=no
Sources: camunda-docs-blog 1, firestart 1, flows-for-apex 1, camunda-marketplace 1
Members: camunda-docs-blog/122/C1, camunda-marketplace/136/C1, firestart/013/C1, flows-for-apex/003/C1

### K22: 3 workflows, 1 slot(s) open (human-review), 3 source(s)

Defined by: structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=no; mutates=some
Closure (all members agree): structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=no; mutates=some
Sources: bonitasoft 1, firestart 1, camunda-marketplace 1
Members: bonitasoft/012/C1, camunda-marketplace/136/C1, firestart/013/C1

### K23: 3 workflows, 1 slot(s) open (human-review), 2 source(s)

Defined by: structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=no; mutates=none
Closure (all members agree): structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=no; mutates=none
Sources: camunda-marketplace 2, uipath-marketplace 1
Members: camunda-marketplace/005/C1, camunda-marketplace/188/C1, uipath-marketplace/002/C1

### K24: 3 workflows, 1 slot(s) open (mutates), 2 source(s)

Defined by: structure=non-agent; autonomy=suggests; writer=not-outsider; shape=not-free-text; outward-ungated=no; human-review=yes
Closure (all members agree): structure=non-agent; autonomy=suggests; writer=not-outsider; shape=not-free-text; outward-ungated=no; human-review=yes
Sources: firestart 2, bizagi 1
Members: bizagi/002/C1, firestart/003/C1, firestart/015/C1

### K25: 3 workflows, 1 slot(s) open (mutates), 2 source(s)

Defined by: structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=no; human-review=no
Closure (all members agree): structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=no; human-review=no
Sources: uipath-marketplace 2, camunda-docs-blog 1
Members: camunda-docs-blog/019/C1, uipath-marketplace/001/C1, uipath-marketplace/002/C1

### K26: 3 workflows, 1 slot(s) open (mutates), 1 source(s)

Defined by: structure=non-agent; autonomy=suggests; writer=outsider; shape=not-free-text; outward-ungated=no; human-review=yes
Closure (all members agree): structure=non-agent; autonomy=suggests; writer=outsider; shape=not-free-text; outward-ungated=no; human-review=yes
Sources: firestart 3
Members: firestart/001/C1, firestart/006/C1, firestart/007/C1

### K27: 3 workflows, 1 slot(s) open (mutates), 2 source(s)

Defined by: structure=non-agent; autonomy=suggests; writer=outsider; shape=not-free-text; outward-ungated=no; human-review=no
Closure (all members agree): structure=non-agent; autonomy=suggests; writer=outsider; shape=not-free-text; outward-ungated=no; human-review=no
Sources: uipath-marketplace 2, firestart 1
Members: firestart/011/C1, uipath-marketplace/005/C3, uipath-marketplace/006/C4

### K28: 3 workflows, 1 slot(s) open (outward-ungated), 2 source(s)

Defined by: structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; mutates=none; human-review=yes
Closure (all members agree): structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; mutates=none; human-review=yes
Sources: camunda-marketplace 2, camunda-docs-blog 1
Members: camunda-docs-blog/024/C1, camunda-marketplace/005/C1, camunda-marketplace/188/C1

### K29: 3 workflows, 1 slot(s) open (outward-ungated), 2 source(s)

Defined by: structure=agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; mutates=some; human-review=no
Closure (all members agree): structure=agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; mutates=some; human-review=no
Sources: flows-for-apex 2, camunda-docs-blog 1
Members: camunda-docs-blog/122/C1, flows-for-apex/002/C1, flows-for-apex/003/C1

### K30: 3 workflows, 1 slot(s) open (autonomy), 2 source(s)

Defined by: structure=non-agent; writer=outsider; shape=not-free-text; outward-ungated=no; mutates=some; human-review=yes
Closure (all members agree): structure=non-agent; writer=outsider; shape=not-free-text; outward-ungated=no; mutates=some; human-review=yes
Sources: firestart 2, bonitasoft 1
Members: bonitasoft/012/C1, firestart/006/C1, firestart/007/C1

### K31: 16 workflows, 2 slot(s) open (outward-ungated, mutates), 7 source(s)

Defined by: structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; human-review=no
Closure (all members agree): structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; human-review=no
Sources: camunda-marketplace 6, firestart 3, uipath-marketplace 2, flowable 2, trisotech 1, newgen 1, camunda-docs-blog 1
Members: camunda-docs-blog/007/C1, camunda-marketplace/016/C1, camunda-marketplace/022/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, camunda-marketplace/112/C1, camunda-marketplace/136/C1, firestart/002/C1, firestart/008/C1, firestart/013/C1, flowable/001/C1, flowable/166/C1, newgen/037/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K32: 16 workflows, 2 slot(s) open (outward-ungated, mutates), 4 source(s)

Defined by: structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; human-review=no
Closure (all members agree): structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; human-review=no
Sources: camunda-docs-blog 9, camunda-marketplace 4, uipath-marketplace 2, quantumbpm 1
Members: camunda-docs-blog/012/C1, camunda-docs-blog/013/C1, camunda-docs-blog/019/C1, camunda-docs-blog/021/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/086/C1, camunda-docs-blog/121/C1, camunda-marketplace/006/C1, camunda-marketplace/023/C1, camunda-marketplace/165/C1, camunda-marketplace/255/C1, quantumbpm/001/C1, uipath-marketplace/001/C1, uipath-marketplace/002/C1

### K33: 16 workflows, 2 slot(s) open (structure, mutates), 4 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes; human-review=no
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes; human-review=no
Sources: camunda-docs-blog 8, camunda-marketplace 4, quantumbpm 2, flows-for-apex 2
Members: camunda-docs-blog/012/C1, camunda-docs-blog/013/C1, camunda-docs-blog/021/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/086/C1, camunda-docs-blog/121/C1, camunda-marketplace/006/C1, camunda-marketplace/023/C1, camunda-marketplace/165/C1, camunda-marketplace/255/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/001/C1, quantumbpm/002/C1

### K34: 15 workflows, 2 slot(s) open (mutates, human-review), 3 source(s)

Defined by: structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes
Closure (all members agree): structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes
Sources: camunda-docs-blog 9, camunda-marketplace 5, quantumbpm 1
Members: camunda-docs-blog/012/C1, camunda-docs-blog/013/C1, camunda-docs-blog/021/C1, camunda-docs-blog/024/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/086/C1, camunda-docs-blog/121/C1, camunda-marketplace/006/C1, camunda-marketplace/023/C1, camunda-marketplace/165/C1, camunda-marketplace/228/C1, camunda-marketplace/255/C1, quantumbpm/001/C1

### K35: 15 workflows, 2 slot(s) open (structure, shape), 5 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; outward-ungated=yes; mutates=some; human-review=no
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; outward-ungated=yes; mutates=some; human-review=no
Sources: camunda-docs-blog 6, camunda-marketplace 5, firestart 2, quantumbpm 1, flows-for-apex 1
Members: camunda-docs-blog/013/C1, camunda-docs-blog/021/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/121/C1, camunda-marketplace/006/C1, camunda-marketplace/022/C1, camunda-marketplace/023/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, firestart/002/C1, firestart/008/C1, flows-for-apex/002/C1, quantumbpm/001/C1

### K36: 14 workflows, 2 slot(s) open (shape, mutates), 4 source(s)

Defined by: structure=agent; autonomy=decides-or-acts; writer=outsider; outward-ungated=yes; human-review=no
Closure (all members agree): structure=agent; autonomy=decides-or-acts; writer=outsider; outward-ungated=yes; human-review=no
Sources: camunda-docs-blog 8, camunda-marketplace 4, quantumbpm 1, flows-for-apex 1
Members: camunda-docs-blog/012/C1, camunda-docs-blog/013/C1, camunda-docs-blog/021/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/086/C1, camunda-docs-blog/121/C1, camunda-marketplace/006/C1, camunda-marketplace/023/C1, camunda-marketplace/165/C1, camunda-marketplace/255/C1, flows-for-apex/002/C1, quantumbpm/001/C1

### K37: 14 workflows, 2 slot(s) open (shape, outward-ungated), 5 source(s)

Defined by: structure=agent; autonomy=decides-or-acts; writer=outsider; mutates=some; human-review=no
Closure (all members agree): structure=agent; autonomy=decides-or-acts; writer=outsider; mutates=some; human-review=no
Sources: camunda-docs-blog 8, camunda-marketplace 2, flows-for-apex 2, quantumbpm 1, uipath-marketplace 1
Members: camunda-docs-blog/013/C1, camunda-docs-blog/019/C1, camunda-docs-blog/021/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/121/C1, camunda-docs-blog/122/C1, camunda-marketplace/006/C1, camunda-marketplace/023/C1, flows-for-apex/002/C1, flows-for-apex/003/C1, quantumbpm/001/C1, uipath-marketplace/001/C1

### K38: 13 workflows, 2 slot(s) open (mutates, human-review), 8 source(s)

Defined by: structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=no
Closure (all members agree): structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=no
Sources: camunda-marketplace 3, firestart 2, uipath-marketplace 2, flowable 2, bonitasoft 1, trisotech 1, newgen 1, camunda-docs-blog 1
Members: bonitasoft/012/C1, camunda-docs-blog/007/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1, camunda-marketplace/136/C1, firestart/012/C1, firestart/013/C1, flowable/001/C1, flowable/166/C1, newgen/037/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K39: 13 workflows, 2 slot(s) open (autonomy, mutates), 7 source(s)

Defined by: structure=non-agent; writer=outsider; shape=not-free-text; outward-ungated=no; human-review=no
Closure (all members agree): structure=non-agent; writer=outsider; shape=not-free-text; outward-ungated=no; human-review=no
Sources: uipath-marketplace 3, camunda-marketplace 3, firestart 2, flowable 2, trisotech 1, newgen 1, camunda-docs-blog 1
Members: camunda-docs-blog/007/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1, camunda-marketplace/136/C1, firestart/011/C1, firestart/013/C1, flowable/001/C1, flowable/166/C1, newgen/037/C1, trisotech/001/C1, uipath-marketplace/005/C3, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/006/C4, uipath-marketplace/007/C2

### K40: 13 workflows, 2 slot(s) open (structure, mutates), 8 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=no; human-review=no
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=no; human-review=no
Sources: camunda-marketplace 3, camunda-docs-blog 2, uipath-marketplace 2, flowable 2, trisotech 1, newgen 1, firestart 1, flows-for-apex 1
Members: camunda-docs-blog/007/C1, camunda-docs-blog/122/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1, camunda-marketplace/136/C1, firestart/013/C1, flowable/001/C1, flowable/166/C1, flows-for-apex/003/C1, newgen/037/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K41: 12 workflows, 2 slot(s) open (outward-ungated, human-review), 4 source(s)

Defined by: structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; mutates=some
Closure (all members agree): structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; mutates=some
Sources: camunda-docs-blog 7, camunda-marketplace 3, quantumbpm 1, uipath-marketplace 1
Members: camunda-docs-blog/013/C1, camunda-docs-blog/019/C1, camunda-docs-blog/021/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/121/C1, camunda-marketplace/006/C1, camunda-marketplace/023/C1, camunda-marketplace/228/C1, quantumbpm/001/C1, uipath-marketplace/001/C1

### K42: 12 workflows, 2 slot(s) open (shape, human-review), 4 source(s)

Defined by: structure=agent; autonomy=decides-or-acts; writer=outsider; outward-ungated=yes; mutates=some
Closure (all members agree): structure=agent; autonomy=decides-or-acts; writer=outsider; outward-ungated=yes; mutates=some
Sources: camunda-docs-blog 6, camunda-marketplace 4, quantumbpm 1, flows-for-apex 1
Members: camunda-docs-blog/013/C1, camunda-docs-blog/021/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/121/C1, camunda-marketplace/006/C1, camunda-marketplace/008/C1, camunda-marketplace/023/C1, camunda-marketplace/228/C1, flows-for-apex/002/C1, quantumbpm/001/C1

### K43: 11 workflows, 2 slot(s) open (structure, human-review), 3 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes; mutates=some
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes; mutates=some
Sources: camunda-docs-blog 7, camunda-marketplace 3, quantumbpm 1
Members: camunda-docs-blog/008/C1, camunda-docs-blog/013/C1, camunda-docs-blog/021/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/121/C1, camunda-marketplace/006/C1, camunda-marketplace/023/C1, camunda-marketplace/228/C1, quantumbpm/001/C1

### K44: 10 workflows, 2 slot(s) open (shape, outward-ungated), 7 source(s)

Defined by: structure=non-agent; autonomy=decides-or-acts; writer=outsider; mutates=none; human-review=no
Closure (all members agree): structure=non-agent; autonomy=decides-or-acts; writer=outsider; mutates=none; human-review=no
Sources: uipath-marketplace 2, camunda-marketplace 2, flows-for-apex 2, trisotech 1, quantumbpm 1, camunda-docs-blog 1, flowable 1
Members: camunda-docs-blog/007/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1, flowable/001/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K45: 10 workflows, 2 slot(s) open (structure, outward-ungated), 4 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; shape=not-free-text; mutates=some; human-review=no
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; shape=not-free-text; mutates=some; human-review=no
Sources: camunda-marketplace 4, firestart 3, flows-for-apex 2, camunda-docs-blog 1
Members: camunda-docs-blog/122/C1, camunda-marketplace/022/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, camunda-marketplace/136/C1, firestart/002/C1, firestart/008/C1, firestart/013/C1, flows-for-apex/002/C1, flows-for-apex/003/C1

### K46: 9 workflows, 2 slot(s) open (outward-ungated, human-review), 6 source(s)

Defined by: structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; mutates=none
Closure (all members agree): structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; mutates=none
Sources: uipath-marketplace 2, camunda-docs-blog 2, camunda-marketplace 2, trisotech 1, firestart 1, flowable 1
Members: camunda-docs-blog/001/C1, camunda-docs-blog/007/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1, firestart/012/C1, flowable/001/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K47: 9 workflows, 2 slot(s) open (autonomy, human-review), 6 source(s)

Defined by: structure=non-agent; writer=outsider; shape=not-free-text; outward-ungated=no; mutates=none
Closure (all members agree): structure=non-agent; writer=outsider; shape=not-free-text; outward-ungated=no; mutates=none
Sources: firestart 2, uipath-marketplace 2, camunda-marketplace 2, trisotech 1, camunda-docs-blog 1, flowable 1
Members: camunda-docs-blog/007/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1, firestart/001/C1, firestart/012/C1, flowable/001/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K48: 9 workflows, 2 slot(s) open (autonomy, outward-ungated), 3 source(s)

Defined by: structure=non-agent; writer=outsider; shape=not-free-text; mutates=some; human-review=no
Closure (all members agree): structure=non-agent; writer=outsider; shape=not-free-text; mutates=some; human-review=no
Sources: firestart 4, camunda-marketplace 4, uipath-marketplace 1
Members: camunda-marketplace/022/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, camunda-marketplace/136/C1, firestart/002/C1, firestart/008/C1, firestart/011/C1, firestart/013/C1, uipath-marketplace/005/C3

### K49: 9 workflows, 2 slot(s) open (structure, human-review), 4 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes; mutates=none
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes; mutates=none
Sources: camunda-docs-blog 4, camunda-marketplace 2, flows-for-apex 2, quantumbpm 1
Members: camunda-docs-blog/012/C1, camunda-docs-blog/016/C1, camunda-docs-blog/024/C1, camunda-docs-blog/086/C1, camunda-marketplace/165/C1, camunda-marketplace/255/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1

### K50: 8 workflows, 2 slot(s) open (outward-ungated, human-review), 3 source(s)

Defined by: structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; mutates=some
Closure (all members agree): structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; mutates=some
Sources: camunda-marketplace 4, firestart 3, bonitasoft 1
Members: bonitasoft/012/C1, camunda-marketplace/022/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, camunda-marketplace/136/C1, firestart/002/C1, firestart/008/C1, firestart/013/C1

### K51: 8 workflows, 2 slot(s) open (outward-ungated, human-review), 3 source(s)

Defined by: structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; mutates=none
Closure (all members agree): structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; mutates=none
Sources: camunda-marketplace 4, camunda-docs-blog 3, uipath-marketplace 1
Members: camunda-docs-blog/012/C1, camunda-docs-blog/024/C1, camunda-docs-blog/086/C1, camunda-marketplace/005/C1, camunda-marketplace/165/C1, camunda-marketplace/188/C1, camunda-marketplace/255/C1, uipath-marketplace/002/C1

### K52: 8 workflows, 2 slot(s) open (shape, mutates), 4 source(s)

Defined by: structure=non-agent; autonomy=decides-or-acts; writer=outsider; outward-ungated=yes; human-review=no
Closure (all members agree): structure=non-agent; autonomy=decides-or-acts; writer=outsider; outward-ungated=yes; human-review=no
Sources: camunda-marketplace 3, firestart 2, flows-for-apex 2, quantumbpm 1
Members: camunda-marketplace/022/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, firestart/002/C1, firestart/008/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1

### K53: 8 workflows, 2 slot(s) open (structure, outward-ungated), 5 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; shape=free-text; mutates=none; human-review=no
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; shape=free-text; mutates=none; human-review=no
Sources: camunda-docs-blog 2, camunda-marketplace 2, flows-for-apex 2, quantumbpm 1, uipath-marketplace 1
Members: camunda-docs-blog/012/C1, camunda-docs-blog/086/C1, camunda-marketplace/165/C1, camunda-marketplace/255/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1, uipath-marketplace/002/C1

### K54: 8 workflows, 2 slot(s) open (structure, shape), 5 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; outward-ungated=no; mutates=none; human-review=no
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; outward-ungated=no; mutates=none; human-review=no
Sources: uipath-marketplace 3, camunda-marketplace 2, trisotech 1, camunda-docs-blog 1, flowable 1
Members: camunda-docs-blog/007/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1, flowable/001/C1, trisotech/001/C1, uipath-marketplace/002/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K55: 7 workflows, 2 slot(s) open (autonomy, human-review), 4 source(s)

Defined by: structure=non-agent; writer=outsider; shape=not-free-text; outward-ungated=no; mutates=some
Closure (all members agree): structure=non-agent; writer=outsider; shape=not-free-text; outward-ungated=no; mutates=some
Sources: firestart 4, bonitasoft 1, uipath-marketplace 1, camunda-marketplace 1
Members: bonitasoft/012/C1, camunda-marketplace/136/C1, firestart/006/C1, firestart/007/C1, firestart/011/C1, firestart/013/C1, uipath-marketplace/005/C3

### K56: 7 workflows, 2 slot(s) open (structure, human-review), 3 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=yes; mutates=some
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=yes; mutates=some
Sources: camunda-marketplace 4, firestart 2, flows-for-apex 1
Members: camunda-marketplace/008/C1, camunda-marketplace/022/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, firestart/002/C1, firestart/008/C1, flows-for-apex/002/C1

### K57: 6 workflows, 2 slot(s) open (mutates, human-review), 3 source(s)

Defined by: structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=yes
Closure (all members agree): structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=yes
Sources: camunda-marketplace 3, firestart 2, camunda-docs-blog 1
Members: camunda-docs-blog/001/C1, camunda-marketplace/022/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, firestart/002/C1, firestart/008/C1

### K58: 6 workflows, 2 slot(s) open (mutates, human-review), 2 source(s)

Defined by: structure=non-agent; autonomy=suggests; writer=outsider; shape=not-free-text; outward-ungated=no
Closure (all members agree): structure=non-agent; autonomy=suggests; writer=outsider; shape=not-free-text; outward-ungated=no
Sources: firestart 4, uipath-marketplace 2
Members: firestart/001/C1, firestart/006/C1, firestart/007/C1, firestart/011/C1, uipath-marketplace/005/C3, uipath-marketplace/006/C4

### K59: 6 workflows, 2 slot(s) open (shape, human-review), 3 source(s)

Defined by: structure=non-agent; autonomy=decides-or-acts; writer=outsider; outward-ungated=yes; mutates=some
Closure (all members agree): structure=non-agent; autonomy=decides-or-acts; writer=outsider; outward-ungated=yes; mutates=some
Sources: camunda-marketplace 3, firestart 2, camunda-docs-blog 1
Members: camunda-docs-blog/008/C1, camunda-marketplace/022/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, firestart/002/C1, firestart/008/C1

### K60: 6 workflows, 2 slot(s) open (autonomy, shape), 3 source(s)

Defined by: structure=non-agent; writer=outsider; outward-ungated=yes; mutates=some; human-review=no
Closure (all members agree): structure=non-agent; writer=outsider; outward-ungated=yes; mutates=some; human-review=no
Sources: camunda-marketplace 3, firestart 2, uipath-marketplace 1
Members: camunda-marketplace/022/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, firestart/002/C1, firestart/008/C1, uipath-marketplace/007/C1

### K61: 6 workflows, 2 slot(s) open (structure, shape), 5 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; outward-ungated=no; mutates=some; human-review=no
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; outward-ungated=no; mutates=some; human-review=no
Sources: camunda-docs-blog 2, uipath-marketplace 1, firestart 1, camunda-marketplace 1, flows-for-apex 1
Members: camunda-docs-blog/019/C1, camunda-docs-blog/122/C1, camunda-marketplace/136/C1, firestart/013/C1, flows-for-apex/003/C1, uipath-marketplace/001/C1

### K62: 5 workflows, 2 slot(s) open (mutates, human-review), 3 source(s)

Defined by: structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes
Closure (all members agree): structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes
Sources: camunda-docs-blog 2, flows-for-apex 2, quantumbpm 1
Members: camunda-docs-blog/008/C1, camunda-docs-blog/016/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1

### K63: 5 workflows, 2 slot(s) open (mutates, human-review), 3 source(s)

Defined by: structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=no
Closure (all members agree): structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=no
Sources: uipath-marketplace 2, camunda-marketplace 2, camunda-docs-blog 1
Members: camunda-docs-blog/019/C1, camunda-marketplace/005/C1, camunda-marketplace/188/C1, uipath-marketplace/001/C1, uipath-marketplace/002/C1

### K64: 5 workflows, 2 slot(s) open (shape, human-review), 3 source(s)

Defined by: structure=non-agent; autonomy=decides-or-acts; writer=outsider; outward-ungated=yes; mutates=none
Closure (all members agree): structure=non-agent; autonomy=decides-or-acts; writer=outsider; outward-ungated=yes; mutates=none
Sources: camunda-docs-blog 2, flows-for-apex 2, quantumbpm 1
Members: camunda-docs-blog/001/C1, camunda-docs-blog/016/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1

### K65: 5 workflows, 2 slot(s) open (shape, mutates), 3 source(s)

Defined by: structure=agent; autonomy=decides-or-acts; writer=outsider; outward-ungated=no; human-review=no
Closure (all members agree): structure=agent; autonomy=decides-or-acts; writer=outsider; outward-ungated=no; human-review=no
Sources: camunda-docs-blog 2, uipath-marketplace 2, flows-for-apex 1
Members: camunda-docs-blog/019/C1, camunda-docs-blog/122/C1, flows-for-apex/003/C1, uipath-marketplace/001/C1, uipath-marketplace/002/C1

### K66: 5 workflows, 2 slot(s) open (shape, mutates), 3 source(s)

Defined by: structure=non-agent; autonomy=suggests; writer=outsider; outward-ungated=no; human-review=yes
Closure (all members agree): structure=non-agent; autonomy=suggests; writer=outsider; outward-ungated=no; human-review=yes
Sources: firestart 3, uipath-maestro-docs 1, camunda-docs-blog 1
Members: camunda-docs-blog/047/C1, firestart/001/C1, firestart/006/C1, firestart/007/C1, uipath-maestro-docs/192/C1

### K67: 5 workflows, 2 slot(s) open (autonomy, mutates), 2 source(s)

Defined by: structure=non-agent; writer=outsider; shape=not-free-text; outward-ungated=no; human-review=yes
Closure (all members agree): structure=non-agent; writer=outsider; shape=not-free-text; outward-ungated=no; human-review=yes
Sources: firestart 4, bonitasoft 1
Members: bonitasoft/012/C1, firestart/001/C1, firestart/006/C1, firestart/007/C1, firestart/012/C1

### K68: 5 workflows, 2 slot(s) open (structure, human-review), 5 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=no; mutates=some
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=no; mutates=some
Sources: bonitasoft 1, camunda-docs-blog 1, firestart 1, camunda-marketplace 1, flows-for-apex 1
Members: bonitasoft/012/C1, camunda-docs-blog/122/C1, camunda-marketplace/136/C1, firestart/013/C1, flows-for-apex/003/C1

### K69: 4 workflows, 2 slot(s) open (mutates, human-review), 3 source(s)

Defined by: structure=non-agent; autonomy=suggests; writer=not-outsider; shape=not-free-text; outward-ungated=no
Closure (all members agree): structure=non-agent; autonomy=suggests; writer=not-outsider; shape=not-free-text; outward-ungated=no
Sources: firestart 2, bizagi 1, camunda-marketplace 1
Members: bizagi/002/C1, camunda-marketplace/064/C1, firestart/003/C1, firestart/015/C1

### K70: 4 workflows, 2 slot(s) open (outward-ungated, human-review), 3 source(s)

Defined by: structure=agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; mutates=some
Closure (all members agree): structure=agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; mutates=some
Sources: flows-for-apex 2, camunda-docs-blog 1, camunda-marketplace 1
Members: camunda-docs-blog/122/C1, camunda-marketplace/008/C1, flows-for-apex/002/C1, flows-for-apex/003/C1

### K71: 4 workflows, 2 slot(s) open (outward-ungated, mutates), 2 source(s)

Defined by: structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; human-review=yes
Closure (all members agree): structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text; human-review=yes
Sources: camunda-marketplace 3, camunda-docs-blog 1
Members: camunda-docs-blog/024/C1, camunda-marketplace/005/C1, camunda-marketplace/188/C1, camunda-marketplace/228/C1

### K72: 4 workflows, 2 slot(s) open (shape, mutates), 3 source(s)

Defined by: structure=non-agent; autonomy=suggests; writer=not-outsider; outward-ungated=no; human-review=yes
Closure (all members agree): structure=non-agent; autonomy=suggests; writer=not-outsider; outward-ungated=no; human-review=yes
Sources: firestart 2, bizagi 1, atamya 1
Members: atamya/010/C1, bizagi/002/C1, firestart/003/C1, firestart/015/C1

### K73: 4 workflows, 2 slot(s) open (autonomy, mutates), 3 source(s)

Defined by: structure=non-agent; writer=outsider; shape=free-text; outward-ungated=yes; human-review=no
Closure (all members agree): structure=non-agent; writer=outsider; shape=free-text; outward-ungated=yes; human-review=no
Sources: flows-for-apex 2, uipath-marketplace 1, quantumbpm 1
Members: flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1, uipath-marketplace/007/C1

### K74: 4 workflows, 2 slot(s) open (structure, mutates), 2 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes; human-review=yes
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes; human-review=yes
Sources: camunda-docs-blog 3, camunda-marketplace 1
Members: camunda-docs-blog/008/C1, camunda-docs-blog/016/C1, camunda-docs-blog/024/C1, camunda-marketplace/228/C1

### K75: 4 workflows, 2 slot(s) open (structure, outward-ungated), 2 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; shape=free-text; mutates=none; human-review=yes
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; shape=free-text; mutates=none; human-review=yes
Sources: camunda-docs-blog 2, camunda-marketplace 2
Members: camunda-docs-blog/016/C1, camunda-docs-blog/024/C1, camunda-marketplace/005/C1, camunda-marketplace/188/C1

### K76: 3 workflows, 2 slot(s) open (outward-ungated, mutates), 3 source(s)

Defined by: structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; human-review=yes
Closure (all members agree): structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text; human-review=yes
Sources: bonitasoft 1, camunda-docs-blog 1, firestart 1
Members: bonitasoft/012/C1, camunda-docs-blog/001/C1, firestart/012/C1

### K77: 3 workflows, 2 slot(s) open (shape, human-review), 3 source(s)

Defined by: structure=non-agent; autonomy=suggests; writer=not-outsider; outward-ungated=no; mutates=some
Closure (all members agree): structure=non-agent; autonomy=suggests; writer=not-outsider; outward-ungated=no; mutates=some
Sources: uipath-marketplace 1, bizagi 1, atamya 1
Members: atamya/010/C1, bizagi/002/C1, uipath-marketplace/003/C1

### K78: 3 workflows, 2 slot(s) open (shape, mutates), 1 source(s)

Defined by: structure=non-agent; autonomy=decides-or-acts; writer=outsider; outward-ungated=yes; human-review=yes
Closure (all members agree): structure=non-agent; autonomy=decides-or-acts; writer=outsider; outward-ungated=yes; human-review=yes
Sources: camunda-docs-blog 3
Members: camunda-docs-blog/001/C1, camunda-docs-blog/008/C1, camunda-docs-blog/016/C1

### K79: 3 workflows, 2 slot(s) open (shape, mutates), 2 source(s)

Defined by: structure=agent; autonomy=decides-or-acts; writer=outsider; outward-ungated=yes; human-review=yes
Closure (all members agree): structure=agent; autonomy=decides-or-acts; writer=outsider; outward-ungated=yes; human-review=yes
Sources: camunda-marketplace 2, camunda-docs-blog 1
Members: camunda-docs-blog/024/C1, camunda-marketplace/008/C1, camunda-marketplace/228/C1

### K80: 3 workflows, 2 slot(s) open (shape, outward-ungated), 2 source(s)

Defined by: structure=non-agent; autonomy=decides-or-acts; writer=outsider; mutates=none; human-review=yes
Closure (all members agree): structure=non-agent; autonomy=decides-or-acts; writer=outsider; mutates=none; human-review=yes
Sources: camunda-docs-blog 2, firestart 1
Members: camunda-docs-blog/001/C1, camunda-docs-blog/016/C1, firestart/012/C1

### K81: 3 workflows, 2 slot(s) open (shape, outward-ungated), 2 source(s)

Defined by: structure=non-agent; autonomy=suggests; writer=outsider; mutates=some; human-review=no
Closure (all members agree): structure=non-agent; autonomy=suggests; writer=outsider; mutates=some; human-review=no
Sources: uipath-marketplace 2, firestart 1
Members: firestart/011/C1, uipath-marketplace/005/C3, uipath-marketplace/007/C1

### K82: 3 workflows, 2 slot(s) open (autonomy, human-review), 3 source(s)

Defined by: structure=non-agent; writer=not-outsider; shape=free-text; outward-ungated=no; mutates=some
Closure (all members agree): structure=non-agent; writer=not-outsider; shape=free-text; outward-ungated=no; mutates=some
Sources: uipath-marketplace 1, atamya 1, bizagi 1
Members: atamya/010/C1, bizagi/001/C1, uipath-marketplace/003/C1

### K83: 3 workflows, 2 slot(s) open (autonomy, outward-ungated), 2 source(s)

Defined by: structure=non-agent; writer=outsider; shape=not-free-text; mutates=none; human-review=yes
Closure (all members agree): structure=non-agent; writer=outsider; shape=not-free-text; mutates=none; human-review=yes
Sources: firestart 2, camunda-docs-blog 1
Members: camunda-docs-blog/001/C1, firestart/001/C1, firestart/012/C1

### K84: 3 workflows, 2 slot(s) open (autonomy, shape), 2 source(s)

Defined by: structure=non-agent; writer=not-outsider; outward-ungated=no; mutates=some; human-review=yes
Closure (all members agree): structure=non-agent; writer=not-outsider; outward-ungated=no; mutates=some; human-review=yes
Sources: bizagi 2, atamya 1
Members: atamya/010/C1, bizagi/001/C1, bizagi/002/C1

### K85: 3 workflows, 2 slot(s) open (autonomy, shape), 2 source(s)

Defined by: structure=non-agent; writer=outsider; outward-ungated=no; mutates=none; human-review=yes
Closure (all members agree): structure=non-agent; writer=outsider; outward-ungated=no; mutates=none; human-review=yes
Sources: firestart 2, camunda-docs-blog 1
Members: camunda-docs-blog/047/C1, firestart/001/C1, firestart/012/C1

### K86: 3 workflows, 2 slot(s) open (structure, shape), 1 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; outward-ungated=yes; mutates=none; human-review=yes
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; outward-ungated=yes; mutates=none; human-review=yes
Sources: camunda-docs-blog 3
Members: camunda-docs-blog/001/C1, camunda-docs-blog/016/C1, camunda-docs-blog/024/C1

### K87: 3 workflows, 2 slot(s) open (structure, shape), 2 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; outward-ungated=yes; mutates=some; human-review=yes
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; outward-ungated=yes; mutates=some; human-review=yes
Sources: camunda-marketplace 2, camunda-docs-blog 1
Members: camunda-docs-blog/008/C1, camunda-marketplace/008/C1, camunda-marketplace/228/C1

### K88: 3 workflows, 2 slot(s) open (structure, shape), 2 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; outward-ungated=no; mutates=none; human-review=yes
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; outward-ungated=no; mutates=none; human-review=yes
Sources: camunda-marketplace 2, firestart 1
Members: camunda-marketplace/005/C1, camunda-marketplace/188/C1, firestart/012/C1

### K89: 22 workflows, 3 slot(s) open (structure, shape, mutates), 5 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; outward-ungated=yes; human-review=no
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; outward-ungated=yes; human-review=no
Sources: camunda-docs-blog 8, camunda-marketplace 7, flows-for-apex 3, firestart 2, quantumbpm 2
Members: camunda-docs-blog/012/C1, camunda-docs-blog/013/C1, camunda-docs-blog/021/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/086/C1, camunda-docs-blog/121/C1, camunda-marketplace/006/C1, camunda-marketplace/022/C1, camunda-marketplace/023/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, camunda-marketplace/165/C1, camunda-marketplace/255/C1, firestart/002/C1, firestart/008/C1, flows-for-apex/001/C1, flows-for-apex/002/C1, flows-for-apex/004/C1, quantumbpm/001/C1, quantumbpm/002/C1

### K90: 21 workflows, 3 slot(s) open (structure, shape, outward-ungated), 6 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; mutates=some; human-review=no
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; mutates=some; human-review=no
Sources: camunda-docs-blog 8, camunda-marketplace 6, firestart 3, flows-for-apex 2, quantumbpm 1, uipath-marketplace 1
Members: camunda-docs-blog/013/C1, camunda-docs-blog/019/C1, camunda-docs-blog/021/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/121/C1, camunda-docs-blog/122/C1, camunda-marketplace/006/C1, camunda-marketplace/022/C1, camunda-marketplace/023/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, camunda-marketplace/136/C1, firestart/002/C1, firestart/008/C1, firestart/013/C1, flows-for-apex/002/C1, flows-for-apex/003/C1, quantumbpm/001/C1, uipath-marketplace/001/C1

### K91: 20 workflows, 3 slot(s) open (outward-ungated, mutates, human-review), 4 source(s)

Defined by: structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text
Closure (all members agree): structure=agent; autonomy=decides-or-acts; writer=outsider; shape=free-text
Sources: camunda-docs-blog 10, camunda-marketplace 7, uipath-marketplace 2, quantumbpm 1
Members: camunda-docs-blog/012/C1, camunda-docs-blog/013/C1, camunda-docs-blog/019/C1, camunda-docs-blog/021/C1, camunda-docs-blog/024/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/086/C1, camunda-docs-blog/121/C1, camunda-marketplace/005/C1, camunda-marketplace/006/C1, camunda-marketplace/023/C1, camunda-marketplace/165/C1, camunda-marketplace/188/C1, camunda-marketplace/228/C1, camunda-marketplace/255/C1, quantumbpm/001/C1, uipath-marketplace/001/C1, uipath-marketplace/002/C1

### K92: 20 workflows, 3 slot(s) open (structure, mutates, human-review), 4 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; shape=free-text; outward-ungated=yes
Sources: camunda-docs-blog 11, camunda-marketplace 5, quantumbpm 2, flows-for-apex 2
Members: camunda-docs-blog/008/C1, camunda-docs-blog/012/C1, camunda-docs-blog/013/C1, camunda-docs-blog/016/C1, camunda-docs-blog/021/C1, camunda-docs-blog/024/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/086/C1, camunda-docs-blog/121/C1, camunda-marketplace/006/C1, camunda-marketplace/023/C1, camunda-marketplace/165/C1, camunda-marketplace/228/C1, camunda-marketplace/255/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/001/C1, quantumbpm/002/C1

### K93: 19 workflows, 3 slot(s) open (outward-ungated, mutates, human-review), 8 source(s)

Defined by: structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text
Closure (all members agree): structure=non-agent; autonomy=decides-or-acts; writer=outsider; shape=not-free-text
Sources: camunda-marketplace 6, firestart 4, camunda-docs-blog 2, flowable 2, uipath-marketplace 2, trisotech 1, bonitasoft 1, newgen 1
Members: bonitasoft/012/C1, camunda-docs-blog/001/C1, camunda-docs-blog/007/C1, camunda-marketplace/016/C1, camunda-marketplace/022/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, camunda-marketplace/112/C1, camunda-marketplace/136/C1, firestart/002/C1, firestart/008/C1, firestart/012/C1, firestart/013/C1, flowable/001/C1, flowable/166/C1, newgen/037/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K94: 19 workflows, 3 slot(s) open (structure, outward-ungated, mutates), 8 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; shape=not-free-text; human-review=no
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; shape=not-free-text; human-review=no
Sources: camunda-marketplace 6, firestart 3, camunda-docs-blog 2, flows-for-apex 2, flowable 2, uipath-marketplace 2, trisotech 1, newgen 1
Members: camunda-docs-blog/007/C1, camunda-docs-blog/122/C1, camunda-marketplace/016/C1, camunda-marketplace/022/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, camunda-marketplace/112/C1, camunda-marketplace/136/C1, firestart/002/C1, firestart/008/C1, firestart/013/C1, flowable/001/C1, flowable/166/C1, flows-for-apex/002/C1, flows-for-apex/003/C1, newgen/037/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K95: 19 workflows, 3 slot(s) open (structure, outward-ungated, mutates), 5 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; shape=free-text; human-review=no
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; shape=free-text; human-review=no
Sources: camunda-docs-blog 9, camunda-marketplace 4, quantumbpm 2, flows-for-apex 2, uipath-marketplace 2
Members: camunda-docs-blog/012/C1, camunda-docs-blog/013/C1, camunda-docs-blog/019/C1, camunda-docs-blog/021/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/086/C1, camunda-docs-blog/121/C1, camunda-marketplace/006/C1, camunda-marketplace/023/C1, camunda-marketplace/165/C1, camunda-marketplace/255/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/001/C1, quantumbpm/002/C1, uipath-marketplace/001/C1, uipath-marketplace/002/C1

### K96: 18 workflows, 3 slot(s) open (autonomy, mutates, human-review), 8 source(s)

Defined by: structure=non-agent; writer=outsider; shape=not-free-text; outward-ungated=no
Closure (all members agree): structure=non-agent; writer=outsider; shape=not-free-text; outward-ungated=no
Sources: firestart 6, uipath-marketplace 3, camunda-marketplace 3, flowable 2, bonitasoft 1, trisotech 1, newgen 1, camunda-docs-blog 1
Members: bonitasoft/012/C1, camunda-docs-blog/007/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1, camunda-marketplace/136/C1, firestart/001/C1, firestart/006/C1, firestart/007/C1, firestart/011/C1, firestart/012/C1, firestart/013/C1, flowable/001/C1, flowable/166/C1, newgen/037/C1, trisotech/001/C1, uipath-marketplace/005/C3, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/006/C4, uipath-marketplace/007/C2

### K97: 18 workflows, 3 slot(s) open (autonomy, outward-ungated, mutates), 7 source(s)

Defined by: structure=non-agent; writer=outsider; shape=not-free-text; human-review=no
Closure (all members agree): structure=non-agent; writer=outsider; shape=not-free-text; human-review=no
Sources: camunda-marketplace 6, firestart 4, uipath-marketplace 3, flowable 2, trisotech 1, newgen 1, camunda-docs-blog 1
Members: camunda-docs-blog/007/C1, camunda-marketplace/016/C1, camunda-marketplace/022/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, camunda-marketplace/112/C1, camunda-marketplace/136/C1, firestart/002/C1, firestart/008/C1, firestart/011/C1, firestart/013/C1, flowable/001/C1, flowable/166/C1, newgen/037/C1, trisotech/001/C1, uipath-marketplace/005/C3, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/006/C4, uipath-marketplace/007/C2

### K98: 18 workflows, 3 slot(s) open (structure, shape, human-review), 5 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; outward-ungated=yes; mutates=some
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; outward-ungated=yes; mutates=some
Sources: camunda-docs-blog 7, camunda-marketplace 7, firestart 2, quantumbpm 1, flows-for-apex 1
Members: camunda-docs-blog/008/C1, camunda-docs-blog/013/C1, camunda-docs-blog/021/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/121/C1, camunda-marketplace/006/C1, camunda-marketplace/008/C1, camunda-marketplace/022/C1, camunda-marketplace/023/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, camunda-marketplace/228/C1, firestart/002/C1, firestart/008/C1, flows-for-apex/002/C1, quantumbpm/001/C1

### K99: 17 workflows, 3 slot(s) open (shape, mutates, human-review), 4 source(s)

Defined by: structure=agent; autonomy=decides-or-acts; writer=outsider; outward-ungated=yes
Closure (all members agree): structure=agent; autonomy=decides-or-acts; writer=outsider; outward-ungated=yes
Sources: camunda-docs-blog 9, camunda-marketplace 6, quantumbpm 1, flows-for-apex 1
Members: camunda-docs-blog/012/C1, camunda-docs-blog/013/C1, camunda-docs-blog/021/C1, camunda-docs-blog/024/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/086/C1, camunda-docs-blog/121/C1, camunda-marketplace/006/C1, camunda-marketplace/008/C1, camunda-marketplace/023/C1, camunda-marketplace/165/C1, camunda-marketplace/228/C1, camunda-marketplace/255/C1, flows-for-apex/002/C1, quantumbpm/001/C1

### K100: 16 workflows, 3 slot(s) open (shape, outward-ungated, human-review), 5 source(s)

Defined by: structure=agent; autonomy=decides-or-acts; writer=outsider; mutates=some
Closure (all members agree): structure=agent; autonomy=decides-or-acts; writer=outsider; mutates=some
Sources: camunda-docs-blog 8, camunda-marketplace 4, flows-for-apex 2, quantumbpm 1, uipath-marketplace 1
Members: camunda-docs-blog/013/C1, camunda-docs-blog/019/C1, camunda-docs-blog/021/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/121/C1, camunda-docs-blog/122/C1, camunda-marketplace/006/C1, camunda-marketplace/008/C1, camunda-marketplace/023/C1, camunda-marketplace/228/C1, flows-for-apex/002/C1, flows-for-apex/003/C1, quantumbpm/001/C1, uipath-marketplace/001/C1

### K101: 16 workflows, 3 slot(s) open (structure, shape, mutates), 8 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; outward-ungated=no; human-review=no
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; outward-ungated=no; human-review=no
Sources: uipath-marketplace 4, camunda-docs-blog 3, camunda-marketplace 3, flowable 2, trisotech 1, newgen 1, firestart 1, flows-for-apex 1
Members: camunda-docs-blog/007/C1, camunda-docs-blog/019/C1, camunda-docs-blog/122/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1, camunda-marketplace/136/C1, firestart/013/C1, flowable/001/C1, flowable/166/C1, flows-for-apex/003/C1, newgen/037/C1, trisotech/001/C1, uipath-marketplace/001/C1, uipath-marketplace/002/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K102: 15 workflows, 3 slot(s) open (structure, mutates, human-review), 9 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=no
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=no
Sources: camunda-marketplace 3, camunda-docs-blog 2, firestart 2, uipath-marketplace 2, flowable 2, bonitasoft 1, trisotech 1, newgen 1, flows-for-apex 1
Members: bonitasoft/012/C1, camunda-docs-blog/007/C1, camunda-docs-blog/122/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1, camunda-marketplace/136/C1, firestart/012/C1, firestart/013/C1, flowable/001/C1, flowable/166/C1, flows-for-apex/003/C1, newgen/037/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K103: 15 workflows, 3 slot(s) open (structure, shape, outward-ungated), 7 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; mutates=none; human-review=no
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; mutates=none; human-review=no
Sources: camunda-marketplace 4, camunda-docs-blog 3, uipath-marketplace 3, flows-for-apex 2, trisotech 1, quantumbpm 1, flowable 1
Members: camunda-docs-blog/007/C1, camunda-docs-blog/012/C1, camunda-docs-blog/086/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1, camunda-marketplace/165/C1, camunda-marketplace/255/C1, flowable/001/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1, trisotech/001/C1, uipath-marketplace/002/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K104: 13 workflows, 3 slot(s) open (shape, outward-ungated, human-review), 8 source(s)

Defined by: structure=non-agent; autonomy=decides-or-acts; writer=outsider; mutates=none
Closure (all members agree): structure=non-agent; autonomy=decides-or-acts; writer=outsider; mutates=none
Sources: camunda-docs-blog 3, uipath-marketplace 2, flows-for-apex 2, camunda-marketplace 2, trisotech 1, firestart 1, quantumbpm 1, flowable 1
Members: camunda-docs-blog/001/C1, camunda-docs-blog/007/C1, camunda-docs-blog/016/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1, firestart/012/C1, flowable/001/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K105: 13 workflows, 3 slot(s) open (structure, outward-ungated, human-review), 4 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; shape=free-text; mutates=some
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; shape=free-text; mutates=some
Sources: camunda-docs-blog 8, camunda-marketplace 3, quantumbpm 1, uipath-marketplace 1
Members: camunda-docs-blog/008/C1, camunda-docs-blog/013/C1, camunda-docs-blog/019/C1, camunda-docs-blog/021/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/121/C1, camunda-marketplace/006/C1, camunda-marketplace/023/C1, camunda-marketplace/228/C1, quantumbpm/001/C1, uipath-marketplace/001/C1

### K106: 12 workflows, 3 slot(s) open (autonomy, outward-ungated, human-review), 4 source(s)

Defined by: structure=non-agent; writer=outsider; shape=not-free-text; mutates=some
Closure (all members agree): structure=non-agent; writer=outsider; shape=not-free-text; mutates=some
Sources: firestart 6, camunda-marketplace 4, bonitasoft 1, uipath-marketplace 1
Members: bonitasoft/012/C1, camunda-marketplace/022/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, camunda-marketplace/136/C1, firestart/002/C1, firestart/006/C1, firestart/007/C1, firestart/008/C1, firestart/011/C1, firestart/013/C1, uipath-marketplace/005/C3

### K107: 12 workflows, 3 slot(s) open (structure, outward-ungated, human-review), 5 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; shape=not-free-text; mutates=some
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; shape=not-free-text; mutates=some
Sources: camunda-marketplace 5, firestart 3, flows-for-apex 2, bonitasoft 1, camunda-docs-blog 1
Members: bonitasoft/012/C1, camunda-docs-blog/122/C1, camunda-marketplace/008/C1, camunda-marketplace/022/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, camunda-marketplace/136/C1, firestart/002/C1, firestart/008/C1, firestart/013/C1, flows-for-apex/002/C1, flows-for-apex/003/C1

### K108: 12 workflows, 3 slot(s) open (structure, outward-ungated, human-review), 5 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; shape=free-text; mutates=none
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; shape=free-text; mutates=none
Sources: camunda-docs-blog 4, camunda-marketplace 4, flows-for-apex 2, quantumbpm 1, uipath-marketplace 1
Members: camunda-docs-blog/012/C1, camunda-docs-blog/016/C1, camunda-docs-blog/024/C1, camunda-docs-blog/086/C1, camunda-marketplace/005/C1, camunda-marketplace/165/C1, camunda-marketplace/188/C1, camunda-marketplace/255/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1, uipath-marketplace/002/C1

### K109: 11 workflows, 3 slot(s) open (shape, mutates, human-review), 5 source(s)

Defined by: structure=non-agent; autonomy=decides-or-acts; writer=outsider; outward-ungated=yes
Closure (all members agree): structure=non-agent; autonomy=decides-or-acts; writer=outsider; outward-ungated=yes
Sources: camunda-docs-blog 3, camunda-marketplace 3, firestart 2, flows-for-apex 2, quantumbpm 1
Members: camunda-docs-blog/001/C1, camunda-docs-blog/008/C1, camunda-docs-blog/016/C1, camunda-marketplace/022/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, firestart/002/C1, firestart/008/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1

### K110: 11 workflows, 3 slot(s) open (structure, shape, human-review), 6 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; outward-ungated=no; mutates=none
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; outward-ungated=no; mutates=none
Sources: camunda-marketplace 4, uipath-marketplace 3, trisotech 1, firestart 1, camunda-docs-blog 1, flowable 1
Members: camunda-docs-blog/007/C1, camunda-marketplace/005/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1, camunda-marketplace/188/C1, firestart/012/C1, flowable/001/C1, trisotech/001/C1, uipath-marketplace/002/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K111: 10 workflows, 3 slot(s) open (autonomy, outward-ungated, human-review), 6 source(s)

Defined by: structure=non-agent; writer=outsider; shape=not-free-text; mutates=none
Closure (all members agree): structure=non-agent; writer=outsider; shape=not-free-text; mutates=none
Sources: firestart 2, uipath-marketplace 2, camunda-docs-blog 2, camunda-marketplace 2, trisotech 1, flowable 1
Members: camunda-docs-blog/001/C1, camunda-docs-blog/007/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1, firestart/001/C1, firestart/012/C1, flowable/001/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K112: 10 workflows, 3 slot(s) open (autonomy, shape, human-review), 6 source(s)

Defined by: structure=non-agent; writer=outsider; outward-ungated=no; mutates=none
Closure (all members agree): structure=non-agent; writer=outsider; outward-ungated=no; mutates=none
Sources: firestart 2, uipath-marketplace 2, camunda-docs-blog 2, camunda-marketplace 2, trisotech 1, flowable 1
Members: camunda-docs-blog/007/C1, camunda-docs-blog/047/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1, firestart/001/C1, firestart/012/C1, flowable/001/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K113: 10 workflows, 3 slot(s) open (autonomy, shape, outward-ungated), 3 source(s)

Defined by: structure=non-agent; writer=outsider; mutates=some; human-review=no
Closure (all members agree): structure=non-agent; writer=outsider; mutates=some; human-review=no
Sources: firestart 4, camunda-marketplace 4, uipath-marketplace 2
Members: camunda-marketplace/022/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, camunda-marketplace/136/C1, firestart/002/C1, firestart/008/C1, firestart/011/C1, firestart/013/C1, uipath-marketplace/005/C3, uipath-marketplace/007/C1

### K114: 10 workflows, 3 slot(s) open (structure, shape, human-review), 4 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; outward-ungated=yes; mutates=none
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; outward-ungated=yes; mutates=none
Sources: camunda-docs-blog 5, camunda-marketplace 2, flows-for-apex 2, quantumbpm 1
Members: camunda-docs-blog/001/C1, camunda-docs-blog/012/C1, camunda-docs-blog/016/C1, camunda-docs-blog/024/C1, camunda-docs-blog/086/C1, camunda-marketplace/165/C1, camunda-marketplace/255/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1

### K115: 9 workflows, 3 slot(s) open (shape, outward-ungated, human-review), 4 source(s)

Defined by: structure=non-agent; autonomy=decides-or-acts; writer=outsider; mutates=some
Closure (all members agree): structure=non-agent; autonomy=decides-or-acts; writer=outsider; mutates=some
Sources: camunda-marketplace 4, firestart 3, camunda-docs-blog 1, bonitasoft 1
Members: bonitasoft/012/C1, camunda-docs-blog/008/C1, camunda-marketplace/022/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, camunda-marketplace/136/C1, firestart/002/C1, firestart/008/C1, firestart/013/C1

### K116: 9 workflows, 3 slot(s) open (autonomy, shape, mutates), 5 source(s)

Defined by: structure=non-agent; writer=outsider; outward-ungated=yes; human-review=no
Closure (all members agree): structure=non-agent; writer=outsider; outward-ungated=yes; human-review=no
Sources: camunda-marketplace 3, firestart 2, flows-for-apex 2, uipath-marketplace 1, quantumbpm 1
Members: camunda-marketplace/022/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, firestart/002/C1, firestart/008/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1, uipath-marketplace/007/C1

### K117: 8 workflows, 3 slot(s) open (shape, mutates, human-review), 4 source(s)

Defined by: structure=non-agent; autonomy=suggests; writer=outsider; outward-ungated=no
Closure (all members agree): structure=non-agent; autonomy=suggests; writer=outsider; outward-ungated=no
Sources: firestart 4, uipath-marketplace 2, uipath-maestro-docs 1, camunda-docs-blog 1
Members: camunda-docs-blog/047/C1, firestart/001/C1, firestart/006/C1, firestart/007/C1, firestart/011/C1, uipath-maestro-docs/192/C1, uipath-marketplace/005/C3, uipath-marketplace/006/C4

### K118: 8 workflows, 3 slot(s) open (structure, mutates, human-review), 4 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=yes
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; shape=not-free-text; outward-ungated=yes
Sources: camunda-marketplace 4, firestart 2, camunda-docs-blog 1, flows-for-apex 1
Members: camunda-docs-blog/001/C1, camunda-marketplace/008/C1, camunda-marketplace/022/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, firestart/002/C1, firestart/008/C1, flows-for-apex/002/C1

### K119: 7 workflows, 3 slot(s) open (shape, mutates, human-review), 4 source(s)

Defined by: structure=agent; autonomy=decides-or-acts; writer=outsider; outward-ungated=no
Closure (all members agree): structure=agent; autonomy=decides-or-acts; writer=outsider; outward-ungated=no
Sources: camunda-docs-blog 2, uipath-marketplace 2, camunda-marketplace 2, flows-for-apex 1
Members: camunda-docs-blog/019/C1, camunda-docs-blog/122/C1, camunda-marketplace/005/C1, camunda-marketplace/188/C1, flows-for-apex/003/C1, uipath-marketplace/001/C1, uipath-marketplace/002/C1

### K120: 7 workflows, 3 slot(s) open (autonomy, shape, human-review), 4 source(s)

Defined by: structure=non-agent; writer=outsider; outward-ungated=yes; mutates=some
Closure (all members agree): structure=non-agent; writer=outsider; outward-ungated=yes; mutates=some
Sources: camunda-marketplace 3, firestart 2, camunda-docs-blog 1, uipath-marketplace 1
Members: camunda-docs-blog/008/C1, camunda-marketplace/022/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, firestart/002/C1, firestart/008/C1, uipath-marketplace/007/C1

### K121: 7 workflows, 3 slot(s) open (autonomy, shape, mutates), 4 source(s)

Defined by: structure=non-agent; writer=outsider; outward-ungated=no; human-review=yes
Closure (all members agree): structure=non-agent; writer=outsider; outward-ungated=no; human-review=yes
Sources: firestart 4, bonitasoft 1, uipath-maestro-docs 1, camunda-docs-blog 1
Members: bonitasoft/012/C1, camunda-docs-blog/047/C1, firestart/001/C1, firestart/006/C1, firestart/007/C1, firestart/012/C1, uipath-maestro-docs/192/C1

### K122: 7 workflows, 3 slot(s) open (structure, shape, human-review), 6 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; outward-ungated=no; mutates=some
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; outward-ungated=no; mutates=some
Sources: camunda-docs-blog 2, bonitasoft 1, uipath-marketplace 1, firestart 1, camunda-marketplace 1, flows-for-apex 1
Members: bonitasoft/012/C1, camunda-docs-blog/019/C1, camunda-docs-blog/122/C1, camunda-marketplace/136/C1, firestart/013/C1, flows-for-apex/003/C1, uipath-marketplace/001/C1

### K123: 6 workflows, 3 slot(s) open (shape, mutates, human-review), 5 source(s)

Defined by: structure=non-agent; autonomy=suggests; writer=not-outsider; outward-ungated=no
Closure (all members agree): structure=non-agent; autonomy=suggests; writer=not-outsider; outward-ungated=no
Sources: firestart 2, atamya 1, bizagi 1, camunda-marketplace 1, uipath-marketplace 1
Members: atamya/010/C1, bizagi/002/C1, camunda-marketplace/064/C1, firestart/003/C1, firestart/015/C1, uipath-marketplace/003/C1

### K124: 6 workflows, 3 slot(s) open (autonomy, mutates, human-review), 4 source(s)

Defined by: structure=non-agent; writer=outsider; shape=free-text; outward-ungated=yes
Closure (all members agree): structure=non-agent; writer=outsider; shape=free-text; outward-ungated=yes
Sources: camunda-docs-blog 2, flows-for-apex 2, uipath-marketplace 1, quantumbpm 1
Members: camunda-docs-blog/008/C1, camunda-docs-blog/016/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1, uipath-marketplace/007/C1

### K125: 6 workflows, 3 slot(s) open (autonomy, outward-ungated, mutates), 3 source(s)

Defined by: structure=non-agent; writer=outsider; shape=not-free-text; human-review=yes
Closure (all members agree): structure=non-agent; writer=outsider; shape=not-free-text; human-review=yes
Sources: firestart 4, bonitasoft 1, camunda-docs-blog 1
Members: bonitasoft/012/C1, camunda-docs-blog/001/C1, firestart/001/C1, firestart/006/C1, firestart/007/C1, firestart/012/C1

### K126: 6 workflows, 3 slot(s) open (structure, outward-ungated, mutates), 2 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; shape=free-text; human-review=yes
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; shape=free-text; human-review=yes
Sources: camunda-docs-blog 3, camunda-marketplace 3
Members: camunda-docs-blog/008/C1, camunda-docs-blog/016/C1, camunda-docs-blog/024/C1, camunda-marketplace/005/C1, camunda-marketplace/188/C1, camunda-marketplace/228/C1

### K127: 6 workflows, 3 slot(s) open (structure, shape, mutates), 2 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; outward-ungated=yes; human-review=yes
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; outward-ungated=yes; human-review=yes
Sources: camunda-docs-blog 4, camunda-marketplace 2
Members: camunda-docs-blog/001/C1, camunda-docs-blog/008/C1, camunda-docs-blog/016/C1, camunda-docs-blog/024/C1, camunda-marketplace/008/C1, camunda-marketplace/228/C1

### K128: 6 workflows, 3 slot(s) open (structure, shape, outward-ungated), 3 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; mutates=none; human-review=yes
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; mutates=none; human-review=yes
Sources: camunda-docs-blog 3, camunda-marketplace 2, firestart 1
Members: camunda-docs-blog/001/C1, camunda-docs-blog/016/C1, camunda-docs-blog/024/C1, camunda-marketplace/005/C1, camunda-marketplace/188/C1, firestart/012/C1

### K129: 5 workflows, 3 slot(s) open (shape, outward-ungated, human-review), 2 source(s)

Defined by: structure=non-agent; autonomy=suggests; writer=outsider; mutates=some
Closure (all members agree): structure=non-agent; autonomy=suggests; writer=outsider; mutates=some
Sources: firestart 3, uipath-marketplace 2
Members: firestart/006/C1, firestart/007/C1, firestart/011/C1, uipath-marketplace/005/C3, uipath-marketplace/007/C1

### K130: 5 workflows, 3 slot(s) open (autonomy, mutates, human-review), 4 source(s)

Defined by: structure=non-agent; writer=not-outsider; shape=not-free-text; outward-ungated=no
Closure (all members agree): structure=non-agent; writer=not-outsider; shape=not-free-text; outward-ungated=no
Sources: firestart 2, bizagi 1, camunda-marketplace 1, uipath-maestro-docs 1
Members: bizagi/002/C1, camunda-marketplace/064/C1, firestart/003/C1, firestart/015/C1, uipath-maestro-docs/133/C1

### K131: 5 workflows, 3 slot(s) open (autonomy, outward-ungated, human-review), 3 source(s)

Defined by: structure=non-agent; writer=outsider; shape=free-text; mutates=none
Closure (all members agree): structure=non-agent; writer=outsider; shape=free-text; mutates=none
Sources: camunda-docs-blog 2, flows-for-apex 2, quantumbpm 1
Members: camunda-docs-blog/016/C1, camunda-docs-blog/047/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1

### K132: 5 workflows, 3 slot(s) open (autonomy, shape, human-review), 4 source(s)

Defined by: structure=non-agent; writer=not-outsider; outward-ungated=no; mutates=some
Closure (all members agree): structure=non-agent; writer=not-outsider; outward-ungated=no; mutates=some
Sources: bizagi 2, atamya 1, uipath-maestro-docs 1, uipath-marketplace 1
Members: atamya/010/C1, bizagi/001/C1, bizagi/002/C1, uipath-maestro-docs/133/C1, uipath-marketplace/003/C1

### K133: 5 workflows, 3 slot(s) open (autonomy, shape, mutates), 3 source(s)

Defined by: structure=non-agent; writer=not-outsider; outward-ungated=no; human-review=yes
Closure (all members agree): structure=non-agent; writer=not-outsider; outward-ungated=no; human-review=yes
Sources: firestart 2, bizagi 2, atamya 1
Members: atamya/010/C1, bizagi/001/C1, bizagi/002/C1, firestart/003/C1, firestart/015/C1

### K134: 5 workflows, 3 slot(s) open (autonomy, shape, outward-ungated), 2 source(s)

Defined by: structure=non-agent; writer=outsider; mutates=none; human-review=yes
Closure (all members agree): structure=non-agent; writer=outsider; mutates=none; human-review=yes
Sources: camunda-docs-blog 3, firestart 2
Members: camunda-docs-blog/001/C1, camunda-docs-blog/016/C1, camunda-docs-blog/047/C1, firestart/001/C1, firestart/012/C1

### K135: 4 workflows, 3 slot(s) open (autonomy, outward-ungated, human-review), 3 source(s)

Defined by: structure=non-agent; writer=not-outsider; shape=free-text; mutates=some
Closure (all members agree): structure=non-agent; writer=not-outsider; shape=free-text; mutates=some
Sources: atamya 2, uipath-marketplace 1, bizagi 1
Members: atamya/010/C1, atamya/011/C1, bizagi/001/C1, uipath-marketplace/003/C1

### K136: 4 workflows, 3 slot(s) open (autonomy, outward-ungated, mutates), 2 source(s)

Defined by: structure=non-agent; writer=outsider; shape=free-text; human-review=yes
Closure (all members agree): structure=non-agent; writer=outsider; shape=free-text; human-review=yes
Sources: camunda-docs-blog 3, uipath-maestro-docs 1
Members: camunda-docs-blog/008/C1, camunda-docs-blog/016/C1, camunda-docs-blog/047/C1, uipath-maestro-docs/192/C1

### K137: 4 workflows, 3 slot(s) open (autonomy, shape, outward-ungated), 3 source(s)

Defined by: structure=non-agent; writer=outsider; mutates=some; human-review=yes
Closure (all members agree): structure=non-agent; writer=outsider; mutates=some; human-review=yes
Sources: firestart 2, bonitasoft 1, camunda-docs-blog 1
Members: bonitasoft/012/C1, camunda-docs-blog/008/C1, firestart/006/C1, firestart/007/C1

### K138: 4 workflows, 3 slot(s) open (structure, outward-ungated, mutates), 4 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; shape=not-free-text; human-review=yes
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; shape=not-free-text; human-review=yes
Sources: bonitasoft 1, camunda-docs-blog 1, camunda-marketplace 1, firestart 1
Members: bonitasoft/012/C1, camunda-docs-blog/001/C1, camunda-marketplace/008/C1, firestart/012/C1

### K139: 4 workflows, 3 slot(s) open (structure, shape, mutates), 3 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; outward-ungated=no; human-review=yes
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; outward-ungated=no; human-review=yes
Sources: camunda-marketplace 2, bonitasoft 1, firestart 1
Members: bonitasoft/012/C1, camunda-marketplace/005/C1, camunda-marketplace/188/C1, firestart/012/C1

### K140: 4 workflows, 3 slot(s) open (structure, shape, outward-ungated), 3 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; mutates=some; human-review=yes
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; mutates=some; human-review=yes
Sources: camunda-marketplace 2, bonitasoft 1, camunda-docs-blog 1
Members: bonitasoft/012/C1, camunda-docs-blog/008/C1, camunda-marketplace/008/C1, camunda-marketplace/228/C1

### K141: 3 workflows, 3 slot(s) open (outward-ungated, mutates, human-review), 3 source(s)

Defined by: structure=non-agent; autonomy=suggests; writer=outsider; shape=free-text
Closure (all members agree): structure=non-agent; autonomy=suggests; writer=outsider; shape=free-text
Sources: camunda-docs-blog 1, uipath-marketplace 1, uipath-maestro-docs 1
Members: camunda-docs-blog/047/C1, uipath-maestro-docs/192/C1, uipath-marketplace/007/C1

### K142: 3 workflows, 3 slot(s) open (shape, outward-ungated, human-review), 3 source(s)

Defined by: structure=non-agent; autonomy=decides-or-acts; writer=not-outsider; mutates=some
Closure (all members agree): structure=non-agent; autonomy=decides-or-acts; writer=not-outsider; mutates=some
Sources: atamya 1, bizagi 1, uipath-maestro-docs 1
Members: atamya/011/C1, bizagi/001/C1, uipath-maestro-docs/133/C1

### K143: 3 workflows, 3 slot(s) open (autonomy, shape, mutates), 3 source(s)

Defined by: structure=non-agent; writer=not-outsider; outward-ungated=no; human-review=no
Closure (all members agree): structure=non-agent; writer=not-outsider; outward-ungated=no; human-review=no
Sources: uipath-marketplace 1, camunda-marketplace 1, uipath-maestro-docs 1
Members: camunda-marketplace/064/C1, uipath-maestro-docs/133/C1, uipath-marketplace/003/C1

### K144: 3 workflows, 3 slot(s) open (autonomy, shape, outward-ungated), 3 source(s)

Defined by: structure=non-agent; writer=not-outsider; mutates=some; human-review=no
Closure (all members agree): structure=non-agent; writer=not-outsider; mutates=some; human-review=no
Sources: uipath-marketplace 1, atamya 1, uipath-maestro-docs 1
Members: atamya/011/C1, uipath-maestro-docs/133/C1, uipath-marketplace/003/C1

### K145: 3 workflows, 3 slot(s) open (structure, shape, human-review), 3 source(s)

Defined by: autonomy=decides-or-acts; writer=not-outsider; outward-ungated=no; mutates=some
Closure (all members agree): autonomy=decides-or-acts; writer=not-outsider; outward-ungated=no; mutates=some
Sources: bizagi 1, camunda-marketplace 1, uipath-maestro-docs 1
Members: bizagi/001/C1, camunda-marketplace/252/C1, uipath-maestro-docs/133/C1

### K146: 3 workflows, 3 slot(s) open (structure, shape, outward-ungated), 3 source(s)

Defined by: autonomy=decides-or-acts; writer=not-outsider; mutates=some; human-review=no
Closure (all members agree): autonomy=decides-or-acts; writer=not-outsider; mutates=some; human-review=no
Sources: atamya 1, camunda-marketplace 1, uipath-maestro-docs 1
Members: atamya/011/C1, camunda-marketplace/252/C1, uipath-maestro-docs/133/C1

### K147: 28 workflows, 4 slot(s) open (structure, shape, mutates, human-review), 5 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; outward-ungated=yes
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; outward-ungated=yes
Sources: camunda-docs-blog 12, camunda-marketplace 9, flows-for-apex 3, firestart 2, quantumbpm 2
Members: camunda-docs-blog/001/C1, camunda-docs-blog/008/C1, camunda-docs-blog/012/C1, camunda-docs-blog/013/C1, camunda-docs-blog/016/C1, camunda-docs-blog/021/C1, camunda-docs-blog/024/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/086/C1, camunda-docs-blog/121/C1, camunda-marketplace/006/C1, camunda-marketplace/008/C1, camunda-marketplace/022/C1, camunda-marketplace/023/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, camunda-marketplace/165/C1, camunda-marketplace/228/C1, camunda-marketplace/255/C1, firestart/002/C1, firestart/008/C1, flows-for-apex/001/C1, flows-for-apex/002/C1, flows-for-apex/004/C1, quantumbpm/001/C1, quantumbpm/002/C1

### K148: 25 workflows, 4 slot(s) open (structure, outward-ungated, mutates, human-review), 5 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; shape=free-text
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; shape=free-text
Sources: camunda-docs-blog 12, camunda-marketplace 7, quantumbpm 2, flows-for-apex 2, uipath-marketplace 2
Members: camunda-docs-blog/008/C1, camunda-docs-blog/012/C1, camunda-docs-blog/013/C1, camunda-docs-blog/016/C1, camunda-docs-blog/019/C1, camunda-docs-blog/021/C1, camunda-docs-blog/024/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/086/C1, camunda-docs-blog/121/C1, camunda-marketplace/005/C1, camunda-marketplace/006/C1, camunda-marketplace/023/C1, camunda-marketplace/165/C1, camunda-marketplace/188/C1, camunda-marketplace/228/C1, camunda-marketplace/255/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/001/C1, quantumbpm/002/C1, uipath-marketplace/001/C1, uipath-marketplace/002/C1

### K149: 25 workflows, 4 slot(s) open (structure, shape, outward-ungated, human-review), 7 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; mutates=some
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; mutates=some
Sources: camunda-docs-blog 9, camunda-marketplace 8, firestart 3, flows-for-apex 2, quantumbpm 1, bonitasoft 1, uipath-marketplace 1
Members: bonitasoft/012/C1, camunda-docs-blog/008/C1, camunda-docs-blog/013/C1, camunda-docs-blog/019/C1, camunda-docs-blog/021/C1, camunda-docs-blog/067/C1, camunda-docs-blog/075/C1, camunda-docs-blog/077/C1, camunda-docs-blog/121/C1, camunda-docs-blog/122/C1, camunda-marketplace/006/C1, camunda-marketplace/008/C1, camunda-marketplace/022/C1, camunda-marketplace/023/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, camunda-marketplace/136/C1, camunda-marketplace/228/C1, firestart/002/C1, firestart/008/C1, firestart/013/C1, flows-for-apex/002/C1, flows-for-apex/003/C1, quantumbpm/001/C1, uipath-marketplace/001/C1

### K150: 24 workflows, 4 slot(s) open (autonomy, outward-ungated, mutates, human-review), 8 source(s)

Defined by: structure=non-agent; writer=outsider; shape=not-free-text
Closure (all members agree): structure=non-agent; writer=outsider; shape=not-free-text
Sources: firestart 8, camunda-marketplace 6, uipath-marketplace 3, camunda-docs-blog 2, flowable 2, trisotech 1, bonitasoft 1, newgen 1
Members: bonitasoft/012/C1, camunda-docs-blog/001/C1, camunda-docs-blog/007/C1, camunda-marketplace/016/C1, camunda-marketplace/022/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, camunda-marketplace/112/C1, camunda-marketplace/136/C1, firestart/001/C1, firestart/002/C1, firestart/006/C1, firestart/007/C1, firestart/008/C1, firestart/011/C1, firestart/012/C1, firestart/013/C1, flowable/001/C1, flowable/166/C1, newgen/037/C1, trisotech/001/C1, uipath-marketplace/005/C3, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/006/C4, uipath-marketplace/007/C2

### K151: 23 workflows, 4 slot(s) open (structure, outward-ungated, mutates, human-review), 9 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; shape=not-free-text
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; shape=not-free-text
Sources: camunda-marketplace 7, firestart 4, camunda-docs-blog 3, flows-for-apex 2, flowable 2, uipath-marketplace 2, trisotech 1, bonitasoft 1, newgen 1
Members: bonitasoft/012/C1, camunda-docs-blog/001/C1, camunda-docs-blog/007/C1, camunda-docs-blog/122/C1, camunda-marketplace/008/C1, camunda-marketplace/016/C1, camunda-marketplace/022/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, camunda-marketplace/112/C1, camunda-marketplace/136/C1, firestart/002/C1, firestart/008/C1, firestart/012/C1, firestart/013/C1, flowable/001/C1, flowable/166/C1, flows-for-apex/002/C1, flows-for-apex/003/C1, newgen/037/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K152: 21 workflows, 4 slot(s) open (structure, shape, outward-ungated, human-review), 8 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; mutates=none
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; mutates=none
Sources: camunda-docs-blog 6, camunda-marketplace 6, uipath-marketplace 3, flows-for-apex 2, trisotech 1, quantumbpm 1, flowable 1, firestart 1
Members: camunda-docs-blog/001/C1, camunda-docs-blog/007/C1, camunda-docs-blog/012/C1, camunda-docs-blog/016/C1, camunda-docs-blog/024/C1, camunda-docs-blog/086/C1, camunda-marketplace/005/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1, camunda-marketplace/165/C1, camunda-marketplace/188/C1, camunda-marketplace/255/C1, firestart/012/C1, flowable/001/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1, trisotech/001/C1, uipath-marketplace/002/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K153: 20 workflows, 4 slot(s) open (autonomy, shape, mutates, human-review), 9 source(s)

Defined by: structure=non-agent; writer=outsider; outward-ungated=no
Closure (all members agree): structure=non-agent; writer=outsider; outward-ungated=no
Sources: firestart 6, camunda-marketplace 3, uipath-marketplace 3, camunda-docs-blog 2, flowable 2, trisotech 1, bonitasoft 1, uipath-maestro-docs 1, newgen 1
Members: bonitasoft/012/C1, camunda-docs-blog/007/C1, camunda-docs-blog/047/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1, camunda-marketplace/136/C1, firestart/001/C1, firestart/006/C1, firestart/007/C1, firestart/011/C1, firestart/012/C1, firestart/013/C1, flowable/001/C1, flowable/166/C1, newgen/037/C1, trisotech/001/C1, uipath-maestro-docs/192/C1, uipath-marketplace/005/C3, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/006/C4, uipath-marketplace/007/C2

### K154: 20 workflows, 4 slot(s) open (structure, shape, mutates, human-review), 9 source(s)

Defined by: autonomy=decides-or-acts; writer=outsider; outward-ungated=no
Closure (all members agree): autonomy=decides-or-acts; writer=outsider; outward-ungated=no
Sources: camunda-marketplace 5, uipath-marketplace 4, camunda-docs-blog 3, flowable 2, firestart 2, trisotech 1, bonitasoft 1, flows-for-apex 1, newgen 1
Members: bonitasoft/012/C1, camunda-docs-blog/007/C1, camunda-docs-blog/019/C1, camunda-docs-blog/122/C1, camunda-marketplace/005/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1, camunda-marketplace/136/C1, camunda-marketplace/188/C1, firestart/012/C1, firestart/013/C1, flowable/001/C1, flowable/166/C1, flows-for-apex/003/C1, newgen/037/C1, trisotech/001/C1, uipath-marketplace/001/C1, uipath-marketplace/002/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K155: 15 workflows, 4 slot(s) open (autonomy, shape, outward-ungated, human-review), 8 source(s)

Defined by: structure=non-agent; writer=outsider; mutates=none
Closure (all members agree): structure=non-agent; writer=outsider; mutates=none
Sources: camunda-docs-blog 4, firestart 2, uipath-marketplace 2, flows-for-apex 2, camunda-marketplace 2, trisotech 1, quantumbpm 1, flowable 1
Members: camunda-docs-blog/001/C1, camunda-docs-blog/007/C1, camunda-docs-blog/016/C1, camunda-docs-blog/047/C1, camunda-marketplace/016/C1, camunda-marketplace/112/C1, firestart/001/C1, firestart/012/C1, flowable/001/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1, trisotech/001/C1, uipath-marketplace/006/C1, uipath-marketplace/006/C2, uipath-marketplace/006/C3, uipath-marketplace/007/C2

### K156: 14 workflows, 4 slot(s) open (autonomy, shape, outward-ungated, human-review), 5 source(s)

Defined by: structure=non-agent; writer=outsider; mutates=some
Closure (all members agree): structure=non-agent; writer=outsider; mutates=some
Sources: firestart 6, camunda-marketplace 4, uipath-marketplace 2, camunda-docs-blog 1, bonitasoft 1
Members: bonitasoft/012/C1, camunda-docs-blog/008/C1, camunda-marketplace/022/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, camunda-marketplace/136/C1, firestart/002/C1, firestart/006/C1, firestart/007/C1, firestart/008/C1, firestart/011/C1, firestart/013/C1, uipath-marketplace/005/C3, uipath-marketplace/007/C1

### K157: 12 workflows, 4 slot(s) open (autonomy, shape, mutates, human-review), 6 source(s)

Defined by: structure=non-agent; writer=outsider; outward-ungated=yes
Closure (all members agree): structure=non-agent; writer=outsider; outward-ungated=yes
Sources: camunda-docs-blog 3, camunda-marketplace 3, firestart 2, flows-for-apex 2, uipath-marketplace 1, quantumbpm 1
Members: camunda-docs-blog/001/C1, camunda-docs-blog/008/C1, camunda-docs-blog/016/C1, camunda-marketplace/022/C1, camunda-marketplace/064/C2, camunda-marketplace/067/C1, firestart/002/C1, firestart/008/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1, uipath-marketplace/007/C1

### K158: 8 workflows, 4 slot(s) open (autonomy, outward-ungated, mutates, human-review), 5 source(s)

Defined by: structure=non-agent; writer=outsider; shape=free-text
Closure (all members agree): structure=non-agent; writer=outsider; shape=free-text
Sources: camunda-docs-blog 3, flows-for-apex 2, uipath-marketplace 1, uipath-maestro-docs 1, quantumbpm 1
Members: camunda-docs-blog/008/C1, camunda-docs-blog/016/C1, camunda-docs-blog/047/C1, flows-for-apex/001/C1, flows-for-apex/004/C1, quantumbpm/002/C1, uipath-maestro-docs/192/C1, uipath-marketplace/007/C1

### K159: 8 workflows, 4 slot(s) open (autonomy, shape, mutates, human-review), 6 source(s)

Defined by: structure=non-agent; writer=not-outsider; outward-ungated=no
Closure (all members agree): structure=non-agent; writer=not-outsider; outward-ungated=no
Sources: firestart 2, bizagi 2, atamya 1, camunda-marketplace 1, uipath-maestro-docs 1, uipath-marketplace 1
Members: atamya/010/C1, bizagi/001/C1, bizagi/002/C1, camunda-marketplace/064/C1, firestart/003/C1, firestart/015/C1, uipath-maestro-docs/133/C1, uipath-marketplace/003/C1

### K160: 6 workflows, 4 slot(s) open (autonomy, shape, outward-ungated, human-review), 4 source(s)

Defined by: structure=non-agent; writer=not-outsider; mutates=some
Closure (all members agree): structure=non-agent; writer=not-outsider; mutates=some
Sources: atamya 2, bizagi 2, uipath-maestro-docs 1, uipath-marketplace 1
Members: atamya/010/C1, atamya/011/C1, bizagi/001/C1, bizagi/002/C1, uipath-maestro-docs/133/C1, uipath-marketplace/003/C1

### K161: 4 workflows, 4 slot(s) open (structure, shape, outward-ungated, human-review), 4 source(s)

Defined by: autonomy=decides-or-acts; writer=not-outsider; mutates=some
Closure (all members agree): autonomy=decides-or-acts; writer=not-outsider; mutates=some
Sources: atamya 1, bizagi 1, camunda-marketplace 1, uipath-maestro-docs 1
Members: atamya/011/C1, bizagi/001/C1, camunda-marketplace/252/C1, uipath-maestro-docs/133/C1
