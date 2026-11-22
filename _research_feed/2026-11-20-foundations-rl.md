---
layout: feed_note
title: "[필수 기초 로드맵 ③] 강화학습(RL) & 로봇 제어: DQN부터 로봇 보행·조작의 표준 PPO·SAC까지 필수 논문 4선"
date: 2026-11-20 08:00:00 +0900
channel: foundations
channel_label: "Foundations · 필수 기초"
tags: ["Humanoid & Locomotion", "Sim & Systems"]
source_url: "https://arxiv.org/abs/1707.06347"
summary: "로봇이 넘어지지 않고 걷거나(Isaac Lab 보행 학습), 스스로 시행착오를 겪으며 정밀 조작을 익히는 심층 강화학습(Deep RL)의 4대 기둥 논문(DQN, DDPG, PPO, SAC)을 수식 부담 없이 핵심 컨셉 중심으로 정리합니다."
---

모방학습(VLA)이 **"선생님(사람)의 시연을 따라 하는 것"**이라면, 강화학습(Reinforcement Learning, RL)은 **"자전거를 처음 배울 때 스스로 넘어져 보면서 균형 잡는 법을 터득하는 것"**입니다. 특히 4족 보행 로봇이나 휴머노이드가 계단을 오르고 외력을 버티는 제어기는 거의 예외 없이 **Isaac Sim / Isaac Lab에서 강화학습(PPO, SAC)**으로 훈련됩니다.

강화학습을 공부할 때 반드시 알아야 할 4편의 기둥 논문을 가장 직관적으로 정리했습니다.

---

## 한눈에 보는 진화 계보

`① DQN (오락실 버튼처럼 딱딱 끊어지는 선택) → ② DDPG (로봇 모터처럼 연속적인 각도·토크 출력) → ③ PPO (가장 안정적인 시뮬레이터 대량 병렬 학습의 표준) → ④ SAC (호기심·엔트로피를 더해 실제 로봇에서도 빠르게 배우는 표준)`

---

## 1. DQN (Deep Q-Network, DeepMind, 2015)
- **원문:** [*Human-level control through deep reinforcement learning* (`Nature 2015` / `arXiv:1312.5602`)](https://arxiv.org/abs/1312.5602)
- **해결한 문제 (왜 중요한가?):** 바둑판이나 작은 미로와 달리, 카메라 화면(픽셀)은 가능한 상태가 무한히 많아서 표(Table)에 점수를 적어둘 수 없었습니다.
- **고등학생도 이해하는 핵심 컨셉:**
  - **"이 화면에서 왼쪽 버튼을 누르면 앞으로 총 몇 점을 받을까(Q-value)?"**를 딥러닝 신경망(CNN)으로 예측하게 만든 최초의 브레이크스루입니다.
  - 신경망이 최근 기억에만 쏠려 고장 나는 것을 막기 위해, 과거 경험을 일기장처럼 모아뒀다가 무작위로 꺼내 복습하는 **경험 리플레이(Experience Replay)**와 정답지를 천천히 업데이트하는 **타깃 네트워크(Target Network)** 두 가지 장치로 학습을 안정시켰습니다.

---

## 2. DDPG (Deep Deterministic Policy Gradient, 2015)
- **원문:** [*Continuous control with deep reinforcement learning* (`arXiv:1509.02971`)](https://arxiv.org/abs/1509.02971)
- **해결한 문제 (왜 중요한가?):** DQN은 '왼쪽/오른쪽/점프'처럼 선택지가 몇 개뿐일 때는 잘 되지만, 로봇 팔 관절처럼 **$-3.14\text{ rad} \sim +3.14\text{ rad}$ 사이의 연속적인 실수 값**을 출력해야 할 때는 가장 점수가 높은 행동을 골라낼 수 없습니다.
- **고등학생도 이해하는 핵심 컨셉:**
  - 역할을 두 명으로 나눕니다(**Actor-Critic** 구조):
    - **배우(Actor):** 현재 상태를 보고 곧바로 연속적인 모터 토크/각도 값을 출력합니다.
    - **평론가(Critic):** 배우가 낸 행동이 몇 점짜리인지 채점하고, *"토크를 조금 더 높이면 점수가 올라가겠어"*라고 기울기(Gradient)로 코칭해 줍니다.

---

## 3. PPO (Proximal Policy Optimization, OpenAI, 2017) — *시뮬레이션 로보틱스 1순위*
- **원문:** [*Proximal Policy Optimization Algorithms* (`arXiv:1707.06347`)](https://arxiv.org/abs/1707.06347)
- **해결한 문제 (왜 중요한가?):** 강화학습에서는 신경망을 한 번에 너무 크게 고치면 로봇이 갑자기 이상한 동작을 하며 넘어지고, 거기서 모은 나쁜 데이터 때문에 신경망이 영영 망가져 버리는 현상(Policy Collapse)이 가장 큰 골칫거리였습니다.
- **고등학생도 이해하는 핵심 컨셉:**
  - **"성적이 좋아지는 방향이라도, 한 번 업데이트할 때 기존 행동 습관에서 $\pm 20\%$($\epsilon=0.2$) 이상은 절대 갑자기 바꾸지 마라!(Clipping)"**라는 안전벨트를 채운 알고리즘입니다.
  - 구조가 단순하고 튜닝이 거의 필요 없어, **NVIDIA Isaac Lab에서 로봇 수천 대를 동시에 띄워놓고 보행·손재주 정책을 학습시킬 때 전 세계 연구자의 90% 이상이 쓰는 절대 표준**입니다.

---

## 4. SAC (Soft Actor-Critic, Berkeley, 2018) — *데이터 효율 & 실물 로봇 RL 1순위*
- **원문:** [*Soft Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with a Stochastic Actor* (`arXiv:1801.01290`)](https://arxiv.org/abs/1801.01290)
- **해결한 문제 (왜 중요한가?):** PPO는 매번 새로 모은 데이터만 쓰고 버리기 때문에(On-Policy) 수천만 번의 시뮬레이션이 필요합니다. 반면 실제 로봇에서 학습하려면 적은 시행착오로도 빠르게 배워야 합니다.
- **고등학생도 이해하는 핵심 컨셉:**
  - 로봇에게 **'점수(Reward)를 많이 받는 것'**과 동시에 **'가능한 한 다양하고 새로운 방법을 시도해 보는 것(최대 엔트로피, Maximum Entropy)'** 두 가지를 함께 칭찬해 줍니다.
  - 덕분에 한 가지 어설픈 동작에 일찍 갇히지 않고 폭넓게 탐색하며, 과거 데이터까지 재활용(Off-Policy)할 수 있어 **적은 데이터로도 강건한 제어 정책을 배우는 대표 알고리즘**입니다.

---

## 언제 PPO를 쓰고, 언제 SAC를 쓸까?

| 알고리즘 | 데이터 재사용 | 최고의 강점 | 로보틱스 실무 추천 상황 |
| --- | --- | --- | --- |
| **PPO** | 불가 (On-Policy) | 압도적인 학습 안정성 & GPU 병렬화 효율 | **Isaac Sim / Isaac Lab**에서 수천 개 로봇을 병렬로 빠르게 돌릴 수 있을 때 |
| **SAC** | 가능 (Off-Policy) | 높은 샘플 효율성 & 다양한 탐색 | 시뮬레이션이 매우 느리거나, **실제 로봇(Real-world)** 데이터를 섞어 미세조정할 때 |
