---
layout: feed_note
title: "로봇 조립에서 perception·primitive·impedance control을 결합한 NVIDIA 사례"
date: 2026-10-07 19:00:00 +0900
channel: ai-robotics
channel_label: "AI & Robotics"
summary: "NVIDIA가 GB300 테스트 트레이 조립에 로봇 학습과 모듈형 제어를 결합한 실제 사례를 공개했다."
---

## 학습 모델 하나보다 중요한 실행 파이프라인

NVIDIA의 Seattle Robotics Lab과 Isaac 엔지니어링 팀은 GB300 tester tray를 조립하는 로봇 시스템을 공개했다. Busbar 조립에는 **FoundationPose 기반 물체 인식 → waypoint planning → Lissajous-curve manipulation primitives → impedance controller**를 연결했다. NVIDIA는 이 모듈형 파이프라인에서 busbar 조립 성공률이 95%를 넘고 사이클 시간이 160초였다고 보고한다.

Multi-connector insertion은 다른 난제였다. 케이블 파지는 SAM3 segmentation을 사용했지만, 커넥터의 정밀 파지는 별도 pose-estimation 접근(DOPER)이 필요했다. 이는 high-level agent가 모든 동작을 직접 생성하기보다, 작업별로 검증된 perception·control primitive를 조합하는 설계가 유효할 수 있음을 보여준다. 보고된 수치는 해당 조립 공정에 한정된다.

## 소형 모델은 속도·비용 중심으로 경쟁

Anthropic은 같은 날 Claude Haiku 5.5를 발표했다. 회사에 따르면 Haiku 4.5보다 평균 실행 비용이 약 75% 낮으며, 분류·요약·subagent·빠른 browser use 같은 고빈도 작업을 겨냥한다. Robot agent에서도 모든 판단을 큰 모델에 맡기는 대신 빠른 경량 모델과 느린 planner를 분리하는 비용·latency 설계의 참고 사례다. 로봇 제어 성능을 직접 보증하는 발표는 아니다.

## 무엇을 재현해야 조립 성과를 비교할 수 있나

보고된 95% 이상은 busbar 조립 공정의 성공률이고 160초는 해당 pipeline의 cycle time이다. 이 값은 multi-connector insertion과 같지 않으며 전체 공장 처리량도 아니다. 반복 횟수, 부품 공차, 실패 후 재시도 여부가 함께 공개돼야 운영 성능을 판단할 수 있다.

Haiku 5.5의 비용·속도 발표는 별도 범용 모델의 주장이다. 조립 사례의 perception이나 impedance control을 Haiku가 수행했다는 근거는 없다. 로봇 시스템에서는 high-level planner를 경량화할 수 있는지와 저수준 제어가 실제 주기·안전 요구를 만족하는지를 각각 측정해야 한다.

## Sources
- [NVIDIA — The Machines that Make the Machines](https://developer.nvidia.com/blog/the-machines-that-make-the-machines/)
- [Anthropic — Claude Haiku 5.5](https://www.anthropic.com/claude-haiku-5-5)
