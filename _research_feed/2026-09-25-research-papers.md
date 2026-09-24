---
layout: feed_note
title: "VLA를 더 견고하게 만드는 두 방법: camera viewpoint와 selective demonstration"
date: 2026-09-25 03:18:00 +0900
channel: research-papers
channel_label: Research Papers
summary: "InfiNoVA는 3D Gaussian 기반 novel-view augmentation으로 unseen camera viewpoint robustness를 높이고, TANDEM은 TAMP와 selective teleoperation을 결합해 long-horizon VLA demonstration 수집 비용을 줄인다."
---

## 카메라를 옮겨도 버티는 VLA를, 새 demonstration 없이 만든다

**InfiNoVA는 synchronized multi-camera demonstration을 time-varying 3D Gaussian scene으로 재구성한 뒤, 새로운 camera pose에서 관측 영상을 렌더링해 VLA training view를 늘린다.** 새 view를 만들면서도 원래 trajectory의 state-action correspondence를 유지한다.

VLA는 training 때 본 camera viewpoint에 강하게 의존할 수 있다. 실제 robot deployment에서 camera 위치가 달라지면 observation distribution도 바뀐다. InfiNoVA는 policy architecture를 바꾸는 대신 **training data의 viewpoint coverage를 geometry-grounded augmentation으로 넓힌다.**

저자 보고 기준 네 real-world manipulation task에서 unseen randomized viewpoint 평균 success는 VISTA 기반 augmentation 및 augmentation 없는 policy보다 **5.4× 높았고**, 실제 다섯 camera view를 모두 training에 사용한 경우보다도 **1.7× 높았다**.

perception robustness를 더 큰 policy나 별도 adaptation module로만 해결하지 않는다는 점이 흥미롭다. camera placement가 고정되지 않는 manipulation system이라면 더 많은 physical demonstration과 더 강한 policy 사이에 **3D-consistent data augmentation**이라는 선택지가 생긴다.

다만 평가는 네 real-world task에 한정되어 있다. 3D reconstruction이 어려운 reflective·transparent·severely occluded scene이나 deformable/entangled object에서도 같은 robustness가 유지되는지는 별도 검증이 필요하다.

## 사람이 전체 task를 시연하지 않고, planner가 막힐 때만 개입한다

**TANDEM은 long-horizon demonstration 수집을 planner가 할 수 있는 구간과 사람이 필요한 구간으로 나눈다.** TAMP(Task and Motion Planning)가 가능한 단계는 자동으로 수행하고, planning domain에 없는 단계에서만 human teleoperator를 on-demand capability처럼 호출한다.

human intervention point를 task마다 미리 hard-code하지 않는다. pretrained vision-language model을 이용해 missing predicate와 사람이 실행할 magic operator를 planning domain에 추가하고, human stage가 끝나면 scene을 다시 perception해 intended effect가 성립했는지 확인한 뒤 autonomous planning을 이어간다.

저자 실험의 대표 long-horizon task에서는 같은 human intervention time으로 full-task teleoperation 대비 **2.9× 많은 demonstrations**를 수집했다. pretrained **π₀.₅-DROID**를 task당 20개의 TANDEM demonstration으로 fine-tune했을 때 다섯 long-horizon task의 평균 success는 **0% → 60%**로 증가했다.

robot learning 관점에서는 사람이 모든 trajectory를 처음부터 끝까지 제공하는 대신, **autonomy가 실패하는 boundary에서만 demonstration을 요청하는 방식**으로 볼 수 있다. deterministic primitive/planner와 learned VLA를 함께 쓰는 system에서는 어디까지 automation하고 어디서 human data를 요청할 것인가를 data-collection 단계부터 설계할 수 있다는 점이 중요하다.

다만 논문은 현재 under review이며 평가는 다섯 long-horizon manipulation task에 한정된다. planner의 domain coverage와 perception error가 달라질 때 human-efficiency gain이 얼마나 유지되는지는 더 넓은 평가가 필요하다.

## Sources
- [arXiv — InfiNoVA: Infinite Novel View Augmentation for Viewpoint Invariant Robot Policies](https://arxiv.org/abs/2609.27734)
- [arXiv — TANDEM: Task and Motion Planning with As-Needed Demonstrations for Efficient Vision-Language-Action Model Fine-tuning](https://arxiv.org/abs/2609.28314)
