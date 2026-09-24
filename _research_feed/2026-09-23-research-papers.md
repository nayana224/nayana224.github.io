---
layout: feed_note
title: "VLA에 느린 brain과 빠른 reflex를 분리한다"
date: 2026-09-23 18:05:00 +0900
channel: research-papers
channel_label: Research Papers
summary: "VT-Bridge는 tactile residual feedback으로 pretrained VLA를 보정하고, VisForce는 force를 fingertip 위치에 visual grounding한다. Real-Time EXPO-FT는 느린 VLA proposal과 빠른 reactive edit policy를 분리해 dynamic manipulation의 latency 문제를 RL로 다룬다."
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

## 3/ Real-Time EXPO-FT: 느린 VLA는 제안하고, 빠른 policy가 마지막 순간에 고친다

**Real-Time EXPO-FT는 큰 pretrained VLA의 느린 action generation과 최신 observation에 반응하는 lightweight edit policy를 서로 다른 시간축으로 분리한다.** VLA는 asynchronous하게 action chunk 후보를 만들고, 실행 직전의 fast edit policy가 현재 state를 보고 후보를 수정한다. Q-function은 수정된 후보 중 실행할 action chunk를 선택한다.

이 구조가 겨냥하는 문제는 단순 inference speed가 아니라 **stale observation**이다. VLA가 observation을 보고 계산하는 동안 실제 robot과 object는 이미 움직였기 때문에, 계산이 끝났을 때 action이 과거 state에 대한 답이 될 수 있다. 저자들은 이 delay 자체를 RL fine-tuning 과정에 포함해 reactive correction을 학습한다.

Kinetix에서는 delayed/non-delayed method를 포함한 비교에서 10개 environment 모두 최고 성능을 기록했고, 네 가지 dynamic real-world task에서는 task당 online robot data를 최대 **10분**으로 제한한 상태에서 평균 policy performance가 **42% → 97%**로 향상됐다. 평가 task는 robot object passing, ball balancing, table-soccer kicking, dynamic object picking이며 online training 중 human correction은 사용하지 않았다.

이 결과가 흥미로운 이유는 큰 VLA를 무조건 더 빠르게 만드는 대신 **semantic·behavior prior를 담당하는 slow policy와 control-frequency correction을 담당하는 fast policy를 분리**했다는 점이다. Closed-loop manipulation에서 perception/model latency를 없앨 수 없다면, `느린 high-level prediction을 유지하면서 최신 observation으로 어디까지 residual correction할 것인가`라는 별도의 설계 축이 생긴다.

다만 결과는 저자들의 dynamic-task setup과 online RL 조건에 한정된다. Sparse reward를 안정적으로 정의하기 어려운 manipulation이나 long-horizon task에서도 10분 수준의 adaptation이 유지되는지는 별도 검증이 필요하다.

### Sources

- [arXiv — VT-Bridge: Bridging Pretrained Foundation VLAs to VTLAs via Lightweight Residual Adaptation](https://arxiv.org/abs/2609.22606)
- [VT-Bridge Project Page](https://hoxnocha.github.io/vt-bridge-web/)
- [arXiv — VisForce: Visual Grounding of Current and Desired Forces for Goal-Conditioned Dexterous Manipulation](https://arxiv.org/abs/2609.25785)
- [arXiv — Reinforcement Learning for Real-Time Vision-Language-Action Policies](https://arxiv.org/abs/2609.18207)
- [Real-Time EXPO-FT Project Page](https://pd-perry.github.io/real-time-expo-ft/)
