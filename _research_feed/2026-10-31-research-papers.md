---
layout: feed_note
title: "TAPESTRY: 비디오를 생성하지 않고 84ms에 로봇 행동 chunk를 예측한다"
date: 2026-10-31 07:00:30 +0900
channel: research-papers
channel_label: "Research Papers"
summary: "10월 27일 공개된 TAPESTRY는 사전학습 video diffusion backbone의 VAE patch 경로에 로봇 action을 직접 넣고, 학습에는 비디오·행동을 함께 쓰되 추론에서는 한 번의 DDIM step으로 행동만 출력한다. RTX 5090에서 16-action chunk 84ms, 실물 양팔 작업 28/30 성공을 보고했지만 평가 플랫폼과 diffusion schedule은 제한된다."
---

비디오 생성 모델이 물체의 움직임을 이해한다면, 로봇 제어에도 그 지식을 쓸 수 있다. 문제는 **다음 장면을 실제로 생성한 뒤 행동을 추출하는 방식이 너무 느리다**는 점이다. 2026년 10월 27일 공개된 *TAPESTRY: A Single Backbone for Video Generation and Robot Control*은 학습할 때 비디오 모델의 동역학 표현을 활용하면서, **실행할 때는 비디오를 생성하지 않고 action chunk만 예측**한다.

TAPESTRY는 *Tokenizing Actions as Video Patches in a Shared Transformer Policy*의 약자다. 별도의 대형 action expert를 붙이는 대신, 비디오 생성 모델의 **기존 patch embedding과 Diffusion Transformer(DiT)**를 로봇 행동에도 재사용한다.

## 행동 하나를 비디오 latent의 patch 하나처럼 만든다

사전학습한 **CogVideoX-2B**는 비디오를 VAE latent로 바꾸고, 그 latent를 작은 patch token으로 나누어 처리한다. TAPESTRY는 20차원 로봇 행동 벡터 하나를 **linear projection → affine-free LayerNorm → 기존 video patchifier**에 통과시켜 행동 token 하나로 변환한다.

이때 추가되는 action projection 행렬은 **1,280개 파라미터**다. 이 숫자는 **전체 모델 크기가 아니라 새 행동 입력 경로의 파라미터 수**이며, DiT 자체는 2B 규모로 fine-tuning한다. 행동을 곧바로 DiT hidden dimension에 사상하면 사전학습 latent의 통계와 어긋나 학습이 불안정해지므로, 기존 VAE patch 경로를 거쳐 입력 분포를 맞춘다.

하나의 backbone은 세 가지 학습 목표를 공유한다.

- **Video diffusion:** 사람·로봇 비디오의 미래 장면을 복원해 동역학 표현을 유지한다.
- **Joint video+action diffusion:** 행동 라벨이 있는 로봇 시연에서 비디오와 행동을 함께 학습한다. 비대칭 attention mask는 action이 비디오를 참고하되 비디오가 action에 의존하지 않게 한다.
- **Action-only diffusion:** 현재 관측·언어에서 행동만 복원한다. 실제 배포 때 쓰는 입력 경로와 일치하도록 만드는 핵심 목표다.

추론에서는 마지막 경로만 남긴다. **Zero-terminal-SNR와 v-prediction** 조건에서 순수 노이즈로부터 **DDIM 한 단계**를 수행해 행동을 출력한다. 연구진은 여러 단계로 반복 복원하면 오히려 고주파 action jitter가 늘어나는 현상을 분석했다. 이 결과는 모든 diffusion policy에 통하는 일반 법칙이 아니라 **해당 사전학습 backbone과 noise schedule의 특성**이다.

## 수치: GPU 추론과 로봇 작업을 구분해야 한다

**추론 속도:** RTX 5090 한 장에서 **16-action chunk를 84ms**, GPU 메모리 **9GB**로 생성했다고 보고했다. 같은 GPU의 최적화된 DreamZero는 약 **3.7초/chunk**로 약 **44배** 느렸다. 단, 비교 대상 DreamZero는 **5B 모델**, TAPESTRY는 **2B 모델**이므로 차이 전체를 tokenization 하나의 효과로 돌릴 수 없다. 84ms 역시 카메라·네트워크·로봇 제어를 포함한 end-to-end 지연이 아니다.

**LIBERO learning-from-video:** 행동 라벨은 LIBERO-90에서만 주고, 평가 대상 네 suite는 **비디오만 학습에 사용**하는 별도 프로토콜에서 평균 성공률 **76%**를 보고했다. Cosmos Policy와 DreamZero는 각각 **70%**였다. 이는 평가 suite의 action label을 사용하는 **표준 fully supervised LIBERO 점수와 직접 비교할 수 없다**.

**실물 양팔 YAM(20-DoF):** 공구함에 드라이버 넣기, 오븐 열고 크루아상 놓기, 옥수수 옮기기 등 학습한 세 작업에서 **28/30 성공**이었다. 같은 설정의 from-scratch Diffusion Policy는 **15/30**이었다. 비디오 공동학습을 제거하면 **20/30**, 비디오 생성 목표를 제거하면 **19/30**으로 내려갔다.

**새로운 조건 세 가지:** 물체 시작 위치, 붓기 동작, 처음 보는 물체 조합을 바꾼 실물 시험에서는 TAPESTRY가 **10/15**, DreamZero가 **4/15**를 성공했다. 하지만 **조건별 5회씩**만 시험했으며, 논문에 따르면 DreamZero와의 차이는 **p=0.07로 통계적으로 유의하지 않았다**. 일반적인 OOD 성공률을 확정할 근거는 아니다.

## 실제 Robotics R&D에서 확인할 지점

TAPESTRY의 설계 질문은 “비디오 모델로 미래 영상을 얼마나 잘 만드는가”가 아니라 **비디오 사전학습의 동역학 지식을 행동 token으로 얼마나 직접 전달하는가**다. 유사한 구조를 구현한다면 patchifier 공유 여부, action token 분포, action-only 학습 분기 유무를 각각 ablation해야 한다.

배포 검증에서는 **chunk 생성 시간과 전체 sensing-to-actuation latency를 분리**하고, 제어 주기별 action 연속성, 두 번째 차분 기반 jerk, chunk 경계의 불연속, 재관측 후 replanning 실패를 기록할 필요가 있다. 빠른 모델 출력만으로 접촉 안정성이나 안전한 실행이 보장되지는 않는다.

마지막으로 **한 단계 출력은 조건부 평균에 가까운 결정적 예측**이어서, 여러 행동이 모두 가능한 multimodal task에서는 평균화가 문제가 될 수 있다. 저자들도 rectified-flow backbone에 같은 1-step 원리를 바로 옮기지 못했으며, **20차원 양팔 action space 이외의 embodiment**는 별도로 검증하지 않았다. 이 연구의 강점은 범용성을 입증했다는 주장보다 **비디오 생성 사전학습과 빠른 폐루프 행동 추론을 같은 backbone에서 연결한 구조적 실험**에 있다.

## 부록: 배경지식

### 행동 청크와 폐루프 제어

**행동 청크(action chunk)**는 로봇의 다음 동작 한 개가 아니라 연속된 여러 시점의 행동을 묶어 예측한 결과다. 예를 들어 팔이 물체에 접근하는 16단계의 목표 움직임을 한 번에 만들 수 있다.

**폐루프 제어(closed-loop control)**는 실행 중 센서로 현재 상태를 다시 관찰하고 다음 행동을 조정하는 방식이다. 물체가 예상보다 움직였다면 카메라 관찰을 바탕으로 경로를 다시 정하는 것이 예다.

**이 글에서의 의미:** TAPESTRY는 16개 행동을 한 번에 생성한다. 청크 생성 시간과 센서 관찰부터 실제 구동까지 걸리는 전체 지연은 다르다. 물체 접근 예시는 개념 설명을 위한 가상 상황이다.

### Diffusion 모델과 DDIM

**Diffusion 모델**은 무작위 잡음에서 출발해 여러 단계에 걸쳐 데이터에 가까운 결과를 만드는 생성 모델이다. 영상 대신 로봇의 행동을 생성하도록 학습할 수도 있다.

**DDIM**은 이런 잡음 제거 과정을 실행하는 샘플링 방법 중 하나다. 단계 수를 줄이면 생성 시간이 짧아질 수 있지만 결과의 품질과 다양성이 바뀔 수 있다.

**이 글에서의 의미:** 저자들은 특정 사전학습 모델과 잡음 설정에서 DDIM 한 단계로 행동을 생성했다. 이 결과가 모든 diffusion 정책에서 한 단계가 최선이라는 뜻은 아니다.

### VAE latent와 토큰

**VAE latent**는 원본 영상의 정보를 더 작은 표현으로 압축한 것이다. **토큰(token)**은 모델이 처리하기 좋게 나눈 정보 단위로, 영상의 작은 영역이나 행동 벡터를 각각 토큰으로 바꿀 수 있다.

**이 글에서의 의미:** TAPESTRY는 행동을 기존 비디오 latent의 patch 처리 경로에 맞게 변환한다. 이를 통해 사전학습된 비디오 모델의 입력 구조를 로봇 행동에도 활용한다.

## Sources

- [TAPESTRY 원문 — arXiv:2610.36823 (2026-10-27)](https://arxiv.org/abs/2610.36823)
- [TAPESTRY 전체 논문 HTML — 구조·Table 1–3·추론 시간·제한사항](https://arxiv.org/html/2610.36823v1)
- [TAPESTRY 연구진 프로젝트 — 방법 개요 및 실물 로봇 시연](https://tapestry-wam.github.io/)
