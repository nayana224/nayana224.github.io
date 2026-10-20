---
layout: feed_note
title: "SCULPT-VLA는 행동을 예측하기 전에 조작 상태를 구조화한다"
date: 2026-09-20 19:00:00 +0900
channel: research-papers
channel_label: "Research Papers"
summary: "SCULPT-VLA는 작업 진행·장면 변화·공간 위치를 별도 latent factor로 학습한 뒤 action 예측에 연결하고, 4개 실제 로봇 과제의 분포 이동에서 π₀.₅보다 높은 평균 성공률을 보고했다."
---

VLA가 같은 장면을 보더라도, 조작 단계가 바뀌면 다음 행동에 필요한 정보도 달라진다. 컵을 옮길 때는 운반이 중요하지만, 쌓는 순간에는 림의 정렬과 그리퍼 해제가 중요하다. 9월 20일 공개된 **SCULPT-VLA**는 이 변화를 하나의 덩어리 표현에 맡기는 대신, action을 조건화하는 내부 상태를 세 가지로 나눠 학습한다.

- **Task progression:** 현재 어떤 subtask 단계인지
- **Scene dynamics:** 상호작용으로 장면이 어떻게 변했는지
- **Spatial grounding:** 목표 물체와 로봇 사이의 기하 관계

핵심 설계는 세 factor를 한 번에 action loss와 함께 학습하지 않는 **3단계 action grounding**이다. 먼저 고정된 teacher representation으로 각 factor의 역할을 만들고, 두 번째 단계에서는 vision·language를 action head에 직접 보여주지 않고 factor들의 조합으로 이산 action을 예측한다. 마지막에는 연속 action 학습을 위해 시각 입력을 다시 열어 정밀 제어를 다듬는다. 배포 시에는 teacher encoder나 이산 action autoregression을 사용하지 않는다.

### 결과: 고정 backbone 비교와 실제 로봇 분포 이동

저자들이 같은 Qwen3-VL backbone과 평가 파이프라인으로 맞춘 비교에서 SCULPT-VLA는 LIBERO 평균 **98.5%**, SimplerEnv-WidowX **83.5%**, RoboTwin 2.0 Full **92.2%**의 성공률을 보고했다. SimplerEnv의 Stack 과제에서는 75.3%로, 같은 실험군의 Qwen3-VL-GR00T 18.8%보다 높았다.

실제 로봇 네 과제의 시험한 분포 이동 조건에서는 평균 성공률이 **58.1%**였고, 논문이 비교한 π₀.₅는 **45.6%**였다. 이 실제 결과는 테스트한 네 과제와 분포 이동에 대한 값이다. 작업장 전반의 강건성이나 모든 embodiment에서의 우위를 뜻하지 않는다.

이 연구의 질문은 “중간 표현을 추가하면 좋은가?”보다 구체적이다. **action 학습이 task 단계·상호작용 변화·공간 관계를 실제로 사용하도록 학습 경로를 설계할 수 있는가?** 논문은 factor별 개입 실험도 제시해, 구조화된 상태가 최종 정책에 계속 기여하는지 살핀다. 다만 높은 LIBERO 점수는 포화에 가까우므로, 이 설계의 차이를 읽을 때는 분포 이동·장기 과제와 실제 로봇 결과를 함께 보는 편이 낫다.

## 무엇을 분리했는지 확인하는 ablation

SCULPT-VLA의 주장은 세 latent factor가 이름만 붙은 보조 feature가 아니라 action 학습에 실제로 쓰인다는 것이다. 따라서 전체 성공률보다 task progression, scene dynamics, spatial grounding을 하나씩 제거했을 때 어느 과제·분포 이동에서 손실이 커지는지가 설계 근거를 가르는 결과다.

재현을 검토한다면 고정 backbone 비교와 별도로 teacher 표현의 생성 비용, factor별 제거 실험, 학습 시점과 배포 시점의 입력 차이를 확인해야 한다. 특히 teacher가 추론 때 빠진다는 점은 배포 단순화의 장점이지만, teacher 표현 오류가 학습 데이터에 남는 문제까지 없애지는 않는다.

## Sources
- [SCULPT-VLA 논문과 전체 평가 표](https://arxiv.org/abs/2609.23275)
- [SCULPT-VLA 논문 HTML](https://arxiv.org/html/2609.23275v1)
