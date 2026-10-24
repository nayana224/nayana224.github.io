---
layout: feed_note
title: "KINO-2는 로봇 추론 속도뿐 아니라 action 실행 경로를 줄였다"
date: 2026-10-24 09:04:52 +0900
channel: ai-robotics
channel_label: "AI & Robotics"
summary: "Bear Robotics가 10월 21일 공개한 KINO-2는 KR1의 시연 기반 조작 정책을 Isaac OS·Holoscan·TensorRT와 기존 로봇 제어 스택에 연결한다. 사내 모델 추론 72.3→17.2ms와 명령 jerk 약 7배 감소를 보고했지만, 이는 자체 장비의 엔지니어링 측정이다."
---

로봇 조작 모델이 더 정확해져도, 카메라 영상이 늦게 들어오거나 action chunk를 실행하는 동안 다시 관측하지 못하면 접촉 상황에 반응하기 어렵다. **Bear Robotics는 10월 21일 KINO-2를 공개하며**, KR1 휴머노이드의 시연 기반 학습부터 온보드 추론·제어·현장 작업까지 연결한 구현과 측정 결과를 설명했다.

KINO-2는 한 가지 VLA 모델의 이름이 아니다. 작업 시연을 수집하고 정책을 학습·평가하며, 자체 조작 모델이나 NVIDIA Isaac GR00T 같은 외부 파운데이션 모델을 공통 로봇 인터페이스에 연결하는 **학습·배포 플랫폼**이다. 회사는 창고의 병 포장과 운반, 매장 반품 처리 등을 고객 PoC로 진행 중이라고 밝혔다.

## 예측은 길게, 실행은 짧게

공개 기술 문서의 자체 모델 예시에서는 카메라 영상, 팔·그리퍼 상태, 작업 조건을 입력으로 사용한다. Action expert는 **10Hz 기준 40개 action step**, 즉 4초 분량을 예측하지만, KR1은 그중 **0.1초짜리 한 step만 실행**하고 새 관측으로 다시 계획한다.

이 구조는 긴 action horizon과 짧은 실행 horizon을 구분한다. 물체가 밀리거나 파지 위치가 달라졌을 때 다음 예측에 그 변화를 반영할 여지를 남긴다. 다만 문서가 제시한 40-step 설정은 회사의 자체 모델 예시이며, 모든 KINO-2 정책에 공통으로 적용되는 제어 규칙은 아니다.

## GPU 추론과 로봇 명령 경로를 따로 최적화

KR1의 Jetson AGX Thor에서는 Isaac OS의 Holoscan SDK 5.0 파이프라인이 카메라 입력·관측 전처리·모델 추론을 연결한다. 회사는 영상이 전처리부터 추론까지 GPU 메모리에 머무르도록 구성하고, NVIDIA Isaac Bridge로 기존 이동·SLAM·작업 관리 스택과 연결했다고 설명한다.

**자체 모델 추론 시간은 72.3ms에서 17.2ms로 감소(4.2배)**했다. 이는 회사가 PyTorch eager 실행과 가속 파이프라인을 비교한 결과다. 별도의 GR00T 1.7 최적화에서는 4개 TensorRT 엔진을 쓰던 이전 구성의 92.2ms 대비, 8개 엔진과 선택적 FP8 양자화를 사용한 구성에서 **action chunk당 GPU 실행 시간 중앙값 56.6ms**를 보고했다. 두 수치는 서로 다른 모델·기준선의 비교이므로 하나의 가속률로 합칠 수 없다.

추론 이외의 실행 경로도 바꿨다. 카메라 노출 시점과 action sequence를 정렬하고, chunk 실행 시작 지연을 줄인 결과 하드웨어 시험 장치에서 **명령 jerk가 237에서 33m/s³로 약 7배 감소**했다고 한다. Jerk는 명령 가속도의 시간 변화율이며, 이 수치만으로 실제 접촉력이나 작업 성공률이 개선됐다고 단정할 수는 없다.

## 모델 성능보다 먼저 분리해서 측정할 것

회사는 Isaac Lab에서 **1,024개 KR1 시뮬레이션 인스턴스**를 병렬로 학습했고, 한 시뮬레이션 pick task의 소요 시간이 7.4초에서 3.7초로 줄었다고 보고했다. 이 실험은 시뮬레이터 상태를 입력으로 사용했으므로 실제 카메라·접촉·지연 조건에서 같은 성능을 입증한 것은 아니다.

KINO-2의 실용적 교훈은 **정책 추론 시간, 카메라부터 관절 동작까지의 반응 시간, 명령 연속성, 실제 task 성공률을 서로 다른 지표로 관리해야 한다**는 점이다. 공개된 수치는 제공사 자체 장비와 설정에 대한 엔지니어링 측정이다. 고객 PoC가 진행 중이라는 사실과 독립적으로 검증된 장기 현장 성공률은 구분해야 한다.

## Sources
- [Bear Robotics — KINO-2 기술 문서: 학습 구조·추론·제어 측정](https://www.bearrobotics.ai/blog/kino-2-production-ai-for-real-world-manipulation)
- [Bear Robotics — KINO-2 공식 발표: Isaac OS 통합과 고객 PoC](https://fl.bearrobotics.ai/blog/bear-robotics-launches-kino-2)
- [NVIDIA — 2026년 10월 21일 Isaac 플랫폼 발표](https://nvidianews.nvidia.com/news/nvidia-advances-isaac-platform-for-general-purpose-robotics-with-new-reference-humanoid-frameworks-simulation-pipelines-and-data)
