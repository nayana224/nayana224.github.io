---
layout: feed_note
title: "VLA의 긴 Action Chunk, 전환 시점과 토큰 품질이 관건"
date: 2026-10-11 19:00:00 +0900
channel: research-papers
channel_label: "Research Papers"
summary: "RACE는 subskill 전환 시점을 예측하고, 별개의 ProAct 연구는 action token의 예측 가능성과 강건성을 학습한다."
---

## RACE: 언제 다음 조작 단계로 넘어갈까?

VLA가 긴 action chunk를 실행하면 모델 호출 사이의 대기 시간은 줄지만, 접촉·파지·이동처럼 조작 단계가 바뀌는 순간에는 예측 오류가 커질 수 있다. 10월 5일 공개된 **RACE**는 추가 one-step denoising으로 subskill 전환 타이밍을 예측해 다음 행동 생성에 반영한다.

저자들은 실제 로봇에서 **4배 긴 chunk**를 사용해 stop-and-go idle time을 약 **5배 줄였다**고 보고했다. 전체 작업 시간이 5배 빨라졌다는 뜻은 아니다. [공식 저장소](https://github.com/Seonghoon-Yu/RACE-VLA)에는 실제 로봇 비교 영상이 있지만, 코드 공개는 아직 예정 상태다.

## Action Tokenizer: 복원 정확도만 높으면 충분할까?

10월 6일 공개된 *Beyond Reconstruction*의 **ProAct**는 행동을 정확하게 복원하는 것뿐 아니라, 정책이 다음 토큰을 쉽게 예측하고 예상 밖의 토큰도 안정적인 행동으로 디코딩하도록 학습한다.

저자들은 Robomimic·LIBERO·RoboTwin에서 평균 성공률 **11.3%p** 향상을 보고했다. VLA와 실제 로봇 실험에서는 각각 평균 **21.8%p, 36.7%p** 개선을 보고했다. 이 수치는 논문의 평가 설정에 한정된다.

두 연구는 각각 **행동 전환 시점**과 **행동 표현의 강건성**을 다룬다. closed-loop manipulation에서 지연과 복구를 평가할 때 구분할 만한 문제다.

## 두 성능 수치의 분모를 확인하기

RACE의 약 5배 감소는 stop-and-go idle time에 대한 보고이며, task 완료 시간 전체의 5배 단축으로 바꿔 말할 수 없다. ProAct의 성공률 향상도 각 benchmark와 학습·평가 설정에 종속된다. 두 수치는 분모와 baseline을 확인해야 의미가 보존된다.

VLA deployment에서 chunk를 늘리는 실험은 idle time뿐 아니라 실패 후 재관측까지의 최대 시간, 접촉 이벤트 직후의 대응, jerk와 성공률을 함께 기록하는 편이 유용하다. tokenizer 비교는 재구성 오차 외에 closed-loop action 결과를 봐야 한다.

## Sources
- [RACE 논문 (2026-10-05)](https://arxiv.org/abs/2610.05719)
- [RACE 실제 로봇 시연](https://github.com/Seonghoon-Yu/RACE-VLA)
- [Action Tokenization 논문 (2026-10-06)](https://arxiv.org/abs/2610.09170)
