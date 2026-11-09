---
layout: feed_note
title: "SLA: 3D 공간 감독을 사전학습에 넣자 실물 조작 성공률이 59.8%→83.8%로 올랐다"
date: 2026-11-10 06:58:10 +0900
channel: research-papers
channel_label: "Research Papers"
summary: "11월 5일 공개된 SLA는 π₀.₅의 시각 특징을 동결된 3D perception teacher와 정렬해 공간 정보를 continual pre-training부터 학습한다. 자체 8개 실물 조건에서 평균 83.8% 대 59.8%를 보고했지만, 조건별 50회 평가와 사후학습 데이터 범위에 유의해야 한다."
---

로봇이 컵을 정확히 집으려면 “컵이 있다”는 의미 이해뿐 아니라 컵이 **3차원 공간에서 어디에 있고 어떻게 움직이는지** 알아야 한다. 2026년 11월 5일 공개된 *SLA: Scaling Spatial-Language-Action Model via Continual Pre-training*은 VLA의 공간 이해를 작업별 fine-tuning에만 맡기지 않고 **continual pre-training 단계부터 3D 특징으로 감독**한다.

## 2D VLM의 시각 특징을 3D teacher에 맞춘다

일반적인 VLA는 이미지·텍스트로 사전학습한 VLM의 시각 표현을 활용한다. 이미지의 물체 종류를 구별하는 데 유리해도 로봇 손끝과 물체의 상대적인 3D 위치·방향을 일관되게 담는다는 보장은 없다. SLA는 기존 **π₀.₅ 정책을 초기화 모델**로 사용하고, 행동 예측 손실과 별개로 **중간 시각 embedding을 동결된 3D perception model의 공간 표현에 정렬하는 보조 손실**을 함께 학습한다.

시각 backbone의 어느 층에 공간 정보가 잘 나타나는지는 장면과 특징에 따라 다르다. 따라서 여러 VLA 층의 embedding을 **feature-dependent gate**로 적응적으로 합쳐 teacher와 비교한다. 학습 데이터에 depth·camera calibration이 일부만 있어도 teacher가 이를 활용하도록 설계했다. 또한 **probabilistic state dropout**으로 상태 입력에 지나치게 의존하는 현상을 줄이고 시각 정보 활용을 유도한다.

핵심은 추론 때 3D teacher를 별도로 실행하지 않는다는 점이다. 공간 정렬용 보조 모듈은 학습에만 쓰고 **기존 VLA 추론 아키텍처를 유지**한다. 다만 이는 계산량이 완전히 같다는 실측 보장이 아니라 아키텍처 수준의 설명이다.

## 이질적인 로봇 데이터에서 공통 공간 표현을 학습한다

논문 Table 1에 열거된 여섯 원천 데이터셋의 **원본 총규모**는 약 **171만 episode, 14,330시간**이다. 이는 선별·전처리 후 실제 학습에 투입된 양과 구분해야 한다. InternData-A1, AgiBotWorld-Beta, RoboCasa365-Pretrain, RoboCOIN, DROID, MolmoAct 등 시뮬레이션과 실물, 서로 다른 로봇의 데이터를 통합한다.

서로 다른 로봇의 관절 수가 달라도 공간적 동작을 비교할 수 있도록 상태는 **end-effector의 절대 pose**, 행동은 **action chunk 내 end-effector pose 변화량**으로 표현한다. 논문은 downstream benchmark 데이터가 사전학습에 섞여 평가를 오염시키지 않도록 제외했다고 설명한다.

## 실제로 어느 조건에서 얼마나 나아졌나

연구진이 제시한 **자체 실물 배치 8개 조건 A–H**의 평균 성공률은 SLA **83.8%**, π₀.₅ **59.8%**, 공간 감독을 post-training에만 넣은 Spatial Forcing **68.0%**다(논문 Table 11). 즉 π₀.₅ 대비 **24.0%p** 개선이다. 각 작업은 50개의 개별 채점 object instance로 평가했다. 작업에는 양손 간 채소 전달, 사람이 던지거나 움직이는 과일 파지, 물병·시계 파지, 학습에서 제외된 검은 테이프 선택 등이 포함된다.

공개 실물 벤치마크 **RoboDojo-Real**에서는 세 로봇 embodiment에 걸친 평균 성공률이 SLA **33.9%**, π₀.₅ **12.8%**였다(논문 Table 5). 자체 실물 배치의 83.8%와 RoboDojo-Real의 33.9%는 **서로 다른 평가 체계**이므로 하나의 일반적인 로봇 성공률로 합쳐 해석할 수 없다. 시뮬레이션 LIBERO-Plus에서는 전체 87.4%, RoboTwin Clean2Random에서는 72.3%를 보고한다.

## 해석과 재현 시 주의할 점

비교 결과는 공간 감독을 사전학습부터 넣는 전략의 가능성을 뒷받침하지만, **데이터 규모·학습 예산·post-training 절차·실물 환경**의 영향을 완전히 제거한 보편적 인과 증명은 아니다. 자체 실물 A–H는 특정 Piper 양팔 및 Franka 단팔 장비와 RealSense 카메라를 사용했다. 논문은 일부 조건에서 100개 시연으로 post-training한 정책을 관련 조건에 재사용한다. 새로운 물체·카메라 배치·제어 주기에서 동일한 24.0%p 향상을 기대해서는 안 된다.

로봇 소프트웨어 관점에서는 **RGB / depth / camera calibration / end-effector pose / action frame**의 정의를 먼저 통일하는 것이 중요하다. 3D teacher와 정책의 특징을 정렬하더라도 실제 추론 단계의 좌표계 변환과 카메라 외부 파라미터가 틀리면 물리 제어는 실패한다. 연구를 재현한다면 동일한 데이터 분할과 평가 seed에서 **공간 정렬 없음 → post-training만 정렬 → 두 단계 모두 정렬**의 ablation을 우선 비교할 만하다.

## 부록: 배경지식

### Continual pre-training(연속 사전학습)

- **정의:** 이미 사전학습된 모델을 새로운 대규모 데이터와 학습 목표로 더 학습하는 단계다.
- **예시(설명용, 논문 실험 아님):** 이미지·언어를 이해하는 모델에 여러 로봇의 파지 시연을 추가로 학습시킨다.
- **이 글에서의 의미:** SLA는 공간 정렬을 특정 작업 fine-tuning 전에 광범위한 로봇 데이터로 학습한다.

### Spatial feature alignment(공간 특징 정렬)

- **정의:** 모델 내부 특징이 3D 위치·형상·방향 정보를 담는 기준 특징과 대응되도록 학습하는 것이다.
- **예시(설명용):** RGB로 본 컵의 특징이 깊이 센서로 추정한 컵의 공간 배치와 일관되도록 맞춘다.
- **이 글에서의 의미:** 동결된 3D teacher가 VLA의 중간 시각 embedding을 감독한다.

### End-effector pose(말단장치 자세)

- **정의:** 로봇 팔 끝의 위치와 방향을 특정 좌표계에서 나타낸 값이다.
- **예시(설명용):** 그리퍼가 로봇 기준 x=0.3 m 위치에 있고 아래를 향한다고 기술한다.
- **이 글에서의 의미:** 서로 다른 관절 구조를 가진 로봇 데이터를 공통 행동 표현으로 통합하는 기준이다.

### State dropout(상태 입력 드롭아웃)

- **정의:** 학습 중 일부 로봇 상태 정보를 확률적으로 가려 다른 관측 신호에 의존하도록 유도하는 방법이다.
- **예시(설명용):** 관절 상태의 일부를 가려도 카메라로 물체와 손의 상대 위치를 추정하도록 훈련한다.
- **이 글에서의 의미:** 시연 궤적의 상태 정보만 암기하지 않고 시각 단서에 주의를 기울이도록 유도한다.

## Sources

- [Li et al., *SLA: Scaling Spatial-Language-Action Model via Continual Pre-training* — arXiv:2611.08373 (2026-11-05)](https://arxiv.org/abs/2611.08373)
- [논문 전체 HTML — 학습 구조, 데이터 Table 1, RoboDojo Table 5, 실물 Table 11 및 한계](https://arxiv.org/html/2611.08373v1)
