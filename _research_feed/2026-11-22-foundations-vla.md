---
layout: feed_note
title: "[필수 기초 로드맵 ①] VLA & 로봇 매니퓰레이션: 모방학습(ACT·Diffusion)부터 범용 로봇 뇌(RT-2·OpenVLA·π0)까지 필수 논문 5선"
date: 2026-11-22 08:00:00 +0900
channel: foundations
channel_label: "Foundations · 필수 기초"
tags: ["VLA / VLM", "Manipulation"]
source_url: "https://arxiv.org/abs/2410.24164"
summary: "로봇 학습(Robot Learning)과 VLA(Vision-Language-Action)를 처음 공부할 때 반드시 순서대로 읽어야 할 핵심 논문 5편(ACT, Diffusion Policy, RT-2, OpenVLA, π0)의 핵심 컨셉과 진화 흐름을 고등학생도 이해할 수 있게 한눈에 정리합니다."
---

로봇 팔에게 **"책상 위 빨간 머그컵을 집어서 바구니에 넣어줘"**라고 시키려면 어떻게 해야 할까요? 과거에는 카메라로 좌표를 계산하고(Perception), 경로를 풀고(MoveIt 2), 모터를 제어하는 코드를 사람이 일일이 짰습니다. 반면 최근 2~3년 사이 등장한 **로봇 학습(Robot Learning)과 VLA(Vision-Language-Action)**는 **"사람이 시연한 데이터를 보여주고, 눈(Vision)+언어(Language)를 곧바로 손동작(Action)으로 번역하자"**는 패러다임입니다.

이 분야의 최신 논문을 막힘없이 읽으려면 아래 **5편의 징검다리 기초 논문**만 순서대로 이해하면 됩니다.

---

## 한눈에 보는 진화 계보

`① ACT (동작 뭉치 예측) → ② Diffusion Policy (여러 정답 경로 다루기) → ③ RT-2 (거대 VLM에 로봇 손 달기) → ④ OpenVLA (누구나 쓰는 7B 오픈소스 VLA) → ⑤ π0 (언어 뇌 + 연속 유체 제어 결합)`

---

## 1. ACT (Action Chunking with Transformers, 2023)
- **원문:** [*Learning Fine-Grained Bimanual Manipulation with Low-Cost Hardware* (`arXiv:2304.13705`)](https://arxiv.org/abs/2304.13705)
- **해결한 문제 (왜 중요한가?):** 로봇이 0.02초마다 한 스텝씩 다음 관절 각도를 예측하면, 작은 오차가 누적되어 덜덜 떨다가 작업에 실패합니다(Compounding Error).
- **고등학생도 이해하는 핵심 컨셉:**
  - 운전할 때 1cm 앞만 보며 핸들을 꺾으면 차가 비틀거리지만, **"앞으로 1~2초 동안 핸들을 이렇게 돌려야지"** 하고 **동작 뭉치(Action Chunk, 예: 미래 $k=100$ 스텝)**를 통째로 계획하면 훨씬 부드럽습니다.
  - ACT는 CVAE + Transformer 구조를 이용해 1스텝이 아니라 **미래 $k$스텝의 관절 궤적 묶음**을 한 번에 예측하고, 겹치는 구간을 시간 가중 평균(Temporal Ensembling)으로 매끄럽게 이어 붙여 양팔 로봇(ALOHA)으로 케이블 끼우기·배터리 넣기 같은 정밀 작업을 성공시켰습니다.

---

## 2. Diffusion Policy (2023)
- **원문:** [*Diffusion Policy: Visuomotor Policy Learning via Action Diffusion* (`arXiv:2303.04137`)](https://arxiv.org/abs/2303.04137)
- **해결한 문제 (왜 중요한가?):** 눈앞에 장애물이 있을 때 **왼쪽으로 피해도 정답, 오른쪽으로 피해도 정답**입니다(Multimodal Action Distribution). 그런데 일반 신경망(MSE 손실)으로 학습하면 왼쪽과 오른쪽의 평균인 **'정면 충돌'**을 출력해 버립니다.
- **고등학생도 이해하는 핵심 컨셉:**
  - 이미지 생성 AI(Stable Diffusion)가 노이즈에서 선명한 그림을 만들어내듯, **완전한 무작위 노이즈 궤적에서 출발해 여러 번 노이즈를 깎아내며(Denoising) 자연스러운 로봇 궤적 하나를 선택**하게 만듭니다.
  - 덕분에 왼쪽/오른쪽을 어정쩡하게 평균 내지 않고, 상황에 맞는 깔끔한 한쪽 경로를 안정적으로 골라냅니다. 현재 거의 모든 최신 로봇 정책의 기본 행동 생성기(Action Head)로 쓰입니다.

---

## 3. RT-2 (Robotic Transformer 2, Google DeepMind, 2023)
- **원문:** [*RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control* (`arXiv:2307.15818`)](https://arxiv.org/abs/2307.15818)
- **해결한 문제 (왜 중요한가?):** ACT나 Diffusion Policy는 손기술은 좋지만, 학습 때 못 본 물체나 *"피곤한 사람에게 필요한 음료를 집어줘(에너지 드링크)"* 같은 상식 추론은 전혀 못 합니다.
- **고등학생도 이해하는 핵심 컨셉:**
  - 인터넷의 수많은 사진과 글을 공부해 이미 세상의 상식을 다 아는 **거대 시각-언어 모델(VLM)**에게 로봇 팔 이동량($\Delta x, \Delta y, \Delta z \dots$)을 **1번부터 256번까지의 '단어(토큰)'처럼 가르치자!**는 발상입니다.
  - 즉, 영어를 한국어로 번역하듯 `[카메라 사진 + 자연어 명령] → [로봇 이동 숫자 토큰]`으로 번역하게 만들어, 최초로 **VLA(Vision-Language-Action)**라는 이름을 탄생시켰습니다.

---

## 4. OpenVLA (Stanford · Berkeley · Toyota, 2024)
- **원문:** [*OpenVLA: An Open-Source Vision-Language-Action Model* (`arXiv:2406.09246`)](https://arxiv.org/abs/2406.09246)
- **해결한 문제 (왜 중요한가?):** RT-2는 구글 내부의 55B짜리 비공개 거대 모델이라 일반 연구실에서는 돌려볼 수도, 내 로봇에 맞게 미세조정(Fine-tuning)할 수도 없었습니다.
- **고등학생도 이해하는 핵심 컨셉:**
  - 97만 개의 공개 로봇 시연 데이터(Open X-Embodiment)로 학습한 **7B 크기의 완전 오픈소스 VLA**입니다.
  - 특히 두 가지 시각 인코더(**DINOv2**로 물체의 공간·기하 위치 파악 + **SigLIP**으로 물체의 의미·이름 파악)를 나란히 결합하고 **Llama 2 7B**에 연결해, 그래픽카드 1~2장으로도 LoRA 미세조정을 통해 내 연구실 로봇에 바로 얹을 수 있는 표준 베이스라인이 되었습니다.

---

## 5. $\pi_0$ (Pi-Zero, Physical Intelligence, 2024)
- **원문:** [*$\pi_0$: A Vision-Language-Action Flow Model for General Robot Control* (`arXiv:2410.24164`)](https://arxiv.org/abs/2410.24164)
- **해결한 문제 (왜 중요한가?):** RT-2나 OpenVLA처럼 로봇 동작을 256개의 딱딱한 숫자 칸(이산 토큰)으로 쪼개서 뱉으면, 빨래 개기처럼 부드럽고 빠른 고주파(50Hz) 연속 동작이 투박해집니다.
- **고등학생도 이해하는 핵심 컨셉:**
  - **3번(VLM의 똑똑한 상식 뇌)**과 **2번(Diffusion/Flow Matching의 부드러운 연속 손기술)**을 하나로 합친 결정판입니다!
  - 사전학습된 VLM(PaliGemma)을 두뇌로 쓰되, 마지막에 단어를 뱉는 대신 **Flow Matching Action Expert**를 달아 50Hz의 매끄러운 연속 관절 궤적 뭉치를 생성합니다. 현재 최신 VLA 연구들이 가장 많이 따르는 표준 아키텍처입니다.

---

## 추천 학습 순서 요약

| 순서 | 논문 | 핵심 키워드 | 읽을 때 집중할 질문 |
| :---: | --- | --- | --- |
| **1** | **ACT** | Action Chunking, CVAE | 왜 1스텝 대신 $k$스텝 묶음을 예측하면 오차 누적이 줄어드는가? |
| **2** | **Diffusion Policy** | Multimodal Action, Denoising | 왜 여러 정답 경로가 있을 때 일반 회귀(MSE)는 실패하고 Diffusion은 성공하는가? |
| **3** | **RT-2** | Action as Language Tokens | 연속적인 로봇 좌표를 어떻게 VLM의 텍스트 토큰으로 바꿨는가? |
| **4** | **OpenVLA** | DINOv2 + SigLIP, LoRA | 왜 로봇 비전에서는 의미(SigLIP)와 공간 구조(DINOv2)를 둘 다 써야 하는가? |
| **5** | **$\pi_0$** | VLM + Flow Matching | 이산 토큰 방식(RT-2/OpenVLA)의 한계를 어떻게 연속 Flow 전문가 모듈로 해결했는가? |
