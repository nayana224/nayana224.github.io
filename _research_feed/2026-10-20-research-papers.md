---
layout: feed_note
title: "VLA 학습 샘플의 절반을 미래 시각 예측에 써도 될까?"
date: 2026-10-20 13:00:00 +0900
channel: research-papers
channel_label: "Research Papers"
summary: "샘플 단위 router로 action prediction과 latent-action·future-vision 목표를 나눠 학습한 연구는, 적절한 보조 목표가 같은 샘플 예산의 action-only 학습을 앞설 수 있다고 보고한다."
---

VLA는 로봇이 실행할 행동을 예측하도록 학습하는 것이 당연해 보인다. 하지만 action prediction에 쓴 샘플은 latent-action이나 future-vision을 학습하는 데 사용할 수 없다. 10월 15일 공개된 이 연구는 **고정된 학습 샘플 예산에서 어떤 목표에 샘플을 배정할지**를 비교한다.

방법은 sample-level router가 각 학습 샘플을 action prediction 또는 보조 목표 하나에 배정한다. 미래 시각 목표는 DINOv3, V-JEPA 2, Wan2.2 표현으로 구성하고, LIBERO·CALVIN·실제 로봇 네 과제에서 평가했다. 추론 시에는 미래 관측을 입력하지 않고 행동만 출력한다.

저자들은 LIBERO에서 action-only 기준선의 평균 성공률 96.50%에 비해, 학습 샘플 절반만 action prediction에 배정하고 나머지를 Wan2.2 future-vision에 쓴 설정이 98.15%를 기록했다고 보고한다. 이 비교는 **샘플 노출 수를 맞춘 결과**다. 계산량(FLOPs)이나 벽시계 학습 시간이 같다는 뜻은 아니다. 또한 보조 목표는 training-time supervision이며, 미래 영상을 실행 중에 예측한다는 주장은 아니다.

로봇 정책의 학습 목표를 설계할 때 action loss 비중만이 아니라, 어떤 보조 target이 어떤 task·embodiment에서 이득을 주는지와 추가 비용을 분리해 비교할 필요가 있다.

## Sources
- [논문 원문과 실험 결과](https://arxiv.org/abs/2610.21915)
- [논문 HTML, training-budget 정의와 표](https://arxiv.org/html/2610.21915v1)
