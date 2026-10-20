---
layout: feed_note
title: "VLA action chunk를 얼마나 실행할지, 미래 상태로 먼저 검증한다"
date: 2026-10-15 19:00:00 +0900
channel: research-papers
channel_label: "Research Papers"
summary: "PAV는 VLA가 제안한 action prefix의 성공적 후속 가능성을 내부 task 표현으로 점수화해, 재관측 시점과 policy query 수를 함께 조절한다."
---

VLA가 action chunk를 길게 실행하면 policy 호출은 줄지만, 중간에 물체가 밀리거나 파지를 놓쳐도 다시 관측할 기회를 잃는다. 짧게 실행하면 반응성은 좋아지지만 모델을 더 자주 호출해야 한다. 10월 15일 공개된 **Policy-Aligned Predictive Verifier(PAV)**는 action을 새로 생성하는 대신, 이미 제안된 chunk 중 **어디까지 실행해도 성공적인 후속 행동이 가능할지**를 예측해 실행 길이를 고른다.

PAV는 각 action prefix가 만든 미래를 VLA의 task-conditioned latent representation에서 예측한다. verifier는 그 상태가 이후 성공으로 이어질 가능성을 점수화하고, 점수가 기준 아래로 떨어지기 전까지의 prefix만 실행한 뒤 새 관측으로 policy를 다시 호출한다. 학습에는 성공/실패 rollout의 최종 결과만 쓰는데, 실패 trajectory 안에도 유효한 초반 구간이 있을 수 있어 local validity를 직접 실패 라벨로 덮지 않도록 localization prior를 둔다.

### 시뮬레이션: 성공률과 호출 횟수의 절충

π₀.₅의 LIBERO action chunk 길이를 50으로 둔 실험에서, 고정 5-step 실행은 평균 성공률 **87.15%**, episode당 평균 VLA query **38.1회**였다. PAV는 **94.65%**, **14.0회**를 기록했다. 즉 더 적게 재호출하면서 성공률도 높았다고 저자들은 보고한다. π₀와 π₀.₅의 여러 chunk 설정에서도 같은 방식으로 비교했으며, RoboTwin 2.0의 50개 과제에서는 PAV가 58.64% 성공과 58.5회 query를 기록해 가장 나은 고정 horizon의 55.76%, 54.5회와 비슷한 호출 비용에서 더 높은 성공률을 보였다.

### 실제 로봇 결과

7-DoF Franka Panda의 tray에 cube 놓기, cube 쌓기, 버튼 누르기 세 과제에서 각 30회 평가했다. PAV는 평균 성공률 **74.4%**와 episode당 평균 replanning **12.87회**를 기록했다. 가장 강한 고정 horizon baseline은 성공률 **41.1%**였고, 30-step 고정 실행은 비슷한 11.97회 replanning에서 40.0%였다. 이 비교는 해당 세 과제와 저자들이 fine-tune한 π₀.₅ 설정에 대한 결과다.

Verifier의 GPU 계산 비용은 action generation 시간의 **0.45–1.24%**였지만, 이는 GPU compute 측정이지 센서부터 actuator까지의 end-to-end control latency가 아니다. 또한 실제 평가는 세 과제에 한정되어 있다. 따라서 PAV를 safety guarantee로 해석하기보다, 정책의 제안을 얼마나 실행한 뒤 다시 볼지 정하는 **adaptive replanning 방법**으로 보는 것이 정확하다.

이 연구는 미래 예측을 world model의 action generator로 쓰지 않고, 이미 만들어진 행동의 **실행 가능 길이를 판정하는 verifier**로 쓴다. action chunking을 평가할 때 평균 query 수만 비교하지 말고, 성공률·재관측 비용·실패 시 되돌릴 수 있는지까지 함께 봐야 한다.

## Sources
- [PAV 논문과 전체 비교 결과](https://arxiv.org/abs/2610.21434)
- [PAV 논문 HTML — 방법·ablation·실제 로봇 결과](https://arxiv.org/html/2610.21434v1)
