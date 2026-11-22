---
layout: feed_note
title: "하나의 Video DiT 사전지식으로 역동역학과 순동역학을 동시에 초기화하는 O²LaF"
date: 2026-11-15 07:30:00 +0900
channel: research-papers
channel_label: "Research Papers"
summary: "2026년 11월 19일 공개된 O²LaF는 동일한 사전학습 Video DiT를 역동역학(IDM)과 순동역학(FDM) 모델의 공통 사전지식으로 재활용해, 라벨 없는 영상에서 전이 가능한 잠재 행동(latent action)을 학습하는 프레임워크다. 내비게이션과 로봇 매니퓰레이션에서 few-shot action probing SOTA와 이기종 간 zero-shot 전이를 달성했으나, 초록 및 도입부 발췌 기준 구체적인 정량 수치와 실물 로봇 폐루프 제어 지연시간 등은 본문 확인이 필요하다."
---

인터넷 규모의 방대한 비디오 데이터는 세상이 어떻게 변하는지는 보여주지만, 그 변화를 일으킨 구체적인 행동(action) 라벨은 거의 포함하고 있지 않다. 이러한 행동 라벨의 부재는 제어 가능한 월드 모델(World Model)과 임바디드 에이전트(Embodied Agent)를 대규모 영상으로 학습시킬 때 가장 큰 병목이 된다. 2026년 11월 19일 공개된 논문 *One Prior, Two Dynamics: Repurposing Video Diffusion Transformers for Self-Supervised Latent Action Learning*([arXiv:2611.26617v1](http://arxiv.org/abs/2611.26617v1))은 사전학습된 비디오 생성 모델 하나를 역동역학(IDM)과 순동역학(FDM) 모두의 출발점으로 삼아 이 문제를 정면으로 다룬다.

## 하나의 사전지식(One Prior)에서 분화한 두 개의 동역학

기존의 자기지도 잠재 행동(Latent Action) 학습 방식은 크게 네 가지 갈래로 나뉘었지만 각기 한계가 있었다. LAPA, Genie, AdaWorld처럼 역동역학(IDM)과 순동역학(FDM)을 처음부터(from scratch) 학습하거나, UniVLA·LAWM-in-the-Wild처럼 DINOv3·V-JEPA의 동결된 시각 특징(frozen visual features)에만 의존하거나, VideoWorld 2·CoLA-World처럼 Video DiT를 FDM에만 적용하고 IDM은 따로 두거나, Olaf-World처럼 외부 비디오 사전지식을 정렬 손실(alignment loss)로만 활용하는 식이다.

저자들이 제안한 **O²LaF**는 **"하나의 사전지식, 두 개의 동역학(One Prior, Two Dynamics)"**이라는 단순한 원칙을 따른다. 동일한 사전학습 Video DiT 가중치로 IDM과 FDM을 모두 초기화한 뒤, 각자의 역할에 맞게 구조를 변형하여 종단간(end-to-end)으로 학습시킨다. 논문 Figure 1에 제시된 전체 흐름은 다음과 같다.

- **입력 → 역동역학(IDM)**: 연속된 프레임 $(x_t, x_{t+1})$이 들어오면, 학습 가능한 행동 쿼리(learnable action queries)가 장착된 피드포워드 전이 인코더(feed-forward transition encoder)로 개조된 IDM이 시각적 변화로부터 콤팩트한 잠재 행동 $z_t \in \mathbb{R}^{32}$를 추출한다.
- **핵심 병목 → 순동역학(FDM)**: 정보 접근을 제어하는 콤팩트한 병목($z_t$)을 거쳐, 인과적(causal) 행동 조건부 비디오 생성기로 개조된 FDM이 현재 프레임 $x_t$와 잠재 행동 $z_t$를 받아 다음 프레임 $\hat{x}_{t+1}$을 예측한다.
- **출력(통합 잠재 행동 공간)**: 이 과정을 통해 1인칭 시점, 3인칭 시점, 게임 영상, 로봇 작업 영상 등 이질적인 도메인에서 추출된 행동들이 하나의 통합된 잠재 행동 공간($\mathbb{R}^{32}$)에 정렬된다.

## 내비게이션·로봇 매니퓰레이션 검증과 아직 확인이 필요한 지점

제공된 초록과 Figure 1 기준, O²LaF는 내비게이션과 로봇 매니퓰레이션 벤치마크 전반에서 검증되었다. 구체적으로 **few-shot action probing**에서 새로운 SOTA(State of the Art)를 기록했으며, 시각적 맥락(1인칭 ↔ 3인칭)과 임바디먼트(embodiment)를 넘나드는 **zero-shot action transfer**에서 기존 대비 더 강한 전이 성능을 보였다. Figure 1의 정성적 예시에서는 동일한 잠재 행동 $z$가 내비게이션과 로봇 장면 모두에서 '우회전(turn right)'을 구동하고, 인간 시연 영상에서 추출한 행동이 GR-1 휴머노이드 로봇의 뚜껑 열기(remove lid)로, 게임(*Hogwarts Legacy*) 속 동작이 윙슈트 비행(Wingsuit flying)으로 zero-shot 전이되는 모습을 보여준다. 또한 생성형 Video DiT 사전지식뿐만 아니라 **V-JEPA2** 같은 예측 표현(predictive representation) 사전지식으로 프레임워크를 확장했을 때도 경쟁력 있는 성능을 확인했다.

반면, 현재 공개된 초록과 도입부 발췌만으로는 판단하기 어려운 **검증의 한계(Caveat)**도 분명히 구분해야 한다.
- **구체적 정량 수치 미포함**: few-shot action probing SOTA 달성 및 경쟁력 있는 성능이라는 정성적 보고 외에, 구체적인 성공률, MSE/FVD 등의 수치나 비교 베이스라인별 격차는 본문 실험 섹션 확인이 필요하다.
- **기반 모델 스펙 및 연산 비용**: 초기화된 사전학습 Video DiT의 정확한 파라미터 규모, 학습에 소요된 컴퓨팅 자원, 그리고 실물 로봇 제어 루프에서 IDM/FDM의 추론 지연시간(latency)은 발췌된 범위에 명시되어 있지 않다.

## 로봇·월드 모델 엔지니어를 위한 실무 시사점

- **IDM과 FDM의 비대칭적 초기화 불균형 해소**: 기존처럼 FDM에만 대형 Video DiT를 쓰고 IDM은 가볍게 바닥부터 학습시키면, IDM이 시각적 변화에서 물리적 인과관계를 포착하는 데 한계가 생긴다. IDM 역시 동일한 비디오 사전지식에서 출발시키되 피드포워드 인코더로 경량화해 짝을 맞추는 설계는 월드 모델과 정책 학습 파이프라인 모두에 유효한 패턴이다.
- **저차원 병목($\mathbb{R}^{32}$)을 통한 도메인 불변(Domain-Invariant) 행동 표현**: 1인칭·3인칭 시점 차이나 인간-로봇(GR-1) 간 외형 차이가 크더라도, 정보 접근을 통제한 콤팩트한 잠재 공간으로 두 동역학을 공동 최적화하면 시점과 신체에 무관한 의미론적 행동(예: turn right, arm +x/+z)을 분리해낼 수 있다.
- **생성형 모델과 예측 표현(JEPA) 간의 아키텍처 호환성**: 이 논문은 Video DiT뿐 아니라 V-JEPA2 같은 비생성형 예측 모델에도 동일한 "One Prior, Two Dynamics" 원리가 통한다는 점을 시사한다. 픽셀 복원 비용이 부담스러운 실시간 로봇 제어 시스템에서는 V-JEPA2 기반 사전지식을 채택하는 변형을 우선 검토할 수 있다.
