---
layout: feed_note
title: "VLA의 두 가지 기억: Task Memory와 Action Memory"
date: 2026-10-19 13:00:00 +0900
channel: research-papers
channel_label: "Research Papers"
summary: "Fast-VLA와 REKI는 각각 반복되는 VLM 추론과 행동 이력 손실을 줄이는 서로 다른 구조를 제안한다."
---

10월 15일 공개된 두 논문은 VLA가 **무엇을 기억해야 하는지**를 다른 관점에서 다룬다. 작업 목표는 상대적으로 오래 유지되지만, 현재 로봇 상태와 직전 행동은 계속 바뀐다.

## Fast-VLA: Task Memory를 한 번 만들고 반복 사용

기존 VLA는 새 action chunk마다 대형 VLM을 다시 실행하는 경우가 많다. Fast-VLA는 frozen 4B VLM을 에피소드 시작에 한 번 실행해 지시문과 초기 카메라 영상을 계층별 KV memory로 저장한다. 이후 작은 online actor가 최신 영상·관절 상태를 읽고 고정된 task memory를 조회해 다음 행동을 만든다.

저자들은 RoboTwin 2.0에서 동일 하드웨어의 세 비교 모델 대비 **평균 정책 추론 시간 10.9–17.1배 감소**를 보고했다. 이는 실제 로봇 작업 완료 시간의 단축률은 아니다.

## REKI: Action Expert에 최근 관측을 남긴다

REKI는 공개 데이터로 학습한 2.4B VLA로, flow-matching action expert에 32개 register token을 추가한다. 이전 프레임의 register key/value를 cache에 보존해, 매번 과거 영상을 VLM에 재입력하지 않고도 최근 상황을 참고한다.

저자들은 chunk 사이의 자세 진동이 **약 4배 덜 발생**했고, 기억으로 인한 chunk 예측 시간 증가가 **1% 미만**이라고 보고했다. 결과는 논문의 평가 환경에 한정된다. 공개 가중치는 비상업적 사용 조건을 확인해야 한다.

두 접근은 서로 대체재가 아니다. 하나는 큰 모델의 반복 호출을 줄이고, 다른 하나는 짧은 관측 이력의 손실을 줄인다. Closed-loop manipulation에서는 **latency와 행동 안정성을 분리해서 평가**할 필요가 있다.

## Sources
- [Fast-VLA 논문](https://arxiv.org/abs/2610.21389)
- [Fast-VLA 프로젝트 및 데모](https://garfield-kh.github.io/FastVLA/)
- [REKI 논문](https://arxiv.org/abs/2610.22178)
- [REKI 공식 코드 및 가중치](https://github.com/kyutai-labs/reki)
