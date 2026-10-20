---
layout: feed_note
title: "VLA의 성공 verifier는 모든 순간을 똑같이 학습할 필요가 없다"
date: 2026-10-04 19:00:00 +0900
channel: research-papers
channel_label: Research Papers
summary: "DiVeR는 행동 후보의 차이가 큰 decision-critical state에 verifier 학습을 집중한다. LIBERO·RoboCasa와 Franka 평가에서 성공률 개선을 보고했으며, 후보 sampling 비용은 별도로 고려해야 한다."
---

VLA가 한 시점에서 낼 수 있는 행동 후보가 거의 비슷하다면, 그 상태의 성공·실패 라벨은 후보 중 무엇을 고를지 가르치는 데 큰 도움을 주지 않을 수 있다. 반대로 파지 방향처럼 후보에 따라 이후 결과가 크게 달라지는 순간은 더 중요하다. **DiVeR**는 verifier를 학습할 때 이 차이를 반영한다.

기존 verifier는 rollout의 여러 상태를 비슷한 비중으로 다루는 경우가 많다. DiVeR는 같은 상태에서 sampling한 action representation들의 분산을 이용해 **선택이 결과에 큰 영향을 줄 decision-critical state**를 추정하고, 그런 상태에 verifier 학습 가중치를 더 둔다. 각 단계에 사람이 따로 중요도 label을 붙이거나, 환경 상호작용을 추가하지 않는 것이 논문의 설계다.

추론에서는 VLA가 여러 action 후보를 만들고 verifier가 성공 가능성이 높은 후보를 선택한다. 저자들은 LIBERO, RoboCasa, Franka Research 3 실험에서 이 방식이 task success를 개선했고 verifier inference overhead는 작았다고 보고한다. 공개 초록에는 세부 과제별 수치가 제시되지 않으므로, 여기서는 개선 폭을 임의로 수치화하지 않는다.

이 방법의 핵심 기여는 단순히 후보를 더 많이 생성하는 데 있지 않고, **학습 데이터 안에서 후보 선택이 중요한 시점에 verifier의 학습을 집중**하는 데 있다. 로봇 조작에서는 모든 시점의 작은 궤적 차이보다 접촉 직전, 파지 형성, 물체 놓기처럼 결과를 갈라놓는 결정 지점이 특히 중요할 수 있다.

다만 후보를 여러 개 생성하는 test-time scaling은 그 후보 생성 비용을 동반한다. verifier 계산량이 작더라도 전체 system의 VLA 호출 수, 지연, 메모리는 별도로 재야 한다. 또한 평균 성공률만으로 verifier가 어떤 결정 지점에서 도움이 됐는지 알기 어려우므로, 후보 수에 따른 성공률·latency 곡선과 실패 유형별 분석이 함께 필요하다.

## Sources
- [DiVeR 논문 원문과 실험 범위](https://arxiv.org/abs/2610.04933)
- [DiVeR 논문 HTML](https://arxiv.org/html/2610.04933v1)
