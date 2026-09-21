---
layout: feed_note
title: "VLA의 회전 일반화를 demonstration 대신 symmetry로 넣었습니다"
date: 2026-09-21 22:10:00 +0900
channel: research-papers
channel_label: Research Papers
summary: "SAVLA는 frozen vision-language backbone에 equivariant flow-matching action head와 learned canonicalizer를 결합해, LIBERO-Goal rotation 조건에서 GR00T N1.5의 41.5%를 90.4%로 끌어올렸습니다."
---

**SAVLA는 VLA가 demonstration에서 공간 관계를 전부 외우게 두는 대신, rotation symmetry를 policy 구조에 직접 넣었습니다.**

최근 공개된 **SAVLA (Symmetry-Aware Vision-Language-Action)** 는 pretrained vision-language backbone을 그대로 frozen한 채, **equivariant flow-matching action head**와 **learned canonicalizer**를 붙입니다.

핵심 문제는 VLA의 spatial competence가 demonstration이 보여준 pose 범위에 크게 의존한다는 점입니다. 카메라나 물체 배치가 회전하면 같은 manipulation task라도 policy가 쉽게 distribution shift를 만납니다.

SAVLA의 action head는 state·action·conditioning을 invariant/equivariant channel로 나눠 geometric transformation 관계를 유지하고, canonicalizer는 oblique-view image를 canonical frame으로 바꾸면서 geometric condition도 함께 회전시킵니다.

결과가 꽤 큽니다. **LIBERO 4개 suite 평균에서는 GR00T N1.5 대비 success rate가 5.1 percentage points 상승했고, LIBERO-Goal의 rotation 조건에서는 41.5% → 90.4%**로 올라갔습니다.

이 논문에서 흥미로운 지점은 더 많은 demonstration만으로 spatial generalization을 해결하려 하지 않는다는 것입니다. manipulation에서 viewpoint·object pose 변화처럼 구조적으로 예상 가능한 variation은 **data augmentation만이 아니라 policy의 inductive bias로 넣을 수 있다**는 방향입니다.

실제 robot에서는 camera pose, workspace orientation, embodiment 차이까지 섞이기 때문에 LIBERO 결과가 그대로 real-world robustness를 의미하지는 않습니다. 그래도 VLA의 geometric generalization을 별도 설계 문제로 떼어낸 접근은 manipulation 쪽에서 확인할 가치가 있습니다.

## Sources

- [arXiv — SAVLA: Symmetry-Aware Vision-Language-Action Models for Robotic Manipulation](https://arxiv.org/abs/2609.16641)
