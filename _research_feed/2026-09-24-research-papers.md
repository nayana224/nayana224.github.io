---
layout: feed_note
title: "Robot learning의 두 경로: agent가 데이터를 만들고, human correction은 constraint가 된다"
date: 2026-09-24 19:07:00 +0900
channel: research-papers
channel_label: Research Papers
summary: "EmbodiedSWE는 coding agent의 verified solution을 VLA supervision으로 확장하고, BEE는 human correction의 일관성을 action-dimension별 constraint로 바꿔 frozen VLA를 real-world RL로 개선한다."
---

## Coding agent가 robot task를 풀고, 그 해법을 VLA 데이터로 바꾼다

**EmbodiedSWE는 coding agent를 단순 robot planner가 아니라 `task solver → verified demonstration generator → VLA teacher`로 사용한다.** 새 EMBODIEDSWE-BENCH는 assembly, deformable object, liquid, cutting, loco-manipulation을 포함한 **6 suites·28 tasks·17 robot embodiments**를 제공하며, 일부 task는 약 **30분 horizon**까지 이어진다.

핵심은 coding agent가 simulator 안에서 자연어 목표를 받고 직접 solution code를 반복 작성한다는 점이다. task-specific macro primitive는 제공하지 않고 scene inspection과 IK 같은 generic controller를 이용하며, 결과는 hidden rubric으로 offline grading한다. 즉 high-level LLM이 미리 준비된 primitive 몇 개를 고르는 구조보다 한 단계 더 나아가, agent가 interaction을 통해 task-specific controller를 만들어 검증받는 setting이다.

하지만 agent solution 자체는 느리고 task-specific하다. EmbodiedSWE-Gen은 여기서 방향을 바꾼다. **한 번 검증된 solution을 scene·strategy·phase·dynamics·visual level에서 다양화해 robot trajectory dataset으로 확장**하고, 이를 VLA supervision으로 사용한다. 공개 project 결과에서 SmolVLA의 평균 success rate는 task당 demonstration을 **10개에서 400개로 늘릴 때 14% → 66%**로 상승했다. 동일한 1,000 demonstrations 비교에서도 agent-aided diversification은 held-out variation 평균 score를 **0.07 → 0.23**으로 높였다.

이 구조가 흥미로운 이유는 `LLM/coding agent`와 `VLA`의 역할을 경쟁 관계로 두지 않는다는 데 있다. 느리지만 reasoning과 tool use가 가능한 agent가 simulation에서 solution을 찾고 검증한 뒤, 그 결과를 빠른 learned policy의 training data로 넘긴다. **high-level agent의 deliberation을 real-time robot control loop에 그대로 넣지 않고 policy learning으로 distill하는 방식**으로 볼 수 있다.

다만 benchmark 결과를 곧바로 real-world autonomy 성능으로 해석하면 안 된다. 주된 agent evaluation과 data generation은 simulation에서 이뤄지며, coding-agent solve에는 상당한 iterative interaction과 시간이 필요하다. 프로젝트는 coding-agent-generated simulation demonstration만으로 fine-tune한 VLA의 real-robot long-horizon transfer 사례도 제시하지만, 이것만으로 광범위한 sim-to-real generalization이 검증됐다고 보기는 이르다.

## Human correction을 그대로 따라 하지 않고, `어디까지 믿을지` 학습한다

**BEE는 real-world VLA reinforcement learning에서 human correction을 정답 action으로 복제하지 않는다. 대신 correction이 action dimension별로 얼마나 일관적인지를 추정해 policy update의 constraint로 사용한다.** 세 real-world manipulation task와 LIBERO-Pro에서 저자 보고 평균 success rate는 **91.2%**, 비교한 RLT는 **57.5%**, DSRL은 **42.1%**였다.

출발점은 실제 correction이 균일하게 신뢰할 수 있는 supervision이 아니라는 관찰이다. 어떤 dimension에서는 사람이 반복해서 거의 같은 방향으로 고치지만, 다른 dimension에서는 correction이 크게 달라질 수 있다. BEE의 Correction Model은 frozen VLA가 제안한 action에 대해 사람이 어떻게 개입할지와 그 일관성을 예측한다. **일관성이 높은 dimension은 human correction 가까이에 policy를 묶고, 변동성이 큰 dimension은 constraint를 느슨하게 만들어 RL이 expert보다 더 나은 action을 탐색할 여지를 남긴다.**

이 점에서 intervention을 단순 DAgger-style demonstration accumulation으로 보는 것과 차이가 있다. 사람은 실패 직전의 precision-critical phase를 알려주는 안전장치이면서 동시에 `이 action component는 얼마나 강하게 고정해야 하는가`를 알려주는 signal이 된다. 저자 실험에서는 모든 real-world task에서 비교 방법보다 human intervention rate도 낮았다.

closed-loop manipulation 관점에서는 꽤 직접적인 아이디어다. 실패 후 다시 demonstration을 모아 전체 policy를 재학습하는 대신, **실행 중 발생하는 correction을 policy improvement의 구조화된 feedback으로 바꾸는 방법**이기 때문이다. 다만 현재 결과는 세 real-world task와 하나의 simulation benchmark에 한정되어 있어, 더 다양한 embodiment와 contact-rich/deformable task에서도 같은 intervention efficiency가 유지되는지는 추가 검증이 필요하다.

## VLA가 위험해지기 전에 checkpoint를 남기고 rollback한다

**SafeLoop는 VLA 자체를 다시 학습하지 않고, vision·proprioception 기반 risk predictor와 rollback controller를 바깥에 붙여 long-horizon manipulation의 실패를 줄인다.** predictor는 body collision과 object failure 각각에 대해 hazard probability와 time-to-hazard를 예측하고, controller는 위험도에 따라 `noop → record → rollback` 중 하나를 선택한다.

핵심은 실패를 감지한 뒤 멈추는 것이 아니라 **아직 안전할 때 waypoint를 checkpoint로 저장하고, hazard가 임박하면 그 지점으로 joint-space retreat한 뒤 base policy를 다시 query한다는 것**이다. learned policy가 매 순간 완벽한 action을 내도록 강제하기보다, 실행 중 잘못된 trajectory에서 빠져나와 다른 continuation을 시도할 수 있는 recovery layer를 둔다.

저자 실험은 **LIBERO 24 tasks × 16 seeds**와 **real-robot 3 tasks × 25 rollouts**에서 진행됐고, SafeLoop는 base-policy control rate와 task success를 유지하면서 hazard case를 약 **70% 감소**시켰다고 보고한다. collision뿐 아니라 object drop 같은 object-level failure까지 별도 risk로 예측한다.

closed-loop manipulation 관점에서는 policy architecture보다 **execution-time verification과 recovery**를 분리해 설계한다는 점이 중요하다. VLA를 교체하거나 fine-tune하지 않고 외부 wrapper로 붙일 수 있어, generalist policy 위에 task-independent safety/recovery layer를 추가하는 방향으로 볼 수 있다. 다만 real-robot 평가는 세 task에 한정되어 있고 rollback 가능한 safe waypoint가 존재한다는 전제가 있으므로, irreversible contact나 deformable/entangled object manipulation에서도 같은 효과가 유지되는지는 아직 검증이 필요하다.

## Sources
- [EmbodiedSWE — project page](https://embodiedswe.github.io/)
- [arXiv — EmbodiedSWE: Coding Agents for Long Horizon Dexterous Robotics](https://arxiv.org/abs/2609.27308)
- [arXiv — BEE: Intervention-Adaptive Real-World Reinforcement Learning with Vision-Language-Action Models](https://arxiv.org/abs/2609.27450)
- [arXiv — SafeLoop: Risk-Aware Rollback for Vision-Language-Action Manipulation](https://arxiv.org/abs/2609.26313)
- [GitHub — SafeLoop implementation](https://github.com/Loule0-0/SafeLoop/tree/release/safeloop)
