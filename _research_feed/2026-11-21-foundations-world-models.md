---
layout: feed_note
title: "[필수 기초 로드맵 ②] World Model & Physical AI: 머릿속에서 미래를 시뮬레이션하는 로봇 뇌 필수 논문 4선"
date: 2026-11-21 08:00:00 +0900
channel: foundations
channel_label: "Foundations · 필수 기초"
tags: ["World Model", "Sim & Systems"]
source_url: "https://arxiv.org/abs/2301.04104"
summary: "로봇이 실제로 물건을 떨어뜨려 보기 전에 '내가 이렇게 밀면 컵이 넘어지겠지?'라고 머릿속에서 물리 세계를 상상·예측하는 World Model 분야의 필수 기초 논문 4편(World Models, DreamerV3, UniSim, Cosmos/Genie)을 쉽게 풀어봅니다."
---

사람은 뜨거운 냄비를 맨손으로 잡아보지 않아도 *"지금 잡으면 손을 데겠구나"*, 컵 끝을 살짝 밀면 *"컵이 쏟아지겠구나"*라고 **머릿속에서 1초 뒤의 미래를 미리 재생(시뮬레이션)**해 봅니다.

로보틱스와 Physical AI에서 말하는 **월드 모델(World Model)**이 바로 이것입니다: **`[지금 상태 + 내가 할 행동] → [1초 뒤 세상이 어떻게 바뀔지 예측]`**하는 내부 물리 엔진입니다. 이 분야를 처음 잡을 때 꼭 읽어야 할 필수 논문 4편을 정리했습니다.

---

## 한눈에 보는 진화 계보

`① World Models (잠재 공간 꿈속에서 학습하기) → ② DreamerV3 (상상만으로 마인크래프트 다이아몬드 캐기) → ③ UniSim (행동 조건부 비디오 생성 시뮬레이터) → ④ NVIDIA Cosmos & World Action Models (피지컬 AI 전용 월드 파운데이션 모델)`

---

## 1. World Models (Ha & Schmidhuber, 2018)
- **원문:** [*World Models* (`arXiv:1803.10122`)](https://arxiv.org/abs/1803.10122)
- **해결한 문제 (왜 중요한가?):** 실제 환경(특히 실제 로봇)에서 수백만 번 부딪히며 시행착오를 겪는 것은 시간도 오래 걸리고 로봇이 망가집니다.
- **고등학생도 이해하는 핵심 컨셉:**
  - 인공지능을 **V(눈: 화면을 짧은 요약 벡터 $z$로 압축하는 VAE)** + **M(기억/상상: 현재 $z$와 행동 $a$를 보고 다음 순간의 $z'$를 예측하는 RNN)** + **C(제어기: 가장 좋은 행동을 고르는 작은 신경망)** 3조각으로 나눕니다.
  - 일단 M이 세상의 물리 법칙을 배우고 나면, 실제 게임을 켜지 않고 **M이 만들어내는 '꿈(Dream) 속 세상'에서만 수만 번 연습**해서 실제 환경에서 바로 고득점을 내는 개념을 최초로 정립했습니다.

---

## 2. DreamerV3 (Hafner et al., 2023)
- **원문:** [*Mastering Diverse Domains through World Models* (`arXiv:2301.04104`)](https://arxiv.org/abs/2301.04104)
- **해결한 문제 (왜 중요한가?):** 기존 월드 모델 기반 강화학습은 작업이 바뀔 때마다 하이퍼파라미터를 새로 튜닝해야 했고, 보상이 아주 드물게 주어지는 장기 작업에서는 학습이 무너졌습니다.
- **고등학생도 이해하는 핵심 컨셉:**
  - **RSSM(Recurrent State-Space Model)**이라는 표준 잠재 월드 모델 구조를 완성해, **단 하나의 고정된 설정**으로 로봇 보행부터 아타리 게임, 그리고 아무런 사람 시연 없이 **마인크래프트에서 다이아몬드를 처음부터 캐는 장기 과제**까지 정복했습니다.
  - 픽셀 화면 전체를 다시 그리느라 힘을 빼는 대신, **'행동 결정에 꼭 필요한 핵심 압축 상태(Latent State)'만 머릿속으로 굴리며 15스텝 앞을 상상**해 정책을 학습합니다.

---

## 3. UniSim (Universal Real-World Simulator, 2023)
- **원문:** [*Learning Interactive Real-World Simulators* (`arXiv:2310.06114`)](https://arxiv.org/abs/2310.06114)
- **해결한 문제 (왜 중요한가?):** Isaac Sim이나 MuJoCo 같은 전통 물리 시뮬레이터는 사람이 3D 에셋과 마찰계수를 일일이 만들어 넣어야 해서, 수건 개기·음식 조리처럼 복잡한 일상 환경을 똑같이 만들기 어렵습니다.
- **고등학생도 이해하는 핵심 컨셉:**
  - 로봇 시연 영상, 사람 1인칭 영상, 인터넷 비디오를 모두 모아 **"내가 로봇 팔을 오른쪽으로 5cm 움직이면(Action Input), 다음 카메라 화면(Video Frame)이 어떻게 보일까?"를 비디오 확산 모델(Video Diffusion)로 직접 그려내는 생성형 시뮬레이터**입니다.
  - 이 생성형 시뮬레이터 안에서 로봇 정책(VLA/RL)을 훈련하거나 평가한 뒤 실제 로봇으로 바로 옮기는(Zero-shot transfer) 길을 열었습니다.

---

## 4. World-Action Models & Physical AI (Cosmos / GR00T 계열, 2025~2026)
- **원문:** [*Cosmos World Foundation Model Platform for Physical AI* (`arXiv:2501.03575`)](https://arxiv.org/abs/2501.03575)
- **핵심 컨셉:**
  - **VLA**가 `[현재 화면 + 명령] → [행동]`으로 곧장 직행한다면, **WAM(World-Action Model)**은 **`[현재 화면 + 명령] → [미래 물리 상태/영상 예측] + [그 미래를 만드는 행동]`**을 함께 학습합니다.
  - 로봇이 사람의 1인칭 요리 영상을 볼 때 '로봇 관절 정답값'은 없지만, **"손이 칼을 움직이면 당근이 어떻게 쪼개지는지(세상의 물리 변화)"**는 배울 수 있습니다. 이를 통해 라벨이 없는 수많은 인간 영상에서 물리 상식을 흡수해 적은 로봇 시연만으로도 빠르게 적응합니다.

---

## 추천 학습 순서 요약

| 순서 | 논문 | 핵심 방식 | 한 줄 핵심 질문 |
| :---: | --- | --- | --- |
| **1** | **World Models (2018)** | VAE + MDN-RNN | 왜 픽셀 공간이 아니라 압축된 잠재 공간(Latent Space)에서 미래를 예측하는가? |
| **2** | **DreamerV3 (2023)** | RSSM + Actor-Critic | 상상 속 궤적(Imagined Rollouts)만으로 어떻게 실제 정책을 안정적으로 업데이트하는가? |
| **3** | **UniSim (2023)** | Action-Conditioned Video Diffusion | 전통 3D 물리 엔진 대신 비디오 생성 모델을 어떻게 인터랙티브 시뮬레이터로 쓰는가? |
| **4** | **Cosmos / WAM** | World Foundation Model | 로봇 관절 라벨이 없는 일반 인간 비디오 데이터를 어떻게 로봇 제어 학습에 활용하는가? |
