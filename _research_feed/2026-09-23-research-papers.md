---
layout: feed_note
title: "Tactile residual부터 visual force grounding까지, VLA가 contact를 다루는 법"
date: 2026-09-23 17:40:00 +0900
channel: research-papers
channel_label: Research Papers
summary: "VT-Bridge는 tactile residual feedback으로 pretrained VLA를 보정하고, VisForce는 fingertip 위치에 force를 시각적으로 grounding한다. rMuscle은 반복 robot execution의 내부 유사성을 cache해 VLA inference를 가속한다."
---

## 1/ VT-Bridge: pretrained VLA 위에 tactile residual correction을 얹는다

**VT-Bridge는 π₀, π₀.₅, SmolVLA 같은 pretrained VLA의 backbone architecture를 바꾸지 않고, 0.98M-parameter residual adapter로 tactile feedback을 action에 반영한다.** 논문에서 task당 필요한 vision-tactile demonstration은 최대 50개였고, 네 가지 contact-rich manipulation task에서 task-level VLA fine-tuning만 사용했을 때 평균 completion rate 11.7%가 VT-Bridge 적용 후 **62.9%**로 올라갔다.

핵심은 tactile signal을 VLA 자체에 대규모로 다시 학습시키는 대신, pretrained policy가 낸 action을 **robot execution frequency에서 residual하게 보정**한다는 점이다. Foundation VLA를 semantic·coarse action prior로 유지하면서 접촉 이후 필요한 correction을 별도 feedback layer가 담당한다.

다만 62.9%는 저자들이 선택한 세 backbone과 네 task에서 얻은 평균이며 모든 tactile manipulation으로 일반화할 수 있는 수치는 아니다. 그럼에도 **pretrained generalist policy + 빠른 feedback correction**이라는 분리는 closed-loop manipulation에서 직접 비교할 만한 architecture pattern이다.

## 2/ VisForce: force를 숫자로만 주지 않고 fingertip 위치에 시각적으로 grounding한다

**VisForce는 dexterous manipulation에서 current force와 desired force를 해당 fingertip 위치의 visual cue로 렌더링하고, 이를 wrist image와 goal image에 직접 grounding한다.** 별도의 force vector를 policy에 넣는 대신 `어디에 얼마만큼의 힘이 걸리고, 어디에 어느 정도의 힘이 필요한가`를 visual representation 안에서 정렬한 뒤 goal-conditioned cross-attention으로 force-aware action을 생성한다.

저자들은 UR10 + RH56F1 dexterous hand 실험에서 desired force가 커질수록 grip force가 일관되게 증가하는 것을 확인했다. Egg와 toothpaste tube의 grasp-and-lift는 각각 **70%, 80%**, multi-stage task의 최종 성공률은 cup insertion/bottle pouring **70%**, tong-assisted bread transfer **55%**, slip-modulated peg-in-hole **40%**였다.

이 접근에서 흥미로운 지점은 force sensing 자체보다 **force와 visual location 사이의 correspondence를 representation 문제로 다룬다**는 것이다. 특히 bread처럼 변형되기 쉽거나 grasp force가 중요한 물체에서는 `현재 접촉 상태 → 목표 접촉 상태 → action correction`을 어떤 representation으로 연결할지가 핵심인데, VisForce는 이를 visual grounding으로 푼 사례다.

다만 실험은 단일 UR10/dexterous-hand setup과 제한된 task에 대한 결과다. 다양한 물체·gripper·camera configuration에서도 fingertip-aligned cue가 유지되는지, 그리고 force cue rendering이 실제 sensor noise와 occlusion에 얼마나 강한지는 추가 검증이 필요하다.

## 3/ rMuscle: 반복되는 robot execution을 VLA의 'muscle memory'로 cache한다

**rMuscle은 VLA inference에서 반복 robot execution 사이의 유사성을 이용해 visual-token output과 neuron activation pattern을 재사용하는 dual-phase cache를 제안한다.** Context Cache는 visual-token computation을 줄이고, Action Cache는 denoising 과정에서 반복되는 activation pattern을 이용해 weight access를 줄인다.

중요한 점은 단순 KV cache를 더 크게 두는 접근이 아니라 **robot workload 자체의 반복성**을 inference optimization 대상으로 삼았다는 것이다. 저자들은 LIBERO, RoboTwin과 physical manipulation task에서 RTX 4090과 Jetson Thor를 평가했고, 기존 success rate를 유지하면서 **1.29–1.42× speedup**을 보고한다. Cache overhead를 줄이기 위해 online cache recomputation, sliding-window retrieval, consecutive denoising step 사이의 mask sharing도 사용한다.

이 결과는 VLA deployment에서 model compression만 볼 필요가 없다는 신호다. 공장·랩 자동화처럼 비슷한 scene과 task가 반복되는 환경이라면 `현재 observation → 매번 전체 VLA 계산` 대신 **이전 execution의 내부 state를 어디까지 안전하게 재사용할 수 있는가**가 별도의 system-design 축이 된다. 특히 edge robot에서는 model latency뿐 아니라 cache memory footprint와 stale-state failure를 함께 봐야 한다.

수치는 저자들이 평가한 model·hardware·task 조합에 한정된다. 반복성이 낮은 open-world manipulation에서도 같은 cache hit와 speedup이 유지되는지는 추가 검증이 필요하다.

### Sources

- [arXiv — VT-Bridge: Bridging Pretrained Foundation VLAs to VTLAs via Lightweight Residual Adaptation](https://arxiv.org/abs/2609.22606)
- [VT-Bridge Project Page](https://hoxnocha.github.io/vt-bridge-web/)
- [arXiv — VisForce: Visual Grounding of Current and Desired Forces for Goal-Conditioned Dexterous Manipulation](https://arxiv.org/abs/2609.25785)
- [arXiv — rMuscle: Robotic Muscle Memory for Efficient Vision-Language-Action Model Inference](https://arxiv.org/abs/2609.19104)
