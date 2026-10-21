---
layout: feed_note
title: "촉각 사전학습부터 빠른 action까지, 새 VLA 연구 세 편"
date: 2026-10-21 14:50:00 +0900
channel: research-papers
channel_label: "Research Papers"
summary: "Spark-0는 촉각을 대규모 사전학습 신호로, DSP는 사람의 짧은 놀이 시연을 자율 데이터 수집의 출발점으로 사용한다. FastVLA는 작업·시간별 비전 토큰을 줄여 추론을 가볍게 한다. 각 결과는 논문별 제한된 벤치마크와 로봇 조건 안에서 읽어야 한다."
---

최근 공개된 세 연구는 로봇 정책의 서로 다른 병목을 겨냥한다. Spark-0와 Dexterity from Supervised Play(DSP)는 접촉이 중요한 손 조작을 위한 데이터와 학습 루프를 다루고, FastVLA는 매 제어 단계의 시각 토큰 계산량을 줄인다. 성능 수치와 평가 조건이 서로 다르므로 하나의 순위처럼 비교할 수는 없다.

## Spark-0: 촉각은 입력이자 시각 표현을 가르치는 신호다

Spark-0는 시각·촉각·언어를 함께 쓰는 dexterous manipulation 정책이다. 연구진은 사람 손에 촉각 장갑을 사용해 수집한 1,000시간 분량의 HumanTouch 데이터를 구축하고, 촉각에서 얻은 접촉 지도로 시각 토큰을 사전학습 중 감독한다. 실제 추론 때 이 보조 목적은 제거되지만, 별도의 촉각 경로는 힘의 변화와 손가락 상태를 action expert에 전달할 수 있다.

논문이 제시한 비교에서 같은 데이터와 계산량을 사용하되 HumanTouch의 촉각 정보를 버린 시각 전용 사전학습과 비교하면, 촉각 감독을 유지한 Spark-0의 시각 전용 Ego Humanoid 성공률은 52.5%에서 71.7%로 높아졌다. 촉각 입력도 사용하는 SparkArena-Real에서는 44%에서 52%로 증가했다고 보고한다. 두 수치는 서로 다른 평가 트랙이므로 직접 비교할 수 없다.

이 결과는 촉각이 실행 때 들어가는 센서 입력뿐 아니라, 시각 표현이 접촉을 학습하도록 돕는 사전학습 신호가 될 수 있음을 시사한다. 다만 이는 저자들이 구성한 벤치마크와 단일 dexterous 로봇 설정의 결과다. 다른 손·촉각 센서, 물체, 실제 작업에서 같은 개선이 재현되는지는 별도로 확인해야 한다.

## DSP: 짧은 사람 놀이로 시작해 로봇이 경험을 모은다

Dexterity from Supervised Play는 사람이 몇 분 동안 자유롭게 물체를 다루는 장면으로 행동 복제 기반의 play policy를 학습한 뒤, 로봇이 이를 사용해 더 긴 상호작용 데이터를 자율 수집하는 구조다. 수집된 경험으로 world model을 학습하고, 추론 때 play policy가 제안한 행동 시퀀스를 모델 기반 계획(MPC)에서 평가한다. 연구진은 학습된 world model 안에서 자기 대국을 통해 goal-conditioned 폐루프 정책을 증류하는 방법도 제안한다.

시뮬레이션과 실제 환경에서 밀기 조작 및 다지 손의 물체 방향 바꾸기를 평가했다. 실제 실험에서 DSP는 hindsight behavior cloning보다 성공률이 69.6% 높았고, 강화학습과 비슷한 성공률을 상호작용 데이터 490분의 1 수준으로 달성했다고 논문은 보고한다.

핵심은 task별 시연을 대량으로 모으는 대신, 짧은 놀이 경험을 탐색과 계획의 기반으로 쓴다는 점이다. 그러나 사람의 초기 놀이 입력이 전혀 없는 것은 아니며, 실험도 두 종류의 조작 과제에 한정된다. 따라서 임의의 손 조작 과제에서 시연이 불필요하다고 일반화하기보다, 초기 시연 이후 자율 수집이 가능한 조건과 비용을 살펴볼 연구로 보는 편이 정확하다.

## FastVLA: 중요도가 높은 시각 토큰에 계산을 배분한다

FastVLA는 학습을 다시 하지 않고 VLA의 시각 토큰을 작업과 시간 단계에 맞춰 줄이는 방법이다. 일반적인 시각 saliency 대신 언어 지시와 시각 토큰의 관계를 사용해 중요도를 추정하고, 중요도 분포에 따라 각 단계의 압축률을 조정한다. 즉 고정된 토큰 수를 매번 남기는 대신, 현재 동작에서 정보가 특정 영역에 집중되는 정도를 반영한다.

OpenVLA, OpenVLA-OFT, CogACT를 LIBERO와 SIMPLER에서 평가했을 때, 논문은 시뮬레이션에서 언어 모델 본체의 FLOPs를 35–59%, action latency를 9–32% 줄이면서 비슷한 성공률을 유지했다고 보고한다. 실제 Franka Research 3에서는 성공률이 비슷한 조건에서 종단 간 지연을 20% 줄였다고 설명한다. 이는 해당 모델·벤치마크·로봇 실험에서의 결과이며 다른 관측 파이프라인이나 하드웨어에도 그대로 적용된다는 뜻은 아니다.

이 논문은 10월 19일 글의 **Fast-VLA: You Only Think Once for Robot Manipulation**과 제목이 비슷하지만 다른 연구다. 10월 19일의 Fast-VLA는 작업 기억(task memory) 설계이고, 여기서 다루는 **FastVLA**는 시각 토큰 압축으로 추론 효율을 높이는 연구다.

## 데이터, 반응성, 계산량을 따로 측정하기

Spark-0와 DSP는 접촉 조작 경험을 어떻게 얻고 표현할지 다루고, FastVLA는 이미 학습된 정책의 추론 비용을 줄이는 데 초점을 둔다. 실제 적용을 비교할 때 Spark-0에는 센서·손 구성별 이득과 촉각 손실에 대한 강건성, DSP에는 사람 초기 입력과 자율 수집 데이터의 비용·실패율, FastVLA에는 성공률을 유지한 상태의 실제 제어주기·지연 분포를 측정해야 한다. 각 논문의 자체 벤치마크 수치만으로 일반적인 실기 성능이나 안전성을 결론내릴 수는 없다.

## Sources
- [arXiv — Spark-0: Scaling Spatially Aligned Tactile Pretraining for Robot Dexterous Manipulation](https://arxiv.org/abs/2610.22342)
- [Spark-0 — project page](https://xsparkai.com/Spark-0/)
- [arXiv — Dexterity from Supervised Play](https://arxiv.org/abs/2610.22340)
- [DSP — project page](https://play-policy.github.io/)
- [arXiv — FastVLA: Task-Conditioned and Temporally Adaptive Visual Token Compression](https://arxiv.org/abs/2610.22146)
- [FastVLA — code](https://github.com/jiuyixu25/FastVLA)
