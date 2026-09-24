---
layout: feed_note
title: "VLA에 symmetry와 task-focused 3D dynamics를 넣는 두 가지 접근"
date: 2026-09-21 22:45:00 +0900
channel: research-papers
channel_label: Research Papers
summary: "SAVLA는 rotation symmetry를 policy에 직접 넣고, FOCAL-VLA는 현재 subtask에 필요한 geometry와 future interaction dynamics만 distill해 VLA의 spatial-temporal representation을 강화합니다."
---

## SAVLA는 VLA가 demonstration에서 공간 관계를 전부 외우게 두는 대신, rotation symmetry를 policy 구조에 직접 넣었습니다.
최근 공개된 **SAVLA (Symmetry-Aware Vision-Language-Action)** 는 pretrained vision-language backbone을 그대로 frozen한 채, **equivariant flow-matching action head**와 **learned canonicalizer**를 붙입니다.

핵심 문제는 VLA의 spatial competence가 demonstration이 보여준 pose 범위에 크게 의존한다는 점입니다. 카메라나 물체 배치가 회전하면 같은 manipulation task라도 policy가 쉽게 distribution shift를 만납니다.

SAVLA의 action head는 state·action·conditioning을 invariant/equivariant channel로 나눠 geometric transformation 관계를 유지하고, canonicalizer는 oblique-view image를 canonical frame으로 바꾸면서 geometric condition도 함께 회전시킵니다.

결과가 꽤 큽니다. **LIBERO 4개 suite 평균에서는 GR00T N1.5 대비 success rate가 5.1 percentage points 상승했고, LIBERO-Goal의 rotation 조건에서는 41.5% → 90.4%**로 올라갔습니다.

이 논문에서 흥미로운 지점은 더 많은 demonstration만으로 spatial generalization을 해결하려 하지 않는다는 것입니다. manipulation에서 viewpoint·object pose 변화처럼 구조적으로 예상 가능한 variation은 **data augmentation만이 아니라 policy의 inductive bias로 넣을 수 있다**는 방향입니다.

실제 robot에서는 camera pose, workspace orientation, embodiment 차이까지 섞이기 때문에 LIBERO 결과가 그대로 real-world robustness를 의미하지는 않습니다. 그래도 VLA의 geometric generalization을 별도 설계 문제로 떼어낸 접근은 manipulation 쪽에서 확인할 가치가 있습니다.

## FOCAL-VLA는 장면 전체가 아니라 지금 subtask에 필요한 geometry와 future dynamics만 VLA에 가르칩니다.
9월 21일 업데이트된 **FOCAL-VLA**는 VLA의 precise·long-horizon manipulation에서 부족한 spatial/temporal understanding을 두 종류의 teacher representation으로 보완합니다.

현재 공간 구조는 **VGGT의 geometry latent**를 그대로 장면 전체에 맞추는 대신, 현재 subtask와 관련된 image region에만 alignment합니다. 미래 변화는 **Track4World**가 current/future demonstration frame에서 만든 feature를 이용해 interaction의 향후 3D dynamics를 implicit하게 학습합니다.

중요한 점은 VGGT와 Track4World가 **training supervision으로만 사용되고 inference 때는 실행되지 않는다**는 것입니다. 즉 3D geometry와 future interaction 정보를 policy representation에 distill하면서 deployment-time teacher overhead는 남기지 않는 구조입니다.

이 접근은 SAVLA와 문제를 푸는 축이 다릅니다. SAVLA가 예상 가능한 geometric transformation을 inductive bias로 넣는다면, FOCAL-VLA는 **현재 interaction에 필요한 geometry와 dynamics를 골라 representation에 압축**합니다.

manipulation 관점에서는 둘을 같이 볼 만합니다. VLA의 generalization을 단순히 더 큰 backbone이나 더 많은 demonstration 문제로만 보지 않고, **어떤 geometric structure를 보존하고 어떤 future physical state를 예측해야 하는가**로 문제를 더 세분화하고 있기 때문입니다.

논문은 simulation benchmark와 real-world manipulation에서 baseline을 앞섰다고 보고하지만, 현재 arXiv abstract만으로는 모든 실험 조건과 generalization 범위를 판단하기 어렵습니다. 수치 자체보다 subtask-focused geometry distillation과 implicit world modeling이라는 설계 선택을 우선해서 볼 가치가 있습니다.

## Sources
- [arXiv — SAVLA: Symmetry-Aware Vision-Language-Action Models for Robotic Manipulation](https://arxiv.org/abs/2609.16641)
- [arXiv — FOCAL-VLA: Subtask-Guided Geometry Distillation and Implicit World Modeling for Vision-Language-Action Models](https://arxiv.org/abs/2609.21228)
- [FOCAL-VLA Project Page](https://zhiyuan-gao.github.io/FOCAL-VLA/)
